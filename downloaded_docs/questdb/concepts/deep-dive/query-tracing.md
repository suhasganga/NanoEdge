Query tracing is a feature that helps you diagnose performance issues with
queries by recording each query's execution time, and the user who launched the query,
in a system table called
`_query_trace`. You can then analyze the data in this table using the full power
of QuestDB's SQL statements.

Query tracing is disabled by default. You can enable it using the following
configuration property in `server.conf`:

```prism-code
query.tracing.enabled=true
```

You don't need to restart the database server for this property to take effect;
just run the following query to reload the configuration:

reload\_config()

```prism-code
SELECT reload_config();
```

This is an example of what the `_query_trace` table may contain:

\_query\_trace

```prism-code
SELECT * from _query_trace;
```

| ts | query\_text | execution\_micros | principal |
| --- | --- | --- | --- |
| 2025-01-15T08:52:56.600757Z | telemetry\_config LIMIT -1 | 1206 | admin |
| 2025-01-15T08:53:03.815732Z | tables() | 1523 | admin |
| 2025-01-15T08:53:22.971239Z | 'sys.query\_trace' | 5384 | admin |

As a simple performance debugging example, to get the text of all queries that
took more than 100 ms, run:

\_query\_trace with filters

```prism-code
SELECT  
    query_text  
FROM _query_trace  
WHERE execution_micros > 100_000  
ORDER BY execution_micros DESC;
```

The `_query_trace` table will drop data older than 24 hours in order to limit
how much storage query tracing uses.