On this page

Sometimes you need to force a designated timestamp in your query. This happens when you want to run operations like `SAMPLE BY` with a non-designated timestamp column, or when QuestDB applies certain functions or joins and loses track of the designated timestamp.

## Problem: Lost designated timestamp[​](#problem-lost-designated-timestamp "Direct link to Problem: Lost designated timestamp")

When you run this query on the demo instance, you'll notice the `time` column is not recognized as a designated timestamp because we cast it to a string and back:

Query without designated timestamp[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20TO_TIMESTAMP(timestamp%3A%3ASTRING%2C%20'yyyy-MM-ddTHH%3Amm%3Ass.SSSUUUZ')%20time%2C%0A%20%20symbol%2C%0A%20%20ecn%2C%0A%20%20bid_price%0AFROM%0A%20%20core_price%0AWHERE%20timestamp%20IN%20today()%0ALIMIT%2010%3B&executeQuery=true)

```prism-code
SELECT  
  TO_TIMESTAMP(timestamp::STRING, 'yyyy-MM-ddTHH:mm:ss.SSSUUUZ') time,  
  symbol,  
  ecn,  
  bid_price  
FROM  
  core_price  
WHERE timestamp IN today()  
LIMIT 10;
```

Without a designated timestamp, you cannot use time-series operations like `SAMPLE BY`.

## Solution: Use the TIMESTAMP keyword[​](#solution-use-the-timestamp-keyword "Direct link to Solution: Use the TIMESTAMP keyword")

You can force the designated timestamp using the `TIMESTAMP()` keyword, which allows you to run time-series operations:

Force designated timestamp with TIMESTAMP keyword[Demo this query](https://demo.questdb.io/?query=WITH%20t%20AS%20(%0A%20%20(%0A%20%20%20%20SELECT%0A%20%20%20%20%20%20TO_TIMESTAMP(timestamp%3A%3ASTRING%2C%20'yyyy-MM-ddTHH%3Amm%3Ass.SSSUUUZ')%20time%2C%0A%20%20%20%20%20%20symbol%2C%0A%20%20%20%20%20%20ecn%2C%0A%20%20%20%20%20%20bid_price%0A%20%20%20%20FROM%0A%20%20%20%20%20%20core_price%0A%20%20%20%20WHERE%20timestamp%20%3E%3D%20dateadd('h'%2C%20-1%2C%20now())%0A%20%20%20%20ORDER%20BY%20time%0A%20%20)%20TIMESTAMP%20(time)%0A)%0ASELECT%20*%20FROM%20t%20LATEST%20BY%20symbol%3B&executeQuery=true)

```prism-code
WITH t AS (  
  (  
    SELECT  
      TO_TIMESTAMP(timestamp::STRING, 'yyyy-MM-ddTHH:mm:ss.SSSUUUZ') time,  
      symbol,  
      ecn,  
      bid_price  
    FROM  
      core_price  
    WHERE timestamp >= dateadd('h', -1, now())  
    ORDER BY time  
  ) TIMESTAMP (time)  
)  
SELECT * FROM t LATEST BY symbol;
```

The `TIMESTAMP(time)` clause explicitly tells QuestDB which column to use as the designated timestamp, enabling `LATEST BY` and other time-series operations. This query gets the most recent price for each symbol in the last hour.

## Common case: UNION queries[​](#common-case-union-queries "Direct link to Common case: UNION queries")

The designated timestamp is often lost when using `UNION` or `UNION ALL`. This is intentional - QuestDB cannot guarantee that the combined results are in order, and designated timestamps must always be in ascending order.

You can restore the designated timestamp by applying `ORDER BY` and then using `TIMESTAMP()`:

Restore designated timestamp after UNION ALL[Demo this query](https://demo.questdb.io/?query=(%0A%20%20SELECT%20*%20FROM%0A%20%20(%0A%20%20%20%20SELECT%20timestamp%2C%20symbol%20FROM%20core_price%20WHERE%20timestamp%20%3E%3D%20dateadd('m'%2C%20-1%2C%20now())%0A%20%20%20%20UNION%20ALL%0A%20%20%20%20SELECT%20timestamp%2C%20symbol%20FROM%20core_price%20WHERE%20timestamp%20%3E%3D%20dateadd('m'%2C%20-1%2C%20now())%0A%20%20)%20ORDER%20BY%20timestamp%0A)%0ATIMESTAMP(timestamp)%0ALIMIT%2010%3B&executeQuery=true)

```prism-code
(  
  SELECT * FROM  
  (  
    SELECT timestamp, symbol FROM core_price WHERE timestamp >= dateadd('m', -1, now())  
    UNION ALL  
    SELECT timestamp, symbol FROM core_price WHERE timestamp >= dateadd('m', -1, now())  
  ) ORDER BY timestamp  
)  
TIMESTAMP(timestamp)  
LIMIT 10;
```

This query combines the last minute of data twice using `UNION ALL`, then restores the designated timestamp.

## Querying external Parquet files[​](#querying-external-parquet-files "Direct link to Querying external Parquet files")

When querying external parquet files using `read_parquet()`, the result does not have a designated timestamp. You need to force it using `TIMESTAMP()` to enable time-series operations like `SAMPLE BY`:

Query parquet file with designated timestamp[Demo this query](https://demo.questdb.io/?query=SELECT%20timestamp%2C%20avg(price)%0AFROM%20((read_parquet('trades.parquet')%20ORDER%20BY%20timestamp)%20TIMESTAMP(timestamp))%0ASAMPLE%20BY%201m%3B&executeQuery=true)

```prism-code
SELECT timestamp, avg(price)  
FROM ((read_parquet('trades.parquet') ORDER BY timestamp) TIMESTAMP(timestamp))  
SAMPLE BY 1m;
```

This query reads from a parquet file, applies ordering, forces the designated timestamp, and then performs time-series aggregation.

Order is Required

The `TIMESTAMP()` keyword requires that the data is already sorted by the timestamp column. If the data is not in order, the query will fail. Always include `ORDER BY` before applying `TIMESTAMP()`.

Related Documentation

* [Designated Timestamp concept](/docs/concepts/designated-timestamp/)
* [TIMESTAMP keyword reference](/docs/query/sql/select/#timestamp)
* [SAMPLE BY aggregation](/docs/query/sql/sample-by/)
* [Parquet functions](/docs/query/functions/parquet/)