On this page

# Event: Risk level change

## Event Description[​](/docs/derivatives/options-trading/user-data-streams/Event-Risk-level-change#event-description "Direct link to Event Description")

* Updates whenever there is an account risk level change. The following are possibly values:
  + NORMAL
  + REDUCE\_ONLY
* Note: Risk level changes are only applicable to VIP and Market Makers user accounts. VIP and certain Market Maker accounts will be automatically placed into REDUCE\_ONLY mode if their margin balance is insufficient to meet their maintenance margin obligations. Once in REDUCE\_ONLY mode, the system will re-evaluate the risk level only upon the following events:
  + Funds transfer
  + Trade fill
  + Option expiry

## URL PATH[​](/docs/derivatives/options-trading/user-data-streams/Event-Risk-level-change#url-path "Direct link to URL PATH")

`/private`

## Event Name[​](/docs/derivatives/options-trading/user-data-streams/Event-Risk-level-change#event-name "Direct link to Event Name")

`RISK_LEVEL_CHANGE`

## Update Speed[​](/docs/derivatives/options-trading/user-data-streams/Event-Risk-level-change#update-speed "Direct link to Update Speed")

**50ms**

## Response Example[​](/docs/derivatives/options-trading/user-data-streams/Event-Risk-level-change#response-example "Direct link to Response Example")

```prism-code
{   
    "e":"RISK_LEVEL_CHANGE", //Event Type   
    "E":1587727187525, //Event Time   
    "s":"REDUCE_ONLY", //risk level  
    "mb":"1534.11708371", //margin balance   
    "mm":"254789.11708371" //maintenance margin   
}
```