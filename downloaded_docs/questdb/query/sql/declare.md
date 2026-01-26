On this page

`DECLARE` specifies a series of variable bindings used throughout your query.

This syntax is supported within `SELECT` queries.

## Syntax[​](#syntax "Direct link to Syntax")

![Flow chart showing the syntax of the DECLARE keyword](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2OTEiIGhlaWdodD0iMTEzIj4KICAgIDxkZWZzPgogICAgICAgIDxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+CiAgICAgICAgICAgIEBuYW1lc3BhY2UgImh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIjsKICAgICAgICAgICAgLmxpbmUgICAgICAgICAgICAgICAgIHtmaWxsOiBub25lOyBzdHJva2U6ICM2MzYyNzM7fQogICAgICAgICAgICAuYm9sZC1saW5lICAgICAgICAgICAge3N0cm9rZTogIzYzNjI3Mzsgc2hhcGUtcmVuZGVyaW5nOiBjcmlzcEVkZ2VzOyBzdHJva2Utd2lkdGg6IDI7IH0KICAgICAgICAgICAgLnRoaW4tbGluZSAgICAgICAgICAge3N0cm9rZTogIzYzNjI3Mzsgc2hhcGUtcmVuZGVyaW5nOiBjcmlzcEVkZ2VzfQogICAgICAgICAgICAuZmlsbGVkICAgICAgICAgICAgICB7ZmlsbDogIzYzNjI3Mzsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgdGV4dC50ZXJtaW5hbCAgICAgICAge2ZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsICJTZWdvZSBVSSIsIFJvYm90bywgVWJ1bnR1LCBDYW50YXJlbGwsIEhlbHZldGljYSwgc2Fucy1zZXJpZjsKICAgICAgICAgICAgZm9udC1zaXplOiAxMnB4OwogICAgICAgICAgICBmaWxsOiAjZmZmZmZmOwogICAgICAgICAgICBmb250LXdlaWdodDogYm9sZDsKICAgICAgICAgICAgfQogICAgICAgICAgICB0ZXh0Lm5vbnRlcm1pbmFsICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICNlMjg5YTQ7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBub3JtYWw7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgdGV4dC5yZWdleHAgICAgICAgICAge2ZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsICJTZWdvZSBVSSIsIFJvYm90bywgVWJ1bnR1LCBDYW50YXJlbGwsIEhlbHZldGljYSwgc2Fucy1zZXJpZjsKICAgICAgICAgICAgZm9udC1zaXplOiAxMnB4OwogICAgICAgICAgICBmaWxsOiAjMDAxNDFGOwogICAgICAgICAgICBmb250LXdlaWdodDogbm9ybWFsOwogICAgICAgICAgICB9CiAgICAgICAgICAgIHJlY3QsIGNpcmNsZSwgcG9seWdvbiB7ZmlsbDogbm9uZTsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgcmVjdC50ZXJtaW5hbCAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogI2JlMmY1Yjt9CiAgICAgICAgICAgIHJlY3Qubm9udGVybWluYWwgICAgIHtmaWxsOiByZ2JhKDI1NSwyNTUsMjU1LDAuMSk7IHN0cm9rZTogbm9uZTt9CiAgICAgICAgICAgIHJlY3QudGV4dCAgICAgICAgICAgIHtmaWxsOiBub25lOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICBwb2x5Z29uLnJlZ2V4cCAgICAgICB7ZmlsbDogI0M3RUNGRjsgc3Ryb2tlOiAjMDM4Y2JjO30KICAgICAgICA8L3N0eWxlPgogICAgPC9kZWZzPgogICAgPHBvbHlnb24gcG9pbnRzPSI5IDYxIDEgNTcgMSA2NSI+PC9wb2x5Z29uPgogICAgICAgICA8cG9seWdvbiBwb2ludHM9IjE3IDYxIDkgNTcgOSA2NSI+PC9wb2x5Z29uPgogICAgICAgICA8cmVjdCB4PSIzMSIgeT0iNDciIHdpZHRoPSI4MiIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjI5IiB5PSI0NSIgd2lkdGg9IjgyIiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjM5IiB5PSI2NSI+REVDTEFSRTwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iMTUzIiB5PSI0NyIgd2lkdGg9Ijg2IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMTUxIiB5PSI0NSIgd2lkdGg9Ijg2IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjE2MSIgeT0iNjUiPkB2YXJpYWJsZTwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iMjU5IiB5PSI0NyIgd2lkdGg9IjM0IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMjU3IiB5PSI0NSIgd2lkdGg9IjM0IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjI2NyIgeT0iNjUiPjo9PC90ZXh0PjxhIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4bGluazpocmVmPSIjZXhwcmVzc2lvbiIgeGxpbms6dGl0bGU9ImV4cHJlc3Npb24iPgogICAgICAgICAgICA8cmVjdCB4PSIzMTMiIHk9IjQ3IiB3aWR0aD0iOTAiIGhlaWdodD0iMzIiPjwvcmVjdD4KICAgICAgICAgICAgPHJlY3QgeD0iMzExIiB5PSI0NSIgd2lkdGg9IjkwIiBoZWlnaHQ9IjMyIiBjbGFzcz0ibm9udGVybWluYWwiPjwvcmVjdD4KICAgICAgICAgICAgPHRleHQgY2xhc3M9Im5vbnRlcm1pbmFsIiB4PSIzMjEiIHk9IjY1Ij5leHByZXNzaW9uPC90ZXh0PjwvYT48cmVjdCB4PSIxNTMiIHk9IjMiIHdpZHRoPSIyNCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjE1MSIgeT0iMSIgd2lkdGg9IjI0IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjE2MSIgeT0iMjEiPiw8L3RleHQ+PGEgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhsaW5rOmhyZWY9IiN3aXRoRXhwciIgeGxpbms6dGl0bGU9IndpdGhFeHByIj4KICAgICAgICAgICAgPHJlY3QgeD0iNDYzIiB5PSI3OSIgd2lkdGg9Ijc0IiBoZWlnaHQ9IjMyIj48L3JlY3Q+CiAgICAgICAgICAgIDxyZWN0IHg9IjQ2MSIgeT0iNzciIHdpZHRoPSI3NCIgaGVpZ2h0PSIzMiIgY2xhc3M9Im5vbnRlcm1pbmFsIj48L3JlY3Q+CiAgICAgICAgICAgIDx0ZXh0IGNsYXNzPSJub250ZXJtaW5hbCIgeD0iNDcxIiB5PSI5NyI+d2l0aEV4cHI8L3RleHQ+PC9hPjxhIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4bGluazpocmVmPSIjc2VsZWN0RXhwciIgeGxpbms6dGl0bGU9InNlbGVjdEV4cHIiPgogICAgICAgICAgICA8cmVjdCB4PSI1NzciIHk9IjQ3IiB3aWR0aD0iODYiIGhlaWdodD0iMzIiPjwvcmVjdD4KICAgICAgICAgICAgPHJlY3QgeD0iNTc1IiB5PSI0NSIgd2lkdGg9Ijg2IiBoZWlnaHQ9IjMyIiBjbGFzcz0ibm9udGVybWluYWwiPjwvcmVjdD4KICAgICAgICAgICAgPHRleHQgY2xhc3M9Im5vbnRlcm1pbmFsIiB4PSI1ODUiIHk9IjY1Ij5zZWxlY3RFeHByPC90ZXh0PjwvYT48cGF0aCBjbGFzcz0ibGluZSIgZD0ibTE3IDYxIGgyIG0wIDAgaDEwIG04MiAwIGgxMCBtMjAgMCBoMTAgbTg2IDAgaDEwIG0wIDAgaDEwIG0zNCAwIGgxMCBtMCAwIGgxMCBtOTAgMCBoMTAgbS0yOTAgMCBsMjAgMCBtLTEgMCBxLTkgMCAtOSAtMTAgbDAgLTI0IHEwIC0xMCAxMCAtMTAgbTI3MCA0NCBsMjAgMCBtLTIwIDAgcTEwIDAgMTAgLTEwIGwwIC0yNCBxMCAtMTAgLTEwIC0xMCBtLTI3MCAwIGgxMCBtMjQgMCBoMTAgbTAgMCBoMjI2IG00MCA0NCBoMTAgbTAgMCBoODQgbS0xMTQgMCBoMjAgbTk0IDAgaDIwIG0tMTM0IDAgcTEwIDAgMTAgMTAgbTExNCAwIHEwIC0xMCAxMCAtMTAgbS0xMjQgMTAgdjEyIG0xMTQgMCB2LTEyIG0tMTE0IDEyIHEwIDEwIDEwIDEwIG05NCAwIHExMCAwIDEwIC0xMCBtLTEwNCAxMCBoMTAgbTc0IDAgaDEwIG0yMCAtMzIgaDEwIG04NiAwIGgxMCBtMyAwIGgtMyI+PC9wYXRoPgogICAgICAgICA8cG9seWdvbiBwb2ludHM9IjY4MSA2MSA2ODkgNTcgNjg5IDY1Ij48L3BvbHlnb24+CiAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iNjgxIDYxIDY3MyA1NyA2NzMgNjUiPjwvcG9seWdvbj4KPC9zdmc+)

## Mechanics[​](#mechanics "Direct link to Mechanics")

The `DECLARE` keyword comes before the `SELECT` clause in your query:

Basic DECLARE[Demo this query](https://demo.questdb.io/?query=DECLARE%0A%20%20%20%20%40x%20%3A%3D%205%0ASELECT%20%40x%3B&executeQuery=true)

```prism-code
DECLARE  
    @x := 5  
SELECT @x;
```

Use the variable binding operator `:=` (walrus) to associate expressions to names.

tip

It is easy to accidentally omit the `:` when writing variable binding expressions.

Don't confuse the `:=` operator with a simple equality `=`!

You should see an error message like this:

> expected variable assignment operator `:=`

The above example declares a single binding, which states that the variable `@x` is replaced with the constant integer `5`.

The variables are resolved at parse-time, meaning that the variable is no longer present
when the query is compiled.

So the above example reduces to this simple query:

basic DECLARE post-reduction[Demo this query](https://demo.questdb.io/?query=SELECT%205%3B&executeQuery=true)

```prism-code
SELECT 5;
```

| 5 |
| --- |
| 5 |

### Multiple bindings[​](#multiple-bindings "Direct link to Multiple bindings")

To declare multiple variables, set the bind expressions with commas `,`:

Multiple variable bindings[Demo this query](https://demo.questdb.io/?query=DECLARE%0A%20%20%20%20%40x%20%3A%3D%205%2C%0A%20%20%20%20%40y%20%3A%3D%202%0ASELECT%20%40x%20%2B%20%40y%3B&executeQuery=true)

```prism-code
DECLARE  
    @x := 5,  
    @y := 2  
SELECT @x + @y;
```

| column |
| --- |
| 7 |

### Variables as functions[​](#variables-as-functions "Direct link to Variables as functions")

A variable need not be just a constant. It could also be a function call,
and variables with function values can be nested:

declaring function variable[Demo this query](https://demo.questdb.io/?query=DECLARE%0A%20%20%40today%20%3A%3D%20today()%2C%0A%20%20%40start%20%3A%3D%20interval_start(%40today)%2C%0A%20%20%40end%20%3A%3D%20interval_end(%40today)%0ASELECT%20%40today%20%3D%20interval(%40start%2C%20%40end)%3B&executeQuery=true)

```prism-code
DECLARE  
  @today := today(),  
  @start := interval_start(@today),  
  @end := interval_end(@today)  
SELECT @today = interval(@start, @end);
```

| column |
| --- |
| true |

### Declarations in subqueries[​](#declarations-in-subqueries "Direct link to Declarations in subqueries")

Declarations made in parent queries are available in subqueries.

variable shadowing[Demo this query](https://demo.questdb.io/?query=DECLARE%0A%20%20%20%20%40x%20%3A%3D%205%0ASELECT%20y%20FROM%20(%0A%20%20%20%20SELECT%20%40x%20AS%20y%0A)%3B&executeQuery=true)

```prism-code
DECLARE  
    @x := 5  
SELECT y FROM (  
    SELECT @x AS y  
);
```

| y |
| --- |
| 5 |

#### Shadowing[​](#shadowing "Direct link to Shadowing")

If a subquery declares a variable of the same name, then the variable is shadowed
and takes on the new value.

However, any queries above this subquery are unaffected - the
variable bind is not globally mutated.

variable shadowing[Demo this query](https://demo.questdb.io/?query=DECLARE%0A%20%20%20%20%40x%20%3A%3D%205%0ASELECT%20%40x%20%2B%20y%20FROM%20(%0A%20%20%20%20DECLARE%20%40x%20%3A%3D%2010%0A%20%20%20%20SELECT%20%40x%20AS%20y%0A)%3B&executeQuery=true)

```prism-code
DECLARE  
    @x := 5  
SELECT @x + y FROM (  
    DECLARE @x := 10  
    SELECT @x AS y  
);
```

| column |
| --- |
| 15 |

### Declarations as subqueries[​](#declarations-as-subqueries "Direct link to Declarations as subqueries")

Declarations themselves can be subqueries.

We suggest that this is not overused, as removing the subquery definition from its execution
location may make queries harder to debug.

Nevertheless, it is possible to define a variable as a subquery:

table cursor as a variable[Demo this query](https://demo.questdb.io/?query=DECLARE%0A%20%20%20%20%40subquery%20%3A%3D%20(SELECT%20timestamp%20FROM%20trades)%0ASELECT%20*%20FROM%20%40subquery%3B&executeQuery=true)

```prism-code
DECLARE  
    @subquery := (SELECT timestamp FROM trades)  
SELECT * FROM @subquery;
```

You can even use already-declared variables to define your subquery variable:

nesting decls inside decl subqueries[Demo this query](https://demo.questdb.io/?query=DECLARE%0A%20%20%20%20%40timestamp%20%3A%3D%20timestamp%2C%0A%20%20%20%20%40symbol%20%3A%3D%20symbol%2C%0A%20%20%20%20%40subquery%20%3A%3D%20(SELECT%20%40timestamp%2C%20%40symbol%20FROM%20trades)%0ASELECT%20*%20FROM%20%40subquery%3B&executeQuery=true)

```prism-code
DECLARE  
    @timestamp := timestamp,  
    @symbol := symbol,  
    @subquery := (SELECT @timestamp, @symbol FROM trades)  
SELECT * FROM @subquery;
```

### Declarations in CTEs[​](#declarations-in-ctes "Direct link to Declarations in CTEs")

Naturally, `DECLARE` also works with CTEs:

declarations inside CTEs[Demo this query](https://demo.questdb.io/?query=DECLARE%0A%20%20%40x%20%3A%3D%205%0AWITH%20first%20AS%20(%0A%20%20DECLARE%20%40x%20%3A%3D%2010%0A%20%20SELECT%20%40x%20as%20a%20--%20a%20%3D%2010%0A)%2C%0Asecond%20AS%20(%0A%20%20DECLARE%20%40y%20%3A%3D%204%0A%20%20SELECT%0A%20%20%20%20%40x%20%2B%20%40y%20as%20b%2C%20--%20b%20%3D%205%20%2B%204%20%3D%209%0A%20%20%20%20a%20--%20a%20%3D%2010%0A%20%20%20%20FROM%20first%0A)%0ASELECT%20a%2C%20b%0AFROM%20second%3B&executeQuery=true)

```prism-code
DECLARE  
  @x := 5  
WITH first AS (  
  DECLARE @x := 10  
  SELECT @x as a -- a = 10  
),  
second AS (  
  DECLARE @y := 4  
  SELECT  
    @x + @y as b, -- b = 5 + 4 = 9  
    a -- a = 10  
    FROM first  
)  
SELECT a, b  
FROM second;
```

| a | b |
| --- | --- |
| 10 | 9 |

### Bind variables[​](#bind-variables "Direct link to Bind variables")

`DECLARE` syntax will work with prepared statements over PG Wire, so long as the client library
does not perform syntax validation that rejects the `DECLARE` syntax:

```prism-code
DECLARE @x := ?, @y := ?  
SELECT @x::int + @y::int;  
  
-- Then bind the following values: (1, 2)
```

| column |
| --- |
| 3 |

This can be useful to minimise repeated bind variables.

For example, rather than passing the same value to multiple positional arguments,
you could instead use a declared variable and send a single bind variable:

```prism-code
-- instead of this:  
SELECT ? as name, id FROM users WHERE name = ?;  
  
-- do this:  
DECLARE @name := ?  
SELECT @name as name, id FROM users WHERE name = @name;
```

Or for repeating columns:

```prism-code
DECLARE  
    @col = ?,  
    @symbol = ?  
SELECT avg(@col), min(@col), max(@col)  
FROM trades  
WHERE symbol = @symbol;
```

## Limitations[​](#limitations "Direct link to Limitations")

Most basic expressions are supported, and we provide examples later in this document.

We suggest you use variables to simplify repeated constants within your code, and minimise
how many places you need to update the constant.

### Disallowed expressions[​](#disallowed-expressions "Direct link to Disallowed expressions")

However, not all expressions are supported. The following are explicitly disallowed:

#### Bracket lists[​](#bracket-lists "Direct link to Bracket lists")

bracket lists are not allowed

```prism-code
DECLARE  
    @symbols := ('BTC-USDT', 'ETH-USDT')  
SELECT timestamp, price, symbol  
FROM trades  
WHERE symbol IN @symbols;  
  
-- error: unexpected bind expression - bracket lists not supported
```

#### SQL statement fragments[​](#sql-statement-fragments "Direct link to SQL statement fragments")

sql fragments are not allowed

```prism-code
DECLARE  
    @x := FROM trades  
SELECT 5 @x;  
  
-- table and column names that are SQL keywords have to be enclosed in double quotes, such as "FROM"```
```

### Language client support[​](#language-client-support "Direct link to Language client support")

Some language SQL clients do not allow identifiers to be passed as if it was a normal value. One example is `psycopg`.
In this case, you should use an alternate API to splice in identifiers, for example:

psycopg

```prism-code
cur.execute(  
    sql.SQL("""  
        DECLARE @col := {}  
        SELECT max(@col), min(@col), avg(price)  
        FROM btc_trades;  
    """).format(sql.Identifier('price')))
```

## Examples[​](#examples "Direct link to Examples")

### SAMPLE BY[​](#sample-by "Direct link to SAMPLE BY")

DECLARE with SAMPLE BY[Demo this query](https://demo.questdb.io/?query=DECLARE%0A%20%20%20%20%40period%20%3A%3D%201m%2C%0A%20%20%20%20%40window%20%3A%3D%20'2024-11-25'%2C%0A%20%20%20%20%40symbol%20%3A%3D%20'ETH-USDT'%0ASELECT%0A%20%20%20timestamp%2C%20symbol%2C%20side%2C%20sum(amount)%20as%20volume%0AFROM%20trades%0AWHERE%20side%20%3D%20'sell'%0AAND%20timestamp%20IN%20%40window%0AAND%20symbol%20%3D%20%40symbol%0ASAMPLE%20BY%20%40period%0AFILL(NULL)%3B&executeQuery=true)

```prism-code
DECLARE  
    @period := 1m,  
    @window := '2024-11-25',  
    @symbol := 'ETH-USDT'  
SELECT  
   timestamp, symbol, side, sum(amount) as volume  
FROM trades  
WHERE side = 'sell'  
AND timestamp IN @window  
AND symbol = @symbol  
SAMPLE BY @period  
FILL(NULL);
```

| timestamp | symbol | side | volume |
| --- | --- | --- | --- |
| 2024-11-25T00:00:00.000000Z | ETH-USDT | sell | 153.470574999999 |
| 2024-11-25T00:01:00.000000Z | ETH-USDT | sell | 298.927738 |
| 2024-11-25T00:02:00.000000Z | ETH-USDT | sell | 66.253058 |
| ... | ... | ... | ... |

### INSERT INTO SELECT[​](#insert-into-select "Direct link to INSERT INTO SELECT")

```prism-code
INSERT INTO trades (timestamp, symbol)  
SELECT * FROM  
(  
    DECLARE  
        @x := now(),  
        @y := 'ETH-USDT'  
    SELECT @x as timestamp, @y as symbol  
);
```

### CREATE TABLE AS SELECT[​](#create-table-as-select "Direct link to CREATE TABLE AS SELECT")

```prism-code
CREATE TABLE trades AS (  
    DECLARE  
        @x := now(),  
        @y := 'ETH-USDT'  
    SELECT @x as timestamp, @y as symbol, 123 as price  
);
```