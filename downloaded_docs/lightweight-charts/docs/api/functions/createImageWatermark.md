Version: 5.1

On this page

> **createImageWatermark**<`T`>(`pane`, `imageUrl`, `options`): [`IImageWatermarkPluginApi`](/lightweight-charts/docs/api/type-aliases/IImageWatermarkPluginApi)<`T`>

Creates an image watermark.

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **T**

## Parameters[​](#parameters "Direct link to Parameters")

• **pane**: [`IPaneApi`](/lightweight-charts/docs/api/interfaces/IPaneApi)<`T`>

Target pane.

• **imageUrl**: `string`

Image URL.

• **options**: [`DeepPartial`](/lightweight-charts/docs/api/type-aliases/DeepPartial) <[`ImageWatermarkOptions`](/lightweight-charts/docs/api/interfaces/ImageWatermarkOptions)>

Watermark options.

## Returns[​](#returns "Direct link to Returns")

[`IImageWatermarkPluginApi`](/lightweight-charts/docs/api/type-aliases/IImageWatermarkPluginApi)<`T`>

Image watermark wrapper.

## Example[​](#example "Direct link to Example")

```prism-code
import { createImageWatermark } from 'lightweight-charts';  
  
const firstPane = chart.panes()[0];  
const imageWatermark = createImageWatermark(firstPane, '/images/my-image.png', {  
  alpha: 0.5,  
  padding: 20,  
});  
// to change options  
imageWatermark.applyOptions({ padding: 10 });  
// to remove watermark from the pane  
imageWatermark.detach();
```