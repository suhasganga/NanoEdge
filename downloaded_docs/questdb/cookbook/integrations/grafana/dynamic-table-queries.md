On this page

Query multiple QuestDB tables dynamically in Grafana using dashboard variables. This is useful when you have many tables with identical schemas (e.g., sensor data, metrics from different sources) and want to visualize them together without hardcoding table names in your queries.

## Problem: Visualize many similar tables[​](#problem-visualize-many-similar-tables "Direct link to Problem: Visualize many similar tables")

You have 100+ tables with the same structure (e.g., `sensor_1`, `sensor_2`, ..., `sensor_n`) and want to:

1. Display data from all tables on a single Grafana chart
2. Avoid manually updating queries when tables are added or removed
3. Allow users to select which tables to visualize via dashboard controls

## Solution: Use Grafana variables with dynamic SQL[​](#solution-use-grafana-variables-with-dynamic-sql "Direct link to Solution: Use Grafana variables with dynamic SQL")

Create Grafana dashboard variables that query QuestDB for table names, then use string aggregation functions to build the SQL query dynamically.

### Step 1: Get table names[​](#step-1-get-table-names "Direct link to Step 1: Get table names")

First, query QuestDB to get all relevant table names:

```prism-code
SELECT table_name FROM tables()  
WHERE table_name LIKE 'sensor_%';
```

This returns a list of all tables matching the pattern.

### Step 2: Create Grafana variables[​](#step-2-create-grafana-variables "Direct link to Step 2: Create Grafana variables")

Create two dashboard variables to construct the dynamic query:

**Variable 1: `$table_list`** - Build the JOIN clause

```prism-code
WITH tbs AS (  
  SELECT string_agg(table_name, ',') as names  
  FROM tables()  
  WHERE table_name LIKE 'sensor_%'  
)  
SELECT replace(names, ',', ' ASOF JOIN ') FROM tbs;
```

**Output:** `sensor_1 ASOF JOIN sensor_2 ASOF JOIN sensor_3 ASOF JOIN sensor_4`

This creates the table list with ASOF JOIN operators between them.

**Variable 2: `$column_avgs`** - Build the column list

```prism-code
SELECT string_agg(concat('avg(', table_name, '.value)'), ',') as columns  
FROM tables()  
WHERE table_name LIKE 'sensor_%';
```

**Output:** `avg(sensor_1.value),avg(sensor_2.value),avg(sensor_3.value),avg(sensor_4.value)`

This creates the column selection list with aggregation functions.

### Step 3: Use variables in dashboard query[​](#step-3-use-variables-in-dashboard-query "Direct link to Step 3: Use variables in dashboard query")

Now reference these variables in your Grafana chart query:

```prism-code
SELECT sensor_1.timestamp, $column_avgs  
FROM $table_list  
SAMPLE BY 1s FROM $__fromTime TO $__toTime FILL(PREV);
```

When Grafana executes this query, it interpolates the variables:

```prism-code
SELECT sensor_1.timestamp, avg(sensor_1.value),avg(sensor_2.value),avg(sensor_3.value),avg(sensor_4.value)  
FROM sensor_1 ASOF JOIN sensor_2 ASOF JOIN sensor_3 ASOF JOIN sensor_4  
SAMPLE BY 1s FROM cast(1571176800000000 as timestamp) TO cast(1571349600000000 as timestamp) FILL(PREV);
```

## How it works[​](#how-it-works "Direct link to How it works")

The solution uses three key QuestDB features:

1. **`tables()` function**: Returns metadata about all tables in the database
2. **`string_agg()`**: Concatenates multiple rows into a single comma-separated string
3. **`replace()`**: Swaps commas for JOIN operators to build the FROM clause

Combined with Grafana's variable interpolation:

* `$column_avgs`: Replaced with the aggregated column list
* `$table_list`: Replaced with the joined table expression
* `$__fromTime` / `$__toTime`: Grafana macros for the dashboard's time range

### Understanding ASOF JOIN[​](#understanding-asof-join "Direct link to Understanding ASOF JOIN")

`ASOF JOIN` is ideal for time-series data with different update frequencies:

* Joins tables on timestamp
* For each row in the first table, finds the closest past timestamp in other tables
* Works like a LEFT JOIN but with time-based matching

This ensures that even if tables update at different rates, you get a complete dataset with the most recent known value from each table.

## Adapting the pattern[​](#adapting-the-pattern "Direct link to Adapting the pattern")

**Filter by different patterns:**

```prism-code
-- Tables starting with "metrics_"  
WHERE table_name LIKE 'metrics_%'  
  
-- Tables matching a regex pattern  
WHERE table_name ~ 'sensor_[0-9]+'  
  
-- Exclude certain tables  
WHERE table_name LIKE 'sensor_%'  
  AND table_name NOT IN ('sensor_test', 'sensor_backup')
```

## Programmatic alternative[​](#programmatic-alternative "Direct link to Programmatic alternative")

If you're not using Grafana, you can achieve the same result programmatically:

1. **Query for table names:**

   ```prism-code
   SELECT table_name FROM tables() WHERE table_name LIKE 'sensor_%';
   ```
2. **Build the query on the client side:**

   ```prism-code
   # Python example  
   tables = ['sensor_1', 'sensor_2', 'sensor_3']  
     
   # Build JOIN clause  
   join_clause = ' ASOF JOIN '.join(tables)  
     
   # Build column list  
   columns = ','.join([f'avg({t}.value)' for t in tables])  
     
   # Final query  
   query = f"""  
       SELECT {tables[0]}.timestamp, {columns}  
       FROM {join_clause}  
       SAMPLE BY 1s FILL(PREV)  
   """
   ```

## Handling different sampling intervals[​](#handling-different-sampling-intervals "Direct link to Handling different sampling intervals")

When tables have different update frequencies, use FILL to handle gaps:

```prism-code
-- Fill with previous value (holds last known value)  
SAMPLE BY 1s FILL(PREV)  
  
-- Fill with linear interpolation  
SAMPLE BY 1s FILL(LINEAR)  
  
-- Fill with NULL (show actual gaps)  
SAMPLE BY 1s FILL(NULL)  
  
-- Fill with zero  
SAMPLE BY 1s FILL(0)
```

**Choose based on your data:**

* **PREV**: Best for metrics that persist (temperatures, prices, statuses)
* **LINEAR**: Best for continuous values that change smoothly
* **NULL**: Best when you want to see actual data gaps
* **0 or constant**: Best for counting or rate metrics

Performance Optimization

Joining many tables can be expensive. To improve performance:

* Use `SAMPLE BY` to reduce the number of rows
* Add timestamp filters early in the query
* Consider pre-aggregating data into a single table for frequently-accessed views
* Limit the number of tables joined (split into multiple charts if needed)

Table Schema Consistency

This pattern assumes all tables have identical schemas. If schemas differ:

* The query will fail at runtime
* You'll need to handle missing columns explicitly
* Consider using separate queries for tables with different structures

Related Documentation

* [ASOF JOIN](/docs/query/sql/join/#asof-join)
* [tables() function](/docs/query/functions/meta/#tables)
* [string\_agg()](/docs/query/functions/aggregation/#string_agg)
* [SAMPLE BY](/docs/query/sql/sample-by/)
* [Grafana QuestDB data source](https://grafana.com/grafana/plugins/questdb-questdb-datasource/)