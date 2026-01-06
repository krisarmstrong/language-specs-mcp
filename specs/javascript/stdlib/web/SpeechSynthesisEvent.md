# SpeechSynthesisEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2018⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSpeechSynthesisEvent&level=high)

The `SpeechSynthesisEvent` interface of the [Web Speech API](/en-US/docs/Web/API/Web_Speech_API) contains information about the current state of [SpeechSynthesisUtterance](/en-US/docs/Web/API/SpeechSynthesisUtterance) objects that have been processed in the speech service.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[SpeechSynthesisEvent()](/en-US/docs/Web/API/SpeechSynthesisEvent/SpeechSynthesisEvent)

Creates a new `SpeechSynthesisEvent`.

## [Instance properties](#instance_properties)

The `SpeechSynthesisEvent` interface also inherits properties from its parent interface, [Event](/en-US/docs/Web/API/Event).

[SpeechSynthesisEvent.charIndex](/en-US/docs/Web/API/SpeechSynthesisEvent/charIndex)Read only

Returns the index position of the character in the [SpeechSynthesisUtterance.text](/en-US/docs/Web/API/SpeechSynthesisUtterance/text) that was being spoken when the event was triggered.

[SpeechSynthesisEvent.charLength](/en-US/docs/Web/API/SpeechSynthesisEvent/charLength)Read only

Returns the number of characters left to be spoken after the `charIndex` position, if the speaking engine supports it. Returns 0 if the speaking engine can't provide the information.

[SpeechSynthesisEvent.elapsedTime](/en-US/docs/Web/API/SpeechSynthesisEvent/elapsedTime)Read only

Returns the elapsed time in seconds after the [SpeechSynthesisUtterance.text](/en-US/docs/Web/API/SpeechSynthesisUtterance/text) started being spoken that the event was triggered at.

[SpeechSynthesisEvent.name](/en-US/docs/Web/API/SpeechSynthesisEvent/name)Read only

Returns the name associated with certain types of events occurring as the [SpeechSynthesisUtterance.text](/en-US/docs/Web/API/SpeechSynthesisUtterance/text) is being spoken: the name of the [SSML](https://www.w3.org/TR/speech-synthesis/#S3.3.2) marker reached in the case of a [mark](/en-US/docs/Web/API/SpeechSynthesisUtterance/mark_event) event, or the type of boundary reached in the case of a [boundary](/en-US/docs/Web/API/SpeechSynthesisUtterance/boundary_event) event.

[SpeechSynthesisEvent.utterance](/en-US/docs/Web/API/SpeechSynthesisEvent/utterance)Read only

Returns the [SpeechSynthesisUtterance](/en-US/docs/Web/API/SpeechSynthesisUtterance) instance that the event was triggered on.

## [Instance methods](#instance_methods)

The `SpeechSynthesisEvent` interface also inherits methods from its parent interface, [Event](/en-US/docs/Web/API/Event).

## [Examples](#examples)

js

```
utterThis.onpause = (event) => {
  const char = event.utterance.text.charAt(event.charIndex);
  console.log(
    `Speech paused at character ${event.charIndex} of "${event.utterance.text}", which is "${char}".`,
  );
};

utterThis.onboundary = (event) => {
  console.log(
    `${event.name} boundary reached after ${event.elapsedTime} seconds.`,
  );
};
```

## [Specifications](#specifications)

Specification
[Web Speech API# speechsynthesisevent](https://webaudio.github.io/web-speech-api/#speechsynthesisevent)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Web Speech API](/en-US/docs/Web/API/Web_Speech_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 24, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/SpeechSynthesisEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/speechsynthesisevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSpeechSynthesisEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fspeechsynthesisevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSpeechSynthesisEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fspeechsynthesisevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F32305cc3cf274fbfdcc73a296bbd400a26f38296%0A*+Document+last+modified%3A+2024-07-24T20%3A47%3A46.000Z%0A%0A%3C%2Fdetails%3E)
