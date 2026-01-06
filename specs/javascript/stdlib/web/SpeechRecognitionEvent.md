# SpeechRecognitionEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSpeechRecognitionEvent&level=not)

The `SpeechRecognitionEvent` interface of the [Web Speech API](/en-US/docs/Web/API/Web_Speech_API) represents the event object for the [result](/en-US/docs/Web/API/SpeechRecognition/result_event) and [nomatch](/en-US/docs/Web/API/SpeechRecognition/nomatch_event) events, and contains all the data associated with an interim or final speech recognition result.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[SpeechRecognitionEvent()](/en-US/docs/Web/API/SpeechRecognitionEvent/SpeechRecognitionEvent)

Creates a new `SpeechRecognitionEvent` object.

## [Instance properties](#instance_properties)

`SpeechRecognitionEvent` also inherits properties from its parent interface, [Event](/en-US/docs/Web/API/Event).

[SpeechRecognitionEvent.resultIndex](/en-US/docs/Web/API/SpeechRecognitionEvent/resultIndex)Read only

Returns the lowest index value result in the [SpeechRecognitionResultList](/en-US/docs/Web/API/SpeechRecognitionResultList) "array" that has actually changed.

[SpeechRecognitionEvent.results](/en-US/docs/Web/API/SpeechRecognitionEvent/results)Read only

Returns a [SpeechRecognitionResultList](/en-US/docs/Web/API/SpeechRecognitionResultList) object representing all the speech recognition results for the current session.

## [Examples](#examples)

This code is excerpted from our [Speech color changer](https://github.com/mdn/dom-examples/blob/main/web-speech-api/speech-color-changer/script.js) example.

js

```
recognition.onresult = (event) => {
  const color = event.results[0][0].transcript;
  diagnostic.textContent = `Result received: ${color}.`;
  bg.style.backgroundColor = color;
};
```

## [Specifications](#specifications)

Specification
[Web Speech API# speechreco-event](https://webaudio.github.io/web-speech-api/#speechreco-event)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Web Speech API](/en-US/docs/Web/API/Web_Speech_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SpeechRecognitionEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/speechrecognitionevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSpeechRecognitionEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fspeechrecognitionevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSpeechRecognitionEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fspeechrecognitionevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0a00e01a8c8097ea9786710c3fc703d18f0af951%0A*+Document+last+modified%3A+2025-09-30T15%3A42%3A24.000Z%0A%0A%3C%2Fdetails%3E)
