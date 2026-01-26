On this page

Combine overall (unsampled) aggregates with sampled aggregates in the same query.

## Problem[​](#problem "Direct link to Problem")

You have a query with three aggregates:

Max and Min[Demo this query](https://demo.questdb.io/?query=SELECT%20max(price)%2C%20avg(price)%2C%20min(price)%0AFROM%20trades%0AWHERE%20timestamp%20IN%20'2024-12-08'%3B&executeQuery=true)

```prism-code
SELECT max(price), avg(price), min(price)  
FROM trades  
WHERE timestamp IN '2024-12-08';
```

This returns:

```prism-code
| max(price) | avg(price)         | min(price)  |  
| ---------- | ------------------ | ----------- |  
| 101464.2   | 15816.513123255792 | 0.000031204 |
```

And another query to get event count per second, then select the maximum:

Sample by 1m and get the top result[Demo this query](https://demo.questdb.io/?query=SELECT%20max(count_sec)%20FROM%20(%0A%20%20SELECT%20count()%20as%20count_sec%20FROM%20trades%0A%20%20WHERE%20timestamp%20IN%20'2024-12-08'%0A%20%20SAMPLE%20BY%201s%0A)%3B&executeQuery=true)

```prism-code
SELECT max(count_sec) FROM (  
  SELECT count() as count_sec FROM trades  
  WHERE timestamp IN '2024-12-08'  
  SAMPLE BY 1s  
);
```

This returns:

```prism-code
| max(count_sec) |  
| -------------- |  
| 4473           |
```

You want to combine both results in a single row:

```prism-code
| max(count_sec) | max(price) | avg(price)         | min(price)  |  
| -------------- | ---------- | ------------------ | ----------- |  
| 4473           | 101464.2   | 15816.513123255792 | 0.000031204 |
```

## Solution: CROSS JOIN[​](#solution-cross-join "Direct link to Solution: CROSS JOIN")

A `CROSS JOIN` can join every row from the first query (1 row) with every row from the second (1 row), so you get a single row with all the aggregates combined:

Combine general and sampled aggregates[Demo this query](https://demo.questdb.io/?query=WITH%0Amax_min%20AS%20(%0ASELECT%20max(price)%2C%20avg(price)%2C%20min(price)%0AFROM%20trades%20WHERE%20timestamp%20IN%20'2024-12-08'%0A)%0ASELECT%20max(count_sec)%2C%20max_min.*%20FROM%20(%0A%20%20SELECT%20count()%20as%20count_sec%20FROM%20trades%0A%20%20WHERE%20timestamp%20IN%20'2024-12-08'%0A%20%20SAMPLE%20BY%201s%0A)%20CROSS%20JOIN%20max_min%3B&executeQuery=true)

```prism-code
WITH  
max_min AS (  
SELECT max(price), avg(price), min(price)  
FROM trades WHERE timestamp IN '2024-12-08'  
)  
SELECT max(count_sec), max_min.* FROM (  
  SELECT count() as count_sec FROM trades  
  WHERE timestamp IN '2024-12-08'  
  SAMPLE BY 1s  
) CROSS JOIN max_min;
```

Related Documentation

* [CROSS JOIN](/docs/query/sql/join/#cross-join)
* [SAMPLE BY](/docs/query/sql/sample-by/)