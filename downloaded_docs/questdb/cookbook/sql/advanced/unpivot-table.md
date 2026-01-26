On this page

Transform wide-format data (multiple columns) into long format (rows) using UNION ALL.

## Problem: Wide format to long format[​](#problem-wide-format-to-long-format "Direct link to Problem: Wide format to long format")

You have query results with multiple columns where only one column has a value per row:

**Wide format (sparse):**

| timestamp | symbol | buy | sell |
| --- | --- | --- | --- |
| 08:10:00 | ETH-USDT | NULL | 3678.25 |
| 08:10:00 | ETH-USDT | NULL | 3678.25 |
| 08:10:00 | ETH-USDT | 3678.01 | NULL |
| 08:10:00 | ETH-USDT | NULL | 3678.00 |

You want to convert this to a format where side and price are explicit:

**Long format (dense):**

| timestamp | symbol | side | price |
| --- | --- | --- | --- |
| 08:10:00 | ETH-USDT | sell | 3678.25 |
| 08:10:00 | ETH-USDT | sell | 3678.25 |
| 08:10:00 | ETH-USDT | buy | 3678.01 |
| 08:10:00 | ETH-USDT | sell | 3678.00 |

## Solution: UNION ALL with literal values[​](#solution-union-all-with-literal-values "Direct link to Solution: UNION ALL with literal values")

Use UNION ALL to stack columns as rows, then filter NULL values:

UNPIVOT buy/sell columns to side/price rows[Demo this query](https://demo.questdb.io/?query=WITH%20pivoted%20AS%20(%0A%20%20SELECT%0A%20%20%20%20timestamp%2C%0A%20%20%20%20symbol%2C%0A%20%20%20%20CASE%20WHEN%20side%20%3D%20'buy'%20THEN%20price%20END%20as%20buy%2C%0A%20%20%20%20CASE%20WHEN%20side%20%3D%20'sell'%20THEN%20price%20END%20as%20sell%0A%20%20FROM%20trades%0A%20%20WHERE%20timestamp%20%3E%3D%20dateadd('m'%2C%20-5%2C%20now())%0A%20%20%20%20AND%20symbol%20%3D%20'ETH-USDT'%0A)%2C%0Aunpivoted%20AS%20(%0A%20%20SELECT%20timestamp%2C%20symbol%2C%20'buy'%20as%20side%2C%20buy%20as%20price%0A%20%20FROM%20pivoted%0A%0A%20%20UNION%20ALL%0A%0A%20%20SELECT%20timestamp%2C%20symbol%2C%20'sell'%20as%20side%2C%20sell%20as%20price%0A%20%20FROM%20pivoted%0A)%0ASELECT%20*%20FROM%20unpivoted%0AWHERE%20price%20IS%20NOT%20NULL%0AORDER%20BY%20timestamp%3B&executeQuery=true)

```prism-code
WITH pivoted AS (  
  SELECT  
    timestamp,  
    symbol,  
    CASE WHEN side = 'buy' THEN price END as buy,  
    CASE WHEN side = 'sell' THEN price END as sell  
  FROM trades  
  WHERE timestamp >= dateadd('m', -5, now())  
    AND symbol = 'ETH-USDT'  
),  
unpivoted AS (  
  SELECT timestamp, symbol, 'buy' as side, buy as price  
  FROM pivoted  
  
  UNION ALL  
  
  SELECT timestamp, symbol, 'sell' as side, sell as price  
  FROM pivoted  
)  
SELECT * FROM unpivoted  
WHERE price IS NOT NULL  
ORDER BY timestamp;
```

**Results:**

| timestamp | symbol | side | price |
| --- | --- | --- | --- |
| 08:10:00 | ETH-USDT | sell | 3678.25 |
| 08:10:00 | ETH-USDT | sell | 3678.25 |
| 08:10:00 | ETH-USDT | buy | 3678.01 |
| 08:10:00 | ETH-USDT | sell | 3678.00 |

## How it works[​](#how-it-works "Direct link to How it works")

### Step 1: Create wide format (if needed)[​](#step-1-create-wide-format-if-needed "Direct link to Step 1: Create wide format (if needed)")

If your data is already in narrow format, you may need to pivot first:

```prism-code
CASE WHEN side = 'buy' THEN price END as buy,  
CASE WHEN side = 'sell' THEN price END as sell
```

This creates NULL values for the opposite side.

### Step 2: UNION ALL[​](#step-2-union-all "Direct link to Step 2: UNION ALL")

```prism-code
SELECT timestamp, symbol, 'buy' as side, buy as price FROM pivoted  
UNION ALL  
SELECT timestamp, symbol, 'sell' as side, sell as price FROM pivoted
```

This creates two copies of every row:

* First copy: Has 'buy' literal with buy column value
* Second copy: Has 'sell' literal with sell column value

### Step 3: Filter NULLs[​](#step-3-filter-nulls "Direct link to Step 3: Filter NULLs")

```prism-code
WHERE price IS NOT NULL
```

Removes rows where the price column is NULL (the opposite side).

## Unpivoting multiple columns[​](#unpivoting-multiple-columns "Direct link to Unpivoting multiple columns")

Transform multiple numeric columns to name-value pairs:

UNPIVOT sensor readings

```prism-code
WITH sensor_data AS (  
  SELECT  
    timestamp,  
    sensor_id,  
    temperature,  
    humidity,  
    pressure  
  FROM sensors  
  WHERE timestamp >= dateadd('h', -1, now())  
)  
SELECT timestamp, sensor_id, 'temperature' as metric, temperature as value FROM sensor_data  
WHERE temperature IS NOT NULL  
  
UNION ALL  
  
SELECT timestamp, sensor_id, 'humidity' as metric, humidity as value FROM sensor_data  
WHERE humidity IS NOT NULL  
  
UNION ALL  
  
SELECT timestamp, sensor_id, 'pressure' as metric, pressure as value FROM sensor_data  
WHERE pressure IS NOT NULL  
  
ORDER BY timestamp, sensor_id, metric;
```

**Results:**

| timestamp | sensor\_id | metric | value |
| --- | --- | --- | --- |
| 10:00:00 | S001 | humidity | 65.2 |
| 10:00:00 | S001 | pressure | 1013.2 |
| 10:00:00 | S001 | temperature | 22.5 |

## Performance considerations[​](#performance-considerations "Direct link to Performance considerations")

**UNION ALL vs UNION:**

```prism-code
-- Fast: UNION ALL (no deduplication)  
SELECT ... UNION ALL SELECT ...  
  
-- Slower: UNION (deduplicates rows)  
SELECT ... UNION SELECT ...
```

Always use `UNION ALL` for unpivoting unless you specifically need deduplication.

Related Documentation

* [UNION](/docs/query/sql/union-except-intersect/)
* [CASE expressions](/docs/query/sql/case/)
* [Pivoting (opposite operation)](/docs/query/sql/pivot/)
* [Pivoting with an 'Others' column](/docs/cookbook/sql/advanced/pivot-with-others/)