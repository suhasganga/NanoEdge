On this page

Calculate Bollinger Bands for volatility analysis and mean reversion trading. Bollinger Bands consist of a moving average with upper and lower bands set at a specified number of standard deviations above and below it. They help identify overbought/oversold conditions and measure market volatility.

## Solution: Calculate variance using window functions[​](#solution-calculate-variance-using-window-functions "Direct link to Solution: Calculate variance using window functions")

Since standard deviation is the square root of variance, and variance is the average of squared differences from the mean,
we can calculate everything in SQL using window functions. This query will compute Bollinger Bands with a 20-period
simple moving average (SMA) and bands at ±2 standard deviations:

Calculate Bollinger Bands with 20-period SMA[Demo this query](https://demo.questdb.io/?query=WITH%20OHLC%20AS%20(%0A%20%20SELECT%0A%20%20%20%20timestamp%2C%20symbol%2C%0A%20%20%20%20%20%20first(price)%20AS%20open%2C%0A%20%20%20%20%20%20max(price)%20as%20high%2C%0A%20%20%20%20%20%20min(price)%20as%20low%2C%0A%20%20%20%20%20%20last(price)%20AS%20close%2C%0A%20%20%20%20%20%20sum(quantity)%20AS%20volume%0A%20FROM%20fx_trades%0A%20WHERE%20symbol%20%3D%20'EURUSD'%20AND%20timestamp%20IN%20yesterday()%0A%20SAMPLE%20BY%2015m%0A)%2C%20stats%20AS%20(%0A%20%20SELECT%0A%20%20%20%20timestamp%2C%0A%20%20%20%20close%2C%0A%20%20%20%20AVG(close)%20OVER%20(%0A%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20%20%20ROWS%2019%20PRECEDING%0A%20%20%20%20)%20AS%20sma20%2C%0A%20%20%20%20AVG(close%20*%20close)%20OVER%20(%0A%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20%20%20ROWS%2019%20PRECEDING%0A%20%20%20%20)%20AS%20avg_close_sq%0A%20%20FROM%20OHLC%0A)%0ASELECT%0A%20%20timestamp%2C%0A%20%20close%2C%0A%20%20sma20%2C%0A%20%20sqrt(avg_close_sq%20-%20(sma20%20*%20sma20))%20as%20stdev20%2C%0A%20%20sma20%20%2B%202%20*%20sqrt(avg_close_sq%20-%20(sma20%20*%20sma20))%20as%20upper_band%2C%0A%20%20sma20%20-%202%20*%20sqrt(avg_close_sq%20-%20(sma20%20*%20sma20))%20as%20lower_band%0AFROM%20stats%0AORDER%20BY%20timestamp%3B&executeQuery=true)

```prism-code
WITH OHLC AS (  
  SELECT  
    timestamp, symbol,  
      first(price) AS open,  
      max(price) as high,  
      min(price) as low,  
      last(price) AS close,  
      sum(quantity) AS volume  
 FROM fx_trades  
 WHERE symbol = 'EURUSD' AND timestamp IN yesterday()  
 SAMPLE BY 15m  
), stats AS (  
  SELECT  
    timestamp,  
    close,  
    AVG(close) OVER (  
      ORDER BY timestamp  
      ROWS 19 PRECEDING  
    ) AS sma20,  
    AVG(close * close) OVER (  
      ORDER BY timestamp  
      ROWS 19 PRECEDING  
    ) AS avg_close_sq  
  FROM OHLC  
)  
SELECT  
  timestamp,  
  close,  
  sma20,  
  sqrt(avg_close_sq - (sma20 * sma20)) as stdev20,  
  sma20 + 2 * sqrt(avg_close_sq - (sma20 * sma20)) as upper_band,  
  sma20 - 2 * sqrt(avg_close_sq - (sma20 * sma20)) as lower_band  
FROM stats  
ORDER BY timestamp;
```

This query:

1. Aggregates trades into 15-minute OHLC candles
2. Calculates a 20-period simple moving average of closing prices
3. Calculates the average of squared closing prices over the same 20-period window
4. Computes standard deviation using the mathematical identity: `σ = √(E[X²] - E[X]²)`
5. Adds/subtracts 2× standard deviation to create upper and lower bands

## How it works[​](#how-it-works "Direct link to How it works")

The core of the Bollinger Bands calculation is the rolling standard deviation. Please check our
[rolling standard deviation recipe](/docs/cookbook/sql/finance/rolling-stddev/) in the cookbook for an explanation about the mathematical formula.

## Adapting the parameters[​](#adapting-the-parameters "Direct link to Adapting the parameters")

**Different period lengths:**

```prism-code
-- 10-period Bollinger Bands (change 19 to 9)  
AVG(close) OVER (ORDER BY timestamp ROWS 9 PRECEDING) AS sma10,  
AVG(close * close) OVER (ORDER BY timestamp ROWS 9 PRECEDING) AS avg_close_sq
```

**Different band multipliers:**

```prism-code
-- 1 standard deviation bands (tighter)  
sma20 + 1 * sqrt(avg_close_sq - (sma20 * sma20)) as upper_band,  
sma20 - 1 * sqrt(avg_close_sq - (sma20 * sma20)) as lower_band  
  
-- 3 standard deviation bands (wider)  
sma20 + 3 * sqrt(avg_close_sq - (sma20 * sma20)) as upper_band,  
sma20 - 3 * sqrt(avg_close_sq - (sma20 * sma20)) as lower_band
```

**Different time intervals:**

```prism-code
-- 5-minute candles  
SAMPLE BY 5m  
  
-- 1-hour candles  
SAMPLE BY 1h
```

**Multiple symbols:**

Bollinger Bands for multiple symbols[Demo this query](https://demo.questdb.io/?query=WITH%20OHLC%20AS%20(%0A%20%20SELECT%0A%20%20%20%20timestamp%2C%20symbol%2C%0A%20%20%20%20%20%20first(price)%20AS%20open%2C%0A%20%20%20%20%20%20last(price)%20AS%20close%2C%0A%20%20%20%20%20%20sum(quantity)%20AS%20volume%0A%20FROM%20fx_trades%0A%20WHERE%20symbol%20IN%20('EURUSD'%2C%20'GBPUSD')%0A%20%20%20AND%20timestamp%20IN%20yesterday()%0A%20SAMPLE%20BY%2015m%0A)%2C%20stats%20AS%20(%0A%20%20SELECT%0A%20%20%20%20timestamp%2C%0A%20%20%20%20symbol%2C%0A%20%20%20%20close%2C%0A%20%20%20%20AVG(close)%20OVER%20(%0A%20%20%20%20%20%20PARTITION%20BY%20symbol%0A%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20%20%20ROWS%2019%20PRECEDING%0A%20%20%20%20)%20AS%20sma20%2C%0A%20%20%20%20AVG(close%20*%20close)%20OVER%20(%0A%20%20%20%20%20%20PARTITION%20BY%20symbol%0A%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20%20%20ROWS%2019%20PRECEDING%0A%20%20%20%20)%20AS%20avg_close_sq%0A%20%20FROM%20OHLC%0A)%0ASELECT%0A%20%20timestamp%2C%0A%20%20symbol%2C%0A%20%20close%2C%0A%20%20sma20%2C%0A%20%20sma20%20%2B%202%20*%20sqrt(avg_close_sq%20-%20(sma20%20*%20sma20))%20as%20upper_band%2C%0A%20%20sma20%20-%202%20*%20sqrt(avg_close_sq%20-%20(sma20%20*%20sma20))%20as%20lower_band%0AFROM%20stats%0AORDER%20BY%20symbol%2C%20timestamp%3B&executeQuery=true)

```prism-code
WITH OHLC AS (  
  SELECT  
    timestamp, symbol,  
      first(price) AS open,  
      last(price) AS close,  
      sum(quantity) AS volume  
 FROM fx_trades  
 WHERE symbol IN ('EURUSD', 'GBPUSD')  
   AND timestamp IN yesterday()  
 SAMPLE BY 15m  
), stats AS (  
  SELECT  
    timestamp,  
    symbol,  
    close,  
    AVG(close) OVER (  
      PARTITION BY symbol  
      ORDER BY timestamp  
      ROWS 19 PRECEDING  
    ) AS sma20,  
    AVG(close * close) OVER (  
      PARTITION BY symbol  
      ORDER BY timestamp  
      ROWS 19 PRECEDING  
    ) AS avg_close_sq  
  FROM OHLC  
)  
SELECT  
  timestamp,  
  symbol,  
  close,  
  sma20,  
  sma20 + 2 * sqrt(avg_close_sq - (sma20 * sma20)) as upper_band,  
  sma20 - 2 * sqrt(avg_close_sq - (sma20 * sma20)) as lower_band  
FROM stats  
ORDER BY symbol, timestamp;
```

Note the addition of `PARTITION BY symbol` to calculate separate Bollinger Bands for each symbol.

Related Documentation

* [Window functions](/docs/query/functions/window-functions/syntax/)
* [AVG window function](/docs/query/functions/window-functions/reference/#avg)
* [SQRT function](/docs/query/functions/numeric/#sqrt)
* [Window frame clauses](/docs/query/functions/window-functions/syntax/#frame-types-and-behavior)