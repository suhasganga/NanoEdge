On this page

# UM Position ADL Quantile Estimation(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/UM-Position-ADL-Quantile-Estimation#api-description "Direct link to API Description")

Query UM Position ADL Quantile Estimation

> * Values update every 30s.
> * Values 0, 1, 2, 3, 4 shows the queue position and possibility of ADL from low to high.
> * For positions of the symbol are in One-way Mode or isolated margined in Hedge Mode, "LONG", "SHORT", and "BOTH" will be returned to show the positions' adl quantiles of different position sides.
> * If the positions of the symbol are crossed margined in Hedge Mode:
>   + "HEDGE" as a sign will be returned instead of "BOTH";
>   + A same value caculated on unrealized pnls on long and short sides' positions will be shown for "LONG" and "SHORT" when there are positions in both of long and short sides.

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/UM-Position-ADL-Quantile-Estimation#http-request "Direct link to HTTP Request")

GET `/papi/v1/um/adlQuantile`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/UM-Position-ADL-Quantile-Estimation#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/UM-Position-ADL-Quantile-Estimation#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin/trade/UM-Position-ADL-Quantile-Estimation#response-example "Direct link to Response Example")

```prism-code
[  
	{  
		"symbol": "ETHUSDT",   
		"adlQuantile":   
			{  
				// if the positions of the symbol are crossed margined in Hedge Mode, "LONG" and "SHORT" will be returned a same quantile value.  
				"LONG": 3,    
				"SHORT": 3,   
				"BOTH": 0    
			}  
	},  
 	{  
 		"symbol": "BTCUSDT",   
 		"adlQuantile":   
 			{  
 				"LONG": 0, 	 	// adl quantile for "LONG" position in hedge mode  
 				"SHORT": 0, 	// adl quantile for "SHORT" position in hedge mode  
 				"BOTH": 2		// adl quantile for position in one-way mode  
 			}  
 	}  
]
```