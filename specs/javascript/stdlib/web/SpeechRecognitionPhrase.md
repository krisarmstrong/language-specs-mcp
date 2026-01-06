# SpeechRecognitionPhrase

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `SpeechRecognitionPhrase` interface of the [Web Speech API](/en-US/docs/Web/API/Web_Speech_API) represents a phrase that can be passed to the speech recognition engine for [contextual biasing](/en-US/docs/Web/API/Web_Speech_API/Using_the_Web_Speech_API#contextual_biasing_in_speech_recognition).

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[SpeechRecognitionPhrase.boost](/en-US/docs/Web/API/SpeechRecognitionPhrase/boost)Read onlyExperimental

A floating point number representing the amount of boost you want to apply to the corresponding `phrase`.

[SpeechRecognitionPhrase.phrase](/en-US/docs/Web/API/SpeechRecognitionPhrase/phrase)Read onlyExperimental

A string containing the word or phrase you want boosted in the recognition engine's bias.

## [Examples](#examples)

### [Basic usage](#basic_usage)

The following code first creates an array containing the phrases to boost and their [boost](/en-US/docs/Web/API/SpeechRecognitionPhrase/boost) values. We convert this data into an `ObservableArray` of `SpeechRecognitionPhrase` objects by mapping the original array elements to [SpeechRecognitionPhrase()](/en-US/docs/Web/API/SpeechRecognitionPhrase/SpeechRecognitionPhrase) constructor calls:

js

```
const phraseData = [
  { phrase: "azure", boost: 5.0 },
  { phrase: "khaki", boost: 3.0 },
  { phrase: "tan", boost: 2.0 },
];

const phraseObjects = phraseData.map(
  (p) => new SpeechRecognitionPhrase(p.phrase, p.boost),
);
```

After creating a [SpeechRecognition](/en-US/docs/Web/API/SpeechRecognition) instance, we add our contextual biasing phrases by setting the `phraseObjects` array as the value of the [SpeechRecognition.phrases](/en-US/docs/Web/API/SpeechRecognition/phrases) property:

js

```
const recognition = new SpeechRecognition();
recognition.continuous = false;
recognition.lang = "en-US";
recognition.interimResults = false;
recognition.processLocally = true;
recognition.phrases = phraseObjects;

// …
```

This code is excerpted from our [on-device speech color changer](https://github.com/mdn/dom-examples/tree/main/web-speech-api/on-device-speech-color-changer) ([run the demo live](https://mdn.github.io/dom-examples/web-speech-api/on-device-speech-color-changer/)). See [Using the Web Speech API](/en-US/docs/Web/API/Web_Speech_API/Using_the_Web_Speech_API) for a full explanation.

## [Specifications](#specifications)

Specification
[Web Speech API# speechrecognitionphrase](https://webaudio.github.io/web-speech-api/#speechrecognitionphrase)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Web Speech API](/en-US/docs/Web/API/Web_Speech_API)
- [SpeechRecognition.phrases](/en-US/docs/Web/API/SpeechRecognition/phrases)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SpeechRecognitionPhrase/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/speechrecognitionphrase/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSpeechRecognitionPhrase&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fspeechrecognitionphrase%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSpeechRecognitionPhrase%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fspeechrecognitionphrase%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F11478c4adedc859a4fe3e3c4004fcfd96ebc1eba%0A*+Document+last+modified%3A+2025-09-30T23%3A55%3A41.000Z%0A%0A%3C%2Fdetails%3E)
