On this page

You want to sample data and fill any potential gaps with interpolated values, using a time interval defined by a starting
and ending timestamp, not only between the first and last existing row in the filtered results.

## Problem[​](#problem "Direct link to Problem")

QuestDB has a built-in [`SAMPLE BY .. FROM/TO`](/docs/query/sql/sample-by/#from-to) syntax available for non-keyed queries (queries that include only aggregated columns beyond the timestamp), and for the `NULL` FILL strategy.

If you use `FROM/TO` in a keyed query (for example, an OHLC with timestamp, symbol, and aggregations) you will get the
following error: *FROM-TO intervals are not supported for keyed SAMPLE BY queries*.

## Solution[​](#solution "Direct link to Solution")

"Sandwich" your data by adding artificial boundary rows at the start and end of your time interval using `UNION ALL`. These rows contain your target timestamps with nulls for all other columns. Then you can use `FILL` without the `FROM/TO` keywords and get results
for every sampled interval within those arbitrary dates.

FILL arbitrary interval with keyed SAMPLE BY[Demo this query](https://demo.questdb.io/?query=%0ADECLARE%0A%20%20%40start_ts%20%3A%3D%20dateadd('m'%2C%20-2%2C%20now())%2C%0A%20%20%40end_ts%20%3A%3D%20dateadd('m'%2C%202%2C%20now())%0AWITH%0Asandwich%20AS%20(%0A%20%20SELECT%20*%20FROM%20(%0A%20%20%20%20SELECT%20%40start_ts%20AS%20timestamp%2C%20null%20AS%20symbol%2C%20null%20AS%20open%2C%20null%20AS%20high%2C%20null%20AS%20close%2C%20null%20AS%20low%0A%20%20%20%20UNION%20ALL%0A%20%20%20%20SELECT%20timestamp%2C%20symbol%2C%20open_mid%20AS%20open%2C%20high_mid%20AS%20high%2C%20close_mid%20AS%20close%2C%20low_mid%20AS%20low%0A%20%20%20%20FROM%20core_price_1s%0A%20%20%20%20WHERE%20timestamp%20BETWEEN%20%40start_ts%20AND%20%40end_ts%0A%20%20%20%20UNION%20ALL%0A%20%20%20%20SELECT%20%40end_ts%20AS%20timestamp%2C%20null%20AS%20symbol%2C%20null%20AS%20open%2C%20null%20AS%20high%2C%20null%20AS%20close%2C%20null%20AS%20low%0A%20%20)%20ORDER%20BY%20timestamp%0A)%2C%0Asampled%20AS%20(%0A%20%20SELECT%0A%20%20%20%20timestamp%2C%0A%20%20%20%20symbol%2C%0A%20%20%20%20first(open)%20AS%20open%2C%0A%20%20%20%20first(high)%20AS%20high%2C%0A%20%20%20%20first(low)%20AS%20low%2C%0A%20%20%20%20first(close)%20AS%20close%0A%20%20FROM%20sandwich%0A%20%20SAMPLE%20BY%2030s%0A%20%20FILL(PREV%2C%20PREV%2C%20PREV%2C%20PREV%2C%200)%0A)%0ASELECT%20*%20FROM%20sampled%20WHERE%20open%20IS%20NOT%20NULL%20AND%20symbol%20IN%20('EURUSD'%2C%20'GBPUSD')%3B&executeQuery=true)

```prism-code
DECLARE  
  @start_ts := dateadd('m', -2, now()),  
  @end_ts := dateadd('m', 2, now())  
WITH  
sandwich AS (  
  SELECT * FROM (  
    SELECT @start_ts AS timestamp, null AS symbol, null AS open, null AS high, null AS close, null AS low  
    UNION ALL  
    SELECT timestamp, symbol, open_mid AS open, high_mid AS high, close_mid AS close, low_mid AS low  
    FROM core_price_1s  
    WHERE timestamp BETWEEN @start_ts AND @end_ts  
    UNION ALL  
    SELECT @end_ts AS timestamp, null AS symbol, null AS open, null AS high, null AS close, null AS low  
  ) ORDER BY timestamp  
),  
sampled AS (  
  SELECT  
    timestamp,  
    symbol,  
    first(open) AS open,  
    first(high) AS high,  
    first(low) AS low,  
    first(close) AS close  
  FROM sandwich  
  SAMPLE BY 30s  
  FILL(PREV, PREV, PREV, PREV, 0)  
)  
SELECT * FROM sampled WHERE open IS NOT NULL AND symbol IN ('EURUSD', 'GBPUSD');
```

This query:

1. Creates boundary rows with null values at the start and end timestamps
2. Combines them with filtered data using `UNION ALL`
3. Applies `ORDER BY timestamp` to preserve the designated timestamp
4. Performs `SAMPLE BY` with `FILL` - gaps are filled across the full interval
5. Filters out the artificial boundary rows using `open IS NOT NULL`

The boundary rows ensure that gaps are filled from the beginning to the end of your specified interval, not just between existing data points.

Related Documentation

* [SAMPLE BY aggregation](/docs/query/sql/sample-by/)
* [FILL keyword](/docs/query/sql/sample-by/#fill-options)
* [Designated timestamp](/docs/concepts/designated-timestamp/)