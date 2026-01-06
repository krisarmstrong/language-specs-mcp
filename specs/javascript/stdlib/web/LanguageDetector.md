# LanguageDetector

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `LanguageDetector` interface of the [Translator and Language Detector APIs](/en-US/docs/Web/API/Translator_and_Language_Detector_APIs) contains all the language detection functionality, including checking AI model availability, creating a new `LanguageDetector` instance, using it to detect a language, and more.

## In this article

- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[inputQuota](/en-US/docs/Web/API/LanguageDetector/inputQuota)Read onlyExperimental

The input quota available to the browser for detecting languages.

[expectedInputLanguages](/en-US/docs/Web/API/LanguageDetector/expectedInputLanguages)Read onlyExperimental

The expected languages to be detected in the input text.

## [Static methods](#static_methods)

[availability()](/en-US/docs/Web/API/LanguageDetector/availability_static)Experimental

Returns an enumerated value that indicates whether the browser AI model supports a given `LanguageDetector` configuration.

[create()](/en-US/docs/Web/API/LanguageDetector/create_static)Experimental

Creates a new `LanguageDetector` instance to detect languages.

## [Instance methods](#instance_methods)

[destroy()](/en-US/docs/Web/API/LanguageDetector/destroy)Experimental

Releases the resources assigned to the `LanguageDetector` instance it is called on and stops any further activity on it.

[detect()](/en-US/docs/Web/API/LanguageDetector/detect)Experimental

Detects the closest matching language or languages that a given text string is most likely to be written in.

[measureInputUsage()](/en-US/docs/Web/API/LanguageDetector/measureInputUsage)Experimental

Reports how much input quota would be used by a language detection operation for a given text input.

## [Examples](#examples)

See [Using the Translator and Language Detector APIs](/en-US/docs/Web/API/Translator_and_Language_Detector_APIs/Using) for a complete example.

### [Creating a LanguageDetector instance](#creating_a_languagedetector_instance)

js

```
const detector = await LanguageDetector.create({
  expectedInputLanguages: ["en-US", "zh"],
});
```

Note: Different implementations will likely support different languages.

### [Detecting languages](#detecting_languages)

js

```
const results = await detector.detect(myTextString);

results.forEach((result) => {
  console.log(`${result.detectedLanguage}: ${result.confidence}`);
});

// Results in logs like this:
// la: 0.8359838724136353
// es: 0.017705978825688362
// sv: 0.012977192178368568
// en: 0.011148443445563316
```

## [Specifications](#specifications)

Specification
[Translator and Language Detector APIs# languagedetector](https://webmachinelearning.github.io/translation-api/#languagedetector)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Translator and Language Detector APIs](/en-US/docs/Web/API/Translator_and_Language_Detector_APIs/Using)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 28, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/LanguageDetector/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/languagedetector/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FLanguageDetector&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Flanguagedetector%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FLanguageDetector%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Flanguagedetector%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff91ff68767990aea89c9cb21fd8fc6b365cef3cb%0A*+Document+last+modified%3A+2025-10-28T11%3A18%3A34.000Z%0A%0A%3C%2Fdetails%3E)
