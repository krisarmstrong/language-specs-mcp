# MIDIMessageEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMIDIMessageEvent&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `MIDIMessageEvent` interface of the [Web MIDI API](/en-US/docs/Web/API/Web_MIDI_API) represents the event passed to the [midimessage](/en-US/docs/Web/API/MIDIInput/midimessage_event) event of the [MIDIInput](/en-US/docs/Web/API/MIDIInput) interface. A `midimessage` event is fired every time a MIDI message is sent from a device represented by a [MIDIInput](/en-US/docs/Web/API/MIDIInput), for example when a MIDI keyboard key is pressed, a knob is tweaked, or a slider is moved.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[MIDIMessageEvent()](/en-US/docs/Web/API/MIDIMessageEvent/MIDIMessageEvent)

Creates a new `MIDIMessageEvent` object instance.

## [Instance properties](#instance_properties)

This interface also inherits properties from [Event](/en-US/docs/Web/API/Event).

[MIDIMessageEvent.data](/en-US/docs/Web/API/MIDIMessageEvent/data)

A [Uint8Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) containing the data bytes of a single MIDI message. See the [MIDI specification](https://midi.org/summary-of-midi-1-0-messages) for more information on its form.

## [Instance methods](#instance_methods)

This interface doesn't implement any specific methods, but inherits methods from [Event](/en-US/docs/Web/API/Event).

## [Examples](#examples)

The following example prints all MIDI messages to the console.

js

```
navigator.requestMIDIAccess().then((midiAccess) => {
  Array.from(midiAccess.inputs).forEach((input) => {
    input[1].onmidimessage = (msg) => {
      console.log(msg);
    };
  });
});
```

## [Specifications](#specifications)

Specification
[Web MIDI API# midimessageevent-interface](https://webaudio.github.io/web-midi-api/#midimessageevent-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 4, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/MIDIMessageEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/midimessageevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMIDIMessageEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmidimessageevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMIDIMessageEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmidimessageevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff2088b8912ef205a737551441d54b73507bd3ac6%0A*+Document+last+modified%3A+2024-08-04T23%3A19%3A14.000Z%0A%0A%3C%2Fdetails%3E)
