On this page

Adds an [index](/docs/concepts/deep-dive/indexes/) to a
[`SYMBOL`](/docs/concepts/symbol/) column in a materialized view, improving
query performance for filtered lookups.

## Syntax[​](#syntax "Direct link to Syntax")

```prism-code
ALTER MATERIALIZED VIEW viewName ALTER COLUMN columnName ADD INDEX [ CAPACITY n ]
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parameter | Description |
| --- | --- |
| `viewName` | Name of the materialized view |
| `columnName` | Name of the `SYMBOL` column to index |
| `CAPACITY` | Optional index capacity (advanced; use default unless you understand implications) |

## When to use[​](#when-to-use "Direct link to When to use")

Add an index when:

* Queries frequently filter by a `SYMBOL` column (e.g., `WHERE symbol = 'BTC-USD'`)
* The column has high cardinality (many distinct values)
* Query performance on the materialized view needs improvement

## Example[​](#example "Direct link to Example")

Add index to symbol column

```prism-code
ALTER MATERIALIZED VIEW trades_hourly  
  ALTER COLUMN symbol ADD INDEX;
```

## Behavior[​](#behavior "Direct link to Behavior")

| Aspect | Description |
| --- | --- |
| Operation type | Atomic, non-blocking, non-waiting |
| Immediate effect | SQL optimizer starts using the index once created |
| Column requirement | Column must be of type `SYMBOL` |

note

Index capacity and [symbol capacity](/docs/concepts/symbol/) are different
settings. Only change index capacity if you understand the
[implications](/docs/concepts/deep-dive/indexes/#index-capacity).

## Permissions (Enterprise)[​](#permissions-enterprise "Direct link to Permissions (Enterprise)")

Adding an index requires the `ALTER MATERIALIZED VIEW` permission:

Grant alter permission

```prism-code
GRANT ALTER MATERIALIZED VIEW ON trades_hourly TO user1;
```

## Errors[​](#errors "Direct link to Errors")

| Error | Cause |
| --- | --- |
| `materialized view does not exist` | View with specified name doesn't exist |
| `column does not exist` | Column not found in the view |
| `column is not a symbol` | Index can only be added to `SYMBOL` columns |
| `index already exists` | Column is already indexed |
| `permission denied` | Missing `ALTER MATERIALIZED VIEW` permission (Enterprise) |

## See also[​](#see-also "Direct link to See also")

* [Materialized views concept](/docs/concepts/materialized-views/)
* [Index concept](/docs/concepts/deep-dive/indexes/)
* [Symbol type](/docs/concepts/symbol/)
* [ALTER MATERIALIZED VIEW DROP INDEX](/docs/query/sql/alter-mat-view-alter-column-drop-index/)
* [ALTER TABLE ADD INDEX](/docs/query/sql/alter-table-alter-column-add-index/)