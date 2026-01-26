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

### Google Compute Engine with Google Cloud Hyperdisk[​](#google-compute-engine-with-google-cloud-hyperdisk "Direct link to Google Compute Engine with Google Cloud Hyperdisk")

Google Compute Engine offers a variety of VM instances tuned for different workloads.

Do **not** use instances containing the letter `A`, such as `C4A`. These are `ARM` architecture instances,
using Axion processors.

Either `AMD EPYC` CPUs (`D` letter) or `Intel Xeon` (no letter) are appropriate for `x86_64` deployments.

We recommend starting with `C-Series` instances, and reviewing other instance types if your workload demands it.

You should deploy using an `x86_64` Linux distribution, such as Ubuntu.

For storage, we recommend using [Hyperdisk Balanced](https://cloud.google.com/compute/docs/disks/hyperdisks) disks,
and provisioning them at `5000 IOPS/300 MBps` until you have tested your workload.

`Hyperdisk Extreme` generally requires much higher `vCPU` counts - for example, it cannot be used on `C3` machines
smaller than `88 vCPUs`.

For the file system, use `zfs` with `lz4`, as this will compress your data. If compression
is not a concern, then use `ext4` or `xfs` for a little higher performance.

### Google Filestore[​](#google-filestore "Direct link to Google Filestore")

Google Filestore is a `NAS` solution offering an `NFS` API to talk to arbitrary volumes.

This should **not** be used as primary storage for QuestDB. It could be used for replication in QuestDB Enterprise,
but `Google Cloud Storage` is likely simpler and cheaper to use.

### Google Cloud Storage[​](#google-cloud-storage "Direct link to Google Cloud Storage")

QuestDB supports `Google Cloud Storage` as its replication object-store in the Enterprise edition.

To get started, create a bucket for the database to use. Then follow the
[Enterprise Quick Start](/docs/getting-started/enterprise-quick-start/) steps to create a connection string and
configure QuestDB.

### Minimum specification[​](#minimum-specification "Direct link to Minimum specification")

* **Instance**: `c3-standard-4` or `c3d-standard-4` `(4 vCPUs, 16 GB RAM)`
* **Storage**
  + **OS disk**: `Hyperdisk Balanced (30 GiB)` volume provisioned with `3000 IOPS/140 MBps`.
  + **Data disk**: `Hyperdisk Balanced (100 GiB)` volume provisioned with `3000 IOPS/140 MBps`.
* **Operating System**: `Linux Ubuntu 24.04 LTS x86_64`.
* **File System**: `ext4`

### Better specification[​](#better-specification "Direct link to Better specification")

* **Instance**: `c3-highmem-8` or `c3d-highmem-8` `(8 vCPUs, 64 GB RAM)`
* **Storage**
  + **OS disk**: `Hyperdisk Balanced (30 GiB)` volume provisioned with `5000 IOPS/300 MBps`.
  + **Data disk**: `Hyperdisk Balanced (300 GiB)` volume provisioned with `5000 IOPS/300 MBps`.
* **Operating System**: `Linux Ubuntu 24.04 LTS x86_64`.
* **File System**: `zfs`

note

You can use the `highcpu` and `highmem` variants to adjust the `standard` `4:1` RAM/vCPU
ratio to `2:1` or `8:1` respectively. Higher RAM can improve performance dramatically
if it means your working set data will fit entirely into memory.

## Launching QuestDB on Google Compute Engine[​](#launching-questdb-on-google-compute-engine "Direct link to Launching QuestDB on Google Compute Engine")

This guide describes how to run QuestDB on a new Google Cloud Platform (GCP)
Compute Engine instance. After completing this guide, you will have an instance
with QuestDB running in a container using the official QuestDB Docker image, as
well as a network rule that enables communication over HTTP and PostgreSQL wire
protocol.

### Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* A [Google Cloud Platform](https://console.cloud.google.com/getting-started)
  (GCP) account and a GCP Project
* The
  [Compute Engine API](https://console.cloud.google.com/apis/api/compute.googleapis.com)
  must be enabled for the corresponding Google Cloud Platform project

### Create a Compute Engine VM[​](#create-a-compute-engine-vm "Direct link to Create a Compute Engine VM")

1. In the Google Cloud Console, navigate to
   [Compute Engine](https://console.cloud.google.com/compute/instances) and
   click **Create Instance**

![The Create Instance wizard on Google Cloud platform](/docs/images/guides/google-cloud-platform/create-instance.webp)

2. Give the instance a name - this example uses `questdb-europe-west3`
3. Choose a **Region** and **Zone** where you want to deploy the instance - this
   example uses `europe-west3 (Frankfurt)` and the default zone
4. Choose a machine configuration. The default choice, `ec2-medium`, is a
   general-purpose instance with 4GB memory and should be enough to run this
   example.

    

   ![Deploying a QuestDB instance on Google Cloud Platform Compute Engine](/docs/images/guides/google-cloud-platform/create-vm.webp)
5. To add a running QuestDB container on instance startup, scroll down and click
   the **Deploy Container** button. Then, provide the `latest` QuestDB Docker
   image in the **Container image** textbox.

   ```prism-code
   questdb/questdb:latest
   ```

   Click the **Select** button at the bottom of the dropdown to complete the
   container configuration.

   Your docker configuration should look like this:

    

   ![Configuring a Docker container to launch in a new QuestDB instance on Google Cloud Platform Compute Engine](/docs/images/guides/google-cloud-platform/create-vm-docker.webp)

Before creating the instance, we need to assign it a **Network tag** so that we
can add a firewall rule that exposes QuestDB-related ports to the internet. This
is required for you to access the database from outside your VPC. To create a
**Network tag**:

1. Expand the **Advanced options** menu below the **firewall** section, and then
   expand the **Networking** panel
2. In the **Networking** panel add a **Network tag** to identify the instance.
   This example uses `questdb`

![Applying a Network tag to a Compute Engine VM Instance on Google Cloud Platform](/docs/images/guides/google-cloud-platform/add-network-tag.webp)

You can now launch the instance by clicking **Create** at the bottom of the
dialog.

### Create a firewall rule[​](#create-a-firewall-rule "Direct link to Create a firewall rule")

Now that we've created our instance with a `questdb` network tag, we need to
create a corresponding firewall rule to associate with that tag. This rule will
expose the required ports for accessing QuestDB. With a network tag, we can
easily apply the new firewall rule to our newly created instance as well as any
other QuestDB instances that we create in the future.

1. Navigate to the
   [Firewall configuration](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies)
   page under **Network Security** -> **Firewall policies**
2. Click the **Create firewall rule** button at the top of the page
3. Enter `questdb` in the **Name** field
4. Scroll down to the **Targets** dropdown and select "Specified target tags"
5. Enter `questdb` in the **Target tags** textbox. This will apply the firewall
   rule to the new instance that was created above
6. Under **Source filter**, enter an IP range that this rule applies to. This
   example uses `0.0.0.0/0`, which allows ingress from any IP address. We
   recommend that you make this rule more restrictive, and naturally that you
   include your current IP address within the chosen range.
7. In the **Protocols and ports** section, select **Specified protocols and
   ports**, check the **TCP** option, and type `8812,9000` in the textbox.
8. Scroll down and click the **Create** button

![Creating a firewall rule in for VPC networking on Google Cloud Platform](/docs/images/guides/google-cloud-platform/firewall-rules.webp)

All VM instances on Compute Engine in this account which have the **Network
tag** `questdb` will now have this firewall rule applied.

The ports we have opened are:

* `9000` for the REST API and [Web Console](/docs/getting-started/web-console/overview/)
* `8812` for the PostgreSQL wire protocol

## Verify the deployment[​](#verify-the-deployment "Direct link to Verify the deployment")

To verify that the instance is running, navigate to **Compute Engine** ->
[VM Instances](https://console.cloud.google.com/compute/instances). A status
indicator should show the instance as **running**:

![A QuestDB instance running on Google Cloud Platform showing a success status indicator](/docs/images/guides/google-cloud-platform/instance-available.webp)

To verify that the QuestDB deployment is operating as expected:

1. Copy the **External IP** of the instance
2. Navigate to `http://<external_ip>:9000` in a browser

The [Web Console](/docs/getting-started/web-console/overview/) should now be visible:

![The QuestDB Web Console running on a VM instance on Google Cloud Platform](/docs/images/guides/google-cloud-platform/gcp-portal.webp)

Alternatively, a request may be sent to the REST API exposed on port 9000:

```prism-code
curl -G \  
  --data-urlencode "query=SELECT * FROM telemetry_config" \  
  <external_ip>:9000/exec
```

### Set up GCP with Pulumi[​](#set-up-gcp-with-pulumi "Direct link to Set up GCP with Pulumi")

If you're using [Pulumi](https://www.pulumi.com/gcp/) to manage your
infrastructure, you can create a QuestDB instance with the following:

```prism-code
import pulumi  
import pulumi_gcp as gcp  
  
# Create a Google Cloud Network  
firewall = gcp.compute.Firewall(  
    "questdb-firewall",  
    network="default",  
    allows=[  
        gcp.compute.FirewallAllowArgs(  
            protocol="tcp",  
            ports=["9000", "8812"],  
        ),  
    ],  
    target_tags=["questdb"],  
    source_ranges=["0.0.0.0/0"],  
)  
  
# Create a Compute Engine Instance  
instance = gcp.compute.Instance(  
    "questdb-instance",  
    machine_type="e2-medium",  
    zone="us-central1-a",  
    boot_disk={  
        "initialize_params": {  
            "image": "ubuntu-os-cloud/ubuntu-2004-lts",  
        },  
    },  
    network_interfaces=[  
        gcp.compute.InstanceNetworkInterfaceArgs(  
            network="default",  
            access_configs=[{}],  # Ephemeral public IP  
        )  
    ],  
    metadata_startup_script="""#!/bin/bash  
        sudo apt-get update  
        sudo apt-get install -y docker.io  
        sudo docker run -d -p 9000:9000 -p 8812:8812 \  
        --env QDB_HTTP_USER="admin" \  
        --env QDB_HTTP_PASSWORD="quest" \  
        questdb/questdb  
        """,  
    tags=["questdb"],  
)  
  
# Export the instance's name and public IP  
pulumi.export("instanceName", instance.name)  
pulumi.export("instance_ip", instance.network_interfaces[0].access_configs[0].nat_ip)
```