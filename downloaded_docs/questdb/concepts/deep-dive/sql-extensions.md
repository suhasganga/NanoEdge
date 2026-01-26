On this page

QuestDB attempts to implement standard ANSI SQL. We also try to be compatible
with PostgreSQL, although parts of this are a work in progress. This page
presents the main extensions we bring to SQL and the main differences that one
might find in SQL but not in QuestDB's dialect.

## SQL extensions[​](#sql-extensions "Direct link to SQL extensions")

We have extended SQL to support our data storage model and simplify semantics of
time series analytics.

### LATEST ON[​](#latest-on "Direct link to LATEST ON")

[LATEST ON](/docs/query/sql/latest-on/) is a clause introduced to help find
the latest entry by timestamp for a given key or combination of keys as part of
a `SELECT` statement.

LATEST ON symbol ID and side[Demo this query](https://demo.questdb.io/?query=SELECT%20*%20FROM%20trades%0AWHERE%20timestamp%20IN%20today()%0ALATEST%20ON%20timestamp%20PARTITION%20BY%20symbol%2C%20side%3B&executeQuery=true)

```prism-code
SELECT * FROM trades  
WHERE timestamp IN today()  
LATEST ON timestamp PARTITION BY symbol, side;
```

### Timestamp search[​](#timestamp-search "Direct link to Timestamp search")

Timestamp search can be performed with regular operators, e.g `>`, `<=` etc.
However, QuestDB provides a
[native notation](/docs/query/sql/where/#timestamp-and-date) which is faster
and less verbose.

Results in a given year[Demo this query](https://demo.questdb.io/?query=SELECT%20*%20FROM%20trades%20WHERE%20timestamp%20IN%20'2025'%3B&executeQuery=true)

```prism-code
SELECT * FROM trades WHERE timestamp IN '2025';
```

### SAMPLE BY[​](#sample-by "Direct link to SAMPLE BY")

[SAMPLE BY](/docs/query/sql/select/#sample-by) is used for time-based
[aggregations](/docs/query/functions/aggregation/) with an efficient syntax.
The short query below will return the average price from a list of
symbols by one hour buckets.

SAMPLE BY one month buckets[Demo this query](https://demo.questdb.io/?query=SELECT%20timestamp%2C%20symbol%2C%20sum(price)%20FROM%20trades%0AWHERE%20timestamp%20in%20today()%0ASAMPLE%20BY%201h%3B&executeQuery=true)

```prism-code
SELECT timestamp, symbol, sum(price) FROM trades  
WHERE timestamp in today()  
SAMPLE BY 1h;
```

## Differences from standard SQL[​](#differences-from-standard-sql "Direct link to Differences from standard SQL")

### SELECT \* FROM is optional[​](#select--from-is-optional "Direct link to SELECT * FROM is optional")

In QuestDB, using `SELECT * FROM` is optional, so `SELECT * FROM my_table;` will
return the same result as `my_table;`. While adding `SELECT * FROM` makes SQL
look more complete, there are examples where omitting these keywords makes
queries a lot easier to read.

Optional use of SELECT \* FROM[Demo this query](https://demo.questdb.io/?query=trades%3B%0A--%20equivalent%20to%3A%0ASELECT%20*%20FROM%20trades%3B&executeQuery=true)

```prism-code
trades;  
-- equivalent to:  
SELECT * FROM trades;
```

### GROUP BY is optional[​](#group-by-is-optional "Direct link to GROUP BY is optional")

The `GROUP BY` clause is optional and can be omitted as the QuestDB optimizer
derives group-by implementation from the `SELECT` clause. In standard SQL, users
might write a query like the following:

Standard SQL GROUP BY[Demo this query](https://demo.questdb.io/?query=SELECT%20symbol%2C%20side%2C%20sum(price)%20FROM%20trades%0AWHERE%20timestamp%20IN%20today()%0AGROUP%20BY%20symbol%2C%20side%3B&executeQuery=true)

```prism-code
SELECT symbol, side, sum(price) FROM trades  
WHERE timestamp IN today()  
GROUP BY symbol, side;
```

However, enumerating a subset of `SELECT` columns in the `GROUP BY` clause is
redundant and therefore unnecessary. The same SQL in QuestDB SQL-dialect can be
written as:

QuestDB Implicit GROUP BY[Demo this query](https://demo.questdb.io/?query=SELECT%20symbol%2C%20side%2C%20sum(price)%20FROM%20trades%0AWHERE%20timestamp%20IN%20today()%3B&executeQuery=true)

```prism-code
SELECT symbol, side, sum(price) FROM trades  
WHERE timestamp IN today();
```

### Implicit HAVING[​](#implicit-having "Direct link to Implicit HAVING")

Let's look at another more complex example using `HAVING` in standard SQL:

Standard SQL GROUP BY/HAVING

```prism-code
SELECT symbol, side, sum(price) FROM trades  
WHERE timestamp IN today()  
GROUP BY symbol, side  
HAVING sum(price) > 1000;
```

In QuestDB's dialect, featherweight sub-queries come to the rescue to create a
smaller, more readable query, without unnecessary repetitive aggregations.
`HAVING` functionality can be obtained implicitly as follows:

QuestDB Implicit HAVING equivalent[Demo this query](https://demo.questdb.io/?query=(%0A%20%20SELECT%20symbol%2C%20side%2C%20sum(price)%20as%20total_price%0A%20%20FROM%20trades%20WHERE%20timestamp%20IN%20today()%0A)%0AWHERE%20total_price%20%3E%2010_000_000%3B&executeQuery=true)

```prism-code
(  
  SELECT symbol, side, sum(price) as total_price  
  FROM trades WHERE timestamp IN today()  
)  
WHERE total_price > 10_000_000;
```