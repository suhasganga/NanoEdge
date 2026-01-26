On this page

Enterprise—

OpenID Connect (OIDC) enables SSO authentication with external Identity Providers.

[Learn more](https://questdb.com/enterprise/)

OpenID Connect (OIDC) integrates with Identity Providers (IdP) external to
QuestDB.

It is a convenient way to integrate QuestDB into your enterprise environment,
and it provides SSO (Single Sign-On) for the [Web Console](/docs/getting-started/web-console/overview/).

Microsoft Active Directory and Azure AD, for example, can be turned into an
Identity Provider.

Specific installation steps depend on the type of the provider.

## Architecture overview[​](#architecture-overview "Direct link to Architecture overview")

Altogether, the architecture appears as such:

![Overall architecture](/docs/images/docs/guide/oidc/oidc-architecture.webp)

Architecture diagram

We can break it down into core components.

### Web Console[​](#web-console "Direct link to Web Console")

QuestDB's interactive UI. Users must authenticate before accessing the database
via the interface.

The [Web Console](/docs/getting-started/web-console/overview/) uses PKCE (Proof Key for Code Exchange) to
secure the authentication and authorization flow.

In OAuth2/OIDC terms, the [Web Console](/docs/getting-started/web-console/overview/) is referred to as
the *client*, and it is assigned an identifier: the **Client Id**.

Each application which integrates via OIDC should be given a different **Client
Id**.

### OIDC Provider[​](#oidc-provider "Direct link to OIDC Provider")

Typically consists of a number of modules.

We are interested in two of them only.

1. The *Identity Provider* holds user identities and user information, capable
   of authenticating users, and to issue an ID Token which uniquely identify
   them.
2. The *Authorization Server* grants access to resources, such as a database, in
   the form of access tokens.

The OIDC Provider usually integrates with a number of applications which require
different access to a number of resources.

These clients communicate with the OIDC Provider via its endpoints.

It exposes a number of APIs, including the Authorization, Token and User Info
endpoints.

### QuestDB[​](#questdb "Direct link to QuestDB")

The database, in OAuth2/OIDC terms the *protected resource* or *resource
server*.

Only processes requests which contain a valid access token.

## Authentication and Authorization Flow[​](#authentication-and-authorization-flow "Direct link to Authentication and Authorization Flow")

The OAuth2/OIDC standard defines different ways of obtaining access and ID
tokens from the OIDC Provider, referred to as the "*flow*".

The goal of this flow is to get the user, who is sitting in front of the Web
Console, authenticated.

Then, it allows QuestDB to determine the user's permissions based on user
information provided by the Identity Providers.

Specifically, the QuestDB [Web Console](/docs/getting-started/web-console/overview/) uses the
`Authorization Code Flow with PKCE` option.

It consists of ten steps...

### 1. Secret generation[​](#1-secret-generation "Direct link to 1. Secret generation")

First the [Web Console](/docs/getting-started/web-console/overview/) generates a cryptographically strong
random secret called the *code verifier*.

The secret is hashed using the *SHA256 algorithm*. The result is the *code
challenge*.

After PKCE initialization the [Web Console](/docs/getting-started/web-console/overview/) requests an
*authorization code* from the OIDC Provider.

It calls the Authorization endpoint with a few parameters, including the:

* **Client Id**
* requested scopes (the list of scopes are configurable, default is `openid`
  only)
* code challenge
* algorithm used to generate the code challenge from the code verifier (SHA256)

When the Authorization Server receives the request, it checks if the user has
been authenticated already:

* If the user has a valid session, it can be provided with an authorization code
  straight away, so we jump to step 4.
* If the user does not have a valid session yet, it will be redirected to the
  Identity Provider for authentication.

Authorization code request example

```prism-code
https://oidc.provider:443/as/authorization.oauth2?client_id=questdb&response_type=code&scope=openid&redirect_uri=https%3A%2F%2Fquestdb.host%3A9000&code_challenge=IwZ-WuypAY3fMtvismbj1MQUe5CzMgrBa87nYcgFoLQ&code_challenge_method=S256
```

### 2. Prove identity[​](#2-prove-identity "Direct link to 2. Prove identity")

Next, the user must prove its identity.

This could be a username with:

* a password,
* an OTP
* facial recognition via a mobile app
* or anything else supported by the Identity Provider.

![Creating profiles](/docs/images/docs/guide/oidc/oidc-setup-1.webp)

Prove identity

### 3. Scope consent[​](#3-scope-consent "Direct link to 3. Scope consent")

After successful authentication, the user provides consent for the requested
scopes.

The list of scopes are configurable.

By default the Web Console requests only the `openid` scope which is mandatory
for OIDC.

No ID Token is issued without it.

The OIDC provider can be configured to provide the consent automatically,
without presenting the user with an additional screen in the browser.

![Openid and profile](/docs/images/docs/guide/oidc/oidc-setup-2.webp)

Scope consent

### 4. Redirection[​](#4-redirection "Direct link to 4. Redirection")

Consent is granted!

The Authorization Server redirects the user back to the
[Web Console](/docs/getting-started/web-console/overview/) with the *authorization code*:

Authorization code response example

```prism-code
https://questdb.host:9000/?code=1L344XEY5XRka1j4ySNa8bVQSLf71as9uGLEuv_A
```

### 5. Credential request[​](#5-credential-request "Direct link to 5. Credential request")

Now, the QuestDB [Web Console](/docs/getting-started/web-console/overview/) requests the ID and access
tokens from the Token endpoint of the OIDC Provider with the authorization code.

It includes the Client ID and the PKCE code verifier together with the
authorization code in the request.

The endpoint then hashes the code verifier using the method specified previously
in step 1.

The result must match the code challenge, also provided in step 1.

The matching code challenge proves that the token is requested by the client
which requested the authorization code, and it was not stolen:

Token request example

```prism-code
POST https://oidc.provider:443/as/token.oauth2 HTTP/1.1  
Content-Type: application/x-www-form-urlencoded  
grant_type=authorization_code&code=1L344XEY5XRka1j4ySNa8bVQSLf71as9uGLEuv_A&client_id=questdb&&redirect_uri=https%3A%2F%2Fquestdb.host%3A9000&code_verifier=uGZh4sQffXLgRna7D-jtEAkuXzp7Lm_okZXBljzP38coAD44kEheIaz7Pdh98KxYtYLZHNiQPCczQYeF
```

### 6. Credentials received[​](#6-credentials-received "Direct link to 6. Credentials received")

If the PKCE check is passed, the Web Console receives the ID and access tokens.

There is a third token in the response too, the refresh token.

The refresh token is used by the Web Console to refresh the access token before
it expires.

Without the refresh token mechanism, the user would be forced to re-authenticate
when the access token expires.

The validity of the tokens are configurable inside the OIDC Provider.

Token response example

```prism-code
{  
  "access_token": "gslpJtzmmi6RwaPSx0dYGD4tEkom",  
  "refresh_token": "FUuAAqMp6LSTKmkUd5uZuodhiE4Kr6M7Eyv.eg83ge",  
  "id_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6I...",  
  "token_type": "Bearer",  
  "expires_in": 300 // In seconds, thus 5 minutes  
}
```

### 7. Database access[​](#7-database-access "Direct link to 7. Database access")

With the tokens, the Web Console can interact with the database.

The access token is in the header of every request sent to QuestDB.

> **Worried about exposing the token?** It is rather opaque and does not contain
> user details.

To carry out permission checks, the database has to know more about the user.

For this, QuestDB has a User Info Cache.

If it finds a valid entry with the access token in the cache, steps 8 and 9 are
skipped:

Query request example

```prism-code
https://questdb.host:9999/exec?query=select%20current_user()  
Authorization: Bearer gslpJtzmmi6RwaPSx0dYGD4tEkom
```

### 8. Find user information[​](#8-find-user-information "Direct link to 8. Find user information")

No user information in the cache, or stale information?

QuestDB uses the access token to request user information from the OIDC
Provider's User Info endpoint.

This call also serves as token validation.

If the token is not real or has been expired, the User Info endpoint replies
with an error:

User info request example

```prism-code
https://oidc.provider:443/idp/userinfo.openid  
Authorization: Bearer gslpJtzmmi6RwaPSx0dYGD4tEkom
```

### 9. Receive user information[​](#9-receive-user-information "Direct link to 9. Receive user information")

If the access token is valid, QuestDB receives the required user information
from the endpoint, then updates its cache.

The cache improves performance, as QuestDB does not have to turn to the OIDC
Provider on every single request.

Do note that cache expiry is configurable:

User info response example with Active Directory groups

```prism-code
{  
  "sub": "externalUser",  
  "name": "External User",  
  "groups": [  
    "CN=TestGroup1,OU=DC Users,DC=ad,DC=quest,DC=dev",  
    "CN=TestGroup2,OU=DC Users,DC=ad,DC=quest,DC=dev"  
  ]  
}
```

### 10. Permission check[​](#10-permission-check "Direct link to 10. Permission check")

With the help of the user information, QuestDB can carry out
[permission checks](#user-permissions).

If the permission check is successful, the database will process the request,
and then sends the results back:

Query response example

```prism-code
{  
  "query": "select current_user()",  
  "columns": [  
    {  
      "name": "current_user",  
      "type": "STRING"  
    }  
  ],  
  "dataset": [["External User"]],  
  "count": 1,  
  "timestamp": -1  
}
```

## Interactive clients[​](#interactive-clients "Direct link to Interactive clients")

Any interactive client - a UI, Jupyter notebook, CLI - can integrate with an
OIDC provider. However, the level of support will vary between these tools.

Interactive clients usually fall into one of the following categories:

* Browser-based clients with support for HTTP redirects; this includes the Web
  Console or any javascript UI
* Applications running in a browser without support for redirects, such as
  Jupyter notebooks
* Non-browser based clients, usually some kind of command line interface (CLI)
  or a standalone application, such as Microsoft Access

### Browser-based clients[​](#browser-based-clients "Direct link to Browser-based clients")

If the tool is browser based and can handle HTTP redirects, it can implement two
possible flows to request an access token.:

1. [Authorization Code](https://openid.net/specs/openid-connect-core-1_0.html#CodeFlowAuth)
   flow **(Recommended, more secure)**
2. [Implicit](https://openid.net/specs/openid-connect-core-1_0.html#ImplicitFlowAuth)
   flow

The Web Console implements the
[Authorization Code Flow with PKCE](https://oauth.net/2/pkce), which is a
special version of the Authorization Code flow designed for mobile apps and
single page applications.

Regardless of which flow is used by the web or mobile application, the requested
access token can be used for authentication and authorization when communicating
with QuestDB as explained in the [above 7th step](#7-database-access).

### Jupyter notebook[​](#jupyter-notebook "Direct link to Jupyter notebook")

JupyterHub can integrate with OAuth2 providers using OAuthenticator, as
described in its
[documentation](https://jupyterhub.readthedocs.io/en/stable/explanation/oauth.html).
The OAuthenticator documentation also contains
[examples](https://oauthenticator.readthedocs.io/en/latest/tutorials/provider-specific-setup/index.html)
using different identity providers.

If Jupyter notebooks are used without JupyterHub, one option for OAuth2
integration is to use the [Resource Owner Password Credentials (ROPC)](https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.3)  flow.
It is likely that enabling this flow in your OAuth2 provider will require
additional setup.

caution

The Resource Owner Password Credentials flow is legacy, and should be used as a last resort.

We can use the code below to acquire an access token in our notebook:

```prism-code
from urllib import request, parse  
import json  
  
url = "https://oidc.provider:443/as/token.oauth2"  
data = parse.urlencode( {  
    "grant_type": "password",  
    "username": "testuser",  
    "password": "testpwd",  
    "scope": "openid",  
    "client_id": "testclient"  
} ).encode()  
req = request.Request(url=url, data=data)  
req.add_header("Content-Type", "application/x-www-form-urlencoded")  
with request.urlopen(req) as f:  
    body = f.read().decode(f.headers.get_content_charset())  
    resp = json.loads(body)  
    access_token = resp["access_token"]
```

This token can be used to authenticate with QuestDB:

```prism-code
query = parse.urlencode({  
    "query": "select current_user()"  
})  
req = request.Request(f"http://localhost:9000/exec?{query}")  
req.add_header("Authorization", f"Bearer {access_token}")  
with request.urlopen(req) as f:  
    body = f.read().decode(f.headers.get_content_charset())  
    resp = json.loads(body)  
    print(resp)
```

#### Externalizing credentials[​](#externalizing-credentials "Direct link to Externalizing credentials")

The above example saves the user's credentials into the notebook, potentially
exposing them to others. One way to improve this is to use environment variables
or files to externalize the username and password.

Here is an example using the `dotenv` library.

First we need to create a file named `.env` with the settings:

```prism-code
username=testuser  
password=testpwd
```

Then load it in our notebook, and use it to request tokens:

```prism-code
from dotenv import load_dotenv  
import os  
from urllib import request, parse  
import json  
  
load_dotenv()  
user = os.environ.get("username")  
pwd = os.environ.get("password")  
  
url = "https://oidc.provider:443/as/token.oauth2"  
data = parse.urlencode( {  
    "grant_type": "password",  
    "username": user,  
    "password": pwd,  
    "scope": "openid",  
    "client_id": "testclient"  
} ).encode()  
req = request.Request(url=url, data=data)  
req.add_header("Content-Type", "application/x-www-form-urlencoded")  
with request.urlopen(req) as f:  
    body = f.read().decode(f.headers.get_content_charset())  
    resp = json.loads(body)  
    access_token = resp["access_token"]
```

#### Enable ROPC[​](#enable-ropc "Direct link to Enable ROPC")

The Resource Owner Password Credentials flow can be enabled in QuestDB within
`server.conf`:

```prism-code
acl.oidc.ropc.flow.enabled = true
```

> Note that the flow also has to be configured in the OAuth2/OIDC provider!

Now we can use Basic Authentication to simplify our code. We send the
credentials to QuestDB, and the database will validate the credentials against
the OAuth2 provider.

```prism-code
from dotenv import load_dotenv  
import os  
from urllib import request  
import base64  
  
load_dotenv()  
user = os.environ.get("username")  
pwd = os.environ.get("password")  
  
query = parse.urlencode({  
    "query": "select current_user()"  
})  
req = request.Request(f"http://localhost:9000/exec?{query}")  
b64credentials = base64.standard_b64encode(f"{user}:{pwd}".encode()).decode()  
req.add_header("Authorization", f"Basic {b64credentials}")  
with request.urlopen(req) as f:  
    body = f.read().decode(f.headers.get_content_charset())  
    resp = json.loads(body)  
    print(resp)
```

We can also use a postgres client to connect to the database:

note

QuestDB never persists the user's credentials.

```prism-code
import psycopg as pg  
from dotenv import load_dotenv  
import os  
  
load_dotenv()  
user = os.environ.get("username")  
pwd = os.environ.get("password")  
  
conn_str = f"user={user} password={pwd} host=localhost port=8812 dbname=qdb"  
with pg.connect(conn_str, autocommit=True) as connection:  
    with connection.cursor() as cur:  
        cur.execute("select current_user()")  
        records = cur.fetchall()  
        for row in records:  
            print(row)
```

### CLI, standalone applications[​](#cli-standalone-applications "Direct link to CLI, standalone applications")

When using CLI tools, such as `psql`, or standalone applications like Microsoft
Access, the best option may be the Resource Owner Password Credentials flow.

The user logs in with their SSO credentials, and the server validates the
details with the OAuth2 provider:

```prism-code
% psql -h localhost -p 8812 -U testuser  
Password for user testuser:  
psql (14.2, server 11.3)  
Type "help" for help.  
  
testldap=>  
testldap=>
```

## Non-interactive clients[​](#non-interactive-clients "Direct link to Non-interactive clients")

Non-interactive clients are usually jobs or standalone applications, such as a
client for ingesting data. It is practical to manage their credentials via an
OAuth2 provider too.

As seen in the Jupyter notebook examples, the clients can request a token
themselves and then use it to authorise data ingestion:

```prism-code
import json  
import os  
import requests  
import pandas as pd  
from dotenv import load_dotenv  
from questdb.ingress import Sender  
  
load_dotenv()  
user = os.environ.get("username")  
pwd = os.environ.get("password")  
  
token_endpoint = "https://oidc.provider:443/as/token.oauth2"  
response = requests.post(token_endpoint,  
                         data={"grant_type": "password",  
                               "client_id": "testclient",  
                               "username": user,  
                               "password": pwd,  
                               "scope": "openid"},  
                         headers={"Content-Type": "application/x-www-form-urlencoded"})  
  
response_body = response.content.decode("utf-8")  
tokens = json.loads(response_body)  
access_token = tokens["access_token"]  
  
conf = f"http::addr=localhost:9000;token={access_token};"  
with Sender.from_conf(conf) as sender:  
    df = pd.read_csv("data.csv")  
    df["ts"] = pd.to_datetime(df["ts"])  
    sender.dataframe(df, table_name="foo", at="ts")
```

Alternatively, a user may rely on QuestDB to authenticate them via the OAuth2
provider when the Resource Owner Password Credentials flow is enabled on the
server side:

```prism-code
import os  
import pandas as pd  
from dotenv import load_dotenv  
from questdb.ingress import Sender  
  
load_dotenv()  
user = os.environ.get("username")  
pwd = os.environ.get("password")  
  
conf = f"http::addr=localhost:9000;username={user};password={pwd};"  
with Sender.from_conf(conf) as sender:  
    df = pd.read_csv("data.csv")  
    df["ts"] = pd.to_datetime(df["ts"])  
    sender.dataframe(df, table_name="foo", at="ts")
```

## OIDC for the PGWire endpoint[​](#oidc-for-the-pgwire-endpoint "Direct link to OIDC for the PGWire endpoint")

If the [Resource Owner Password Credentials (ROPC)](https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.3)  flow is not an option, we can still authenticate via OIDC on the PGWire endpoint.
However, in this case the client's responsibility to source the token required for authentication.
This method works wherever a Postgres client library is available, including jupyter notebooks.

Token authentication for the PGWire endpoint should be enabled by adding the `acl.oidc.pg.token.as.password.enabled=true` setting to the server configuration.

The token should be sent in the password field, while the username field should contain the string `_sso`, or left empty if that is an option:

```prism-code
import psycopg as pg  
  
token = "token_requested_from_the_oauth2_provider"  
  
conn_str = f"user=_sso password={token} host=localhost port=8812 dbname=qdb"  
with pg.connect(conn_str, autocommit=True) as connection:  
    with connection.cursor() as cur:  
        cur.execute('select current_user()')  
        records = cur.fetchall()  
        for row in records:  
            print(row)
```

## User permissions[​](#user-permissions "Direct link to User permissions")

QuestDB requires additional user information to be able to construct the user's
access list.

As a reminder, the access list is the list of permissions that determines what
the user can and cannot do.

QuestDB itself does not store external users, nor their passwords or any other
authentication related detail.

External users and their authentication methods are managed by the Identity
Provider.

Since external users are not managed by QuestDB, permissions cannot be granted
to them directly.

Instead, the database expects a list of groups, called the *groups claim* to be
present in the user information.

These external group names are mapped to QuestDB's own groups.

The access list of the external user consists of the permissions granted to
those groups:

![OpenID setup](/docs/images/docs/guide/oidc/oidc-setup-3.webp)

User permissions

### Mapping user permissions[​](#mapping-user-permissions "Direct link to Mapping user permissions")

The mappings between external and QuestDB groups are managed with the following
SQL commands:

Create a group which is mapped to an Active Directory group

```prism-code
CREATE GROUP groupName WITH EXTERNAL ALIAS 'CN=TestGroup1,OU=DC Users,DC=ad,DC=quest,DC=dev';
```

Map an Active Directory group to an already existing QuestDB group

```prism-code
ALTER GROUP groupName WITH EXTERNAL ALIAS 'CN=TestGroup1,OU=DC Users,DC=ad,DC=quest,DC=dev';
```

Remove an Active Directory mapping without deleting the QuestDB group

```prism-code
ALTER GROUP groupName DROP EXTERNAL ALIAS 'CN=TestGroup1,OU=DC Users,DC=ad,DC=quest,DC=dev';
```

QuestDB works the list of external groups out from the User Info response
message.

If we take the example used earlier, we will see that the message contains a
claim called `groups`. This name is configurable in QuestDB.

If the groups claim is missing or it is an empty list, the user cannot access
the database.

Although the user is authenticated, they have no permissions at all.

The user has to have at least the `HTTP` permission to be able to successfully
login via the [Web Console](/docs/getting-started/web-console/overview/).

User info response example with Active Directory groups

```prism-code
{  
  "sub": "externalUser",  
  "name": "External User",  
  "groups": [  
    "CN=TestGroup1,OU=DC Users,DC=ad,DC=quest,DC=dev",  
    "CN=TestGroup2,OU=DC Users,DC=ad,DC=quest,DC=dev"  
  ]  
}
```

Any change made to the user's group membership in the Identity Provider, QuestDB
will adjust the user's access list.

note

There may be a slight delay due to the User Info Cache.

QuestDB will use the cached information until it becomes stale, and gets
updated.

The same stands for changes made to the user's status within the Identity
Provider.

For example, a disabled user will not be kicked out of QuestDB immediately.

The `acl.oidc.cache.ttl` config option drives how often user information should
be synchronized with the Identity Providers.

It should be set accordingly to your organization's policies.

Other parts of the user information, such as the `sub` and the `name` also used
by QuestDB.

They could be displayed in the [Web Console](/docs/getting-started/web-console/overview/), or appear in
the logs, for example.

## Configuration options[​](#configuration-options "Direct link to Configuration options")

For all OIDC-related configuration options of QuestDB, see
[Configuration](/docs/configuration/overview/#openid-connect-oidc).

  

## Active Directory[​](#active-directory "Direct link to Active Directory")

The following sections are guides for setting up single sign-on (SSO) with various OAuth2 providers.

### PingFederate[​](#pingfederate "Direct link to PingFederate")

This document helps set up SSO authentication for the Web Console in
[PingFederate](https://www.pingidentity.com/en/platform/capabilities/authentication-authority/pingfederate.html).

It is assumed that the Azure Active Directory serves as the Identity Provider
(IdP).

#### Set up PingFederate client[​](#set-up-pingfederate-client "Direct link to Set up PingFederate client")

First thing first, let's pick a name for the client!

![PingFederate image, naming the client.](/docs/images/guides/active-directory/1.webp)

Picking a name

The QuestDB [Web Console](/docs/getting-started/web-console/overview/) is a SPA (Single Page App).

As a result, it cannot store safely a client secret.

Instead it can use PKCE (Proof Key for Code Exchange) to secure the flow.

As shown above, leave the client authentication disabled.

We also have to white list the URL of the [Web Console](/docs/getting-started/web-console/overview/) as a redirection URL:

![PingFederate image, redirection URL](/docs/images/guides/active-directory/2.webp)

Whitelist the redirection URL

We can instruct PingFederate to automatically authorize the scopes requested by
the [Web Console](/docs/getting-started/web-console/overview/).

The user will not be presented the extra window asking for consent after
authentication:

![PingFederate, bypass approval](/docs/images/guides/active-directory/3.webp)

Bypass, please

The [Web Console](/docs/getting-started/web-console/overview/) uses the
[Authorization Code Flow](/docs/security/oidc/#authentication-and-authorization-flow),
and refreshes tokens automatically.

Next, enable the grant types required for this flow:

![PingFederate, granting types](/docs/images/guides/active-directory/4.webp)

Granted

We've selected:

* Authorization Code
* Refresh Token
* Access Token Validation (Client is a Resource Server)

After that, select the token manager for the client.

The token manager is responsible for issuing access tokens.

All token related settings should be configured in the token manager.

![](/docs/images/guides/active-directory/5.webp)

PKCE enabled

Finally, enable PKCE - as shown above - and save the settings.

#### Access Token Manager settings[​](#access-token-manager-settings "Direct link to Access Token Manager settings")

QuestDB does not require any special setup regarding the access token.

We recommend that you do not to use shorter tokens than the default 28
characters.

As the QuestDB [Web Console](/docs/getting-started/web-console/overview/) refreshes the token automatically, there is no need
for long-lived tokens:

![PingFederate, access token management UI](/docs/images/guides/active-directory/6.webp)

Click to zoom

We've selected:

* Token length: 28
* Token lifetime: 5
* Lifetime extension policy: None
* Maximum token lifetime: Null
* Lifetime extension threshold percentage: 30

For the next step, we tune the Authorization Server.

#### Authorization Server settings[​](#authorization-server-settings "Direct link to Authorization Server settings")

These settings relate to the authorization code, refresh token and CORS.

![PingFederate, auth server image](/docs/images/guides/active-directory/7.webp)

Authorization server

In this section, we've entered:

* Authorization code timeout: 60
* Authorization code entropy: 30
* Client secret retention period: 0

Next, ensure the `ROLL REFRESH TOKEN VALUES` option is selected:

![PingFederate, auth server settings ui](/docs/images/guides/active-directory/8.webp)

Click to zoom

It is also important to whitelist the [Web Console](/docs/getting-started/web-console/overview/)'s URL on the CORS list:

![PingFederate, authorization server ui](/docs/images/guides/active-directory/9.webp)

Port 9000, or your custom port

#### Set up a Microsoft Entra ID Data Source[​](#set-up-a-microsoft-entra-id-data-source "Direct link to Set up a Microsoft Entra ID Data Source")

PingFederate needs a Data Source setup.

This is a secure LDAP connection to Microsoft Entra ID, formerly known as Azure
Active Directory.

The data source needs a:

* name
* hostname
* port
* username and password for the LDAP connection

![PingFederate, data and credential storage](/docs/images/guides/active-directory/10.webp)

Configuring our data source

We have given it the name EntraDS and it will be applied later.

#### Set up a Password Credential Validator[​](#set-up-a-password-credential-validator "Direct link to Set up a Password Credential Validator")

Now that PingFederate has an LDAP connection, we can use it for authentication.

First, create a Password Credential Validator:

![PingFederate, create a PCV view ](/docs/images/guides/active-directory/11.webp)

Create the PCV

We've entered:

* Instance name: EntraPCV
* Instance ID: EntraPCV
* Selected: LDAP Username Password Credential Validator
* Parent instance: None

Furthermore, we now declare our previously created data source (`EntraDS`):

![PingFederate, additional PCV details](/docs/images/guides/active-directory/12.webp)

Click to zoom

This links our data store (`EntraDS`) to our PCV (`EntraPCV`).

#### Set up an Identity Provider[​](#set-up-an-identity-provider "Direct link to Set up an Identity Provider")

We can use our PCV once we set up an Identity Provider.

The IdP will be used to authenticate users against Active Directory using the
LDAP connection.

We do this in the Type subsection:

![PingFederate, IdP adapters](/docs/images/guides/active-directory/13.webp)

Defining an adapter

Next, in the IdP Adapter section...

Click: Add a new row to Credential Validators.

Select the PCV (`EntraPCV`) we created.

Optionally alter number of retries:

![PingFederate, selecting PCV ](/docs/images/guides/active-directory/14.webp)

Select the PCV

#### Add groups to OIDC policy management[​](#add-groups-to-oidc-policy-management "Direct link to Add groups to OIDC policy management")

QuestDB now needs to know about the user's AD group memberships to find their
permissions.

Groups are passed to QuestDB inside the User Info object in a custom claim.

This has to be added in the OpenID Connect Policy Management.

The field is Multi-Valued, because it is a list of group names.

Under the Attribute Contract subsection, see:

![PingFederate, Attribute Contract subsection](/docs/images/guides/active-directory/15.webp)

Click to zoom

Next, click to the Attribute Scopes subsection.

Ensure `groups` is among the `openid` attributes:

![PingFederate, Attribute Scopes](/docs/images/guides/active-directory/16.webp)

Click to zoom

Onwards to the Attribute Sources & User Lookup Section.

From this view, you can add local data stores.

Note item `test` of type of LDAP:

![PingFederate, Attribute Sources & User Lookup ui](/docs/images/guides/active-directory/17.webp)

Click to zoom

We created it via the following choices in Add Attribute Source:

![PingFederate, Add Attribute Source ui](/docs/images/guides/active-directory/18.webp)

Click to zoom

Note where we specified the Data Store (`EntraDS`).

This is also where the directory search parameters are defined.

Back at the Attribute Sources & User Lookup Section section, note we have set
`email`.

The source is `LDAP (test)`, while the value is `usePrincipalName`:

![PingFederate, Policy Management ui](/docs/images/guides/active-directory/19.webp)

Click to zoom

And finally!

In the same Attribute Sources & User Lookup Section...

Find `groups`.

Note the definition of Source (`LDAP (test)`) that bridges our various parts.

The value is `memberOf`.

![PingFederate, associating groups with the source](/docs/images/guides/active-directory/20.webp)

Click to zoom

#### Enable Resource Owner Password Credentials (ROPC) flow[​](#enable-resource-owner-password-credentials-ropc-flow "Direct link to Enable Resource Owner Password Credentials (ROPC) flow")

As described in the
[OIDC operations document](/docs/security/oidc/#enable-ropc)
tools - such as `psql` - can be integrated with the OIDC provider using the ROPC flow.

When setting this flow up, enable the Resource Owner Password Credentials flow in the
client settings.

Next, create a Resource Owner Credentials Grant Mapping to map values obtained from
the Password Credential Validator (PCV) into the persistent grants.

When setting this up, select the previously created LDAP Data Source and IdP Adapter, which links
to the existing PCV.

Then select the `username` attribute of the PCV as `USER_KEY`.

#### Confirm QuestDB mappings and login[​](#confirm-questdb-mappings-and-login "Direct link to Confirm QuestDB mappings and login")

QuestDB requires a mapping, as laid out in the
[OIDC operations document](/docs/security/oidc/#mapping-user-permissions).

If a given user has the HTTP permission, they will be able to now login via the
[Web Console](/docs/getting-started/web-console/overview/).

To test, head to `http://localhost:9000` and login.

If all has been wired up well, then login will succeed.

  

### Microsoft EntraId[​](#microsoft-entraid "Direct link to Microsoft EntraId")

This document sets up SSO authentication for the [QuestDB Web Console](/docs/getting-started/web-console/overview/) in
[Microsoft EntraID](https://www.microsoft.com/en-gb/security/business/identity-access/microsoft-entra-id), formerly known as Azure AD.

tip

To enlarge the images, click or tap them.

#### Set up the client application in Entra ID[​](#set-up-the-client-application-in-entra-id "Direct link to Set up the client application in Entra ID")

First thing first, let's pick a name for the client!

Then head to *Microsoft Entra Admin Center*, and register the application
under *Identity - App registrations - New registration*.

![EntraID image, app registration.](/docs/images/guides/active-directory-entraid/1_app_registration.webp)

App registration

The QuestDB [Web Console](/docs/getting-started/web-console/overview/) is a SPA (Single Page App).

As a result, it cannot store safely a client secret.

Instead, it can use PKCE (Proof Key for Code Exchange) to secure the flow.

When registering the application, select the SPA platform.

We also have to specify the URL of the [Web Console](/docs/getting-started/web-console/overview/) as Redirect URI.

![EntraID image, SPA and redirection URI](/docs/images/guides/active-directory-entraid/2_spa_redirect_uri.webp)

Add SPA platform with the redirection URI

After clicking *Register*, we have created a client application with the
name *QuestDB*.

Each application is assigned a unique id (known as Client ID in the
OAuth2 - OIDC standard). The client will identify itself with this id
when sending requests to Entra ID.

![EntraID image, application ID](/docs/images/guides/active-directory-entraid/3_application_id.webp)

Application ID

We find the platform configurations under *Authentication*. This is the place where
the previously set redirect URI can be viewed and modified. We can also specify
additional redirect URIs, if necessary.

The redirect URIs of the application are automatically eligible for the
*Authorization Code Flow with PKCE*, which is a special version of the OAuth2 standard's
Authorization Code Flow. It is specifically designed for applications where a client
secret (e.g. a password) could not be kept safely. As single page applications run in
the browser, they fall into this category.

The redirect URIs are also added to the *CORS* (Cross-Origin Resource Sharing) policy
of EntraID. CORS is a mechanism to allow a web page, such as the Web Console, to access
resources from a different domain than the one that served the page. In this context
this means that we let the Web Console to access Entra ID, while its origin is the
HTTP endpoint of QuestDB.

![EntraID image, PKCE and CORS](/docs/images/guides/active-directory-entraid/4_cors_pkce.webp)

PKCE and CORS

If we scroll down to the bottom of this page, we can also find a section where we
can enable the *Resource Owner Password Credential Flow*.

This OAuth2 flow is legacy, and should be enabled only if there is a requirement
of connecting to QuestDB using SSO (Single Sign-On) via clients not supporting
redirect based web flows.
This could mean a Postgres client without OAuth2 integration, such as *psql*, or
a standalone in-house client application, or could be just a jupyter notebook.

The main issue with this flow is that the client application has to be trusted
with the user's login details. The user's credentials are passed to the
application, in this case to QuestDB, and the client application uses these
credentials to authenticate the user by forwarding them to the identity provider,
in this case to Entra ID.

It is guaranteed that QuestDB does not store the user's credentials in any way.
They are not persisted into the database, not even in encrypted form.
The login details are treated as passthrough information. Only exception is
that server logs can contain the username, logged for audit purposes.

![EntraID image, enable ROPC](/docs/images/guides/active-directory-entraid/5_ropc.webp)

Enable ROPC

Our next stop is the *Token configuration*, where the OAuth2/OIDC access and ID
tokens can be customized.

Note that users can be authenticated without customized tokens, but authorization
would prove to be challenging. The user's security groups are not included
in the tokens by default.

QuestDB can be configured to request the user's groups from the UserInfo
endpoint of the OAuth2 server, but Entra ID cannot be configured to provide
this information via the UserInfo endpoint.
Therefore, we choose to customize the tokens, QuestDB will decode and
validate the ID token, and take the group information from there.

QuestDB authorization relies on receiving the group memberships of the user.
Entra ID groups should be mapped to QuestDB groups, and permissions can be
granted to the QuestDB groups. Detailed information about group mappings can
be found in the [OIDC integration](/docs/security/oidc/#user-permissions)
documentation.

![EntraID image, token customization](/docs/images/guides/active-directory-entraid/6_token_customization.webp)

Token customization

The customized tokens contain user information which cannot be accessed
without permission. User information is provided by Microsoft Graph, so
the client application needs specific permissions to access
Microsoft Graph APIs.

These permissions can be configured under *API permissions*. It is important
to note that we will be setting *Delegated* permissions here, meaning we
are not granting actual permissions to access user data. Instead, each user
logging into QuestDB will have to consent to accessing their user profile.

![EntraID image, API permissions](/docs/images/guides/active-directory-entraid/7_API_permissions.webp)

API permissions

By default, the *User.Read* permission is added to the list, but what we
really need is:

* openid: to be able to issue ID tokens
* profile: to access user information
* offline\_access: to be able to issue refresh tokens

By clicking on *Microsoft Graph* we can select and add these permissions.

![EntraID image, add openid permissions](/docs/images/guides/active-directory-entraid/8_add_openid_permissions.webp)

Add openid permissions

The *User.Read* permission is not needed. It can be removed by clicking
on the `...` at the end of the row, and selecting *Remove permission* from
the popup menu.

![EntraID image, permissions final](/docs/images/guides/active-directory-entraid/9_permissions_final.webp)

Permissions final list

With this we have finished setting up the QuestDB client application
in Entra ID, and now we can wire QuestDB and Entra ID together by
adding OIDC configuration to QuestDB.

#### QuestDB configuration[​](#questdb-configuration "Direct link to QuestDB configuration")

The below should be set in QuestDB's `server.conf`:

```prism-code
# enable OIDC  
acl.oidc.enabled=true  
  
# the claim contains the username or user id  
acl.oidc.sub.claim=name  
  
# the claim contains the user's group memberships  
acl.oidc.groups.claim=groups  
  
# groups are encoded in the token  
acl.oidc.groups.encoded.in.token=true  
  
# OIDC configuration endpoint of Entra ID  
acl.oidc.configuration.url=https://login.microsoftonline.com/12345678-1234-1234-1234-123456789abc/v2.0/.well-known/openid-configuration  
  
# application ID taken from Entra ID  
acl.oidc.client.id=8de84b90-1ea5-4e41-9e84-dba860aa01a6  
  
# redirect URI, QuestDB's HTTP endpoint  
acl.oidc.redirect.uri=http://localhost:9000  
  
# OAuth scopes the user has to consent to  
acl.oidc.scope=openid profile offline_access  
  
# enable ROPC flow  
# optional, required only if ROPC is enabled in Entra ID  
acl.oidc.ropc.flow.enabled=true
```

The application ID and the OIDC configuration endpoint's URL can be found
in the Overview of the application in Entra ID.

The application ID is displayed right under the application's name, the
OIDC configuration endpoint is displayed on the panel which opens up when
the *Endpoints* button is clicked.

![EntraID image, overview](/docs/images/guides/active-directory-entraid/10_overview.webp)

Application overview

#### Map groups and grant permissions[​](#map-groups-and-grant-permissions "Direct link to Map groups and grant permissions")

Now we can start QuestDB, and login with the built-in admin to create
group mappings.

As mentioned earlier, authorization works by mapping Entra ID groups
to QuestDB groups. When the user logs in, QuestDB decodes Entra ID
group memberships from the token, then finds the QuestDB groups
mapped to them, and the user gets the permissions based on the
mapped groups.

Create a group which is mapped to an Entra ID group

```prism-code
CREATE GROUP extUsers WITH EXTERNAL ALIAS '87654321-1234-1234-1234-123456789abc';
```

The above command maps the Entra ID group identified by object
id `87654321-1234-1234-1234-123456789abc` to a QuestDB group called `extUsers`.

We should grant the necessary QuestDB endpoint permissions first
to make sure users can access the Web Console, Postgres and ILP
interfaces as required. [Read more about endpoint permissions](/docs/security/rbac/#endpoint-permissions).

Grant endpoint permissions

```prism-code
GRANT HTTP, PGWIRE TO groupName;
```

Now we can grant the rest of the permissions as required. We can
grant access to tables, for example.

Grant database permissions

```prism-code
GRANT SELECT ON table1, table2 to groupName;
```

#### Confirm group mappings and login[​](#confirm-group-mappings-and-login "Direct link to Confirm group mappings and login")

To test, head to the Web Console and login.

If all has been wired up well, then login will succeed, and the user
will have the access granted to them.