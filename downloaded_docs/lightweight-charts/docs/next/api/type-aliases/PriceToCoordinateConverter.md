Version: Next

On this page

> **PriceToCoordinateConverter**: (`price`) => [`Coordinate`](/lightweight-charts/docs/next/api/type-aliases/Coordinate) | `null`

Converter function for changing prices into vertical coordinate values.

This is provided as a convenience function since the series original data will most likely be defined
in price values, and the renderer needs to draw with coordinates. This returns the same values as
directly using the series' priceToCoordinate method.

## Parameters[​](#parameters "Direct link to Parameters")

• **price**: `number`

## Returns[​](#returns "Direct link to Returns")

[`Coordinate`](/lightweight-charts/docs/next/api/type-aliases/Coordinate) | `null`