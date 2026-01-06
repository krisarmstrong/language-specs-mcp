# SerialPort

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSerialPort&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is available in [Dedicated Web Workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope).

The `SerialPort` interface of the [Web Serial API](/en-US/docs/Web/API/Web_Serial_API) provides access to a serial port on the host device.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

Instances of this interface may be obtained by calling methods of the [Serial](/en-US/docs/Web/API/Serial) interface, therefore it has no constructor of its own.

## [Instance properties](#instance_properties)

[SerialPort.connected](/en-US/docs/Web/API/SerialPort/connected)Read onlyExperimental

Returns a boolean value that indicates whether the port is logically connected to the device.

[SerialPort.readable](/en-US/docs/Web/API/SerialPort/readable)Read onlyExperimental

Returns a [ReadableStream](/en-US/docs/Web/API/ReadableStream) for receiving data from the device connected to the port.

[SerialPort.writable](/en-US/docs/Web/API/SerialPort/writable)Read onlyExperimental

Returns a [WritableStream](/en-US/docs/Web/API/WritableStream) for sending data to the device connected to the port.

## [Instance methods](#instance_methods)

[SerialPort.forget()](/en-US/docs/Web/API/SerialPort/forget)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when access to the serial port is revoked. Calling this "forgets" the device, resetting any previously-set permissions so the calling site can no longer communicate with the port.

[SerialPort.getInfo()](/en-US/docs/Web/API/SerialPort/getInfo)Experimental

Returns an object containing identifying information for the device available via the port.

[SerialPort.open()](/en-US/docs/Web/API/SerialPort/open)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when the port is opened. By default the port is opened with 8 data bits, 1 stop bit and no parity checking.

[SerialPort.setSignals()](/en-US/docs/Web/API/SerialPort/setSignals)Experimental

Sets control signals on the port and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when they are set.

[SerialPort.getSignals()](/en-US/docs/Web/API/SerialPort/getSignals)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with an object containing the current state of the port's control signals.

[SerialPort.close()](/en-US/docs/Web/API/SerialPort/close)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when the port closes.

## [Events](#events)

[connect](/en-US/docs/Web/API/SerialPort/connect_event)Experimental

Fired when the port connects to the device.

[disconnect](/en-US/docs/Web/API/SerialPort/disconnect_event)Experimental

Fired when the port disconnects from the device.

## [Examples](#examples)

### [Opening a port](#opening_a_port)

Before communicating on a serial port it must be opened. Opening the port allows the site to specify the necessary parameters that control how data is transmitted and received. Developers should check the documentation for the device they are connecting to for the appropriate parameters.

js

```
await port.open({ baudRate: 9600 /* pick your baud rate */ });
```

Once the `Promise` returned by `open()` resolves the `readable` and `writable` attributes can be accessed to get the [ReadableStream](/en-US/docs/Web/API/ReadableStream) and [WritableStream](/en-US/docs/Web/API/WritableStream) instances for receiving data from and sending data to the connected device.

### [Reading data from a port](#reading_data_from_a_port)

The following example shows how to read data from a port. The outer loop handles non-fatal errors, creating a new reader until a fatal error is encountered and `readable` becomes `null`.

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
      // Do something with |value|…
    }
  } catch (error) {
    // Handle |error|…
  } finally {
    reader.releaseLock();
  }
}
```

### [Writing data to a port](#writing_data_to_a_port)

The following example shows how to write a string to a port. A [TextEncoder](/en-US/docs/Web/API/TextEncoder) converts the string to a `Uint8Array` before transmission.

js

```
const encoder = new TextEncoder();
const writer = port.writable.getWriter();
await writer.write(encoder.encode("PING"));
writer.releaseLock();
```

## [Specifications](#specifications)

Specification
[Web Serial API# dom-serialport](https://wicg.github.io/serial/#dom-serialport)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 2, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/SerialPort/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/serialport/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSerialPort&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fserialport%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSerialPort%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fserialport%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F861d367a39f380ac4e6a01ae215fc1beb3e27c31%0A*+Document+last+modified%3A+2024-12-02T10%3A21%3A55.000Z%0A%0A%3C%2Fdetails%3E)
