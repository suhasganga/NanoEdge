Version: Next

On this page

Object containing references to the chart instance, and a requestUpdate method for triggering
a refresh of the chart.

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](/lightweight-charts/docs/next/api/type-aliases/Time)

## Properties[​](#properties "Direct link to Properties")

### chart[​](#chart "Direct link to chart")

> **chart**: [`IChartApiBase`](/lightweight-charts/docs/next/api/interfaces/IChartApiBase)<`HorzScaleItem`>

Chart instance.

---

### requestUpdate()[​](#requestupdate "Direct link to requestUpdate()")

> **requestUpdate**: () => `void`

Request an update (redraw the chart)

#### Returns[​](#returns "Direct link to Returns")

`void`