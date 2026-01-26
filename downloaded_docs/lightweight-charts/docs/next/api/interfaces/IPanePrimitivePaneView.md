Version: Next

On this page

This interface represents the primitive for one of the pane of the chart (main chart area, time scale, price scale).

## Methods[​](#methods "Direct link to Methods")

### zOrder()?[​](#zorder "Direct link to zOrder()?")

> `optional` **zOrder**(): [`PrimitivePaneViewZOrder`](/lightweight-charts/docs/next/api/type-aliases/PrimitivePaneViewZOrder)

Defines where in the visual layer stack the renderer should be executed. Default is `'normal'`.

#### Returns[​](#returns "Direct link to Returns")

[`PrimitivePaneViewZOrder`](/lightweight-charts/docs/next/api/type-aliases/PrimitivePaneViewZOrder)

the desired position in the visual layer stack.

#### See[​](#see "Direct link to See")

[PrimitivePaneViewZOrder](/lightweight-charts/docs/next/api/type-aliases/PrimitivePaneViewZOrder)

---

### renderer()[​](#renderer "Direct link to renderer()")

> **renderer**(): [`IPrimitivePaneRenderer`](/lightweight-charts/docs/next/api/interfaces/IPrimitivePaneRenderer)

This method returns a renderer - special object to draw data

#### Returns[​](#returns-1 "Direct link to Returns")

[`IPrimitivePaneRenderer`](/lightweight-charts/docs/next/api/interfaces/IPrimitivePaneRenderer)

an renderer object to be used for drawing, or `null` if we have nothing to draw.