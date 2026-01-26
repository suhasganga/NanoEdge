On this page

Remove outlier trades that differ significantly from recent average prices.

## Problem[​](#problem "Direct link to Problem")

You have candle data from trading pairs where some markets have very low volume trades that move the candle significantly. These are usually single trades with very low volume where the exchange rate differs a lot from the actual exchange rate. This makes charts hard to use and you would like to remove those from the chart.

Current query:

Daily OHLC candles[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20%20%20timestamp%2C%20symbol%2C%0A%20%20%20%20first(price)%20AS%20open%2C%0A%20%20%20%20last(price)%20AS%20close%2C%0A%20%20%20%20min(price)%2C%0A%20%20%20%20max(price)%2C%0A%20%20%20%20sum(quantity)%20AS%20volume%0AFROM%20fx_trades%0AWHERE%20symbol%20%3D%20'EURUSD'%20AND%20timestamp%20%3E%20dateadd('d'%2C%20-14%2C%20now())%0ASAMPLE%20BY%201d%3B&executeQuery=true)

```prism-code
SELECT  
    timestamp, symbol,  
    first(price) AS open,  
    last(price) AS close,  
    min(price),  
    max(price),  
    sum(quantity) AS volume  
FROM fx_trades  
WHERE symbol = 'EURUSD' AND timestamp > dateadd('d', -14, now())  
SAMPLE BY 1d;
```

The question is: is there a way to only select trades where the price deviates significantly from recent patterns?

## Solution[​](#solution "Direct link to Solution")

Use a window function to calculate a moving average of price, then filter out trades where the price deviates more than a threshold (e.g., 1%) from the moving average before aggregating with `SAMPLE BY`.

This query excludes trades where price deviates more than 1% from the 7-day moving average:

Filter outliers using 7-day moving average[Demo this query](https://demo.questdb.io/?query=WITH%20moving_trades%20AS%20(%0A%20%20SELECT%20timestamp%2C%20symbol%2C%20price%2C%20quantity%2C%0A%20%20%20%20avg(price)%20OVER%20(%0A%20%20%20%20%20%20PARTITION%20BY%20symbol%0A%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20%20%20RANGE%20BETWEEN%207%20days%20PRECEDING%20AND%201%20day%20PRECEDING%0A%20%20%20%20)%20AS%20moving_avg_price%0A%20%20FROM%20fx_trades%0A%20%20WHERE%20symbol%20%3D%20'EURUSD'%20AND%20timestamp%20%3E%20dateadd('d'%2C%20-21%2C%20now())%0A)%0ASELECT%0A%20%20%20%20timestamp%2C%20symbol%2C%0A%20%20%20%20first(price)%20AS%20open%2C%0A%20%20%20%20last(price)%20AS%20close%2C%0A%20%20%20%20min(price)%2C%0A%20%20%20%20max(price)%2C%0A%20%20%20%20sum(quantity)%20AS%20volume%0AFROM%20moving_trades%0AWHERE%20timestamp%20%3E%20dateadd('d'%2C%20-14%2C%20now())%0A%20%20AND%20moving_avg_price%20IS%20NOT%20NULL%0A%20%20AND%20ABS(price%20-%20moving_avg_price)%20%3C%3D%20moving_avg_price%20*%200.01%0ASAMPLE%20BY%201d%3B&executeQuery=true)

```prism-code
WITH moving_trades AS (  
  SELECT timestamp, symbol, price, quantity,  
    avg(price) OVER (  
      PARTITION BY symbol  
      ORDER BY timestamp  
      RANGE BETWEEN 7 days PRECEDING AND 1 day PRECEDING  
    ) AS moving_avg_price  
  FROM fx_trades  
  WHERE symbol = 'EURUSD' AND timestamp > dateadd('d', -21, now())  
)  
SELECT  
    timestamp, symbol,  
    first(price) AS open,  
    last(price) AS close,  
    min(price),  
    max(price),  
    sum(quantity) AS volume  
FROM moving_trades  
WHERE timestamp > dateadd('d', -14, now())  
  AND moving_avg_price IS NOT NULL  
  AND ABS(price - moving_avg_price) <= moving_avg_price * 0.01  
SAMPLE BY 1d;
```

Moving Average Window

The CTE fetches 21 days of data (7 extra days) so the 7-day moving average window has enough history for the first rows in the 14-day result period.

Related Documentation

* [Window functions](/docs/query/functions/window-functions/syntax/)
* [AVG window function](/docs/query/functions/window-functions/reference/#avg)
* [SAMPLE BY](/docs/query/sql/sample-by/)