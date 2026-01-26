On this page

This guide will get your first QuestDB instance running.

As the goal is to, well, *start quickly*, we'll presume defaults.

Once running, we'll provide guides for inserting data, configuration and
production hosting.

> **QuestDB already running? [Jump ahead!](/docs/getting-started/quick-start/#bring-your-data)
> Select a first-party client or ingest method.**

## Install QuestDB[​](#install-questdb "Direct link to Install QuestDB")

Choose from the following options:

* [Docker](#docker)
* [Homebrew](#homebrew)
* [Binaries](#binaries)

### Docker[​](#docker "Direct link to Docker")

To use Docker, one must have Docker. You can find installation guides for your
platform on the [official documentation](https://docs.docker.com/get-docker/).

Once Docker is installed, pull and run QuestDB:

```prism-code
docker run -p 9000:9000 -p 8812:8812 -p 9003:9003 questdb/questdb:9.3.1
```

This exposes the Web Console (9000), PostgreSQL wire (8812), and health endpoint (9003).

For deeper instructions, see the
[Docker deployment guide](/docs/deployment/docker/).

### Homebrew[​](#homebrew "Direct link to Homebrew")

To install QuestDB via [Homebrew](https://brew.sh/), run the following command:

```prism-code
brew install questdb
```

On macOS, the location of the root directory of QuestDB and
[server configuration](/docs/configuration/overview/) files depend on the chip:

* Apple Silicon (M1/M2/M\*) chip: `/opt/homebrew/var/questdb`
* Intel chip: `/usr/local/var/questdb`

### Binaries[​](#binaries "Direct link to Binaries")

Download and run QuestDB via binaries.

Select your platform of choice:

* Linux
* Windows
* Any (no JVM)

Download the binary:   
  
[questdb-9.3.1-rt-linux-x86-64.tar.gz](https://github.com/questdb/questdb/releases/download/9.3.1/questdb-9.3.1-rt-linux-x86-64.tar.gz)  
  
Next, unpack it:   
  

```prism-code
tar -xvf questdb-9.3.1-rt-linux-x86-64.tar.gz
```

The default directory becomes:  
  

```prism-code
$HOME/.questdb
```

Download the executable:    
  
[questdb-9.3.1-rt-windows-x86-64.tar.gz](https://github.com/questdb/questdb/releases/download/9.3.1/questdb-9.3.1-rt-windows-x86-64.tar.gz)  
  
The default root directory becomes:  
  

```prism-code
C:\Windows\System32\qdbroot
```

Download the binary:

[questdb-9.3.1-no-jre-bin.tar.gz](https://github.com/questdb/questdb/releases/download/9.3.1/questdb-9.3.1-no-jre-bin.tar.gz)

This package does not embed Java.

Use this if there is no package for your platform, such as ARM Linux.

Requires local Java 17.

To check your installed version:

```prism-code
java -version
```

If you do not have Java, install one of the following:

* AdoptOpenJDK
* Amazon Corretto
* OpenJDK
* Oracle Java

Other Java distributions might work but are not tested regularly. For example, it is known that Azul Zing 17 is incompatible.

For environment variable, point `JAVA_HOME` to your Java 17 installation folder.

## Run QuestDB[​](#run-questdb "Direct link to Run QuestDB")

* Linux/No JVM
* macOS (Homebrew)
* Windows

```prism-code
./questdb.sh start
```

To stop: `./questdb.sh stop` | To check status: `./questdb.sh status`

All options

```prism-code
./questdb.sh [start|stop|status] [-d dir] [-f] [-n] [-t tag]
```

| Option | Description |
| --- | --- |
| `-d` | Expects a `dir` directory value which is a folder that will be used as QuestDB's root directory. For more information and the default values, see the [default root](/docs/configuration/command-line-options/#default-root-directory-1) section below. |
| `-t` | Expects a `tag` string value which will be as a tag for the service. This option allows users to run several QuestDB services and manage them separately. If this option is omitted, the default tag will be `questdb`. |
| `-f` | Force re-deploying the [Web Console](/docs/getting-started/web-console/overview/). Without this option, the [Web Console](/docs/getting-started/web-console/overview/) is cached and deployed only when missing. |
| `-n` | Do not respond to the HUP signal. This keeps QuestDB alive after you close the terminal window where you started it. |

```prism-code
questdb start
```

To stop: `questdb stop` | To check status: `questdb status`

All options

```prism-code
questdb [start|stop|status] [-d dir] [-f] [-n] [-t tag]
```

| Option | Description |
| --- | --- |
| `-d` | Expects a `dir` directory value which is a folder that will be used as QuestDB's root directory. For more information and the default values, see the [default root](/docs/configuration/command-line-options/#default-root-directory-1) section below. |
| `-t` | Expects a `tag` string value which will be as a tag for the service. This option allows users to run several QuestDB services and manage them separately. If this option is omitted, the default tag will be `questdb`. |
| `-f` | Force re-deploying the [Web Console](/docs/getting-started/web-console/overview/). Without this option, the [Web Console](/docs/getting-started/web-console/overview/) is cached and deployed only when missing. |
| `-n` | Do not respond to the HUP signal. This keeps QuestDB alive after you close the terminal window where you started it. |

```prism-code
questdb.exe start
```

To stop: `questdb.exe stop` | To check status: `questdb.exe status`

All options

```prism-code
questdb.exe [start|stop|status|install|remove] \  
  [-d dir] [-f] [-j JAVA_HOME] [-t tag]
```

| Option | Description |
| --- | --- |
| `install` | Installs the Windows QuestDB service. The service will start automatically at startup. |
| `remove` | Removes the Windows QuestDB service. It will no longer start at startup. |
| `-d` | Expects a `dir` directory value which is a folder that will be used as QuestDB's root directory. For more information and the default values, see the [default root](/docs/configuration/command-line-options/#default-root-directory-1) section below. |
| `-t` | Expects a `tag` string value which will be as a tag for the service. This option allows users to run several QuestDB services and manage them separately. If this option is omitted, the default tag will be `questdb`. |
| `-f` | Force re-deploying the [Web Console](/docs/getting-started/web-console/overview/). Without this option, the [Web Console](/docs/getting-started/web-console/overview/) is cached and deployed only when missing. |
| `-j` | **Windows only!** This option allows to specify a path to `JAVA_HOME`. |

## Verify installation[​](#verify-installation "Direct link to Verify installation")

Open `http://localhost:9000` in your browser.

You should see the QuestDB [Web Console](/docs/getting-started/web-console/overview/).

Try running your first query in the SQL editor:

```prism-code
CREATE TABLE test (ts TIMESTAMP, val DOUBLE) TIMESTAMP(ts);  
INSERT INTO test VALUES (now(), 42.5);  
SELECT * FROM test;
```

It works? You're ready to bring your data.

**Default ports:**

| Port | Service |
| --- | --- |
| `9000` | [REST API](/docs/query/rest-api/) and [Web Console](/docs/getting-started/web-console/overview/) |
| `9009` | [InfluxDB Line Protocol (ILP)](/docs/ingestion/ilp/overview/) - Legacy TCP, use HTTP instead |
| `8812` | [PostgreSQL Wire Protocol](/docs/query/pgwire/overview/) |
| `9003` | [Health endpoint](/docs/operations/logging-metrics/#minimal-http-server) |

## Bring your data[​](#bring-your-data "Direct link to Bring your data")

Now... Time to really blast-off. 🚀

Next up: Bring your data - the *life blood* of any database.

Choose from one of our premium ingest-only language clients:

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

*Want more options? See the [ingestion overview](/docs/ingestion/overview/).*

### Create new data[​](#create-new-data "Direct link to Create new data")

No data yet and still want to trial QuestDB?

There are several quick options:

1. [QuestDB demo instance](https://demo.questdb.io): Hosted, fully loaded and
   ready to go. Quickly explore the Web Console and SQL syntax.
2. [Create my first data set guide](/docs/getting-started/create-database/): create
   tables, use `rnd_` functions and make your own data.
3. [Sample dataset repos](https://github.com/questdb/sample-datasets): IoT,
   e-commerce, finance or git logs? Check them out!
4. [Quick start repos](https://github.com/questdb/questdb-quickstart):
   Code-based quick starts that cover ingestion, querying and data visualization
   using common programming languages and use cases. Also, a cat in a tracksuit.
5. [Time series streaming analytics template](https://github.com/questdb/time-series-streaming-analytics-template):
   A handy template for near real-time analytics using open source technologies.

## Learn QuestDB[​](#learn-questdb "Direct link to Learn QuestDB")

For operators or developers looking for next steps to run an efficient instance,
see:

* **[Capacity planning](/docs/getting-started/capacity-planning/) for recommended
  configurations for operating QuestDB in production**
* [Configuration](/docs/configuration/overview/) to see all of the available options in
  your `server.conf` file
* [Schema design](/docs/schema-design-essentials/) for tips
  and tricks
* [Visualize with Grafana](/docs/integrations/visualization/grafana/) to create useful
  dashboards and visualizations from your data
  + Looking for inspiration? Checkout our
    [real-time crypto dashboard](https://questdb.com/dashboards/crypto/).