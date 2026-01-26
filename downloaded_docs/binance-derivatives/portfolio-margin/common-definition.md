On this page

# Public API Definitions

## Terminology[​](/docs/derivatives/portfolio-margin/common-definition#terminology "Direct link to Terminology")

* `baseasseet` refers to the asset that is the `quantity` of a symbol.
* `quoteAsset` refers to the asset that is the `price` of a symbol.
* `Margin` refers to `Cross Margin`
* `UM` refers to `USD-M Futures`
* `CM` refers to `Coin-M Futures`

## ENUM definitions[​](/docs/derivatives/portfolio-margin/common-definition#enum-definitions "Direct link to ENUM definitions")

**Order side (side)**

* BUY
* SELL

**Position side for Futures (positionSide)**

* BOTH
* LONG
* SHORT

**Time in force (timeInForce)**

* GTC - Good Till Cancel
* IOC - Immediate or Cancel
* FOK - Fill or Kill
* GTX - Good Till Crossing (Post Only)

**Stop-Limit Time in force (stopLimitTimeInForce)**

* GTC - Good Till Cancel
* IOC - Immediate or Cancel
* FOK - Fill or Kill

**Side Effect Type (sideEffectType)**

* NO\_SIDE\_EFFECT
* MARGIN\_BUY
* AUTO\_REPAY

**Price Match (priceMatch)**

* NONE: no price match
* OPPONENT: counterparty best price
* OPPONENT\_5: counterparty 5th best price
* OPPONENT\_10: counterparty 10th best price
* OPPONENT\_20: counterparty 20th best price
* QUEUE: the best price on the same side of the order book
* QUEUE\_5: the 5th best price on the same side of the order book
* QUEUE\_10: the 10th best price on the same side of the order book
* QUEUE\_20: the 20th best price on the same side of the order book

**Self-Trade Prevention mode (selfTradePreventionMode)**

* NONE: No Self-Trade Prevention
* EXPIRE\_TAKER: expire taker order when STP trigger
* EXPIRE\_BOTH: expire taker and maker order when STP trigger
* EXPIRE\_MAKER: expire maker order when STP trigger

**Response Type (newOrderRespType)**

* ACK
* RESULT

**Order types (type)**

* LIMIT
* MARKET

**Conditional Order types (strategyType)**

* STOP
* STOP\_MARKET
* TAKE\_PROFIT
* TAKE\_PROFIT\_MARKET
* TRAILING\_STOP\_MARKET

**Working Type for Futures Conditional Orders (workingType)**

* MARK\_PRICE

**Order status (status)**

* NEW
* CANCELED
* REJECTED
* PARTIALLY\_FILLED
* FILLED
* EXPIRED

**Conditional Order status (strategyStatus)**

* NEW
* CANCELED
* TRIGGERED - conditional order is triggered
* FINISHED - triggered order is filled
* EXPIRED

**Futures Contract type (contractType):**

* PERPETUAL
* CURRENT\_MONTH
* NEXT\_MONTH
* CURRENT\_QUARTER
* NEXT\_QUARTER
* PERPETUAL\_DELIVERING

**Contract status (contractStatus, status):**

* PENDING\_TRADING
* TRADING
* PRE\_DELIVERING
* DELIVERING
* DELIVERED
* PRE\_SETTLE
* SETTLING
* CLOSE

**Rate limiters (rateLimitType)**

* REQUEST\_WEIGHT
* ORDERS

> **REQUEST\_WEIGHT**

```prism-code
  {  
    "rateLimitType": "REQUEST_WEIGHT",  
    "interval": "MINUTE",  
    "intervalNum": 1,  
    "limit": 2400  
  }
```

> **ORDERS**

```prism-code
  {  
    "rateLimitType": "ORDERS",  
    "interval": "MINUTE",  
    "intervalNum": 1,  
    "limit": 1200  
   }
```

**Rate limit intervals (interval)**

* MINUTE

# Filters

Filters define trading rules on a symbol or an exchange.

## Symbol filters[​](/docs/derivatives/portfolio-margin/common-definition#symbol-filters "Direct link to Symbol filters")

### PRICE\_FILTER[​](/docs/derivatives/portfolio-margin/common-definition#price_filter "Direct link to PRICE_FILTER")

The `PRICE_FILTER` defines the `price` rules for a symbol. There are 3 parts:

* `minPrice` defines the minimum `price`/`stopPrice` allowed; disabled on `minPrice` == 0.
* `maxPrice` defines the maximum `price`/`stopPrice` allowed; disabled on `maxPrice` == 0.
* `tickSize` defines the intervals that a `price`/`stopPrice` can be increased/decreased by; disabled on `tickSize` == 0.

Any of the above variables can be set to 0, which disables that rule in the `price filter`. In order to pass the `price filter`, the following must be true for `price`/`stopPrice` of the enabled rules:

* sell order `price` >= `minPrice`
* buy order `price` <= `maxPrice`
* (`price`-`minPrice`) % `tickSize` == 0

> **ExchangeInfo format:**

```prism-code
{  
    "filterType": "PRICE_FILTER",  
    "minPrice": "0.00000100",  
    "maxPrice": "100000.00000000",  
    "tickSize": "0.00000100"  
}
```

### LOT\_SIZE[​](/docs/derivatives/portfolio-margin/common-definition#lot_size "Direct link to LOT_SIZE")

The `LOT_SIZE` filter defines the `quantity` (aka "lots" in auction terms) rules for a symbol. There are 3 parts:

* `minQty` defines the minimum `quantity` allowed.
* `maxQty` defines the maximum `quantity` allowed.
* `stepSize` defines the intervals that a `quantity` can be increased/decreased by.

In order to pass the `lot size`, the following must be true for `quantity`:

* `quantity` >= `minQty`
* `quantity` <= `maxQty`
* (`quantity`-`minQty`) % `stepSize` == 0

> **/exchangeInfo format:**

```prism-code
{  
    "filterType": "LOT_SIZE",  
    "minQty": "0.00100000",  
    "maxQty": "100000.00000000",  
    "stepSize": "0.00100000"  
}
```

### PERCENT\_PRICE[​](/docs/derivatives/portfolio-margin/common-definition#percent_price "Direct link to PERCENT_PRICE")

The `PERCENT_PRICE` filter defines valid range for a price based on the mark price in Futures and on the average of the previous trades in Cross Margin. For Cross Margin `avgPriceMins` is the number of minutes the average price is calculated over. 0 means the last price is used.

In order to pass the `percent price`, the following must be true for `price`:

* Futures
  BUY: `price` <= `markPrice` \_ `multiplierUp`
  SELL: `price` >= `markPrice` \_ `multiplierDown`
* Cross Margin
  BUY: `price` <= `weightedAveragePrice` \_ `multiplierUp`
  SELL: `price` >= `weightedAveragePrice` \_ `multiplierDown`

### MIN\_NOTIONAL[​](/docs/derivatives/portfolio-margin/common-definition#min_notional "Direct link to MIN_NOTIONAL")

The `MIN_NOTIONAL` filter defines the minimum notional value allowed for an order on a symbol. An order's notional value is the `price` \* `quantity`. Since `MARKET` orders have no price, the `mark price` is used in Futures and the average price is used over the last `avgPriceMins` for Cross Margin. `avgPriceMins` is the number of minutes the average price is calculated over. 0 means the last price is used.

### MARKET\_LOT\_SIZE[​](/docs/derivatives/portfolio-margin/common-definition#market_lot_size "Direct link to MARKET_LOT_SIZE")

The `MARKET_LOT_SIZE` filter defines the `quantity` (aka "lots" in auction terms) rules for `MARKET` orders on a symbol. There are 3 parts:

* `minQty` defines the minimum `quantity` allowed.
* `maxQty` defines the maximum `quantity` allowed.
* `stepSize` defines the intervals that a `quantity` can be increased/decreased by.

In order to pass the `market lot size`, the following must be true for `quantity`:

* `quantity` >= `minQty`
* `quantity` <= `maxQty`
* (`quantity`-`minQty`) % `stepSize` == 0

> **/exchangeInfo format:**

```prism-code
{  
  "filterType": "MARKET_LOT_SIZE",  
  "minQty": "0.00100000",  
  "maxQty": "100000.00000000",  
  "stepSize": "0.00100000"  
}
```

### MAX\_NUM\_ORDERS[​](/docs/derivatives/portfolio-margin/common-definition#max_num_orders "Direct link to MAX_NUM_ORDERS")

The `MAX_NUM_ORDERS` filter defines the maximum number of orders an account is allowed to have open on a symbol.
Note that both "algo" orders and normal orders are counted for this filter.

> **/exchangeInfo format:**

```prism-code
{  
  "filterType": "MAX_NUM_ORDERS",  
  "limit": 200  
}
```

### MAX\_NUM\_ALGO\_ORDERS[​](/docs/derivatives/portfolio-margin/common-definition#max_num_algo_orders "Direct link to MAX_NUM_ALGO_ORDERS")

The `MAX_NUM_ALGO_ORDERS` filter defines the maximum number of all kinds of algo orders an account is allowed to have open on a symbol.
The algo orders include `STOP`, `STOP_MARKET`, `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`, and `TRAILING_STOP_MARKET` orders.

> **/exchangeInfo format:**

```prism-code
{  
  "filterType": "MAX_NUM_ALGO_ORDERS",  
  "limit": 100  
}
```