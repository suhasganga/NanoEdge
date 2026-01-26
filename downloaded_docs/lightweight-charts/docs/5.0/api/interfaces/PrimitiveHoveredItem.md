Version: 5.0

On this page

Data representing the currently hovered object from the Hit test.

## Properties[​](#properties "Direct link to Properties")

### cursorStyle?[​](#cursorstyle "Direct link to cursorStyle?")

> `optional` **cursorStyle**: `string`

CSS cursor style as defined here: [MDN: CSS Cursor](https://developer.mozilla.org/en-US/docs/Web/CSS/cursor) or `undefined`
if you want the library to use the default cursor style instead.

---

### externalId[​](#externalid "Direct link to externalId")

> **externalId**: `string`

Hovered objects external ID. Can be used to identify the source item within a mouse subscriber event.

---

### zOrder[​](#zorder "Direct link to zOrder")

> **zOrder**: [`PrimitivePaneViewZOrder`](/lightweight-charts/docs/5.0/api/type-aliases/PrimitivePaneViewZOrder)

The zOrder of the hovered item.

---

### isBackground?[​](#isbackground "Direct link to isBackground?")

> `optional` **isBackground**: `boolean`

Set to true if the object is rendered using `drawBackground` instead of `draw`.