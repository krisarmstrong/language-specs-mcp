# MIDIConnectionEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMIDIConnectionEvent&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `MIDIConnectionEvent` interface of the [Web MIDI API](/en-US/docs/Web/API/Web_MIDI_API) is the event passed to the [statechange](/en-US/docs/Web/API/MIDIAccess/statechange_event) event of the [MIDIAccess](/en-US/docs/Web/API/MIDIAccess) interface and the [statechange](/en-US/docs/Web/API/MIDIPort/statechange_event) event of the [MIDIPort](/en-US/docs/Web/API/MIDIPort) interface. This occurs any time a new port becomes available, or when a previously available port becomes unavailable. For example, this event is fired whenever a MIDI device is either plugged in to or unplugged from a computer.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[MIDIConnectionEvent()](/en-US/docs/Web/API/MIDIConnectionEvent/MIDIConnectionEvent)

Creates a new `MIDIConnectionEvent` object.

## [Instance properties](#instance_properties)

[MIDIConnectionEvent.port](/en-US/docs/Web/API/MIDIConnectionEvent/port)Read only

Returns a reference to a [MIDIPort](/en-US/docs/Web/API/MIDIPort) instance for a port that has been connected or disconnected.

## [Examples](#examples)

The [Navigator.requestMIDIAccess()](/en-US/docs/Web/API/Navigator/requestMIDIAccess) method returns a promise that resolves with a [MIDIAccess](/en-US/docs/Web/API/MIDIAccess) object. When a port changes state, a `MIDIConnectionEvent` is passed to [statechange](/en-US/docs/Web/API/MIDIAccess/statechange_event) event. Information about the port can then be printed to the console.

js

```
navigator.requestMIDIAccess().then((access) => {
  access.onstatechange = (event) => {
    console.log(event.port.name, event.port.manufacturer, event.port.state);
  };
});
```

## [Specifications](#specifications)

Specification
[Web MIDI API# midiconnectionevent-interface](https://webaudio.github.io/web-midi-api/#midiconnectionevent-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 6, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/MIDIConnectionEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/midiconnectionevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMIDIConnectionEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmidiconnectionevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMIDIConnectionEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmidiconnectionevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F758ff14c18157e6be318a498083333558c1e50c1%0A*+Document+last+modified%3A+2023-09-06T12%3A59%3A54.000Z%0A%0A%3C%2Fdetails%3E)
