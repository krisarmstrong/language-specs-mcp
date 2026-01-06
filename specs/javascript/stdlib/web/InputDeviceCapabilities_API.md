# InputDeviceCapabilities API

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The InputDeviceCapabilities API provides details about the underlying sources of input events. The API attempts to describe how the device behaves rather than what it is. For example, the first version of the API indicates whether a device fires touch events rather than whether it is a touch screen.

## In this article

- [Input device capabilities concepts and usage](#input_device_capabilities_concepts_and_usage)
- [Interfaces](#interfaces)
- [Extensions to other interfaces](#extensions_to_other_interfaces)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Input device capabilities concepts and usage](#input_device_capabilities_concepts_and_usage)

Because DOM events abstract device input, they provide no way to learn what device or type of device fired an event. This can lead to instances where the same action triggers multiple event handlers. To deal with this, developers make assumptions and use heuristics to normalize behavior on web pages.

The InputDeviceCapabilities API addresses this problem by abstracting the capabilities of input devices. For example, let's say we have a web page that implements both a `touchstart` and a `mousedown` event. We can assume that if the touchstart event is triggered that the user's device has a touch interface. What about when the mousedown event is triggered? It would be useful to know if a `touchstart` event were also triggered so that we don't take the same action twice. We can do this by checking the sourceCapabilities property of the [UIEvent](/en-US/docs/Web/API/UIEvent).

js

```
myButton.addEventListener("mousedown", (e) => {
  // Touch event case handled above, don't change the style again on tap.
  if (!e.sourceCapabilities.firesTouchEvents) myButton.classList.add("pressed");
});
```

## [Interfaces](#interfaces)

[InputDeviceCapabilities](/en-US/docs/Web/API/InputDeviceCapabilities)Experimental

Provides logical information about an input device.

## [Extensions to other interfaces](#extensions_to_other_interfaces)

[UIEvent.sourceCapabilities](/en-US/docs/Web/API/UIEvent/sourceCapabilities)ExperimentalRead only

Returns an instance of the `InputDeviceCapabilities` interface, which provides information about the physical device responsible for generating a touch event.

## [Specifications](#specifications)

Specification
[Input Device Capabilities# dom-inputdevicecapabilities](https://wicg.github.io/input-device-capabilities/#dom-inputdevicecapabilities)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 2, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/InputDeviceCapabilities_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/inputdevicecapabilities_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInputDeviceCapabilities_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Finputdevicecapabilities_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInputDeviceCapabilities_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Finputdevicecapabilities_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F8cac4a3fed6a702840efd2deda67a922120732d0%0A*+Document+last+modified%3A+2023-12-02T09%3A34%3A08.000Z%0A%0A%3C%2Fdetails%3E)
