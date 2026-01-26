On this page

QuestDB implements the InfluxDB Line Protocol to ingest data.

The InfluxDB Line Protocol is for **data ingestion only**.

For building queries, see the
[Query & SQL Overview](/docs/query/overview/).

Each ILP client library also has its own language-specific documentation set.

This supporting document thus provides an overview to aid in client selection
and initial configuration:

1. [Client libraries](/docs/ingestion/ilp/overview/#client-libraries)
2. [Server-Side configuration](/docs/ingestion/ilp/overview/#server-side-configuration)
3. [Transport selection](/docs/ingestion/ilp/overview/#transport-selection)
4. [Client-Side configuration](/docs/ingestion/ilp/overview/#client-side-configuration)
5. [Error handling](/docs/ingestion/ilp/overview/#error-handling)
6. [Authentication](/docs/ingestion/ilp/overview/#authentication)
7. [Table and column auto-creation](/docs/ingestion/ilp/overview/#table-and-column-auto-creation)
8. [Timestamp column name](/docs/ingestion/ilp/overview/#timestamp-column-name)
9. [HTTP Transaction semantics](/docs/ingestion/ilp/overview/#http-transaction-semantics)
10. [Exactly-once delivery](/docs/ingestion/ilp/overview/#exactly-once-delivery-vs-at-least-once-delivery)
11. [Multiple URLs for High Availability](/docs/ingestion/ilp/overview/#multiple-urls-for-high-availability)
12. [Health Check](/docs/ingestion/ilp/overview/#health-check)

## Client libraries[​](#client-libraries "Direct link to Client libraries")

The quickest way to get started is to select your library of choice.

From there, its documentation will carry you through to implementation.

Client libraries are available for several languages:

### C & C++

High-performance client for systems programming and embedded applications.

[Read more](/docs/ingestion/clients/c-and-cpp/)

![C & C++ logo](/docs/images/logos/cplusplus.svg)

### .NET

Cross-platform client for building applications with .NET technologies.

[Read more](/docs/ingestion/clients/dotnet/)

![.NET logo](/docs/images/logos/dotnet.svg)

### Go

An open-source programming language supported by Google with built-in concurrency.

[Read more](/docs/ingestion/clients/go/)

![Go logo](/docs/images/logos/go.svg)

### Java

Platform-independent client for enterprise applications and Android development.

[Read more](/docs/ingestion/clients/java/)

![Java logo](/docs/images/logos/java.svg)

### Node.js

Node.js® is an open-source, cross-platform JavaScript runtime environment.

[Read more](/docs/ingestion/clients/nodejs/)

![Node.js logo](/docs/images/logos/nodejs-light.svg)

### Python

Python is a programming language that lets you work quickly and integrate systems more effectively.

[Read more](/docs/ingestion/clients/python/)

![Python logo](/docs/images/logos/python.svg)

### Rust

Systems programming language focused on safety, speed, and concurrency.

[Read more](/docs/ingestion/clients/rust/)

![Rust logo](/docs/images/logos/rust.svg)

If you'd like more context on ILP overall, please continue reading.

## Enable or disable ILP[​](#enable-or-disable-ilp "Direct link to Enable or disable ILP")

If going over HTTP, ILP will use shared HTTP port `9000` (default) if the
following is set in `server.conf`:

```prism-code
line.http.enabled=true
```

## Server-Side Configuration[​](#server-side-configuration "Direct link to Server-Side Configuration")

The HTTP receiver configuration can be completely customized using
[QuestDB configuration keys for ILP](/docs/configuration/overview/#influxdb-line-protocol-ilp).

Configure the thread pools, buffer and queue sizes, receiver IP address and
port, load balancing, and more.

For more guidance in how to tune QuestDB, see
[capacity planning](/docs/getting-started/capacity-planning/).

## Transport selection[​](#transport-selection "Direct link to Transport selection")

The ILP protocol in QuestDB supports the following transport options:

* HTTP (default port 9000)
* TCP (default port 9009)

On QuestDB Enterprise HTTPS and TCPS are also available.

The HTTP(s) transport is recommended for most use cases. It provides feedback on
errors, automatically retries failed requests, and is easier to configure. The
TCP(s) transport is kept for compatibility with older QuestDB versions. It has
limited error feedback, no automatic retries, and requires manual handling of
connection failures. However, while HTTP is recommended, TCP has slightly lower
overhead than HTTP and may be useful in high-throughput scenarios in
high-latency networks.

## Client-Side Configuration[​](#client-side-configuration "Direct link to Client-Side Configuration")

Clients connect to a QuestDB using ILP via a configuration string. Configuration
strings combine a set of key/value pairs.

The standard configuration string pattern is:

```prism-code
schema::key1=value1;key2=value2;key3=value3;
```

It is made up of the following parts:

* **Schema**: One of the specified schemas in the
  [core parameters](/docs/ingestion/ilp/overview/#core-parameters) section
  below
* **Key=Value**: Each key-value pair sets a specific parameter for the client
* **Terminating semicolon**: A semicolon must follow the last key-value pair

Basic example:

```prism-code
http::addr=localhost:9000;
```

### Client parameters[​](#client-parameters "Direct link to Client parameters")

Below is a list of common parameters that ILP clients will accept.

These params facilitate connection to QuestDB's ILP server and define
client-specific behaviors.

Some are shared across all clients, while some are client specific. Refer to the
clients documentation for details.

warning

Any parameters tagged as `SENSITIVE` must be handled with care.

Exposing these values may expose your database to bad actors.

#### Core parameters[​](#core-parameters "Direct link to Core parameters")

* **schema**: Specifies the transport method, with support for: `http`, `https`,
  `tcp` & `tcps`
* **addr**: The address and port of the QuestDB server, as in `localhost:9000`.
* **protocol\_version**: QuestDB has evolved its protocol beyond the basic ILP.
  HTTP client autodetects the highest protocol version it can use, but TCP
  doesn't and defaults to 1. This is how you specify protocol version 2 (latest):

```prism-code
tcp::addr=localhost:9009;protocol_version=2
```

You need protocol version 2 in order to ingest n-dimensional arrays.
It is available from QuestDB version 9.0.0.

#### HTTP Parameters[​](#http-parameters "Direct link to HTTP Parameters")

* **password** (SENSITIVE): Password for HTTP Basic Authentication.
* **request\_min\_throughput**: Expected throughput for network send to the
  database server, in bytes.
  + Defaults to 100 KiB/s
  + Used to calculate a dynamic timeout for the request, so that larger requests
    do not prematurely timeout.
* **request\_timeout**: Base timeout for HTTP requests to the database, in
  milliseconds.
  + Defaults to 10 seconds.
* **retry\_timeout**: Maximum allowed time for client to attempt retries, in
  milliseconds.
  + Defaults to 10 seconds.
  + Not all errors are retriable.
* **token** (SENSITIVE): Bearer token for HTTP Token authentication.
  + Open source HTTP users are unable to generate tokens. For TCP token auth,
    see the below section.
* **username**: Username for HTTP Basic Authentication.

#### TCP Parameters[​](#tcp-parameters "Direct link to TCP Parameters")

note

These parameters are only useful when using ILP over TCP with authentication
enabled. Most users should use ILP over HTTP. These parameters are listed for
completeness and for users who have specific requirements.

*See the [Authentication](/docs/ingestion/ilp/overview/#authentication)
section below for configuration.*

* **auth\_timeout**: Timeout for TCP authentication with QuestDB server, in
  milliseconds.
  + Default 15 seconds.
* **token** (SENSITIVE): TCP Authentication `d` parameter.
  + **token\_x** (SENSITIVE): TCP Authentication `x` parameter.
    - Used in C/C++/Rust/Python clients.
  + **token\_y** (SENSITIVE): TCP Authentication `y` parameter.
    - Used in C/C++/Rust/Python clients.
* **username**: Username for TCP authentication.

#### Auto-flushing behavior[​](#auto-flushing-behavior "Direct link to Auto-flushing behavior")

* **auto\_flush**: Enable or disable automatic flushing (`on`/`off`).

  + Default is “on” for clients that support auto-flushing (all except C, C++ &
    Rust).
* **auto\_flush\_bytes** Auto-flushing is triggered above this buffer size.

  + Disabled by default.
* **auto\_flush\_interval**: Auto-flushing is triggered after this time period has
  elapsed since the last flush, in milliseconds.

  + Defaults to 1 second
  + This is not a periodic timer - it will only be checked on the next row
    creation.
* **auto\_flush\_rows**: Auto-flushing is triggered above this row count.

  + Defaults to `75,000` for HTTP, and `600` for TCP.
  + If set, this implies “auto\_flush=on”.

#### Buffer configuration[​](#buffer-configuration "Direct link to Buffer configuration")

* **init\_buf\_size**: Set the initial (but growable) size of the buffer in bytes.
  + Defaults to `64 KiB`.
* **max\_buf\_size**: Sets the growth limit of the buffer in bytes.
  + Defaults to `100 MiB`.
  + Clients will error if this is exceeded.
* **max\_name\_len**: The maximum alloable number of UTF-8 bytes in the table or
  column names.
  + Defaults to `127`.
  + Related to length limits for filenames on the user's host OS.

#### TLS configuration[​](#tls-configuration "Direct link to TLS configuration")

*QuestDB Enterprise only.*

* **tls\_verify**: Toggle verification of TLS certificates. Default is `on`.
* **tls\_roots**: Specify the source of bundled TLS certificates.
  + The defaults and possible param values are client-specific.
    - In Rust and Python this might be “webpki”, “os-certs” or a path to a “pem”
      file.
    - In Java this might be a path to a “jks” trust store.
    - **tls\_roots\_password** Password to a configured tls\_roots if any.
      * Passwords are sensitive! Manage appropriately.
* **tls\_ca**: Path to single certificate authourity, not supported on all
  clients.
  + Java for instance would apply `tls_roots=/path/to/Java/key/store`

#### Network configuration[​](#network-configuration "Direct link to Network configuration")

* **bind\_interface**: Optionally, specify the local network interface for
  outbound connections. Useful if you have multiple interfaces or an accelerated
  network interface (e.g. Solarflare)
  + Not to be confused with the QuestDB port in the `addr` param.

## Error handling[​](#error-handling "Direct link to Error handling")

The HTTP transport supports automatic retries for failed requests deemed
recoverable. Recoverable errors include network errors, some server errors, and
timeouts, while non-recoverable errors encompass invalid data, authentication
errors, and other client-side errors.

Retrying is particularly beneficial during network issues or when the server is
temporarily unavailable. The retrying behavior can be configured through the
`retry_timeout` configuration option or, in some clients, via their API. The
client continues to retry recoverable errors until they either succeed or the
specified timeout is reached.

The TCP transport lacks support for error propagation from the server. In such
cases, the server merely closes the connection upon encountering an error.
Consequently, the client receives no additional error information from the
server. This limitation significantly contributes to the preference for HTTP
transport over TCP transport.

## Authentication[​](#authentication "Direct link to Authentication")

note

Using [QuestDB Enterprise](https://questdb.com/enterprise/)?

Skip to [advanced security features](/docs/security/rbac/) instead, which
provides holistic security out-of-the-box.

InfluxDB Line Protocol supports authentication via HTTP Basic Authentication,
using [the HTTP Parameters](/docs/ingestion/ilp/overview/#http-parameters),
or via token when using the TCP transport, using
[the TCP Parameters](/docs/ingestion/ilp/overview/#tcp-parameters).

A similar pattern is used across all client libraries. If you want to use a TCP
token, you need to configure your QuestDB server. This document will break down
and demonstrate the configuration keys and core configuration options.

Once a client has been selected and configured, resume from your language client
documentation.

### TCP token authentication setup[​](#tcp-token-authentication-setup "Direct link to TCP token authentication setup")

Create `d`, `x` & `y` tokens for client usage.

#### Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* `jose`: C-language implementation of Javascript Object Signing and Encryption.
  Generates tokens.
* `jq`: For pretty JSON output.

* macOS
* Debian
* Ubuntu

```prism-code
brew install jose  
brew install jq
```

```prism-code
yum install jose  
yum install jq
```

```prism-code
apt install jose  
apt install jq
```

#### Server configuration[​](#server-configuration "Direct link to Server configuration")

Next, create an authentication file.

Only elliptic curve (P-256) are supported (key type `ec-p-256-sha256`):

```prism-code
testUser1 ec-p-256-sha256 fLKYEaoEb9lrn3nkwLDA-M_xnuFOdSt9y0Z7_vWSHLU Dt5tbS1dEDMSYfym3fgMv0B99szno-dFc1rYF9t0aac  
# [key/user id] [key type] {keyX keyY}
```

Generate an authentication file using the `jose` utility:

```prism-code
jose jwk gen -i '{"alg":"ES256", "kid": "testUser1"}' -o /var/lib/questdb/conf/full_auth.json  
  
KID=$(cat /var/lib/questdb/conf/full_auth.json | jq -r '.kid')  
X=$(cat /var/lib/questdb/conf/full_auth.json | jq -r '.x')  
Y=$(cat /var/lib/questdb/conf/full_auth.json | jq -r '.y')  
  
echo "$KID ec-p-256-sha256 $X $Y" | tee /var/lib/questdb/conf/auth.txt
```

Once created, reference it in the server [configuration](/docs/configuration/overview/):

/path/to/server.conf

```prism-code
line.tcp.auth.db.path=conf/auth.txt
```

#### Client keys[​](#client-keys "Direct link to Client keys")

For the server configuration above, the corresponding JSON Web Key must be
stored on the clients' side.

When sending a fully-composed JWK, it will have the following keys:

```prism-code
{  
  "kty": "EC",  
  "d": "5UjEMuA0Pj5pjK8a-fa24dyIf-Es5mYny3oE_Wmus48",  
  "crv": "P-256",  
  "kid": "testUser1",  
  "x": "fLKYEaoEb9lrn3nkwLDA-M_xnuFOdSt9y0Z7_vWSHLU",  
  "y": "Dt5tbS1dEDMSYfym3fgMv0B99szno-dFc1rYF9t0aac"  
}
```

The `d`, `x` and `y` parameters generate the public key.

For example, the Python client would be configured as outlined in the
[Python docs](https://py-questdb-client.readthedocs.io/en/latest/conf.html#tcp-auth).

## Table and column auto-creation[​](#table-and-column-auto-creation "Direct link to Table and column auto-creation")

When sending data to a table that does not exist, the server will create the
table automatically. This also applies to columns that do not exist. The server
will use the first row of data to determine the column types. Please note that table
and column names must follow the QuestDB [naming rules](/docs/query/sql/create-table/#table-name).

If the table already exists, the server will validate that the columns match the
existing table. If the columns do not match, the server will return a
non-recoverable error which, when using the HTTP/HTTPS transport, is propagated
to the client.

You can avoid table and/or column auto-creation by setting the
`line.auto.create.new.columns` and `line.auto.create.new.tables`configuration
parameters to false.

If you're using QuestDB Enterprise, you must grant further permissions to the
authenticated user:

```prism-code
CREATE SERVICE ACCOUNT ingest_user; -- creates a service account to be used by a client  
GRANT ilp, create table TO ingest_user; -- grants permissions to ingest data and create tables  
GRANT add column, insert ON all tables TO ingest_user; -- grants permissions to add columns and insert data to all tables  
--  OR  
GRANT add column, insert ON table1, table2 TO ingest_user; -- grants permissions to add columns and insert data to specific tables
```

Read more setup details in the
[Enterprise quickstart](/docs/getting-started/enterprise-quick-start/#4-ingest-data-influxdb-line-protocol)
and the [role-based access control](/docs/security/rbac/) guides.

## Timestamp Column Name[​](#timestamp-column-name "Direct link to Timestamp Column Name")

QuestDB's ILP protocol sends timestamps without a column name.

**Auto-created tables always use `timestamp` as the designated timestamp column name.**
There is no client-side option to change this. If you need a different column name,
you must pre-create the table before sending data.

If the table already exists, the designated timestamp column is used regardless
of its name.

To pre-create a table with a custom timestamp column name, use `CREATE TABLE`:

Creating a timestamp named my\_ts

```prism-code
CREATE TABLE IF NOT EXISTS 'trades' (  
  symbol SYMBOL capacity 256 CACHE,  
  side SYMBOL capacity 256 CACHE,  
  price DOUBLE,  
  amount DOUBLE,  
  my_ts TIMESTAMP  
) timestamp (my_ts) PARTITION BY DAY WAL;
```

You can use the `CREATE TABLE IF NOT EXISTS` construct to make sure the table is
created, but without raising an error if the table already exists.

## HTTP transaction semantics[​](#http-transaction-semantics "Direct link to HTTP transaction semantics")

The TCP endpoint does not support transactions. The HTTP ILP endpoint treats
every requests as an individual transaction, so long as it contains rows for a
single table.

As of writing, the HTTP endpoint does not provide full transactionality in all
cases.

Specifically:

* If an HTTP request contains data for two tables and the final commit fails for
  the second table, the data for the first table will still be committed. This
  is a deviation from full transactionality, where a failure in any part of the
  transaction would result in the entire transaction being rolled back. If data
  transactionality is important for you, the best practice is to make sure you
  flush data to the server in batches that contain rows for a single table.
* Even when you are sending data to a single table, when dynamically adding new
  columns to a table, an implicit commit occurs each time a new column is added.
  If the request is aborted or has parse errors, no data will be inserted into
  the corresponding table, but the new column will be added and will not be
  rolled back.
* Some clients have built-in support for controlling transactions. These APIs
  help to comply with the single-table-per-request pre-requisite for HTTP
  transactions, but they don't control if new columns are being added.
* As of writing, if you want to make sure you have data transactionality and
  schema/metadata transactionality, you should disable
  `line.auto.create.new.columns` and `line.auto.create.new.tables` on your
  configuration. Be aware that if you do this, you will not have dynamic schema
  capabilities and you will need to create each table and column before you try
  to ingest data, via [`CREATE TABLE`](/docs/query/sql/create-table/) and/or
  [`ALTER TABLE ADD COLUMN`](/docs/query/sql/alter-table-add-column/) SQL
  statements.

## Exactly-once delivery vs at-least-once delivery[​](#exactly-once-delivery-vs-at-least-once-delivery "Direct link to Exactly-once delivery vs at-least-once delivery")

The retrying behavior of the HTTP transport can lead to some data being sent to
the server more than once.

**Example**: Client sends a batch to the server, the server receives the batch,
processes it, but fails to send a response back to the client due to a network
error. The client will retry sending the batch to the server. This means the
server will receive the batch again and process it again. This can lead to
duplicated rows in the server.

The are two ways to mitigate this issue:

* Use [QuestDB deduplication feature](/docs/concepts/deduplication/) to remove
  duplicated rows. QuestDB server can detect and remove duplicated rows
  automatically, resulting in exactly-once processing. This is recommended when
  using the HTTP transport with retrying enabled.
* Disable retrying by setting `retry_timeout` to 0. This will make the client
  send the batch only once, failed requests will not be retried and the client
  will receive an error. This effectively turns the client into an at-most-once
  delivery.

## Multiple URLs for High Availability[​](#multiple-urls-for-high-availability "Direct link to Multiple URLs for High Availability")

The ILP client can be configured with multiple possible endpoints to send your data to.
Only one will be sent to at any one time.

note

This feature requires QuestDB OSS 9.1.0+ or Enterprise 3.0.4+. OSS users are discouraged of using
this feature, as once data is sent to another primary, there is no way to reconcilliate the
diverging instances. QuestDB Enterprise users can leverage this feature to transparently
handle replication failover.

To configure this feature, simply provide multiple addr entries. For example, when using Java:

```prism-code
try (Sender sender = Sender.fromConfig("http::addr=localhost:9000;addr=localhost:9999;")) {  
   // ...  
}
```

tip

At the moment of writing this guide, only some of the QuestDB clients support multi-url configuration. Please
refer to the documentation of your client to make sure it is available.

On initialisation, if `protocol_version=auto`, the sender will identify the first instance that is writeable. Then it
will stick to this instance and write any subsequent data to it.

In the event that the instance becomes unavailable for writes, the client will retry the other possible endpoints. As long
as one instance becomes writable before the maximum retry timeout is reached, it will stick to it instead. This unvailability is characterised by failures to connect or locate the instance, or the instance returning an error code due to it being read-only.

By configuring multiple addresses, you can continue capturing data if your primary instance fails, without having to reconfigure the clients, as they will automatically failover to the new primary once available.

Enterprise users can use multiple URLs to handle replication failover, without the need to introduce a load-balancer or reconfigure clients.

## Health Check[​](#health-check "Direct link to Health Check")

To monitor your active connection, there is a `ping` endpoint:

```prism-code
curl -I http://localhost:9000/ping
```

Returns (pong!):

```prism-code
HTTP/1.1 204 OK  
Server: questDB/1.0  
Date: Fri, 2 Feb 2024 17:09:38 GMT  
Transfer-Encoding: chunked  
Content-Type: text/plain; charset=utf-8  
X-Influxdb-Version: v2.7.4
```

Determine whether an instance is active and confirm the version of InfluxDB Line
Protocol with which you are interacting.