Version: 4.2

On this page

> **createChartEx**<`HorzScaleItem`, `THorzScaleBehavior`>(`container`, `horzScaleBehavior`, `options`?): [`IChartApiBase`](/lightweight-charts/docs/4.2/api/interfaces/IChartApiBase)<`HorzScaleItem`>

This function is the main entry point of the Lightweight Charting Library. If you are using time values
for the horizontal scale then it is recommended that you rather use the [createChart](/lightweight-charts/docs/4.2/api/functions/createChart) function.

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem**

type of points on the horizontal scale

• **THorzScaleBehavior** *extends* [`IHorzScaleBehavior`](/lightweight-charts/docs/4.2/api/interfaces/IHorzScaleBehavior)<`HorzScaleItem`>

type of horizontal axis strategy that encapsulate all the specific behaviors of the horizontal scale type

## Parameters[​](#parameters "Direct link to Parameters")

• **container**: `string` | `HTMLElement`

ID of HTML element or element itself

• **horzScaleBehavior**: `THorzScaleBehavior`

Horizontal scale behavior

• **options?**: [`DeepPartial`](/lightweight-charts/docs/4.2/api/type-aliases/DeepPartial)<`ReturnType`<`THorzScaleBehavior`[`"options"`]>>

Any subset of options to be applied at start.

## Returns[​](#returns "Direct link to Returns")

[`IChartApiBase`](/lightweight-charts/docs/4.2/api/interfaces/IChartApiBase)<`HorzScaleItem`>

An interface to the created chart