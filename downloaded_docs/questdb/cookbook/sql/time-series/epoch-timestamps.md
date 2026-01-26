On this page

Query using epoch timestamps instead of timestamp literals.

## Problem[​](#problem "Direct link to Problem")

You want to query data using epoch values rather than timestamp literals.

## Solution[​](#solution "Direct link to Solution")

Use epoch values directly in your WHERE clause. QuestDB expects microseconds by default for `timestamp` columns:

Query with epoch in microseconds[Demo this query](https://demo.questdb.io/?query=SELECT%20*%0AFROM%20trades%0AWHERE%20timestamp%20BETWEEN%201746552420000000%20AND%201746811620000000%3B&executeQuery=true)

```prism-code
SELECT *  
FROM trades  
WHERE timestamp BETWEEN 1746552420000000 AND 1746811620000000;
```

Millisecond Resolution

If you have epoch values in milliseconds, you need to multiply by 1000 to convert to microseconds.

Nanoseconds can be used when the timestamp column is of type `timestamp_ns`.

Query with epoch in nanoseconds[Demo this query](https://demo.questdb.io/?query=SELECT%20*%0AFROM%20fx_trades%0AWHERE%20timestamp%20BETWEEN%201768303754000000000%20AND%201778303754000000000%3B&executeQuery=true)

```prism-code
SELECT *  
FROM fx_trades  
WHERE timestamp BETWEEN 1768303754000000000 AND 1778303754000000000;
```

If the query does not return any data

Since the `fx_trades` table has a TTL, the query above may return empty results. To find valid epoch values with data, run:

`select timestamp::long as from_epoch, dateadd('s', -10, timestamp)::long as to_epoch from fx_trades limit -1;`

Then replace the `BETWEEN` values with the epochs returned.

Related Documentation

* [Timestamp types](/docs/query/datatypes/overview/#timestamp-and-date-considerations)
* [WHERE clause](/docs/query/sql/where/)