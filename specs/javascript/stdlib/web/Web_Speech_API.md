# Web Speech API

The Web Speech API enables you to incorporate voice data into web apps. The Web Speech API has two parts: `SpeechSynthesis` (Text-to-Speech), and `SpeechRecognition` (Asynchronous Speech Recognition.)

## In this article

- [Web speech concepts and usage](#web_speech_concepts_and_usage)
- [Web Speech API Interfaces](#web_speech_api_interfaces)
- [Errors](#errors)
- [Security considerations](#security_considerations)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Web speech concepts and usage](#web_speech_concepts_and_usage)

The Web Speech API enables web apps to handle voice data. It has two components:

- Speech recognition is accessed via the [SpeechRecognition](/en-US/docs/Web/API/SpeechRecognition) interface, which provides the ability to recognize voice context from an audio source and allows your app to respond appropriately. Generally, you use the interface's constructor to create a new [SpeechRecognition](/en-US/docs/Web/API/SpeechRecognition) object. This object provides a number of event handlers to detect when speech is incoming from the device's microphone (or from an audio track). You can specify whether you want the speech recognition to use a service provided by the user's platform (the default) or be performed [locally in the browser](/en-US/docs/Web/API/Web_Speech_API/Using_the_Web_Speech_API#on-device_speech_recognition).
- Speech synthesis is accessed via the [SpeechSynthesis](/en-US/docs/Web/API/SpeechSynthesis) interface, a text-to-speech component that allows programs to read out their text content (normally via the device's default speech synthesizer.) Different voice types are represented by [SpeechSynthesisVoice](/en-US/docs/Web/API/SpeechSynthesisVoice) objects, and different parts of text that you want to be spoken are represented by [SpeechSynthesisUtterance](/en-US/docs/Web/API/SpeechSynthesisUtterance) objects. You can get these spoken by passing them to the [SpeechSynthesis.speak()](/en-US/docs/Web/API/SpeechSynthesis/speak) method.

For more details on using these features, see [Using the Web Speech API](/en-US/docs/Web/API/Web_Speech_API/Using_the_Web_Speech_API).

## [Web Speech API Interfaces](#web_speech_api_interfaces)

### [Speech recognition](#speech_recognition)

[SpeechRecognition](/en-US/docs/Web/API/SpeechRecognition)

The controller interface for the recognition service; this also handles the [SpeechRecognitionEvent](/en-US/docs/Web/API/SpeechRecognitionEvent) sent from the recognition service.

[SpeechRecognitionAlternative](/en-US/docs/Web/API/SpeechRecognitionAlternative)

Represents a single word that has been recognized by the speech recognition service.

[SpeechRecognitionErrorEvent](/en-US/docs/Web/API/SpeechRecognitionErrorEvent)

Represents error messages from the recognition service.

[SpeechRecognitionEvent](/en-US/docs/Web/API/SpeechRecognitionEvent)

The event object for the [result](/en-US/docs/Web/API/SpeechRecognition/result_event) and [nomatch](/en-US/docs/Web/API/SpeechRecognition/nomatch_event) events, and contains all the data associated with an interim or final speech recognition result.

[SpeechRecognitionPhrase](/en-US/docs/Web/API/SpeechRecognitionPhrase)

Represents a phrase that can be passed into the speech recognition engine to be used for [contextual biasing](/en-US/docs/Web/API/Web_Speech_API/Using_the_Web_Speech_API#contextual_biasing_in_speech_recognition).

[SpeechRecognitionResult](/en-US/docs/Web/API/SpeechRecognitionResult)

Represents a single recognition match, which may contain multiple [SpeechRecognitionAlternative](/en-US/docs/Web/API/SpeechRecognitionAlternative) objects.

[SpeechRecognitionResultList](/en-US/docs/Web/API/SpeechRecognitionResultList)

Represents a list of [SpeechRecognitionResult](/en-US/docs/Web/API/SpeechRecognitionResult) objects, or a single one if results are being captured in [continuous](/en-US/docs/Web/API/SpeechRecognition/continuous) mode.

### [Speech synthesis](#speech_synthesis)

[SpeechSynthesis](/en-US/docs/Web/API/SpeechSynthesis)

The controller interface for the speech service; this can be used to retrieve information about the synthesis voices available on the device, start and pause speech, and other commands besides.

[SpeechSynthesisErrorEvent](/en-US/docs/Web/API/SpeechSynthesisErrorEvent)

Contains information about any errors that occur while processing [SpeechSynthesisUtterance](/en-US/docs/Web/API/SpeechSynthesisUtterance) objects in the speech service.

[SpeechSynthesisEvent](/en-US/docs/Web/API/SpeechSynthesisEvent)

Contains information about the current state of [SpeechSynthesisUtterance](/en-US/docs/Web/API/SpeechSynthesisUtterance) objects that have been processed in the speech service.

[SpeechSynthesisUtterance](/en-US/docs/Web/API/SpeechSynthesisUtterance)

Represents a speech request. It contains the content the speech service should read and information about how to read it (e.g., language, pitch and volume.)

[SpeechSynthesisVoice](/en-US/docs/Web/API/SpeechSynthesisVoice)

Represents a voice that the system supports. Every `SpeechSynthesisVoice` has its own relative speech service including information about language, name and URI.

[Window.speechSynthesis](/en-US/docs/Web/API/Window/speechSynthesis)

Specified out as part of a `[NoInterfaceObject]` interface called `SpeechSynthesisGetter`, and Implemented by the `Window` object, the `speechSynthesis` property provides access to the [SpeechSynthesis](/en-US/docs/Web/API/SpeechSynthesis) controller, and therefore the entry point to speech synthesis functionality.

### [Deprecated interfaces](#deprecated_interfaces)

The concept of grammar has been removed from the Web Speech API. Related features remain in the specification and are still recognized by supporting browsers for backwards compatibility, but they have no effect on speech recognition services.

[SpeechGrammar](/en-US/docs/Web/API/SpeechGrammar)Deprecated

Represents words or patterns of words for the recognition service to recognize.

[SpeechGrammarList](/en-US/docs/Web/API/SpeechGrammarList)Deprecated

Represents a list of [SpeechGrammar](/en-US/docs/Web/API/SpeechGrammar) objects.

## [Errors](#errors)

For information on errors reported by the Speech API (for example, `"language-not-supported"` and `"language-unavailable"`), see the following documentation:

- [error property of the SpeechRecognitionErrorEvent object](/en-US/docs/Web/API/SpeechRecognitionErrorEvent/error)
- [error property of the SpeechSynthesisErrorEvent object](/en-US/docs/Web/API/SpeechSynthesisErrorEvent/error)

## [Security considerations](#security_considerations)

Access to the [on-device speech recognition](/en-US/docs/Web/API/Web_Speech_API/Using_the_Web_Speech_API#on-device_speech_recognition) functionality of the Web Speech API is controlled by the [on-device-speech-recognition](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/on-device-speech-recognition)[Permissions-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy) directive.

Specifically, where a defined policy blocks usage, any attempts to call the API's [SpeechRecognition.available()](/en-US/docs/Web/API/SpeechRecognition/available_static) or [SpeechRecognition.install()](/en-US/docs/Web/API/SpeechRecognition/install_static) methods will fail.

## [Examples](#examples)

Our [Web Speech API examples](https://mdn.github.io/dom-examples/web-speech-api/) illustrate speech recognition and synthesis.

## [Specifications](#specifications)

Specification
[Web Speech API# speechreco-section](https://webaudio.github.io/web-speech-api/#speechreco-section)
[Web Speech API# tts-section](https://webaudio.github.io/web-speech-api/#tts-section)

## [Browser compatibility](#browser_compatibility)

### [api.SpeechRecognition](#api.SpeechRecognition)

### [api.SpeechSynthesis](#api.SpeechSynthesis)

## [See also](#see_also)

- [Using the Web Speech API](/en-US/docs/Web/API/Web_Speech_API/Using_the_Web_Speech_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Web_Speech_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/web_speech_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_Speech_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fweb_speech_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_Speech_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fweb_speech_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0a00e01a8c8097ea9786710c3fc703d18f0af951%0A*+Document+last+modified%3A+2025-09-30T15%3A42%3A24.000Z%0A%0A%3C%2Fdetails%3E)
