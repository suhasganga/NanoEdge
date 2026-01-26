On this page

This page provides detailed documentation for each window function. For an introduction to window functions and how they work, see the [Overview](/docs/query/functions/window-functions/overview/). For syntax details on the `OVER` clause, see [OVER Clause Syntax](/docs/query/functions/window-functions/syntax/).

## Aggregate window functions[​](#aggregate-window-functions "Direct link to Aggregate window functions")

These functions respect the frame clause and calculate values over the specified window frame.

### avg()[​](#avg "Direct link to avg()")

Calculates the average of values over the window frame. Supports standard arithmetic average, Exponential Moving Average (EMA), and Volume-Weighted Exponential Moving Average (VWEMA).

**Syntax:**

```prism-code
-- Standard average  
avg(value) OVER (window_definition)  
  
-- Exponential Moving Average (EMA)  
avg(value, kind, param) OVER (window_definition)  
  
-- Volume-Weighted Exponential Moving Average (VWEMA)  
avg(value, kind, param, volume) OVER (window_definition)
```

**Arguments:**

* `value`: Numeric column to calculate the average of
* `kind` (EMA/VWEMA): Smoothing mode - `'alpha'`, `'period'`, or a time unit (`'second'`, `'minute'`, `'hour'`, `'day'`, `'week'`)
* `param` (EMA/VWEMA): Parameter for the smoothing mode (see below)
* `volume` (VWEMA only): Numeric column representing volume weights

**Return value:**

* The average of `value` for rows in the window frame

**Description:**

`avg()` operates on the window defined by `PARTITION BY`, `ORDER BY`, and frame specification. It respects the frame clause, calculating a separate average for each row based on its corresponding window.

**Example:**

4-row moving average[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20%20%20symbol%2C%0A%20%20%20%20price%2C%0A%20%20%20%20timestamp%2C%0A%20%20%20%20avg(price)%20OVER%20(%0A%20%20%20%20%20%20%20%20PARTITION%20BY%20symbol%0A%20%20%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20%20%20%20%20ROWS%20BETWEEN%203%20PRECEDING%20AND%20CURRENT%20ROW%0A%20%20%20%20)%20AS%20moving_avg%0AFROM%20trades%0AWHERE%20timestamp%20IN%20today()%3B&executeQuery=true)

```prism-code
SELECT  
    symbol,  
    price,  
    timestamp,  
    avg(price) OVER (  
        PARTITION BY symbol  
        ORDER BY timestamp  
        ROWS BETWEEN 3 PRECEDING AND CURRENT ROW  
    ) AS moving_avg  
FROM trades  
WHERE timestamp IN today();
```

#### Exponential Moving Average (EMA)[​](#exponential-moving-average-ema "Direct link to Exponential Moving Average (EMA)")

The EMA variant applies exponential smoothing, giving more weight to recent values. It supports three smoothing modes:

| Mode | `kind` | `param` | Description |
| --- | --- | --- | --- |
| Direct alpha | `'alpha'` | 0 < α ≤ 1 | Use smoothing factor directly |
| Period-based | `'period'` | N | N-period EMA where α = 2 / (N + 1) |
| Time-weighted | `'second'`, `'minute'`, `'hour'`, `'day'`, `'week'` | τ (tau) | Time-weighted decay where α = 1 - exp(-Δt / τ) |

**EMA formula:**

```prism-code
EMA = α × current_value + (1 - α) × previous_EMA
```

**Examples:**

EMA with direct alpha

```prism-code
SELECT  
    symbol,  
    price,  
    avg(price, 'alpha', 0.2) OVER (  
        PARTITION BY symbol  
        ORDER BY timestamp  
    ) AS ema_alpha  
FROM trades;
```

10-period EMA

```prism-code
SELECT  
    symbol,  
    price,  
    avg(price, 'period', 10) OVER (  
        PARTITION BY symbol  
        ORDER BY timestamp  
    ) AS ema_10  
FROM trades;
```

Time-weighted EMA with 5-minute decay

```prism-code
SELECT  
    symbol,  
    price,  
    avg(price, 'minute', 5) OVER (  
        PARTITION BY symbol  
        ORDER BY timestamp  
    ) AS ema_5min  
FROM trades;
```

EMA behavior

* NULL values are skipped; the previous EMA value is preserved
* The first non-NULL value initializes the EMA
* Works with both `TIMESTAMP` and `TIMESTAMP_NS` precision
* EMA ignores the frame clause and operates cumulatively from the first row

#### Volume-Weighted Exponential Moving Average (VWEMA)[​](#volume-weighted-exponential-moving-average-vwema "Direct link to Volume-Weighted Exponential Moving Average (VWEMA)")

VWEMA combines exponential smoothing with volume weighting, useful for financial analysis where trading volume affects price significance.

**VWEMA formula:**

```prism-code
numerator   = α × price × volume + (1 - α) × prev_numerator  
denominator = α × volume + (1 - α) × prev_denominator  
VWEMA       = numerator / denominator
```

For time-weighted mode: `α = 1 - exp(-Δt / τ)`

**Examples:**

VWEMA with direct alpha

```prism-code
SELECT  
    symbol,  
    price,  
    avg(price, 'alpha', 0.1, volume) OVER (  
        PARTITION BY symbol  
        ORDER BY timestamp  
    ) AS vwema_alpha  
FROM trades;
```

10-period VWEMA

```prism-code
SELECT  
    symbol,  
    price,  
    avg(price, 'period', 10, amount) OVER (  
        PARTITION BY symbol  
        ORDER BY timestamp  
    ) AS vwema_10  
FROM trades;
```

Time-weighted VWEMA with 1-hour decay

```prism-code
SELECT  
    symbol,  
    price,  
    avg(price, 'hour', 1, amount) OVER (  
        PARTITION BY symbol  
        ORDER BY timestamp  
    ) AS vwema_1h  
FROM trades;
```

VWEMA behavior

* Rows with NULL price, NULL volume, or zero volume are skipped
* When timestamps are identical (Δt = 0), the row is skipped in time-weighted mode
* VWEMA ignores the frame clause and operates cumulatively from the first row

---

### count()[​](#count "Direct link to count()")

Counts rows or non-null values over the window frame.

**Syntax:**

```prism-code
count(*) OVER (window_definition)  
count(value) OVER (window_definition)
```

**Arguments:**

* `*`: Counts all rows in the frame
* `value`: Counts non-null values only

**Return value:**

* Number of rows or non-null values in the window frame

**Example:**

Trades in last second[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20%20%20symbol%2C%0A%20%20%20%20count(*)%20OVER%20(%0A%20%20%20%20%20%20%20%20PARTITION%20BY%20symbol%0A%20%20%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20%20%20%20%20RANGE%20BETWEEN%20'1'%20SECOND%20PRECEDING%20AND%20CURRENT%20ROW%0A%20%20%20%20)%20AS%20trades_last_second%0AFROM%20trades%3B&executeQuery=true)

```prism-code
SELECT  
    symbol,  
    count(*) OVER (  
        PARTITION BY symbol  
        ORDER BY timestamp  
        RANGE BETWEEN '1' SECOND PRECEDING AND CURRENT ROW  
    ) AS trades_last_second  
FROM trades;
```

---

### sum()[​](#sum "Direct link to sum()")

Calculates the sum of values over the window frame. Commonly used for running totals.

**Syntax:**

```prism-code
sum(value) OVER (window_definition)
```

**Arguments:**

* `value`: Numeric column (except decimal)

**Return value:**

* The sum of `value` for rows in the window frame

**Example:**

Cumulative amount[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20%20%20symbol%2C%0A%20%20%20%20amount%2C%0A%20%20%20%20timestamp%2C%0A%20%20%20%20sum(amount)%20OVER%20(%0A%20%20%20%20%20%20%20%20PARTITION%20BY%20symbol%0A%20%20%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20%20%20%20%20ROWS%20BETWEEN%20UNBOUNDED%20PRECEDING%20AND%20CURRENT%20ROW%0A%20%20%20%20)%20AS%20cumulative_amount%0AFROM%20trades%0AWHERE%20timestamp%20IN%20today()%3B&executeQuery=true)

```prism-code
SELECT  
    symbol,  
    amount,  
    timestamp,  
    sum(amount) OVER (  
        PARTITION BY symbol  
        ORDER BY timestamp  
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW  
    ) AS cumulative_amount  
FROM trades  
WHERE timestamp IN today();
```

---

### ksum()[​](#ksum "Direct link to ksum()")

Calculates the sum of values over the window frame using the Kahan summation algorithm for improved floating-point precision. This is particularly useful when summing many floating-point values where standard summation might accumulate rounding errors.

**Syntax:**

```prism-code
ksum(value) OVER (window_definition)
```

**Arguments:**

* `value`: Numeric column to sum

**Return value:**

* The sum of `value` for rows in the window frame with improved precision

**Description:**

`ksum()` uses the [Kahan summation algorithm](https://en.wikipedia.org/wiki/Kahan_summation_algorithm) which maintains a running compensation for lost low-order bits. This is useful when summing many floating-point numbers where the standard `sum()` function might accumulate significant rounding errors.

**Example:**

Cumulative sum with Kahan precision[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20%20%20symbol%2C%0A%20%20%20%20price%2C%0A%20%20%20%20timestamp%2C%0A%20%20%20%20ksum(price)%20OVER%20(%0A%20%20%20%20%20%20%20%20PARTITION%20BY%20symbol%0A%20%20%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20%20%20%20%20ROWS%20BETWEEN%20UNBOUNDED%20PRECEDING%20AND%20CURRENT%20ROW%0A%20%20%20%20)%20AS%20cumulative_price%0AFROM%20trades%0AWHERE%20timestamp%20IN%20today()%3B&executeQuery=true)

```prism-code
SELECT  
    symbol,  
    price,  
    timestamp,  
    ksum(price) OVER (  
        PARTITION BY symbol  
        ORDER BY timestamp  
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW  
    ) AS cumulative_price  
FROM trades  
WHERE timestamp IN today();
```

Sliding window sum with precision

```prism-code
SELECT  
    symbol,  
    price,  
    ksum(price) OVER (  
        ORDER BY timestamp  
        ROWS BETWEEN 3 PRECEDING AND CURRENT ROW  
    ) AS rolling_sum  
FROM trades;
```

---

### min()[​](#min "Direct link to min()")

Returns the minimum value within the window frame.

**Syntax:**

```prism-code
min(value) OVER (window_definition)
```

**Arguments:**

* `value`: Numeric column (except decimal)

**Return value:**

* The minimum value (excluding null) in the window frame

**Example:**

Rolling minimum price[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20%20%20symbol%2C%0A%20%20%20%20price%2C%0A%20%20%20%20timestamp%2C%0A%20%20%20%20min(price)%20OVER%20(%0A%20%20%20%20%20%20%20%20PARTITION%20BY%20symbol%0A%20%20%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20%20%20%20%20ROWS%20BETWEEN%203%20PRECEDING%20AND%20CURRENT%20ROW%0A%20%20%20%20)%20AS%20lowest_price%0AFROM%20trades%0AWHERE%20timestamp%20IN%20today()%3B&executeQuery=true)

```prism-code
SELECT  
    symbol,  
    price,  
    timestamp,  
    min(price) OVER (  
        PARTITION BY symbol  
        ORDER BY timestamp  
        ROWS BETWEEN 3 PRECEDING AND CURRENT ROW  
    ) AS lowest_price  
FROM trades  
WHERE timestamp IN today();
```

---

### max()[​](#max "Direct link to max()")

Returns the maximum value within the window frame.

**Syntax:**

```prism-code
max(value) OVER (window_definition)
```

**Arguments:**

* `value`: Numeric column (except decimal)

**Return value:**

* The maximum value (excluding null) in the window frame

**Example:**

Rolling maximum price[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20%20%20symbol%2C%0A%20%20%20%20price%2C%0A%20%20%20%20timestamp%2C%0A%20%20%20%20max(price)%20OVER%20(%0A%20%20%20%20%20%20%20%20PARTITION%20BY%20symbol%0A%20%20%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20%20%20%20%20ROWS%20BETWEEN%203%20PRECEDING%20AND%20CURRENT%20ROW%0A%20%20%20%20)%20AS%20highest_price%0AFROM%20trades%0AWHERE%20timestamp%20IN%20today()%3B&executeQuery=true)

```prism-code
SELECT  
    symbol,  
    price,  
    timestamp,  
    max(price) OVER (  
        PARTITION BY symbol  
        ORDER BY timestamp  
        ROWS BETWEEN 3 PRECEDING AND CURRENT ROW  
    ) AS highest_price  
FROM trades  
WHERE timestamp IN today();
```

---

### first\_value()[​](#first_value "Direct link to first_value()")

Returns the first value in the window frame. Supports `IGNORE NULLS` clause.

**Syntax:**

```prism-code
first_value(value) [(IGNORE|RESPECT) NULLS]  
OVER ([PARTITION BY partition_expression]  
      [ORDER BY sort_expression]  
      [frame_clause])
```

**Arguments:**

* `value`: Column or expression to get value from
* `IGNORE NULLS` (optional): Skip null values
* `RESPECT NULLS` (default): Include null values

**Return value:**

* The first value in the window frame (or first non-null with `IGNORE NULLS`)

**Example:**

First price in partition[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20%20%20symbol%2C%0A%20%20%20%20price%2C%0A%20%20%20%20timestamp%2C%0A%20%20%20%20first_value(price)%20OVER%20(%0A%20%20%20%20%20%20%20%20PARTITION%20BY%20symbol%0A%20%20%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20)%20AS%20first_price%2C%0A%20%20%20%20first_value(price)%20IGNORE%20NULLS%20OVER%20(%0A%20%20%20%20%20%20%20%20PARTITION%20BY%20symbol%0A%20%20%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20)%20AS%20first_non_null_price%0AFROM%20trades%0AWHERE%20timestamp%20IN%20today()%3B&executeQuery=true)

```prism-code
SELECT  
    symbol,  
    price,  
    timestamp,  
    first_value(price) OVER (  
        PARTITION BY symbol  
        ORDER BY timestamp  
    ) AS first_price,  
    first_value(price) IGNORE NULLS OVER (  
        PARTITION BY symbol  
        ORDER BY timestamp  
    ) AS first_non_null_price  
FROM trades  
WHERE timestamp IN today();
```

---

### last\_value()[​](#last_value "Direct link to last_value()")

Returns the last value in the window frame. Supports `IGNORE NULLS` clause.

**Syntax:**

```prism-code
last_value(value) [(IGNORE|RESPECT) NULLS]  
OVER ([PARTITION BY partition_expression]  
      [ORDER BY sort_expression]  
      [frame_clause])
```

**Arguments:**

* `value`: Column or expression to get value from
* `IGNORE NULLS` (optional): Skip null values
* `RESPECT NULLS` (default): Include null values

**Return value:**

* The last value in the window frame (or last non-null with `IGNORE NULLS`)

**Frame behavior:**

* Without `ORDER BY` or frame clause: default is `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`
* With `ORDER BY` but no frame clause: default is `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`

**Example:**

Last value with IGNORE NULLS[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20%20%20timestamp%2C%0A%20%20%20%20price%2C%0A%20%20%20%20last_value(price)%20OVER%20(%0A%20%20%20%20%20%20%20%20PARTITION%20BY%20symbol%0A%20%20%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20%20%20%20%20ROWS%20BETWEEN%202%20PRECEDING%20AND%20CURRENT%20ROW%0A%20%20%20%20)%20AS%20last_price%2C%0A%20%20%20%20last_value(price)%20IGNORE%20NULLS%20OVER%20(%0A%20%20%20%20%20%20%20%20PARTITION%20BY%20symbol%0A%20%20%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20)%20AS%20last_non_null_price%0AFROM%20trades%0AWHERE%20timestamp%20IN%20today()%3B&executeQuery=true)

```prism-code
SELECT  
    timestamp,  
    price,  
    last_value(price) OVER (  
        PARTITION BY symbol  
        ORDER BY timestamp  
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW  
    ) AS last_price,  
    last_value(price) IGNORE NULLS OVER (  
        PARTITION BY symbol  
        ORDER BY timestamp  
    ) AS last_non_null_price  
FROM trades  
WHERE timestamp IN today();
```

This example:

* Gets the last price within a 3-row window for each symbol (`last_price`)
* Gets the last non-null price for each symbol (`last_non_null_price`)
* Demonstrates both `RESPECT NULLS` (default) and `IGNORE NULLS` behavior

---

## Ranking functions[​](#ranking-functions "Direct link to Ranking functions")

These functions assign ranks or row numbers. They ignore the frame clause and operate on the entire partition.

### row\_number()[​](#row_number "Direct link to row_number()")

Assigns a unique sequential number to each row within its partition, starting at 1.

**Syntax:**

```prism-code
row_number() OVER (window_definition)
```

**Arguments:**

* None required

**Return value:**

* Sequential row number (`long` type)

**Description:**

`row_number()` assigns unique numbers even when rows have equal values in the `ORDER BY` column. The assignment among equal values is non-deterministic.

**Example:**

Number trades sequentially[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20%20%20symbol%2C%0A%20%20%20%20price%2C%0A%20%20%20%20timestamp%2C%0A%20%20%20%20row_number()%20OVER%20(%0A%20%20%20%20%20%20%20%20PARTITION%20BY%20symbol%0A%20%20%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20)%20AS%20trade_number%0AFROM%20trades%0AWHERE%20timestamp%20IN%20today()%3B&executeQuery=true)

```prism-code
SELECT  
    symbol,  
    price,  
    timestamp,  
    row_number() OVER (  
        PARTITION BY symbol  
        ORDER BY timestamp  
    ) AS trade_number  
FROM trades  
WHERE timestamp IN today();
```

---

### rank()[​](#rank "Direct link to rank()")

Assigns ranks within a partition. Rows with equal values get the same rank, with gaps in the sequence.

**Syntax:**

```prism-code
rank() OVER (window_definition)
```

**Arguments:**

* None required

**Return value:**

* Rank number (`long` type)

**Description:**

With `rank()`, if two rows tie for rank 2, the next row gets rank 4 (not 3). The rank equals the `row_number` of the first row in its peer group.

**Example:**

Rank by price[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20%20%20symbol%2C%0A%20%20%20%20price%2C%0A%20%20%20%20timestamp%2C%0A%20%20%20%20rank()%20OVER%20(%0A%20%20%20%20%20%20%20%20PARTITION%20BY%20symbol%0A%20%20%20%20%20%20%20%20ORDER%20BY%20price%20DESC%0A%20%20%20%20)%20AS%20price_rank%0AFROM%20trades%0AWHERE%20timestamp%20IN%20today()%3B&executeQuery=true)

```prism-code
SELECT  
    symbol,  
    price,  
    timestamp,  
    rank() OVER (  
        PARTITION BY symbol  
        ORDER BY price DESC  
    ) AS price_rank  
FROM trades  
WHERE timestamp IN today();
```

---

### dense\_rank()[​](#dense_rank "Direct link to dense_rank()")

Assigns ranks within a partition. Rows with equal values get the same rank, with no gaps in the sequence.

**Syntax:**

```prism-code
dense_rank() OVER (window_definition)
```

**Arguments:**

* None required

**Return value:**

* Rank number (`long` type)

**Description:**

Unlike `rank()`, `dense_rank()` produces consecutive rank numbers. If two rows tie for rank 2, the next row gets rank 3.

**Example:**

Dense rank by price[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20%20%20symbol%2C%0A%20%20%20%20price%2C%0A%20%20%20%20timestamp%2C%0A%20%20%20%20dense_rank()%20OVER%20(%0A%20%20%20%20%20%20%20%20PARTITION%20BY%20symbol%0A%20%20%20%20%20%20%20%20ORDER%20BY%20price%20DESC%0A%20%20%20%20)%20AS%20price_rank%0AFROM%20trades%0AWHERE%20timestamp%20IN%20today()%3B&executeQuery=true)

```prism-code
SELECT  
    symbol,  
    price,  
    timestamp,  
    dense_rank() OVER (  
        PARTITION BY symbol  
        ORDER BY price DESC  
    ) AS price_rank  
FROM trades  
WHERE timestamp IN today();
```

---

## Offset functions[​](#offset-functions "Direct link to Offset functions")

These functions access values from other rows relative to the current row. They ignore frame clauses.

### lag()[​](#lag "Direct link to lag()")

Accesses data from a previous row without a self-join.

**Syntax:**

```prism-code
lag(value [, offset [, default]]) [(IGNORE|RESPECT) NULLS]  
OVER ([PARTITION BY partition_expression] [ORDER BY sort_expression])
```

**Arguments:**

* `value`: Column or expression to retrieve
* `offset` (optional): Number of rows back. Default is 1
* `default` (optional): Value when offset exceeds partition bounds. Default is `NULL`
* `IGNORE NULLS` (optional): Skip null values when counting offset
* `RESPECT NULLS` (default): Include null values in offset counting

**Return value:**

* Value from the specified previous row

**Behavior:**

* When `offset` is 0, returns current row value
* Frame clauses (`ROWS`/`RANGE`) are ignored
* Without `ORDER BY`, uses table scan order

**Example:**

Previous price and price change[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20%20%20timestamp%2C%0A%20%20%20%20price%2C%0A%20%20%20%20lag(price)%20OVER%20(%0A%20%20%20%20%20%20%20%20PARTITION%20BY%20symbol%0A%20%20%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20)%20AS%20previous_price%2C%0A%20%20%20%20lag(price%2C%202%2C%200.0)%20OVER%20(%0A%20%20%20%20%20%20%20%20PARTITION%20BY%20symbol%0A%20%20%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20)%20AS%20price_two_rows_back%0AFROM%20trades%0AWHERE%20timestamp%20IN%20today()%3B&executeQuery=true)

```prism-code
SELECT  
    timestamp,  
    price,  
    lag(price) OVER (  
        PARTITION BY symbol  
        ORDER BY timestamp  
    ) AS previous_price,  
    lag(price, 2, 0.0) OVER (  
        PARTITION BY symbol  
        ORDER BY timestamp  
    ) AS price_two_rows_back  
FROM trades  
WHERE timestamp IN today();
```

This example:

* Gets the previous price for each symbol (`previous_price`)
* Gets the price from 2 rows back (`price_two_rows_back`)
* Uses 0.0 as default when looking 2 rows back reaches the partition start

---

### lead()[​](#lead "Direct link to lead()")

Accesses data from a subsequent row without a self-join.

**Syntax:**

```prism-code
lead(value [, offset [, default]]) [(IGNORE|RESPECT) NULLS]  
OVER ([PARTITION BY partition_expression] [ORDER BY sort_expression])
```

**Arguments:**

* `value`: Column or expression to retrieve
* `offset` (optional): Number of rows forward. Default is 1
* `default` (optional): Value when offset exceeds partition bounds. Default is `NULL`
* `IGNORE NULLS` (optional): Skip null values when counting offset
* `RESPECT NULLS` (default): Include null values in offset counting

**Return value:**

* Value from the specified following row

**Behavior:**

* When `offset` is 0, returns current row value
* Frame clauses (`ROWS`/`RANGE`) are ignored
* Without `ORDER BY`, uses table scan order

**Example:**

Next price[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20%20%20timestamp%2C%0A%20%20%20%20price%2C%0A%20%20%20%20lead(price)%20OVER%20(%0A%20%20%20%20%20%20%20%20PARTITION%20BY%20symbol%0A%20%20%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20)%20AS%20next_price%2C%0A%20%20%20%20lead(price%2C%202%2C%200.0)%20OVER%20(%0A%20%20%20%20%20%20%20%20PARTITION%20BY%20symbol%0A%20%20%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20)%20AS%20price_after_next%0AFROM%20trades%0AWHERE%20timestamp%20IN%20today()%3B&executeQuery=true)

```prism-code
SELECT  
    timestamp,  
    price,  
    lead(price) OVER (  
        PARTITION BY symbol  
        ORDER BY timestamp  
    ) AS next_price,  
    lead(price, 2, 0.0) OVER (  
        PARTITION BY symbol  
        ORDER BY timestamp  
    ) AS price_after_next  
FROM trades  
WHERE timestamp IN today();
```

This example:

* Gets the next price for each symbol (`next_price`)
* Gets the price from 2 rows ahead (`price_after_next`)
* Uses 0.0 as default when looking 2 rows ahead reaches the partition end

---

## Examples[​](#examples "Direct link to Examples")

### Moving average of best bid price[​](#moving-average-of-best-bid-price "Direct link to Moving average of best bid price")

4-row moving average of best bid[Demo this query](https://demo.questdb.io/?query=DECLARE%20%40best_bid%20%3A%3D%20bids%5B1%2C1%5D%0ASELECT%0A%20%20%20%20timestamp%2C%0A%20%20%20%20symbol%2C%0A%20%20%20%20%40best_bid%20AS%20best_bid%2C%0A%20%20%20%20avg(%40best_bid)%20OVER%20(%0A%20%20%20%20%20%20%20%20PARTITION%20BY%20symbol%0A%20%20%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20%20%20%20%20ROWS%20BETWEEN%203%20PRECEDING%20AND%20CURRENT%20ROW%0A%20%20%20%20)%20AS%20bid_moving_avg%0AFROM%20market_data%0AWHERE%20timestamp%20IN%20today()%3B&executeQuery=true)

```prism-code
DECLARE @best_bid := bids[1,1]  
SELECT  
    timestamp,  
    symbol,  
    @best_bid AS best_bid,  
    avg(@best_bid) OVER (  
        PARTITION BY symbol  
        ORDER BY timestamp  
        ROWS BETWEEN 3 PRECEDING AND CURRENT ROW  
    ) AS bid_moving_avg  
FROM market_data  
WHERE timestamp IN today();
```

### Cumulative bid size[​](#cumulative-bid-size "Direct link to Cumulative bid size")

Rolling 5-row volume[Demo this query](https://demo.questdb.io/?query=DECLARE%0A%20%20%40best_bid%20%3A%3D%20bids%5B1%2C1%5D%2C%0A%20%20%40volume_l1%20%3A%3D%20bids%5B2%2C1%5D%0ASELECT%0A%20%20%20%20timestamp%2C%20symbol%2C%0A%20%20%20%20%40best_bid%20AS%20bid_price_l1%2C%0A%20%20%20%20%40volume_l1%20AS%20bid_volume_l1%2C%0A%20%20%20%20sum(%40volume_l1)%20OVER%20(%0A%20%20%20%20%20%20%20%20PARTITION%20BY%20symbol%20ORDER%20BY%20timestamp%0A%20%20%20%20%20%20%20%20ROWS%20BETWEEN%205%20PRECEDING%20AND%20CURRENT%20ROW%0A%20%20%20%20)%20AS%20bid_volume_l1_5rows%0AFROM%20market_data%0AWHERE%20timestamp%20IN%20today()%3B&executeQuery=true)

```prism-code
DECLARE  
  @best_bid := bids[1,1],  
  @volume_l1 := bids[2,1]  
SELECT  
    timestamp, symbol,  
    @best_bid AS bid_price_l1,  
    @volume_l1 AS bid_volume_l1,  
    sum(@volume_l1) OVER (  
        PARTITION BY symbol ORDER BY timestamp  
        ROWS BETWEEN 5 PRECEDING AND CURRENT ROW  
    ) AS bid_volume_l1_5rows  
FROM market_data  
WHERE timestamp IN today();
```

### Time-based rolling sum[​](#time-based-rolling-sum "Direct link to Time-based rolling sum")

1-minute rolling bid volume[Demo this query](https://demo.questdb.io/?query=DECLARE%0A%20%20%20%20%40best_bid%20%3A%3D%20bids%5B1%2C1%5D%2C%0A%20%20%20%20%40volume_l1%20%3A%3D%20bids%5B2%2C1%5D%0ASELECT%0A%20%20%20%20timestamp%2C%0A%20%20%20%20sum(%40volume_l1)%20OVER%20(%0A%20%20%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20%20%20%20%20RANGE%20BETWEEN%20'1'%20MINUTE%20PRECEDING%20AND%20CURRENT%20ROW%0A%20%20%20%20)%20AS%20bid_volume_1min%0AFROM%20market_data%0AWHERE%20timestamp%20IN%20today()%20AND%20symbol%20%3D%20'GBPUSD'%3B&executeQuery=true)

```prism-code
DECLARE  
    @best_bid := bids[1,1],  
    @volume_l1 := bids[2,1]  
SELECT  
    timestamp,  
    sum(@volume_l1) OVER (  
        ORDER BY timestamp  
        RANGE BETWEEN '1' MINUTE PRECEDING AND CURRENT ROW  
    ) AS bid_volume_1min  
FROM market_data  
WHERE timestamp IN today() AND symbol = 'GBPUSD';
```

### Trade frequency analysis[​](#trade-frequency-analysis "Direct link to Trade frequency analysis")

Trades per minute by side[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20%20%20timestamp%2C%0A%20%20%20%20symbol%2C%0A%20%20%20%20COUNT(*)%20OVER%20(%0A%20%20%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20%20%20%20%20RANGE%20BETWEEN%2060000000%20PRECEDING%20AND%20CURRENT%20ROW%0A%20%20%20%20)%20AS%20updates_per_min%2C%0A%20%20%20%20COUNT(CASE%20WHEN%20side%20%3D%20'buy'%20THEN%201%20END)%20OVER%20(%0A%20%20%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20%20%20%20%20RANGE%20BETWEEN%2060000000%20PRECEDING%20AND%20CURRENT%20ROW%0A%20%20%20%20)%20AS%20buys_per_minute%2C%0A%20%20%20%20COUNT(CASE%20WHEN%20side%20%3D%20'sell'%20THEN%201%20END)%20OVER%20(%0A%20%20%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20%20%20%20%20RANGE%20BETWEEN%2060000000%20PRECEDING%20AND%20CURRENT%20ROW%0A%20%20%20%20)%20AS%20sells_per_minute%0AFROM%20trades%0AWHERE%20timestamp%20IN%20today()%20AND%20symbol%20%3D%20'BTC-USD'%3B&executeQuery=true)

```prism-code
SELECT  
    timestamp,  
    symbol,  
    COUNT(*) OVER (  
        ORDER BY timestamp  
        RANGE BETWEEN 60000000 PRECEDING AND CURRENT ROW  
    ) AS updates_per_min,  
    COUNT(CASE WHEN side = 'buy' THEN 1 END) OVER (  
        ORDER BY timestamp  
        RANGE BETWEEN 60000000 PRECEDING AND CURRENT ROW  
    ) AS buys_per_minute,  
    COUNT(CASE WHEN side = 'sell' THEN 1 END) OVER (  
        ORDER BY timestamp  
        RANGE BETWEEN 60000000 PRECEDING AND CURRENT ROW  
    ) AS sells_per_minute  
FROM trades  
WHERE timestamp IN today() AND symbol = 'BTC-USD';
```

---

## Notes[​](#notes "Direct link to Notes")

* The order of rows in the result set is not guaranteed to be consistent across query executions. Use an `ORDER BY` clause outside the `OVER` clause to ensure consistent ordering.
* Ranking functions (`row_number`, `rank`, `dense_rank`) and offset functions (`lag`, `lead`) ignore frame specifications.
* For time-based calculations, consider using `RANGE` frames with timestamp columns.