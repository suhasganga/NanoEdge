On this page

This page lists the supported InfluxDB Line Protocol columnset value types and
details about type casting.

If a target column does not exist, QuestDB will create a column using the same
type that the ILP client sends.

Type casts that cause data loss will cause the entire line to be rejected.

## Integer[​](#integer "Direct link to Integer")

64-bit signed integer values, which correspond to QuestDB type `long`. The
values are required to have `i` suffix. For example:

```prism-code
temps,device=cpu,location=south value=96i 1638202821000000000\n
```

Sometimes integer values are small and do not warrant 64 bits to store them. To
reduce storage for such values it is possible to create a table upfront with
smaller type, for example:

```prism-code
CREATE TABLE temps (device SYMBOL, location SYMBOL, value SHORT);
```

The line above will be accepted and `96i` will be cast to `short`.

### Cast table[​](#cast-table "Direct link to Cast table")

The following `cast` operations are supported when the existing table column
type is not `long`:

|  | `byte` | `short` | `int` | `long` | `float` | `double` | `date` | `timestamp` | `decimal` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `integer` | cast | cast | cast | `native` | cast | cast | cast | cast | cast |

## Long256[​](#long256 "Direct link to Long256")

Custom type, which corresponds to QuestDB type `long256`. The values are hex
encoded 256-bit unsigned integer values with `i` suffix. For example:

```prism-code
temps,device=cpu,location=south value=0x123a4i 1638202821000000000\n
```

When column does not exist, it will be created with type `long256`. Values
overflowing 256-bit integer will cause the entire line to be rejected.

`long256` cannot be cast to anything else.

## Float[​](#float "Direct link to Float")

These values correspond to QuestDB type `double`. They actually do not have any
suffix, which might lead to a confusion. For example:

```prism-code
trade,ticker=BTCUSD price=30 1638202821000000000\n
```

`price` value will be stored as `double` even though it does not look like a
conventional double value would.

### Cast table[​](#cast-table-1 "Direct link to Cast table")

The following `cast` operations are supported when the existing table column
type is not `double`:

|  | `float` | `double` | `decimal` |
| --- | --- | --- | --- |
| `float` | cast | `native` | cast |

## Decimal[​](#decimal "Direct link to Decimal")

Decimal values, which correspond to QuestDB type `decimal`. The values are
required to have a `d` suffix. For example:

```prism-code
trade,ticker=BTCUSD price=30000.50d 1638202821000000000\n
```

When the column does not exist, it will be created with the `decimal` type using
the default precision of 18 and scale of 3. To specify custom precision and
scale, create the table upfront:

```prism-code
CREATE TABLE trade (ticker SYMBOL, price DECIMAL(18, 2));
```

The line above will be accepted and `30000.50` will be stored as `decimal`.

### Cast table[​](#cast-table-2 "Direct link to Cast table")

The following `cast` operations are supported when the existing table column
type is not `decimal`:

|  | `decimal` | `float` | `double` |
| --- | --- | --- | --- |
| `decimal` | `native` | cast | cast |

## Boolean[​](#boolean "Direct link to Boolean")

These values correspond to QuestDB type `boolean`. In InfluxDB Line Protocol
`boolean` values can be represented in any of the following ways:

| Actual value | Single char lowercase | Single char uppercase | Full lowercase | Full camelcase | Full uppercase |
| --- | --- | --- | --- | --- | --- |
| `true` | `t` | `T` | `true` | `True` | `TRUE` |
| `false` | `f` | `F` | `false` | `False` | `FALSE` |

Example:

```prism-code
sensors,location=south warning=false\n
```

### Cast table[​](#cast-table-3 "Direct link to Cast table")

The following `cast` operations are supported when the existing table column
type is not `boolean`:

|  | `boolean` | `byte` | `short` | `int` | `float` | `long` | `double` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `boolean` | `native` | cast | cast | cast | cast | cast | cast |

When cast to numeric type, boolean `true` is `1` and `false` is `0`

## String[​](#string "Direct link to String")

These values correspond to QuestDB type `varchar`. They must be enclosed in
quotes. The following characters in values must be escaped with a `\`: `"`,
`\n`, `\r` and `\`. For example:

```prism-code
trade,ticker=BTCUSD description="this is a \"rare\" value",user="John" 1638202821000000000\n
```

The result:

| timestamp | ticker | description | user |
| --- | --- | --- | --- |
| 1638202821000000000 | BTCUSD | this is a "rare" value | John |

note

String values must be UTF-8 encoded before sending.

### Cast table[​](#cast-table-4 "Direct link to Cast table")

The following `cast` operations are supported when the existing table column
type is not `varchar`:

|  | `varchar` | `char` | `string` | `geohash` | `symbol` | `uuid` | `decimal` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `string` | `native` | cast | cast | cast | cast | cast | cast |

### Cast to CHAR[​](#cast-to-char "Direct link to Cast to CHAR")

String value can be cast to `char` type if its length is less than 2 characters.
The following examples are valid lines:

```prism-code
trade,ticker=BTCUSD status="A" 1638202821000000000\n  
trade,ticker=BTCUSD status="" 1638202821000000001\n
```

The result:

| timestamp | ticker | status |
| --- | --- | --- |
| 1638202821000000000 | BTCUSD | A |
| 1638202821000000001 | BTCUSD | `null` |

Casting strings with 2 or more characters to `char` will cause the entire line
to be rejected.

### Cast to GEOHASH[​](#cast-to-geohash "Direct link to Cast to GEOHASH")

String value can be cast to `geohash` type when the destination column exists
and is of a `GEOHASH` type already. Do make sure that column is created upfront.
Otherwise, InfluxDB Line Protocol will create `STRING` column regardless of the
value.

Example:

Upcasting is an attempt to store higher resolution `geohash` in a lower
resolution column. Let's create table before sending a message. Our `geohash`
column has resolution of 4 bits.

```prism-code
CREATE TABLE tracking (  
    geohash GEOHASH(4b),  
    ts TIMESTAMP  
) TIMESTAMP(ts) PARTITION BY HOUR;
```

Send message including `16c` `geohash` value:

```prism-code
tracking,obj=VLCC\ STEPHANIE gh="9v1s8hm7wpkssv1h" 1000000000\n
```

The result: the `geohash` value has been truncated to size of the column.

| ts | gh |
| --- | --- |
| 1970-01-01T00:00:01.000000Z | 0100 |

Sending empty string value will insert `null` into `geohash` column of any size:

```prism-code
tracking,obj=VLCC\ STEPHANIE gh="" 2000000000\n
```

| ts | gh |
| --- | --- |
| 1970-01-01T00:00:01.000000Z | `null` |

note

Downcast of `geohash` value, which is inserting of lower resolution values into
higher resolution column, will cause the entire line to be rejected.

### Cast to SYMBOL[​](#cast-to-symbol "Direct link to Cast to SYMBOL")

The symbol values correspond to the QuestDB type
[`symbol`](/docs/concepts/symbol/). String values can be cast to the `symbol`
type when the destination column exists and its type is `symbol`. This gives
clients an option to populate `symbol` columns without knowing the type of the
columns.

```prism-code
CREATE TABLE trade (  
    ticker SYMBOL,  
    timestamp TIMESTAMP  
) TIMESTAMP(ts) PARTITION BY HOUR;
```

Send message including `BTCUSD` as `string`:

```prism-code
trade ticker="BTCUSD" 1638202821000000000\n  
trade ticker="BTCUSD" 1638402821000000000\n
```

The `ticker` column is populated with `symbol` values:

| timestamp | ticker |
| --- | --- |
| 2021-11-29T16:20:21.000000Z | BTCUSD |
| 2021-12-01T23:53:41.000000Z | BTCUSD |

We recommend sending `symbol` values directly as the `symbol` type because it
will automatically create a `symbol` column if it doesn't exist.

When sending `symbol` values as the `string` type and the column does not exist,
then it will be created as the `string` type.

### Cast to UUID[​](#cast-to-uuid "Direct link to Cast to UUID")

String values can be cast to the `uuid` type when all the following are true:

* The destination column exists.
* The destination column type is `uuid`.
* The `string` values are valid UUID.

```prism-code
CREATE TABLE trade (  
    ticker SYMBOL,  
    uuid UUID,  
    timestamp TIMESTAMP  
) TIMESTAMP(timestamp) PARTITION BY HOUR;
```

Send messages including the UUID value `a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11` as
`string`:

```prism-code
trade,ticker="BTCUSD" uuid="a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11" 1638202821000000000\n  
trade,ticker="BTCUSD" uuid="a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11" 1638402821000000000\n
```

The `uuid` column is populated with `uuid` values:

| timestamp | ticker | uuid |
| --- | --- | --- |
| 2021-11-29T16:20:21.000000Z | BTCUSD | a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11 |
| 2021-12-01T23:53:41.000000Z | BTCUSD | a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11 |

When the `string` value is not a valid UUID, the entire line will be rejected.

### Cast to DECIMAL[​](#cast-to-decimal "Direct link to Cast to DECIMAL")

String values can be cast to the `decimal` type when all the following are true:

* The destination column exists.
* The destination column type is `decimal`.
* The `string` values are valid IEEE-754 decimal values.

```prism-code
CREATE TABLE trade (  
    ticker SYMBOL,  
    price DECIMAL(18, 2),  
    timestamp TIMESTAMP  
) TIMESTAMP(timestamp) PARTITION BY HOUR;
```

Send messages including decimal values as `string`:

```prism-code
trade,ticker="BTCUSD" price="30000.50" 1638202821000000000\n  
trade,ticker="BTCUSD" price="29999.99" 1638402821000000000\n
```

The `price` column is populated with `decimal` values:

| timestamp | ticker | price |
| --- | --- | --- |
| 2021-11-29T16:20:21.000000Z | BTCUSD | 30000.50 |
| 2021-12-01T23:53:41.000000Z | BTCUSD | 29999.99 |

When the `string` value is not a valid IEEE-754 decimal value, the entire line
will be rejected.

## Timestamp[​](#timestamp "Direct link to Timestamp")

These values correspond to QuestDB type `timestamp`. Timestamp values are epoch
`microseconds` suffixed with `t`. In this example we're populating
*non-designated* timestamp field `ts1`:

```prism-code
tracking,obj=VLCC\ STEPHANIE gh="9v1s8hm7wpkssv1h",ts1=10000t 1000000000\n
```

It is possible to populate *designated* timestamp using `columnset`, although
this is not recommended. Let's see how this works in practice. Assuming table:

```prism-code
CREATE TABLE (loc SYMBOL, ts TIMESTAMP) TIMESTAMP(ts) PARTITION BY DAY;
```

When we send:

Sending mixed designated timestamp values

```prism-code
tracking,loc=north ts=2000000000t 1000000000\n  
tracking,loc=south ts=3000000000t\n
```

The `columnset` value always wins:

| loc | ts |
| --- | --- |
| north | 2000000000 |
| south | 3000000000 |