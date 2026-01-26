Version: Next

On this page

Helper drawing utilities exposed by the library to a Primitive (a.k.a plugin).

## Properties[​](#properties "Direct link to Properties")

### setLineStyle()[​](#setlinestyle "Direct link to setLineStyle()")

> `readonly` **setLineStyle**: (`ctx`, `lineStyle`) => `void`

Drawing utility to change the line style on the canvas context to one of the
built-in line styles.

#### Parameters[​](#parameters "Direct link to Parameters")

• **ctx**: `CanvasRenderingContext2D`

2D rendering context for the target canvas.

• **lineStyle**: [`LineStyle`](/lightweight-charts/docs/next/api/enumerations/LineStyle)

Built-in [LineStyle](/lightweight-charts/docs/next/api/enumerations/LineStyle) to set on the canvas context.

#### Returns[​](#returns "Direct link to Returns")

`void`