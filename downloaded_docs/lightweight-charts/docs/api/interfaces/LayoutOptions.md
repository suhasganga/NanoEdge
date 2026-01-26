Version: 5.1

On this page

Represents layout options

## Properties[​](#properties "Direct link to Properties")

### background[​](#background "Direct link to background")

> **background**: [`Background`](/lightweight-charts/docs/api/type-aliases/Background)

Chart and scales background color.

#### Default Value[​](#default-value "Direct link to Default Value")

`{ type: ColorType.Solid, color: '#FFFFFF' }`

---

### textColor[​](#textcolor "Direct link to textColor")

> **textColor**: `string`

Color of text on the scales.

#### Default Value[​](#default-value-1 "Direct link to Default Value")

`'#191919'`

---

### fontSize[​](#fontsize "Direct link to fontSize")

> **fontSize**: `number`

Font size of text on scales in pixels.

#### Default Value[​](#default-value-2 "Direct link to Default Value")

`12`

---

### fontFamily[​](#fontfamily "Direct link to fontFamily")

> **fontFamily**: `string`

Font family of text on the scales.

#### Default Value[​](#default-value-3 "Direct link to Default Value")

`-apple-system, BlinkMacSystemFont, 'Trebuchet MS', Roboto, Ubuntu, sans-serif`

---

### panes[​](#panes "Direct link to panes")

> **panes**: [`LayoutPanesOptions`](/lightweight-charts/docs/api/interfaces/LayoutPanesOptions)

Panes options.

#### Default Value[​](#default-value-4 "Direct link to Default Value")

`{ enableResize: true, separatorColor: '#2B2B43', separatorHoverColor: 'rgba(178, 181, 189, 0.2)'}`

---

### attributionLogo[​](#attributionlogo "Direct link to attributionLogo")

> **attributionLogo**: `boolean`

Display the TradingView attribution logo on the main chart pane.

The licence for library specifies that you add the "attribution notice"
from the NOTICE file to your code and a link to <https://www.tradingview.com/> to
the page of your website or mobile application that is available to your users.
Using this attribution logo is sufficient for meeting this linking requirement.
However, if you already fulfill this requirement then you can disable this
attribution logo.

#### Default Value[​](#default-value-5 "Direct link to Default Value")

```prism-code
true
```

---

### colorSpace[​](#colorspace "Direct link to colorSpace")

> **colorSpace**: [`ColorSpace`](/lightweight-charts/docs/api/type-aliases/ColorSpace)

Specifies the color space of the rendering context for the internal
canvas elements.

Note: this option should only be specified during the chart creation
and not changed at a later stage by using `applyOptions`.

#### Default Value[​](#default-value-6 "Direct link to Default Value")

`srgb`

See [HTMLCanvasElement: getContext() method - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/getContext#colorspace) for more info

---

### colorParsers[​](#colorparsers "Direct link to colorParsers")

> **colorParsers**: [`CustomColorParser`](/lightweight-charts/docs/api/type-aliases/CustomColorParser)[]

Array of custom color parser functions to handle color formats outside of standard sRGB values.
Each parser function takes a string input and should return either:

* An [Rgba](/lightweight-charts/docs/api/type-aliases/Rgba) array [r,g,b,a] for valid colors (with values 0-255 for rgb and 0-1 for a)
* null if the parser cannot handle that color string, allowing the next parser to attempt it

Parsers are tried in order until one returns a non-null result. This allows chaining multiple
parsers to handle different color space formats.

Note: this option should only be specified during the chart creation
and not changed at a later stage by using `applyOptions`.

The library already supports these color formats by default:

* Hex colors (#RGB, #RGBA, #RRGGBB, #RRGGBBAA)
* RGB/RGBA functions (rgb(), rgba())
* HSL/HSLA functions (hsl(), hsla())
* HWB function (hwb())
* Named colors (red, blue, etc.)
* 'transparent' keyword

Custom parsers are only needed for other color spaces like:

* Display P3: color(display-p3 r g b)
* CIE Lab: lab(l a b)
* LCH: lch(l c h)
* Oklab: oklab(l a b)
* Oklch: oklch(l c h)
* ...