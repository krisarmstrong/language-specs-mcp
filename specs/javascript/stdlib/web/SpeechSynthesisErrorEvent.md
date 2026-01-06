# SpeechSynthesisErrorEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨October 2018⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSpeechSynthesisErrorEvent&level=high)

The `SpeechSynthesisErrorEvent` interface of the [Web Speech API](/en-US/docs/Web/API/Web_Speech_API) contains information about any errors that occur while processing [SpeechSynthesisUtterance](/en-US/docs/Web/API/SpeechSynthesisUtterance) objects in the speech service.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[SpeechSynthesisErrorEvent()](/en-US/docs/Web/API/SpeechSynthesisErrorEvent/SpeechSynthesisErrorEvent)

Creates a new `SpeechSynthesisErrorEvent`.

## [Instance properties](#instance_properties)

`SpeechSynthesisErrorEvent` extends the [SpeechSynthesisEvent](/en-US/docs/Web/API/SpeechSynthesisEvent) interface, which inherits properties from its parent interface, [Event](/en-US/docs/Web/API/Event).

[SpeechSynthesisErrorEvent.error](/en-US/docs/Web/API/SpeechSynthesisErrorEvent/error)Read only

Returns an error code indicating what has gone wrong with a speech synthesis attempt.

## [Instance methods](#instance_methods)

`SpeechSynthesisErrorEvent` extends the [SpeechSynthesisEvent](/en-US/docs/Web/API/SpeechSynthesisEvent) interface, which inherits methods from its parent interface, [Event](/en-US/docs/Web/API/Event).

## [Examples](#examples)

js

```
const synth = window.speechSynthesis;

const inputForm = document.querySelector("form");
const inputTxt = document.querySelector("input");
const voiceSelect = document.querySelector("select");

const voices = synth.getVoices();

// …

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

  synth.speak(utterThis);

  utterThis.onerror = (event) => {
    console.log(
      `An error has occurred with the speech synthesis: ${event.error}`,
    );
  };

  inputTxt.blur();
};
```

## [Specifications](#specifications)

Specification
[Web Speech API# speechsynthesiserrorevent](https://webaudio.github.io/web-speech-api/#speechsynthesiserrorevent)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Web Speech API](/en-US/docs/Web/API/Web_Speech_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SpeechSynthesisErrorEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/speechsynthesiserrorevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSpeechSynthesisErrorEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fspeechsynthesiserrorevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSpeechSynthesisErrorEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fspeechsynthesiserrorevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb5437b737639d6952d18b95ebd1045ed73e4bfa7%0A*+Document+last+modified%3A+2025-05-27T11%3A11%3A59.000Z%0A%0A%3C%2Fdetails%3E)
