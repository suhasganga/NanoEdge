On this page

# Filters

Filters define trading rules on a symbol or an exchange.
Filters come in three forms: `symbol filters`, `exchange filters` and `asset filters`.

## Symbol filters[​](/docs/binance-spot-api-docs/filters#symbol-filters "Direct link to Symbol filters")

### PRICE\_FILTER[​](/docs/binance-spot-api-docs/filters#price_filter "Direct link to PRICE_FILTER")

The `PRICE_FILTER` defines the `price` rules for a symbol. There are 3 parts:

* `minPrice` defines the minimum `price`/`stopPrice` allowed; disabled on `minPrice` == 0.
* `maxPrice` defines the maximum `price`/`stopPrice` allowed; disabled on `maxPrice` == 0.
* `tickSize` defines the intervals that a `price`/`stopPrice` can be increased/decreased by; disabled on `tickSize` == 0.

Any of the above variables can be set to 0, which disables that rule in the `price filter`. In order to pass the `price filter`, the following must be true for `price`/`stopPrice` of the enabled rules:

* `price` >= `minPrice`
* `price` <= `maxPrice`
* `price` % `tickSize` == 0

**/exchangeInfo format:**

```prism-code
{  
    "filterType": "PRICE_FILTER",  
    "minPrice": "0.00000100",  
    "maxPrice": "100000.00000000",  
    "tickSize": "0.00000100"  
}
```

### PERCENT\_PRICE[​](/docs/binance-spot-api-docs/filters#percent_price "Direct link to PERCENT_PRICE")

The `PERCENT_PRICE` filter defines the valid range for the price based on the average of the previous trades.
`avgPriceMins` is the number of minutes the average price is calculated over. 0 means the last price is used.

In order to pass the `percent price`, the following must be true for `price`:

* `price` <= `weightedAveragePrice` \* `multiplierUp`
* `price` >= `weightedAveragePrice` \* `multiplierDown`

**/exchangeInfo format:**

```prism-code
{  
    "filterType": "PERCENT_PRICE",  
    "multiplierUp": "1.3000",  
    "multiplierDown": "0.7000",  
    "avgPriceMins": 5  
}
```

### PERCENT\_PRICE\_BY\_SIDE[​](/docs/binance-spot-api-docs/filters#percent_price_by_side "Direct link to PERCENT_PRICE_BY_SIDE")

The `PERCENT_PRICE_BY_SIDE` filter defines the valid range for the price based on the average of the previous trades.  
`avgPriceMins` is the number of minutes the average price is calculated over. 0 means the last price is used.   
There is a different range depending on whether the order is placed on the `BUY` side or the `SELL` side.

Buy orders will succeed on this filter if:

* `Order price` <= `weightedAveragePrice` \* `bidMultiplierUp`
* `Order price` >= `weightedAveragePrice` \* `bidMultiplierDown`

Sell orders will succeed on this filter if:

* `Order Price` <= `weightedAveragePrice` \* `askMultiplierUp`
* `Order Price` >= `weightedAveragePrice` \* `askMultiplierDown`

**/exchangeInfo format:**

```prism-code
{  
    "filterType": "PERCENT_PRICE_BY_SIDE",  
    "bidMultiplierUp": "1.2",  
    "bidMultiplierDown": "0.2",  
    "askMultiplierUp": "5",  
    "askMultiplierDown": "0.8",  
    "avgPriceMins": 1  
}
```

### LOT\_SIZE[​](/docs/binance-spot-api-docs/filters#lot_size "Direct link to LOT_SIZE")

The `LOT_SIZE` filter defines the `quantity` (aka "lots" in auction terms) rules for a symbol. There are 3 parts:

* `minQty` defines the minimum `quantity`/`icebergQty` allowed.
* `maxQty` defines the maximum `quantity`/`icebergQty` allowed.
* `stepSize` defines the intervals that a `quantity`/`icebergQty` can be increased/decreased by.

In order to pass the `lot size`, the following must be true for `quantity`/`icebergQty`:

* `quantity` >= `minQty`
* `quantity` <= `maxQty`
* `quantity` % `stepSize` == 0

**/exchangeInfo format:**

```prism-code
{  
    "filterType": "LOT_SIZE",  
    "minQty": "0.00100000",  
    "maxQty": "100000.00000000",  
    "stepSize": "0.00100000"  
}
```

### MIN\_NOTIONAL[​](/docs/binance-spot-api-docs/filters#min_notional "Direct link to MIN_NOTIONAL")

The `MIN_NOTIONAL` filter defines the minimum notional value allowed for an order on a symbol.
An order's notional value is the `price` \* `quantity`.
`applyToMarket` determines whether or not the `MIN_NOTIONAL` filter will also be applied to `MARKET` orders.
Since `MARKET` orders have no price, the average price is used over the last `avgPriceMins` minutes.
`avgPriceMins` is the number of minutes the average price is calculated over. 0 means the last price is used.

**/exchangeInfo format:**

```prism-code
{  
    "filterType": "MIN_NOTIONAL",  
    "minNotional": "0.00100000",  
    "applyToMarket": true,  
    "avgPriceMins": 5  
}
```

### NOTIONAL[​](/docs/binance-spot-api-docs/filters#notional "Direct link to NOTIONAL")

The `NOTIONAL` filter defines the acceptable notional range allowed for an order on a symbol.   
  
`applyMinToMarket` determines whether the `minNotional` will be applied to `MARKET` orders.   
`applyMaxToMarket` determines whether the `maxNotional` will be applied to `MARKET` orders.

In order to pass this filter, the notional (`price * quantity`) has to pass the following conditions:

* `price * quantity` <= `maxNotional`
* `price * quantity` >= `minNotional`

For `MARKET` orders, the average price used over the last `avgPriceMins` minutes will be used for calculation.   
If the `avgPriceMins` is 0, then the last price will be used.

**/exchangeInfo format:**

```prism-code
{  
    "filterType": "NOTIONAL",  
    "minNotional": "10.00000000",  
    "applyMinToMarket": false,  
    "maxNotional": "10000.00000000",  
    "applyMaxToMarket": false,  
    "avgPriceMins": 5  
}
```

### ICEBERG\_PARTS[​](/docs/binance-spot-api-docs/filters#iceberg_parts "Direct link to ICEBERG_PARTS")

The `ICEBERG_PARTS` filter defines the maximum parts an iceberg order can have. The number of `ICEBERG_PARTS` is defined as `CEIL(qty / icebergQty)`.

**/exchangeInfo format:**

```prism-code
{  
    "filterType": "ICEBERG_PARTS",  
    "limit": 10  
}
```

### MARKET\_LOT\_SIZE[​](/docs/binance-spot-api-docs/filters#market_lot_size "Direct link to MARKET_LOT_SIZE")

The `MARKET_LOT_SIZE` filter defines the `quantity` (aka "lots" in auction terms) rules for `MARKET` orders on a symbol. There are 3 parts:

* `minQty` defines the minimum `quantity` allowed.
* `maxQty` defines the maximum `quantity` allowed.
* `stepSize` defines the intervals that a `quantity` can be increased/decreased by.

In order to pass the `market lot size`, the following must be true for `quantity`:

* `quantity` >= `minQty`
* `quantity` <= `maxQty`
* `quantity` % `stepSize` == 0

**/exchangeInfo format:**

```prism-code
{  
    "filterType": "MARKET_LOT_SIZE",  
    "minQty": "0.00100000",  
    "maxQty": "100000.00000000",  
    "stepSize": "0.00100000"  
}
```

### MAX\_NUM\_ORDERS[​](/docs/binance-spot-api-docs/filters#max_num_orders "Direct link to MAX_NUM_ORDERS")

The `MAX_NUM_ORDERS` filter defines the maximum number of orders an account is allowed to have open on a symbol.
Note that both "algo" orders and normal orders are counted for this filter.

**/exchangeInfo format:**

```prism-code
{  
    "filterType": "MAX_NUM_ORDERS",  
    "maxNumOrders": 25  
}
```

### MAX\_NUM\_ALGO\_ORDERS[​](/docs/binance-spot-api-docs/filters#max_num_algo_orders "Direct link to MAX_NUM_ALGO_ORDERS")

The `MAX_NUM_ALGO_ORDERS` filter defines the maximum number of "algo" orders an account is allowed to have open on a symbol.
"Algo" orders are `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders.

**/exchangeInfo format:**

```prism-code
{  
    "filterType": "MAX_NUM_ALGO_ORDERS",  
    "maxNumAlgoOrders": 5  
}
```

### MAX\_NUM\_ICEBERG\_ORDERS[​](/docs/binance-spot-api-docs/filters#max_num_iceberg_orders "Direct link to MAX_NUM_ICEBERG_ORDERS")

The `MAX_NUM_ICEBERG_ORDERS` filter defines the maximum number of `ICEBERG` orders an account is allowed to have open on a symbol.
An `ICEBERG` order is any order where the `icebergQty` is > 0.

**/exchangeInfo format:**

```prism-code
{  
    "filterType": "MAX_NUM_ICEBERG_ORDERS",  
    "maxNumIcebergOrders": 5  
}
```

### MAX\_POSITION[​](/docs/binance-spot-api-docs/filters#max_position "Direct link to MAX_POSITION")

The `MAX_POSITION` filter defines the allowed maximum position an account can have on the base asset of a symbol. An account's position defined as the sum of the account's:

1. free balance of the base asset
2. locked balance of the base asset
3. sum of the qty of all open BUY orders

`BUY` orders will be rejected if the account's position is greater than the maximum position allowed.

If an order's `quantity` can cause the position to overflow, this will also fail the `MAX_POSITION` filter.

**/exchangeInfo format:**

```prism-code
{  
    "filterType": "MAX_POSITION",  
    "maxPosition": "10.00000000"  
}
```

### TRAILING\_DELTA[​](/docs/binance-spot-api-docs/filters#trailing_delta "Direct link to TRAILING_DELTA")

The `TRAILING_DELTA` filter defines the minimum and maximum value for the parameter [`trailingDelta`](/docs/binance-spot-api-docs/faqs/trailing-stop-faq).

In order for a trailing stop order to pass this filter, the following must be true:

For `STOP_LOSS BUY`, `STOP_LOSS_LIMIT_BUY`,`TAKE_PROFIT SELL` and `TAKE_PROFIT_LIMIT SELL` orders:

* `trailingDelta` >= `minTrailingAboveDelta`
* `trailingDelta` <= `maxTrailingAboveDelta`

For `STOP_LOSS SELL`, `STOP_LOSS_LIMIT SELL`, `TAKE_PROFIT BUY`, and `TAKE_PROFIT_LIMIT BUY` orders:

* `trailingDelta` >= `minTrailingBelowDelta`
* `trailingDelta` <= `maxTrailingBelowDelta`

**/exchangeInfo format:**

```prism-code
{  
    "filterType": "TRAILING_DELTA",  
    "minTrailingAboveDelta": 10,  
    "maxTrailingAboveDelta": 2000,  
    "minTrailingBelowDelta": 10,  
    "maxTrailingBelowDelta": 2000  
}
```

### MAX\_NUM\_ORDER\_AMENDS[​](/docs/binance-spot-api-docs/filters#max_num_order_amends "Direct link to MAX_NUM_ORDER_AMENDS")

The `MAX_NUM_ORDER_AMENDS` filter defines the maximum number of times an order can be amended on the given symbol.

If there are too many order amendments made on a single order, you will receive the `-2038` error code.

**/exchangeInfo format:**

```prism-code
{  
    "filterType": "MAX_NUM_ORDER_AMENDS",  
    "maxNumOrderAmends": 10  
}
```

### MAX\_NUM\_ORDER\_LISTS[​](/docs/binance-spot-api-docs/filters#max_num_order_lists "Direct link to MAX_NUM_ORDER_LISTS")

The `MAX_NUM_ORDER_LISTS` filter defines the maximum number of open order lists an account can have on a symbol. Note that OTOCOs count as one order list.

**/exchangeInfo format:**

```prism-code
{  
    "filterType": "MAX_NUM_ORDER_LISTS",  
    "maxNumOrderLists": 20  
}
```

## Exchange Filters[​](/docs/binance-spot-api-docs/filters#exchange-filters "Direct link to Exchange Filters")

### EXCHANGE\_MAX\_NUM\_ORDERS[​](/docs/binance-spot-api-docs/filters#exchange_max_num_orders "Direct link to EXCHANGE_MAX_NUM_ORDERS")

The `EXCHANGE_MAX_NUM_ORDERS` filter defines the maximum number of orders an account is allowed to have open on the exchange.
Note that both "algo" orders and normal orders are counted for this filter.

**/exchangeInfo format:**

```prism-code
{  
    "filterType": "EXCHANGE_MAX_NUM_ORDERS",  
    "maxNumOrders": 1000  
}
```

### EXCHANGE\_MAX\_NUM\_ALGO\_ORDERS[​](/docs/binance-spot-api-docs/filters#exchange_max_num_algo_orders "Direct link to EXCHANGE_MAX_NUM_ALGO_ORDERS")

The `EXCHANGE_MAX_NUM_ALGO_ORDERS` filter defines the maximum number of "algo" orders an account is allowed to have open on the exchange.
"Algo" orders are `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders.

**/exchangeInfo format:**

```prism-code
{  
    "filterType": "EXCHANGE_MAX_NUM_ALGO_ORDERS",  
    "maxNumAlgoOrders": 200  
}
```

### EXCHANGE\_MAX\_NUM\_ICEBERG\_ORDERS[​](/docs/binance-spot-api-docs/filters#exchange_max_num_iceberg_orders "Direct link to EXCHANGE_MAX_NUM_ICEBERG_ORDERS")

The `EXCHANGE_MAX_NUM_ICEBERG_ORDERS` filter defines the maximum number of iceberg orders an account is allowed to have open on the exchange.

**/exchangeInfo format:**

```prism-code
{  
    "filterType": "EXCHANGE_MAX_NUM_ICEBERG_ORDERS",  
    "maxNumIcebergOrders": 10000  
}
```

### EXCHANGE\_MAX\_NUM\_ORDER\_LISTS[​](/docs/binance-spot-api-docs/filters#exchange_max_num_order_lists "Direct link to EXCHANGE_MAX_NUM_ORDER_LISTS")

The `EXCHANGE_MAX_NUM_ORDERS` filter defines the maximum number of order lists an account is allowed to have open on the exchange. Note that OTOCOs count as one order list.

**/exchangeInfo format:**

```prism-code
{  
    "filterType": "EXCHANGE_MAX_NUM_ORDER_LISTS",  
    "maxNumOrderLists": 20  
}
```

## Asset Filters[​](/docs/binance-spot-api-docs/filters#asset-filters "Direct link to Asset Filters")

### MAX\_ASSET[​](/docs/binance-spot-api-docs/filters#max_asset "Direct link to MAX_ASSET")

The `MAX_ASSET` filter defines the maximum quantity of an asset that an account is allowed to transact in a single order.

* When the asset is a symbol's base asset, the limit applies to the order's quantity.
* When the asset is a symbol's quote asset, the limit applies to the order's notional value.
* For example, a MAX\_ASSET filter for USDC applies to all symbols that have USDC as either a base or quote asset, such as:
  + USDCBNB
  + BNBUSDC

**/myFilters format:**

```prism-code
{  
    "filterType": "MAX_ASSET",  
    "asset": "USDC",  
    "limit": "42.00000000"  
}
```