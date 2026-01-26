On this page

When a query includes a condition on the
[designated timestamp](/docs/concepts/designated-timestamp/), QuestDB performs an
**Interval Scan**.

For a breakdown of interval syntax in time-based queries, see the
[`WHERE` clause reference](/docs/query/sql/where/).

## How Interval Scan works[​](#how-interval-scan-works "Direct link to How Interval Scan works")

This process involves:

1. **Analyzing the condition**: QuestDB examines the query to identify the
   conditions applied to the designated timestamp.
2. **Extracting a list of timestamp intervals**: Based on the condition, QuestDB
   determines the specific intervals of time that need to be scanned.
3. **Performing a binary search for each interval's scan boundaries in the
   designated timestamp column**: For each identified interval, QuestDB uses a
   binary search to quickly find the start and end points of the interval in the
   timestamp column. A binary search is a fast search algorithm that finds the
   position of a target value within a sorted array, which in this case is a
   sorted timestamp column.
4. **Scanning table data only within the found boundaries:** QuestDB then scans
   only the rows of the table that fall within these boundaries, significantly
   reducing the amount of data that needs to be processed.

The **Interval Scan** is possible because tables with a designated timestamp
store data in timestamp order. This allows QuestDB to efficiently skip over data
that falls outside the relevant intervals. However, it's important to note that
**Interval Scan** does not apply to the results of sub-queries, as the data
returned from a sub-query is not guaranteed to be in timestamp order.

![Interval scan.](/docs/images/blog/2023-04-25/intervalScan.webp)

## EXPLAIN Interval Scan[​](#explain-interval-scan "Direct link to EXPLAIN Interval Scan")

You can determine whether an **Interval Scan** is used to execute a query using
the [EXPLAIN](/docs/query/sql/explain/) command.

For example, consider the `trades` table with a `timestamp` designated
timestamp. The following query:

SELECT a full day interval[Demo this query](https://demo.questdb.io/?query=EXPLAIN%0ASELECT%20*%20FROM%20trades%0AWHERE%20timestamp%20IN%20'2023-01-20'%3B&executeQuery=true)

```prism-code
EXPLAIN  
SELECT * FROM trades  
WHERE timestamp IN '2023-01-20';
```

Produces this query plan:

| QUERY PLAN |
| --- |
| DataFrame |
| Row forward scan |
| Interval forward scan on: trades |
| intervals: [("2023-01-20T00:00:00.000000Z","2023-01-20T23:59:59.999999Z")] |

The query optimizer reduces scanning to a single interval related to the
`2023-01-20` day.

## Examples[​](#examples "Direct link to Examples")

The following three queries all produce the same **Interval Scan** plan because
they all specify the same time range for the `timestamp` column, just in
different ways:

Different ways of getting the data for an interval: using IN[Demo this query](https://demo.questdb.io/?query=EXPLAIN%0ASELECT%20*%20FROM%20trades%0AWHERE%20timestamp%20IN%20'2023-01-20'%3B&executeQuery=true)

```prism-code
EXPLAIN  
SELECT * FROM trades  
WHERE timestamp IN '2023-01-20';
```

Different ways of getting the data for an interval: using BETWEEN[Demo this query](https://demo.questdb.io/?query=EXPLAIN%0ASELECT%20*%20FROM%20trades%0AWHERE%20timestamp%20between%20'2023-01-20T00%3A00%3A00.000000Z'%20and%20'2023-01-20T23%3A59%3A59.999999Z'%3B&executeQuery=true)

```prism-code
EXPLAIN  
SELECT * FROM trades  
WHERE timestamp between '2023-01-20T00:00:00.000000Z' and '2023-01-20T23:59:59.999999Z';
```

Different ways of getting the data for an interval: using Operators[Demo this query](https://demo.questdb.io/?query=EXPLAIN%0ASELECT%20*%20FROM%20trades%0AWHERE%20timestamp%20%3E%3D%20'2023-01-20T00%3A00%3A00.000000Z'%20and%20timestamp%20%3C%3D%20'2023-01-20T23%3A59%3A59.999999Z'%3B&executeQuery=true)

```prism-code
EXPLAIN  
SELECT * FROM trades  
WHERE timestamp >= '2023-01-20T00:00:00.000000Z' and timestamp <= '2023-01-20T23:59:59.999999Z';
```

The **Interval Scan** plan looks like this:

| QUERY PLAN |
| --- |
| DataFrame |
| Row forward scan |
| Interval forward scan on: trades |
| intervals: [("2023-01-20T00:00:00.000000Z","2023-01-20T23:59:59.999999Z")] |

If need to scan more than one interval, you can use the
[timestamp IN operator](/docs/query/operators/date-time/):

Scanning more than one interval with the IN operator[Demo this query](https://demo.questdb.io/?query=EXPLAIN%0ASELECT%20*%20FROM%20trades%0AWHERE%20timestamp%20IN%20'2023-01-01%3B1d%3B1y%3B2'%3B&executeQuery=true)

```prism-code
EXPLAIN  
SELECT * FROM trades  
WHERE timestamp IN '2023-01-01;1d;1y;2';
```

This query results in an **Interval Scan** plan that includes two intervals:

| QUERY PLAN |
| --- |
| DataFrame |
| Row forward scan |
| Interval forward scan on: trades |
| intervals: [(2023-01-01T00:00:00.000000Z,2023-01-02T23:59:59.999999Z), (2024-01-01T00:00:00.000000Z,2024-01-02T23:59:59.999999Z)] |

The table scan is limited to these two intervals:

* `<2023-01-01T00:00:00.000000Z,2023-01-02T23:59:59.999999Z>`
* `<2024-01-01T00:00:00.000000Z,2024-01-02T23:59:59.999999Z>`

If a table doesn't have a designated timestamp, you can declare one using the
`timestamp(columnName)` function.

For example, the following query results in a full scan with an **Async
Filter**, which is a process that scans the entire table without taking
advantage of the designated timestamp:

```prism-code
EXPLAIN  
SELECT * FROM trades_nodts  
WHERE timestamp IN '2023-01-20'
```

However, if you declare a designated timestamp:

```prism-code
EXPLAIN  
SELECT * FROM trades_nodts timestamp(timestamp)  
WHERE timestamp IN '2023-01-20'
```

It results in an **Interval Forward Scan**.

Note that declaring a designated timestamp only works if the data is truly
ordered. For example, if data are sorted in ascending order by the timestamp.
Otherwise the result is undefined, meaning that the query may not return the
expected results.