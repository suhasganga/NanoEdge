On this page

QuestDB includes a JIT compiler which is run on queries (and sub-queries) that
perform a full scan over a table or table partitions. The main goal behind this
feature is to improve performance for filters with arithmetical expressions. To
do so, the JIT compiler emits machine code with a single function that may also
use SIMD (vector) instructions.

For details on the implementation, motivation, and internals of this feature,
see our [article about SQL JIT compilation](https://questdb.com/blog/2022/01/12/jit-sql-compiler).
This post describes our storage model, how we built a JIT compiler for SQL and
our plans for improving it in future.

## Queries eligible for JIT compilation[​](#queries-eligible-for-jit-compilation "Direct link to Queries eligible for JIT compilation")

The types of queries that are eligible for performance improvements via JIT
compilation are those which contain `WHERE` clauses. Here are some examples
you can execute on the [QuestDB Public Demo Datasets](https://demo.questdb.io):

basic filtering in WHERE clauses with JIT[Demo this query](https://demo.questdb.io/?query=--%20basic%20filtering%20in%20WHERE%20clauses%0ASELECT%20count()%2C%20max(bid_price)%20FROM%20core_price%0AWHERE%0Atimestamp%20in%20today()%20AND%20bid_price%20%3E%201%20AND%20Symbol%20%3D%20'EURUSD'%3B&executeQuery=true)

```prism-code
-- basic filtering in WHERE clauses  
SELECT count(), max(bid_price) FROM core_price  
WHERE  
timestamp in today() AND bid_price > 1 AND Symbol = 'EURUSD';
```

Filtering and aggregating with JIT[Demo this query](https://demo.questdb.io/?query=--%20sub-queries%0AEXPLAIN%20SELECT%20symbol%2C%20count()%2C%20max(bid_price)%20FROM%20core_price%0AWHERE%20timestamp%20in%20today()%20AND%20bid_price%20%3E%201%3B&executeQuery=true)

```prism-code
-- sub-queries  
EXPLAIN SELECT symbol, count(), max(bid_price) FROM core_price  
WHERE timestamp in today() AND bid_price > 1;
```

## JIT compiler usage[​](#jit-compiler-usage "Direct link to JIT compiler usage")

The JIT compiler is enabled by default for QuestDB 6.3 onwards. If you wish to
disable it, change the `cairo.sql.jit.mode` setting in the
[server configuration](/docs/configuration/overview/) file from `on` to `off`:

path/to/server.conf

```prism-code
cairo.sql.jit.mode=off
```

Embedded API users are able to enable or disable the compiler globally by
providing their `CairoConfiguration` implementation. Alternatively, JIT
compilation can be changed for a single query by using the
`SqlExecutionContext#setJitMode` method. The latter may look like the following:

```prism-code
final CairoConfiguration configuration = new DefaultCairoConfiguration(temp.getRoot().getAbsolutePath());  
try (CairoEngine engine = new CairoEngine(configuration)) {  
    final SqlExecutionContextImpl ctx = new SqlExecutionContextImpl(engine, 1);  
    // Enable SQL JIT compiler  
    ctx.setJitMode(SqlJitMode.JIT_MODE_ENABLED);  
    // Subsequent query execution (called as usual) with have JIT enabled  
    try (SqlCompiler compiler = new SqlCompiler(engine)) {  
        try (RecordCursorFactory factory = compiler.compile("abc", ctx).getRecordCursorFactory()) {  
            try (RecordCursor cursor = factory.getCursor(ctx)) {  
                // ...  
            }  
        }  
    }  
}
```

Server logs should contain references to `SQL JIT compiler mode`:

```prism-code
2021-12-16T09:25:34.472450Z A server-main SQL JIT compiler mode: on
```

Due to certain limitations noted below, JIT compilation won't take place for all
queries. To understand whether JIT compilation took place for a query, one will
see something similar in the server logs:

```prism-code
2021-12-16T09:35:01.738910Z I i.q.g.SqlCompiler plan [q=`select-group-by count() count from (select [usage_user] from cpu timestamp (timestamp) where usage_user > 75)`, fd=73]  
2021-12-16T09:35:01.742777Z I i.q.g.SqlCodeGenerator JIT enabled for (sub)query [tableName=cpu, fd=73]
```

## Known limitations[​](#known-limitations "Direct link to Known limitations")

The current implementation of the JIT SQL compiler has a number of limitations:

* Only x86-64 CPUs are currently supported.
* Vectorized filter execution requires AVX2 instruction set.
* Filters with any SQL function, such as `now()`, or `abs()`, or `round()`, are
  not supported.
* Filters with any pseudo-function or operator, such as `in()` on symbol column,
  or `between` on non-designated timestamp column, or `within` on geohash
  column, are not supported.
* Only the following arithmetic operations are allowed to be present in the
  filter: `+`, `-`, `*`, `/`.
* Only filters with fixed-size columns are supported: BOOLEAN, BYTE, GEOBYTE,
  SHORT, GEOSHORT, CHAR, INT, GEOINT, SYMBOL, FLOAT, LONG, GEOLONG, DATE,
  TIMESTAMP, DOUBLE, UUID.