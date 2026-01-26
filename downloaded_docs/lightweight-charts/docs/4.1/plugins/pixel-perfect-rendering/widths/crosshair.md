Version: 4.1

tip

It is recommend that you first read the [Pixel Perfect Rendering](/lightweight-charts/docs/4.1/plugins/pixel-perfect-rendering) page.

The following functions can be used to get the calculated width that the library would use for a crosshair or grid line at a specific device pixel ratio.

```prism-code
/**  
 * Default grid / crosshair line width in Bitmap sizing  
 * @param horizontalPixelRatio - horizontal pixel ratio  
 * @returns default grid / crosshair line width in Bitmap sizing  
 */  
export function gridAndCrosshairBitmapWidth(  
    horizontalPixelRatio: number  
): number {  
    return Math.max(1, Math.floor(horizontalPixelRatio));  
}  
  
/**  
 * Default grid / crosshair line width in Media sizing  
 * @param horizontalPixelRatio - horizontal pixel ratio  
 * @returns default grid / crosshair line width in Media sizing  
 */  
export function gridAndCrosshairMediaWidth(  
    horizontalPixelRatio: number  
): number {  
    return (  
        gridAndCrosshairBitmapWidth(horizontalPixelRatio) / horizontalPixelRatio  
    );  
}
```