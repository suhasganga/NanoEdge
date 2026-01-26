On this page

Create aggregated results showing the top N items individually, with all remaining items combined into a single "Others" row. This pattern is useful for dashboards and reports where you want to highlight the most important items while still showing the total.

## Problem: Show top items plus remainder[​](#problem-show-top-items-plus-remainder "Direct link to Problem: Show top items plus remainder")

You want to display results like:

| symbol | total\_trades |
| --- | --- |
| BTC-USDT | 15234 |
| ETH-USDT | 12890 |
| SOL-USDT | 8945 |
| MATIC-USDT | 6723 |
| AVAX-USDT | 5891 |
| -Others- | 23456 |

Instead of listing all symbols (which might be thousands), show the top 5 individually and aggregate the rest.

## Solution: Use rank() with CASE statement[​](#solution-use-rank-with-case-statement "Direct link to Solution: Use rank() with CASE statement")

Use `rank()` to identify top N rows, then use `CASE` to group remaining rows:

Top 5 symbols plus Others[Demo this query](https://demo.questdb.io/?query=WITH%20totals%20AS%20(%0A%20%20SELECT%0A%20%20%20%20symbol%2C%0A%20%20%20%20count()%20as%20total%0A%20%20FROM%20trades%0A%20%20WHERE%20timestamp%20%3E%3D%20dateadd('d'%2C%20-1%2C%20now())%0A)%2C%0Aranked%20AS%20(%0A%20%20SELECT%0A%20%20%20%20*%2C%0A%20%20%20%20rank()%20OVER%20(ORDER%20BY%20total%20DESC)%20as%20ranking%0A%20%20FROM%20totals%0A)%0ASELECT%0A%20%20CASE%0A%20%20%20%20WHEN%20ranking%20%3C%3D%205%20THEN%20symbol%0A%20%20%20%20ELSE%20'-Others-'%0A%20%20END%20as%20symbol%2C%0A%20%20SUM(total)%20as%20total_trades%0AFROM%20ranked%0AGROUP%20BY%201%0AORDER%20BY%20total_trades%20DESC%3B&executeQuery=true)

```prism-code
WITH totals AS (  
  SELECT  
    symbol,  
    count() as total  
  FROM trades  
  WHERE timestamp >= dateadd('d', -1, now())  
),  
ranked AS (  
  SELECT  
    *,  
    rank() OVER (ORDER BY total DESC) as ranking  
  FROM totals  
)  
SELECT  
  CASE  
    WHEN ranking <= 5 THEN symbol  
    ELSE '-Others-'  
  END as symbol,  
  SUM(total) as total_trades  
FROM ranked  
GROUP BY 1  
ORDER BY total_trades DESC;
```

**Results:**

| symbol | total\_trades |
| --- | --- |
| BTC-USDT | 15234 |
| ETH-USDT | 12890 |
| SOL-USDT | 8945 |
| MATIC-USDT | 6723 |
| AVAX-USDT | 5891 |
| -Others- | 23456 |

## How it works[​](#how-it-works "Direct link to How it works")

The query uses a three-step approach:

1. **Aggregate data** (`totals` CTE):

   * Count or sum values by the grouping column
   * Creates base data for ranking
2. **Rank rows** (`ranked` CTE):

   * `rank() OVER (ORDER BY total DESC)`: Assigns rank based on count (1 = highest)
   * Ties receive the same rank
3. **Conditional grouping** (outer query):

   * `CASE WHEN ranking <= 5`: Keep top 5 with original names
   * `ELSE '-Others-'`: Rename all others to "-Others-"
   * `SUM(total)`: Aggregate counts (combines all "Others" into one row)
   * `GROUP BY 1`: Group by the CASE expression result

### Understanding rank()[​](#understanding-rank "Direct link to Understanding rank()")

`rank()` assigns ranks with gaps for ties:

| symbol | total | rank |
| --- | --- | --- |
| BTC-USDT | 1000 | 1 |
| ETH-USDT | 900 | 2 |
| SOL-USDT | 900 | 2 |
| AVAX-USDT | 800 | 4 |
| MATIC-USDT | 700 | 5 |

If there are ties at the boundary (rank 5), all tied items will be included in top N.

## Alternative: Using row\_number()[​](#alternative-using-row_number "Direct link to Alternative: Using row_number()")

If you don't want to handle ties and always want exactly N rows in top tier:

Top 5 symbols, discarding extra buckets in case of a match[Demo this query](https://demo.questdb.io/?query=WITH%20totals%20AS%20(%0A%20%20SELECT%20symbol%2C%20count()%20as%20total%0A%20%20FROM%20trades%0A)%2C%0Aranked%20AS%20(%0A%20%20SELECT%20*%2C%20row_number()%20OVER%20(ORDER%20BY%20total%20DESC)%20as%20rn%0A%20%20FROM%20totals%0A)%0ASELECT%0A%20%20CASE%20WHEN%20rn%20%3C%3D%205%20THEN%20symbol%20ELSE%20'-Others-'%20END%20as%20symbol%2C%0A%20%20SUM(total)%20as%20total_trades%0AFROM%20ranked%0AGROUP%20BY%201%0AORDER%20BY%20total_trades%20DESC%3B&executeQuery=true)

```prism-code
WITH totals AS (  
  SELECT symbol, count() as total  
  FROM trades  
),  
ranked AS (  
  SELECT *, row_number() OVER (ORDER BY total DESC) as rn  
  FROM totals  
)  
SELECT  
  CASE WHEN rn <= 5 THEN symbol ELSE '-Others-' END as symbol,  
  SUM(total) as total_trades  
FROM ranked  
GROUP BY 1  
ORDER BY total_trades DESC;
```

**Difference:**

* `rank()`: May include more than N if there are ties at position N
* `row_number()`: Always exactly N in top tier (breaks ties arbitrarily)

## Adapting the pattern[​](#adapting-the-pattern "Direct link to Adapting the pattern")

**Different top N:**

```prism-code
-- Top 10 instead of top 5  
WHEN ranking <= 10 THEN symbol  
  
-- Top 3  
WHEN ranking <= 3 THEN symbol
```

**Different aggregations:**

```prism-code
-- Sum instead of count  
WITH totals AS (  
  SELECT symbol, SUM(amount) as total_volume  
  FROM trades  
)  
...
```

**Multiple levels:**

```prism-code
SELECT  
  CASE  
    WHEN ranking <= 5 THEN symbol  
    WHEN ranking <= 10 THEN '-Top 10-'  
    ELSE '-Others-'  
  END as category,  
  SUM(total) as count  
FROM ranked  
GROUP BY 1;
```

Results in three groups: top 5 individual, ranks 6-10 combined, rest combined.

**With percentage:**

Top 5 symbols with percentage of total[Demo this query](https://demo.questdb.io/?query=WITH%20totals%20AS%20(%0A%20%20SELECT%20symbol%2C%20count()%20as%20total%0A%20%20FROM%20trades%0A%20%20WHERE%20timestamp%20%3E%3D%20dateadd('d'%2C%20-1%2C%20now())%0A)%2C%0Aranked%20AS%20(%0A%20%20SELECT%20*%2C%20rank()%20OVER%20(ORDER%20BY%20total%20DESC)%20as%20ranking%0A%20%20FROM%20totals%0A)%2C%0Asummed%20AS%20(%0A%20%20SELECT%20SUM(total)%20as%20grand_total%20FROM%20totals%0A)%2C%0Agrouped%20AS%20(%0A%20%20SELECT%0A%20%20%20%20CASE%20WHEN%20ranking%20%3C%3D%205%20THEN%20symbol%20ELSE%20'-Others-'%20END%20as%20symbol%2C%0A%20%20%20%20SUM(total)%20as%20total_trades%0A%20%20FROM%20ranked%0A%20%20GROUP%20BY%201%0A)%0ASELECT%0A%20%20symbol%2C%0A%20%20total_trades%2C%0A%20%20round(100.0%20*%20total_trades%20%2F%20grand_total%2C%202)%20as%20percentage%0AFROM%20grouped%20CROSS%20JOIN%20summed%0AORDER%20BY%20total_trades%20DESC%3B&executeQuery=true)

```prism-code
WITH totals AS (  
  SELECT symbol, count() as total  
  FROM trades  
  WHERE timestamp >= dateadd('d', -1, now())  
),  
ranked AS (  
  SELECT *, rank() OVER (ORDER BY total DESC) as ranking  
  FROM totals  
),  
summed AS (  
  SELECT SUM(total) as grand_total FROM totals  
),  
grouped AS (  
  SELECT  
    CASE WHEN ranking <= 5 THEN symbol ELSE '-Others-' END as symbol,  
    SUM(total) as total_trades  
  FROM ranked  
  GROUP BY 1  
)  
SELECT  
  symbol,  
  total_trades,  
  round(100.0 * total_trades / grand_total, 2) as percentage  
FROM grouped CROSS JOIN summed  
ORDER BY total_trades DESC;
```

## Multiple grouping columns[​](#multiple-grouping-columns "Direct link to Multiple grouping columns")

Show top N for multiple dimensions:

Top 3 for each symbol and side[Demo this query](https://demo.questdb.io/?query=WITH%20totals%20AS%20(%0A%20%20SELECT%0A%20%20%20%20symbol%2C%0A%20%20%20%20side%2C%0A%20%20%20%20count()%20as%20total%0A%20%20FROM%20trades%0A%20%20WHERE%20timestamp%20%3E%3D%20dateadd('d'%2C%20-1%2C%20now())%0A)%2C%0Aranked%20AS%20(%0A%20%20SELECT%0A%20%20%20%20*%2C%0A%20%20%20%20rank()%20OVER%20(PARTITION%20BY%20side%20ORDER%20BY%20total%20DESC)%20as%20ranking%0A%20%20FROM%20totals%0A)%0ASELECT%0A%20%20side%2C%0A%20%20CASE%20WHEN%20ranking%20%3C%3D%203%20THEN%20symbol%20ELSE%20'-Others-'%20END%20as%20symbol%2C%0A%20%20SUM(total)%20as%20total_trades%0AFROM%20ranked%0AGROUP%20BY%20side%2C%202%0AORDER%20BY%20side%2C%20total_trades%20DESC%3B&executeQuery=true)

```prism-code
WITH totals AS (  
  SELECT  
    symbol,  
    side,  
    count() as total  
  FROM trades  
  WHERE timestamp >= dateadd('d', -1, now())  
),  
ranked AS (  
  SELECT  
    *,  
    rank() OVER (PARTITION BY side ORDER BY total DESC) as ranking  
  FROM totals  
)  
SELECT  
  side,  
  CASE WHEN ranking <= 3 THEN symbol ELSE '-Others-' END as symbol,  
  SUM(total) as total_trades  
FROM ranked  
GROUP BY side, 2  
ORDER BY side, total_trades DESC;
```

This shows top 3 symbols separately for buy and sell sides.

## Visualization considerations[​](#visualization-considerations "Direct link to Visualization considerations")

This pattern is particularly useful for charts:

**Pie/Donut charts:**

```prism-code
-- Top 5 slices plus "Others" slice  
CASE WHEN ranking <= 5 THEN symbol ELSE '-Others-' END
```

**Bar charts:**

```prism-code
-- Top 10 bars, sorted by value  
CASE WHEN ranking <= 10 THEN symbol ELSE '-Others-' END  
ORDER BY total_trades DESC
```

Empty Others Row

If there are N or fewer distinct values, the "Others" row won't appear (or will have 0 count). Handle this in your visualization logic if needed.

Related Documentation

* [rank() window function](/docs/query/functions/window-functions/reference/#rank)
* [row\_number() window function](/docs/query/functions/window-functions/reference/#row_number)
* [CASE expressions](/docs/query/sql/case/)
* [Window functions](/docs/query/functions/window-functions/syntax/)