Version: 5.1

On this page

Interface for a pane primitive.

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **T**

• **Options**

## Properties[​](#properties "Direct link to Properties")

### detach()[​](#detach "Direct link to detach()")

> **detach**: () => `void`

Detaches the plugin from the pane.

#### Returns[​](#returns "Direct link to Returns")

`void`

---

### getPane()[​](#getpane "Direct link to getPane()")

> **getPane**: () => [`IPaneApi`](/lightweight-charts/docs/api/interfaces/IPaneApi)<`T`>

Returns the current pane.

#### Returns[​](#returns-1 "Direct link to Returns")

[`IPaneApi`](/lightweight-charts/docs/api/interfaces/IPaneApi)<`T`>

---

### applyOptions()?[​](#applyoptions "Direct link to applyOptions()?")

> `optional` **applyOptions**: (`options`) => `void`

Applies options to the primitive.

#### Parameters[​](#parameters "Direct link to Parameters")

• **options**: [`DeepPartial`](/lightweight-charts/docs/api/type-aliases/DeepPartial)<`Options`>

Options to apply. The options are deeply merged with the current options.

#### Returns[​](#returns-2 "Direct link to Returns")

`void`