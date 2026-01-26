On this page

Upgrading from QuestDB Open Source to QuestDB Enterprise is straightforward:
**download the Enterprise binaries, swap them in, and restart**. Your data
stays in place and works immediately.

## What you get with QuestDB Enterprise[​](#what-you-get-with-questdb-enterprise "Direct link to What you get with QuestDB Enterprise")

* **TLS encryption** for all network interfaces
* **Role-based access control (RBAC)** with users, groups, and permissions
* **Single Sign-On (SSO)** via OpenID Connect
* **Database replication** for high availability
* **Multi-tier storage** with seamless object storage integration
* **Automated backup and recovery** for data protection

## Upgrade steps[​](#upgrade-steps "Direct link to Upgrade steps")

### 1. Download Enterprise binaries[​](#1-download-enterprise-binaries "Direct link to 1. Download Enterprise binaries")

You should have received an email with download credentials for the Enterprise
binaries. Download the version matching your operating system and architecture.

tip

Check the [release notes](https://questdb.com/release-notes/?ref=docs&type=enterprise)
for the latest features and improvements.

### 2. Swap binaries and restart[​](#2-swap-binaries-and-restart "Direct link to 2. Swap binaries and restart")

1. Stop your running QuestDB instance
2. Replace the existing QuestDB binaries with the Enterprise ones
3. Start QuestDB with the new binaries

That's it! The database will automatically prepare your existing tables for
Enterprise features on first startup.

Optional: Create a backup first

While upgrades are safe, you can create a restore point before upgrading:

```prism-code
CHECKPOINT CREATE
```

Then back up your data directory (e.g., create a `.tar` archive or cloud
snapshot). See [Backup and restore](/docs/operations/backup/) for details.

## Configure QuestDB Enterprise features[​](#configure-questdb-enterprise-features "Direct link to Configure QuestDB Enterprise features")

These steps are **optional** - configure only the features you need.

### TLS encryption[​](#tls-encryption "Direct link to TLS encryption")

Secure all network connections with TLS. You'll need a certificate in PEM
format, or you can use a
[self-signed demo certificate](/docs/security/tls/#demo-certificates) to get
started.

See the [TLS Encryption guide](/docs/security/tls/).

### User accounts and permissions[​](#user-accounts-and-permissions "Direct link to User accounts and permissions")

Replace the default admin credentials in `server.conf`:

server.conf

```prism-code
acl.admin.user=myadmin  
acl.admin.password=mypwd
```

For production, create proper admin accounts and disable the built-in admin:

```prism-code
CREATE USER administrator WITH PASSWORD adminpwd;  
GRANT ALL TO administrator WITH GRANT OPTION;
```

server.conf

```prism-code
acl.admin.user.enabled=false
```

See the [RBAC documentation](/docs/security/rbac/) for complete setup.

### Single Sign-On (SSO)[​](#single-sign-on-sso "Direct link to Single Sign-On (SSO)")

Integrate with your identity provider (Microsoft Entra ID, PingFederate, etc.)
for centralized authentication.

See the [OIDC Integration guide](/docs/security/oidc/).

### Replication[​](#replication "Direct link to Replication")

Set up database replication for high availability and disaster recovery.

See the [Database Replication guide](/docs/high-availability/setup/).

## Important notes[​](#important-notes "Direct link to Important notes")

The upgrade process modifies table metadata to enable Enterprise features. For
this reason:

* Always perform an **in-place upgrade** (swap binaries in the same
  installation)
* Don't copy data directories between Open Source and Enterprise installations
* If reusing an object store from a test Enterprise instance, clear it first

Have a complex migration scenario?
[Contact us](https://questdb.com/enterprise/contact/) and we'll help with your setup.