# MIDIAccess

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMIDIAccess&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `MIDIAccess` interface of the [Web MIDI API](/en-US/docs/Web/API/Web_MIDI_API) provides methods for listing MIDI input and output devices, and obtaining access to those devices.

`MIDIAccess` is a [transferable object](/en-US/docs/Web/API/Web_Workers_API/Transferable_objects).

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[MIDIAccess.inputs](/en-US/docs/Web/API/MIDIAccess/inputs)Read only

Returns an instance of [MIDIInputMap](/en-US/docs/Web/API/MIDIInputMap) which provides access to any available MIDI input ports.

[MIDIAccess.outputs](/en-US/docs/Web/API/MIDIAccess/outputs)Read only

Returns an instance of [MIDIOutputMap](/en-US/docs/Web/API/MIDIOutputMap) which provides access to any available MIDI output ports.

[MIDIAccess.sysexEnabled](/en-US/docs/Web/API/MIDIAccess/sysexEnabled)Read only

A boolean attribute indicating whether system exclusive support is enabled on the current MIDIAccess instance.

### [Events](#events)

[statechange](/en-US/docs/Web/API/MIDIAccess/statechange_event)

Called whenever a new MIDI port is added or an existing port changes state.

## [Examples](#examples)

The [Navigator.requestMIDIAccess()](/en-US/docs/Web/API/Navigator/requestMIDIAccess) method returns a promise that resolves with a `MIDIAccess` object. Information about the input and output ports is returned.

When a port changes state, information about that port is printed to the console.

js

```
navigator.requestMIDIAccess().then((access) => {
  // Get lists of available MIDI controllers
  const inputs = access.inputs.values();
  const outputs = access.outputs.values();

  access.onstatechange = (event) => {
    // Print information about the (dis)connected MIDI controller
    console.log(event.port.name, event.port.manufacturer, event.port.state);
  };
});
```

## [Specifications](#specifications)

Specification
[Web MIDI API# midiaccess-interface](https://webaudio.github.io/web-midi-api/#midiaccess-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 20, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/MIDIAccess/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/midiaccess/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMIDIAccess&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmidiaccess%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMIDIAccess%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmidiaccess%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F47c461a1ebc95289543ea2962c6dbc8d57ee76d9%0A*+Document+last+modified%3A+2024-10-20T23%3A33%3A37.000Z%0A%0A%3C%2Fdetails%3E)
