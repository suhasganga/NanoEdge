On this page

In the following examples, we'll use the table schema below. The order book is
stored in a 2D array with two rows: the top row are the prices, and the bottom
row are the volumes at each price point.

Create Table with Arrays

```prism-code
CREATE TABLE market_data (  
  timestamp TIMESTAMP,  
  symbol SYMBOL,  
  bids DOUBLE[][],  
  asks DOUBLE[][]  
) TIMESTAMP(timestamp) PARTITION BY HOUR;
```

## Basic order book analytics[​](#basic-order-book-analytics "Direct link to Basic order book analytics")

### What is the bid-ask spread at any moment?[​](#what-is-the-bid-ask-spread-at-any-moment "Direct link to What is the bid-ask spread at any moment?")

Bid-Ask Spread[Demo this query](https://demo.questdb.io/?query=SELECT%20timestamp%2C%20spread(bids%5B1%5D%5B1%5D%2C%20asks%5B1%5D%5B1%5D)%20spread%0AFROM%20market_data%20WHERE%20symbol%3D'EURUSD'%0ALIMIT%20-10%3B&executeQuery=true)

```prism-code
SELECT timestamp, spread(bids[1][1], asks[1][1]) spread  
FROM market_data WHERE symbol='EURUSD'  
LIMIT -10;
```

#### Sample data and result[​](#sample-data-and-result "Direct link to Sample data and result")

Inserting Rows with Arrays

```prism-code
INSERT INTO market_data VALUES  
  ('2025-07-01T12:00:00Z', 'EURUSD', ARRAY[ [9.3, 9.2], [0, 0] ], ARRAY[ [10.1, 10.2], [0, 0] ]),  
  ('2025-07-01T12:00:01Z', 'EURUSD', ARRAY[ [9.7, 9.4], [0, 0] ], ARRAY[ [10.3, 10.5], [0, 0] ]);
```

| timestamp | spread |
| --- | --- |
| 2025-07-01T12:00:00 | 0.8 |
| 2025-07-01T12:00:01 | 0.6 |

### How much volume is available within 1% of the best price?[​](#how-much-volume-is-available-within-1-of-the-best-price "Direct link to How much volume is available within 1% of the best price?")

Volume Available within 1%[Demo this query](https://demo.questdb.io/?query=DECLARE%0A%20%20%20%20%40prices%20%3A%3D%20asks%5B1%5D%2C%0A%20%20%20%20%40volumes%20%3A%3D%20asks%5B2%5D%2C%0A%20%20%20%20%40best_price%20%3A%3D%20%40prices%5B1%5D%2C%0A%20%20%20%20%40multiplier%20%3A%3D%201.01%2C%0A%20%20%20%20%40target_price%20%3A%3D%20%40multiplier%20*%20%20%40best_price%2C%0A%20%20%20%20%40relevant_volume_levels%20%3A%3D%20%40volumes%5B1%3Ainsertion_point(%40prices%2C%20%40target_price)%5D%0ASELECT%20timestamp%2C%20array_sum(%40relevant_volume_levels)%20total_volume%0AFROM%20market_data%20WHERE%20symbol%3D'EURUSD'%0ALIMIT%20-10%3B&executeQuery=true)

```prism-code
DECLARE  
    @prices := asks[1],  
    @volumes := asks[2],  
    @best_price := @prices[1],  
    @multiplier := 1.01,  
    @target_price := @multiplier *  @best_price,  
    @relevant_volume_levels := @volumes[1:insertion_point(@prices, @target_price)]  
SELECT timestamp, array_sum(@relevant_volume_levels) total_volume  
FROM market_data WHERE symbol='EURUSD'  
LIMIT -10;
```

#### Sample data and result[​](#sample-data-and-result-1 "Direct link to Sample data and result")

```prism-code
INSERT INTO market_data VALUES  
  ('2025-07-01T12:00:00Z', 'EURUSD', NULL, ARRAY[ [10.00, 10.02, 10.04, 10.10, 10.12, 10.14], [10.0, 15, 13, 12, 18, 20] ]),  
  ('2025-07-01T12:00:01Z', 'EURUSD', NULL, ARRAY[ [20.00, 20.02, 20.04, 20.10, 20.12, 20.14], [1.0, 5, 3, 2, 8, 10] ]);
```

| timestamp | volume |
| --- | --- |
| 2025-07-01T12:00:00 | 50.0 |
| 2025-07-01T12:00:01 | 29.0 |

## Liquidity-driven execution[​](#liquidity-driven-execution "Direct link to Liquidity-driven execution")

### How much of a large order can be executed without moving the price more than a set amount?[​](#how-much-of-a-large-order-can-be-executed-without-moving-the-price-more-than-a-set-amount "Direct link to How much of a large order can be executed without moving the price more than a set amount?")

Find the order book level at which the price passes a threshold, and then sum
the sizes up to that level.

Sum Volumes Starting at Price Threshold[Demo this query](https://demo.questdb.io/?query=DECLARE%0A%20%20%40prices%20%3A%3D%20asks%5B1%5D%2C%0A%20%20%40volumes%20%3A%3D%20asks%5B2%5D%2C%0A%20%20%40best_price%20%3A%3D%20%40prices%5B1%5D%2C%0A%20%20%40price_delta%20%3A%3D%200.1%2C%0A%20%20%40target_price%20%3A%3D%20%40best_price%20%2B%20%40price_delta%2C%0A%20%20%40relevant_volumes%20%3A%3D%20%40volumes%5B1%3Ainsertion_point(%40prices%2C%20%40target_price)%5D%0ASELECT%20timestamp%2C%20array_sum(%40relevant_volumes)%20volume%0AFROM%20market_data%20WHERE%20symbol%3D'EURUSD'%0ALIMIT%20-10%3B&executeQuery=true)

```prism-code
DECLARE  
  @prices := asks[1],  
  @volumes := asks[2],  
  @best_price := @prices[1],  
  @price_delta := 0.1,  
  @target_price := @best_price + @price_delta,  
  @relevant_volumes := @volumes[1:insertion_point(@prices, @target_price)]  
SELECT timestamp, array_sum(@relevant_volumes) volume  
FROM market_data WHERE symbol='EURUSD'  
LIMIT -10;
```

#### Sample data and result[​](#sample-data-and-result-2 "Direct link to Sample data and result")

```prism-code
INSERT INTO market_data VALUES  
  ('2025-07-01T12:00:00Z', 'EURUSD', NULL, ARRAY[ [10.0, 10.02, 10.04, 10.10, 10.12, 10.14], [10.0, 15, 13, 12, 18, 20] ]),  
  ('2025-07-01T12:00:01Z', 'EURUSD', NULL, ARRAY[ [10.0, 10.10, 10.12, 10.14, 10.16, 10.18], [1.0, 5, 3, 2, 8, 10] ]);
```

| timestamp | volume |
| --- | --- |
| 2025-07-01T12:00:00 | 50.0 |
| 2025-07-01T12:00:01 | 6.0 |

### What price level will a buy order for the given volume reach?[​](#what-price-level-will-a-buy-order-for-the-given-volume-reach "Direct link to What price level will a buy order for the given volume reach?")

Price Level for Order with Given Volume[Demo this query](https://demo.questdb.io/?query=DECLARE%0A%20%20%40prices%20%3A%3D%20asks%5B1%5D%2C%0A%20%20%40volumes%20%3A%3D%20asks%5B2%5D%2C%0A%20%20%40target_volume%20%3A%3D%2030.0%0ASELECT%0A%20%20timestamp%2C%0A%20%20array_cum_sum(%40volumes)%20cum_volumes%2C%0A%20%20insertion_point(cum_volumes%2C%20%40target_volume%2C%20true)%20target_level%2C%0A%20%20%40prices%5Btarget_level%5D%20price%0AFROM%20market_data%20WHERE%20symbol%3D'EURUSD'%0ALIMIT%20-10%3B&executeQuery=true)

```prism-code
DECLARE  
  @prices := asks[1],  
  @volumes := asks[2],  
  @target_volume := 30.0  
SELECT  
  timestamp,  
  array_cum_sum(@volumes) cum_volumes,  
  insertion_point(cum_volumes, @target_volume, true) target_level,  
  @prices[target_level] price  
FROM market_data WHERE symbol='EURUSD'  
LIMIT -10;
```

#### Sample data and result[​](#sample-data-and-result-3 "Direct link to Sample data and result")

```prism-code
INSERT INTO market_data VALUES  
  ('2025-07-01T12:00:00Z', 'EURUSD', NULL, ARRAY[ [10.0, 10.02, 10.04, 10.10, 10.12, 10.14], [10.0, 15, 13, 12, 18, 20] ]),  
  ('2025-07-01T12:00:01Z', 'EURUSD', NULL, ARRAY[ [10.0, 10.02, 10.04, 10.10, 10.12, 10.14], [10.0,  5,  3, 12, 18, 20] ]);
```

| timestamp | cum\_volumes | target\_level | price |
| --- | --- | --- | --- |
| 2025-07-01T12:00:00 | [10.0, 25.0, 38.0, 50.0, ...] | 3 | 10.04 |
| 2025-07-01T12:00:01 | [10.0, 15.0, 18.0, 30.0, ...] | 4 | 10.10 |

## Order book imbalance[​](#order-book-imbalance "Direct link to Order book imbalance")

### Imbalance at the top level[​](#imbalance-at-the-top-level "Direct link to Imbalance at the top level")

What is the ratio of bid volume to ask volume at the top level of the order
book?

This indicates pressure in one direction (e.g. buyers heavily outweighing
sellers at the top of the book).

Bid/Ask Ratio[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20timestamp%2C%20bids%5B2%2C%201%5D%20%2F%20asks%5B2%2C%201%5D%20imbalance%0AFROM%20market_data%20WHERE%20symbol%3D'EURUSD'%0ALIMIT%20-10%3B&executeQuery=true)

```prism-code
SELECT  
  timestamp, bids[2, 1] / asks[2, 1] imbalance  
FROM market_data WHERE symbol='EURUSD'  
LIMIT -10;
```

#### Sample data and result[​](#sample-data-and-result-4 "Direct link to Sample data and result")

```prism-code
INSERT INTO market_data VALUES  
  ('2025-07-01T12:00:00Z', 'EURUSD', ARRAY[ [0.0,0], [20.0, 25] ], ARRAY[ [0.0,0], [10.0, 15] ]),  
  ('2025-07-01T12:00:01Z', 'EURUSD', ARRAY[ [0.0,0], [14.0, 45] ], ARRAY[ [0.0,0], [15.0,  2] ]);
```

| timestamp | imbalance |
| --- | --- |
| 2025-07-01T12:00:00 | 2.0 |
| 2025-07-01T12:00:01 | 0.93 |

### Cumulative imbalance (Top 3 Levels)[​](#cumulative-imbalance-top-3-levels "Direct link to Cumulative imbalance (Top 3 Levels)")

Cumulative Imbalance - Top 3 Levels[Demo this query](https://demo.questdb.io/?query=DECLARE%0A%20%20%40bid_volumes%20%3A%3D%20bids%5B2%5D%2C%0A%20%20%40ask_volumes%20%3A%3D%20asks%5B2%5D%0ASELECT%0A%20%20timestamp%2C%0A%20%20array_sum(%40bid_volumes%5B1%3A4%5D)%20bid_vol%2C%0A%20%20array_sum(%40ask_volumes%5B1%3A4%5D)%20ask_vol%2C%0A%20%20bid_vol%20%2F%20ask_vol%20ratio%0AFROM%20market_data%20WHERE%20symbol%3D'EURUSD'%0ALIMIT%20-10%3B&executeQuery=true)

```prism-code
DECLARE  
  @bid_volumes := bids[2],  
  @ask_volumes := asks[2]  
SELECT  
  timestamp,  
  array_sum(@bid_volumes[1:4]) bid_vol,  
  array_sum(@ask_volumes[1:4]) ask_vol,  
  bid_vol / ask_vol ratio  
FROM market_data WHERE symbol='EURUSD'  
LIMIT -10;
```

#### Sample data and result[​](#sample-data-and-result-5 "Direct link to Sample data and result")

```prism-code
INSERT INTO market_data VALUES  
  ('2025-07-01T12:00:00Z', 'EURUSD', ARRAY[ [0.0,0,0,0], [20.0, 25, 23, 22] ], ARRAY[ [0.0,0,0,0], [10.0, 15, 13, 12] ]),  
  ('2025-07-01T12:00:01Z', 'EURUSD', ARRAY[ [0.0,0,0,0], [14.0, 45, 22,  5] ], ARRAY[ [0.0,0,0,0], [15.0,  2, 20, 23] ]);
```

| timestamp | bid\_vol | ask\_vol | ratio |
| --- | --- | --- | --- |
| 2025-07-01T12:00:00 | 68.0 | 38.0 | 1.79 |
| 2025-07-01T12:00:01 | 81.0 | 37.0 | 2.19 |

### Detect quote stuffing/fading (Volume dropoff)[​](#detect-quote-stuffingfading-volume-dropoff "Direct link to Detect quote stuffing/fading (Volume dropoff)")

Detect where the order book thins out rapidly after the first two levels. This
signals lack of depth (fading) or fake orders (stuffing).

Volume Dropoff[Demo this query](https://demo.questdb.io/?query=DECLARE%0A%20%20%40volumes%20%3A%3D%20asks%5B2%5D%2C%0A%20%20%40dropoff_ratio%20%3A%3D%203.0%0ASELECT%20*%20FROM%20(%0A%20%20SELECT%0A%20%20%20%20timestamp%2C%0A%20%20%20%20array_avg(%40volumes%5B1%3A3%5D)%20top%2C%0A%20%20%20%20array_avg(%40volumes%5B3%3A6%5D)%20deep%0A%20%20FROM%20market_data%0A%20%20WHERE%20timestamp%20%3E%20dateadd('m'%2C-30%2Cnow())%20)%0AWHERE%20top%20%3E%20%40dropoff_ratio%20*%20deep%3B&executeQuery=true)

```prism-code
DECLARE  
  @volumes := asks[2],  
  @dropoff_ratio := 3.0  
SELECT * FROM (  
  SELECT  
    timestamp,  
    array_avg(@volumes[1:3]) top,  
    array_avg(@volumes[3:6]) deep  
  FROM market_data  
  WHERE timestamp > dateadd('m',-30,now()) )  
WHERE top > @dropoff_ratio * deep;
```

#### Sample data and result[​](#sample-data-and-result-6 "Direct link to Sample data and result")

```prism-code
INSERT INTO market_data VALUES  
  ('2025-07-01T12:00:00Z', 'EURUSD', NULL, ARRAY[ [0.0,0,0,0,0,0], [20.0, 15, 13, 12, 18, 20] ]),  
  ('2025-07-01T12:00:01Z', 'EURUSD', NULL, ARRAY[ [0.0,0,0,0,0,0], [20.0, 25,  3,  7,  5,  2] ]);
```

| timestamp | top | deep |
| --- | --- | --- |
| 2025-07-01T12:00:01 | 22.5 | 5.0 |

### Detect sudden bid/ask drop[​](#detect-sudden-bidask-drop "Direct link to Detect sudden bid/ask drop")

Look for cases where the top bid/ask volume dropped compared to the prior
snapshot — potential order withdrawal ahead of adverse movement.

Sudden Drop[Demo this query](https://demo.questdb.io/?query=DECLARE%0A%20%20%40top_bid_volume%20%3A%3D%20bids%5B2%2C%201%5D%2C%0A%20%20%40top_ask_volume%20%3A%3D%20asks%5B2%2C%201%5D%2C%0A%20%20%40drop_ratio%20%3A%3D%201.5%0ASELECT%20*%20FROM%20(%0A%20%20SELECT%0A%20%20%20%20timestamp%2C%0A%20%20%20%20lag(%40top_bid_volume)%20OVER%20()%20prev_bid_vol%2C%0A%20%20%20%20%40top_bid_volume%20curr_bid_vol%2C%0A%20%20%20%20lag(%40top_ask_volume)%20OVER%20()%20prev_ask_vol%2C%0A%20%20%20%20%40top_ask_volume%20curr_ask_vol%0A%20%20FROM%20market_data%20WHERE%20timestamp%20%3E%20dateadd('h'%2C-1%2Cnow())%20AND%20symbol%3D'EURUSD'%20)%0AWHERE%20prev_bid_vol%20%3E%20curr_bid_vol%20*%20%40drop_ratio%20OR%20prev_ask_vol%20%3E%20curr_ask_vol%20*%20%40drop_ratio%0ALIMIT%2010%3B&executeQuery=true)

```prism-code
DECLARE  
  @top_bid_volume := bids[2, 1],  
  @top_ask_volume := asks[2, 1],  
  @drop_ratio := 1.5  
SELECT * FROM (  
  SELECT  
    timestamp,  
    lag(@top_bid_volume) OVER () prev_bid_vol,  
    @top_bid_volume curr_bid_vol,  
    lag(@top_ask_volume) OVER () prev_ask_vol,  
    @top_ask_volume curr_ask_vol  
  FROM market_data WHERE timestamp > dateadd('h',-1,now()) AND symbol='EURUSD' )  
WHERE prev_bid_vol > curr_bid_vol * @drop_ratio OR prev_ask_vol > curr_ask_vol * @drop_ratio  
LIMIT 10;
```

#### Sample data and result[​](#sample-data-and-result-7 "Direct link to Sample data and result")

```prism-code
INSERT INTO market_data VALUES  
  ('2025-07-01T12:00:00Z', 'EURUSD', ARRAY[ [0.0], [10.0] ], ARRAY[ [0.0], [10.0] ]),  
  ('2025-07-01T12:00:01Z', 'EURUSD', ARRAY[ [0.0], [ 9.0] ], ARRAY[ [0.0], [ 9.0] ]),  
  ('2025-07-01T12:00:02Z', 'EURUSD', ARRAY[ [0.0], [ 8.0] ], ARRAY[ [0.0], [ 4.0] ]),  
  ('2025-07-01T12:00:03Z', 'EURUSD', ARRAY[ [0.0], [ 4.0] ], ARRAY[ [0.0], [ 4.0] ]);
```

| timestamp | prev\_bid\_vol | curr\_bid\_vol | prev\_ask\_vol | curr\_ask\_vol |
| --- | --- | --- | --- | --- |
| 2025-07-01T12:00:02 | 9.0 | 8.0 | 9.0 | 4.0 |
| 2025-07-01T12:00:03 | 8.0 | 4.0 | 4.0 | 4.0 |

### Price-weighted volume imbalance[​](#price-weighted-volume-imbalance "Direct link to Price-weighted volume imbalance")

For each level, calculate the deviation from the mid price (midpoint between
best bid and best ask), and weight it by the volume at that level. This shows us
whether there's stronger buying or selling interest.

Price-weighted volume imbalance[Demo this query](https://demo.questdb.io/?query=DECLARE%0A%20%20%40bid_prices%20%3A%3D%20bids%5B1%5D%2C%0A%20%20%40bid_volumes%20%3A%3D%20bids%5B2%5D%2C%0A%20%20%40ask_prices%20%3A%3D%20asks%5B1%5D%2C%0A%20%20%40ask_volumes%20%3A%3D%20asks%5B2%5D%2C%0A%20%20%40best_bid_price%20%3A%3D%20bids%5B1%2C%201%5D%2C%0A%20%20%40best_ask_price%20%3A%3D%20asks%5B1%2C%201%5D%0ASELECT%0A%20%20timestamp%2C%0A%20%20round((%40best_bid_price%20%2B%20%40best_ask_price)%20%2F%202%2C%202)%20mid_price%2C%0A%20%20(mid_price%20-%20%40bid_prices)%20*%20%40bid_volumes%20weighted_bid_pressure%2C%0A%20%20(%40ask_prices%20-%20mid_price)%20*%20%40ask_volumes%20weighted_ask_pressure%0AFROM%20market_data%20WHERE%20timestamp%20IN%20today()%20AND%20symbol%3D'EURUSD'%0ALIMIT%20-10%3B&executeQuery=true)

```prism-code
DECLARE  
  @bid_prices := bids[1],  
  @bid_volumes := bids[2],  
  @ask_prices := asks[1],  
  @ask_volumes := asks[2],  
  @best_bid_price := bids[1, 1],  
  @best_ask_price := asks[1, 1]  
SELECT  
  timestamp,  
  round((@best_bid_price + @best_ask_price) / 2, 2) mid_price,  
  (mid_price - @bid_prices) * @bid_volumes weighted_bid_pressure,  
  (@ask_prices - mid_price) * @ask_volumes weighted_ask_pressure  
FROM market_data WHERE timestamp IN today() AND symbol='EURUSD'  
LIMIT -10;
```

#### Sample data and result[​](#sample-data-and-result-8 "Direct link to Sample data and result")

```prism-code
INSERT INTO market_data VALUES  
  ('2025-07-01T12:00:00Z', 'EURUSD', ARRAY[ [5.0, 5.1], [10.0, 20] ], ARRAY[ [6.0, 6.1], [15.0, 25] ]),  
  ('2025-07-01T12:00:01Z', 'EURUSD', ARRAY[ [5.1, 5.2], [20.0, 25] ], ARRAY[ [6.2, 6.4], [20.0,  9] ]);
```

| timestamp | mid\_price | weighted\_bid\_pressure | weighted\_ask\_pressure |
| --- | --- | --- | --- |
| 2025-07-01T12:00:00 | 5.5 | [5.0, 8.0] | [7.5, 15.0] |
| 2025-07-01T12:00:01 | 5.65 | [11.0, 11.25] | [11.0, 6.75] |