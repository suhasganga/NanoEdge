On this page

Create histograms with consistent bucket boundaries for distribution analysis. Different approaches suit different data characteristics.

## Problem[​](#problem "Direct link to Problem")

A fixed bucket size works well for some data but poorly for others. For example, a bucket size of 0.5 produces a nice histogram for BTC trade amounts, but may produce just one or two buckets for assets with smaller typical values.

## Solution 1: Fixed bucket size[​](#solution-1-fixed-bucket-size "Direct link to Solution 1: Fixed bucket size")

When you know your data range, use a fixed bucket size:

Histogram with fixed 0.5 buckets[Demo this query](https://demo.questdb.io/?query=DECLARE%20%40bucket_size%20%3A%3D%200.5%0ASELECT%0A%20%20floor(amount%20%2F%20%40bucket_size)%20*%20%40bucket_size%20AS%20bucket%2C%0A%20%20count(*)%20AS%20count%0AFROM%20trades%0AWHERE%20symbol%20%3D%20'BTC-USDT'%20AND%20timestamp%20IN%20today()%0AGROUP%20BY%20bucket%0AORDER%20BY%20bucket%3B&executeQuery=true)

```prism-code
DECLARE @bucket_size := 0.5  
SELECT  
  floor(amount / @bucket_size) * @bucket_size AS bucket,  
  count(*) AS count  
FROM trades  
WHERE symbol = 'BTC-USDT' AND timestamp IN today()  
GROUP BY bucket  
ORDER BY bucket;
```

### How it works[​](#how-it-works "Direct link to How it works")

```prism-code
floor(amount / 0.5) * 0.5
```

1. `amount / 0.5`: Divide by bucket width (1.3 → 2.6)
2. `floor(...)`: Truncate to integer (2.6 → 2)
3. `* 0.5`: Multiply back (2 → 1.0)

Examples:

* 0.3 → floor(0.6) × 0.5 = 0.0
* 1.3 → floor(2.6) × 0.5 = 1.0
* 2.7 → floor(5.4) × 0.5 = 2.5

note

You must tune `@bucket_size` for your data range. A size that works for one symbol may not work for another.

## Solution 2: Fixed bucket count (dynamic size)[​](#solution-2-fixed-bucket-count-dynamic-size "Direct link to Solution 2: Fixed bucket count (dynamic size)")

To always get approximately N buckets regardless of the data range, calculate the bucket size dynamically:

Always ~50 buckets[Demo this query](https://demo.questdb.io/?query=DECLARE%20%40bucket_count%20%3A%3D%2050%0A%0AWITH%20raw_data%20AS%20(%0A%20%20SELECT%20price%2C%20amount%20FROM%20trades%0A%20%20WHERE%20symbol%20%3D%20'BTC-USDT'%20AND%20timestamp%20IN%20today()%0A)%2C%0Abucket_size%20AS%20(%0A%20%20SELECT%20(max(price)%20-%20min(price))%20%2F%20(%40bucket_count%20-%201)%20AS%20bucket_size%20FROM%20raw_data%0A)%0ASELECT%0A%20%20floor(price%20%2F%20bucket_size)%20*%20bucket_size%20AS%20price_bin%2C%0A%20%20round(sum(amount)%2C%202)%20AS%20volume%0AFROM%20raw_data%20CROSS%20JOIN%20bucket_size%0AGROUP%20BY%201%0AORDER%20BY%201%3B&executeQuery=true)

```prism-code
DECLARE @bucket_count := 50  
  
WITH raw_data AS (  
  SELECT price, amount FROM trades  
  WHERE symbol = 'BTC-USDT' AND timestamp IN today()  
),  
bucket_size AS (  
  SELECT (max(price) - min(price)) / (@bucket_count - 1) AS bucket_size FROM raw_data  
)  
SELECT  
  floor(price / bucket_size) * bucket_size AS price_bin,  
  round(sum(amount), 2) AS volume  
FROM raw_data CROSS JOIN bucket_size  
GROUP BY 1  
ORDER BY 1;
```

This calculates `(max - min) / 49` to create 50 evenly distributed buckets. The `CROSS JOIN` makes the calculated bucket\_size available to each row.

tip

If there are fewer distinct values than requested buckets, or if some buckets have no data, you'll get fewer than 50 results.

## Solution 3: Logarithmic buckets[​](#solution-3-logarithmic-buckets "Direct link to Solution 3: Logarithmic buckets")

For data spanning multiple orders of magnitude:

Logarithmic buckets for wide value ranges[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20power(10%2C%20floor(log(amount)))%20AS%20bucket%2C%0A%20%20count(*)%20AS%20count%0AFROM%20trades%0AWHERE%20symbol%20%3D%20'BTC-USDT'%0A%20%20AND%20amount%20%3E%200.000001%20--%20optional.%20Just%20adding%20here%20for%20easier%20visualization%0A%20%20AND%20timestamp%20IN%20today()%0AGROUP%20BY%20bucket%0AORDER%20BY%20bucket%3B&executeQuery=true)

```prism-code
SELECT  
  power(10, floor(log(amount))) AS bucket,  
  count(*) AS count  
FROM trades  
WHERE symbol = 'BTC-USDT'  
  AND amount > 0.000001 -- optional. Just adding here for easier visualization  
  AND timestamp IN today()  
GROUP BY bucket  
ORDER BY bucket;
```

Each bucket covers one order of magnitude (0.001-0.01, 0.01-0.1, 0.1-1.0, etc.).

## Solution 4: Manual buckets[​](#solution-4-manual-buckets "Direct link to Solution 4: Manual buckets")

For simple categorical grouping:

Manual category buckets[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20CASE%0A%20%20%20%20WHEN%20amount%20%3C%200.01%20THEN%20'micro'%0A%20%20%20%20WHEN%20amount%20%3C%200.1%20THEN%20'small'%0A%20%20%20%20WHEN%20amount%20%3C%201.0%20THEN%20'medium'%0A%20%20%20%20ELSE%20'large'%0A%20%20END%20AS%20bucket%2C%0A%20%20count(*)%20AS%20count%0AFROM%20trades%0AWHERE%20symbol%20%3D%20'BTC-USDT'%20AND%20timestamp%20IN%20today()%0AGROUP%20BY%20bucket%3B&executeQuery=true)

```prism-code
SELECT  
  CASE  
    WHEN amount < 0.01 THEN 'micro'  
    WHEN amount < 0.1 THEN 'small'  
    WHEN amount < 1.0 THEN 'medium'  
    ELSE 'large'  
  END AS bucket,  
  count(*) AS count  
FROM trades  
WHERE symbol = 'BTC-USDT' AND timestamp IN today()  
GROUP BY bucket;
```

## Time-series histogram[​](#time-series-histogram "Direct link to Time-series histogram")

Track distribution changes over time by combining with `SAMPLE BY`:

Hourly histogram evolution[Demo this query](https://demo.questdb.io/?query=DECLARE%20%40bucket_size%20%3A%3D%200.5%0ASELECT%0A%20%20timestamp%2C%0A%20%20floor(amount%20%2F%20%40bucket_size)%20*%20%40bucket_size%20AS%20bucket%2C%0A%20%20count(*)%20AS%20count%0AFROM%20trades%0AWHERE%20symbol%20%3D%20'BTC-USDT'%20AND%20timestamp%20IN%20today()%0ASAMPLE%20BY%201h%0AORDER%20BY%20timestamp%2C%20bucket%3B&executeQuery=true)

```prism-code
DECLARE @bucket_size := 0.5  
SELECT  
  timestamp,  
  floor(amount / @bucket_size) * @bucket_size AS bucket,  
  count(*) AS count  
FROM trades  
WHERE symbol = 'BTC-USDT' AND timestamp IN today()  
SAMPLE BY 1h  
ORDER BY timestamp, bucket;
```

Related Documentation

* [Aggregate functions](/docs/query/functions/aggregation/)
* [DECLARE](/docs/query/sql/declare/)
* [SAMPLE BY](/docs/query/sql/sample-by/)