On this page

[qStudio](https://www.timestored.com/qstudio/) is a free SQL GUI. It allows to
run SQL scripts, browse tables easily, chart and export results.

qStudio includes charting functionality including time-series charting which is
particularly useful with QuestDB. It works on every operating system and with
every database including QuestDB via the PostgreSQL driver.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* A running QuestDB instance (See [Getting Started](/docs/getting-started/quick-start/))

## Configure QuestDB connection[​](#configure-questdb-connection "Direct link to Configure QuestDB connection")

1. [Download qStudio](https://www.timestored.com/qstudio/download) for your OS
2. Launch qStudio
3. Go to `Server` -> `Add Server`
4. Click `Add data source`
5. Choose the `PostgreSQL` plugin and configure it with the following settings:

   ```prism-code
   host:localhost  
   port:8812  
   database:qdb  
   user:admin  
   password:quest
   ```

## Sending Queries[​](#sending-queries "Direct link to Sending Queries")

Run queries with:

* `Ctrl+Enter` to run the current line, or
* `Ctrl+E` to run the highlighted code.

![Screenshot of the qStudio UI running QuestDB query](/docs/images/guides/qstudio/qstudio-query.webp)

Screenshot of the qStudio UI running QuestDB query

## See also[​](#see-also "Direct link to See also")

* [QuestDB Postgres wire protocol](/docs/query/pgwire/overview/)