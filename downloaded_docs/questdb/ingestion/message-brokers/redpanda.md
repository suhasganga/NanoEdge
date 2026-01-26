On this page

[Redpanda](https://redpanda.com/) is an open-source, Kafka-compatible streaming
platform that uses C++ and Raft to replace Java and Zookeeper. Since it is Kafka
compatible, it can be used with the
[QuestDB Kafka connector](/docs/ingestion/message-brokers/kafka/#questdb-kafka-connect-connector),
providing an alternative data [streaming](https://questdb.com/glossary/stream-processing) option.

This guide also covers [Redpanda Connect](#redpanda-connect), a stream processing
tool that can be used to build data pipelines.

### Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Docker
* A local JDK installation
* A running QuestDB instance

### Configure and start Redpanda[​](#configure-and-start-redpanda "Direct link to Configure and start Redpanda")

The Redpanda
[Quick start guide](https://docs.redpanda.com/docs/get-started/quick-start/quick-start-docker/#start-redpanda)
provides a `docker-compose.yaml` file that can be used. Copy and paste the
content into into a file named `docker-compose.yml` on your local filesystem:

docker-compose.yml

```prism-code
---  
version: "3.7"  
name: redpanda-quickstart  
networks:  
  redpanda_network:  
    driver: bridge  
volumes:  
  redpanda-0: null  
services:  
  redpanda-0:  
    command:  
      - redpanda  
      - start  
      - --kafka-addr  
      - internal://0.0.0.0:9092,external://0.0.0.0:19092  
      # use the internal addresses to connect to the Redpanda brokers'  
      # from inside the same Docker network.  
      #  
      # use the external addresses to connect to the Redpanda brokers'  
      # from outside the Docker network.  
      #  
      # address the broker advertises to clients that connect to the Kafka API.  
      - --advertise-kafka-addr  
      - internal://redpanda-0:9092,external://localhost:19092  
      - --pandaproxy-addr  
      - internal://0.0.0.0:8082,external://0.0.0.0:18082  
      # address the broker advertises to clients that connect to PandaProxy.  
      - --advertise-pandaproxy-addr  
      - internal://redpanda-0:8082,external://localhost:18082  
      - --schema-registry-addr  
      - internal://0.0.0.0:8081,external://0.0.0.0:18081  
      # Redpanda brokers use the RPC API to communicate with eachother internally.  
      - --rpc-addr  
      - redpanda-0:33145  
      - --advertise-rpc-addr  
      - redpanda-0:33145  
      # tells Seastar (the framework Redpanda uses under the hood) to use 1 core on the system.  
      - --smp 1  
      # the amount of memory to make available to Redpanda.  
      - --memory 1G  
      # the amount of memory that's left for the Seastar subsystem.  
      # For development purposes this is set to 0.  
      - --reserve-memory 0M  
      # Redpanda won't assume it has all of the provisioned CPU  
      # (to accommodate Docker resource limitations).  
      - --overprovisioned  
      # enable logs for debugging.  
      - --default-log-level=debug  
    image: docker.redpanda.com/vectorized/redpanda:v22.3.11  
    container_name: redpanda-0  
    volumes:  
      - redpanda-0:/var/lib/redpanda/data  
    networks:  
      - redpanda_network  
    ports:  
      - 18081:18081  
      - 18082:18082  
      - 19092:19092  
      - 19644:9644  
  console:  
    container_name: redpanda-console  
    image: docker.redpanda.com/vectorized/console:v2.1.1  
    networks:  
      - redpanda_network  
    entrypoint: /bin/sh  
    command: -c 'echo "$$CONSOLE_CONFIG_FILE" > /tmp/config.yml; /app/console'  
    environment:  
      CONFIG_FILEPATH: /tmp/config.yml  
      CONSOLE_CONFIG_FILE: |  
        kafka:  
          brokers: ["redpanda-0:9092"]  
          schemaRegistry:  
            enabled: true  
            urls: ["http://redpanda-0:8081"]  
        redpanda:  
          adminApi:  
            enabled: true  
            urls: ["http://redpanda-0:9644"]  
    ports:  
      - 8080:8080  
    depends_on:  
      - redpanda-0
```

Once the file is saved, run the following command to start a single Redpanda
broker inside Docker and expose Redpanda to your host machine:

```prism-code
docker compose up
```

It also start the
[Redpanda web UI](https://docs.redpanda.com/docs/get-started/quick-start/quick-start-docker/#explore-your-topic-in-redpanda-console).

### Download Apache Kafka[​](#download-apache-kafka "Direct link to Download Apache Kafka")

Download
[Apache Kafka](https://downloads.apache.org/kafka/3.7.0/kafka_2.12-3.7.0.tgz)
and unzip the file.

This step is required as Redpanda does not have its own Kafka Connect
equivalent.

### Download the QuestDB Kafka connector[​](#download-the-questdb-kafka-connector "Direct link to Download the QuestDB Kafka connector")

Download
[the QuestDB Kafka connector](https://github.com/questdb/kafka-questdb-connector/releases/latest),
under the zip archive named `kafka-questdb-connector-<version>-bin.zip`.

tip

You can automate downloading the latest connector package by running this
command:

```prism-code
curl -s https://api.github.com/repos/questdb/kafka-questdb-connector/releases/latest |  
jq -r '.assets[]|select(.content_type == "application/zip")|.browser_download_url'|  
wget -qi -
```

Unzip the connector - it has a directory with 2 JARs: Copy these JARs into
/path/to/kafka/lib:

```prism-code
unzip kafka-questdb-connector-*-bin.zip  
cd kafka-questdb-connector  
cp ./*.jar /path/to/kafka/libs
```

There should be already a lot of other JAR files. That's how you can tell you
are in the right directory.

### Configure properties[​](#configure-properties "Direct link to Configure properties")

Go to /path/to/kafka/config - there should be already quite a few \*.property
files. Create a new file: `questdb-connector.properties` with the following
lines:

questdb-connector.properties

```prism-code
name=questdb-sink  
connector.class=io.questdb.kafka.QuestDBSinkConnector  
client.conf.string=http::addr=localhost:9000;  
timestamp.kafka.native=true  
topics=example-topic  
table=example_table  
include.key=false  
value.converter=org.apache.kafka.connect.json.JsonConverter  
value.converter.schemas.enable=false  
key.converter=org.apache.kafka.connect.storage.StringConverter
```

In addition, pointing the open `connect-standalone.properties` and replace:

```prism-code
bootstrap.servers=localhost:9092
```

with the Redpanda broker URL:

```prism-code
bootstrap.servers=127.0.0.1:19092
```

### Start Kafka Connect[​](#start-kafka-connect "Direct link to Start Kafka Connect")

Navigate to the Kafka Connect folder and then run:

```prism-code
./bin/connect-standalone.sh config/connect-standalone.properties config/questdb-connector.properties
```

Now the Kafka Connect is initiated.

### Send a message[​](#send-a-message "Direct link to Send a message")

Open the Redpanda UI topic page at `http://127.0.0.1:8080/topics`. It should
display `example-topic`:

![Screenshot of the Redpanda UI showing the example-topic](/docs/assets/images/redpanda-topic-7095711f40c335603fcb03e3957193ac.webp)

If the topic is not there then refresh a few times.

Select `example-topic` to expand more details and click `Actions` -->
`Publish Message`:

![Screenshot of the Redpanda UI highlighting the Actions button](/docs/assets/images/redpanda-actions-a02f6ba7c99068a2192bd9d8b016638c.webp)

Paste the following message into the message box:

```prism-code
{ "firstname": "Arthur", "lastname": "Dent", "age": 42 }
```

![Screenshot of the Redpanda UI add message page](/docs/assets/images/redpanda-add-messsage-1a0ad8eb2cd0254ac6d984b048b788dd.webp)

Then, click 'Publish'.

### See result from QuestDB[​](#see-result-from-questdb "Direct link to See result from QuestDB")

Go to QuestDB web console at `http://localhost:9000`. Run
a `SELECT` query:

```prism-code
SELECT * FROM example_table;
```

The message is delivered to QuestDB:

![QuestDB web console result showing the Redpanda message](/docs/assets/images/questdb-select-6ef0f3d71437e5e5b35aefd8dfc056b5.webp)

### Summary and next steps[​](#summary-and-next-steps "Direct link to Summary and next steps")

The guide demonstrates how to use Redpanda with the QuestDB Kafka connector. The
connector implicitly creates a table in QuestDB with inferred schema from the
Kafka message.

Our connector configuration properties includes a key
`timestamp.kafka.native=true` which tells the connector to use the timestamp
from the Kafka message metadata.

The connector can be also configured to use a custom timestamp field from the
Kafka message. See the
[QuestDB Kafka Connector reference manual](/docs/ingestion/message-brokers/kafka/#designated-timestamps)
for details.

A possible improvement could be to explicitly create the target table in QuestDB
instead of relying on the connector to create it implicitly. This way, you can
control the schema, [partitioning](https://questdb.com/glossary/database-partitioning/) and data
types of the table. It also enables QuestDB's native
[deduplication feature](/docs/concepts/deduplication/). Deduplication is required
for [Exactly-Once](/docs/ingestion/message-brokers/kafka/#fault-tolerance)
processing semantics.

## See also[​](#see-also "Direct link to See also")

* [QuestDB Kafka Connector reference manual](/docs/ingestion/message-brokers/kafka/)

## Redpanda Connect[​](#redpanda-connect "Direct link to Redpanda Connect")

Redpanda Connect is a stream processing tool that can be used to build data pipelines.
It's a lightweight alternative to [Apache Kafka Connect](/docs/ingestion/message-brokers/kafka/#questdb-kafka-connect-connector).
This guide shows the steps to use the Redpanda Connect to write JSON data
as rows into a QuestDB table.

### Prerequisites[​](#prerequisites-1 "Direct link to Prerequisites")

You will need the following:

* [Redpanda Connect](https://docs.redpanda.com/redpanda-connect/about/)
* A running QuestDB instance

### Download Redpanda Connect[​](#download-redpanda-connect "Direct link to Download Redpanda Connect")

The QuestDB output component was added to Redpanda Connect in version v4.37.0.

To download the latest version of Redpanda Connect, follow the [installation instructions](https://docs.redpanda.com/redpanda-connect/guides/getting_started/#install) in the official documentation.

### Configure Redpanda Connect[​](#configure-redpanda-connect "Direct link to Configure Redpanda Connect")

One of Redpanda Connect's strengths is the ability to configure an entire data pipeline in a single
yaml file. We will create a simple configuration to demonstrate the QuestDB connector's capabilities
by using a straightforward input source.

Create this file and name it `config.yaml` in your current directory

```prism-code
input:  
  stdin: {}  
  
output:  
  questdb:  
    address: localhost:9000  
    table: redpanda_connect_demo  
    doubles:  
      - price  
    designated_timestamp_field: timestamp
```

This configuration will read lines from stdin and publish them to your running QuestDB instance

### Run Redpanda Connect and publish messages[​](#run-redpanda-connect-and-publish-messages "Direct link to Run Redpanda Connect and publish messages")

Run the following command to send some messages to QuestDB through Redpanda Connect

```prism-code
echo \  
'{"symbol": "AAPL", "price": 225.83, "timestamp": 1727294094}  
{"symbol": "MSFT", "price": 431.78, "timestamp": 1727294142}' \  
| rpk connect run config.yaml
```

The command above sends two JSON messages to Redpanda Connect standard input, which then writes them to QuestDB.

### Verify the integration[​](#verify-the-integration "Direct link to Verify the integration")

Navigate to the QuestDB Web Console at `http://localhost:9000` and run the following query to see your data:

```prism-code
SELECT *  
FROM redpanda_connect_demo
```

### Next steps[​](#next-steps "Direct link to Next steps")

Explore Redpanda Connect's [official documentation](https://docs.redpanda.com/redpanda-connect/about/) to learn more
about its capabilities and how to use it in your projects.