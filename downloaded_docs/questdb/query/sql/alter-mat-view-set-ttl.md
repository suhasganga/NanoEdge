On this page

Sets the [time-to-live](/docs/concepts/ttl/) (TTL) period on a materialized
view, automatically dropping partitions older than the specified duration.

## Syntax[​](#syntax "Direct link to Syntax")

```prism-code
ALTER MATERIALIZED VIEW viewName SET TTL n timeUnit
```

Where `timeUnit` is: `HOURS | DAYS | WEEKS | MONTHS | YEARS` (or shorthand:
`h`, `d`, `w`, `M`, `y`)

## Parameters[​](#parameters "Direct link to Parameters")

| Parameter | Description |
| --- | --- |
| `viewName` | Name of the materialized view to modify |
| `n` | Number of time units to retain |
| `timeUnit` | Time unit for the retention period |

## When to use[​](#when-to-use "Direct link to When to use")

Set a TTL when:

* You only need recent aggregated data (e.g., last 30 days)
* Disk space is a concern for long-running views
* Compliance requires automatic data expiration

## How it works[​](#how-it-works "Direct link to How it works")

QuestDB automatically drops partitions that exceed the TTL. Data removal happens
at partition boundaries, not row-by-row.

note

The TTL period must be a whole number multiple of the view's partition size.
For example, a view with `PARTITION BY DAY` can have `TTL 7 DAYS` but not
`TTL 36 HOURS`.

## Time units[​](#time-units "Direct link to Time units")

| Unit | Singular | Plural | Shorthand |
| --- | --- | --- | --- |
| Hours | `HOUR` | `HOURS` | `h` |
| Days | `DAY` | `DAYS` | `d` |
| Weeks | `WEEK` | `WEEKS` | `w` |
| Months | `MONTH` | `MONTHS` | `M` |
| Years | `YEAR` | `YEARS` | `y` |

## Examples[​](#examples "Direct link to Examples")

Keep 3 days of data

```prism-code
ALTER MATERIALIZED VIEW trades_hourly SET TTL 3 DAYS;
```

Keep 12 hours of data (shorthand)

```prism-code
ALTER MATERIALIZED VIEW trades_hourly SET TTL 12h;
```

Keep 1 year of data

```prism-code
ALTER MATERIALIZED VIEW trades_daily SET TTL 1 YEAR;
```

## Behavior[​](#behavior "Direct link to Behavior")

| Aspect | Description |
| --- | --- |
| Granularity | Data dropped at partition boundaries only |
| Independence | View TTL is separate from base table TTL |
| Immediate effect | Expired partitions dropped on next maintenance cycle |

## Permissions (Enterprise)[​](#permissions-enterprise "Direct link to Permissions (Enterprise)")

Changing TTL requires the `ALTER MATERIALIZED VIEW` permission:

Grant alter permission

```prism-code
GRANT ALTER MATERIALIZED VIEW ON trades_hourly TO user1;
```

## Errors[​](#errors "Direct link to Errors")

| Error | Cause |
| --- | --- |
| `materialized view does not exist` | View with specified name doesn't exist |
| `invalid TTL` | TTL not a multiple of partition size |
| `invalid time unit` | Unrecognized time unit |
| `permission denied` | Missing `ALTER MATERIALIZED VIEW` permission (Enterprise) |

## See also[​](#see-also "Direct link to See also")

* [Materialized views concept](/docs/concepts/materialized-views/)
* [TTL concept](/docs/concepts/ttl/)
* [ALTER TABLE SET TTL](/docs/query/sql/alter-table-set-ttl/)
* [CREATE MATERIALIZED VIEW](/docs/query/sql/create-mat-view/)