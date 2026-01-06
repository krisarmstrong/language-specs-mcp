# Translator and Language Detector APIs

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The Translator and Language Detector APIs provide functionality to detect the language that text is written in, and to translate text into different languages, via a browser's own internal AI model (which may differ between browsers).

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [HTTP headers](#http_headers)
- [Security considerations](#security_considerations)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

Translating a body of text is a common task on today's web. Typical use cases include:

- On-the-fly translation of an article that isn't available in your language.
- Translating a user's support requests into a language the support agent understands.
- Facilitating chats between users that don't speak each other's languages.

Detecting the language of a body of test is an important precursor for successful automated translation, but has other uses beyond direct translation. For example, it allows automatic UI configuration based on user text entry, ranging from updating UI and error strings, to automatically loading appropriate dictionaries for spell checking or curse word detection.

AI is well-suited to facilitating language detection and translation. The Translator and Language Detector APIs provide asynchronous ([Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)-based) mechanisms for a website to detect languages and translate text via the browser's own internal AI model. This is useful and efficient because the browser handles the service, rather than the developer having to rely on the user downloading AI models, or host or pay for a cloud-based translation service.

- Language detection is done via the [LanguageDetector](/en-US/docs/Web/API/LanguageDetector) interface. A `LanguageDetector` object instance is created using the [LanguageDetector.create()](/en-US/docs/Web/API/LanguageDetector/create_static) static method, then the [detect()](/en-US/docs/Web/API/LanguageDetector/detect) instance method is passed the text string to detect the language for.
- Translation is done via the [Translator](/en-US/docs/Web/API/Translator) interface. A `Translator` object instance is created using the [Translator.create()](/en-US/docs/Web/API/Translator/create_static) static method, then the [translate()](/en-US/docs/Web/API/Translator/translate) instance method is passed the text string to translate.

You can cancel a pending `create()`, `detect()`, or `translate()` operation using an [AbortController](/en-US/docs/Web/API/AbortController).

After a `LanguageDetector` or `Translator` instance has been created, you can release its assigned resources and stop any further activity by calling its [LanguageDetector.destroy()](/en-US/docs/Web/API/LanguageDetector/destroy)/[Translator.destroy()](/en-US/docs/Web/API/Translator/destroy) method. You are encouraged to do this after you've finished with the object as it can consume a lot of resources.

See [Using the Translator and Language Detector APIs](/en-US/docs/Web/API/Translator_and_Language_Detector_APIs/Using) for a walkthrough of how to use the APIs.

## [Interfaces](#interfaces)

[LanguageDetector](/en-US/docs/Web/API/LanguageDetector)Experimental

Contains all the language detection functionality, including checking AI model availability, creating a new `LanguageDetector` instance, using it to detect a language, and more.

[Translator](/en-US/docs/Web/API/Translator)Experimental

Contains all the translation functionality, including checking AI model availability, creating a new `Translator` instance, using it to create a translation, and more.

## [HTTP headers](#http_headers)

[Permissions-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy); the [language-detector](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/language-detector) directive

Controls access to the language detection functionality. Where a policy specifically disallows its use, any attempts to call the `LanguageDetector` methods will fail with a `NotAllowedError`[DOMException](/en-US/docs/Web/API/DOMException).

[Permissions-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy); the [translator](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/translator) directive

Controls access to the translation functionality. Where a policy specifically disallows its use, any attempts to call the `Translator` methods will fail with a `NotAllowedError`[DOMException](/en-US/docs/Web/API/DOMException).

## [Security considerations](#security_considerations)

Creation of `LanguageDetector` and `Translator` objects requires that the user has recently interacted with the page ([transient user activation](/en-US/docs/Web/Security/Defenses/User_activation) is required).

Access to the API is also controlled via [language-detector](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/language-detector) and [translator](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/translator)[Permissions-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy) directives.

## [Examples](#examples)

For a full example, see [Using the Translator and Language Detector APIs](/en-US/docs/Web/API/Translator_and_Language_Detector_APIs/Using).

## [Specifications](#specifications)

Specification[Unknown specification](https://webmachinelearning.github.io/translation-api)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Language detection with built-in AI](https://developer.chrome.com/docs/ai/language-detection) on developer.chrome.com (2025)
- [Translation with built-in AI](https://developer.chrome.com/docs/ai/translator-api) on developer.chrome.com (2025)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Translator_and_Language_Detector_APIs/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/translator_and_language_detector_apis/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTranslator_and_Language_Detector_APIs&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftranslator_and_language_detector_apis%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTranslator_and_Language_Detector_APIs%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftranslator_and_language_detector_apis%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca26363fcc6fc861103d40ac0205e5c5b79eb2fa%0A*+Document+last+modified%3A+2025-11-30T02%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
