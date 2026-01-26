Version: 5.0

On this page

Base interface for series primitives. It must be implemented to add some external graphics to series

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **TSeriesAttachedParameters** = `unknown`

## Methods[​](#methods "Direct link to Methods")

### updateAllViews()?[​](#updateallviews "Direct link to updateAllViews()?")

> `optional` **updateAllViews**(): `void`

This method is called when viewport has been changed, so primitive have to recalculate / invalidate its data

#### Returns[​](#returns "Direct link to Returns")

`void`

---

### priceAxisViews()?[​](#priceaxisviews "Direct link to priceAxisViews()?")

> `optional` **priceAxisViews**(): readonly [`ISeriesPrimitiveAxisView`](/lightweight-charts/docs/5.0/api/interfaces/ISeriesPrimitiveAxisView)[]

Returns array of labels to be drawn on the price axis used by the series

#### Returns[​](#returns-1 "Direct link to Returns")

readonly [`ISeriesPrimitiveAxisView`](/lightweight-charts/docs/5.0/api/interfaces/ISeriesPrimitiveAxisView)[]

array of objects; each of then must implement ISeriesPrimitiveAxisView interface

For performance reasons, the lightweight library uses internal caches based on references to arrays
So, this method must return new array if set of views has changed and should try to return the same array if nothing changed

---

### timeAxisViews()?[​](#timeaxisviews "Direct link to timeAxisViews()?")

> `optional` **timeAxisViews**(): readonly [`ISeriesPrimitiveAxisView`](/lightweight-charts/docs/5.0/api/interfaces/ISeriesPrimitiveAxisView)[]

Returns array of labels to be drawn on the time axis

#### Returns[​](#returns-2 "Direct link to Returns")

readonly [`ISeriesPrimitiveAxisView`](/lightweight-charts/docs/5.0/api/interfaces/ISeriesPrimitiveAxisView)[]

array of objects; each of then must implement ISeriesPrimitiveAxisView interface

For performance reasons, the lightweight library uses internal caches based on references to arrays
So, this method must return new array if set of views has changed and should try to return the same array if nothing changed

---

### paneViews()?[​](#paneviews "Direct link to paneViews()?")

> `optional` **paneViews**(): readonly [`IPrimitivePaneView`](/lightweight-charts/docs/5.0/api/interfaces/IPrimitivePaneView)[]

Returns array of objects representing primitive in the main area of the chart

#### Returns[​](#returns-3 "Direct link to Returns")

readonly [`IPrimitivePaneView`](/lightweight-charts/docs/5.0/api/interfaces/IPrimitivePaneView)[]

array of objects; each of then must implement ISeriesPrimitivePaneView interface

For performance reasons, the lightweight library uses internal caches based on references to arrays
So, this method must return new array if set of views has changed and should try to return the same array if nothing changed

---

### priceAxisPaneViews()?[​](#priceaxispaneviews "Direct link to priceAxisPaneViews()?")

> `optional` **priceAxisPaneViews**(): readonly [`IPrimitivePaneView`](/lightweight-charts/docs/5.0/api/interfaces/IPrimitivePaneView)[]

Returns array of objects representing primitive in the price axis area of the chart

#### Returns[​](#returns-4 "Direct link to Returns")

readonly [`IPrimitivePaneView`](/lightweight-charts/docs/5.0/api/interfaces/IPrimitivePaneView)[]

array of objects; each of then must implement ISeriesPrimitivePaneView interface

For performance reasons, the lightweight library uses internal caches based on references to arrays
So, this method must return new array if set of views has changed and should try to return the same array if nothing changed

---

### timeAxisPaneViews()?[​](#timeaxispaneviews "Direct link to timeAxisPaneViews()?")

> `optional` **timeAxisPaneViews**(): readonly [`IPrimitivePaneView`](/lightweight-charts/docs/5.0/api/interfaces/IPrimitivePaneView)[]

Returns array of objects representing primitive in the time axis area of the chart

#### Returns[​](#returns-5 "Direct link to Returns")

readonly [`IPrimitivePaneView`](/lightweight-charts/docs/5.0/api/interfaces/IPrimitivePaneView)[]

array of objects; each of then must implement ISeriesPrimitivePaneView interface

For performance reasons, the lightweight library uses internal caches based on references to arrays
So, this method must return new array if set of views has changed and should try to return the same array if nothing changed

---

### autoscaleInfo()?[​](#autoscaleinfo "Direct link to autoscaleInfo()?")

> `optional` **autoscaleInfo**(`startTimePoint`, `endTimePoint`): [`AutoscaleInfo`](/lightweight-charts/docs/5.0/api/interfaces/AutoscaleInfo)

Return autoscaleInfo which will be merged with the series base autoscaleInfo. You can use this to expand the autoscale range
to include visual elements drawn outside of the series' current visible price range.

**Important**: Please note that this method will be evoked very often during scrolling and zooming of the chart, thus it
is recommended that this method is either simple to execute, or makes use of optimisations such as caching to ensure that
the chart remains responsive.

#### Parameters[​](#parameters "Direct link to Parameters")

• **startTimePoint**: [`Logical`](/lightweight-charts/docs/5.0/api/type-aliases/Logical)

start time point for the current visible range

• **endTimePoint**: [`Logical`](/lightweight-charts/docs/5.0/api/type-aliases/Logical)

end time point for the current visible range

#### Returns[​](#returns-6 "Direct link to Returns")

[`AutoscaleInfo`](/lightweight-charts/docs/5.0/api/interfaces/AutoscaleInfo)

AutoscaleInfo

---

### attached()?[​](#attached "Direct link to attached()?")

> `optional` **attached**(`param`): `void`

Attached Lifecycle hook.

#### Parameters[​](#parameters-1 "Direct link to Parameters")

• **param**: `TSeriesAttachedParameters`

An object containing useful references for the attached primitive to use.

#### Returns[​](#returns-7 "Direct link to Returns")

`void`

void

---

### detached()?[​](#detached "Direct link to detached()?")

> `optional` **detached**(): `void`

Detached Lifecycle hook.

#### Returns[​](#returns-8 "Direct link to Returns")

`void`

void

---

### hitTest()?[​](#hittest "Direct link to hitTest()?")

> `optional` **hitTest**(`x`, `y`): [`PrimitiveHoveredItem`](/lightweight-charts/docs/5.0/api/interfaces/PrimitiveHoveredItem)

Hit test method which will be called by the library when the cursor is moved.
Use this to register object ids being hovered for use within the crosshairMoved
and click events emitted by the chart. Additionally, the hit test result can
specify a preferred cursor type to display for the main chart pane. This method
should return the top most hit for this primitive if more than one object is
being intersected.

#### Parameters[​](#parameters-2 "Direct link to Parameters")

• **x**: `number`

x Coordinate of mouse event

• **y**: `number`

y Coordinate of mouse event

#### Returns[​](#returns-9 "Direct link to Returns")

[`PrimitiveHoveredItem`](/lightweight-charts/docs/5.0/api/interfaces/PrimitiveHoveredItem)