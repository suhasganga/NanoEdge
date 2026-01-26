On this page

Calculate volume profile to show the distribution of trading volume across different price levels.

## Solution[​](#solution "Direct link to Solution")

Group trades into price bins using `FLOOR` and a tick size parameter:

Calculate volume profile with fixed tick size[Demo this query](https://demo.questdb.io/?query=DECLARE%20%40tick_size%20%3A%3D%201.0%0ASELECT%0A%20%20floor(price%20%2F%20%40tick_size)%20*%20%40tick_size%20AS%20price_bin%2C%0A%20%20round(SUM(quantity)%2C%202)%20AS%20volume%0AFROM%20fx_trades%0AWHERE%20symbol%20%3D%20'EURUSD'%0A%20%20AND%20timestamp%20IN%20today()%0AORDER%20BY%20price_bin%3B&executeQuery=true)

```prism-code
DECLARE @tick_size := 1.0  
SELECT  
  floor(price / @tick_size) * @tick_size AS price_bin,  
  round(SUM(quantity), 2) AS volume  
FROM fx_trades  
WHERE symbol = 'EURUSD'  
  AND timestamp IN today()  
ORDER BY price_bin;
```

Since QuestDB does an implicit GROUP BY on all non-aggregated columns, you can omit the explicit GROUP BY clause.

## Dynamic tick size[​](#dynamic-tick-size "Direct link to Dynamic tick size")

For consistent histograms across different price ranges, calculate the tick size dynamically to always produce approximately 50 bins:

Volume profile with dynamic 50-bin distribution[Demo this query](https://demo.questdb.io/?query=WITH%20raw_data%20AS%20(%0A%20%20SELECT%20price%2C%20quantity%0A%20%20FROM%20fx_trades%0A%20%20WHERE%20symbol%20%3D%20'EURUSD'%20AND%20timestamp%20IN%20today()%0A)%2C%0Atick_size%20AS%20(%0A%20%20SELECT%20(max(price)%20-%20min(price))%20%2F%2049%20as%20tick_size%0A%20%20FROM%20raw_data%0A)%0ASELECT%0A%20%20floor(price%20%2F%20tick_size)%20*%20tick_size%20AS%20price_bin%2C%0A%20%20round(SUM(quantity)%2C%202)%20AS%20volume%0AFROM%20raw_data%20CROSS%20JOIN%20tick_size%0AORDER%20BY%201%3B&executeQuery=true)

```prism-code
WITH raw_data AS (  
  SELECT price, quantity  
  FROM fx_trades  
  WHERE symbol = 'EURUSD' AND timestamp IN today()  
),  
tick_size AS (  
  SELECT (max(price) - min(price)) / 49 as tick_size  
  FROM raw_data  
)  
SELECT  
  floor(price / tick_size) * tick_size AS price_bin,  
  round(SUM(quantity), 2) AS volume  
FROM raw_data CROSS JOIN tick_size  
ORDER BY 1;
```

This will produce a histogram with a maximum of 50 buckets. If you have enough price difference between the first and last price for the interval, and if there are enough events with different prices, then you will get the full 50 buckets. If price difference is too small or if there are buckets with no events, then you might get less than 50.

Related Documentation

* [FLOOR function](/docs/query/functions/numeric/#floor)
* [SUM aggregate](/docs/query/functions/aggregation/#sum)
* [DECLARE variables](/docs/query/sql/declare/)
* [CROSS JOIN](/docs/query/sql/join/#cross-join)