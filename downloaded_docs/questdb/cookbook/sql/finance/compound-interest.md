On this page

Calculate compound interest over multiple periods using SQL, where each period's interest is calculated on the previous period's ending balance. This is useful for financial modeling, investment projections, and interest calculations.

Generated Data

This query uses generated data from `long_sequence()` to create a time series of years, so it can run directly on the demo instance without requiring any existing tables.

## Problem: Need year-by-year growth[​](#problem-need-year-by-year-growth "Direct link to Problem: Need year-by-year growth")

You want to calculate compound interest over 5 years, starting with an initial principal of 1000, with an annual interest rate of 0.1 (10%). Each year's interest should be calculated on the previous year's ending balance.

## Solution: Use POWER function with window functions[​](#solution-use-power-function-with-window-functions "Direct link to Solution: Use POWER function with window functions")

The compound interest formula is `principal * (1 + rate)^periods`. Use `POWER()` to calculate the exponential part:

Calculate compound interest over 5 years[Demo this query](https://demo.questdb.io/?query=WITH%0Ayear_series%20AS%20(%0A%20%20%20%20DECLARE%20%40year%3A%3D2000%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%40rate%20%3A%3D%200.1%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%40principal%20%3A%3D%201000.0%0A%20%20%20%20SELECT%20%40year%20as%20start_year%2C%20%40year%20%2B%20(x%20-%201)%20AS%20timestamp%2C%0A%20%20%20%20%40rate%20AS%20interest_rate%2C%20%40principal%20as%20initial_principal%0A%20%20%20%20FROM%20long_sequence(5)%20--%20number%20of%20years%0A)%2C%0Acompounded_values%20AS%20(%0A%20%20%20%20SELECT%0A%20%20%20%20%20%20%20%20timestamp%2C%0A%20%20%20%20%20%20%20%20initial_principal%2C%0A%20%20%20%20%20%20%20%20interest_rate%2C%0A%20%20%20%20%20%20%20%20initial_principal%20*%0A%20%20%20%20%20%20%20%20%20%20%20%20POWER(%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%201%20%2B%20interest_rate%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20timestamp%20-%20start_year%20%2B%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20)%20AS%20compounding%0A%20%20%20%20FROM%0A%20%20%20%20%20%20%20%20year_series%0A)%2C%20compounding_year_before%20AS%20(%0ASELECT%0A%20%20%20%20timestamp%2C%0A%20%20%20%20initial_principal%2C%0A%20%20%20%20interest_rate%2C%0A%20%20%20%20LAG(cv.compounding)%20OVER%20(ORDER%20BY%20timestamp)%20AS%20year_principal%2C%0A%20%20%20%20cv.compounding%20as%20compounding_amount%0AFROM%0A%20%20%20%20compounded_values%20cv%0AORDER%20BY%0A%20%20%20%20timestamp%0A%20%20%20%20)%0Aselect%20timestamp%2C%20initial_principal%2C%20interest_rate%2C%0Acoalesce(year_principal%2C%20initial_principal)%20as%20year_principal%2C%0Acompounding_amount%0Afrom%20compounding_year_before%3B&executeQuery=true)

```prism-code
WITH  
year_series AS (  
    DECLARE @year:=2000,  
            @rate := 0.1,  
            @principal := 1000.0  
    SELECT @year as start_year, @year + (x - 1) AS timestamp,  
    @rate AS interest_rate, @principal as initial_principal  
    FROM long_sequence(5) -- number of years  
),  
compounded_values AS (  
    SELECT  
        timestamp,  
        initial_principal,  
        interest_rate,  
        initial_principal *  
            POWER(  
                  1 + interest_rate,  
                  timestamp - start_year + 1  
                  ) AS compounding  
    FROM  
        year_series  
), compounding_year_before AS (  
SELECT  
    timestamp,  
    initial_principal,  
    interest_rate,  
    LAG(cv.compounding) OVER (ORDER BY timestamp) AS year_principal,  
    cv.compounding as compounding_amount  
FROM  
    compounded_values cv  
ORDER BY  
    timestamp  
    )  
select timestamp, initial_principal, interest_rate,  
coalesce(year_principal, initial_principal) as year_principal,  
compounding_amount  
from compounding_year_before;
```

**Results:**

| timestamp | initial\_principal | interest\_rate | year\_principal | compounding\_amount |
| --- | --- | --- | --- | --- |
| 2000 | 1000.0 | 0.1 | 1000.0 | 1100.0 |
| 2001 | 1000.0 | 0.1 | 1100.0 | 1210.0 |
| 2002 | 1000.0 | 0.1 | 1210.0 | 1331.0 |
| 2003 | 1000.0 | 0.1 | 1331.0 | 1464.1 |
| 2004 | 1000.0 | 0.1 | 1464.1 | 1610.51 |

Each row shows how the principal grows year over year, with interest compounding on the previous year's ending balance.

## How it works[​](#how-it-works "Direct link to How it works")

The query uses a multi-step CTE approach:

1. **Generate year series**: Use `long_sequence(5)` to create 5 rows representing years 2000-2004
2. **Calculate compound amount**: Use `POWER(1 + interest_rate, years)` to compute the ending balance for each year
3. **Get previous year's balance**: Use `LAG()` to access the previous row's compounding amount
4. **Handle first year**: Use `COALESCE()` to show the initial principal for the first year

tip

For more complex scenarios like monthly or quarterly compounding, adjust the time period generation and the exponent in the POWER function accordingly.

Related Documentation

* [POWER function](/docs/query/functions/numeric/#power)
* [Window functions](/docs/query/functions/window-functions/syntax/)
* [LAG window function](/docs/query/functions/window-functions/reference/#lag)
* [long\_sequence](/docs/query/functions/row-generator/#long_sequence)