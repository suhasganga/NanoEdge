On this page

Detect volume spikes by comparing current trading volume against the previous candle's volume.

## Problem[​](#problem "Direct link to Problem")

You have candles aggregated at 30 seconds intervals, and you want to show a flag 'spike' if volume is bigger than twice the latest record for the same symbol. Otherwise it should display 'normal'.

## Solution[​](#solution "Direct link to Solution")

Use the `LAG` window function to retrieve the previous candle's volume, then compare with a `CASE` statement:

Detect volume spikes exceeding 2x previous volume[Demo this query](https://demo.questdb.io/?query=DECLARE%0A%20%20%40anchor_date%20%3A%3D%20timestamp_floor('30s'%2C%20now())%2C%0A%20%20%40start_date%20%3A%3D%20dateadd('h'%2C%20-7%2C%20%40anchor_date)%2C%0A%20%20%40symbol%20%3A%3D%20'EURUSD'%0AWITH%20candles%20AS%20(%0A%20%20SELECT%0A%20%20%20%20timestamp%2C%0A%20%20%20%20symbol%2C%0A%20%20%20%20sum(quantity)%20AS%20volume%0A%20%20FROM%20fx_trades%0A%20%20WHERE%20timestamp%20%3E%3D%20%40start_date%0A%20%20%20%20AND%20symbol%20%3D%20%40symbol%0A%20%20SAMPLE%20BY%2030s%0A)%2C%0Aprev_volumes%20AS%20(%0A%20%20SELECT%0A%20%20%20%20timestamp%2C%0A%20%20%20%20symbol%2C%0A%20%20%20%20volume%2C%0A%20%20%20%20LAG(volume)%20OVER%20(PARTITION%20BY%20symbol%20ORDER%20BY%20timestamp)%20AS%20prev_volume%0A%20%20FROM%20candles%0A)%0ASELECT%0A%20%20*%2C%0A%20%20CASE%0A%20%20%20%20WHEN%20volume%20%3E%202%20*%20prev_volume%20THEN%20'spike'%0A%20%20%20%20ELSE%20'normal'%0A%20%20END%20AS%20spike_flag%0AFROM%20prev_volumes%3B&executeQuery=true)

```prism-code
DECLARE  
  @anchor_date := timestamp_floor('30s', now()),  
  @start_date := dateadd('h', -7, @anchor_date),  
  @symbol := 'EURUSD'  
WITH candles AS (  
  SELECT  
    timestamp,  
    symbol,  
    sum(quantity) AS volume  
  FROM fx_trades  
  WHERE timestamp >= @start_date  
    AND symbol = @symbol  
  SAMPLE BY 30s  
),  
prev_volumes AS (  
  SELECT  
    timestamp,  
    symbol,  
    volume,  
    LAG(volume) OVER (PARTITION BY symbol ORDER BY timestamp) AS prev_volume  
  FROM candles  
)  
SELECT  
  *,  
  CASE  
    WHEN volume > 2 * prev_volume THEN 'spike'  
    ELSE 'normal'  
  END AS spike_flag  
FROM prev_volumes;
```

Related Documentation

* [LAG window function](/docs/query/functions/window-functions/reference/#lag)
* [SAMPLE BY](/docs/query/sql/sample-by/)
* [CASE expressions](/docs/query/sql/case/)