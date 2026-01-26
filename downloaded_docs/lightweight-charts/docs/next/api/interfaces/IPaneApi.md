Version: Next

On this page

Represents the interface for interacting with a pane in a lightweight chart.

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem**

## Methods[​](#methods "Direct link to Methods")

### getHeight()[​](#getheight "Direct link to getHeight()")

> **getHeight**(): `number`

Retrieves the height of the pane in pixels.

#### Returns[​](#returns "Direct link to Returns")

`number`

The height of the pane in pixels.

---

### setHeight()[​](#setheight "Direct link to setHeight()")

> **setHeight**(`height`): `void`

Sets the height of the pane.

#### Parameters[​](#parameters "Direct link to Parameters")

• **height**: `number`

The number of pixels to set as the height of the pane.

#### Returns[​](#returns-1 "Direct link to Returns")

`void`

---

### moveTo()[​](#moveto "Direct link to moveTo()")

> **moveTo**(`paneIndex`): `void`

Moves the pane to a new position.

#### Parameters[​](#parameters-1 "Direct link to Parameters")

• **paneIndex**: `number`

The target index of the pane. Should be a number between 0 and the total number of panes - 1.

#### Returns[​](#returns-2 "Direct link to Returns")

`void`

---

### paneIndex()[​](#paneindex "Direct link to paneIndex()")

> **paneIndex**(): `number`

Retrieves the index of the pane.

#### Returns[​](#returns-3 "Direct link to Returns")

`number`

The index of the pane. It is a number between 0 and the total number of panes - 1.

---

### getSeries()[​](#getseries "Direct link to getSeries()")

> **getSeries**(): [`ISeriesApi`](/lightweight-charts/docs/next/api/interfaces/ISeriesApi)<keyof [`SeriesOptionsMap`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsMap), `HorzScaleItem`, [`AreaData`](/lightweight-charts/docs/next/api/interfaces/AreaData)<`HorzScaleItem`> | [`WhitespaceData`](/lightweight-charts/docs/next/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`BarData`](/lightweight-charts/docs/next/api/interfaces/BarData)<`HorzScaleItem`> | [`CandlestickData`](/lightweight-charts/docs/next/api/interfaces/CandlestickData)<`HorzScaleItem`> | [`BaselineData`](/lightweight-charts/docs/next/api/interfaces/BaselineData)<`HorzScaleItem`> | [`LineData`](/lightweight-charts/docs/next/api/interfaces/LineData)<`HorzScaleItem`> | [`HistogramData`](/lightweight-charts/docs/next/api/interfaces/HistogramData)<`HorzScaleItem`> | [`CustomData`](/lightweight-charts/docs/next/api/interfaces/CustomData)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](/lightweight-charts/docs/next/api/interfaces/CustomSeriesWhitespaceData)<`HorzScaleItem`>, [`CustomSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/CustomSeriesOptions) | [`AreaSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/AreaSeriesOptions) | [`BarSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/BarSeriesOptions) | [`CandlestickSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/CandlestickSeriesOptions) | [`BaselineSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/BaselineSeriesOptions) | [`LineSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/LineSeriesOptions) | [`HistogramSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/HistogramSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`AreaStyleOptions`](/lightweight-charts/docs/next/api/interfaces/AreaStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`BarStyleOptions`](/lightweight-charts/docs/next/api/interfaces/BarStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`CandlestickStyleOptions`](/lightweight-charts/docs/next/api/interfaces/CandlestickStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`BaselineStyleOptions`](/lightweight-charts/docs/next/api/interfaces/BaselineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`LineStyleOptions`](/lightweight-charts/docs/next/api/interfaces/LineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`HistogramStyleOptions`](/lightweight-charts/docs/next/api/interfaces/HistogramStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`CustomStyleOptions`](/lightweight-charts/docs/next/api/interfaces/CustomStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)>>[]

Retrieves the array of series for the current pane.

#### Returns[​](#returns-4 "Direct link to Returns")

[`ISeriesApi`](/lightweight-charts/docs/next/api/interfaces/ISeriesApi)<keyof [`SeriesOptionsMap`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsMap), `HorzScaleItem`, [`AreaData`](/lightweight-charts/docs/next/api/interfaces/AreaData)<`HorzScaleItem`> | [`WhitespaceData`](/lightweight-charts/docs/next/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`BarData`](/lightweight-charts/docs/next/api/interfaces/BarData)<`HorzScaleItem`> | [`CandlestickData`](/lightweight-charts/docs/next/api/interfaces/CandlestickData)<`HorzScaleItem`> | [`BaselineData`](/lightweight-charts/docs/next/api/interfaces/BaselineData)<`HorzScaleItem`> | [`LineData`](/lightweight-charts/docs/next/api/interfaces/LineData)<`HorzScaleItem`> | [`HistogramData`](/lightweight-charts/docs/next/api/interfaces/HistogramData)<`HorzScaleItem`> | [`CustomData`](/lightweight-charts/docs/next/api/interfaces/CustomData)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](/lightweight-charts/docs/next/api/interfaces/CustomSeriesWhitespaceData)<`HorzScaleItem`>, [`CustomSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/CustomSeriesOptions) | [`AreaSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/AreaSeriesOptions) | [`BarSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/BarSeriesOptions) | [`CandlestickSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/CandlestickSeriesOptions) | [`BaselineSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/BaselineSeriesOptions) | [`LineSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/LineSeriesOptions) | [`HistogramSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/HistogramSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`AreaStyleOptions`](/lightweight-charts/docs/next/api/interfaces/AreaStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`BarStyleOptions`](/lightweight-charts/docs/next/api/interfaces/BarStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`CandlestickStyleOptions`](/lightweight-charts/docs/next/api/interfaces/CandlestickStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`BaselineStyleOptions`](/lightweight-charts/docs/next/api/interfaces/BaselineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`LineStyleOptions`](/lightweight-charts/docs/next/api/interfaces/LineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`HistogramStyleOptions`](/lightweight-charts/docs/next/api/interfaces/HistogramStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`CustomStyleOptions`](/lightweight-charts/docs/next/api/interfaces/CustomStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)>>[]

An array of series.

---

### getHTMLElement()[​](#gethtmlelement "Direct link to getHTMLElement()")

> **getHTMLElement**(): `HTMLElement`

Retrieves the HTML element of the pane.

#### Returns[​](#returns-5 "Direct link to Returns")

`HTMLElement`

The HTML element of the pane or null if pane wasn't created yet.

---

### attachPrimitive()[​](#attachprimitive "Direct link to attachPrimitive()")

> **attachPrimitive**(`primitive`): `void`

Attaches additional drawing primitive to the pane

#### Parameters[​](#parameters-2 "Direct link to Parameters")

• **primitive**: [`IPanePrimitive`](/lightweight-charts/docs/next/api/type-aliases/IPanePrimitive)<`HorzScaleItem`>

any implementation of IPanePrimitive interface

#### Returns[​](#returns-6 "Direct link to Returns")

`void`

---

### detachPrimitive()[​](#detachprimitive "Direct link to detachPrimitive()")

> **detachPrimitive**(`primitive`): `void`

Detaches additional drawing primitive from the pane

#### Parameters[​](#parameters-3 "Direct link to Parameters")

• **primitive**: [`IPanePrimitive`](/lightweight-charts/docs/next/api/type-aliases/IPanePrimitive)<`HorzScaleItem`>

implementation of IPanePrimitive interface attached before
Does nothing if specified primitive was not attached

#### Returns[​](#returns-7 "Direct link to Returns")

`void`

---

### priceScale()[​](#pricescale "Direct link to priceScale()")

> **priceScale**(`priceScaleId`): [`IPriceScaleApi`](/lightweight-charts/docs/next/api/interfaces/IPriceScaleApi)

Returns the price scale with the given id.

#### Parameters[​](#parameters-4 "Direct link to Parameters")

• **priceScaleId**: `string`

ID of the price scale to find

#### Returns[​](#returns-8 "Direct link to Returns")

[`IPriceScaleApi`](/lightweight-charts/docs/next/api/interfaces/IPriceScaleApi)

#### Throws[​](#throws "Direct link to Throws")

If the price scale with the given id is not found in this pane

---

### setPreserveEmptyPane()[​](#setpreserveemptypane "Direct link to setPreserveEmptyPane()")

> **setPreserveEmptyPane**(`preserve`): `void`

Sets whether to preserve the empty pane

#### Parameters[​](#parameters-5 "Direct link to Parameters")

• **preserve**: `boolean`

Whether to preserve the empty pane

#### Returns[​](#returns-9 "Direct link to Returns")

`void`

---

### preserveEmptyPane()[​](#preserveemptypane "Direct link to preserveEmptyPane()")

> **preserveEmptyPane**(): `boolean`

Returns whether to preserve the empty pane

#### Returns[​](#returns-10 "Direct link to Returns")

`boolean`

Whether to preserve the empty pane

---

### getStretchFactor()[​](#getstretchfactor "Direct link to getStretchFactor()")

> **getStretchFactor**(): `number`

Returns the stretch factor of the pane.
Stretch factor determines the relative size of the pane compared to other panes.

#### Returns[​](#returns-11 "Direct link to Returns")

`number`

The stretch factor of the pane. Default is 1

---

### setStretchFactor()[​](#setstretchfactor "Direct link to setStretchFactor()")

> **setStretchFactor**(`stretchFactor`): `void`

Sets the stretch factor of the pane.
When you creating a pane, the stretch factor is 1 by default.
So if you have three panes, and you want to make the first pane twice as big as the second and third panes, you can set the stretch factor of the first pane to 2000.
Example:

```prism-code
const pane1 = chart.addPane();  
const pane2 = chart.addPane();  
const pane3 = chart.addPane();  
pane1.setStretchFactor(0.2);  
pane2.setStretchFactor(0.3);  
pane3.setStretchFactor(0.5);  
// Now the first pane will be 20% of the total height, the second pane will be 30% of the total height, and the third pane will be 50% of the total height.  
// Note: if you have one pane with default stretch factor of 1 and set other pane's stretch factor to 50,  
// library will try to make second pane 50 times smaller than the first pane
```

#### Parameters[​](#parameters-6 "Direct link to Parameters")

• **stretchFactor**: `number`

The stretch factor of the pane.

#### Returns[​](#returns-12 "Direct link to Returns")

`void`

---

### addCustomSeries()[​](#addcustomseries "Direct link to addCustomSeries()")

> **addCustomSeries**<`TData`, `TOptions`, `TPartialOptions`>(`customPaneView`, `customOptions`?): [`ISeriesApi`](/lightweight-charts/docs/next/api/interfaces/ISeriesApi)<`"Custom"`, `HorzScaleItem`, [`WhitespaceData`](/lightweight-charts/docs/next/api/interfaces/WhitespaceData)<`HorzScaleItem`> | `TData`, `TOptions`, `TPartialOptions`>

Creates a custom series with specified parameters.

A custom series is a generic series which can be extended with a custom renderer to
implement chart types which the library doesn't support by default.

#### Type parameters[​](#type-parameters-1 "Direct link to Type parameters")

• **TData** *extends* [`CustomData`](/lightweight-charts/docs/next/api/interfaces/CustomData)<`HorzScaleItem`>

• **TOptions** *extends* [`CustomSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/CustomSeriesOptions)

• **TPartialOptions** *extends* [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial)<`TOptions` & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> = [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial)<`TOptions` & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)>

#### Parameters[​](#parameters-7 "Direct link to Parameters")

• **customPaneView**: [`ICustomSeriesPaneView`](/lightweight-charts/docs/next/api/interfaces/ICustomSeriesPaneView)<`HorzScaleItem`, `TData`, `TOptions`>

A custom series pane view which implements the custom renderer.

• **customOptions?**: [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial)<`TOptions` & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)>

Customization parameters of the series being created.

```prism-code
const series = pane.addCustomSeries(myCustomPaneView);
```

#### Returns[​](#returns-13 "Direct link to Returns")

[`ISeriesApi`](/lightweight-charts/docs/next/api/interfaces/ISeriesApi)<`"Custom"`, `HorzScaleItem`, [`WhitespaceData`](/lightweight-charts/docs/next/api/interfaces/WhitespaceData)<`HorzScaleItem`> | `TData`, `TOptions`, `TPartialOptions`>

---

### addSeries()[​](#addseries "Direct link to addSeries()")

> **addSeries**<`T`>(`definition`, `options`?): [`ISeriesApi`](/lightweight-charts/docs/next/api/interfaces/ISeriesApi)<`T`, `HorzScaleItem`, [`SeriesDataItemTypeMap`](/lightweight-charts/docs/next/api/interfaces/SeriesDataItemTypeMap)<`HorzScaleItem`>[`T`], [`SeriesOptionsMap`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsMap)[`T`], [`SeriesPartialOptionsMap`](/lightweight-charts/docs/next/api/interfaces/SeriesPartialOptionsMap)[`T`]>

Creates a series with specified parameters.

#### Type parameters[​](#type-parameters-2 "Direct link to Type parameters")

• **T** *extends* keyof [`SeriesOptionsMap`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsMap)

#### Parameters[​](#parameters-8 "Direct link to Parameters")

• **definition**: [`SeriesDefinition`](/lightweight-charts/docs/next/api/interfaces/SeriesDefinition)<`T`>

A series definition.

• **options?**: [`SeriesPartialOptionsMap`](/lightweight-charts/docs/next/api/interfaces/SeriesPartialOptionsMap)[`T`]

Customization parameters of the series being created.

```prism-code
const series = pane.addSeries(LineSeries, { lineWidth: 2 });
```

#### Returns[​](#returns-14 "Direct link to Returns")

[`ISeriesApi`](/lightweight-charts/docs/next/api/interfaces/ISeriesApi)<`T`, `HorzScaleItem`, [`SeriesDataItemTypeMap`](/lightweight-charts/docs/next/api/interfaces/SeriesDataItemTypeMap)<`HorzScaleItem`>[`T`], [`SeriesOptionsMap`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsMap)[`T`], [`SeriesPartialOptionsMap`](/lightweight-charts/docs/next/api/interfaces/SeriesPartialOptionsMap)[`T`]>