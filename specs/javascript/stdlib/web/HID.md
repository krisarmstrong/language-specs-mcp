# HID

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHID&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API), except for [Shared Web Workers](/en-US/docs/Web/API/SharedWorkerGlobalScope).

The `HID` interface provides methods for connecting to HID devices, listing attached HID devices and event handlers for connected HID devices.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface also inherits properties of its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

## [Instance methods](#instance_methods)

This interface also inherits methods of its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[getDevices()](/en-US/docs/Web/API/HID/getDevices)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with an array of connected HID devices that the user has previously been granted access to in response to a [requestDevice()](/en-US/docs/Web/API/HID/requestDevice) call.

[requestDevice()](/en-US/docs/Web/API/HID/requestDevice)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with an array of connected [HIDDevice](/en-US/docs/Web/API/HIDDevice) objects. Calling this function will trigger the user agent's permission flow in order to gain permission to access one selected device from the returned list of devices.

### [Events](#events)

[connect](/en-US/docs/Web/API/HID/connect_event)Experimental

Fired when an HID device is connected.

[disconnect](/en-US/docs/Web/API/HID/disconnect_event)Experimental

Fired when an HID device is disconnected.

## [Specifications](#specifications)

Specification
[WebHID API# dom-hid](https://wicg.github.io/webhid/#dom-hid)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebHID API](/en-US/docs/Web/API/WebHID_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 17, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/HID/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/hid/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHID&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhid%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHID%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhid%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F534e2c61fee576355e8a9b7036d9fa36056edb03%0A*+Document+last+modified%3A+2024-10-17T16%3A09%3A06.000Z%0A%0A%3C%2Fdetails%3E)
