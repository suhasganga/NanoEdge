On this page

[Databento](/docs/integrations/other/databento/) is a market data aggregator that provides a single,
normalized feed covering multiple venues,
simplifying the process of ingesting live market data.
It interfaces well with QuestDB for real-time data analysis and visualization in Grafana.

This guide will show how to ingest live market data from [Databento](/docs/integrations/other/databento/) into QuestDB and visualize it using Grafana.

For a deeper dive, see our [Databento & QuestDB blog](https://questdb.com/blog/ingesting-live-market-data-data-bento/).

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* [QuestDB](https://questdb.com/download/)
* [Databento Python client](https://pypi.org/project/databento/)
* [QuestDB Python client](/docs/ingestion/clients/python/)
* [Grafana](/docs/integrations/visualization/grafana/) (Optional)

Install the required Python libraries:

```prism-code
pip3 install questdb  
pip3 install databento
```

## Ingest Data from Databento into QuestDB[​](#ingest-data-from-databento-into-questdb "Direct link to Ingest Data from Databento into QuestDB")

### Create Databento Client[​](#create-databento-client "Direct link to Create Databento Client")

Set up a Databento client with your API key:

```prism-code
import databento as db  
  
db_client = db.Live(key="YOUR_API_KEY")
```

### Subscribe to Market Data[​](#subscribe-to-market-data "Direct link to Subscribe to Market Data")

Subscribe to a data feed, such as the CME S&P 500 E-Mini futures:

```prism-code
db_client.subscribe(  
dataset="GLBX.MDP3",  
schema="mbp-1",  
stype_in="raw_symbol",  
symbols="ESM4"  
)
```

### Ingest Data into QuestDB[​](#ingest-data-into-questdb "Direct link to Ingest Data into QuestDB")

Ingest the data into QuestDB using the Sender class:

```prism-code
from questdb.ingress import Sender  
import numpy as np  
  
questdb_conf = "http::addr=localhost:9000;username=admin;password=quest;"  
with Sender.from_conf(questdb_conf) as sender:  
sender.row(  
'top_of_book',  
symbols={'instrument': 'ESM4'},  
columns={'bid_size': record.levels[0].bid_sz,  
'bid': record.levels[0].bid_px*0.000000001,  
'ask': record.levels[0].ask_px*0.000000001,  
'ask_size': record.levels[0].ask_sz},  
at=np.datetime64(record.ts_event, 'ns').astype('datetime64[ms]').astype(object))  
sender.flush()
```

## Query QuestDB[​](#query-questdb "Direct link to Query QuestDB")

Now that data is flowing, you can visit QuestDB at `http://localhost:9000` to try some queries.

Read our [SQL Overview](/docs/query/overview/) to learn more about the power and depth of querying.

## Visualize in Grafana[​](#visualize-in-grafana "Direct link to Visualize in Grafana")

After ingesting the data, you can visualize it in Grafana by creating a dashboard with SQL queries such as:

```prism-code
SELECT timestamp, instrument, bid, ask  
FROM top_of_book  
WHERE $\_\_timeFilter(timestamp) AND instrument = $symbol
```

For more detailed analysis, create multiple charts using Grafana's variable and repeat options.

To learn the basics of QuestDB and Grafana, see [our blog](https://questdb.com/blog/time-series-monitoring-dashboard-grafana-questdb/).

You can substitute the demonstration queries with your own!

## Summary[​](#summary "Direct link to Summary")

In this guide, we set up a pipeline to ingest live market data from Databento into QuestDB and optionally created a visualization using Grafana.
This setup allows you to build powerful dashboards and analyze market data efficiently.

For more information, check out [Databento’s documentation](https://databento.com/docs/).