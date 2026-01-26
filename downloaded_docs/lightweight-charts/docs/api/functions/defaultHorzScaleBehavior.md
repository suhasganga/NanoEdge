Version: 5.1

On this page

> **defaultHorzScaleBehavior**(): () => [`IHorzScaleBehavior`](/lightweight-charts/docs/api/interfaces/IHorzScaleBehavior) <[`Time`](/lightweight-charts/docs/api/type-aliases/Time)>

Provides the default implementation of the horizontal scale (time-based) that can be used as a base for extending the horizontal scale with custom behavior.
This allows for the introduction of custom functionality without re-implementing the entire [IHorzScaleBehavior](/lightweight-charts/docs/api/interfaces/IHorzScaleBehavior)<[Time](/lightweight-charts/docs/api/type-aliases/Time)> interface.

For further details, refer to the [createChartEx](/lightweight-charts/docs/api/functions/createChartEx) chart constructor method.

## Returns[​](#returns "Direct link to Returns")

`Function`

An uninitialized class implementing the [IHorzScaleBehavior](/lightweight-charts/docs/api/interfaces/IHorzScaleBehavior)<[Time](/lightweight-charts/docs/api/type-aliases/Time)> interface

### Returns[​](#returns-1 "Direct link to Returns")

[`IHorzScaleBehavior`](/lightweight-charts/docs/api/interfaces/IHorzScaleBehavior) <[`Time`](/lightweight-charts/docs/api/type-aliases/Time)>