# Translator

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `Translator` interface of the [Translator and Language Detector APIs](/en-US/docs/Web/API/Translator_and_Language_Detector_APIs) contains all the associated translation functionality, including checking AI model availability, creating a new `Translator` instance, using it to create a translation, and more.

## In this article

- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[inputQuota](/en-US/docs/Web/API/Translator/inputQuota)Read onlyExperimental

The input quota available to the browser for generating translations.

[sourceLanguage](/en-US/docs/Web/API/Translator/sourceLanguage)Read onlyExperimental

The expected language of the input text to be translated.

[targetLanguage](/en-US/docs/Web/API/Translator/targetLanguage)Read onlyExperimental

The language that the input text will be translated into.

## [Static methods](#static_methods)

[availability()](/en-US/docs/Web/API/Translator/availability_static)Experimental

Returns an enumerated value that indicates the availability of the AI model for the given `Translator` configuration.

[create()](/en-US/docs/Web/API/Translator/create_static)Experimental

Creates a new `Translator` instance from which to generate translations.

## [Instance methods](#instance_methods)

[destroy()](/en-US/docs/Web/API/Translator/destroy)Experimental

Releases the resources assigned to the `Translator` instance it is called on and stops any further activity on it.

[measureInputUsage()](/en-US/docs/Web/API/Translator/measureInputUsage)Experimental

Reports how much input quota would be used by a translation operation for a given text input.

[translate()](/en-US/docs/Web/API/Translator/translate)Experimental

Returns a string containing a translation of the input string.

[translateStreaming()](/en-US/docs/Web/API/Translator/translateStreaming)Experimental

Generates a translation of the input string as a [ReadableStream](/en-US/docs/Web/API/ReadableStream).

## [Examples](#examples)

See [Using the Translator and Language Detector APIs](/en-US/docs/Web/API/Translator_and_Language_Detector_APIs/Using) for a complete example.

### [Creating a Translator instance](#creating_a_translator_instance)

js

```
const translator = await Translator.create({
  sourceLanguage: "en",
  targetLanguage: "ja",
});
```

### [Generating a translation](#generating_a_translation)

js

```
const translation = await translator.translate(myTextString);
console.log(translation);
```

### [Generating a translation stream](#generating_a_translation_stream)

js

```
const stream = translator.translateStreaming(myTextString);
let translation = "";

for await (const chunk of stream) {
  translation += chunk;
}

console.log("Stream complete");
console.log(translation);
```

## [Specifications](#specifications)

Specification
[Translator and Language Detector APIs# translator](https://webmachinelearning.github.io/translation-api/#translator)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Translator and Language Detector APIs](/en-US/docs/Web/API/Translator_and_Language_Detector_APIs/Using)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 28, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Translator/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/translator/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTranslator&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftranslator%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTranslator%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftranslator%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff91ff68767990aea89c9cb21fd8fc6b365cef3cb%0A*+Document+last+modified%3A+2025-10-28T11%3A18%3A34.000Z%0A%0A%3C%2Fdetails%3E)
