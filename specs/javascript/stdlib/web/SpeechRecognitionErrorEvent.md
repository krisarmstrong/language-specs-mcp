# SpeechRecognitionErrorEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSpeechRecognitionErrorEvent&level=not)

The `SpeechRecognitionErrorEvent` interface of the [Web Speech API](/en-US/docs/Web/API/Web_Speech_API) represents error messages from the recognition service.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[SpeechRecognitionErrorEvent()](/en-US/docs/Web/API/SpeechRecognitionErrorEvent/SpeechRecognitionErrorEvent)

Creates a new `SpeechRecognitionErrorEvent` object.

## [Instance properties](#instance_properties)

`SpeechRecognitionErrorEvent` also inherits properties from its parent interface, [Event](/en-US/docs/Web/API/Event).

[SpeechRecognitionErrorEvent.error](/en-US/docs/Web/API/SpeechRecognitionErrorEvent/error)Read only

Returns the type of error raised.

[SpeechRecognitionErrorEvent.message](/en-US/docs/Web/API/SpeechRecognitionErrorEvent/message)Read only

Returns a message describing the error in more detail.

## [Examples](#examples)

js

```
const recognition = new SpeechRecognition();

recognition.onerror = (event) => {
  console.log(`Speech recognition error detected: ${event.error}`);
  console.log(`Additional information: ${event.message}`);
};
```

## [Specifications](#specifications)

Specification
[Web Speech API# speechrecognitionerrorevent](https://webaudio.github.io/web-speech-api/#speechrecognitionerrorevent)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Web Speech API](/en-US/docs/Web/API/Web_Speech_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SpeechRecognitionErrorEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/speechrecognitionerrorevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSpeechRecognitionErrorEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fspeechrecognitionerrorevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSpeechRecognitionErrorEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fspeechrecognitionerrorevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0a00e01a8c8097ea9786710c3fc703d18f0af951%0A*+Document+last+modified%3A+2025-09-30T15%3A42%3A24.000Z%0A%0A%3C%2Fdetails%3E)
