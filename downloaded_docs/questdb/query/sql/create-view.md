On this page

Creates a new view in the database. A view is a virtual table defined by a SQL
`SELECT` statement that does not store data itself.

For more information on views, see the [Views](/docs/concepts/views/)
documentation.

## Syntax[​](#syntax "Direct link to Syntax")

```prism-code
CREATE [ OR REPLACE ] VIEW [ IF NOT EXISTS ] view_name AS ( query )
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parameter | Description |
| --- | --- |
| `IF NOT EXISTS` | Prevents error if view already exists |
| `OR REPLACE` | Replaces existing view or creates new one |
| `view_name` | Name of the view (case-insensitive, Unicode supported) |
| `query` | SELECT statement defining the view |

## Examples[​](#examples "Direct link to Examples")

### Basic view[​](#basic-view "Direct link to Basic view")

Create a simple view

```prism-code
CREATE VIEW my_view AS (  
  SELECT ts, symbol, price FROM trades  
)
```

### View with aggregation[​](#view-with-aggregation "Direct link to View with aggregation")

Create a view with SAMPLE BY

```prism-code
CREATE VIEW hourly_ohlc AS (  
  SELECT  
    ts,  
    symbol,  
    first(price) as open,  
    max(price) as high,  
    min(price) as low,  
    last(price) as close,  
    sum(quantity) as volume  
  FROM trades  
  SAMPLE BY 1h  
)
```

### View with filtering[​](#view-with-filtering "Direct link to View with filtering")

Create a view with WHERE clause

```prism-code
CREATE VIEW high_value_trades AS (  
  SELECT ts, symbol, price, quantity  
  FROM trades  
  WHERE price * quantity > 10000  
)
```

### View with JOIN[​](#view-with-join "Direct link to View with JOIN")

Create a view with JOIN

```prism-code
CREATE VIEW enriched_trades AS (  
  SELECT t.ts, t.symbol, t.price, m.company_name  
  FROM trades t  
  JOIN metadata m ON t.symbol = m.symbol  
)
```

### View with UNION[​](#view-with-union "Direct link to View with UNION")

Create a view with UNION

```prism-code
CREATE VIEW all_markets AS (  
  SELECT ts, symbol, price FROM nyse_trades  
  UNION ALL  
  SELECT ts, symbol, price FROM nasdaq_trades  
)
```

### IF NOT EXISTS[​](#if-not-exists "Direct link to IF NOT EXISTS")

Create view only if it doesn't exist

```prism-code
CREATE VIEW IF NOT EXISTS price_view AS (  
  SELECT symbol, last(price) as price FROM trades SAMPLE BY 1h  
)
```

### OR REPLACE[​](#or-replace "Direct link to OR REPLACE")

Create or replace existing view

```prism-code
CREATE OR REPLACE VIEW price_view AS (  
  SELECT symbol, last(price) as price, ts FROM trades SAMPLE BY 1h  
)
```

### Parameterized view with DECLARE[​](#parameterized-view-with-declare "Direct link to Parameterized view with DECLARE")

By default, `DECLARE` variables are **non-overridable**. Users querying the view
cannot change the parameter value:

Create a view with non-overridable parameter

```prism-code
CREATE VIEW filtered_trades AS (  
  DECLARE @min_price := 100  
  SELECT ts, symbol, price FROM trades WHERE price >= @min_price  
)
```

Query uses the default parameter value:

```prism-code
SELECT * FROM filtered_trades  
-- Uses @min_price = 100
```

Attempting to override a non-overridable parameter will fail:

```prism-code
-- This fails with "variable is not overridable: @min_price"  
DECLARE @min_price := 500 SELECT * FROM filtered_trades
```

### DECLARE with OVERRIDABLE[​](#declare-with-overridable "Direct link to DECLARE with OVERRIDABLE")

Use the `OVERRIDABLE` keyword to allow users to override the parameter at query
time:

Create view with overridable parameter

```prism-code
CREATE VIEW flexible_view AS (  
  DECLARE OVERRIDABLE @min_value := 0  
  SELECT * FROM trades WHERE value >= @min_value  
)
```

Users can now override the parameter:

```prism-code
-- Override the default value  
DECLARE @min_value := 100 SELECT * FROM flexible_view
```

### Multiple overridable parameters[​](#multiple-overridable-parameters "Direct link to Multiple overridable parameters")

View with multiple overridable parameters

```prism-code
CREATE VIEW price_range AS (  
  DECLARE OVERRIDABLE @lo := 100, OVERRIDABLE @hi := 1000  
  SELECT ts, symbol, price FROM trades  
  WHERE price >= @lo AND price <= @hi  
)  
  
-- Override one or both parameters  
DECLARE @lo := 50, @hi := 200 SELECT * FROM price_range
```

### Mixed overridable and non-overridable parameters[​](#mixed-overridable-and-non-overridable-parameters "Direct link to Mixed overridable and non-overridable parameters")

View with mixed parameter types

```prism-code
CREATE VIEW mixed_params AS (  
  DECLARE @fixed := 5, OVERRIDABLE @adjustable := 10  
  SELECT * FROM data WHERE a >= @fixed AND b <= @adjustable  
)  
  
-- @adjustable can be overridden, @fixed cannot  
DECLARE @adjustable := 20 SELECT * FROM mixed_params  -- OK  
DECLARE @fixed := 0 SELECT * FROM mixed_params        -- ERROR: variable is not overridable: @fixed
```

### Unicode view name[​](#unicode-view-name "Direct link to Unicode view name")

Create view with Unicode name

```prism-code
CREATE VIEW 日本語ビュー AS (SELECT * FROM trades)  
CREATE VIEW Részvény_árak AS (SELECT * FROM prices)
```

### Specifying timestamp column[​](#specifying-timestamp-column "Direct link to Specifying timestamp column")

When a view's result doesn't have an obvious designated timestamp, you can
specify one:

Create view with explicit timestamp

```prism-code
CREATE VIEW with_timestamp AS (  
  (SELECT ts, value FROM my_view ORDER BY ts) timestamp(ts)  
)
```

## Errors[​](#errors "Direct link to Errors")

| Error | Cause |
| --- | --- |
| `view already exists` | View exists and `IF NOT EXISTS` not specified |
| `table does not exist` | Referenced table doesn't exist |
| `Invalid column` | Column in query doesn't exist |
| `circular dependency detected` | View would create circular reference |
| `variable is not overridable` | Attempted to override a non-`OVERRIDABLE` DECLARE variable |

## View naming[​](#view-naming "Direct link to View naming")

View names follow the same rules as table names:

* Case-insensitive
* Unicode characters supported
* Cannot be the same as an existing table or materialized view name
* Reserved SQL keywords require quoting

Quoting reserved words

```prism-code
CREATE VIEW 'select' AS (...)    -- Quoted reserved word  
CREATE VIEW 'My View' AS (...)   -- Quoted name with spaces
```

## OWNED BY (Enterprise)[​](#owned-by-enterprise "Direct link to OWNED BY (Enterprise)")

When a user creates a new view, they are automatically assigned all view level
permissions with the `GRANT` option for that view. This behavior can be
overridden using `OWNED BY`.

```prism-code
CREATE GROUP analysts;  
CREATE VIEW trades_summary AS (  
  SELECT ts, symbol, sum(quantity) as volume  
  FROM trades  
  SAMPLE BY 1h  
)  
OWNED BY 'analysts';
```

## See also[​](#see-also "Direct link to See also")

* [Views concept](/docs/concepts/views/)
* [ALTER VIEW](/docs/query/sql/alter-view/)
* [DROP VIEW](/docs/query/sql/drop-view/)
* [COMPILE VIEW](/docs/query/sql/compile-view/)
* [DECLARE](/docs/query/sql/declare/)