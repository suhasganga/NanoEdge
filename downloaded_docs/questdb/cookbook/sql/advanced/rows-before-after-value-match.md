On this page

Access values from rows before and after the current row to find patterns, detect changes, or provide context around events.

## Problem[​](#problem "Direct link to Problem")

You want to see values from surrounding rows alongside the current row - for example, the 5 previous and 5 next bid prices for each row.

## Solution[​](#solution "Direct link to Solution")

Use `LAG()` to access rows before the current row and `LEAD()` to access rows after:

Access surrounding row values with LAG and LEAD[Demo this query](https://demo.questdb.io/?query=SELECT%20timestamp%2C%20bid_price%2C%0A%20%20LAG(bid_price%2C%201)%20OVER%20()%20AS%20prev_1%2C%0A%20%20LAG(bid_price%2C%202)%20OVER%20()%20AS%20prev_2%2C%0A%20%20LAG(bid_price%2C%203)%20OVER%20()%20AS%20prev_3%2C%0A%20%20LAG(bid_price%2C%204)%20OVER%20()%20AS%20prev_4%2C%0A%20%20LAG(bid_price%2C%205)%20OVER%20()%20AS%20prev_5%2C%0A%20%20LEAD(bid_price%2C%201)%20OVER%20()%20AS%20next_1%2C%0A%20%20LEAD(bid_price%2C%202)%20OVER%20()%20AS%20next_2%2C%0A%20%20LEAD(bid_price%2C%203)%20OVER%20()%20AS%20next_3%2C%0A%20%20LEAD(bid_price%2C%204)%20OVER%20()%20AS%20next_4%2C%0A%20%20LEAD(bid_price%2C%205)%20OVER%20()%20AS%20next_5%0AFROM%20core_price%0AWHERE%20timestamp%20%3E%3D%20dateadd('m'%2C%20-1%2C%20now())%20AND%20symbol%20%3D%20'EURUSD'%3B&executeQuery=true)

```prism-code
SELECT timestamp, bid_price,  
  LAG(bid_price, 1) OVER () AS prev_1,  
  LAG(bid_price, 2) OVER () AS prev_2,  
  LAG(bid_price, 3) OVER () AS prev_3,  
  LAG(bid_price, 4) OVER () AS prev_4,  
  LAG(bid_price, 5) OVER () AS prev_5,  
  LEAD(bid_price, 1) OVER () AS next_1,  
  LEAD(bid_price, 2) OVER () AS next_2,  
  LEAD(bid_price, 3) OVER () AS next_3,  
  LEAD(bid_price, 4) OVER () AS next_4,  
  LEAD(bid_price, 5) OVER () AS next_5  
FROM core_price  
WHERE timestamp >= dateadd('m', -1, now()) AND symbol = 'EURUSD';
```

## How it works[​](#how-it-works "Direct link to How it works")

* **`LAG(column, N)`** - Gets the value from N rows **before** the current row (earlier in time)
* **`LEAD(column, N)`** - Gets the value from N rows **after** the current row (later in time)

Both functions return `NULL` for rows where the offset goes beyond the dataset boundaries (e.g., `LAG(5)` returns `NULL` for the first 5 rows).

Related Documentation

* [LAG window function](/docs/query/functions/window-functions/reference/#lag)
* [LEAD window function](/docs/query/functions/window-functions/reference/#lead)
* [Window functions overview](/docs/query/functions/window-functions/syntax/)