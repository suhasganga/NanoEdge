On this page

Changes a materialized view's refresh strategy and parameters without recreating
the view.

## Syntax[​](#syntax "Direct link to Syntax")

```prism-code
ALTER MATERIALIZED VIEW viewName SET REFRESH  
[ IMMEDIATE | MANUAL | EVERY interval [ START timestamp ] [ TIME ZONE timezone ] ]  
[ PERIOD ( LENGTH length [ TIME ZONE timezone ] [ DELAY delay ] ) ]  
[ PERIOD ( SAMPLE BY INTERVAL ) ]
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parameter | Description |
| --- | --- |
| `viewName` | Name of the materialized view to modify |
| `IMMEDIATE` | Refresh after each base table transaction |
| `MANUAL` | Refresh only when explicitly triggered |
| `EVERY interval` | Refresh on a timer (e.g., `10m`, `1h`, `1d`) |
| `START timestamp` | When to begin the timer schedule |
| `TIME ZONE` | Timezone for schedule alignment |
| `PERIOD LENGTH` | Define fixed-length refresh periods |
| `PERIOD SAMPLE BY INTERVAL` | Match period to the view's `SAMPLE BY` interval |
| `DELAY` | Grace period before period closes |

## When to use[​](#when-to-use "Direct link to When to use")

Change refresh strategy when:

* Switching from real-time (`IMMEDIATE`) to batched (`EVERY`) for performance
* Adding period-based refresh for data that arrives at fixed intervals
* Switching to `MANUAL` for full control during maintenance windows

## Examples[​](#examples "Direct link to Examples")

### Switch to timer-based refresh[​](#switch-to-timer-based-refresh "Direct link to Switch to timer-based refresh")

Refresh every 12 hours

```prism-code
ALTER MATERIALIZED VIEW trades_hourly  
SET REFRESH EVERY 12h START '2025-12-31T00:00:00Z' TIME ZONE 'Europe/London';
```

### Add period-based refresh[​](#add-period-based-refresh "Direct link to Add period-based refresh")

Daily periods with 1-hour delay for late data

```prism-code
ALTER MATERIALIZED VIEW trades_daily  
SET REFRESH PERIOD (LENGTH 1d DELAY 1h);
```

### Match period to SAMPLE BY[​](#match-period-to-sample-by "Direct link to Match period to SAMPLE BY")

Period matches view's aggregation interval

```prism-code
ALTER MATERIALIZED VIEW trades_hourly  
SET REFRESH PERIOD (SAMPLE BY INTERVAL);
```

### Switch to immediate refresh[​](#switch-to-immediate-refresh "Direct link to Switch to immediate refresh")

Real-time refresh

```prism-code
ALTER MATERIALIZED VIEW trades_hourly SET REFRESH IMMEDIATE;
```

### Switch to manual refresh[​](#switch-to-manual-refresh "Direct link to Switch to manual refresh")

Manual control

```prism-code
ALTER MATERIALIZED VIEW trades_hourly SET REFRESH MANUAL;
```

## Behavior[​](#behavior "Direct link to Behavior")

| Aspect | Description |
| --- | --- |
| Existing data | Preserved; only future refresh behavior changes |
| Pending refresh | Completes before new strategy takes effect |
| Timer reset | `EVERY` schedule resets based on `START` time |

## Permissions (Enterprise)[​](#permissions-enterprise "Direct link to Permissions (Enterprise)")

Changing refresh settings requires the `ALTER MATERIALIZED VIEW` permission:

Grant alter permission

```prism-code
GRANT ALTER MATERIALIZED VIEW ON trades_hourly TO user1;
```

## Errors[​](#errors "Direct link to Errors")

| Error | Cause |
| --- | --- |
| `materialized view does not exist` | View with specified name doesn't exist |
| `invalid interval` | Timer interval is invalid or below minimum (`1m`) |
| `permission denied` | Missing `ALTER MATERIALIZED VIEW` permission (Enterprise) |

## See also[​](#see-also "Direct link to See also")

* [Materialized views concept](/docs/concepts/materialized-views/)
* [CREATE MATERIALIZED VIEW](/docs/query/sql/create-mat-view/)
* [REFRESH MATERIALIZED VIEW](/docs/query/sql/refresh-mat-view/)