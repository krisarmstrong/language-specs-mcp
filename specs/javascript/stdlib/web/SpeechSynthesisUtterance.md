# SpeechSynthesisUtterance

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2018⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSpeechSynthesisUtterance&level=high)

The `SpeechSynthesisUtterance` interface of the [Web Speech API](/en-US/docs/Web/API/Web_Speech_API) represents a speech request. It contains the content the speech service should read and information about how to read it (e.g., language, pitch and volume.)

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[SpeechSynthesisUtterance()](/en-US/docs/Web/API/SpeechSynthesisUtterance/SpeechSynthesisUtterance)

Returns a new `SpeechSynthesisUtterance` object instance.

## [Instance properties](#instance_properties)

`SpeechSynthesisUtterance` also inherits properties from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[SpeechSynthesisUtterance.lang](/en-US/docs/Web/API/SpeechSynthesisUtterance/lang)

Gets and sets the language of the utterance.

[SpeechSynthesisUtterance.pitch](/en-US/docs/Web/API/SpeechSynthesisUtterance/pitch)

Gets and sets the pitch at which the utterance will be spoken at.

[SpeechSynthesisUtterance.rate](/en-US/docs/Web/API/SpeechSynthesisUtterance/rate)

Gets and sets the speed at which the utterance will be spoken at.

[SpeechSynthesisUtterance.text](/en-US/docs/Web/API/SpeechSynthesisUtterance/text)

Gets and sets the text that will be synthesized when the utterance is spoken.

[SpeechSynthesisUtterance.voice](/en-US/docs/Web/API/SpeechSynthesisUtterance/voice)

Gets and sets the voice that will be used to speak the utterance.

[SpeechSynthesisUtterance.volume](/en-US/docs/Web/API/SpeechSynthesisUtterance/volume)

Gets and sets the volume that the utterance will be spoken at.

## [Events](#events)

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface.

[boundary](/en-US/docs/Web/API/SpeechSynthesisUtterance/boundary_event)

Fired when the spoken utterance reaches a word or sentence boundary. Also available via the `onboundary` property.

[end](/en-US/docs/Web/API/SpeechSynthesisUtterance/end_event)

Fired when the utterance has finished being spoken. Also available via the `onend` property.

[error](/en-US/docs/Web/API/SpeechSynthesisUtterance/error_event)

Fired when an error occurs that prevents the utterance from being successfully spoken. Also available via the `onerror` property

[mark](/en-US/docs/Web/API/SpeechSynthesisUtterance/mark_event)

Fired when the spoken utterance reaches a named SSML "mark" tag. Also available via the `onmark` property.

[pause](/en-US/docs/Web/API/SpeechSynthesisUtterance/pause_event)

Fired when the utterance is paused part way through. Also available via the `onpause` property.

[resume](/en-US/docs/Web/API/SpeechSynthesisUtterance/resume_event)

Fired when a paused utterance is resumed. Also available via the `onresume` property.

[start](/en-US/docs/Web/API/SpeechSynthesisUtterance/start_event)

Fired when the utterance has begun to be spoken. Also available via the `onstart` property.

## [Examples](#examples)

In our basic [Speech synthesizer demo](https://mdn.github.io/dom-examples/web-speech-api/speak-easy-synthesis/), we first grab a reference to the SpeechSynthesis controller using `window.speechSynthesis`. After defining some necessary variables, we retrieve a list of the voices available using [SpeechSynthesis.getVoices()](/en-US/docs/Web/API/SpeechSynthesis/getVoices) and populate a select menu with them so the user can choose what voice they want.

Inside the `inputForm.onsubmit` handler, we stop the form submitting with [preventDefault()](/en-US/docs/Web/API/Event/preventDefault), use the [constructor](/en-US/docs/Web/API/SpeechSynthesisUtterance/SpeechSynthesisUtterance) to create a new utterance instance containing the text from the text [<input>](/en-US/docs/Web/HTML/Reference/Elements/input), set the utterance's [voice](/en-US/docs/Web/API/SpeechSynthesisUtterance/voice) to the voice selected in the [<select>](/en-US/docs/Web/HTML/Reference/Elements/select) element, and start the utterance speaking via the [SpeechSynthesis.speak()](/en-US/docs/Web/API/SpeechSynthesis/speak) method.

js

```
const synth = window.speechSynthesis;

const inputForm = document.querySelector("form");
const inputTxt = document.querySelector("input");
const voiceSelect = document.querySelector("select");

let voices;

function loadVoices() {
  voices = synth.getVoices();
  for (const [i, voice] of voices.entries()) {
    const option = document.createElement("option");
    option.textContent = `${voice.name} (${voice.lang})`;
    option.value = i;
    voiceSelect.appendChild(option);
  }
}

// in Google Chrome the voices are not ready on page load
if ("onvoiceschanged" in synth) {
  synth.onvoiceschanged = loadVoices;
} else {
  loadVoices();
}

inputForm.onsubmit = (event) => {
  event.preventDefault();

  const utterThis = new SpeechSynthesisUtterance(inputTxt.value);
  utterThis.voice = voices[voiceSelect.value];
  synth.speak(utterThis);
  inputTxt.blur();
};
```

## [Specifications](#specifications)

Specification
[Web Speech API# speechsynthesisutterance](https://webaudio.github.io/web-speech-api/#speechsynthesisutterance)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Web Speech API](/en-US/docs/Web/API/Web_Speech_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SpeechSynthesisUtterance/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/speechsynthesisutterance/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSpeechSynthesisUtterance&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fspeechsynthesisutterance%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSpeechSynthesisUtterance%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fspeechsynthesisutterance%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb5437b737639d6952d18b95ebd1045ed73e4bfa7%0A*+Document+last+modified%3A+2025-05-27T11%3A11%3A59.000Z%0A%0A%3C%2Fdetails%3E)
