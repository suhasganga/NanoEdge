On this page

When ingesting data to a WAL table using ILP protocol, inserts are asynchronous. This recipe shows how to ensure all ingested rows are visible for read-only queries.

## Problem[​](#problem "Direct link to Problem")

You're performing a single-time ingestion of a large data volume using ILP protocol to a table that uses Write-Ahead Log (WAL). Since inserts are asynchronous, you need to confirm that all ingested rows are visible for read-only queries before proceeding with operations.

## Solution[​](#solution "Direct link to Solution")

Query the `wal_tables()` function to check if the writer transaction matches the sequencer transaction. When these values match, all rows have become visible:

Check applied transactions from WAL files[Demo this query](https://demo.questdb.io/?query=SELECT%20*%0AFROM%20wal_tables()%0AWHERE%20name%20%3D%20'core_price'%20AND%20writerTxn%20%3D%20sequencerTxn%3B&executeQuery=true)

```prism-code
SELECT *  
FROM wal_tables()  
WHERE name = 'core_price' AND writerTxn = sequencerTxn;
```

This query returns a row when `writerTxn` equals `sequencerTxn` for your table:

* `writerTxn` is the last committed transaction available for read-only queries
* `sequencerTxn` is the last transaction committed to WAL

When they match, all WAL transactions have been applied and all rows are visible for queries.

Another viable approach is to run `SELECT count(*) FROM my_table` and verify the expected row count.

Related Documentation

* [Write-Ahead Log concept](/docs/concepts/write-ahead-log/)
* [Meta functions reference](/docs/query/functions/meta/)
* [InfluxDB Line Protocol overview](/docs/ingestion/ilp/overview/)