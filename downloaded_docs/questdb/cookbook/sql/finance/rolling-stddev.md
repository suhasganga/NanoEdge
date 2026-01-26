On this page

Calculate rolling standard deviation to measure price volatility over time.

## Problem[​](#problem "Direct link to Problem")

You want to calculate rolling standard deviation.

## Solution[​](#solution "Direct link to Solution")

Use the mathematical identity: `σ = √(E[X²] - E[X]²)`

Compute both `AVG(price)` and `AVG(price * price)` as window functions, then derive the standard deviation:

Calculate rolling standard deviation[Demo this query](https://demo.questdb.io/?query=WITH%20stats%20AS%20(%0A%20%20SELECT%0A%20%20%20%20timestamp%2C%0A%20%20%20%20symbol%2C%0A%20%20%20%20price%2C%0A%20%20%20%20AVG(price)%20OVER%20(PARTITION%20BY%20symbol%20ORDER%20BY%20timestamp)%20AS%20rolling_avg%2C%0A%20%20%20%20AVG(price%20*%20price)%20OVER%20(PARTITION%20BY%20symbol%20ORDER%20BY%20timestamp)%20AS%20rolling_avg_sq%0A%20%20FROM%20fx_trades%0A%20%20WHERE%20timestamp%20IN%20yesterday()%20AND%20symbol%20%3D%20'EURUSD'%0A)%0ASELECT%0A%20%20timestamp%2C%0A%20%20symbol%2C%0A%20%20price%2C%0A%20%20rolling_avg%2C%0A%20%20SQRT(rolling_avg_sq%20-%20rolling_avg%20*%20rolling_avg)%20AS%20rolling_stddev%0AFROM%20stats%0ALIMIT%2010%3B&executeQuery=true)

```prism-code
WITH stats AS (  
  SELECT  
    timestamp,  
    symbol,  
    price,  
    AVG(price) OVER (PARTITION BY symbol ORDER BY timestamp) AS rolling_avg,  
    AVG(price * price) OVER (PARTITION BY symbol ORDER BY timestamp) AS rolling_avg_sq  
  FROM fx_trades  
  WHERE timestamp IN yesterday() AND symbol = 'EURUSD'  
)  
SELECT  
  timestamp,  
  symbol,  
  price,  
  rolling_avg,  
  SQRT(rolling_avg_sq - rolling_avg * rolling_avg) AS rolling_stddev  
FROM stats  
LIMIT 10;
```

## How it works[​](#how-it-works "Direct link to How it works")

The mathematical relationship used here is:

```prism-code
Variance(X) = E[X²] - (E[X])²  
StdDev(X) = √(E[X²] - (E[X])²)
```

Where:

* `E[X]` is the average (SMA) of prices
* `E[X²]` is the average of squared prices
* `√` is the square root function

Related documentation

* [Window functions](/docs/query/functions/window-functions/syntax/)
* [AVG window function](/docs/query/functions/window-functions/reference/#avg)
* [SQRT function](/docs/query/functions/numeric/#sqrt)