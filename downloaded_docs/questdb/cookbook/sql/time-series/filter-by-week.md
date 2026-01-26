On this page

Filter time-series data by week number using either the built-in `week_of_year()` function or `dateadd()` for better performance on large tables.

## Solution 1: Using week\_of\_year()[​](#solution-1-using-week_of_year "Direct link to Solution 1: Using week_of_year()")

There is a built-in `week_of_year()` function, so this could be solved as:

Filter by week using week\_of\_year()[Demo this query](https://demo.questdb.io/?query=SELECT%20*%20FROM%20trades%0AWHERE%20week_of_year(timestamp)%20%3D%2024%3B&executeQuery=true)

```prism-code
SELECT * FROM trades  
WHERE week_of_year(timestamp) = 24;
```

## Solution 2: Using dateadd() (faster)[​](#solution-2-using-dateadd-faster "Direct link to Solution 2: Using dateadd() (faster)")

However, depending on your table size, especially if you are not filtering by any timestamp, you might prefer this alternative, as it executes faster:

Filter by week using dateadd()[Demo this query](https://demo.questdb.io/?query=SELECT%20*%20FROM%20trades%0AWHERE%20timestamp%20%3E%3D%20dateadd('w'%2C%2023%2C%20'2025-01-01')%0A%20%20AND%20timestamp%20%3C%20dateadd('w'%2C%2024%2C%20'2025-01-01')%3B&executeQuery=true)

```prism-code
SELECT * FROM trades  
WHERE timestamp >= dateadd('w', 23, '2025-01-01')  
  AND timestamp < dateadd('w', 24, '2025-01-01');
```

You need to be careful with that query, as it will start counting time from Jan 1st 1970, which is not a Monday.

## Solution 3: Start at first Monday of year[​](#solution-3-start-at-first-monday-of-year "Direct link to Solution 3: Start at first Monday of year")

This alternative would start at the Monday of the week that includes January 1st:

Filter by week using first Monday calculation[Demo this query](https://demo.questdb.io/?query=DECLARE%0A%20%20%40year%20%3A%3D%20'2025'%2C%0A%20%20%40week%20%3A%3D%2024%2C%0A%20%20%40first_monday%20%3A%3D%20dateadd('d'%2C%20-1%20*%20day_of_week(%40year)%20%2B%201%2C%20%40year)%2C%0A%20%20%40week_start%20%3A%3D%20dateadd('w'%2C%20%40week%20-%201%2C%20%40first_monday)%2C%0A%20%20%40week_end%20%3A%3D%20dateadd('w'%2C%20%40week%2C%20%40first_monday)%0ASELECT%20*%20FROM%20trades%0AWHERE%20timestamp%20%3E%3D%20%40week_start%0A%20%20AND%20timestamp%20%3C%20%40week_end%3B&executeQuery=true)

```prism-code
DECLARE  
  @year := '2025',  
  @week := 24,  
  @first_monday := dateadd('d', -1 * day_of_week(@year) + 1, @year),  
  @week_start := dateadd('w', @week - 1, @first_monday),  
  @week_end := dateadd('w', @week, @first_monday)  
SELECT * FROM trades  
WHERE timestamp >= @week_start  
  AND timestamp < @week_end;
```

Related Documentation

* [week\_of\_year()](/docs/query/functions/date-time/#week_of_year)
* [dateadd()](/docs/query/functions/date-time/#dateadd)
* [day\_of\_week()](/docs/query/functions/date-time/#day_of_week)
* [DECLARE](/docs/query/sql/declare/)