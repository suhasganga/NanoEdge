Version: 4.1

On this page

This interface represents the primitive for one of the pane of the chart (main chart area, time scale, price scale).

## Methods[​](#methods "Direct link to Methods")

### zOrder()?[​](#zorder "Direct link to zOrder()?")

> `optional` **zOrder**(): [`SeriesPrimitivePaneViewZOrder`](/lightweight-charts/docs/4.1/api/type-aliases/SeriesPrimitivePaneViewZOrder)

Defines where in the visual layer stack the renderer should be executed. Default is `'normal'`.

#### Returns[​](#returns "Direct link to Returns")

[`SeriesPrimitivePaneViewZOrder`](/lightweight-charts/docs/4.1/api/type-aliases/SeriesPrimitivePaneViewZOrder)

the desired position in the visual layer stack.

#### See[​](#see "Direct link to See")

[SeriesPrimitivePaneViewZOrder](/lightweight-charts/docs/4.1/api/type-aliases/SeriesPrimitivePaneViewZOrder)

---

### renderer()[​](#renderer "Direct link to renderer()")

> **renderer**(): [`ISeriesPrimitivePaneRenderer`](/lightweight-charts/docs/4.1/api/interfaces/ISeriesPrimitivePaneRenderer)

This method returns a renderer - special object to draw data

#### Returns[​](#returns-1 "Direct link to Returns")

[`ISeriesPrimitivePaneRenderer`](/lightweight-charts/docs/4.1/api/interfaces/ISeriesPrimitivePaneRenderer)

an renderer object to be used for drawing, or `null` if we have nothing to draw.