On this page

Calculate multiple aggregates with different conditions in a single pass through the data using CASE expressions.

## Problem[​](#problem "Direct link to Problem")

You need to calculate various metrics from the same dataset with different conditions:

* Count of buy orders
* Count of sell orders
* Average buy price
* Average sell price
* Total volume for large trades (> 1.0)
* Total volume for small trades (≤ 1.0)

Running separate queries is inefficient.

## Solution: CASE within aggregate functions[​](#solution-case-within-aggregate-functions "Direct link to Solution: CASE within aggregate functions")

Use CASE expressions inside aggregates to calculate all metrics in one query:

Multiple conditional aggregates in single query[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20symbol%2C%0A%20%20count(CASE%20WHEN%20side%20%3D%20'buy'%20THEN%201%20END)%20as%20buy_count%2C%0A%20%20count(CASE%20WHEN%20side%20%3D%20'sell'%20THEN%201%20END)%20as%20sell_count%2C%0A%20%20avg(CASE%20WHEN%20side%20%3D%20'buy'%20THEN%20price%20END)%20as%20avg_buy_price%2C%0A%20%20avg(CASE%20WHEN%20side%20%3D%20'sell'%20THEN%20price%20END)%20as%20avg_sell_price%2C%0A%20%20sum(CASE%20WHEN%20amount%20%3E%201.0%20THEN%20amount%20END)%20as%20large_trade_volume%2C%0A%20%20sum(CASE%20WHEN%20amount%20%3C%3D%201.0%20THEN%20amount%20END)%20as%20small_trade_volume%2C%0A%20%20sum(amount)%20as%20total_volume%0AFROM%20trades%0AWHERE%20timestamp%20%3E%3D%20dateadd('d'%2C%20-1%2C%20now())%0A%20%20AND%20symbol%20IN%20('BTC-USDT'%2C%20'ETH-USDT')%0AGROUP%20BY%20symbol%3B&executeQuery=true)

```prism-code
SELECT  
  symbol,  
  count(CASE WHEN side = 'buy' THEN 1 END) as buy_count,  
  count(CASE WHEN side = 'sell' THEN 1 END) as sell_count,  
  avg(CASE WHEN side = 'buy' THEN price END) as avg_buy_price,  
  avg(CASE WHEN side = 'sell' THEN price END) as avg_sell_price,  
  sum(CASE WHEN amount > 1.0 THEN amount END) as large_trade_volume,  
  sum(CASE WHEN amount <= 1.0 THEN amount END) as small_trade_volume,  
  sum(amount) as total_volume  
FROM trades  
WHERE timestamp >= dateadd('d', -1, now())  
  AND symbol IN ('BTC-USDT', 'ETH-USDT')  
GROUP BY symbol;
```

Which returns:

| symbol | buy\_count | sell\_count | avg\_buy\_price | avg\_sell\_price | large\_trade\_volume | small\_trade\_volume | total\_volume |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ETH-USDT | 262870 | 212163 | 3275.286678129868 | 3273.6747631773655 | 152042.02150799974 | 51934.917160999976 | 203976.93866900489 |
| BTC-USDT | 789959 | 712152 | 94286.52121793582 | 94304.92124321847 | 1713.1241887299993 | 8803.505760999722 | 10516.629949730019 |

## How it works[​](#how-it-works "Direct link to How it works")

### CASE returns NULL for non-matching rows[​](#case-returns-null-for-non-matching-rows "Direct link to CASE returns NULL for non-matching rows")

```prism-code
count(CASE WHEN side = 'buy' THEN 1 END)
```

* When `side = 'buy'`: CASE returns 1
* When `side != 'buy'`: CASE returns NULL (implicit ELSE NULL)
* `count()` only counts non-NULL values
* Result: counts only rows where side is 'buy'

### Aggregate functions ignore NULL[​](#aggregate-functions-ignore-null "Direct link to Aggregate functions ignore NULL")

```prism-code
avg(CASE WHEN side = 'buy' THEN price END)
```

* `avg()` calculates average of non-NULL values only
* Only includes price when side is 'buy'
* Automatically skips all other rows

Related Documentation

* [CASE expressions](/docs/query/sql/case/)
* [Aggregate functions](/docs/query/functions/aggregation/)
* [count()](/docs/query/functions/aggregation/#count)