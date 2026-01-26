Version: Next

On this page

> **createTextWatermark**<`T`>(`pane`, `options`): [`ITextWatermarkPluginApi`](/lightweight-charts/docs/next/api/type-aliases/ITextWatermarkPluginApi)<`T`>

Creates an image watermark.

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **T**

## Parameters[​](#parameters "Direct link to Parameters")

• **pane**: [`IPaneApi`](/lightweight-charts/docs/next/api/interfaces/IPaneApi)<`T`>

Target pane.

• **options**: [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`TextWatermarkOptions`](/lightweight-charts/docs/next/api/interfaces/TextWatermarkOptions)>

Watermark options.

## Returns[​](#returns "Direct link to Returns")

[`ITextWatermarkPluginApi`](/lightweight-charts/docs/next/api/type-aliases/ITextWatermarkPluginApi)<`T`>

Image watermark wrapper.

## Example[​](#example "Direct link to Example")

```prism-code
import { createTextWatermark } from 'lightweight-charts';  
  
const firstPane = chart.panes()[0];  
const textWatermark = createTextWatermark(firstPane, {  
      horzAlign: 'center',  
      vertAlign: 'center',  
      lines: [  
        {  
          text: 'Hello',  
          color: 'rgba(255,0,0,0.5)',  
          fontSize: 100,  
          fontStyle: 'bold',  
        },  
        {  
          text: 'This is a text watermark',  
          color: 'rgba(0,0,255,0.5)',  
          fontSize: 50,  
          fontStyle: 'italic',  
          fontFamily: 'monospace',  
        },  
      ],  
});  
// to change options  
textWatermark.applyOptions({ horzAlign: 'left' });  
// to remove watermark from the pane  
textWatermark.detach();
```