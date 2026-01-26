On this page

# Error Codes

> Here is the error JSON payload:

```prism-code
{  
  "code":-1121,  
  "msg":"Invalid symbol."  
}
```

Errors consist of two parts: an error code and a message.  
Codes are universal,but messages can vary.

## 10xx - General Server or Network issues[​](/docs/derivatives/options-trading/error-code#10xx---general-server-or-network-issues "Direct link to 10xx - General Server or Network issues")

### -1000 UNKNOWN[​](/docs/derivatives/options-trading/error-code#-1000-unknown "Direct link to -1000 UNKNOWN")

* An unknown error occurred while processing the request.

### -1001 DISCONNECTED[​](/docs/derivatives/options-trading/error-code#-1001-disconnected "Direct link to -1001 DISCONNECTED")

* Internal error; unable to process your request. Please try again.

### -1002 UNAUTHORIZED[​](/docs/derivatives/options-trading/error-code#-1002-unauthorized "Direct link to -1002 UNAUTHORIZED")

* You are not authorized to execute this request.

### -1008 TOO\_MANY\_REQUESTS[​](/docs/derivatives/options-trading/error-code#-1008-too_many_requests "Direct link to -1008 TOO_MANY_REQUESTS")

* Too many requests queued.
* Too much request weight used; please use the websocket for live updates to avoid polling the API.
* Too much request weight used; current limit is %s request weight per %s %s. Please use the websocket for live updates to avoid polling the API.
* Way too much request weight used; IP banned until %s. Please use the websocket for live updates to avoid bans.

### -1014 UNKNOWN\_ORDER\_COMPOSITION[​](/docs/derivatives/options-trading/error-code#-1014-unknown_order_composition "Direct link to -1014 UNKNOWN_ORDER_COMPOSITION")

* Unsupported order combination.

### -1015 TOO\_MANY\_ORDERS[​](/docs/derivatives/options-trading/error-code#-1015-too_many_orders "Direct link to -1015 TOO_MANY_ORDERS")

* Too many new orders.
* Too many new orders; current limit is %s orders per %s.

### -1016 SERVICE\_SHUTTING\_DOWN[​](/docs/derivatives/options-trading/error-code#-1016-service_shutting_down "Direct link to -1016 SERVICE_SHUTTING_DOWN")

* This service is no longer available.

### -1020 UNSUPPORTED\_OPERATION[​](/docs/derivatives/options-trading/error-code#-1020-unsupported_operation "Direct link to -1020 UNSUPPORTED_OPERATION")

* This operation is not supported.

### -1021 INVALID\_TIMESTAMP[​](/docs/derivatives/options-trading/error-code#-1021-invalid_timestamp "Direct link to -1021 INVALID_TIMESTAMP")

* Timestamp for this request is outside of the recvWindow.
* Timestamp for this request was 1000ms ahead of the server's time.

### -1022 INVALID\_SIGNATURE[​](/docs/derivatives/options-trading/error-code#-1022-invalid_signature "Direct link to -1022 INVALID_SIGNATURE")

* Signature for this request is not valid.

## 11xx - 2xxx Request issues[​](/docs/derivatives/options-trading/error-code#11xx---2xxx-request-issues "Direct link to 11xx - 2xxx Request issues")

### -1100 ILLEGAL\_CHARS[​](/docs/derivatives/options-trading/error-code#-1100-illegal_chars "Direct link to -1100 ILLEGAL_CHARS")

* Illegal characters found in a parameter.
* Illegal characters found in a parameter. %s
* Illegal characters found in parameter `%s`; legal range is `%s`.

### -1101 TOO\_MANY\_PARAMETERS[​](/docs/derivatives/options-trading/error-code#-1101-too_many_parameters "Direct link to -1101 TOO_MANY_PARAMETERS")

* Too many parameters sent for this endpoint.
* Too many parameters; expected `%s` and received `%s`.
* Duplicate values for a parameter detected.

### -1102 MANDATORY\_PARAM\_EMPTY\_OR\_MALFORMED[​](/docs/derivatives/options-trading/error-code#-1102-mandatory_param_empty_or_malformed "Direct link to -1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED")

* A mandatory parameter was not sent, was empty/null, or malformed.
* Mandatory parameter `%s` was not sent, was empty/null, or malformed.
* Param `%s` or `%s` must be sent, but both were empty/null!

### -1103 UNKNOWN\_PARAM[​](/docs/derivatives/options-trading/error-code#-1103-unknown_param "Direct link to -1103 UNKNOWN_PARAM")

* An unknown parameter was sent.

### -1104 UNREAD\_PARAMETERS[​](/docs/derivatives/options-trading/error-code#-1104-unread_parameters "Direct link to -1104 UNREAD_PARAMETERS")

* Not all sent parameters were read.
* Not all sent parameters were read; read `%s` parameter(s) but was sent `%s`.

### -1105 PARAM\_EMPTY[​](/docs/derivatives/options-trading/error-code#-1105-param_empty "Direct link to -1105 PARAM_EMPTY")

* A parameter was empty.
* Parameter `%s` was empty.

### -1106 PARAM\_NOT\_REQUIRED[​](/docs/derivatives/options-trading/error-code#-1106-param_not_required "Direct link to -1106 PARAM_NOT_REQUIRED")

* A parameter was sent when not required.
* Parameter `%s` sent when not required.

### -1111 BAD\_PRECISION[​](/docs/derivatives/options-trading/error-code#-1111-bad_precision "Direct link to -1111 BAD_PRECISION")

* Precision is over the maximum defined for this asset.

### -1115 INVALID\_TIF[​](/docs/derivatives/options-trading/error-code#-1115-invalid_tif "Direct link to -1115 INVALID_TIF")

* Invalid timeInForce.

### -1116 INVALID\_ORDER\_TYPE[​](/docs/derivatives/options-trading/error-code#-1116-invalid_order_type "Direct link to -1116 INVALID_ORDER_TYPE")

* Invalid orderType.

### -1117 INVALID\_SIDE[​](/docs/derivatives/options-trading/error-code#-1117-invalid_side "Direct link to -1117 INVALID_SIDE")

* Invalid side.

### -1118 EMPTY\_NEW\_CL\_ORD\_ID[​](/docs/derivatives/options-trading/error-code#-1118-empty_new_cl_ord_id "Direct link to -1118 EMPTY_NEW_CL_ORD_ID")

* New client order ID was empty.

### -1119 EMPTY\_ORG\_CL\_ORD\_ID[​](/docs/derivatives/options-trading/error-code#-1119-empty_org_cl_ord_id "Direct link to -1119 EMPTY_ORG_CL_ORD_ID")

* Original client order ID was empty.

### -1120 BAD\_INTERVAL[​](/docs/derivatives/options-trading/error-code#-1120-bad_interval "Direct link to -1120 BAD_INTERVAL")

* Invalid interval.

### -1121 BAD\_SYMBOL[​](/docs/derivatives/options-trading/error-code#-1121-bad_symbol "Direct link to -1121 BAD_SYMBOL")

* Invalid symbol.

### -1125 INVALID\_LISTEN\_KEY[​](/docs/derivatives/options-trading/error-code#-1125-invalid_listen_key "Direct link to -1125 INVALID_LISTEN_KEY")

* This listenKey does not exist.

### -1127 MORE\_THAN\_XX\_HOURS[​](/docs/derivatives/options-trading/error-code#-1127-more_than_xx_hours "Direct link to -1127 MORE_THAN_XX_HOURS")

* Lookup interval is too big.
* More than %s hours between startTime and endTime.

### -1128 BAD\_CONTRACT[​](/docs/derivatives/options-trading/error-code#-1128-bad_contract "Direct link to -1128 BAD_CONTRACT")

* Invalid underlying

### -1129 BAD\_CURRENCY[​](/docs/derivatives/options-trading/error-code#-1129-bad_currency "Direct link to -1129 BAD_CURRENCY")

* Invalid asset。

### -1130 INVALID\_PARAMETER[​](/docs/derivatives/options-trading/error-code#-1130-invalid_parameter "Direct link to -1130 INVALID_PARAMETER")

* Invalid data sent for a parameter.
* Data sent for paramter `%s` is not valid.

### -1131 BAD\_RECV\_WINDOW[​](/docs/derivatives/options-trading/error-code#-1131-bad_recv_window "Direct link to -1131 BAD_RECV_WINDOW")

* recvWindow must be less than 60000

### -2010 NEW\_ORDER\_REJECTED[​](/docs/derivatives/options-trading/error-code#-2010-new_order_rejected "Direct link to -2010 NEW_ORDER_REJECTED")

* NEW\_ORDER\_REJECTED

### -2013 NO\_SUCH\_ORDER[​](/docs/derivatives/options-trading/error-code#-2013-no_such_order "Direct link to -2013 NO_SUCH_ORDER")

* Order does not exist.

### -2014 BAD\_API\_KEY\_FMT[​](/docs/derivatives/options-trading/error-code#-2014-bad_api_key_fmt "Direct link to -2014 BAD_API_KEY_FMT")

* API-key format invalid.

### -2015 INVALID\_API\_KEY[​](/docs/derivatives/options-trading/error-code#-2015-invalid_api_key "Direct link to -2015 INVALID_API_KEY")

* Invalid API-key, IP, or permissions for action.

### -2018 BALANCE\_NOT\_SUFFICIENT[​](/docs/derivatives/options-trading/error-code#-2018-balance_not_sufficient "Direct link to -2018 BALANCE_NOT_SUFFICIENT")

* Balance is insufficient.

### -2027 OPTION\_MARGIN\_NOT\_SUFFICIENT[​](/docs/derivatives/options-trading/error-code#-2027-option_margin_not_sufficient "Direct link to -2027 OPTION_MARGIN_NOT_SUFFICIENT")

* Option margin is insufficient.

## 3xxx-5xxx Filters and other issues[​](/docs/derivatives/options-trading/error-code#3xxx-5xxx-filters-and-other-issues "Direct link to 3xxx-5xxx Filters and other issues")

### -3029 TRANSFER\_FAILED[​](/docs/derivatives/options-trading/error-code#-3029-transfer_failed "Direct link to -3029 TRANSFER_FAILED")

* Asset transfer fail.

### -4001 PRICE\_LESS\_THAN\_ZERO[​](/docs/derivatives/options-trading/error-code#-4001-price_less_than_zero "Direct link to -4001 PRICE_LESS_THAN_ZERO")

* Price less than 0.

### -4002 PRICE\_GREATER\_THAN\_MAX\_PRICE[​](/docs/derivatives/options-trading/error-code#-4002-price_greater_than_max_price "Direct link to -4002 PRICE_GREATER_THAN_MAX_PRICE")

* Price greater than max price.

### -4003 QTY\_LESS\_THAN\_ZERO[​](/docs/derivatives/options-trading/error-code#-4003-qty_less_than_zero "Direct link to -4003 QTY_LESS_THAN_ZERO")

* Quantity less than zero.

### -4004 QTY\_LESS\_THAN\_MIN\_QTY[​](/docs/derivatives/options-trading/error-code#-4004-qty_less_than_min_qty "Direct link to -4004 QTY_LESS_THAN_MIN_QTY")

* Quantity less than min quantity.

### -4005 QTY\_GREATER\_THAN\_MAX\_QTY[​](/docs/derivatives/options-trading/error-code#-4005-qty_greater_than_max_qty "Direct link to -4005 QTY_GREATER_THAN_MAX_QTY")

* Quantity greater than max quantity.

### -4013 PRICE\_LESS\_THAN\_MIN\_PRICE[​](/docs/derivatives/options-trading/error-code#-4013-price_less_than_min_price "Direct link to -4013 PRICE_LESS_THAN_MIN_PRICE")

* Price less than min price.

### -4029 INVALID\_TICK\_SIZE\_PRECISION[​](/docs/derivatives/options-trading/error-code#-4029-invalid_tick_size_precision "Direct link to -4029 INVALID_TICK_SIZE_PRECISION")

* Tick size precision is invalid.

### -4030 INVALID\_QTY\_PRECISION[​](/docs/derivatives/options-trading/error-code#-4030-invalid_qty_precision "Direct link to -4030 INVALID_QTY_PRECISION")

* Step size precision is invalid.

### -4055 AMOUNT\_MUST\_BE\_POSITIVE[​](/docs/derivatives/options-trading/error-code#-4055-amount_must_be_positive "Direct link to -4055 AMOUNT_MUST_BE_POSITIVE")

* Amount must be positive.

### -4056 INVALID\_AMOUNT[​](/docs/derivatives/options-trading/error-code#-4056-invalid_amount "Direct link to -4056 INVALID_AMOUNT")

* Amount is invalid.

### -4078 OPTIONS\_COMMON\_ERROR[​](/docs/derivatives/options-trading/error-code#-4078-options_common_error "Direct link to -4078 OPTIONS_COMMON_ERROR")

* options internal error

### -5001 USER\_EXIST[​](/docs/derivatives/options-trading/error-code#-5001-user_exist "Direct link to -5001 USER_EXIST")

* Option user already exist

### -5002 USER\_NOT\_ACCESS[​](/docs/derivatives/options-trading/error-code#-5002-user_not_access "Direct link to -5002 USER_NOT_ACCESS")

* Option user not access

### -5003 BAD\_INVITE\_CODE[​](/docs/derivatives/options-trading/error-code#-5003-bad_invite_code "Direct link to -5003 BAD_INVITE_CODE")

* Invalid invite code

### -5004 USED\_INVITE\_CODE[​](/docs/derivatives/options-trading/error-code#-5004-used_invite_code "Direct link to -5004 USED_INVITE_CODE")

* Invite code has bean used

### -5005 BLACK\_COUNTRY[​](/docs/derivatives/options-trading/error-code#-5005-black_country "Direct link to -5005 BLACK_COUNTRY")

* Black country

### -5006 ITEMS\_EXIST[​](/docs/derivatives/options-trading/error-code#-5006-items_exist "Direct link to -5006 ITEMS_EXIST")

* Items '%s' already exist

### -5007 USER\_API\_EXIST[​](/docs/derivatives/options-trading/error-code#-5007-user_api_exist "Direct link to -5007 USER_API_EXIST")

* User api already exist

### -5008 KYC\_NOT\_PASS[​](/docs/derivatives/options-trading/error-code#-5008-kyc_not_pass "Direct link to -5008 KYC_NOT_PASS")

* User kyc not pass

### -5009 IP\_COUNTRY\_BLACK[​](/docs/derivatives/options-trading/error-code#-5009-ip_country_black "Direct link to -5009 IP_COUNTRY_BLACK")

* Restricted jurisdiction ip address

### -5010 NOT\_ENOUGH\_POSITION[​](/docs/derivatives/options-trading/error-code#-5010-not_enough_position "Direct link to -5010 NOT_ENOUGH_POSITION")

* User doesn't have enough position to sell

### -6001 INVALID\_MMP\_WINDOW\_TIME\_LIMIT[​](/docs/derivatives/options-trading/error-code#-6001-invalid_mmp_window_time_limit "Direct link to -6001 INVALID_MMP_WINDOW_TIME_LIMIT")

* Invalid mmp window time limit

### -6002 INVALID\_MMP\_FROZEN\_TIME\_LIMIT[​](/docs/derivatives/options-trading/error-code#-6002-invalid_mmp_frozen_time_limit "Direct link to -6002 INVALID_MMP_FROZEN_TIME_LIMIT")

* Invalid mmp frozen time limit

### -6003 INVALID\_UNDERLYING[​](/docs/derivatives/options-trading/error-code#-6003-invalid_underlying "Direct link to -6003 INVALID_UNDERLYING")

* Invalid underlying

### -6004 MMP\_UNDERLYING\_NOT\_FOUND[​](/docs/derivatives/options-trading/error-code#-6004-mmp_underlying_not_found "Direct link to -6004 MMP_UNDERLYING_NOT_FOUND")

* Underlying not found

### -6005 IS\_NOT\_MARKET\_MAKER[​](/docs/derivatives/options-trading/error-code#-6005-is_not_market_maker "Direct link to -6005 IS_NOT_MARKET_MAKER")

* It is not market maker

### -6006 MMP\_RULES\_NOT\_EXISTING[​](/docs/derivatives/options-trading/error-code#-6006-mmp_rules_not_existing "Direct link to -6006 MMP_RULES_NOT_EXISTING")

* Mmp rules are not existing

### -6007 MMP\_ERROR\_UNKNOWN[​](/docs/derivatives/options-trading/error-code#-6007-mmp_error_unknown "Direct link to -6007 MMP_ERROR_UNKNOWN")

* Mmp unknown error

### -6008 INVALID\_LIMIT[​](/docs/derivatives/options-trading/error-code#-6008-invalid_limit "Direct link to -6008 INVALID_LIMIT")

* parameter 'limit' is invalid.

### -6009 INVALID\_COUNTDOWN\_TIME[​](/docs/derivatives/options-trading/error-code#-6009-invalid_countdown_time "Direct link to -6009 INVALID_COUNTDOWN_TIME")

* countdownTime must be no less than 5000 or equal to 0

### -6010 OPEN\_INTEREST\_ERR\_DATA[​](/docs/derivatives/options-trading/error-code#-6010-open_interest_err_data "Direct link to -6010 OPEN_INTEREST_ERR_DATA")

* open interest error data.

### -6011 EXCEED\_MAXIMUM\_BATCH\_ORDERS[​](/docs/derivatives/options-trading/error-code#-6011-exceed_maximum_batch_orders "Direct link to -6011 EXCEED_MAXIMUM_BATCH_ORDERS")

* Maximum 10 orders in one batchOrder request.

### -6012 EXCEED\_MAXIMUM\_BLOCK\_ORDER\_LEGS[​](/docs/derivatives/options-trading/error-code#-6012-exceed_maximum_block_order_legs "Direct link to -6012 EXCEED_MAXIMUM_BLOCK_ORDER_LEGS")

* Exceed maximum number of legs in one block order request.

### -6013 BLOCK\_ORDER\_LEGS\_WITH\_DUPLICATE\_SYMBOL[​](/docs/derivatives/options-trading/error-code#-6013-block_order_legs_with_duplicate_symbol "Direct link to -6013 BLOCK_ORDER_LEGS_WITH_DUPLICATE_SYMBOL")

* Duplicate symbol in one block order request.

### -6014 GRFQ\_INVALID\_LEGS[​](/docs/derivatives/options-trading/error-code#-6014-grfq_invalid_legs "Direct link to -6014 GRFQ_INVALID_LEGS")

* Invalid legs

### -6015 GRFQ\_QTY\_IS\_NOT\_MULTIPLE\_OF\_MINIMUM\_QTY[​](/docs/derivatives/options-trading/error-code#-6015-grfq_qty_is_not_multiple_of_minimum_qty "Direct link to -6015 GRFQ_QTY_IS_NOT_MULTIPLE_OF_MINIMUM_QTY")

* Quantity is not multiple of minimum quantity

### -6016 GRFQ\_QUOTE\_NOT\_FOUND[​](/docs/derivatives/options-trading/error-code#-6016-grfq_quote_not_found "Direct link to -6016 GRFQ_QUOTE_NOT_FOUND")

* Quote is not found

### -6017 GRFQ\_QUOTE\_NOT\_ENOUGH\_QTY\_LEFT[​](/docs/derivatives/options-trading/error-code#-6017-grfq_quote_not_enough_qty_left "Direct link to -6017 GRFQ_QUOTE_NOT_ENOUGH_QTY_LEFT")

* Not enough quantity left

### -6018 GRFQ\_QUOTE\_REQUEST\_NOT\_FOUND[​](/docs/derivatives/options-trading/error-code#-6018-grfq_quote_request_not_found "Direct link to -6018 GRFQ_QUOTE_REQUEST_NOT_FOUND")

* Quote request is not found

### -6019 GRFQ\_QUOTE\_INVALID\_EXPIRE\_TIME[​](/docs/derivatives/options-trading/error-code#-6019-grfq_quote_invalid_expire_time "Direct link to -6019 GRFQ_QUOTE_INVALID_EXPIRE_TIME")

* Invalid quote expire time

### -6020 GRFQ\_QUOTE\_EXPIRED[​](/docs/derivatives/options-trading/error-code#-6020-grfq_quote_expired "Direct link to -6020 GRFQ_QUOTE_EXPIRED")

* Quote expired

### -6021 GRFQ\_INVALID\_SIDE[​](/docs/derivatives/options-trading/error-code#-6021-grfq_invalid_side "Direct link to -6021 GRFQ_INVALID_SIDE")

* Invalid side

### -6022 GRFQ\_INVALID\_USER[​](/docs/derivatives/options-trading/error-code#-6022-grfq_invalid_user "Direct link to -6022 GRFQ_INVALID_USER")

* Not Global RFQ user

### -6023 SELF\_TRADE\_PREVENTION[​](/docs/derivatives/options-trading/error-code#-6023-self_trade_prevention "Direct link to -6023 SELF_TRADE_PREVENTION")

* Self trade prevention

### -6024 CHANGE\_USER\_FLAG\_FAILED[​](/docs/derivatives/options-trading/error-code#-6024-change_user_flag_failed "Direct link to -6024 CHANGE_USER_FLAG_FAILED")

* Change user flag failed

### -6025 GRFQ\_INVALID\_QUOTE\_PRICE[​](/docs/derivatives/options-trading/error-code#-6025-grfq_invalid_quote_price "Direct link to -6025 GRFQ_INVALID_QUOTE_PRICE")

* Invalid quote price

### -6026 INVALID\_QTY[​](/docs/derivatives/options-trading/error-code#-6026-invalid_qty "Direct link to -6026 INVALID_QTY")

* Invalid qty

### -6027 INVALID\_PRICE[​](/docs/derivatives/options-trading/error-code#-6027-invalid_price "Direct link to -6027 INVALID_PRICE")

* Invalid price

### -6028 ORDER\_IS\_FINAL[​](/docs/derivatives/options-trading/error-code#-6028-order_is_final "Direct link to -6028 ORDER_IS_FINAL")

* Order is in final state

### -6029 PARAMETER\_IS\_REQUIRED[​](/docs/derivatives/options-trading/error-code#-6029-parameter_is_required "Direct link to -6029 PARAMETER_IS_REQUIRED")

* %s is required

### -6030 INVALID\_TIME\_INTERVAL[​](/docs/derivatives/options-trading/error-code#-6030-invalid_time_interval "Direct link to -6030 INVALID_TIME_INTERVAL")

* Invalid time interval.

### -6031 START\_TIME\_GREATER\_THAN\_END\_TIME[​](/docs/derivatives/options-trading/error-code#-6031-start_time_greater_than_end_time "Direct link to -6031 START_TIME_GREATER_THAN_END_TIME")

* Start time is greater than end time.

### -6032 HAS\_OPEN\_ORDER[​](/docs/derivatives/options-trading/error-code#-6032-has_open_order "Direct link to -6032 HAS_OPEN_ORDER")

* Has open order.

### -6033 HAS\_NEGATIVE\_BALANCE[​](/docs/derivatives/options-trading/error-code#-6033-has_negative_balance "Direct link to -6033 HAS_NEGATIVE_BALANCE")

* Has negative balance.

### -6034 HAS\_POSITION[​](/docs/derivatives/options-trading/error-code#-6034-has_position "Direct link to -6034 HAS_POSITION")

* Has position.

### -6035 NO\_NEED\_TO\_CHANGE[​](/docs/derivatives/options-trading/error-code#-6035-no_need_to_change "Direct link to -6035 NO_NEED_TO_CHANGE")

* No need to change.

### -6036 NO\_PERMISSION\_TO\_CHANGE[​](/docs/derivatives/options-trading/error-code#-6036-no_permission_to_change "Direct link to -6036 NO_PERMISSION_TO_CHANGE")

* no permission to change.

### -6037 NO\_RECORDS\_FOUND[​](/docs/derivatives/options-trading/error-code#-6037-no_records_found "Direct link to -6037 NO_RECORDS_FOUND")

* No records found.

### -6038 SCALE\_NOT\_MATCH[​](/docs/derivatives/options-trading/error-code#-6038-scale_not_match "Direct link to -6038 SCALE_NOT_MATCH")

* scale not match.

### -6039 INVALID\_STEP\_SIZE\_PRECISION[​](/docs/derivatives/options-trading/error-code#-6039-invalid_step_size_precision "Direct link to -6039 INVALID_STEP_SIZE_PRECISION")

* Step size precision is invalid.

### -6040 INVALID\_QTYLIMIT\_DELTALIMIT[​](/docs/derivatives/options-trading/error-code#-6040-invalid_qtylimit_deltalimit "Direct link to -6040 INVALID_QTYLIMIT_DELTALIMIT")

* Invalid qtyLimit or deltaLimit.

### -6041 START\_TRADING\_MUST\_SLOWLY[​](/docs/derivatives/options-trading/error-code#-6041-start_trading_must_slowly "Direct link to -6041 START_TRADING_MUST_SLOWLY")

* Start Trading Must Slowly..

### -6042 INDEX\_COMMISSION\_NOT\_MATCH[​](/docs/derivatives/options-trading/error-code#-6042-index_commission_not_match "Direct link to -6042 INDEX_COMMISSION_NOT_MATCH")

* Index Commission Not Match..

### -6043 INDEX\_RISKPARAMETER\_NOT\_MATCH[​](/docs/derivatives/options-trading/error-code#-6043-index_riskparameter_not_match "Direct link to -6043 INDEX_RISKPARAMETER_NOT_MATCH")

* Index RiskParameter Not Match..

### -6044 CLI\_ORD\_ID\_ERROR[​](/docs/derivatives/options-trading/error-code#-6044-cli_ord_id_error "Direct link to -6044 CLI_ORD_ID_ERROR")

* clientOrderId is duplicated

### -6045 REDUCE\_ONLY\_REJECT[​](/docs/derivatives/options-trading/error-code#-6045-reduce_only_reject "Direct link to -6045 REDUCE_ONLY_REJECT")

* Reduce-only order rejected. The new reduce-only order conflicts with existing open orders. Please cancel the conflicting orders and resubmit.

### -6046 FOK\_ORDER\_REJECT[​](/docs/derivatives/options-trading/error-code#-6046-fok_order_reject "Direct link to -6046 FOK_ORDER_REJECT")

* Due to the order could not be filled immediately, the FOK order has been rejected.

### -6047 GTX\_ORDER\_REJECT[​](/docs/derivatives/options-trading/error-code#-6047-gtx_order_reject "Direct link to -6047 GTX_ORDER_REJECT")

* Due to the order could not be executed as maker, the Post Only order will be rejected.

### -6048 INVALID\_BLOCK\_ORDER[​](/docs/derivatives/options-trading/error-code#-6048-invalid_block_order "Direct link to -6048 INVALID_BLOCK_ORDER")

* Block order parameter is invalid

### -6049 SYMBOL\_NOT\_TRADING[​](/docs/derivatives/options-trading/error-code#-6049-symbol_not_trading "Direct link to -6049 SYMBOL_NOT_TRADING")

* this symbol is not in trading status

### -6050 MAX\_OPEN\_ORDERS\_ON\_SYMBOL\_EXCEEDED[​](/docs/derivatives/options-trading/error-code#-6050-max_open_orders_on_symbol_exceeded "Direct link to -6050 MAX_OPEN_ORDERS_ON_SYMBOL_EXCEEDED")

* Maximum open orders reached for this symbol. Please cancel existing orders and try again.

### -6051 MAX\_OPEN\_ORDERS\_ON\_INDEX\_EXCEEDED[​](/docs/derivatives/options-trading/error-code#-6051-max_open_orders_on_index_exceeded "Direct link to -6051 MAX_OPEN_ORDERS_ON_INDEX_EXCEEDED")

* Maximum open orders reached for this underlying. Please cancel existing orders and try again.

### -6052 MAX\_SHORT\_POSITION\_ON\_SYMBOL\_EXCEEDED[​](/docs/derivatives/options-trading/error-code#-6052-max_short_position_on_symbol_exceeded "Direct link to -6052 MAX_SHORT_POSITION_ON_SYMBOL_EXCEEDED")

* Maximum short position size reached for this symbol

### -6053 MAX\_SHORT\_POSITION\_ON\_INDEX\_EXCEEDED[​](/docs/derivatives/options-trading/error-code#-6053-max_short_position_on_index_exceeded "Direct link to -6053 MAX_SHORT_POSITION_ON_INDEX_EXCEEDED")

* Maximum short position size reached for this underlying

### -6054 MAX\_QUANTITY\_ON\_SINGLE\_ORDER\_EXCEEDED[​](/docs/derivatives/options-trading/error-code#-6054-max_quantity_on_single_order_exceeded "Direct link to -6054 MAX_QUANTITY_ON_SINGLE_ORDER_EXCEEDED")

* Quantity greater than max quantity

### -6055 USER\_LIQUIDATING[​](/docs/derivatives/options-trading/error-code#-6055-user_liquidating "Direct link to -6055 USER_LIQUIDATING")

* User is in liquidation process

### -6056 REDUCE\_ONLY\_MARGIN\_CHECK\_FAILED[​](/docs/derivatives/options-trading/error-code#-6056-reduce_only_margin_check_failed "Direct link to -6056 REDUCE_ONLY_MARGIN_CHECK_FAILED")

* Reduce-only order failed. Your new reduce-only order, when combined with existing same-side open orders, would flip your position and cause insufficient margin. Please cancel those open orders and try again.

### -6057 WRITER\_CANT\_NAKED\_SELL[​](/docs/derivatives/options-trading/error-code#-6057-writer_cant_naked_sell "Direct link to -6057 WRITER_CANT_NAKED_SELL")

* The current symbol is not eligible for option writing.

### -6058 MMP\_TRIGGERED[​](/docs/derivatives/options-trading/error-code#-6058-mmp_triggered "Direct link to -6058 MMP_TRIGGERED")

* MMP triggered. Please reset MMP config

### -6059 USER\_IN\_LIQUIDATION[​](/docs/derivatives/options-trading/error-code#-6059-user_in_liquidation "Direct link to -6059 USER_IN_LIQUIDATION")

* User is in liquidation process

### -6060 LOCKED\_BALANCE\_NOT\_FOUND[​](/docs/derivatives/options-trading/error-code#-6060-locked_balance_not_found "Direct link to -6060 LOCKED_BALANCE_NOT_FOUND")

* OTC order fail due to unable to lock balance

### -6061 LOCKED\_OTC\_ORDER\_NOT\_FOUNT[​](/docs/derivatives/options-trading/error-code#-6061-locked_otc_order_not_fount "Direct link to -6061 LOCKED_OTC_ORDER_NOT_FOUNT")

* OTC order fail due to unable to lock order

### -6062 INVALID\_USER\_STATUS[​](/docs/derivatives/options-trading/error-code#-6062-invalid_user_status "Direct link to -6062 INVALID_USER_STATUS")

* Operation is not supported for current user status

### -6063 CANCEL\_REJECTED[​](/docs/derivatives/options-trading/error-code#-6063-cancel_rejected "Direct link to -6063 CANCEL_REJECTED")

* Cancel rejected by system