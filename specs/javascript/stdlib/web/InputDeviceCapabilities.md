# InputDeviceCapabilities

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `InputDeviceCapabilities` interface of the [Input Device Capabilities API](/en-US/docs/Web/API/InputDeviceCapabilities_API) provides information about the physical device or a group of related devices responsible for generating input events. Events caused by the same physical input device get the same instance of this object, but the converse isn't true. For example, two mice with the same capabilities in a system may appear as a single `InputDeviceCapabilities` instance.

In some instances, `InputDeviceCapabilities` represents the capabilities of logical devices rather than physical devices. This allows, for example, touchscreen keyboards and physical keyboards to be represented the same way when they produce the same input.

## In this article

- [Constructors](#constructors)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructors](#constructors)

[InputDeviceCapabilities()](/en-US/docs/Web/API/InputDeviceCapabilities/InputDeviceCapabilities)Experimental

Creates an `InputDeviceCapabilities` object.

## [Instance properties](#instance_properties)

[InputDeviceCapabilities.firesTouchEvents](/en-US/docs/Web/API/InputDeviceCapabilities/firesTouchEvents)Read onlyExperimental

A [Boolean](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean) that indicates whether the device dispatches touch events.

## [Instance methods](#instance_methods)

None.

## [Specifications](#specifications)

Specification
[Input Device Capabilities# dom-inputdevicecapabilities](https://wicg.github.io/input-device-capabilities/#dom-inputdevicecapabilities)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 2, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/InputDeviceCapabilities/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/inputdevicecapabilities/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInputDeviceCapabilities&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Finputdevicecapabilities%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInputDeviceCapabilities%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Finputdevicecapabilities%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F8cac4a3fed6a702840efd2deda67a922120732d0%0A*+Document+last+modified%3A+2023-12-02T09%3A34%3A08.000Z%0A%0A%3C%2Fdetails%3E)
