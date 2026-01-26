On this page

Retrieve the most recent N rows for each distinct partition value (e.g., latest 5 trades per symbol, last 10 readings per sensor). While `LATEST ON` returns only the single most recent row per partition, this pattern extends it to get multiple recent rows per partition.

## Problem: Need multiple recent rows per group[​](#problem-need-multiple-recent-rows-per-group "Direct link to Problem: Need multiple recent rows per group")

You want to get the latest N rows for each distinct value in a column. For example:

* Latest 5 trades for each trading symbol
* Last 10 sensor readings per device
* Most recent 3 log entries per service

`LATEST ON` only returns one row per partition:

LATEST ON returns only 1 row per symbol[Demo this query](https://demo.questdb.io/?query=SELECT%20*%20FROM%20trades%0AWHERE%20timestamp%20in%20today()%0ALATEST%20ON%20timestamp%20PARTITION%20BY%20symbol%3B&executeQuery=true)

```prism-code
SELECT * FROM trades  
WHERE timestamp in today()  
LATEST ON timestamp PARTITION BY symbol;
```

But you need multiple rows per symbol.

## Solution: Use ROW\_NUMBER() window function[​](#solution-use-row_number-window-function "Direct link to Solution: Use ROW_NUMBER() window function")

Use `row_number()` to rank rows within each partition, then filter to keep only the top N:

Get latest 5 trades for each symbol[Demo this query](https://demo.questdb.io/?query=WITH%20ranked%20AS%20(%0A%20%20SELECT%0A%20%20%20%20*%2C%0A%20%20%20%20row_number()%20OVER%20(PARTITION%20BY%20symbol%20ORDER%20BY%20timestamp%20DESC)%20as%20rn%0A%20%20FROM%20trades%0A%20%20WHERE%20timestamp%20in%20today()%0A)%0ASELECT%20timestamp%2C%20symbol%2C%20side%2C%20price%2C%20amount%0AFROM%20ranked%0AWHERE%20rn%20%3C%3D%205%0AORDER%20BY%20symbol%2C%20timestamp%20DESC%3B&executeQuery=true)

```prism-code
WITH ranked AS (  
  SELECT  
    *,  
    row_number() OVER (PARTITION BY symbol ORDER BY timestamp DESC) as rn  
  FROM trades  
  WHERE timestamp in today()  
)  
SELECT timestamp, symbol, side, price, amount  
FROM ranked  
WHERE rn <= 5  
ORDER BY symbol, timestamp DESC;
```

This returns up to 5 most recent trades for each symbol from the last day.

## How it works[​](#how-it-works "Direct link to How it works")

The query uses a two-step approach:

1. **Ranking step (CTE):**

   * `row_number() OVER (...)`: Assigns sequential numbers to rows within each partition
   * `PARTITION BY symbol`: Separate ranking for each symbol
   * `ORDER BY timestamp DESC`: Newest rows get lower numbers (1, 2, 3, ...)
   * Result: Each row gets a rank within its symbol group
2. **Filtering step (outer query):**

   * `WHERE rn <= 5`: Keep only rows ranked 1-5 (the 5 most recent)
   * `ORDER BY symbol, timestamp DESC`: Sort final results

### Understanding row\_number()[​](#understanding-row_number "Direct link to Understanding row_number()")

`row_number()` assigns a unique sequential number within each partition:

| timestamp | symbol | price | (row number) |
| --- | --- | --- | --- |
| 10:03:00 | BTC-USDT | 63000 | 1 (newest) |
| 10:02:00 | BTC-USDT | 62900 | 2 |
| 10:01:00 | BTC-USDT | 62800 | 3 |
| 10:03:30 | ETH-USDT | 3100 | 1 (newest) |
| 10:02:30 | ETH-USDT | 3095 | 2 |

With `WHERE rn <= 3`, we keep rows 1-3 for each symbol.

## Adapting the query[​](#adapting-the-query "Direct link to Adapting the query")

**Different partition columns:**

```prism-code
-- Latest 10 per sensor_id  
PARTITION BY sensor_id  
  
-- Latest 5 per combination of symbol and exchange  
PARTITION BY symbol, exchange  
  
-- Latest N per user_id  
PARTITION BY user_id
```

**Different sort orders:**

```prism-code
-- Oldest N rows per partition  
ORDER BY timestamp ASC  
  
-- Highest prices first  
ORDER BY price DESC  
  
-- Alphabetically  
ORDER BY name ASC
```

**Dynamic N value:**

Latest N trades with variable limit[Demo this query](https://demo.questdb.io/?query=DECLARE%20%40limit%20%3A%3D%2010%0A%0AWITH%20ranked%20AS%20(%0A%20%20SELECT%20*%2C%20row_number()%20OVER%20(PARTITION%20BY%20symbol%20ORDER%20BY%20timestamp%20DESC)%20as%20rn%0A%20%20FROM%20trades%0A%20%20WHERE%20timestamp%20%3E%3D%20dateadd('d'%2C%20-1%2C%20now())%0A)%0ASELECT%20*%20FROM%20ranked%20WHERE%20rn%20%3C%3D%20%40limit%3B&executeQuery=true)

```prism-code
DECLARE @limit := 10  
  
WITH ranked AS (  
  SELECT *, row_number() OVER (PARTITION BY symbol ORDER BY timestamp DESC) as rn  
  FROM trades  
  WHERE timestamp >= dateadd('d', -1, now())  
)  
SELECT * FROM ranked WHERE rn <= @limit;
```

**Include additional filtering:**

Latest 5 buy orders per symbol[Demo this query](https://demo.questdb.io/?query=WITH%20ranked%20AS%20(%0A%20%20SELECT%0A%20%20%20%20*%2C%0A%20%20%20%20row_number()%20OVER%20(PARTITION%20BY%20symbol%20ORDER%20BY%20timestamp%20DESC)%20as%20rn%0A%20%20FROM%20trades%0A%20%20WHERE%20timestamp%20in%20today()%0A%20%20%20%20AND%20side%20%3D%20'buy'%20%20--%20Additional%20filter%20before%20ranking%0A)%0ASELECT%20timestamp%2C%20symbol%2C%20side%2C%20price%2C%20amount%0AFROM%20ranked%0AWHERE%20rn%20%3C%3D%205%3B&executeQuery=true)

```prism-code
WITH ranked AS (  
  SELECT  
    *,  
    row_number() OVER (PARTITION BY symbol ORDER BY timestamp DESC) as rn  
  FROM trades  
  WHERE timestamp in today()  
    AND side = 'buy'  -- Additional filter before ranking  
)  
SELECT timestamp, symbol, side, price, amount  
FROM ranked  
WHERE rn <= 5;
```

**Show rank in results:**

Show rank number in results[Demo this query](https://demo.questdb.io/?query=WITH%20ranked%20AS%20(%0A%20%20SELECT%20*%2C%20row_number()%20OVER%20(PARTITION%20BY%20symbol%20ORDER%20BY%20timestamp%20DESC)%20as%20rn%0A%20%20FROM%20trades%0A%20%20WHERE%20timestamp%20in%20today()%0A)%0ASELECT%20timestamp%2C%20symbol%2C%20price%2C%20rn%20as%20rank%0AFROM%20ranked%0AWHERE%20rn%20%3C%3D%205%3B&executeQuery=true)

```prism-code
WITH ranked AS (  
  SELECT *, row_number() OVER (PARTITION BY symbol ORDER BY timestamp DESC) as rn  
  FROM trades  
  WHERE timestamp in today()  
)  
SELECT timestamp, symbol, price, rn as rank  
FROM ranked  
WHERE rn <= 5;
```

## Alternative: Use negative LIMIT[​](#alternative-use-negative-limit "Direct link to Alternative: Use negative LIMIT")

For a simpler approach when you need the latest N rows **total** (not per partition), use negative LIMIT:

Latest 100 trades overall (all symbols)[Demo this query](https://demo.questdb.io/?query=SELECT%20*%20FROM%20trades%0AWHERE%20symbol%20%3D%20'BTC-USDT'%0AORDER%20BY%20timestamp%20DESC%0ALIMIT%20100%3B&executeQuery=true)

```prism-code
SELECT * FROM trades  
WHERE symbol = 'BTC-USDT'  
ORDER BY timestamp DESC  
LIMIT 100;
```

Or more convenient with QuestDB's negative LIMIT feature:

Latest 100 trades using negative LIMIT[Demo this query](https://demo.questdb.io/?query=SELECT%20*%20FROM%20trades%0AWHERE%20symbol%20%3D%20'BTC-USDT'%0ALIMIT%20-100%3B&executeQuery=true)

```prism-code
SELECT * FROM trades  
WHERE symbol = 'BTC-USDT'  
LIMIT -100;
```

**But this doesn't work per partition** - it returns 100 total rows, not 100 per symbol.

## Performance optimization[​](#performance-optimization "Direct link to Performance optimization")

**Filter by timestamp first:**

```prism-code
-- Good: Reduces dataset before windowing  
WITH ranked AS (  
  SELECT *, row_number() OVER (PARTITION BY symbol ORDER BY timestamp DESC) as rn  
  FROM trades  
  WHERE timestamp in today()  -- Filter early  
)  
SELECT * FROM ranked WHERE rn <= 5;  
  
-- Less efficient: Windows over entire table  
WITH ranked AS (  
  SELECT *, row_number() OVER (PARTITION BY symbol ORDER BY timestamp DESC) as rn  
  FROM trades  -- No filter  
)  
SELECT * FROM ranked WHERE rn <= 5 AND timestamp in today();
```

**Limit partitions:**

```prism-code
-- Process only specific symbols  
WHERE timestamp in today()  
  AND symbol IN ('BTC-USDT', 'ETH-USDT', 'SOL-USDT')
```

## Top N with aggregates[​](#top-n-with-aggregates "Direct link to Top N with aggregates")

Combine with aggregates to get summary statistics for top N:

Average price of latest 10 trades per symbol[Demo this query](https://demo.questdb.io/?query=WITH%20ranked%20AS%20(%0A%20%20SELECT%0A%20%20%20%20timestamp%2C%0A%20%20%20%20symbol%2C%0A%20%20%20%20price%2C%0A%20%20%20%20row_number()%20OVER%20(PARTITION%20BY%20symbol%20ORDER%20BY%20timestamp%20DESC)%20as%20rn%0A%20%20FROM%20trades%0A%20%20WHERE%20timestamp%20in%20today()%0A)%0ASELECT%0A%20%20symbol%2C%0A%20%20count(*)%20as%20trade_count%2C%0A%20%20avg(price)%20as%20avg_price%2C%0A%20%20min(price)%20as%20min_price%2C%0A%20%20max(price)%20as%20max_price%0AFROM%20ranked%0AWHERE%20rn%20%3C%3D%2010%0AGROUP%20BY%20symbol%3B&executeQuery=true)

```prism-code
WITH ranked AS (  
  SELECT  
    timestamp,  
    symbol,  
    price,  
    row_number() OVER (PARTITION BY symbol ORDER BY timestamp DESC) as rn  
  FROM trades  
  WHERE timestamp in today()  
)  
SELECT  
  symbol,  
  count(*) as trade_count,  
  avg(price) as avg_price,  
  min(price) as min_price,  
  max(price) as max_price  
FROM ranked  
WHERE rn <= 10  
GROUP BY symbol;
```

## Comparison with LATEST ON[​](#comparison-with-latest-on "Direct link to Comparison with LATEST ON")

| Feature | LATEST ON | row\_number() + Filter |
| --- | --- | --- |
| **Rows per partition** | Exactly 1 | Any number (N) |
| **Performance** | Very fast (optimized) | Moderate (requires ranking) |
| **Flexibility** | Fast | High (custom ordering, filtering) |
| **Use case** | Single latest value | Multiple recent values |

Related Documentation

* [row\_number() window function](/docs/query/functions/window-functions/reference/#row_number)
* [LATEST ON](/docs/query/sql/latest-on/)
* [Window functions](/docs/query/functions/window-functions/syntax/)
* [LIMIT](/docs/query/sql/select/#limit)