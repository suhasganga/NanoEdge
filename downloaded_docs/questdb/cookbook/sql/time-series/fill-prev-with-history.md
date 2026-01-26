On this page

When using `FILL(PREV)` with `SAMPLE BY` on a filtered time interval, gaps at the beginning may have null values because `PREV` only uses values from within the filtered interval. This recipe shows how to carry forward the last known value from before the interval.

## Problem[​](#problem "Direct link to Problem")

When you filter a time range and use `FILL(PREV)` or `FILL(LINEAR)`, QuestDB only considers values within the filtered interval. If the first sample bucket has no data, it will be null instead of carrying forward the last known value from before the interval.

## Solution[​](#solution "Direct link to Solution")

Use a "filler row" by querying the latest value before the filtered interval with `LIMIT -1`, then combine it with your filtered data using `UNION ALL`. The filler row provides the initial value for `FILL(PREV)` to use:

FILL with PREV values carried over last row before the time range in the WHERE[Demo this query](https://demo.questdb.io/?query=DECLARE%0A%20%20%40start_ts%20%3A%3D%20dateadd('s'%2C%20-3%2C%20now())%2C%0A%20%20%40end_ts%20%3A%3D%20now()%0AWITH%0Afiller_row%20AS%20(%0A%20%20SELECT%20timestamp%2C%20open_mid%20AS%20open%2C%20high_mid%20AS%20high%2C%20close_mid%20AS%20close%2C%20low_mid%20AS%20low%0A%20%20FROM%20core_price_1s%0A%20%20WHERE%20timestamp%20%3C%20%40start_ts%0A%20%20LIMIT%20-1%0A)%2C%0Asandwich%20AS%20(%0A%20%20SELECT%20*%20FROM%20(%0A%20%20%20%20SELECT%20*%20FROM%20filler_row%0A%20%20%20%20UNION%20ALL%0A%20%20%20%20SELECT%20timestamp%2C%20open_mid%20AS%20open%2C%20high_mid%20AS%20high%2C%20close_mid%20AS%20close%2C%20low_mid%20AS%20low%0A%20%20%20%20FROM%20core_price_1s%0A%20%20%20%20WHERE%20timestamp%20BETWEEN%20%40start_ts%20AND%20%40end_ts%0A%20%20)%20ORDER%20BY%20timestamp%0A)%2C%0Asampled%20AS%20(%0A%20%20SELECT%0A%20%20%20%20timestamp%2C%0A%20%20%20%20first(open)%20AS%20open%2C%0A%20%20%20%20first(high)%20AS%20high%2C%0A%20%20%20%20first(low)%20AS%20low%2C%0A%20%20%20%20first(close)%20AS%20close%0A%20%20FROM%20sandwich%0A%20%20SAMPLE%20BY%20100T%0A%20%20FILL(PREV%2C%20PREV%2C%20PREV%2C%20PREV%2C%200)%0A)%0ASELECT%20*%20FROM%20sampled%20WHERE%20timestamp%20%3E%3D%20%40start_ts%3B&executeQuery=true)

```prism-code
DECLARE  
  @start_ts := dateadd('s', -3, now()),  
  @end_ts := now()  
WITH  
filler_row AS (  
  SELECT timestamp, open_mid AS open, high_mid AS high, close_mid AS close, low_mid AS low  
  FROM core_price_1s  
  WHERE timestamp < @start_ts  
  LIMIT -1  
),  
sandwich AS (  
  SELECT * FROM (  
    SELECT * FROM filler_row  
    UNION ALL  
    SELECT timestamp, open_mid AS open, high_mid AS high, close_mid AS close, low_mid AS low  
    FROM core_price_1s  
    WHERE timestamp BETWEEN @start_ts AND @end_ts  
  ) ORDER BY timestamp  
),  
sampled AS (  
  SELECT  
    timestamp,  
    first(open) AS open,  
    first(high) AS high,  
    first(low) AS low,  
    first(close) AS close  
  FROM sandwich  
  SAMPLE BY 100T  
  FILL(PREV, PREV, PREV, PREV, 0)  
)  
SELECT * FROM sampled WHERE timestamp >= @start_ts;
```

This query:

1. Gets the latest row before the filtered interval using `LIMIT -1` (last row)
2. Combines it with filtered interval data using `UNION ALL`
3. Applies `SAMPLE BY` with `FILL(PREV)` - the filler row provides initial values
4. Filters results to exclude the filler row, keeping only the requested interval

The filler row ensures that gaps at the beginning of the interval carry forward the last known value rather than showing nulls.

Related Documentation

* [SAMPLE BY aggregation](/docs/query/sql/sample-by/)
* [FILL keyword](/docs/query/sql/sample-by/#fill-options)
* [LIMIT keyword](/docs/query/sql/limit/)