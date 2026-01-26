On this page

Find the minimum and maximum values within a time window around each row to detect local peaks, troughs, or price ranges.

## Problem[​](#problem "Direct link to Problem")

You want to find the local minimum and maximum bid price within a time range of each row - for example, the min/max within 1 second before and after each data point.

## Solution 1: Window function (past only)[​](#solution-1-window-function-past-only "Direct link to Solution 1: Window function (past only)")

If you only need to look at **past data**, use a window function with `RANGE`:

Local min/max from preceding 1 second[Demo this query](https://demo.questdb.io/?query=SELECT%20timestamp%2C%20bid_price%2C%0A%20%20min(bid_price)%20OVER%20(ORDER%20BY%20timestamp%20RANGE%201%20second%20PRECEDING)%20AS%20min_price%2C%0A%20%20max(bid_price)%20OVER%20(ORDER%20BY%20timestamp%20RANGE%201%20second%20PRECEDING)%20AS%20max_price%0AFROM%20core_price%0AWHERE%20timestamp%20%3E%3D%20dateadd('m'%2C%20-1%2C%20now())%20AND%20symbol%20%3D%20'EURUSD'%3B&executeQuery=true)

```prism-code
SELECT timestamp, bid_price,  
  min(bid_price) OVER (ORDER BY timestamp RANGE 1 second PRECEDING) AS min_price,  
  max(bid_price) OVER (ORDER BY timestamp RANGE 1 second PRECEDING) AS max_price  
FROM core_price  
WHERE timestamp >= dateadd('m', -1, now()) AND symbol = 'EURUSD';
```

This returns the minimum and maximum bid price from the 1 second preceding each row.

## Solution 2: WINDOW JOIN (past and future)[​](#solution-2-window-join-past-and-future "Direct link to Solution 2: WINDOW JOIN (past and future)")

If you need to look at **both past and future data**, use a `WINDOW JOIN`. QuestDB window functions don't support `FOLLOWING`, but WINDOW JOIN allows bidirectional lookback:

Local min/max from 1 second before and after[Demo this query](https://demo.questdb.io/?query=SELECT%20p.timestamp%2C%20p.bid_price%2C%0A%20%20min(pp.bid_price)%20AS%20min_price%2C%0A%20%20max(pp.bid_price)%20AS%20max_price%0AFROM%20core_price%20p%0AWINDOW%20JOIN%20core_price%20pp%20ON%20symbol%0A%20%20RANGE%20BETWEEN%201%20second%20PRECEDING%20AND%201%20second%20FOLLOWING%0AWHERE%20p.timestamp%20%3E%3D%20dateadd('m'%2C%20-1%2C%20now())%20AND%20p.symbol%20%3D%20'EURUSD'%3B&executeQuery=true)

```prism-code
SELECT p.timestamp, p.bid_price,  
  min(pp.bid_price) AS min_price,  
  max(pp.bid_price) AS max_price  
FROM core_price p  
WINDOW JOIN core_price pp ON symbol  
  RANGE BETWEEN 1 second PRECEDING AND 1 second FOLLOWING  
WHERE p.timestamp >= dateadd('m', -1, now()) AND p.symbol = 'EURUSD';
```

This returns the minimum and maximum bid price from 1 second before to 1 second after each row.

## When to use each approach[​](#when-to-use-each-approach "Direct link to When to use each approach")

| Approach | Use When |
| --- | --- |
| Window function | You only need to look at past data |
| WINDOW JOIN | You need to look at both past and future data |

Related Documentation

* [Window functions](/docs/query/functions/window-functions/syntax/)
* [WINDOW JOIN](/docs/query/sql/window-join/)
* [MIN/MAX aggregate functions](/docs/query/functions/aggregation/#min)