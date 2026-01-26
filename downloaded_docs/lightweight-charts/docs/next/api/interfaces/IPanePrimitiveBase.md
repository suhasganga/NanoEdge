Version: Next

On this page

Base interface for series primitives. It must be implemented to add some external graphics to series

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **TPaneAttachedParameters** = `unknown`

## Methods[​](#methods "Direct link to Methods")

### updateAllViews()?[​](#updateallviews "Direct link to updateAllViews()?")

> `optional` **updateAllViews**(): `void`

This method is called when viewport has been changed, so primitive have to recalculate / invalidate its data

#### Returns[​](#returns "Direct link to Returns")

`void`

---

### paneViews()?[​](#paneviews "Direct link to paneViews()?")

> `optional` **paneViews**(): readonly [`IPanePrimitivePaneView`](/lightweight-charts/docs/next/api/interfaces/IPanePrimitivePaneView)[]

Returns array of objects representing primitive in the main area of the chart

#### Returns[​](#returns-1 "Direct link to Returns")

readonly [`IPanePrimitivePaneView`](/lightweight-charts/docs/next/api/interfaces/IPanePrimitivePaneView)[]

array of objects; each of then must implement IPrimitivePaneView interface

For performance reasons, the lightweight library uses internal caches based on references to arrays
So, this method must return new array if set of views has changed and should try to return the same array if nothing changed

---

### attached()?[​](#attached "Direct link to attached()?")

> `optional` **attached**(`param`): `void`

Attached Lifecycle hook.

#### Parameters[​](#parameters "Direct link to Parameters")

• **param**: `TPaneAttachedParameters`

An object containing useful references for the attached primitive to use.

#### Returns[​](#returns-2 "Direct link to Returns")

`void`

void

---

### detached()?[​](#detached "Direct link to detached()?")

> `optional` **detached**(): `void`

Detached Lifecycle hook.

#### Returns[​](#returns-3 "Direct link to Returns")

`void`

void

---

### hitTest()?[​](#hittest "Direct link to hitTest()?")

> `optional` **hitTest**(`x`, `y`): [`PrimitiveHoveredItem`](/lightweight-charts/docs/next/api/interfaces/PrimitiveHoveredItem)

Hit test method which will be called by the library when the cursor is moved.
Use this to register object ids being hovered for use within the crosshairMoved
and click events emitted by the chart. Additionally, the hit test result can
specify a preferred cursor type to display for the main chart pane. This method
should return the top most hit for this primitive if more than one object is
being intersected.

#### Parameters[​](#parameters-1 "Direct link to Parameters")

• **x**: `number`

x Coordinate of mouse event

• **y**: `number`

y Coordinate of mouse event

#### Returns[​](#returns-4 "Direct link to Returns")

[`PrimitiveHoveredItem`](/lightweight-charts/docs/next/api/interfaces/PrimitiveHoveredItem)