On this page

Fill missing intervals using the previous value from a specific column to populate multiple columns.

## Problem[​](#problem "Direct link to Problem")

You have a query like this:

SAMPLE BY with FILL(PREV)[Demo this query](https://demo.questdb.io/?query=SELECT%20timestamp%2C%20symbol%2C%20avg(bid_price)%20as%20bid_price%2C%20avg(ask_price)%20as%20ask_price%0AFROM%20core_price%0AWHERE%20symbol%20%3D%20'EURUSD'%20AND%20timestamp%20IN%20today()%0ASAMPLE%20BY%20100T%20FILL(PREV%2C%20PREV)%3B&executeQuery=true)

```prism-code
SELECT timestamp, symbol, avg(bid_price) as bid_price, avg(ask_price) as ask_price  
FROM core_price  
WHERE symbol = 'EURUSD' AND timestamp IN today()  
SAMPLE BY 100T FILL(PREV, PREV);
```

But when there is an interpolation, instead of getting the PREV value for `bid_price` and previous for `ask_price`, you want both prices to show the PREV known value for the `ask_price`. Imagine this SQL was valid:

```prism-code
SELECT timestamp, symbol, avg(bid_price) as bid_price, avg(ask_price) as ask_price  
FROM core_price  
WHERE symbol = 'EURUSD' AND timestamp IN today()  
SAMPLE BY 100T FILL(PREV(ask_price), PREV);
```

## Solution[​](#solution "Direct link to Solution")

The only way to do this is in multiple steps within a single query: first get the sampled data interpolating with null values, then use a window function to get the last non-null value for the reference column, and finally coalesce the missing columns with this filler value.

Fill bid and ask prices with value from ask price[Demo this query](https://demo.questdb.io/?query=WITH%20sampled%20AS%20(%0A%20%20SELECT%20timestamp%2C%20symbol%2C%20avg(bid_price)%20as%20bid_price%2C%20avg(ask_price)%20as%20ask_price%0A%20%20FROM%20core_price%0A%20%20WHERE%20symbol%20%3D%20'EURUSD'%20AND%20timestamp%20IN%20today()%0A%20%20SAMPLE%20BY%20100T%20FILL(null)%0A)%2C%20with_previous_vals%20AS%20(%0A%20%20SELECT%20*%2C%0A%20%20%20%20last_value(ask_price)%20IGNORE%20NULLS%20OVER(PARTITION%20BY%20symbol%20ORDER%20BY%20timestamp)%20as%20filler%0A%20%20FROM%20sampled%0A)%0ASELECT%20timestamp%2C%20symbol%2C%20coalesce(bid_price%2C%20filler)%20as%20bid_price%2C%0A%20%20%20%20%20%20%20coalesce(ask_price%2C%20filler)%20as%20ask_price%0AFROM%20with_previous_vals%3B&executeQuery=true)

```prism-code
WITH sampled AS (  
  SELECT timestamp, symbol, avg(bid_price) as bid_price, avg(ask_price) as ask_price  
  FROM core_price  
  WHERE symbol = 'EURUSD' AND timestamp IN today()  
  SAMPLE BY 100T FILL(null)  
), with_previous_vals AS (  
  SELECT *,  
    last_value(ask_price) IGNORE NULLS OVER(PARTITION BY symbol ORDER BY timestamp) as filler  
  FROM sampled  
)  
SELECT timestamp, symbol, coalesce(bid_price, filler) as bid_price,  
       coalesce(ask_price, filler) as ask_price  
FROM with_previous_vals;
```

Note the use of `IGNORE NULLS` modifier on the window function to make sure we always look back for a value, rather than just over the previous row.

You can mark which rows were filled by adding a column that flags interpolated values:

Show which rows were filled[Demo this query](https://demo.questdb.io/?query=WITH%20sampled%20AS%20(%0A%20%20SELECT%20timestamp%2C%20symbol%2C%20avg(bid_price)%20as%20bid_price%2C%20avg(ask_price)%20as%20ask_price%0A%20%20FROM%20core_price%0A%20%20WHERE%20symbol%20%3D%20'EURUSD'%20AND%20timestamp%20IN%20today()%0A%20%20SAMPLE%20BY%20100T%20FILL(null)%0A)%2C%20with_previous_vals%20AS%20(%0A%20%20SELECT%20*%2C%0A%20%20%20%20last_value(ask_price)%20IGNORE%20NULLS%20OVER(PARTITION%20BY%20symbol%20ORDER%20BY%20timestamp)%20as%20filler%0A%20%20FROM%20sampled%0A)%0ASELECT%20timestamp%2C%20symbol%2C%20coalesce(bid_price%2C%20filler)%20as%20bid_price%2C%0A%20%20%20%20%20%20%20coalesce(ask_price%2C%20filler)%20as%20ask_price%2C%0A%20%20%20%20%20%20%20case%20when%20bid_price%20is%20NULL%20then%20true%20END%20as%20filled%0AFROM%20with_previous_vals%3B&executeQuery=true)

```prism-code
WITH sampled AS (  
  SELECT timestamp, symbol, avg(bid_price) as bid_price, avg(ask_price) as ask_price  
  FROM core_price  
  WHERE symbol = 'EURUSD' AND timestamp IN today()  
  SAMPLE BY 100T FILL(null)  
), with_previous_vals AS (  
  SELECT *,  
    last_value(ask_price) IGNORE NULLS OVER(PARTITION BY symbol ORDER BY timestamp) as filler  
  FROM sampled  
)  
SELECT timestamp, symbol, coalesce(bid_price, filler) as bid_price,  
       coalesce(ask_price, filler) as ask_price,  
       case when bid_price is NULL then true END as filled  
FROM with_previous_vals;
```

Related Documentation

* [SAMPLE BY](/docs/query/sql/sample-by/)
* [FILL keyword](/docs/query/sql/sample-by/#fill-keywords)
* [Window functions](/docs/query/functions/window-functions/syntax/)
* [last\_value()](/docs/query/functions/window-functions/reference/#last_value)