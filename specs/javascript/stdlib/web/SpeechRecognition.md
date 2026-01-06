# SpeechRecognition

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSpeechRecognition&level=not)

The `SpeechRecognition` interface of the [Web Speech API](/en-US/docs/Web/API/Web_Speech_API) is the controller interface for the recognition service; this also handles the [SpeechRecognitionEvent](/en-US/docs/Web/API/SpeechRecognitionEvent) sent from the recognition service.

Note: On some browsers, like Chrome, using Speech Recognition on a web page involves a server-based recognition engine. Your audio is sent to a web service for recognition processing, so it won't work offline.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[SpeechRecognition()](/en-US/docs/Web/API/SpeechRecognition/SpeechRecognition)

Creates a new `SpeechRecognition` object.

## [Instance properties](#instance_properties)

`SpeechRecognition` also inherits properties from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[SpeechRecognition.lang](/en-US/docs/Web/API/SpeechRecognition/lang)

Returns and sets the language of the current `SpeechRecognition`. If not specified, this defaults to the HTML [lang](/en-US/docs/Web/HTML/Reference/Global_attributes/lang) attribute value, or the user agent's language setting if that isn't set either.

[SpeechRecognition.continuous](/en-US/docs/Web/API/SpeechRecognition/continuous)

Controls whether continuous results are returned for each recognition, or only a single result. Defaults to single (`false`.)

[SpeechRecognition.interimResults](/en-US/docs/Web/API/SpeechRecognition/interimResults)

Controls whether interim results should be returned (`true`) or not (`false`.) Interim results are results that are not yet final (e.g., the [SpeechRecognitionResult.isFinal](/en-US/docs/Web/API/SpeechRecognitionResult/isFinal) property is `false`.)

[SpeechRecognition.maxAlternatives](/en-US/docs/Web/API/SpeechRecognition/maxAlternatives)

Sets the maximum number of [SpeechRecognitionAlternative](/en-US/docs/Web/API/SpeechRecognitionAlternative)s provided per result. The default value is 1.

[SpeechRecognition.phrases](/en-US/docs/Web/API/SpeechRecognition/phrases)Experimental

Sets an array of [SpeechRecognitionPhrase](/en-US/docs/Web/API/SpeechRecognitionPhrase) objects to be used for [contextual biasing](/en-US/docs/Web/API/Web_Speech_API/Using_the_Web_Speech_API#contextual_biasing_in_speech_recognition).

[SpeechRecognition.processLocally](/en-US/docs/Web/API/SpeechRecognition/processLocally)Experimental

Specifies whether speech recognition must be performed locally on the user's device.

### [Deprecated properties](#deprecated_properties)

The concept of grammar has been removed from the Web Speech API. Related features remain in the specification and are still recognized by supporting browsers for backwards compatibility, but they have no effect on speech recognition services.

[SpeechRecognition.grammars](/en-US/docs/Web/API/SpeechRecognition/grammars)

Returns and sets a collection of [SpeechGrammar](/en-US/docs/Web/API/SpeechGrammar) objects that represent the grammars understood by the current `SpeechRecognition`.

## [Static methods](#static_methods)

[SpeechRecognition.available()](/en-US/docs/Web/API/SpeechRecognition/available_static)Experimental

Checks whether the specified languages are available for speech recognition.

[SpeechRecognition.install()](/en-US/docs/Web/API/SpeechRecognition/install_static)Experimental

Installs the required language packs for on-device speech recognition in the specified languages.

## [Instance methods](#instance_methods)

`SpeechRecognition` also inherits methods from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[SpeechRecognition.abort()](/en-US/docs/Web/API/SpeechRecognition/abort)

Stops the speech recognition service from listening to incoming audio, and doesn't attempt to return a [SpeechRecognitionResult](/en-US/docs/Web/API/SpeechRecognitionResult).

[SpeechRecognition.start()](/en-US/docs/Web/API/SpeechRecognition/start)

Starts the speech recognition service to listen for incoming audio (from a microphone or an audio track) and returns the results of that recognition.

[SpeechRecognition.stop()](/en-US/docs/Web/API/SpeechRecognition/stop)

Stops the speech recognition service from listening for incoming audio and attempts to return a [SpeechRecognitionResult](/en-US/docs/Web/API/SpeechRecognitionResult) based on the results captured so far.

## [Events](#events)

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface.

[audiostart](/en-US/docs/Web/API/SpeechRecognition/audiostart_event)

Fired when the user agent has started to capture audio.

[audioend](/en-US/docs/Web/API/SpeechRecognition/audioend_event)

Fired when the user agent has finished capturing audio.

[end](/en-US/docs/Web/API/SpeechRecognition/end_event)

Fired when the speech recognition service has disconnected.

[error](/en-US/docs/Web/API/SpeechRecognition/error_event)

Fired when a speech recognition error occurs.

[nomatch](/en-US/docs/Web/API/SpeechRecognition/nomatch_event)

Fired when the speech recognition service returns a final result with no significant recognition. This may involve some degree of recognition, which doesn't meet or exceed the [confidence](/en-US/docs/Web/API/SpeechRecognitionAlternative/confidence) threshold.

[result](/en-US/docs/Web/API/SpeechRecognition/result_event)

Fired when the speech recognition service returns a result — a word or phrase has been positively recognized and this has been communicated back to the app.

[soundstart](/en-US/docs/Web/API/SpeechRecognition/soundstart_event)

Fired when any sound — recognizable speech or not — has been detected.

[soundend](/en-US/docs/Web/API/SpeechRecognition/soundend_event)

Fired when any sound — recognizable speech or not — has stopped being detected.

[speechstart](/en-US/docs/Web/API/SpeechRecognition/speechstart_event)

Fired when sound that is recognized by the speech recognition service as speech has been detected.

[speechend](/en-US/docs/Web/API/SpeechRecognition/speechend_event)

Fired when speech recognized by the speech recognition service has stopped being detected.

[start](/en-US/docs/Web/API/SpeechRecognition/start_event)

Fired when the speech recognition service begins listening for audio to recognize.

## [Examples](#examples)

In our [Speech color changer](https://mdn.github.io/dom-examples/web-speech-api/speech-color-changer/) example, we create a new `SpeechRecognition` object instance using the [SpeechRecognition()](/en-US/docs/Web/API/SpeechRecognition/SpeechRecognition) constructor.

After some other values have been defined, we then set it so that the recognition service starts when a button is clicked (see [SpeechRecognition.start()](/en-US/docs/Web/API/SpeechRecognition/start)). When a result has been successfully recognized, the [result](/en-US/docs/Web/API/SpeechRecognition/result_event) event fires, we extract the color that was spoken from the event object, and then set the background color of the [<html>](/en-US/docs/Web/HTML/Reference/Elements/html) element to that color.

js

```
const recognition = new SpeechRecognition();
recognition.continuous = false;
recognition.lang = "en-US";
recognition.interimResults = false;
recognition.maxAlternatives = 1;

const diagnostic = document.querySelector(".output");
const bg = document.querySelector("html");
const startBtn = document.querySelector("button");

startBtn.onclick = () => {
  recognition.start();
  console.log("Ready to receive a color command.");
};

recognition.onresult = (event) => {
  const color = event.results[0][0].transcript;
  diagnostic.textContent = `Result received: ${color}`;
  bg.style.backgroundColor = color;
};
```

## [Specifications](#specifications)

Specification
[Web Speech API# speechreco-section](https://webaudio.github.io/web-speech-api/#speechreco-section)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Web Speech API](/en-US/docs/Web/API/Web_Speech_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 1, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SpeechRecognition/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/speechrecognition/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSpeechRecognition&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fspeechrecognition%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSpeechRecognition%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fspeechrecognition%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6ba4f3b350be482ba22726f31bbcf8ad3c92a9c6%0A*+Document+last+modified%3A+2025-10-01T13%3A56%3A32.000Z%0A%0A%3C%2Fdetails%3E)
