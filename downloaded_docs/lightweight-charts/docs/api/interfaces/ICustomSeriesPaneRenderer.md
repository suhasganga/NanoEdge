Version: 5.1

On this page

Renderer for the custom series. This paints on the main chart pane.

## Methods[​](#methods "Direct link to Methods")

### draw()[​](#draw "Direct link to draw()")

> **draw**(`target`, `priceConverter`, `isHovered`, `hitTestData`?): `void`

Draw function for the renderer.

#### Parameters[​](#parameters "Direct link to Parameters")

• **target**: `CanvasRenderingTarget2D`

canvas context to draw on, refer to FancyCanvas library for more details about this class.

• **priceConverter**: [`PriceToCoordinateConverter`](/lightweight-charts/docs/api/type-aliases/PriceToCoordinateConverter)

converter function for changing prices into vertical coordinate values.

• **isHovered**: `boolean`

Whether the series is hovered.

• **hitTestData?**: `unknown`

Optional hit test data for the series.

#### Returns[​](#returns "Direct link to Returns")

`void`