On this page

[Apache Flink](https://flink.apache.org/) is a popular framework and
[stream processing](https://questdb.com/glossary/stream-processing) engine. QuestDB ships a
[QuestDB Flink Sink connector](https://github.com/questdb/flink-questdb-connector)
for fast ingestion from Apache Flink into QuestDB. The connector implements the
[Table API and SQL](https://nightlies.apache.org/flink/flink-docs-release-1.16/docs/dev/table/overview/)
for Flink.

![Apache Flink logo](/docs/assets/images/flink-c07b4f947c1cde3356cdb19fa674ce56.svg)

## Quick start[​](#quick-start "Direct link to Quick start")

This section shows the steps to use the QuestDB Flink connector to ingest data
from Flink into QuestDB. The connector uses the SQL interface to interact with
Flink. The overall steps are the followings:

1. The connector creates a table in Flink backed by QuestDB.
2. The connector inserts data into the table.
3. Finally it queries the data in QuestDB.

### Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* A local JDK version 11 installation
* Docker for running QuestDB

### Connector installation[​](#connector-installation "Direct link to Connector installation")

* Start the QuestDB container image:

  ```prism-code
  docker run -p 9000:9000 -p 9009:9009 questdb/questdb:9.3.1
  ```
* Download [Apache Flink distribution](https://flink.apache.org/downloads/) and
  unpack it.
* [Download](https://repo1.maven.org/maven2/org/questdb/flink-questdb-connector/0.2/flink-questdb-connector-0.2.jar)
  the QuestDB Flink connector from Maven Central and place it in the `lib`
  directory of your Flink installation.
* Go to the `bin` directory of your Flink installation and run the following to
  start a Flink cluster:

  ```prism-code
  ./start-cluster.sh
  ```
* While still in the `bin` directory, start a Flink SQL console by running:

  ```prism-code
  ./sql-client.sh
  ```

  Then, run the following SQL command in the Flink SQL console:

  ```prism-code
  CREATE TABLE Orders (  
    order_number BIGINT,  
    price        BIGINT,  
     buyer        STRING  
    ) WITH (  
    'connector'='questdb',  
    'host'='localhost'  
    );
  ```

  Expected output: `[INFO] Execute statement succeed.`

  This command created a Flink table backed by QuestDB. The table is called
  `Orders` and has three columns: `order_number`, `price`, and `buyer`. The
  `connector` option specifies the QuestDB Flink connector. The `host` option
  specifies the host and port where QuestDB is running. The default port is
  `9009`.
* While still in the Flink SQL console execute:

  ```prism-code
  INSERT INTO Orders values (0, 42, 'IBM');
  ```

  Expected output:

  ```prism-code
  [INFO] SQL update statement has been successfully submitted to the cluster:  
  Job ID: <random hexadecimal id>
  ```

  This command used Flink SQL to insert a row into the `Orders` table in Flink.
  The table is connected to QuestDB, so the row is also into QuestDB.
* Go to the QuestDB [Web Console](/docs/getting-started/web-console/overview/) at `http://localhost:9000`
  and execute this query:

  ```prism-code
  SELECT * FROM Orders;
  ```

  You should see a table with one row.

  ![QuestDB web console screenshot with the query result](/docs/assets/images/flink-questdb-console-374ad37cc8c9d0f70dbc8c6752e395bc.webp)

Congratulations! You have successfully used the QuestDB Flink connector to
ingest data from Flink into QuestDB. You can now build Flink data pipelines that
use QuestDB as a sink.

See the
[QuestDB Flink connector GitHub repository](https://github.com/questdb/flink-questdb-connector/tree/main/samples)
for more examples.

## Configuration[​](#configuration "Direct link to Configuration")

The QuestDB Flink connector supports the following configuration options:

| Name | Type | Example | Default | Meaning |
| --- | --- | --- | --- | --- |
| host | `string` | localhost:9009 | N/A | Host and port where QuestDB server is running |
| username | `string` | testUser1 | admin | Username for authentication. The default is used when also `token` is set. |
| token | `string` | GwBXoGG5c6NoUTLXnzMxw | admin | Token for authentication |
| table | `string` | my\_table | Same as Flink table name | Target table in QuestDB |
| tls | `boolean` | true | false | Whether to use TLS/SSL for connecting to QuestDB server |
| buffer.size.kb | `integer` | 32 | 64 | Size of the QuestDB client send buffer |
| sink.parallelism | `integer` | 2 | Same as upstream processors | QuestDB Sink Parallelism |

Example configuration for connecting to QuestDB running on localhost:

```prism-code
CREATE TABLE Orders (  
     order_number BIGINT,  
     price        BIGINT,  
     buyer        STRING  
 ) WITH (  
   'connector'='questdb',  
   'host'='localhost',  
   'table' = 'orders'  
);
```

## Connector Distribution[​](#connector-distribution "Direct link to Connector Distribution")

The connector is distributed as a single jar file. The jar file is available in
the
[Maven Central repository](https://repo1.maven.org/maven2/org/questdb/flink-questdb-connector/)
and it's available under the following coordinates:

```prism-code
<dependency>  
  <groupId>org.questdb</groupId>  
  <artifactId>flink-questdb-connector</artifactId>  
  <version>LATEST</version>  
</dependency>
```

## FAQ[​](#faq "Direct link to FAQ")

Q: Why is QuestDB client not repackaged into a different Java package?  
 A:
QuestDB client uses native code, this makes repackaging hard.

Q: I need to use QuestDB as a Flink source, what should I do?  
 A: This
connector is Sink only. If you want to use QuestDB as a Source then your best
chance is to use
[Flink JDBC source](https://nightlies.apache.org/flink/flink-docs-release-1.15/docs/connectors/table/jdbc/)
and rely on
[QuestDB Postgres compatibility](/docs/query/overview/#postgresql).