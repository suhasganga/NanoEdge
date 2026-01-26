On this page

Use the right interval bound (end of interval) instead of the left bound (start of interval) for SAMPLE BY timestamps.

## Problem[​](#problem "Direct link to Problem")

Records are grouped in a 15-minute interval. For example, records between 2025-03-22T00:00:00.000000Z and 2025-03-22T00:15:00.000000Z are aggregated with timestamp 2025-03-22T00:00:00.000000Z.

You want the aggregation to show 2025-03-22T00:15:00.000000Z (the right bound of the interval rather than left).

## Solution[​](#solution "Direct link to Solution")

Simply shift the timestamp in the SELECT:

SAMPLE BY with right bound[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20%20%20dateadd('m'%2C%2015%2C%20timestamp)%20AS%20timestamp%2C%20symbol%2C%0A%20%20%20%20first(price)%20AS%20open%2C%0A%20%20%20%20last(price)%20AS%20close%2C%0A%20%20%20%20min(price)%2C%0A%20%20%20%20max(price)%2C%0A%20%20%20%20sum(quantity)%20AS%20volume%0AFROM%20fx_trades%0AWHERE%20symbol%20%3D%20'EURUSD'%20AND%20timestamp%20IN%20today()%0ASAMPLE%20BY%2015m%3B&executeQuery=true)

```prism-code
SELECT  
    dateadd('m', 15, timestamp) AS timestamp, symbol,  
    first(price) AS open,  
    last(price) AS close,  
    min(price),  
    max(price),  
    sum(quantity) AS volume  
FROM fx_trades  
WHERE symbol = 'EURUSD' AND timestamp IN today()  
SAMPLE BY 15m;
```

Related Documentation

* [SAMPLE BY](/docs/query/sql/sample-by/)
* [dateadd()](/docs/query/functions/date-time/#dateadd)