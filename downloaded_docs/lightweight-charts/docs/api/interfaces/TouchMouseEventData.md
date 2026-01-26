Version: 5.1

On this page

The TouchMouseEventData interface represents events that occur due to the user interacting with a
pointing device (such as a mouse).
See [MouseEvent](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent)

## Properties[​](#properties "Direct link to Properties")

### clientX[​](#clientx "Direct link to clientX")

> `readonly` **clientX**: [`Coordinate`](/lightweight-charts/docs/api/type-aliases/Coordinate)

The X coordinate of the mouse pointer in local (DOM content) coordinates.

---

### clientY[​](#clienty "Direct link to clientY")

> `readonly` **clientY**: [`Coordinate`](/lightweight-charts/docs/api/type-aliases/Coordinate)

The Y coordinate of the mouse pointer in local (DOM content) coordinates.

---

### pageX[​](#pagex "Direct link to pageX")

> `readonly` **pageX**: [`Coordinate`](/lightweight-charts/docs/api/type-aliases/Coordinate)

The X coordinate of the mouse pointer relative to the whole document.

---

### pageY[​](#pagey "Direct link to pageY")

> `readonly` **pageY**: [`Coordinate`](/lightweight-charts/docs/api/type-aliases/Coordinate)

The Y coordinate of the mouse pointer relative to the whole document.

---

### screenX[​](#screenx "Direct link to screenX")

> `readonly` **screenX**: [`Coordinate`](/lightweight-charts/docs/api/type-aliases/Coordinate)

The X coordinate of the mouse pointer in global (screen) coordinates.

---

### screenY[​](#screeny "Direct link to screenY")

> `readonly` **screenY**: [`Coordinate`](/lightweight-charts/docs/api/type-aliases/Coordinate)

The Y coordinate of the mouse pointer in global (screen) coordinates.

---

### localX[​](#localx "Direct link to localX")

> `readonly` **localX**: [`Coordinate`](/lightweight-charts/docs/api/type-aliases/Coordinate)

The X coordinate of the mouse pointer relative to the chart / price axis / time axis canvas element.

---

### localY[​](#localy "Direct link to localY")

> `readonly` **localY**: [`Coordinate`](/lightweight-charts/docs/api/type-aliases/Coordinate)

The Y coordinate of the mouse pointer relative to the chart / price axis / time axis canvas element.

---

### ctrlKey[​](#ctrlkey "Direct link to ctrlKey")

> `readonly` **ctrlKey**: `boolean`

Returns a boolean value that is true if the Ctrl key was active when the key event was generated.

---

### altKey[​](#altkey "Direct link to altKey")

> `readonly` **altKey**: `boolean`

Returns a boolean value that is true if the Alt (Option or ⌥ on macOS) key was active when the
key event was generated.

---

### shiftKey[​](#shiftkey "Direct link to shiftKey")

> `readonly` **shiftKey**: `boolean`

Returns a boolean value that is true if the Shift key was active when the key event was generated.

---

### metaKey[​](#metakey "Direct link to metaKey")

> `readonly` **metaKey**: `boolean`

Returns a boolean value that is true if the Meta key (on Mac keyboards, the ⌘ Command key; on
Windows keyboards, the Windows key (⊞)) was active when the key event was generated.