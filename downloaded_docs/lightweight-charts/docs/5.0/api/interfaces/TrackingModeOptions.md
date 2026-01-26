Version: 5.0

On this page

Represent options for the tracking mode's behavior.

Mobile users will not have the ability to see the values/dates like they do on desktop.
To see it, they should enter the tracking mode. The tracking mode will deactivate the scrolling
and make it possible to check values and dates.

## Properties[​](#properties "Direct link to Properties")

### exitMode[​](#exitmode "Direct link to exitMode")

> **exitMode**: [`TrackingModeExitMode`](/lightweight-charts/docs/5.0/api/enumerations/TrackingModeExitMode)

Determine how to exit the tracking mode.

By default, mobile users will long press to deactivate the scroll and have the ability to check values and dates.
Another press is required to activate the scroll, be able to move left/right, zoom, etc.

#### Default Value[​](#default-value "Direct link to Default Value")

```prism-code
{@link TrackingModeExitMode.OnNextTap}
```