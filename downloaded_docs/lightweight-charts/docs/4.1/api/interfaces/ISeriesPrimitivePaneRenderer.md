Version: 4.1

On this page

This interface represents rendering some element on the canvas

## Methods[​](#methods "Direct link to Methods")

### draw()[​](#draw "Direct link to draw()")

> **draw**(`target`): `void`

Method to draw main content of the element

#### Parameters[​](#parameters "Direct link to Parameters")

• **target**: `CanvasRenderingTarget2D`

canvas context to draw on, refer to FancyCanvas library for more details about this class

#### Returns[​](#returns "Direct link to Returns")

`void`

---

### drawBackground()?[​](#drawbackground "Direct link to drawBackground()?")

> `optional` **drawBackground**(`target`): `void`

Optional method to draw the background.
Some elements could implement this method to draw on the background of the chart.
Usually this is some kind of watermarks or time areas highlighting.

#### Parameters[​](#parameters-1 "Direct link to Parameters")

• **target**: `CanvasRenderingTarget2D`

canvas context to draw on, refer FancyCanvas library for more details about this class

#### Returns[​](#returns-1 "Direct link to Returns")

`void`