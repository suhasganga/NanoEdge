Version: 5.1

On this page

This interface represents a label on the price or time axis

## Methods[​](#methods "Direct link to Methods")

### coordinate()[​](#coordinate "Direct link to coordinate()")

> **coordinate**(): `number`

The desired coordinate for the label. Note that the label will be automatically moved to prevent overlapping with other labels. If you would like the label to be drawn at the
exact coordinate under all circumstances then rather use `fixedCoordinate`.
For a price axis the value returned will represent the vertical distance (pixels) from the top. For a time axis the value will represent the horizontal distance from the left.

#### Returns[​](#returns "Direct link to Returns")

`number`

coordinate. distance from top for price axis, or distance from left for time axis.

---

### fixedCoordinate()?[​](#fixedcoordinate "Direct link to fixedCoordinate()?")

> `optional` **fixedCoordinate**(): `number`

fixed coordinate of the label. A label with a fixed coordinate value will always be drawn at the specified coordinate and will appear above any 'unfixed' labels. If you supply
a fixed coordinate then you should return a large negative number for `coordinate` so that the automatic placement of unfixed labels doesn't leave a blank space for this label.
For a price axis the value returned will represent the vertical distance (pixels) from the top. For a time axis the value will represent the horizontal distance from the left.

#### Returns[​](#returns-1 "Direct link to Returns")

`number`

coordinate. distance from top for price axis, or distance from left for time axis.

---

### text()[​](#text "Direct link to text()")

> **text**(): `string`

#### Returns[​](#returns-2 "Direct link to Returns")

`string`

text of the label

---

### textColor()[​](#textcolor "Direct link to textColor()")

> **textColor**(): `string`

#### Returns[​](#returns-3 "Direct link to Returns")

`string`

text color of the label

---

### backColor()[​](#backcolor "Direct link to backColor()")

> **backColor**(): `string`

#### Returns[​](#returns-4 "Direct link to Returns")

`string`

background color of the label

---

### visible()?[​](#visible "Direct link to visible()?")

> `optional` **visible**(): `boolean`

#### Returns[​](#returns-5 "Direct link to Returns")

`boolean`

whether the label should be visible (default: `true`)

---

### tickVisible()?[​](#tickvisible "Direct link to tickVisible()?")

> `optional` **tickVisible**(): `boolean`

#### Returns[​](#returns-6 "Direct link to Returns")

`boolean`

whether the tick mark line should be visible (default: `true`)