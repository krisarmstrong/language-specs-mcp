# SpeechSynthesis

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2018⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSpeechSynthesis&level=high)

The `SpeechSynthesis` interface of the [Web Speech API](/en-US/docs/Web/API/Web_Speech_API) is the controller interface for the speech service; this can be used to retrieve information about the synthesis voices available on the device, start and pause speech, and other commands besides.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

`SpeechSynthesis` also inherits properties from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[SpeechSynthesis.paused](/en-US/docs/Web/API/SpeechSynthesis/paused)Read only

A boolean value that returns `true` if the `SpeechSynthesis` object is in a paused state.

[SpeechSynthesis.pending](/en-US/docs/Web/API/SpeechSynthesis/pending)Read only

A boolean value that returns `true` if the utterance queue contains as-yet-unspoken utterances.

[SpeechSynthesis.speaking](/en-US/docs/Web/API/SpeechSynthesis/speaking)Read only

A boolean value that returns `true` if an utterance is currently in the process of being spoken — even if `SpeechSynthesis` is in a paused state.

## [Instance methods](#instance_methods)

`SpeechSynthesis` also inherits methods from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[SpeechSynthesis.cancel()](/en-US/docs/Web/API/SpeechSynthesis/cancel)

Removes all utterances from the utterance queue.

[SpeechSynthesis.getVoices()](/en-US/docs/Web/API/SpeechSynthesis/getVoices)

Returns a list of [SpeechSynthesisVoice](/en-US/docs/Web/API/SpeechSynthesisVoice) objects representing all the available voices on the current device.

[SpeechSynthesis.pause()](/en-US/docs/Web/API/SpeechSynthesis/pause)

Puts the `SpeechSynthesis` object into a paused state.

[SpeechSynthesis.resume()](/en-US/docs/Web/API/SpeechSynthesis/resume)

Puts the `SpeechSynthesis` object into a non-paused state: resumes it if it was already paused.

[SpeechSynthesis.speak()](/en-US/docs/Web/API/SpeechSynthesis/speak)

Adds an [utterance](/en-US/docs/Web/API/SpeechSynthesisUtterance) to the utterance queue; it will be spoken when any other utterances queued before it have been spoken.

## [Events](#events)

Listen to this event using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface.

[voiceschanged](/en-US/docs/Web/API/SpeechSynthesis/voiceschanged_event)

Fired when the list of [SpeechSynthesisVoice](/en-US/docs/Web/API/SpeechSynthesisVoice) objects that would be returned by the [SpeechSynthesis.getVoices()](/en-US/docs/Web/API/SpeechSynthesis/getVoices) method has changed. Also available via the `onvoiceschanged` property.

## [Examples](#examples)

First, an example:

js

```
let utterance = new SpeechSynthesisUtterance("Hello world!");
speechSynthesis.speak(utterance);
```

Now we'll look at a more fully-fledged example. In our [Speech synthesizer demo](https://github.com/mdn/dom-examples/tree/main/web-speech-api/speak-easy-synthesis), we first grab a reference to the SpeechSynthesis controller using `window.speechSynthesis`. After defining some necessary variables, we retrieve a list of the voices available using [SpeechSynthesis.getVoices()](/en-US/docs/Web/API/SpeechSynthesis/getVoices) and populate a select menu with them so the user can choose what voice they want.

Inside the `inputForm.onsubmit` handler, we stop the form submitting with [preventDefault()](/en-US/docs/Web/API/Event/preventDefault), create a new [SpeechSynthesisUtterance](/en-US/docs/Web/API/SpeechSynthesisUtterance) instance containing the text from the text [<input>](/en-US/docs/Web/HTML/Reference/Elements/input), set the utterance's voice to the voice selected in the [<select>](/en-US/docs/Web/HTML/Reference/Elements/select) element, and start the utterance speaking via the [SpeechSynthesis.speak()](/en-US/docs/Web/API/SpeechSynthesis/speak) method.

js

```
const synth = window.speechSynthesis;

const inputForm = document.querySelector("form");
const inputTxt = document.querySelector(".txt");
const voiceSelect = document.querySelector("select");
const pitch = document.querySelector("#pitch");
const pitchValue = document.querySelector(".pitch-value");
const rate = document.querySelector("#rate");
const rateValue = document.querySelector(".rate-value");

let voices = [];

function populateVoiceList() {
  voices = synth.getVoices();

  for (const voice of voices) {
    const option = document.createElement("option");
    option.textContent = `${voice.name} (${voice.lang})`;

    if (voice.default) {
      option.textContent += " — DEFAULT";
    }

    option.setAttribute("data-lang", voice.lang);
    option.setAttribute("data-name", voice.name);
    voiceSelect.appendChild(option);
  }
}

populateVoiceList();
if (speechSynthesis.onvoiceschanged !== undefined) {
  speechSynthesis.onvoiceschanged = populateVoiceList;
}

inputForm.onsubmit = (event) => {
  event.preventDefault();

  const utterThis = new SpeechSynthesisUtterance(inputTxt.value);
  const selectedOption =
    voiceSelect.selectedOptions[0].getAttribute("data-name");
  for (const voice of voices) {
    if (voice.name === selectedOption) {
      utterThis.voice = voice;
    }
  }
  utterThis.pitch = pitch.value;
  utterThis.rate = rate.value;
  synth.speak(utterThis);

  inputTxt.blur();
};
```

## [Specifications](#specifications)

Specification
[Web Speech API# tts-section](https://webaudio.github.io/web-speech-api/#tts-section)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Web Speech API](/en-US/docs/Web/API/Web_Speech_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SpeechSynthesis/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/speechsynthesis/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSpeechSynthesis&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fspeechsynthesis%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSpeechSynthesis%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fspeechsynthesis%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb5437b737639d6952d18b95ebd1045ed73e4bfa7%0A*+Document+last+modified%3A+2025-05-27T11%3A11%3A59.000Z%0A%0A%3C%2Fdetails%3E)
