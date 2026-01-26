On this page

This page describes the available functions to assist with performing time-based
calculations using timestamps.

## Timestamp format[​](#timestamp-format "Direct link to Timestamp format")

The timestamp format is formed by units and arbitrary text. A unit is a
combination of letters representing a date or time component, as defined by the
table below. The letters used to form a unit are case-sensitive.

See
[Timestamps in QuestDB](/docs/concepts/timestamps-timezones/#timestamps-in-questdb)
for more examples of how the units are used to parse inputs.

| Unit | Date or Time Component | Presentation | Examples |
| --- | --- | --- | --- |
| `G` | Era designator | Text | AD |
| `y` | `y` single digit or greedy year, depending on the number of digits in input | Year | 1996; 96; 999; 3 |
| `yy` | Two digit year of the current century | Year | 96 (interpreted as 2096) |
| `yyy` | Three-digit year | Year | 999 |
| `yyyy` | Four-digit year | Year | 1996 |
| `M` | Month in year, numeric, greedy | Month | 7; 07; 007; etc. |
| `MM` | Month in year, two-digit | Month | 07 |
| `MMM` | Month in year, name | Month | Jul; July |
| `w` | Week in year | Number | 2 |
| `ww` | ISO week of year (two-digit) | Number | 02 |
| `D` | Day in year | Number | 189 |
| `d` | Day in month | Number | 10 |
| `F` | Day of week in month | Number | 2 |
| `E` | Day name in week | Text | Tuesday; Tue |
| `u` | Day number of week (1 = Monday, ..., 7 = Sunday) | Number | 1 |
| `a` | Am/pm marker | Text | PM |
| `H` | Hour in day (0-23) | Number | 0 |
| `k` | Hour in day (1-24) | Number | 24 |
| `K` | Hour in am/pm (0-11) | Number | 0 |
| `h` | Hour in am/pm (1-12) | Number | 12 |
| `m` | Minute in hour | Number | 30 |
| `s` | Second in minute | Number | 55 |
| `SSS` | 3-digit millisecond (see explanation below for fraction-of-second) | Number | 978 |
| `S` | Millisecond up to 3 digits (see explanation below for fraction-of-second) | Number | 900 |
| `UUU` | 3-digit microsecond (see explanation below for fraction-of-second) | Number | 456 |
| `U` | Microsecond up to 3 digits (see explanation below for fraction-of-second) | Number | 456 |
| `U+` | Microsecond up to 6 digits (see explanation below for fraction-of-second) | Number | 123456 |
| `N` | Nanosecond up to 3 digits (see explanation below for fraction-of-second) | Number | 900 |
| `N+` | Microsecond up to 9 digits (see explanation below for fraction-of-second) | Number | 123456789 |
| `z` | Time zone | General time zone | Pacific Standard Time; PST; GMT-08:00 |
| `Z` | Time zone | RFC 822 time zone | -0800 |
| `x` | Time zone | ISO 8601 time zone | -08; -0800; -08:00 |

### Examples for greedy year format `y`[​](#examples-for-greedy-year-format-y "Direct link to examples-for-greedy-year-format-y")

The interpretation of `y` depends on the number of digits in the input text:

* If the input year is a two-digit number, the output timestamp assumes the
  current century.
* Otherwise, the number is interpreted as it is.

| Input year | Timestamp value interpreted by `y-M` | Notes |
| --- | --- | --- |
| `5-03` | `0005-03-01T00:00:00.000000Z` | Greedily parsing the number as it is |
| `05-03` | `2005-03-01T00:00:00.000000Z` | Greedily parsing the number assuming current century |
| `005-03` | `0005-03-01T00:00:00.000000Z` | Greedily parsing the number as it is |
| `0005-03` | `0005-03-01T00:00:00.000000Z` | Greedily parsing the number as it is |

### Examples for fractions of a second[​](#examples-for-fractions-of-a-second "Direct link to Examples for fractions of a second")

In a basic example, `y-M-dTHH:mm:ss.S` specifies to parse 1, 2, or 3 decimals.
Here are more examples, showing just the last part starting with the `.`:

| format | number of decimals | example input | parsed fraction of second |
| --- | --- | --- | --- |
| `.S` | 1-3 | `.12` | 12 milliseconds |
| `.SSS` | 3 | `.123` | 123 milliseconds |
| `.SSSU` | 4-6 | `.1234` | 123,400 microseconds |
| `.SSSUUU` | 6 | `.123456` | 123,456 microseconds |
| `.U+` | 1-6 | `.12345` | 123,450 microseconds |
| `.SSSUUUN` | 7-9 | `.1234567` | 123,456,700 nanoseconds |
| `.SSSUUUNNN` | 9 | `.123456789` | 123,456,789 nanoseconds |
| `.N+` | 1-9 | `.12` | 120,000,000 nanoseconds |

## Timestamp to Date conversion[​](#timestamp-to-date-conversion "Direct link to Timestamp to Date conversion")

As described at the [data types section](/docs/query/datatypes/overview/), the
only difference between `TIMESTAMP`, `TIMESTAMP_NS`, and `DATE` in QuestDB type
system is the resolution. Whilst `TIMESTAMP` stores resolution as an offset from Unix epoch in
microseconds, `TIMESTAMP_NS` stores it as an offset in nanoseconds, and `DATE` stores the
offset in milliseconds.

Since the three types are backed by a signed long, this means the `DATE` type has a
wider range. A `DATE` column can store about ±2.9 million years from the Unix
epoch, whereas a `TIMESTAMP` has an approximate range of ±290,000 years, and a
`TIMESTAMP_NS` has an approximate range of ±2262 years.

For most purposes a `TIMESTAMP` is preferred, as it offers a wider range of
functions whilst still being 8 bytes in size.

Be aware that, when using a `TIMESTAMP` or `TIMESTAMP_NS` as the designated
timestamp, you cannot set it to any value before the Unix epoch (`1970-01-01T00:00:00.000000Z`).

To explicitly convert from `TIMESTAMP` to `DATE` or `TIMESTAMP_NS`, you can use
`CAST(ts_column AS DATE)` or `CAST(ts_column AS TIMESTAMP_NS)`. To convert from
`DATE` or `TIMESTAMP_NS` to `TIMESTAMP` you can `CAST(column AS TIMESTAMP_NS)`.

### Programmatically convert from language-specific datetimes into QuestDB timestamps[​](#programmatically-convert-from-language-specific-datetimes-into-questdb-timestamps "Direct link to Programmatically convert from language-specific datetimes into QuestDB timestamps")

Different programming languages use different types of objects to represent the
`DATE` type. To learn how to convert from the `DATE` type into a `TIMESTAMP`
object in Python, Go, Java, JavaScript, C/C++, Rust, or C#/.NET, please visit
our [Date to Timestamp conversion](/docs/ingestion/clients/date-to-timestamp-conversion/)
reference.

---

## date\_trunc[​](#date_trunc "Direct link to date_trunc")

`date_trunc(unit, timestamp)` - returns a timestamp truncated to the specified
precision.

**Arguments:**

* `unit` is one of the following:

  + `millennium`
  + `decade`
  + `century`
  + `year`
  + `quarter`
  + `month`
  + `week`
  + `day`
  + `hour`
  + `minute`
  + `second`
  + `millisecond`
  + `microsecond`
  + `nanosecond`
* `timestamp` is any `timestamp`, `timestamp_ns`, or ISO-8601 string value.

**Return value:**

Return value defaults to `timestamp`, but it will return a `timestamp_ns` if the timestamp argument is
of type `timestamp_ns` or if the date passed as a string contains nanoseconds resolution.

**Examples:**

```prism-code
SELECT date_trunc('hour', '2022-03-11T22:00:30.555555Z') hour,  
date_trunc('month', '2022-03-11T22:00:30.555555Z') month,  
date_trunc('year','2022-03-11T22:00:30.555555Z') year;  
date_trunc('year','2022-03-11T22:00:30.555555000Z') year;
```

| hour (timestamp\_ns) | month (timestamp\_ns) | year (timestamp\_ns) | year (timestamp\_ns) |
| --- | --- | --- | --- |
| 2022-03-11T22:00:00.000000Z | 2022-03-01T00:00:00.000000Z | 2022-01-01T00:00:00.000000Z | 2022-01-01T00:00:00.000000000Z |

## dateadd[​](#dateadd "Direct link to dateadd")

`dateadd(period, n, startDate[, timezone])` - adds `n` `period` to `startDate`,
optionally respecting timezone DST transitions.

tip

When a timezone is specified, the function handles daylight savings time
transitions correctly. This is particularly important when adding periods that
could cross DST boundaries (like weeks, months, or years).

Without the timezone parameter, the function performs simple UTC arithmetic
which may lead to incorrect results when crossing DST boundaries. For
timezone-aware calculations, use the timezone parameter.

**Arguments:**

* `period` is a `char`. Period to be added. Available periods are:

  + `n`: nanoseconds
  + `u`: microseconds
  + `T`: milliseconds
  + `s`: second
  + `m`: minute
  + `h`: hour
  + `d`: day
  + `w`: week
  + `M`: month
  + `y`: year
* `n` is an `int` indicating the number of periods to add.
* `startDate` is a timestamp, timestamp\_ns, or date indicating the timestamp to add the period
  to.
* `timezone` (optional) is a string specifying the timezone to use for DST-aware
  calculations - for example, 'Europe/London'.

**Return value:**

Return value type defaults to `timestamp`, but it will return a `timestamp_ns` if the `startDate`
argument is a `timetamp_ns`.

**Examples:**

Adding hours

```prism-code
SELECT systimestamp(), dateadd('h', 2, systimestamp())  
FROM long_sequence(1);
```

| systimestamp | dateadd |
| --- | --- |
| 2020-04-17T00:30:51.380499Z | 2020-04-17T02:30:51.380499Z |

Adding days

```prism-code
SELECT systimestamp(), dateadd('d', 2, systimestamp())  
FROM long_sequence(1);
```

| systimestamp | dateadd |
| --- | --- |
| 2020-04-17T00:30:51.380499Z | 2020-04-19T00:30:51.380499Z |

Adding weeks with timezone

```prism-code
SELECT  
    '2024-10-21T10:00:00Z',  
    dateadd('w', 1, '2024-10-21T10:00:00Z', 'Europe/Bratislava') as with_tz,  
    dateadd('w', 1, '2024-10-21T10:00:00Z') as without_tz  
FROM long_sequence(1);
```

| timestamp | with\_tz | without\_tz |
| --- | --- | --- |
| 2024-10-21T10:00:00.000Z | 2024-10-28T10:00:00.000Z | 2024-10-28T09:00:00.000Z |

Note how the timezone-aware calculation correctly handles the DST transition in
`Europe/Bratislava`.

Adding months

```prism-code
SELECT systimestamp(), dateadd('M', 2, systimestamp())  
FROM long_sequence(1);
```

| systimestamp | dateadd |
| --- | --- |
| 2020-04-17T00:30:51.380499Z | 2020-06-17T00:30:51.380499Z |

## datediff[​](#datediff "Direct link to datediff")

`datediff(period, date1, date2)` - returns the absolute number of `period`
between `date1` and `date2`.

**Arguments:**

* `period` is a char. Period to be added. Available periods are:

  + `n`: nanoseconds
  + `u`: microseconds
  + `T`: milliseconds
  + `s`: second
  + `m`: minute
  + `h`: hour
  + `d`: day
  + `w`: week
  + `M`: month
  + `y`: year
* `date1` and `date2` are `timestamp`, `timestamp_ns`, `date`, or date literal strings defining the dates to compare.

**Return value:**

Return value type is `long`

**Examples:**

Difference in days

```prism-code
SELECT datediff('d', '2020-01-23', '2020-01-27');
```

| datediff |
| --- |
| 4 |

Difference in months

```prism-code
SELECT datediff('M', '2020-01-23', '2020-02-27');
```

| datediff |
| --- |
| 1 |

## day[​](#day "Direct link to day")

`day(value)` - returns the `day` of month for a given timestamp from `1` to
`31`.

**Arguments:**

* `value` is any `timestamp`, `timestamp_ns`, or `date`

**Return value:**

Return value type is `int`

**Examples:**

Day of the month[Demo this query](https://demo.questdb.io/?query=SELECT%20day(to_timestamp('2020-03-01%3A15%3A43%3A21'%2C%20'yyyy-MM-dd%3AHH%3Amm%3Ass'))%0AFROM%20trades%0ALIMIT%20-1%3B&executeQuery=true)

```prism-code
SELECT day(to_timestamp('2020-03-01:15:43:21', 'yyyy-MM-dd:HH:mm:ss'))  
FROM trades  
LIMIT -1;
```

| day |
| --- |
| 01 |

Using in an aggregation

```prism-code
SELECT day(ts), count() FROM transactions;
```

| day | count |
| --- | --- |
| 1 | 2323 |
| 2 | 6548 |
| ... | ... |
| 30 | 9876 |
| 31 | 2567 |

## day\_of\_week[​](#day_of_week "Direct link to day_of_week")

`day_of_week(value)` - returns the day number in a week from `1` (Monday) to `7`
(Sunday).

**Arguments:**

* `value` is any `timestamp`, `timestamp_ns`, or `date`

**Return value:**

Return value type is `int`

**Examples:**

```prism-code
SELECT to_str(ts,'EE'),day_of_week(ts) FROM myTable;
```

| day | day\_of\_week |
| --- | --- |
| Monday | 1 |
| Tuesday | 2 |
| Wednesday | 3 |
| Thursday | 4 |
| Friday | 5 |
| Saturday | 6 |
| Sunday | 7 |

## day\_of\_week\_sunday\_first[​](#day_of_week_sunday_first "Direct link to day_of_week_sunday_first")

`day_of_week_sunday_first(value)` - returns the day number in a week from `1`
(Sunday) to `7` (Saturday).

**Arguments:**

* `value` is any `timestamp`, `timestamp_ns`, or `date`

**Return value:**

Return value type is `int`

**Examples:**

```prism-code
SELECT to_str(ts,'EE'),day_of_week_sunday_first(ts) FROM myTable;
```

| day | day\_of\_week\_sunday\_first |
| --- | --- |
| Monday | 2 |
| Tuesday | 3 |
| Wednesday | 4 |
| Thursday | 5 |
| Friday | 6 |
| Saturday | 7 |
| Sunday | 1 |

## days\_in\_month[​](#days_in_month "Direct link to days_in_month")

`days_in_month(value)` - returns the number of days in a month from a given
timestamp or date.

**Arguments:**

* `value` is any `timestamp`, `timestamp_ns`, or `date`

**Return value:**

Return value type is `int`

**Examples:**

```prism-code
SELECT month(ts), days_in_month(ts) FROM myTable;
```

| month | days\_in\_month |
| --- | --- |
| 4 | 30 |
| 5 | 31 |
| 6 | 30 |
| 7 | 31 |
| 8 | 31 |

## extract[​](#extract "Direct link to extract")

`extract(unit, timestamp)` - returns the selected time unit from the input
timestamp.

**Arguments:**

* `unit` is one of the following:

  + `millennium`
  + `epoch`
  + `decade`
  + `century`
  + `year`
  + `isoyear`
  + `doy` (day of year)
  + `quarter`
  + `month`
  + `week`
  + `dow` (day of week)
  + `isodow`
  + `day`
  + `hour`
  + `minute`
  + `second`
  + `microseconds`
  + `milliseconds`
* `timestamp` is any `timestamp`, `timestamp_ns`, `date`, or date literal string value.

**Return value:**

Return value type is `integer`.

**Examples**

```prism-code
SELECT extract(millennium from '2023-03-11T22:00:30.555555Z') millennium,  
extract(year from '2023-03-11T22:00:30.555555Z') year,  
extract(month from '2023-03-11T22:00:30.555555Z') month,  
extract(week from '2023-03-11T22:00:30.555555Z') quarter,  
extract(hour from '2023-03-11T22:00:30.555555Z') hour,  
extract(second from '2023-03-11T22:00:30.555555Z') second;
```

| millennium | year | month | quarter | hour | second |
| --- | --- | --- | --- | --- | --- |
| 3 | 2023 | 3 | 10 | 22 | 30 |

## hour[​](#hour "Direct link to hour")

`hour(value)` - returns the `hour` of day for a given timestamp from `0` to
`23`.

**Arguments:**

* `timestamp` is any `timestamp`, `timestamp_ns`, `date`, or date literal string value.

**Return value:**

Return value type is `int`

**Examples:**

Hour of the day

```prism-code
SELECT hour(to_timestamp('2020-03-01:15:43:21', 'yyyy-MM-dd:HH:mm:ss'))  
FROM long_sequence(1);
```

| hour |
| --- |
| 12 |

Using in an aggregation

```prism-code
SELECT hour(ts), count() FROM transactions;
```

| hour | count |
| --- | --- |
| 0 | 2323 |
| 1 | 6548 |
| ... | ... |
| 22 | 9876 |
| 23 | 2567 |

## interval[​](#interval "Direct link to interval")

`interval(start_timestamp, end_timestamp)` - creates a time interval from two
timestamps.

**Arguments:**

* `start_timestamp` is a timestamp.
* `end_timestamp` is a timestamp not earlier than the `start_timestamp`.

**Return value:**

Return value type is `interval`.

**Examples:**

Construct an interval[Demo this query](https://demo.questdb.io/?query=SELECT%20interval('2024-10-08T11%3A09%3A47.573Z'%2C%20'2024-10-09T11%3A09%3A47.573Z')&executeQuery=true)

```prism-code
SELECT interval('2024-10-08T11:09:47.573Z', '2024-10-09T11:09:47.573Z')
```

| interval |
| --- |
| ('2024-10-08T11:09:47.573Z', '2024-10-09T11:09:47.573Z') |

## interval\_start[​](#interval_start "Direct link to interval_start")

`interval_start(interval)` - extracts the lower bound of the interval.

**Arguments:**

* `interval` is an `interval`.

**Return value:**

Return value type is `timestamp` or `timestamp_ns`, depending on the type of values in the interval.

**Examples:**

Extract an interval lower bound[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20interval_start(%0A%20%20%20%20interval('2024-10-08T11%3A09%3A47.573Z'%2C%20'2024-10-09T11%3A09%3A47.573Z')%0A%20%20)&executeQuery=true)

```prism-code
SELECT  
  interval_start(  
    interval('2024-10-08T11:09:47.573Z', '2024-10-09T11:09:47.573Z')  
  )
```

| interval\_start |
| --- |
| 2024-10-08T11:09:47.573000Z |

## interval\_end[​](#interval_end "Direct link to interval_end")

`interval_end(interval)` - extracts the upper bound of the interval.

**Arguments:**

* `interval` is an `interval`.

**Return value:**

Return value type is `timestamp` or `timestamp_ns`, depending on the type of values in the interval.

**Examples:**

Extract an interval upper bound[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20interval_end(%0A%20%20%20%20interval('2024-10-08T11%3A09%3A47.573Z'%2C%20'2024-10-09T11%3A09%3A47.573Z')%0A%20%20)&executeQuery=true)

```prism-code
SELECT  
  interval_end(  
    interval('2024-10-08T11:09:47.573Z', '2024-10-09T11:09:47.573Z')  
  )
```

| interval\_end |
| --- |
| 2024-10-09T11:09:47.573000Z |

## is\_leap\_year[​](#is_leap_year "Direct link to is_leap_year")

`is_leap_year(value)` - returns `true` if the `year` of `value` is a leap year,
`false` otherwise.

**Arguments:**

* `value` is any `timestamp`, `timestamp_ns`, or `date`

**Return value:**

Return value type is `boolean`

**Examples:**

Simple example[Demo this query](https://demo.questdb.io/?query=SELECT%20year(timestamp)%2C%20is_leap_year(timestamp)%0AFROM%20trades%0Alimit%20-1%3B&executeQuery=true)

```prism-code
SELECT year(timestamp), is_leap_year(timestamp)  
FROM trades  
limit -1;
```

| year | is\_leap\_year |
| --- | --- |
| 2020 | true |
| 2021 | false |
| 2022 | false |
| 2023 | false |
| 2024 | true |
| 2025 | false |

## micros[​](#micros "Direct link to micros")

`micros(value)` - returns the `micros` of the millisecond for a given date or
timestamp from `0` to `999`.

**Arguments:**

* `value` is any `timestamp`, `timestamp_ns`, or `date`

**Return value:**

Return value type is `int`

**Examples:**

Micros of the second

```prism-code
SELECT micros(to_timestamp('2020-03-01:15:43:21.123456', 'yyyy-MM-dd:HH:mm:ss.SSSUUU'))  
FROM long_sequence(1);
```

| millis |
| --- |
| 456 |

Parsing 3 digits when no unit is added after U

```prism-code
SELECT micros(to_timestamp('2020-03-01:15:43:21.123456', 'yyyy-MM-dd:HH:mm:ss.SSSU'))  
FROM long_sequence(1);
```

| millis |
| --- |
| 456 |

Using in an aggregation

```prism-code
SELECT micros(ts), count() FROM transactions;
```

| second | count |
| --- | --- |
| 0 | 2323 |
| 1 | 6548 |
| ... | ... |
| 998 | 9876 |
| 999 | 2567 |

## millis[​](#millis "Direct link to millis")

`millis(value)` - returns the `millis` of the second for a given date or
timestamp from `0` to `999`.

**Arguments:**

* `value` is any `timestamp`, `timestamp_ns`, or `date`

**Return value:**

Return value type is `int`

**Examples:**

Millis of the second

```prism-code
SELECT millis(  
    to_timestamp('2020-03-01:15:43:21.123456', 'yyyy-MM-dd:HH:mm:ss.SSSUUU'))  
FROM long_sequence(1);
```

| millis |
| --- |
| 123 |

Parsing 3 digits when no unit is added after S

```prism-code
SELECT millis(to_timestamp('2020-03-01:15:43:21.123', 'yyyy-MM-dd:HH:mm:ss.S'))  
FROM long_sequence(1);
```

| millis |
| --- |
| 123 |

Using in an aggregation

```prism-code
SELECT millis(ts), count() FROM transactions;
```

| second | count |
| --- | --- |
| 0 | 2323 |
| 1 | 6548 |
| ... | ... |
| 998 | 9876 |
| 999 | 2567 |

## minute[​](#minute "Direct link to minute")

`minute(value)` - returns the `minute` of the hour for a given timestamp from
`0` to `59`.

**Arguments:**

* `value` is any `timestamp`, `timestamp_ns`, or `date`

**Return value:**

Return value type is `int`

**Examples:**

Minute of the hour[Demo this query](https://demo.questdb.io/?query=SELECT%20minute(to_timestamp('2022-03-01%3A15%3A43%3A21'%2C%20'yyyy-MM-dd%3AHH%3Amm%3Ass'))%0AFROM%20trades%0ALIMIT%20-1%3B&executeQuery=true)

```prism-code
SELECT minute(to_timestamp('2022-03-01:15:43:21', 'yyyy-MM-dd:HH:mm:ss'))  
FROM trades  
LIMIT -1;
```

| minute |
| --- |
| 43 |

Using in an aggregation

```prism-code
SELECT minute(ts), count() FROM transactions;
```

| minute | count |
| --- | --- |
| 0 | 2323 |
| 1 | 6548 |
| ... | ... |
| 58 | 9876 |
| 59 | 2567 |

## month[​](#month "Direct link to month")

`month(value)` - returns the `month` of year for a given date from `1` to `12`.

**Arguments:**

* `value` is any `timestamp`, `timestamp_ns`, or `date`

**Return value:**

Return value type is `int`

**Examples:**

Month of the year

```prism-code
SELECT month(to_timestamp('2020-03-01:15:43:21', 'yyyy-MM-dd:HH:mm:ss'))  
FROM long_sequence(1);
```

| month |
| --- |
| 03 |

Using in an aggregation

```prism-code
SELECT month(ts), count() FROM transactions;
```

| month | count |
| --- | --- |
| 1 | 2323 |
| 2 | 6548 |
| ... | ... |
| 11 | 9876 |
| 12 | 2567 |

## nanos[​](#nanos "Direct link to nanos")

`nanos(value)` - returns the `nanos` of the second for a given date or
timestamp from `0` to `999`.

**Arguments:**

* `value` is any `timestamp`, `timestamp_ns`, or `date`

**Return value:**

Return value type is `int`

**Examples:**

Nanos of the second

```prism-code
SELECT nanos(  
    to_timestamp_ns('2020-03-01:15:43:21.123456789', 'yyyy-MM-dd:HH:mm:ss.SSSUUUNNN')) as nanos  
FROM long_sequence(1);
```

| nanos |
| --- |
| 789 |

## now[​](#now "Direct link to now")

`now()` - offset from UTC Epoch in microseconds.

Calculates `UTC timestamp` using system's real time clock. Unlike
`systimestamp()`, it does not change within the query execution timeframe and
should be used in WHERE clause to filter designated timestamp column relative to
current time, i.e.:

* `SELECT now() FROM long_sequence(200)` will return the same timestamp for all
  rows
* `SELECT systimestamp() FROM long_sequence(200)` will have new timestamp values
  for each row

**Arguments:**

* `now()` does not accept arguments.

**Return value:**

Return value type is `timestamp`.

**Examples:**

Filter records to created within last day

```prism-code
SELECT created, origin FROM telemetry  
WHERE created > dateadd('d', -1, now());
```

| created | origin |
| --- | --- |
| 2021-02-01T21:51:34.443726Z | 1 |

Query returns same timestamp in every row

```prism-code
SELECT now() FROM long_sequence(3)
```

| now |
| --- |
| 2021-02-01T21:51:34.443726Z |
| 2021-02-01T21:51:34.443726Z |
| 2021-02-01T21:51:34.443726Z |

Query based on last minute

```prism-code
SELECT * FROM trades  
WHERE timestamp > now() - 60000000L;
```

## pg\_postmaster\_start\_time[​](#pg_postmaster_start_time "Direct link to pg_postmaster_start_time")

`pg_postmaster_start_time()` - returns the time when the server started.

**Arguments**

* `pg_postmaster_start_time()` does not accept arguments.

**Return value:**

Return value type is `timestamp`

**Examples**

```prism-code
SELECT pg_postmaster_start_time();
```

| pg\_postmaster\_start\_time |
| --- |
| 2023-03-30T16:20:29.763961Z |

## second[​](#second "Direct link to second")

`second(value)` - returns the `second` of the minute for a given date or
timestamp from `0` to `59`.

**Arguments:**

* `value` is any `timestamp`, `timestamp_ns`, or `date`

**Return value:**

Return value type is `int`

**Examples:**

Second of the minute

```prism-code
SELECT second(to_timestamp('2020-03-01:15:43:21', 'yyyy-MM-dd:HH:mm:ss'))  
FROM long_sequence(1);
```

| second |
| --- |
| 43 |

Using in an aggregation

```prism-code
SELECT second(ts), count() FROM transactions;
```

| second | count |
| --- | --- |
| 0 | 2323 |
| 1 | 6548 |
| ... | ... |
| 58 | 9876 |
| 59 | 2567 |

## today, tomorrow, yesterday[​](#today-tomorrow-yesterday "Direct link to today, tomorrow, yesterday")

* `today()` - returns an interval representing the current day.
* `tomorrow()` - returns an interval representing the next day.
* `yesterday()` - returns an interval representing the previous day.

Interval is in the UTC/GMT+0 timezone.

**Arguments:**

No arguments taken.

**Return value:**

Return value is of type `interval`.

**Examples:**

Using today

```prism-code
SELECT true as in_today FROM long_sequence(1)  
WHERE now() IN today();
```

## today, tomorrow, yesterday with timezone[​](#today-tomorrow-yesterday-with-timezone "Direct link to today, tomorrow, yesterday with timezone")

* `today(timezone)` - returns an interval representing the current day with
  timezone adjustment.
* `tomorrow(timezone)` - returns an interval representing the next day timezone
  adjustment.
* `yesterday(timezone)` - returns an interval representing the previous day
  timezone adjustment.

**Arguments:**

`timezone` is a `string` matching a timezone.

**Return value:**

Return value is of type `interval`.

**Examples:**

Using today[Demo this query](https://demo.questdb.io/?query=SELECT%20today()%20as%20today%2C%20today('CEST')%20as%20adjusted%3B&executeQuery=true)

```prism-code
SELECT today() as today, today('CEST') as adjusted;
```

| today | adjusted |
| --- | --- |
| ('2024-10-08T00:00:00.000Z', '2024-10-08T23:59:59.999Z') | ('2024-10-07T22:00:00.000Z', '2024-10-08T21:59:59.999Z') |

This function allows the user to specify their local timezone and receive a UTC
interval that corresponds to their 'day'.

In this example, `CEST` is a +2h offset, so the `CEST` day started at `10:00 PM`
`UTC` the day before.

## sysdate[​](#sysdate "Direct link to sysdate")

`sysdate()` - returns the timestamp of the host system as a `date` with
`millisecond` precision.

Calculates `UTC date` with millisecond precision using system's real time clock.
The value is affected by discontinuous jumps in the system time (e.g., if the
system administrator manually changes the system time).

`sysdate()` value can change within the query execution timeframe and should
**NOT** be used in WHERE clause to filter designated timestamp column.

tip

Use `now()` with WHERE clause filter.

**Arguments:**

* `sysdate()` does not accept arguments.

**Return value:**

Return value type is `date`.

**Examples:**

Insert current system date along with a value

```prism-code
INSERT INTO readings  
VALUES(sysdate(), 123.5);
```

| sysdate | reading |
| --- | --- |
| 2020-01-02T19:28:48.727516Z | 123.5 |

Query based on last minute

```prism-code
SELECT * FROM trades  
WHERE timestamp > sysdate() - 60000000L;
```

## systimestamp[​](#systimestamp "Direct link to systimestamp")

`systimestamp()` - offset from UTC Epoch in microseconds. Calculates
`UTC timestamp` using system's real time clock. The value is affected by
discontinuous jumps in the system time (e.g., if the system administrator
manually changes the system time).

`systimestamp()` value can change within the query execution timeframe and
should **NOT** be used in WHERE clause to filter designated timestamp column.

tip

Use now() with WHERE clause filter.

**Arguments:**

* `systimestamp()` does not accept arguments.

**Return value:**

Return value type is `timestamp`.

**Examples:**

Insert current system timestamp

```prism-code
INSERT INTO readings  
VALUES(systimestamp(), 123.5);
```

| ts | reading |
| --- | --- |
| 2020-01-02T19:28:48.727516Z | 123.5 |

## systimestamp\_ns[​](#systimestamp_ns "Direct link to systimestamp_ns")

`systimestamp_ns()` - offset from UTC Epoch in nanoseconds. Calculates
`UTC timestamp` using system's real time clock. The value is affected by
discontinuous jumps in the system time (e.g., if the system administrator
manually changes the system time).

`systimestamp_ns()` value can change within the query execution timeframe and
should **NOT** be used in WHERE clause to filter designated timestamp column.

tip

Use now() with WHERE clause filter.

**Arguments:**

* `systimestamp_ns()` does not accept arguments.

**Return value:**

Return value type is `timestamp_ns`.

**Examples:**

Insert current system timestamp\_ns

```prism-code
INSERT INTO readings  
VALUES(systimestamp_ns(), 123.5);
```

| ts | reading |
| --- | --- |
| 2020-01-02T19:28:48.727516132Z | 123.5 |

## timestamp\_ceil[​](#timestamp_ceil "Direct link to timestamp_ceil")

`timestamp_ceil(unit, timestamp)` - performs a ceiling calculation on a
timestamp by given unit.

A unit must be provided to specify which granularity to perform rounding.

**Arguments:**

`timestamp_ceil(unit, timestamp)` has the following arguments:

`unit` - may be one of the following:

* `n` nanoseconds
* `U` microseconds
* `T` milliseconds
* `s` seconds
* `m` minutes
* `h` hours
* `d` days
* `M` months
* `y` year

`timestamp` - any `timestamp`, `timestamp_ns`, `date`, or date literal string value.

**Return value:**

Return value type defaults to `timestamp`, but it will return a `timestamp_ns` if the timestamp argument is of type
`timestamp_ns` or if the date passed as a string contains nanoseconds resolution.

**Examples:**

```prism-code
WITH t AS (SELECT cast('2016-02-10T16:18:22.862145333Z' AS timestamp_ns) ts)  
SELECT  
  ts,  
  timestamp_ceil('n', ts) c_nano,  
  timestamp_ceil('U', ts) c_micro,  
  timestamp_ceil('T', ts) c_milli,  
  timestamp_ceil('s', ts) c_second,  
  timestamp_ceil('m', ts) c_minute,  
  timestamp_ceil('h', ts) c_hour,  
  timestamp_ceil('d', ts) c_day,  
  timestamp_ceil('M', ts) c_month,  
  timestamp_ceil('y', ts) c_year  
  FROM t
```

| ts | c\_nano | c\_micro | c\_milli | c\_second | c\_minute | c\_hour | c\_day | c\_month | c\_year |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2016-02-10T16:18:22.862145333Z | 2016-02-10T16:18:22.862145333Z | 2016-02-10T16:18:22.862146000Z | 2016-02-10T16:18:22.863000000Z | 2016-02-10T16:18:23.000000000Z |  |  |  |  |  |

## timestamp\_floor[​](#timestamp_floor "Direct link to timestamp_floor")

`timestamp_floor(interval, timestamp)` - performs a floor calculation on a
timestamp by given interval expression.

An interval expression must be provided to specify which granularity to perform
rounding for.

**Arguments:**

`timestamp_floor(interval, timestamp)` has the following arguments:

`unit` - is a time interval expression that may use one of the following
suffices:

* `n` nanoseconds
* `U` microseconds
* `T` milliseconds
* `s` seconds
* `m` minutes
* `h` hours
* `d` days
* `M` months
* `y` year

`timestamp` - any `timestamp`, `timestamp_ns`, `date`, or date literal string value.

**Return value:**

Return value type defaults to `timestamp`, but it will return a `timestamp_ns` if the timestamp argument is of type
`timestamp_ns` or if the date passed as a string contains nanoseconds resolution.

**Examples:**

```prism-code
SELECT timestamp_floor('5d', '2018-01-01')
```

Gives:

| timestamp\_floor |
| --- |
| 2017-12-30T00:00:00.000000Z |

The number part of the expression is optional:

```prism-code
WITH t AS (SELECT cast('2016-02-10T16:18:22.862145333Z' AS timestamp_ns) ts)  
SELECT  
  ts,  
  timestamp_floor('n', ts) c_nano,  
  timestamp_floor('U', ts) c_micro,  
  timestamp_floor('T', ts) c_milli,  
  timestamp_floor('s', ts) c_second,  
  timestamp_floor('m', ts) c_minute,  
  timestamp_floor('h', ts) c_hour,  
  timestamp_floor('d', ts) c_day,  
  timestamp_floor('M', ts) c_month,  
  timestamp_floor('y', ts) c_year  
  FROM t
```

Gives:

| ts | c\_nano | c\_micro | c\_milli | c\_second | c\_minute | c\_hour | c\_day | c\_month | c\_year |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2016-02-10T16:18:22.862145333Z | 2016-02-10T16:18:22.862145333Z | 2016-02-10T16:18:22.862145000Z | 2016-02-10T16:18:22.862000000Z | 2016-02-10T16:18:22.000000000Z |  |  |  |  |  |

#### timestamp\_floor with offset[​](#timestamp_floor-with-offset "Direct link to timestamp_floor with offset")

When timestamps are floored by `timestamp_floor(interval, timestamp)`, they are
based on a root timestamp of `0`. This means that some floorings with a stride
can be confusing, since they are based on a modulo from `1970-01-01`.

For example:

```prism-code
SELECT timestamp_floor('5d', '2018-01-01')
```

Gives:

| timestamp\_floor |
| --- |
| 2017-12-30T00:00:00.000000Z |

If you wish to calculate bins from an offset other than `1970-01-01`, you can
add a third parameter: `timestamp_floor(interval, timestamp, offset)`. The
offset acts as a baseline from which further values are calculated.

```prism-code
SELECT timestamp_floor('5d', '2018-01-01', '2018-01-01')
```

Gives:

| timestamp\_floor |
| --- |
| 2018-01-01T00:00:00.000000Z |

You can test this on the QuestDB Demo:

```prism-code
SELECT timestamp_floor('5d', timestamp, '2018') t, count  
FROM trades  
WHERE timestamp in '2018'  
ORDER BY 1;
```

Gives:

| t | count |
| --- | --- |
| 2018-01-01T00:00:00.000000Z | 1226531 |
| 2018-01-06T00:00:00.000000Z | 1468302 |
| 2018-01-11T00:00:00.000000Z | 1604016 |
| 2018-01-16T00:00:00.000000Z | 1677303 |
| ... | ... |

## timestamp\_shuffle[​](#timestamp_shuffle "Direct link to timestamp_shuffle")

`timestamp_shuffle(timestamp_1, timestamp_2)` - generates a random timestamp
inclusively between the two input timestamps.

**Arguments:**

* `timestamp_1` - any `timestamp`, `timestamp_ns`, `date`, or date literal string value.
* `timestamp_2` - a timestamp value that is not equal to `timestamp_1`

**Return value:**

Return value type defaults to `timestamp`, but it will return a `timestamp_ns` if the timestamp argument is of type
`timestamp_ns` or if the date passed as a string contains nanoseconds resolution.

**Examples:**

```prism-code
SELECT timestamp_shuffle('2023-03-31T22:00:30.555998Z', '2023-04-01T22:00:30.555998Z');
```

| timestamp\_shuffle |
| --- |
| 2023-04-01T11:44:41.893394Z |

## to\_date[​](#to_date "Direct link to to_date")

note

While the `date` data type is available, we highly recommend applying the
`timestamp` data type in its place.

The only material advantage of date is a wider time range; timestamp however is
adequate in virtually all cases.

Date supports fewer functions and uses milliseconds instead of microseconds.

`to_date(string, format)` - converts string to `date` by using the supplied
`format` to extract the value.

Will convert a `string` to `date` using the format definition passed as an
argument. When the `format` definition does not match the `string` input, the
result will be `null`.

For more information about recognized timestamp formats, see the
[timestamp format section](#timestamp-format).

**Arguments:**

* `string` is any string that represents a date and/or time.
* `format` is a string that describes the `date format` in which `string` is
  expressed.

**Return value:**

Return value type is `date`

**Examples:**

string matches format[Demo this query](https://demo.questdb.io/?query=SELECT%20to_date('2020-03-01%3A15%3A43%3A21'%2C%20'yyyy-MM-dd%3AHH%3Amm%3Ass')%0AFROM%20trades%3B&executeQuery=true)

```prism-code
SELECT to_date('2020-03-01:15:43:21', 'yyyy-MM-dd:HH:mm:ss')  
FROM trades;
```

| to\_date |
| --- |
| 2020-03-01T15:43:21.000Z |

string does not match format

```prism-code
SELECT to_date('2020-03-01:15:43:21', 'yyyy')  
FROM long_sequence(1);
```

| to\_date |
| --- |
| null |

Using with INSERT

```prism-code
INSERT INTO measurements  
values(to_date('2019-12-12T12:15', 'yyyy-MM-ddTHH:mm'), 123.5);
```

| date | value |
| --- | --- |
| 2019-12-12T12:15:00.000Z | 123.5 |

## to\_str[​](#to_str "Direct link to to_str")

`to_str(value, format)` - converts timestamp value to a string in the specified
format.

Will convert a timestamp value to a string using the format definition passed as
an argument. When elements in the `format` definition are unrecognized, they
will be passed-through as string.

For more information about recognized timestamp formats, see the
[timestamp format section](#timestamp-format).

**Arguments:**

* `value` is any `date`, `timestamp`, or `timestamp_ns` value
* `format` is a timestamp format.

**Return value:**

Return value type is `string`

**Examples:**

* Basic example

```prism-code
SELECT to_str(systimestamp(), 'yyyy-MM-dd') FROM long_sequence(1);
```

| to\_str |
| --- |
| 2020-03-04 |

* With unrecognized timestamp definition

```prism-code
SELECT to_str(systimestamp(), 'yyyy-MM-dd gooD DAY 123') FROM long_sequence(1);
```

| to\_str |
| --- |
| 2020-03-04 gooD DAY 123 |

## to\_timestamp[​](#to_timestamp "Direct link to to_timestamp")

`to_timestamp(string, format)` - converts `string` to `timestamp` by using the
supplied `format` to extract the value with microsecond precision.

When the `format` definition does not match the `string` input, the result will
be `null`.

For more information about recognized timestamp formats, see the
[timestamp format section](#timestamp-format).

**Arguments:**

* `string` is any string that represents a date and/or time.
* `format` is a string that describes the timestamp format in which `string` is
  expressed.

**Return value:**

Return value type is `timestamp`. QuestDB provides `timestamp` with microsecond
resolution. Input strings with nanosecond precision will be parsed but lose the
precision. Use [`to_timestamp_ns`](#to_timestamp_ns) if nanosecond precision is required.

**Examples:**

Pattern matching with microsecond precision

```prism-code
SELECT to_timestamp('2020-03-01:15:43:21.127329', 'yyyy-MM-dd:HH:mm:ss.SSSUUU')  
FROM long_sequence(1);
```

| to\_timestamp |
| --- |
| 2020-03-01T15:43:21.127329Z |

Precision loss when pattern matching with nanosecond precision

```prism-code
SELECT to_timestamp('2020-03-01:15:43:00.000000001Z', 'yyyy-MM-dd:HH:mm:ss.SSSUUUNNNZ')  
FROM long_sequence(1);
```

| to\_timestamp |
| --- |
| 2020-03-01T15:43:00.000000Z |

String does not match format

```prism-code
SELECT to_timestamp('2020-03-01:15:43:21', 'yyyy')  
FROM long_sequence(1);
```

| to\_timestamp |
| --- |
| null |

Using with INSERT

```prism-code
INSERT INTO measurements  
values(to_timestamp('2019-12-12T12:15', 'yyyy-MM-ddTHH:mm'), 123.5);
```

| timestamp | value |
| --- | --- |
| 2019-12-12T12:15:00.000000Z | 123.5 |

Note that conversion of ISO timestamp format is optional. QuestDB automatically
converts `string` to `timestamp` if it is a partial or full form of
`yyyy-MM-ddTHH:mm:ss.SSSUUU` or `yyyy-MM-dd HH:mm:ss.SSSUUU` with a valid time
offset, `+01:00` or `Z`. See more examples in
[Native timestamp](/docs/query/sql/where/#native-timestamp-format)

## to\_timestamp\_ns[​](#to_timestamp_ns "Direct link to to_timestamp_ns")

`to_timestamp_ns(string, format)` - converts `string` to `timestamp_ns` by using the
supplied `format` to extract the value with nanosecond precision.

When the `format` definition does not match the `string` input, the result will
be `null`.

For more information about recognized timestamp formats, see the
[timestamp format section](#timestamp-format).

**Arguments:**

* `string` is any string that represents a date and/or time.
* `format` is a string that describes the timestamp format in which `string` is
  expressed.

**Return value:**

Return value type is `timestamp_ns`. If nanoseconds are not needed, you can use
[`to_timestamp`](#to_timestamp) instead.

**Examples:**

Pattern matching with nanosecond precision

```prism-code
SELECT to_timestamp_ns('2020-03-01:15:43:21.127329512', 'yyyy-MM-dd:HH:mm:ss.SSSUUUNNN') as timestamp_ns  
FROM long_sequence(1);
```

| timestamp\_ns |
| --- |
| 2020-03-01T15:43:21.127329512Z |

## to\_timezone[​](#to_timezone "Direct link to to_timezone")

`to_timezone(timestamp, timezone)` - converts a timestamp value to a specified
timezone. For more information on the time zone database used for this function,
see the
[QuestDB time zone database documentation](/docs/concepts/timestamps-timezones/).

**Arguments:**

* `timestamp` is any `timestamp`, `timestamp_ns`, microsecond Epoch, or string equivalent
* `timezone` may be `Country/City` tz database name, time zone abbreviation such
  as `PST` or in UTC offset in string format.

**Return value:**

Return value defaults to `timestamp`, but it will return a `timestamp_ns` if the timestamp argument is
of type `timestamp_ns` or if the date passed as a string contains nanoseconds resolution.

**Examples:**

* Unix UTC timestamp in microseconds to `Europe/Berlin`

```prism-code
SELECT to_timezone(1623167145000000, 'Europe/Berlin')
```

| to\_timezone |
| --- |
| 2021-06-08T17:45:45.000000Z |

* Unix UTC timestamp in microseconds to PST by UTC offset

```prism-code
SELECT to_timezone(1623167145000000, '-08:00')
```

| to\_timezone |
| --- |
| 2021-06-08T07:45:45.000000Z |

* Timestamp as string to `PST`

```prism-code
SELECT to_timezone('2021-06-08T13:45:45.000000Z', 'PST')
```

| to\_timezone |
| --- |
| 2021-06-08T06:45:45.000000Z |

## to\_utc[​](#to_utc "Direct link to to_utc")

`to_utc(timestamp, timezone)` - converts a timestamp by specified timezone to
UTC. May be provided a timezone in string format or a UTC offset in hours and
minutes. For more information on the time zone database used for this function,
see the
[QuestDB time zone database documentation](/docs/concepts/timestamps-timezones/).

**Arguments:**

* `timestamp` is any `timestamp`, `timestamp_ns`, microsecond Epoch, or string equivalent
* `timezone` may be `Country/City` tz database name, time zone abbreviation such
  as `PST` or in UTC offset in string format.

**Return value:**

Return value defaults to `timestamp`, but it will return a `timestamp_ns` if the timestamp argument is
of type `timestamp_ns` or if the date passed as a string contains nanoseconds resolution.

**Examples:**

* Convert a Unix timestamp in microseconds from the `Europe/Berlin` timezone to
  UTC

```prism-code
SELECT to_utc(1623167145000000, 'Europe/Berlin')
```

| to\_utc |
| --- |
| 2021-06-08T13:45:45.000000Z |

* Unix timestamp in microseconds from PST to UTC by UTC offset

```prism-code
SELECT to_utc(1623167145000000, '-08:00')
```

| to\_utc |
| --- |
| 2021-06-08T23:45:45.000000Z |

* Timestamp as string in `PST` to UTC

```prism-code
SELECT to_utc('2021-06-08T13:45:45.000000Z', 'PST')
```

| to\_utc |
| --- |
| 2021-06-08T20:45:45.000000Z |

## week\_of\_year[​](#week_of_year "Direct link to week_of_year")

`week_of_year(value)` - returns the number representing the week number in the
year.

**Arguments:**

* `value` is any `timestamp`, `timestamp_ns`, `date`, or date string literal.

**Return value:**

Return value type is `int`

**Examples**

```prism-code
SELECT week_of_year('2023-03-31T22:00:30.555998Z');
```

| week\_of\_year |
| --- |
| 13 |

## year[​](#year "Direct link to year")

`year(value)` - returns the `year` for a given timestamp

**Arguments:**

* `value` is any `timestamp`, `timestamp_ns`, `date`, or date string literal.

**Return value:**

Return value type is `int`

**Examples:**

Year

```prism-code
SELECT year(to_timestamp('2020-03-01:15:43:21', 'yyyy-MM-dd:HH:mm:ss'))  
FROM long_sequence(1);
```

| year |
| --- |
| 2020 |

Using in an aggregation

```prism-code
SELECT month(ts), count() FROM transactions;
```

| year | count |
| --- | --- |
| 2015 | 2323 |
| 2016 | 9876 |
| 2017 | 2567 |