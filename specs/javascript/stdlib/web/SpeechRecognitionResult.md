# SpeechRecognitionResult

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSpeechRecognitionResult&level=not)

The `SpeechRecognitionResult` interface of the [Web Speech API](/en-US/docs/Web/API/Web_Speech_API) represents a single recognition match, which may contain multiple [SpeechRecognitionAlternative](/en-US/docs/Web/API/SpeechRecognitionAlternative) objects.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[SpeechRecognitionResult.isFinal](/en-US/docs/Web/API/SpeechRecognitionResult/isFinal)Read only

A boolean value that states whether this result is final (true) or not (false) — if so, then this is the final time this result will be returned; if not, then this result is an interim result, and may be updated later on.

[SpeechRecognitionResult.length](/en-US/docs/Web/API/SpeechRecognitionResult/length)Read only

Returns the length of the "array" — the number of [SpeechRecognitionAlternative](/en-US/docs/Web/API/SpeechRecognitionAlternative) objects contained in the result (also referred to as "n-best alternatives".)

## [Instance methods](#instance_methods)

[SpeechRecognitionResult.item](/en-US/docs/Web/API/SpeechRecognitionResult/item)

A standard getter that allows [SpeechRecognitionAlternative](/en-US/docs/Web/API/SpeechRecognitionAlternative) objects within the result to be accessed via array syntax.

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
[Web Speech API# speechreco-result](https://webaudio.github.io/web-speech-api/#speechreco-result)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Web Speech API](/en-US/docs/Web/API/Web_Speech_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SpeechRecognitionResult/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/speechrecognitionresult/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSpeechRecognitionResult&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fspeechrecognitionresult%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSpeechRecognitionResult%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fspeechrecognitionresult%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0a00e01a8c8097ea9786710c3fc703d18f0af951%0A*+Document+last+modified%3A+2025-09-30T15%3A42%3A24.000Z%0A%0A%3C%2Fdetails%3E)
