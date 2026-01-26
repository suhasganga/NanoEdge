On this page

This page describes the available functions related to UUID data type.

## to\_uuid[​](#to_uuid "Direct link to to_uuid")

`to_uuid(value, value)` combines two 64-bit `long` into a single 128-bit `uuid`.

### Arguments[​](#arguments "Direct link to Arguments")

* `value` is any `long`

### Return value[​](#return-value "Direct link to Return value")

Return value type is `uuid`.

### Examples[​](#examples "Direct link to Examples")

```prism-code
SELECT to_uuid(2, 1)  
AS uuid FROM long_sequence(1);
```

Returns:

```prism-code
00000000-0000-0001-0000-000000000002
```