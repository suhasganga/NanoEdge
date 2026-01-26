On this page

Efficiently query sparse sensor data by splitting wide tables into narrow tables and joining them with different strategies.

## Problem[​](#problem "Direct link to Problem")

You have a sparse sensors table with 120 sensor columns, in which you are getting just a few sensor values at any given timestamp, so most values are null.

When you want to query data from any given sensor, you first SAMPLE the data with an `avg` or a `last_not_null` function aggregation, and then often build a CTE and call `LATEST ON` to get results:

```prism-code
SELECT  
  timestamp,  
  vehicle_id,  
  avg(sensor_1) AS avg_sensor_1, avg(sensor_2) AS avg_sensor_2,  
  ...  
  avg(sensor_119) AS avg_sensor_119, avg(sensor_120) AS avg_sensor_120  
FROM  
  vehicle_sensor_data  
-- WHERE vehicle_id = 'AAA0000'  
SAMPLE BY 30s  
LIMIT 100000;
```

This works, but it is not super fast (1sec for 10 million rows, in a table with 120 sensor columns and with 10k different vehicle\_ids), and it is also not very efficient because `null` columns take some bytes on disk.

## Solution: Multiple narrow tables with joins[​](#solution-multiple-narrow-tables-with-joins "Direct link to Solution: Multiple narrow tables with joins")

A single table works, but there is a more efficient (although a bit more cumbersome if you compose queries by hand) way to do this.

You can create 120 tables, one per sensor, rather than a table with 120 columns. Well, technically you probably want 121 tables, one with the common dimensions, then 1 per sensor. Or maybe you want N tables, one for the common dimensions, then N depending on how many sensor groups you have, as some groups might always send in sync. In any case, rather than a wide table you would end up with several narrow tables that you would need to join.

Now for joining the tables there are three potential ways, depending on the results you are after:

* To see the *LATEST* known value for all the metrics *for a given series*, use a `CROSS JOIN` strategy (example below). This returns a single row.
* To see the *LATEST* known value for all the metrics and *for all or several series*, use a `LEFT JOIN` strategy. This returns a single row per series (example below).
* To see the *rolling view of all the latest known values* regarding the current row for one of the metrics, use an `ASOF JOIN` strategy. This returns as many rows as you have in the main metric you are querying (example below).

### Performance[​](#performance "Direct link to Performance")

The three approaches perform well. The three queries were executed on a table like the initial one, with 10 million rows representing sparse data from 10k series and across 120 metrics, so 120 tables. Each of the 120 tables had ~83k records (which times 120 is ~10 million rows).

`CROSS JOIN` is the fastest, executing in 23ms, `ASOF JOIN` is second with 123 ms, and `LEFT JOIN` is the slowest at 880ms. Still not too bad, as you probably will not want to get all the sensors from all the devices all the time, and joining fewer tables would perform better.

## Strategy 1: CROSS JOIN[​](#strategy-1-cross-join "Direct link to Strategy 1: CROSS JOIN")

We first find the latest point in each of the 120 tables for the given series (AAA0000), so we get a value per table, and then do a `CROSS JOIN`, to get a single row.

```prism-code
WITH  
s1 AS (SELECT timestamp, vehicle_id, value FROM vehicle_sensor_1  
    WHERE vehicle_id = 'AAA0000' LATEST ON timestamp PARTITION BY vehicle_id),  
s2 AS (SELECT timestamp, vehicle_id, value FROM vehicle_sensor_2  
    WHERE vehicle_id = 'AAA0000' LATEST ON timestamp PARTITION BY vehicle_id),  
...  
s119 AS (SELECT timestamp, vehicle_id, value FROM vehicle_sensor_119  
    WHERE vehicle_id = 'AAA0000' LATEST ON timestamp PARTITION BY vehicle_id),  
s120 AS (SELECT timestamp, vehicle_id, value FROM vehicle_sensor_120  
    WHERE vehicle_id = 'AAA0000' LATEST ON timestamp PARTITION BY vehicle_id)  
SELECT s1.timestamp, s1.vehicle_id, s1.value AS value_1,  
s2.value AS value_2,  
...  
s119.value AS value_119,  
s120.value AS value_120  
FROM s1  
CROSS JOIN s2  
CROSS JOIN ...  
CROSS JOIN s119  
CROSS JOIN s120;
```

## Strategy 2: LEFT JOIN[​](#strategy-2-left-join "Direct link to Strategy 2: LEFT JOIN")

We first find the latest point in each of the 120 tables for each series, so we get a value per table and series, and then do a `LEFT JOIN` on the series ID, to get a single row for each different series (10K rows in our example).

```prism-code
WITH  
s1 AS (SELECT timestamp, vehicle_id, value FROM vehicle_sensor_1  
    LATEST ON timestamp PARTITION BY vehicle_id),  
s2 AS (SELECT timestamp, vehicle_id, value FROM vehicle_sensor_2  
    LATEST ON timestamp PARTITION BY vehicle_id),  
...  
s119 AS (SELECT timestamp, vehicle_id, value FROM vehicle_sensor_119  
    LATEST ON timestamp PARTITION BY vehicle_id),  
s120 AS (SELECT timestamp, vehicle_id, value FROM vehicle_sensor_120  
    LATEST ON timestamp PARTITION BY vehicle_id)  
SELECT s1.timestamp, s1.vehicle_id, s1.value AS value_1,  
s2.value AS value_2,  
...  
s119.value AS value_119,  
s120.value AS value_120  
FROM s1  
LEFT JOIN s2 ON s1.vehicle_id = s2.vehicle_id  
LEFT JOIN ...  
LEFT JOIN s119 ON s1.vehicle_id = s119.vehicle_id  
LEFT JOIN s120 ON s1.vehicle_id = s120.vehicle_id;
```

## Strategy 3: ASOF JOIN[​](#strategy-3-asof-join "Direct link to Strategy 3: ASOF JOIN")

We get all the rows in all the tables, then do an `ASOF JOIN` on the series ID, so we get a row for each row of the first table in the query, in our example ~83K results.

```prism-code
WITH  
s1 AS (SELECT timestamp, vehicle_id, value FROM vehicle_sensor_1 ),  
s2 AS (SELECT timestamp, vehicle_id, value FROM vehicle_sensor_2 ),  
...  
s118 AS (SELECT timestamp, vehicle_id, value FROM vehicle_sensor_118 ),  
s119 AS (SELECT timestamp, vehicle_id, value FROM vehicle_sensor_119 ),  
s120 AS (SELECT timestamp, vehicle_id, value FROM vehicle_sensor_120 )  
SELECT s1.timestamp, s1.vehicle_id, s1.value AS value_1,  
       s2.value AS value_2,  
       ...  
       s119.value AS value_119,  
       s120.value AS value_120  
FROM s1  
ASOF JOIN s2 ON s1.vehicle_id = s2.vehicle_id  
ASOF JOIN ...  
ASOF JOIN s119 ON s1.vehicle_id = s119.vehicle_id  
ASOF JOIN s120 ON s1.vehicle_id = s120.vehicle_id;
```

Related Documentation

* [ASOF JOIN](/docs/query/sql/join/#asof-join)
* [LEFT JOIN](/docs/query/sql/join/#left-outer-join)
* [CROSS JOIN](/docs/query/sql/join/#cross-join)
* [LATEST ON](/docs/query/sql/select/#latest-on)