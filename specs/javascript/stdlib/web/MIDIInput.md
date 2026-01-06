# MIDIInput

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMIDIInput&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `MIDIInput` interface of the [Web MIDI API](/en-US/docs/Web/API/Web_MIDI_API) receives messages from a MIDI input port.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

This interface doesn't implement any specific properties, but inherits properties from [MIDIPort](/en-US/docs/Web/API/MIDIPort).

## [Instance methods](#instance_methods)

This interface doesn't implement any specific methods, but inherits methods from [MIDIPort](/en-US/docs/Web/API/MIDIPort).

### [Events](#events)

[midimessage](/en-US/docs/Web/API/MIDIInput/midimessage_event)

Fired when the current port receives a MIDI message.

## [Examples](#examples)

In the following example the name of each `MIDIInput` is printed to the console. Then, `midimessage` events are listened for on all input ports. When a message is received the [MIDIMessageEvent.data](/en-US/docs/Web/API/MIDIMessageEvent/data) property is printed to the console.

js

```
inputs.forEach((input) => {
  console.log(input.name); /* inherited property from MIDIPort */
  input.onmidimessage = (message) => {
    console.log(message.data);
  };
});
```

## [Specifications](#specifications)

Specification
[Web MIDI API# midiinput-interface](https://webaudio.github.io/web-midi-api/#midiinput-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 28, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/MIDIInput/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/midiinput/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMIDIInput&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmidiinput%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMIDIInput%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmidiinput%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2ba2c0efbdf0c34b1da02203e4e84b571c883629%0A*+Document+last+modified%3A+2023-02-28T14%3A00%3A22.000Z%0A%0A%3C%2Fdetails%3E)
