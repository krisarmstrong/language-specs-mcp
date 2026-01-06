# Serial

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSerial&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is available in [Dedicated Web Workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope).

The `Serial` interface of the [Web Serial API](/en-US/docs/Web/API/Web_Serial_API) provides attributes and methods for finding and connecting to serial ports from a web page.

## In this article

- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance methods](#instance_methods)

[Serial.requestPort()](/en-US/docs/Web/API/Serial/requestPort)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with an instance of [SerialPort](/en-US/docs/Web/API/SerialPort) representing the device chosen by the user. This method must be called via [transient activation](/en-US/docs/Glossary/Transient_activation).

[Serial.getPorts()](/en-US/docs/Web/API/Serial/getPorts)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with an array of [SerialPort](/en-US/docs/Web/API/SerialPort) objects representing serial ports connected to the host which the origin has permission to access.

## [Events](#events)

The following events are available to `Serial` via event bubbling from [SerialPort](/en-US/docs/Web/API/SerialPort):

`SerialPort`[connect](/en-US/docs/Web/API/SerialPort/connect_event) event

An event fired when a port has been connected to the device.

`SerialPort`[disconnect](/en-US/docs/Web/API/SerialPort/disconnect_event) event

An event fired when a port has been disconnected from the device.

## [Examples](#examples)

The following example shows how a site can check for available ports and allow the user to grant it permission to access additional ports.

On load event listeners are added for the [connect](/en-US/docs/Web/API/SerialPort/connect_event) and [disconnect](/en-US/docs/Web/API/SerialPort/disconnect_event) events so that the site can react when a device is connected or disconnected from the system. The [getPorts()](/en-US/docs/Web/API/Serial/getPorts) method is then called to see which ports are connected that the site already has access to.

If the site doesn't have access to any connected ports it has to wait until it has user activation to proceed. In this example we use a [click](/en-US/docs/Web/API/Element/click_event) event handler on a button for this task. A filter is passed to [requestPort()](/en-US/docs/Web/API/Serial/requestPort) with a USB vendor ID in order to limit the set of devices shown to the user to only USB devices built by a particular manufacturer.

js

```
navigator.serial.addEventListener("connect", (e) => {
  // Connect to `e.target` or add it to a list of available ports.
});

navigator.serial.addEventListener("disconnect", (e) => {
  // Remove `e.target` from the list of available ports.
});

navigator.serial.getPorts().then((ports) => {
  // Initialize the list of available ports with `ports` on page load.
});

button.addEventListener("click", () => {
  const usbVendorId = 0xabcd;
  navigator.serial
    .requestPort({ filters: [{ usbVendorId }] })
    .then((port) => {
      // Connect to `port` or add it to the list of available ports.
    })
    .catch((e) => {
      // The user didn't select a port.
    });
});
```

## [Specifications](#specifications)

Specification
[Web Serial API# serial-interface](https://wicg.github.io/serial/#serial-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Serial/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/serial/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSerial&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fserial%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSerial%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fserial%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
