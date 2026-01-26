On this page

Manually triggers recompilation of a view to validate its definition against the
current database state.

**This command is optional.** Views are automatically compiled when queried, so
you don't need to run `COMPILE VIEW` for normal operation. Use it when you want
to validate a view without executing it, or to check if schema changes have
broken a view.

For more information on views, see the [Views](/docs/concepts/views/)
documentation.

## Syntax[​](#syntax "Direct link to Syntax")

```prism-code
COMPILE VIEW view_name
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parameter | Description |
| --- | --- |
| `view_name` | Name of the view to compile |

## Examples[​](#examples "Direct link to Examples")

### Validate a view[​](#validate-a-view "Direct link to Validate a view")

Compile view

```prism-code
COMPILE VIEW my_view
```

### Check and fix invalid view[​](#check-and-fix-invalid-view "Direct link to Check and fix invalid view")

Diagnose and compile view

```prism-code
-- Check view status  
SELECT view_name, view_status, invalidation_reason  
FROM views()  
WHERE view_name = 'my_view';  
  
-- If invalid, fix the underlying issue, then compile  
COMPILE VIEW my_view;  
  
-- Verify it's now valid  
SELECT view_status FROM views() WHERE view_name = 'my_view';
```

### Bulk view repair[​](#bulk-view-repair "Direct link to Bulk view repair")

When multiple views are broken due to schema changes:

Compile multiple views

```prism-code
-- Find all invalid views  
SELECT view_name, invalidation_reason  
FROM views()  
WHERE view_status = 'invalid';  
  
-- Compile each view after fixing underlying issues  
COMPILE VIEW view1;  
COMPILE VIEW view2;  
COMPILE VIEW view3;
```

## Behavior[​](#behavior "Direct link to Behavior")

* If the view compiles successfully, its status becomes `valid`
* If the view fails to compile, its status becomes `invalid` and the reason is
  stored in `invalidation_reason`
* Compiling an already valid view re-validates it against current schema
* Dependent views (views that reference the compiled view) are also recompiled
  recursively

### Automatic compilation[​](#automatic-compilation "Direct link to Automatic compilation")

Views are **automatically compiled** in these situations:

* **On query**: When you `SELECT` from a view, it is compiled if needed
* **On schema fix**: When a dropped table is recreated or a renamed column is
  renamed back
* **Background job**: A background job periodically recompiles invalid views

Because of automatic compilation, `COMPILE VIEW` is rarely needed for normal
operation.

### When to use COMPILE VIEW[​](#when-to-use-compile-view "Direct link to When to use COMPILE VIEW")

Use `COMPILE VIEW` when you want to:

1. **Validate without executing**: Check if a view is valid without running the
   actual query
2. **Pre-validate after schema changes**: Verify views work before users hit
   errors
3. **Update metadata**: Force view metadata refresh after column type changes
4. **Diagnose issues**: Check why a view is invalid by triggering compilation
   errors

## Errors[​](#errors "Direct link to Errors")

| Error | Cause |
| --- | --- |
| `view does not exist [view=name]` | View with specified name doesn't exist |
| `table does not exist [table=name]` | View references a table that doesn't exist |
| `Invalid column` | View references a column that doesn't exist |
| `Access denied [COMPILE VIEW on view_name]` | User lacks permission (Enterprise) |

## Permissions (Enterprise)[​](#permissions-enterprise "Direct link to Permissions (Enterprise)")

Compiling a view requires the `COMPILE VIEW` permission on that view:

```prism-code
-- Grant COMPILE VIEW permission  
GRANT COMPILE VIEW ON my_view TO username;  
  
-- Grant on multiple views  
GRANT COMPILE VIEW ON view1, view2 TO username;
```

Note: `COMPILE VIEW` does **not** require `SELECT` permission on the underlying
tables. The compilation validates the view definition using system privileges,
not user privileges.

## See also[​](#see-also "Direct link to See also")

* [Views concept](/docs/concepts/views/)
* [CREATE VIEW](/docs/query/sql/create-view/)
* [ALTER VIEW](/docs/query/sql/alter-view/)
* [DROP VIEW](/docs/query/sql/drop-view/)