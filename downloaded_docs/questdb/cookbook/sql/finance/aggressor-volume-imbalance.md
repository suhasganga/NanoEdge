On this page

Calculate the imbalance between buy and sell aggressor volume to analyze order flow. The aggressor is the party that initiated the trade by crossing the spread.

## Problem: Measure order flow imbalance[​](#problem-measure-order-flow-imbalance "Direct link to Problem: Measure order flow imbalance")

You have trade data with a `side` column indicating the aggressor (buyer or seller), and want to measure the imbalance between buying and selling pressure.

## Solution: Aggregate by side and calculate ratios[​](#solution-aggregate-by-side-and-calculate-ratios "Direct link to Solution: Aggregate by side and calculate ratios")

Aggressor volume imbalance per symbol[Demo this query](https://demo.questdb.io/?query=WITH%20volumes%20AS%20(%0A%20%20SELECT%0A%20%20%20%20symbol%2C%0A%20%20%20%20SUM(CASE%20WHEN%20side%20%3D%20'buy'%20THEN%20amount%20ELSE%200%20END)%20AS%20buy_volume%2C%0A%20%20%20%20SUM(CASE%20WHEN%20side%20%3D%20'sell'%20THEN%20amount%20ELSE%200%20END)%20AS%20sell_volume%0A%20%20FROM%20trades%0A%20%20WHERE%20timestamp%20IN%20yesterday()%0A%20%20%20%20AND%20symbol%20IN%20('ETH-USDT'%2C%20'BTC-USDT'%2C%20'ETH-BTC')%0A)%0ASELECT%0A%20%20symbol%2C%0A%20%20buy_volume%2C%0A%20%20sell_volume%2C%0A%20%20((buy_volume%20-%20sell_volume)%3A%3Adouble%20%2F%20(buy_volume%20%2B%20sell_volume))%20*%20100%20AS%20imbalance%0AFROM%20volumes%3B&executeQuery=true)

```prism-code
WITH volumes AS (  
  SELECT  
    symbol,  
    SUM(CASE WHEN side = 'buy' THEN amount ELSE 0 END) AS buy_volume,  
    SUM(CASE WHEN side = 'sell' THEN amount ELSE 0 END) AS sell_volume  
  FROM trades  
  WHERE timestamp IN yesterday()  
    AND symbol IN ('ETH-USDT', 'BTC-USDT', 'ETH-BTC')  
)  
SELECT  
  symbol,  
  buy_volume,  
  sell_volume,  
  ((buy_volume - sell_volume)::double / (buy_volume + sell_volume)) * 100 AS imbalance  
FROM volumes;
```

The imbalance ranges from -100% (all sell) to +100% (all buy), with 0% indicating balanced flow.

Related documentation

* [CASE expressions](/docs/query/sql/case/)
* [Aggregation functions](/docs/query/functions/aggregation/)