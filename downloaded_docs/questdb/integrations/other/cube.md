On this page

Cube is middleware that connects your data sources and your data applications.
Cube provides an API-first semantic layer for consolidating, caching, and
securing connections. Instead of having independent lines between data stores
and analytics, business or AI tools, Cube consolidates the complexity of overall
data modelling and cross-source data exchange into a cleaner interface.

As a high performance [time-series database](https://questdb.com/glossary/time-series-database/),
QuestDB and Cube are a strong pair. Together, they efficiently bridge your QuestDB
data to one of the many applications and libraries which integrate with Cube.

![A diagram of QuestDB and Cube](/docs/images/guides/cube/questdb-cube-railchart.webp)

## Getting Started[​](#getting-started "Direct link to Getting Started")

This section will help you get QuestDB and Cube running together using Docker.

### Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/)

### Setup[​](#setup "Direct link to Setup")

Create a project directory:

```prism-code
mkdir questdb-cube && cd $_
```

Create a `docker-compose.yml` file:

```prism-code
version: "2.2"  
  
services:  
  cube:  
    environment:  
      - CUBEJS_DEV_MODE=true  
    image: "cubejs/cube:latest"  
    ports:  
      - "4000:4000"  
    env_file: "cube.env"  
    volumes:  
      - ".:/cube/conf"  
  questdb:  
    container_name: questdb  
    hostname: questdb  
    image: "questdb/questdb:latest"  
    ports:  
      - "9000:9000"  
      - "8812:8812"
```

Create a `cube.env` file with connection details:

```prism-code
CUBEJS_DB_HOST=questdb  
CUBEJS_DB_PORT=8812  
CUBEJS_DB_NAME=qdb  
CUBEJS_DB_USER=admin  
CUBEJS_DB_PASS=quest  
CUBEJS_DB_TYPE=questdb
```

Create a `model` directory for Cube and start the containers:

```prism-code
mkdir model  
docker-compose up -d
```

Both applications are now available:

* QuestDB Web Console: `http://localhost:9000`
* Cube Playground: `http://localhost:4000`

## Tutorial: Crypto Price Analytics[​](#tutorial-crypto-price-analytics "Direct link to Tutorial: Crypto Price Analytics")

In this tutorial, we'll build a crypto price analysis pipeline using the
[Kaggle Crypto dataset](https://www.kaggle.com/datasets/sudalairajkumar/cryptocurrencypricehistory)
(requires a free Kaggle account to download).
We'll import data into QuestDB, build a Cube data model, and expose it via APIs.

### Importing Data into QuestDB[​](#importing-data-into-questdb "Direct link to Importing Data into QuestDB")

Navigate to `http://localhost:9000` to open QuestDB's Web Console. Click on the
"Upload" icon on the left-hand panel, and import a
[CSV file from the Kaggle dataset](https://www.kaggle.com/sudalairajkumar/cryptocurrencypricehistory).
This example uses the Ethereum dataset, but any coin dataset will work.

![QuestDB import view](/docs/images/guides/cube/questdb-import-view.webp)

Cube works best with table names that do not contain special characters. Rename
the table:

```prism-code
RENAME TABLE 'coin_Ethereum.csv' TO 'ethereum';
```

![QuestDB web console](/docs/images/guides/cube/questdb-web-console.webp)

You can now query the data:

![QuestDB web console querying ethereum table](/docs/images/guides/cube/ethereum-query.webp)

### Building a Cube Data Model[​](#building-a-cube-data-model "Direct link to Building a Cube Data Model")

The [Cube data model](https://cube.dev/docs/schema/fundamentals/concepts)
consists of entities called 'cubes' that define metrics by dimensions
(qualitative categories) and measures (numerical values).

Navigate to `http://localhost:4000/#/schema` and select the `ethereum` table:

![Generate Schema on Cube](/docs/images/guides/cube/cube-generate-schema.webp)

Click "Generate Data Model" to create a cube in the `model` directory. Open the
generated `Ethereum.js` file and customize it to include price columns:

```prism-code
cube(`Ethereum`, {  
  sql: `SELECT * FROM ethereum`,  
  
  measures: {  
    count: {  
      type: `count`,  
      drillMembers: [name, date],  
    },  
    avgHigh: {  
      type: "avg",  
      sql: `${CUBE}."High"`,  
    },  
    avgLow: {  
      type: "avg",  
      sql: `${CUBE}."Low"`,  
    },  
  },  
  
  dimensions: {  
    name: {  
      sql: `${CUBE}."Name"`,  
      type: `string`,  
    },  
  
    symbol: {  
      sql: `${CUBE}."Symbol"`,  
      type: `string`,  
    },  
  
    date: {  
      sql: `${CUBE}."Date"`,  
      type: `time`,  
    },  
  
    high: {  
      type: "number",  
      sql: `${CUBE}."High"`,  
    },  
  
    low: {  
      type: "number",  
      sql: `${CUBE}."Low"`,  
    },  
  },  
})
```

In the Cube Playground "Build" tab, you can now query and visualize the data:

![Cube build tab](/docs/images/guides/cube/cube-build-tab.webp)

Create a price-over-time chart:

![Price over time graph](/docs/images/guides/cube/price-over-time-graph.webp)

### Pre-aggregations[​](#pre-aggregations "Direct link to Pre-aggregations")

Cube can [pre-aggregate](https://cube.dev/docs/caching/using-pre-aggregations)
data to speed up queries. It creates materialized rollups of specified
dimensions and measures, then uses aggregate awareness logic to route queries to
the most optimal pre-aggregation.

Add a `preAggregations` block to your cube definition in `Ethereum.js`:

```prism-code
cube(`Ethereum`, {  
  sql: `SELECT * FROM ethereum`,  
  
  preAggregations: {  
    main: {  
      measures: [avgHigh, avgLow],  
      timeDimension: date,  
      granularity: "day"  
    }  
  },  
  
  measures: {  
    // ... existing measures  
  },  
  
  dimensions: {  
    // ... existing dimensions  
  },  
})
```

note

QuestDB also supports [materialized views](/docs/concepts/materialized-views/)
that can be used to speed up queries directly at the database level.

### Consuming Data via APIs[​](#consuming-data-via-apis "Direct link to Consuming Data via APIs")

Cube's API-first approach enables you to connect to any data application. API
endpoints ensure that metrics are consistent across different applications,
tools, and teams.

![Various ways to connect with Cube](/docs/images/guides/cube/cube-various-ways-to-connect.webp)

Three API endpoints are available:

1. **REST API**: Connect your application backend via the
   [REST API](https://cube.dev/docs/rest-api).
2. **GraphQL API**: Use standard GraphQL queries for embedded analytics via the
   [GraphQL API](https://cube.dev/docs/backend/graphql).
3. **SQL API**: Query data using standard ANSI SQL via the
   [SQL API](https://cube.dev/docs/backend/sql). This is useful for BI tools,
   dashboards, or data science models.

![GraphQL API](/docs/images/guides/cube/graphql-api.webp)

## See also[​](#see-also "Direct link to See also")

* [Cube documentation](https://cube.dev/docs/)
* [Cube Cloud](https://cube.dev/cloud)
* [QuestDB SQL extensions](/docs/concepts/deep-dive/sql-extensions/)