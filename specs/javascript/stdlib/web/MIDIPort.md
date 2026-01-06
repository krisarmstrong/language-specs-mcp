# MIDIPort

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMIDIPort&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `MIDIPort` interface of the [Web MIDI API](/en-US/docs/Web/API/Web_MIDI_API) represents a MIDI input or output port.

A `MIDIPort` instance is created when a new MIDI device is connected. Therefore it has no constructor.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[MIDIPort.id](/en-US/docs/Web/API/MIDIPort/id)Read only

Returns a string containing the unique ID of the port.

[MIDIPort.manufacturer](/en-US/docs/Web/API/MIDIPort/manufacturer)Read only

Returns a string containing the manufacturer of the port.

[MIDIPort.name](/en-US/docs/Web/API/MIDIPort/name)Read only

Returns a string containing the system name of the port.

[MIDIPort.type](/en-US/docs/Web/API/MIDIPort/type)Read only

Returns a string containing the type of the port, one of:

["input"](#input)

The `MIDIPort` is an input port.

["output"](#output)

The `MIDIPort` is an output port.

[MIDIPort.version](/en-US/docs/Web/API/MIDIPort/version)Read only

Returns a string containing the version of the port.

[MIDIPort.state](/en-US/docs/Web/API/MIDIPort/state)Read only

Returns a string containing the state of the port, one of:

["disconnected"](#disconnected)

The device that this `MIDIPort` represents is disconnected from the system.

["connected"](#connected)

The device that this `MIDIPort` represents is currently connected.

[MIDIPort.connection](/en-US/docs/Web/API/MIDIPort/connection)Read only

Returns a string containing the connection state of the port, one of:

["open"](#open)

The device that this `MIDIPort` represents has been opened and is available.

["closed"](#closed)

The device that this `MIDIPort` represents has not been opened, or has been closed.

["pending"](#pending)

The device that this `MIDIPort` represents has been opened but has subsequently disconnected.

## [Instance methods](#instance_methods)

This interface also inherits methods from [EventTarget](/en-US/docs/Web/API/EventTarget).

[MIDIPort.open()](/en-US/docs/Web/API/MIDIPort/open)

Makes the MIDI device connected to this `MIDIPort` explicitly available, and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which resolves once access to the port has been successful.

[MIDIPort.close()](/en-US/docs/Web/API/MIDIPort/close)

Makes the MIDI device connected to this `MIDIPort` unavailable, changing the [state](/en-US/docs/Web/API/MIDIPort/state) from `"open"` to `"closed"`. This returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which resolves once the port has been closed.

## [Events](#events)

[statechange](/en-US/docs/Web/API/MIDIPort/statechange_event)

Called when an existing port changes its state or connection.

## [Examples](#examples)

### [List ports and their information](#list_ports_and_their_information)

The following example lists input and output ports, and displays information about them using properties of `MIDIPort`.

js

```
function listInputsAndOutputs(midiAccess) {
  for (const entry of midiAccess.inputs) {
    const input = entry[1];
    console.log(
      `Input port [type:'${input.type}'] id:'${input.id}' manufacturer: '${input.manufacturer}' name: '${input.name}' version: '${input.version}'`,
    );
  }

  for (const entry of midiAccess.outputs) {
    const output = entry[1];
    console.log(
      `Output port [type:'${output.type}'] id: '${output.id}' manufacturer: '${output.manufacturer}' name: '${output.name}' version: '${output.version}'`,
    );
  }
}
```

### [Add available ports to a select list](#add_available_ports_to_a_select_list)

The following example takes the list of input ports and adds them to a select list, in order that a user can choose the device they want to use.

js

```
inputs.forEach((port, key) => {
  const opt = document.createElement("option");
  opt.text = port.name;
  document.getElementById("port-selector").add(opt);
});
```

## [Specifications](#specifications)

Specification
[Web MIDI API# MIDIPort](https://webaudio.github.io/web-midi-api/#MIDIPort)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/MIDIPort/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/midiport/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMIDIPort&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmidiport%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMIDIPort%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmidiport%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
