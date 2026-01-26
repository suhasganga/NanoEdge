On this page

# Public Endpoints Info

## Terminology[​](/docs/derivatives/options-trading/common-definition#terminology "Direct link to Terminology")

* `symbol` refers to the symbol name of a options contract symbol
* `underlying` refers to the underlying symbol of a options contract symbol
* `quoteAsset` refers to the asset that is the price of a symbol.
* `settleAsset` refers to the settlement asset when options are exercised

## ENUM definitions[​](/docs/derivatives/options-trading/common-definition#enum-definitions "Direct link to ENUM definitions")

**Options contract type**

* CALL
* PUT

**Order side (side)**

* BUY
* SELL

**Position side (positionSide)**

* LONG
* SHORT

**Time in force (timeInForce)**

* GTC - Good Till Cancel
* IOC - Immediate or Cancel
* FOK - Fill or Kill
* GTX - Post only

**Response Type (newOrderRespType)**

* ACK
* RESULT

**Order types (type)**

* LIMIT

**Order status (status)**

* NEW
* REJECTED
* PARTIALLY\_FILLED
* FILLED
* CANCELED
* EXPIRED

**Kline/Candlestick chart intervals:**

m -> minutes; h -> hours; d -> days; w -> weeks; M -> months

* 1m
* 3m
* 5m
* 15m
* 30m
* 1h
* 2h
* 4h
* 6h
* 8h
* 12h
* 1d
* 3d
* 1w
* 1M

**Rate limiters (rateLimitType)**

> REQUEST\_WEIGHT

```prism-code
  {  
  	"rateLimitType": "REQUEST_WEIGHT",  
  	"interval": "MINUTE",  
  	"intervalNum": 1,  
  	"limit": 2400  
  }
```

> ORDERS

```prism-code
  {  
  	"rateLimitType": "ORDERS",  
  	"interval": "MINUTE",  
  	"intervalNum": 1,  
  	"limit": 1200  
   }
```

* REQUEST\_WEIGHT
* ORDERS

**Rate limit intervals (interval)**

* MINUTE

# Filters

Filters define trading rules on a symbol or an exchange.

## Symbol filters[​](/docs/derivatives/options-trading/common-definition#symbol-filters "Direct link to Symbol filters")

### PRICE\_FILTER[​](/docs/derivatives/options-trading/common-definition#price_filter "Direct link to PRICE_FILTER")

> **/exchangeInfo format:**

```prism-code
{  
  "filterType": "PRICE_FILTER",  
  "minPrice": "793.112",  
  "maxPrice": "1189.668",  
  "tickSize": "5.000"  
}
```

The `PRICE_FILTER` defines the `price` rules for a symbol. There are 3 parts:

* `minPrice` defines the minimum `price` allowed; disabled on `minPrice` == 0.
* `maxPrice` defines the maximum `price` allowed; disabled on `maxPrice` == 0.
* `tickSize` defines the intervals that a `price` can be increased/decreased by; disabled on `tickSize` == 0.

Any of the above variables can be set to 0, which disables that rule in the `price filter`. In order to pass the `price filter`, the following must be true for `price`/`stopPrice` of the enabled rules:

* sell order `price` >= `minPrice`
* buy order `price` <= `maxPrice`
* (`price`-`minPrice`) % `tickSize` == 0

### LOT\_SIZE[​](/docs/derivatives/options-trading/common-definition#lot_size "Direct link to LOT_SIZE")

> **/exchangeInfo format:**

```prism-code
{  
  "filterType": "LOT_SIZE",  
  "minQty": "0.0001",  
  "maxQty": "1000",  
  "stepSize": "0.0100"  
}
```

The `LOT_SIZE` filter defines the `quantity` (aka "lots" in auction terms) rules for a symbol. There are 3 parts:

* `minQty` defines the minimum `quantity` allowed.
* `maxQty` defines the maximum `quantity` allowed.
* `stepSize` defines the intervals that a `quantity` can be increased/decreased by.

In order to pass the `lot size`, the following must be true for `quantity`:

* `quantity` >= `minQty`
* `quantity` <= `maxQty`
* (`quantity`-`minQty`) % `stepSize` == 0