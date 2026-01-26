On this page

Enterprise—

This guide covers setting up primary-replica replication.

[Learn more](https://questdb.com/enterprise/)

This guide walks you through setting up QuestDB Enterprise replication.

**Prerequisites:** Read the [Replication overview](/docs/high-availability/overview/)
to understand how replication works.

## Setup steps[​](#setup-steps "Direct link to Setup steps")

1. Configure object storage (AWS S3, Azure Blob, GCS, or NFS)
2. Configure the **primary** node
3. Take a snapshot of the primary
4. Configure **replica** node(s)

## 1. Configure object storage[​](#1-configure-object-storage "Direct link to 1. Configure object storage")

Choose your object storage provider and build the connection string for
`replication.object.store` in `server.conf`.

### AWS S3[​](#aws-s3 "Direct link to AWS S3")

Create an S3 bucket following
[AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html).

**Recommendations:**

* Select a region close to your primary node
* Disable blob versioning
* Set up a
  [lifecycle policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html)
  to manage WAL file retention (see [Snapshot and expiration policies](#snapshot-and-expiration-policies))

**Connection string:**

```prism-code
replication.object.store=s3::bucket=${BUCKET_NAME};root=${DB_INSTANCE_NAME};region=${AWS_REGION};access_key_id=${AWS_ACCESS_KEY};secret_access_key=${AWS_SECRET_ACCESS_KEY};
```

`DB_INSTANCE_NAME` can be any unique alphanumeric string (dashes allowed). Use
the same value across all nodes in your replication cluster.

### Azure Blob Storage[​](#azure-blob-storage "Direct link to Azure Blob Storage")

Create a Storage Account following
[Azure documentation](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal),
then create a Blob Container.

**Recommendations:**

* Select a region close to your primary node
* Disable blob versioning
* Set up
  [Lifecycle Management](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-policy-configure?tabs=azure-portal)
  for WAL file retention

**Connection string:**

```prism-code
replication.object.store=azblob::endpoint=https://${STORE_ACCOUNT}.blob.core.windows.net;container=${BLOB_CONTAINER};root=${DB_INSTANCE_NAME};account_name=${STORE_ACCOUNT};account_key=${STORE_KEY};
```

### Google Cloud Storage[​](#google-cloud-storage "Direct link to Google Cloud Storage")

Create a GCS bucket, then create a service account with `Storage Admin` (or
equivalent) permissions. Download the JSON key and encode it as Base64:

```prism-code
cat <key>.json | base64
```

**Connection string:**

```prism-code
replication.object.store=gcs::bucket=${BUCKET_NAME};root=/;credential=${BASE64_ENCODED_KEY};
```

Alternatively, use `credential_path` to reference the key file directly.

### NFS[​](#nfs "Direct link to NFS")

Mount the shared filesystem on all nodes. Ensure the QuestDB user has read/write
permissions.

**Important:** Both the WAL folder and scratch folder must be on the same NFS
mount to prevent write corruption.

**Connection string:**

```prism-code
replication.object.store=fs::root=/mnt/nfs_replication/final;atomic_write_dir=/mnt/nfs_replication/scratch;
```

## 2. Configure the primary node[​](#2-configure-the-primary-node "Direct link to 2. Configure the primary node")

Add to `server.conf`:

| Setting | Value |
| --- | --- |
| `replication.role` | `primary` |
| `replication.object.store` | Your connection string from step 1 |
| `cairo.snapshot.instance.id` | Unique UUID for this node |

Restart QuestDB.

## 3. Take a snapshot[​](#3-take-a-snapshot "Direct link to 3. Take a snapshot")

Replicas are initialized from a snapshot of the primary's data. This involves
creating a backup of the primary and preparing it for restoration on replica
nodes.

See [Backup and restore](/docs/operations/backup/) for the full procedure.

tip

Set up regular snapshots (daily or weekly). See
[Snapshot and expiration policies](#snapshot-and-expiration-policies) for
guidance.

## 4. Configure replica node(s)[​](#4-configure-replica-nodes "Direct link to 4. Configure replica node(s)")

Create a new QuestDB instance. Add to `server.conf`:

| Setting | Value |
| --- | --- |
| `replication.role` | `replica` |
| `replication.object.store` | Same connection string as primary |
| `cairo.snapshot.instance.id` | Unique UUID for this replica |

warning

Do not copy `server.conf` from the primary. Two nodes configured as primary
with the same object store will break replication.

Restore the `db` directory from the primary's snapshot, then start the replica.
It will download and apply WAL files to catch up with the primary.

## Configuration reference[​](#configuration-reference "Direct link to Configuration reference")

All replication settings go in `server.conf`. After changes, restart QuestDB.

tip

Use environment variables for sensitive settings:

```prism-code
export QDB_REPLICATION_OBJECT_STORE="azblob::..."
```

| Property | Default | Reloadable | Description |
| --- | --- | --- | --- |
| replication.role | none | No | Defaults to `none` for stand-alone instances. To enable replication set to one of: `primary`, `replica`. |
| replication.object.store |  | No | A configuration string that allows connecting to an object store. The format is **scheme::key1=value;key2=value2;…**. The various keys and values are detailed in a later section. Ignored if replication is disabled. No default given variability. |
| cairo.wal.segment.rollover.size | 2097152 | No | The size of the WAL segment before it is rolled over. Default is `2MiB`. However, defaults to `0` unless `replication.role=primary` is set. |
| cairo.writer.command.queue.capacity | 32 | No | Maximum writer ALTER TABLE and replication command capacity. Shared between all the tables. |
| replication.primary.throttle.window.duration | 10000 | No | The millisecond duration of the sliding window used to process replication batches. Default is `10000` ms. |
| replication.requests.max.concurrent | 0 | No | A limit to the number of concurrent object store requests. The default is `0` for unlimited. |
| replication.requests.retry.attempts | 3 | No | Maximum number of times to retry a failed object store request before logging an error and reattempting later after a delay. Default is `3`. |
| replication.requests.retry.interval | 200 | No | How long to wait before retrying a failed operation. Default is `200` ms. |
| replication.primary.compression.threads | calculated | No | Max number of threads used to perform file compression operations before uploading to the object store. The default value is calculated as half the number of CPU cores. |
| replication.primary.compression.level | 1 | No | Zstd compression level. Defaults to `1`. Valid values are from 1 to 22. |
| replication.replica.poll.interval | 1000 | No | Millisecond polling rate of a replica instance to check for the availability of new changes. |
| replication.primary.sequencer.part.txn.count | 5000 | No | Sets the txn chunking size for each compressed batch. Smaller is better for constrained networks (but more costly). |
| replication.primary.checksum=service-dependent | service-dependent | No | Where a checksum should be calculated for each uploaded artifact. Required for some object stores. Other options: never, always |
| replication.primary.upload.truncated | true | No | Skip trailing, empty column data inside a WAL column file. |
| replication.requests.buffer.size | 32768 | No | Buffer size used for object-storage downloads. |
| replication.summary.interval | 1m | No | Frequency for printing replication progress summary in the logs. |
| replication.metrics.per.table | true | No | Enable per-table replication metrics on the prometheus metrics endpoint. |
| replication.metrics.dropped.table.poll.count | 10 | No | How many scrapes of prometheus metrics endpoint before dropped tables will no longer appear. |
| replication.requests.max.batch.size.fast | 64 | No | Number of parallel requests allowed during the 'fast' process (non-resource constrained). |
| replication.requests.max.batch.size.slow | 2 | No | Number of parallel requests allowed during the 'slow' process (error/resource constrained path). |
| replication.requests.base.timeout | 10s | No | Replication upload/download request timeout. |
| replication.requests.min.throughput | 262144 | No | Expected minimum network speed for replication transfers. Used to expand the timeout and account for network delays. |
| native.async.io.threads | cpuCount | No | The number of async (network) io threads used for replication (and in the future cold storage). The default should be appropriate for most use cases. |
| native.max.blocking.threads | cpuCount \* 4 | No | Maximum number of threads for parallel blocking disk IO read/write operations for replication (and other). These threads are ephemeral: They are spawned per need and shut down after a short duration if no longer in use. These are not cpu-bound threads, hence the relative large number. The default should be appropriate for most use cases. |

For tuning options, see the [Tuning guide](/docs/high-availability/tuning/).

## Snapshot and expiration policies[​](#snapshot-and-expiration-policies "Direct link to Snapshot and expiration policies")

WAL files are typically read by replicas shortly after upload. To optimize
costs, move files to cooler storage tiers after 1-7 days.

**Recommendations:**

* Take snapshots every 1-7 days
* Keep WAL files for at least 30 days
* Ensure snapshot interval is shorter than WAL expiration

Example: Weekly snapshots + 30-day WAL retention = ability to restore up to 23
days back. Daily snapshots restore faster but use more storage.

## Disaster recovery[​](#disaster-recovery "Direct link to Disaster recovery")

### Failure scenarios[​](#failure-scenarios "Direct link to Failure scenarios")

| Node | Recoverable | Unrecoverable |
| --- | --- | --- |
| Primary | Restart | Promote replica, create new replica |
| Replica | Restart | Destroy and recreate |

### Network partitions[​](#network-partitions "Direct link to Network partitions")

Temporary partitions cause replicas to lag, then catch up when connectivity
restores. This is normal operation.

Permanent partitions require [emergency primary migration](#emergency-primary-migration).

### Instance crashes[​](#instance-crashes "Direct link to Instance crashes")

If a crash corrupts transactions, tables may suspend on restart. You can skip
the corrupted transaction and reload missing data, or follow the emergency
migration flow.

### Disk failures[​](#disk-failures "Direct link to Disk failures")

Symptoms: high latency, unmounted disk, suspended tables. Follow the emergency
migration flow to move to new storage.

## Migration procedures[​](#migration-procedures "Direct link to Migration procedures")

### Planned primary migration[​](#planned-primary-migration "Direct link to Planned primary migration")

Use when the current primary is healthy but you want to switch to a new one.

1. Stop the primary
2. Restart with `replication.role=primary-catchup-uploads`
3. Wait for uploads to complete (exits with code 0)
4. Follow emergency migration steps below

### Emergency primary migration[​](#emergency-primary-migration "Direct link to Emergency primary migration")

Use when the primary has failed.

1. Stop the failed primary (ensure it cannot restart)
2. Stop the replica
3. Set `replication.role=primary` on the replica
4. Create an empty `_migrate_primary` file in the installation directory
5. Start the replica (now the new primary)
6. Create a new replica to replace the promoted one

warning

Data committed to the primary but not yet replicated will be lost. Use planned
migration if the primary is still functional.

### Point-in-time recovery[​](#point-in-time-recovery "Direct link to Point-in-time recovery")

Restore the database to a specific historical timestamp.

1. Locate a snapshot from before your target timestamp
2. Create a new instance from the snapshot (do not start it)
3. Create a `_recover_point_in_time` file containing:

   ```prism-code
   replication.object.store=<source object store>  
   replication.recovery.timestamp=YYYY-MM-DDThh:mm:ss.mmmZ
   ```
4. If using a snapshot, create a `_restore` file to trigger recovery
5. Optionally configure `server.conf` to replicate to a **new** object store
6. Start the instance

## Next steps[​](#next-steps "Direct link to Next steps")

* [Tuning guide](/docs/high-availability/tuning/) - Optimize replication
  performance