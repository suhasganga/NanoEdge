On this page

## Hardware recommendations[​](#hardware-recommendations "Direct link to Hardware recommendations")

#### CPU/RAM[​](#cpuram "Direct link to CPU/RAM")

A production instance for QuestDB should be provisioned with at least `4 vCPUs` and `8 GiB` of memory. If possible,
a 1:4 `vCPU/RAM` ratio should be used. Some use cases may benefit from a `1:8` ratio, if this means that all the working
set data will fit into memory; this can increase query performance by as much as `10x`.

It is **not recommended** to run production workloads on less than `4 vCPUs`, as below this number, parallel querying optimisations
may be disabled. This is to ensure there is sufficient resources available for ingestion.

#### Architecture[​](#architecture "Direct link to Architecture")

QuestDB should be deployed on Intel/AMD architectures i.e. `x86_64` and **not** on `ARM` i.e. `aarch64`. Some optimisations are not available
on `ARM`, e.g. `SIMD`.

#### Storage[​](#storage "Direct link to Storage")

Data should be stored on a data disk with at minimum 3000 IOPS/125 MBps, and ideally at least 5000 IOPS/300 MBps.
Higher end workloads should scale up the disks appropriately, or use multiple disks if necessary.

It is also worth checking the burst capacity of your storage. This capacity should only be used during
heavy I/O spikes/infrequent out-of-order (O3) writes. It is useful to have in case you hit unexpected load bursts.

### Elastic Compute Cloud (EC2) with Elastic Block Storage (EBS)[​](#elastic-compute-cloud-ec2-with-elastic-block-storage-ebs "Direct link to Elastic Compute Cloud (EC2) with Elastic Block Storage (EBS)")

We recommend starting with `M8` instances, with an upgrade to
`R8` instances if extra RAM is needed. You can use either `i` (Intel) or `a` (AMD) instances.

These should be deployed with an `x86_64` Linux distribution, such as Ubuntu.

For storage, we recommend using `gp3` disks, as these provide a better price-to-performance
ratio compared to `gp2` or `io1` offerings.`5000 IOPS/300 MBps` is a good starting point until
you have tested your workload.

For the file system, use `zfs` with `lz4`, as this will compress your data. If compression
is not a concern, then use `ext4` or `xfs` for a little higher performance.

### Elastic File System (EFS)[​](#elastic-file-system-efs "Direct link to Elastic File System (EFS)")

QuestDB **does not** support `EFS` for its primary storage. Do not use it instead of `EBS`.

You can use it as object store, but we would recommend using `S3` instead, as a simpler,
and cheaper, alternative.

### Simple Storage Service (S3)[​](#simple-storage-service-s3 "Direct link to Simple Storage Service (S3)")

QuestDB supports `S3` as its replication object-store in the Enterprise edition.

This requires very little provisioning - simply create a bucket or virtual subdirectory and follow
the [Enterprise Quick Start](/docs/getting-started/enterprise-quick-start/) steps to configure replication.

### Minimum specification[​](#minimum-specification "Direct link to Minimum specification")

* **Instance**: `m8i.xlarge` or `m8a.xlarge` `(4 vCPUs, 16 GiB RAM)`
* **Storage**
  + **OS disk**: `gp3 (30 GiB)` volume provisioned with `3000 IOPS/125 MBps`.
  + **Data disk**: `gp3 (100 GiB)` volume provisioned with `3000 IOPS/125 MBps`.
* **Operating System**: `Linux Ubuntu 24.04 LTS x86_64`.
* **File System**: `ext4`

### Better specification[​](#better-specification "Direct link to Better specification")

* **Instance**: `r8i.2xlarge` or `r8a.2xlarge` `(8 vCPUs, 64 GiB RAM)`
* **Storage**
  + **OS disk**: `gp3 (30 GiB)` volume provisioned with `5000 IOPS/300 MBps`.
  + **Data disk**: `gp3 (300 GiB)` volume provisioned with `5000 IOPS/300 MBps`.
* **Operating System**: `Linux Ubuntu 24.04 LTS x86_64`.
* **File System**: `zfs` with `lz4` compression.

note

If the above instance types are not available in your region, then simply downgrade to an earlier version i.e. `8 -> 7 -> 6`.

### AWS Graviton[​](#aws-graviton "Direct link to AWS Graviton")

QuestDB can also be deployed on AWS Graviton (ARM) instances, which have a strong price-to-performance ratio.

For example, `r8g` instances are cheaper than `r6i` instances, and will offer superior performance for most Java-centric code.
Queries which rely on the `JIT` compiler (native WHERE filters) or vectorisation optimisations will potentially run slower.
Ingestion speed is generally unaffected.

Therefore, if your use case is ingestion-centric, or your queries do not heavily leverage SIMD/JIT, `r8g` instances
may offer better performance and better value overall.

### Storage Optimised Instances (Enterprise)[​](#storage-optimised-instances-enterprise "Direct link to Storage Optimised Instances (Enterprise)")

AWS offers storage-optimised instances (e.g. `i7i`), which include locally-attached NVMe devices. Workloads which
are disk-limited (for example, heavy out-of-order writes) will benefit significantly from the faster storage.

However, it is not recommended to use locally-attached NVMe on QuestDB OSS, as instance termination or failure
will lead to data loss. QuestDB Enterprise replicates data eagerly to object storage (`S3`), preserving
data in the event of an instance failure, and can therefore can safely leverage the faster disks.

## Launching QuestDB on EC2[​](#launching-questdb-on-ec2 "Direct link to Launching QuestDB on EC2")

Once you have provisioned your `EC2` instance with attached `EBS` storage, you can simply
follow the setup instructions for a [Docker](/docs/deployment/docker/) or [systemd](/docs/deployment/systemd/) installation.

You can also keep it simple - just [download](https://questdb.com/download/) the binary and run it directly.
QuestDB is a single self-contained binary and easy to deploy.

## Launching QuestDB on the AWS Marketplace[​](#launching-questdb-on-the-aws-marketplace "Direct link to Launching QuestDB on the AWS Marketplace")

[AWS Marketplace](https://aws.amazon.com/marketplace) is a digital catalog with software listings from independent
software vendors that runs on AWS. This guide describes how to launch QuestDB
via the AWS Marketplace using the official listing. This document also describes
usage instructions after you have launched the instance, including hints for
authentication, the available interfaces, and tips for accessing the REST API
and [Web Console](/docs/getting-started/web-console/overview/).

The QuestDB listing can be found in the AWS Marketplace under the databases
category. To launch a QuestDB instance:

1. Navigate to the
   [QuestDB listing](https://aws.amazon.com/marketplace/search/results?searchTerms=questdb)
2. Click **Continue to Subscribe** and subscribe to the offering
3. **Configure** a version, an AWS region and click **Continue to** **Launch**
4. Choose an instance type and network configuration and click **Launch**

An information panel displays the ID of the QuestDB instance with launch
configuration details and hints for locating the instance in the EC2 console.

The default user is `admin` and password is `quest` to log in to the Web Console.

## QuestDB configuration[​](#questdb-configuration "Direct link to QuestDB configuration")

Connect to the instance where QuestDB is deployed using SSH. The server
configuration file is at the following location on the AMI:

```prism-code
/var/lib/questdb/conf/server.conf
```

For details on the server properties and using this file, see the
[server configuration documentation](/docs/configuration/overview/).

The default ports used by QuestDB interfaces are as follows:

* [Web Console](/docs/getting-started/web-console/overview/) & REST API is available on port `9000`
* PostgreSQL wire protocol available on `8812`
* InfluxDB line protocol `9009` (TCP and UDP)
* Health monitoring & Prometheus `/metrics` `9003`

### Postgres credentials[​](#postgres-credentials "Direct link to Postgres credentials")

Generated credentials can be found in the server configuration file:

```prism-code
/var/lib/questdb/conf/server.conf
```

The default Postgres username is `admin` and a password is randomly generated
during startup:

```prism-code
pg.user=admin  
pg.password=...
```

To use the credentials that are randomly generated and stored in the
`server.conf`file, restart the database using the command
`sudo systemctl restart questdb`.

### InfluxDB line protocol credentials[​](#influxdb-line-protocol-credentials "Direct link to InfluxDB line protocol credentials")

The credentials for InfluxDB line protocol can be found at

```prism-code
/var/lib/questdb/conf/full_auth.json
```

For details on authentication using this protocol, see the
[InfluxDB line protocol authentication guide](/docs/ingestion/ilp/overview/#authentication).

### Disabling authentication[​](#disabling-authentication "Direct link to Disabling authentication")

If you would like to disable authentication for Postgres wire protocol or
InfluxDB line protocol, comment out the following lines in the server
configuration file:

/var/lib/questdb/conf/server.conf

```prism-code
# pg.password=...  
  
# line.tcp.auth.db.path=conf/auth.txt
```

### Disabling interfaces[​](#disabling-interfaces "Direct link to Disabling interfaces")

Interfaces may be **disabled completely** with the following configuration:

/var/lib/questdb/conf/server.conf

```prism-code
# disable postgres  
pg.enabled=false  
  
# disable InfluxDB line protocol over TCP and UDP  
line.tcp.enabled=false  
line.udp.enabled=false  
  
# disable HTTP (web console and REST API)  
http.enabled=false
```

The HTTP interface may alternatively be set to **readonly**:

/var/lib/questdb/conf/server.conf

```prism-code
# set HTTP interface to readonly  
http.security.readonly=true
```

## Upgrading QuestDB[​](#upgrading-questdb "Direct link to Upgrading QuestDB")

note

* Check the [release notes](https://github.com/questdb/questdb/releases) and
  ensure that necessary [backup](/docs/operations/backup/) is completed.

You can perform the following steps to upgrade your QuestDB version on an
official AWS QuestDB AMI:

* Stop the service:

```prism-code
systemctl stop questdb.service
```

* Download and copy over the new binary

```prism-code
wget https://github.com/questdb/questdb/releases/download/9.3.1/questdb-9.3.1-no-jre-bin.tar.gz \  
tar xzvf questdb-9.3.1-no-jre-bin.tar.gz  
cp questdb-9.3.1-no-jre-bin/questdb.jar /usr/local/bin/questdb.jar  
cp questdb-9.3.1-no-jre-bin/questdb.jar /usr/local/bin/questdb-9.3.1.jar
```

* Restart the service again:

```prism-code
systemctl restart questdb.service  
systemctl status questdb.service
```