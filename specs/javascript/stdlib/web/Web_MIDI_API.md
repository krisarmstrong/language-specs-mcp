# Web MIDI API

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The Web MIDI API connects to and interacts with Musical Instrument Digital Interface (MIDI) Devices.

The interfaces deal with the practical aspects of sending and receiving MIDI messages. Therefore, the API can be used for musical and non-musical uses, with any MIDI device connected to your computer.

## In this article

- [Interfaces](#interfaces)
- [Security requirements](#security_requirements)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Interfaces](#interfaces)

[MIDIInputMap](/en-US/docs/Web/API/MIDIInputMap)

Represents all of the available MIDI input ports.

[MIDIOutputMap](/en-US/docs/Web/API/MIDIOutputMap)

Represents all of the available MIDI output ports.

[MIDIAccess](/en-US/docs/Web/API/MIDIAccess)

Provides the methods to list input and output devices, and to access an individual device.

[MIDIPort](/en-US/docs/Web/API/MIDIPort)

Represents an individual MIDI port.

[MIDIInput](/en-US/docs/Web/API/MIDIInput)

Provides a method for dealing with MIDI messages from an input port.

[MIDIOutput](/en-US/docs/Web/API/MIDIOutput)

Queues messages to the linked MIDI port. Messages can be sent immediately or after a specified delay.

[MIDIMessageEvent](/en-US/docs/Web/API/MIDIMessageEvent)

The event passed to the `MIDIInput`[midimessage](/en-US/docs/Web/API/MIDIInput/midimessage_event) event.

[MIDIConnectionEvent](/en-US/docs/Web/API/MIDIConnectionEvent)

The event passed to the `MIDIAccess`[statechange](/en-US/docs/Web/API/MIDIAccess/statechange_event) and `MIDIPort`[statechange](/en-US/docs/Web/API/MIDIPort/statechange_event) events, when a port becomes available or unavailable.

## [Security requirements](#security_requirements)

Access to the API is requested using the [navigator.requestMIDIAccess()](/en-US/docs/Web/API/Navigator/requestMIDIAccess) method.

- The method must be called in a [secure context](/en-US/docs/Web/Security/Defenses/Secure_Contexts).
- Access may be gated by the [midi](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/midi) HTTP [Permission Policy](/en-US/docs/Web/HTTP/Guides/Permissions_Policy).
- The user must explicitly grant permission to use the API through a user-agent specific mechanism, or have previously granted permission. Note that if access is denied by a permission policy it cannot be granted by a user permission.

The permission status can be queried using the [Permissions API](/en-US/docs/Web/API/Permissions_API) method [navigator.permissions.query()](/en-US/docs/Web/API/Permissions/query), passing a permission descriptor with the `midi` permission and (optional) `sysex` property:

js

```
navigator.permissions.query({ name: "midi", sysex: true }).then((result) => {
  if (result.state === "granted") {
    // Access granted.
  } else if (result.state === "prompt") {
    // Using API will prompt for permission
  }
  // Permission was denied by user prompt or permission policy
});
```

## [Examples](#examples)

### [Gaining access to the MIDI port](#gaining_access_to_the_midi_port)

The [navigator.requestMIDIAccess()](/en-US/docs/Web/API/Navigator/requestMIDIAccess) method returns a promise that resolves to a [MIDIAccess](/en-US/docs/Web/API/MIDIAccess) object, which can then be used to access a MIDI device. The method must be called in a secure context.

js

```
let midi = null; // global MIDIAccess object
function onMIDISuccess(midiAccess) {
  console.log("MIDI ready!");
  midi = midiAccess; // store in the global (in real usage, would probably keep in an object instance)
}

function onMIDIFailure(msg) {
  console.error(`Failed to get MIDI access - ${msg}`);
}

navigator.requestMIDIAccess().then(onMIDISuccess, onMIDIFailure);
```

### [Listing inputs and outputs](#listing_inputs_and_outputs)

In this example the list of input and output ports are retrieved and printed to the console.

js

```
function listInputsAndOutputs(midiAccess) {
  for (const entry of midiAccess.inputs) {
    const input = entry[1];
    console.log(
      `Input port [type:'${input.type}']` +
        ` id:'${input.id}'` +
        ` manufacturer:'${input.manufacturer}'` +
        ` name:'${input.name}'` +
        ` version:'${input.version}'`,
    );
  }

  for (const entry of midiAccess.outputs) {
    const output = entry[1];
    console.log(
      `Output port [type:'${output.type}'] id:'${output.id}' manufacturer:'${output.manufacturer}' name:'${output.name}' version:'${output.version}'`,
    );
  }
}
```

### [Handling MIDI Input](#handling_midi_input)

This example prints all MIDI input messages to the console.

js

```
function onMIDIMessage(event) {
  let str = `MIDI message received at timestamp ${event.timeStamp}[${event.data.length} bytes]: `;
  for (const character of event.data) {
    str += `0x${character.toString(16)} `;
  }
  console.log(str);
}

function startLoggingMIDIInput(midiAccess) {
  midiAccess.inputs.forEach((entry) => {
    entry.onmidimessage = onMIDIMessage;
  });
}
```

## [Specifications](#specifications)

Specification[Web MIDI API](https://webaudio.github.io/web-midi-api/)

## [Browser compatibility](#browser_compatibility)

### [api.Navigator.requestMIDIAccess](#api.Navigator.requestMIDIAccess)

### [http.headers.Permissions-Policy.midi](#http.headers.Permissions-Policy.midi)

### [api.Permissions.permission_midi](#api.Permissions.permission_midi)

## [See also](#see_also)

- [Introduction to Web MIDI](https://code.tutsplus.com/introduction-to-web-midi--cms-25220t)
- [Making Music in the Browser](https://www.keithmcmillen.com/blog/making-music-in-the-browser-web-midi-api/)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Web_MIDI_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/web_midi_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_MIDI_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fweb_midi_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_MIDI_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fweb_midi_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca26363fcc6fc861103d40ac0205e5c5b79eb2fa%0A*+Document+last+modified%3A+2025-11-30T02%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
