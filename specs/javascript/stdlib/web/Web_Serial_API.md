# Web Serial API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_Serial_API&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is available in [Dedicated Web Workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope).

The Web Serial API provides a way for websites to read from and write to serial devices. These devices may be connected via a serial port, or be USB or Bluetooth devices that emulate a serial port.

## In this article

- [Concepts and Usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Extensions to other interfaces](#extensions_to_other_interfaces)
- [HTTP headers](#http_headers)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and Usage](#concepts_and_usage)

The Web Serial API is one of a set of APIs that allow websites to communicate with peripherals connected to a user's computer. It provides the ability to connect to devices that are required by the operating system to communicate via the serial API, rather than USB which can be accessed via the [WebUSB API](/en-US/docs/Web/API/WebUSB_API), or input devices that can be accessed via [WebHID API](/en-US/docs/Web/API/WebHID_API).

Examples of serial devices include 3D printers, and microcontrollers such as the [BBC micro:bit board](https://microbit.org/).

## [Interfaces](#interfaces)

[Serial](/en-US/docs/Web/API/Serial)Experimental

Provides attributes and methods for finding and connecting to serial ports from a web page.

[SerialPort](/en-US/docs/Web/API/SerialPort)Experimental

Provides access to a serial port on the host device.

## [Extensions to other interfaces](#extensions_to_other_interfaces)

[Navigator.serial](/en-US/docs/Web/API/Navigator/serial)Read onlyExperimental

Returns a [Serial](/en-US/docs/Web/API/Serial) object, which represents the entry point into the Web Serial API to enable the control of serial ports.

[WorkerNavigator.serial](/en-US/docs/Web/API/WorkerNavigator/serial)Read onlyExperimental

Returns a [Serial](/en-US/docs/Web/API/Serial) object, which represents the entry point into the Web Serial API to enable the control of serial ports.

## [HTTP headers](#http_headers)

[Permissions-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy)[serial](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/serial) directive

Controls whether the current document is allowed to use the Web Serial API to communicate with serial devices, either directly connected via a serial port, or via USB or Bluetooth devices emulating a serial port.

## [Examples](#examples)

The following examples demonstrate some of the functionality provided by the Web Serial API.

### [Checking for available ports](#checking_for_available_ports)

The following example shows how to check for available ports and allows the user to grant it permission to access additional ports.

The `connect` and `disconnect` events let sites react when a device is connected or disconnected from the system. The [getPorts()](/en-US/docs/Web/API/Serial/getPorts) method is then called to see connected ports that the site already has access to.

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

### [Reading data from a port](#reading_data_from_a_port)

The following example shows how to read data from a port. The outer loop handles non-fatal errors, creating a new reader until a fatal error is encountered and [SerialPort.readable](/en-US/docs/Web/API/SerialPort/readable) becomes `null`.

js

```
while (port.readable) {
  const reader = port.readable.getReader();
  try {
    while (true) {
      const { value, done } = await reader.read();
      if (done) {
        // |reader| has been canceled.
        break;
      }
      // Do something with |value|...
    }
  } catch (error) {
    // Handle |error|...
  } finally {
    reader.releaseLock();
  }
}
```

## [Specifications](#specifications)

Specification
[Web Serial API# serial-interface](https://wicg.github.io/serial/#serial-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Read from and write to a serial port](https://developer.chrome.com/docs/capabilities/serial)
- [Getting started with the Web Serial API](https://codelabs.developers.google.com/codelabs/web-serial#0)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 2, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Web_Serial_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/web_serial_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_Serial_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fweb_serial_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_Serial_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fweb_serial_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0e2c698518ac4aaf54975093a139e764cff62670%0A*+Document+last+modified%3A+2024-12-02T10%3A18%3A54.000Z%0A%0A%3C%2Fdetails%3E)
