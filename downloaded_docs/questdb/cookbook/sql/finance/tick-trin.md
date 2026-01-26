On this page

Calculate TICK and TRIN (Trading Index, also known as the ARMS Index) to measure market breadth. These indicators classify each time period as advancing or declining based on price movement.

## Problem: Measure market breadth by price direction[​](#problem-measure-market-breadth-by-price-direction "Direct link to Problem: Measure market breadth by price direction")

You want to calculate TICK and TRIN indicators using traditional definitions:

* **Uptick**: Current price > previous price
* **Downtick**: Current price < previous price
* **TICK** = upticks - downticks
* **TRIN** = (upticks / downticks) / (uptick\_volume / downtick\_volume)

## Solution: Use LAG to compare consecutive prices[​](#solution-use-lag-to-compare-consecutive-prices "Direct link to Solution: Use LAG to compare consecutive prices")

### Per-symbol TICK and TRIN[​](#per-symbol-tick-and-trin "Direct link to Per-symbol TICK and TRIN")

Calculate separate indicators for each currency pair:

TICK and TRIN per symbol[Demo this query](https://demo.questdb.io/?query=WITH%20candles%20AS%20(%0A%20%20SELECT%20timestamp%2C%20symbol%2C%20last(price)%20AS%20close%2C%20sum(quantity)%20AS%20total_volume%0A%20%20FROM%20fx_trades%0A%20%20WHERE%20timestamp%20IN%20yesterday()%0A%20%20%20%20AND%20symbol%20IN%20('EURUSD'%2C%20'GBPUSD'%2C%20'USDJPY')%0A%20%20SAMPLE%20BY%2010m%0A)%2C%0Aprev_prices%20AS%20(%0A%20%20SELECT%20timestamp%2C%20symbol%2C%20close%2C%20total_volume%2C%0A%20%20%20%20LAG(close)%20OVER%20(PARTITION%20BY%20symbol%20ORDER%20BY%20timestamp)%20AS%20prev_close%0A%20%20FROM%20candles%0A)%2C%0Aclassified%20AS%20(%0A%20%20SELECT%20*%2C%0A%20%20%20%20CASE%20WHEN%20close%20%3E%20prev_close%20THEN%201%20ELSE%200%20END%20AS%20is_uptick%2C%0A%20%20%20%20CASE%20WHEN%20close%20%3C%20prev_close%20THEN%201%20ELSE%200%20END%20AS%20is_downtick%2C%0A%20%20%20%20CASE%20WHEN%20close%20%3E%20prev_close%20THEN%20total_volume%20ELSE%200%20END%20AS%20uptick_vol%2C%0A%20%20%20%20CASE%20WHEN%20close%20%3C%20prev_close%20THEN%20total_volume%20ELSE%200%20END%20AS%20downtick_vol%0A%20%20FROM%20prev_prices%0A%20%20WHERE%20prev_close%20IS%20NOT%20NULL%0A)%2C%0Aaggregated%20AS%20(%0A%20%20SELECT%20symbol%2C%0A%20%20%20%20SUM(is_uptick)%20AS%20upticks%2C%0A%20%20%20%20SUM(is_downtick)%20AS%20downticks%2C%0A%20%20%20%20SUM(is_uptick)%20-%20SUM(is_downtick)%20AS%20tick%2C%0A%20%20%20%20SUM(uptick_vol)%20AS%20uptick_vol%2C%0A%20%20%20%20SUM(downtick_vol)%20AS%20downtick_vol%0A%20%20FROM%20classified%0A)%0ASELECT%20symbol%2C%0A%20%20upticks%2C%0A%20%20downticks%2C%0A%20%20tick%2C%0A%20%20upticks%3A%3Adouble%20%2F%20downticks%20AS%20advance_decline_ratio%2C%0A%20%20uptick_vol%3A%3Adouble%20%2F%20downtick_vol%20AS%20upside_downside_ratio%2C%0A%20%20(upticks%3A%3Adouble%20%2F%20downticks)%20%2F%20(uptick_vol%3A%3Adouble%20%2F%20downtick_vol)%20AS%20trin%0AFROM%20aggregated%3B&executeQuery=true)

```prism-code
WITH candles AS (  
  SELECT timestamp, symbol, last(price) AS close, sum(quantity) AS total_volume  
  FROM fx_trades  
  WHERE timestamp IN yesterday()  
    AND symbol IN ('EURUSD', 'GBPUSD', 'USDJPY')  
  SAMPLE BY 10m  
),  
prev_prices AS (  
  SELECT timestamp, symbol, close, total_volume,  
    LAG(close) OVER (PARTITION BY symbol ORDER BY timestamp) AS prev_close  
  FROM candles  
),  
classified AS (  
  SELECT *,  
    CASE WHEN close > prev_close THEN 1 ELSE 0 END AS is_uptick,  
    CASE WHEN close < prev_close THEN 1 ELSE 0 END AS is_downtick,  
    CASE WHEN close > prev_close THEN total_volume ELSE 0 END AS uptick_vol,  
    CASE WHEN close < prev_close THEN total_volume ELSE 0 END AS downtick_vol  
  FROM prev_prices  
  WHERE prev_close IS NOT NULL  
),  
aggregated AS (  
  SELECT symbol,  
    SUM(is_uptick) AS upticks,  
    SUM(is_downtick) AS downticks,  
    SUM(is_uptick) - SUM(is_downtick) AS tick,  
    SUM(uptick_vol) AS uptick_vol,  
    SUM(downtick_vol) AS downtick_vol  
  FROM classified  
)  
SELECT symbol,  
  upticks,  
  downticks,  
  tick,  
  upticks::double / downticks AS advance_decline_ratio,  
  uptick_vol::double / downtick_vol AS upside_downside_ratio,  
  (upticks::double / downticks) / (uptick_vol::double / downtick_vol) AS trin  
FROM aggregated;
```

### Market-wide TICK and TRIN[​](#market-wide-tick-and-trin "Direct link to Market-wide TICK and TRIN")

Aggregate across all symbols for a single market breadth reading:

Market-wide TICK and TRIN[Demo this query](https://demo.questdb.io/?query=WITH%20candles%20AS%20(%0A%20%20SELECT%20timestamp%2C%20symbol%2C%20last(price)%20AS%20close%2C%20sum(quantity)%20AS%20total_volume%0A%20%20FROM%20fx_trades%0A%20%20WHERE%20timestamp%20IN%20yesterday()%0A%20%20%20%20AND%20symbol%20IN%20('EURUSD'%2C%20'GBPUSD'%2C%20'USDJPY')%0A%20%20SAMPLE%20BY%2010m%0A)%2C%0Aprev_prices%20AS%20(%0A%20%20SELECT%20timestamp%2C%20symbol%2C%20close%2C%20total_volume%2C%0A%20%20%20%20LAG(close)%20OVER%20(PARTITION%20BY%20symbol%20ORDER%20BY%20timestamp)%20AS%20prev_close%0A%20%20FROM%20candles%0A)%2C%0Aclassified%20AS%20(%0A%20%20SELECT%20*%2C%0A%20%20%20%20CASE%20WHEN%20close%20%3E%20prev_close%20THEN%201%20ELSE%200%20END%20AS%20is_uptick%2C%0A%20%20%20%20CASE%20WHEN%20close%20%3C%20prev_close%20THEN%201%20ELSE%200%20END%20AS%20is_downtick%2C%0A%20%20%20%20CASE%20WHEN%20close%20%3E%20prev_close%20THEN%20total_volume%20ELSE%200%20END%20AS%20uptick_vol%2C%0A%20%20%20%20CASE%20WHEN%20close%20%3C%20prev_close%20THEN%20total_volume%20ELSE%200%20END%20AS%20downtick_vol%0A%20%20FROM%20prev_prices%0A%20%20WHERE%20prev_close%20IS%20NOT%20NULL%0A)%2C%0Aaggregated%20AS%20(%0A%20%20SELECT%0A%20%20%20%20SUM(is_uptick)%20AS%20upticks%2C%0A%20%20%20%20SUM(is_downtick)%20AS%20downticks%2C%0A%20%20%20%20SUM(is_uptick)%20-%20SUM(is_downtick)%20AS%20tick%2C%0A%20%20%20%20SUM(uptick_vol)%20AS%20uptick_vol%2C%0A%20%20%20%20SUM(downtick_vol)%20AS%20downtick_vol%0A%20%20FROM%20classified%0A)%0ASELECT%0A%20%20upticks%2C%0A%20%20downticks%2C%0A%20%20tick%2C%0A%20%20upticks%3A%3Adouble%20%2F%20downticks%20AS%20advance_decline_ratio%2C%0A%20%20uptick_vol%3A%3Adouble%20%2F%20downtick_vol%20AS%20upside_downside_ratio%2C%0A%20%20(upticks%3A%3Adouble%20%2F%20downticks)%20%2F%20(uptick_vol%3A%3Adouble%20%2F%20downtick_vol)%20AS%20trin%0AFROM%20aggregated%3B&executeQuery=true)

```prism-code
WITH candles AS (  
  SELECT timestamp, symbol, last(price) AS close, sum(quantity) AS total_volume  
  FROM fx_trades  
  WHERE timestamp IN yesterday()  
    AND symbol IN ('EURUSD', 'GBPUSD', 'USDJPY')  
  SAMPLE BY 10m  
),  
prev_prices AS (  
  SELECT timestamp, symbol, close, total_volume,  
    LAG(close) OVER (PARTITION BY symbol ORDER BY timestamp) AS prev_close  
  FROM candles  
),  
classified AS (  
  SELECT *,  
    CASE WHEN close > prev_close THEN 1 ELSE 0 END AS is_uptick,  
    CASE WHEN close < prev_close THEN 1 ELSE 0 END AS is_downtick,  
    CASE WHEN close > prev_close THEN total_volume ELSE 0 END AS uptick_vol,  
    CASE WHEN close < prev_close THEN total_volume ELSE 0 END AS downtick_vol  
  FROM prev_prices  
  WHERE prev_close IS NOT NULL  
),  
aggregated AS (  
  SELECT  
    SUM(is_uptick) AS upticks,  
    SUM(is_downtick) AS downticks,  
    SUM(is_uptick) - SUM(is_downtick) AS tick,  
    SUM(uptick_vol) AS uptick_vol,  
    SUM(downtick_vol) AS downtick_vol  
  FROM classified  
)  
SELECT  
  upticks,  
  downticks,  
  tick,  
  upticks::double / downticks AS advance_decline_ratio,  
  uptick_vol::double / downtick_vol AS upside_downside_ratio,  
  (upticks::double / downticks) / (uptick_vol::double / downtick_vol) AS trin  
FROM aggregated;
```

## Interpreting the indicators[​](#interpreting-the-indicators "Direct link to Interpreting the indicators")

**TICK:**

* **Positive**: More upticks than downticks (bullish)
* **Negative**: More downticks than upticks (bearish)
* **Near zero**: Balanced market

**TRIN (ARMS Index):**

* **< 1.0**: Volume favoring advances (bullish)
* **> 1.0**: Volume favoring declines (bearish)
* **= 1.0**: Neutral

TRIN limitations

TRIN can produce counterintuitive results. For example, if advances outnumber declines 2:1 and advancing volume also leads 2:1, TRIN equals 1.0 (neutral) despite bullish conditions. The query includes separate **advance\_decline\_ratio** and **upside\_downside\_ratio** columns to help identify such cases.

Related documentation

* [Window functions](/docs/query/functions/window-functions/syntax/)
* [LAG function](/docs/query/functions/window-functions/reference/#lag)
* [CASE expressions](/docs/query/sql/case/)