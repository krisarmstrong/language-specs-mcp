# MIDIOutput

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMIDIOutput&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `MIDIOutput` interface of the [Web MIDI API](/en-US/docs/Web/API/Web_MIDI_API) provides methods to add messages to the queue of an output device, and to clear the queue of messages.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

This interface doesn't implement any specific properties, but inherits properties from [MIDIPort](/en-US/docs/Web/API/MIDIPort).

## [Instance methods](#instance_methods)

This interface also inherits methods from [MIDIPort](/en-US/docs/Web/API/MIDIPort).

[MIDIOutput.send()](/en-US/docs/Web/API/MIDIOutput/send)

Queues a message to be sent to the MIDI port.

[MIDIOutput.clear()](/en-US/docs/Web/API/MIDIOutput/clear)

Clears any pending send data from the queue.

## [Examples](#examples)

The following example sends a middle C immediately on MIDI channel 1.

js

```
function sendMiddleC(midiAccess, portID) {
  const noteOnMessage = [0x90, 60, 0x7f]; // note on, middle C, full velocity
  const output = midiAccess.outputs.get(portID);
  output.send(noteOnMessage); // sends the message.
}
```

## [Specifications](#specifications)

Specification
[Web MIDI API# MIDIOutput](https://webaudio.github.io/web-midi-api/#MIDIOutput)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/MIDIOutput/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/midioutput/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMIDIOutput&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmidioutput%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMIDIOutput%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmidioutput%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F70d988f9c45e5fe9493c0da0854be5dcde2a49fe%0A*+Document+last+modified%3A+2024-03-08T14%3A04%3A48.000Z%0A%0A%3C%2Fdetails%3E)
