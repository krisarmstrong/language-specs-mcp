# TextEncoder

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextEncoder&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `TextEncoder` interface enables you to [encode](/en-US/docs/Glossary/Character_encoding) a JavaScript string using [UTF-8](/en-US/docs/Glossary/UTF-8).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[TextEncoder()](/en-US/docs/Web/API/TextEncoder/TextEncoder)

Creates and returns a new `TextEncoder`.

## [Instance properties](#instance_properties)

The `TextEncoder` interface doesn't inherit any properties.

[TextEncoder.encoding](/en-US/docs/Web/API/TextEncoder/encoding)Read only

Always returns `utf-8`.

## [Instance methods](#instance_methods)

The `TextEncoder` interface doesn't inherit any methods.

[TextEncoder.encode()](/en-US/docs/Web/API/TextEncoder/encode)

Takes a string as input, and returns a [Uint8Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) containing the string encoded using UTF-8.

[TextEncoder.encodeInto()](/en-US/docs/Web/API/TextEncoder/encodeInto)

Takes a string to encode and a destination [Uint8Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) to put the resulting UTF-8 encoded text into, and returns an object indicating the progress of the encoding. This is potentially more performant than the older `encode()` method.

## [Examples](#examples)

### [Encoding to UTF-8](#encoding_to_utf-8)

This example shows how to encode the "€" character to UTF-8.

html

```
<button id="encode">Encode</button>
<button id="reset">Reset</button>
<div id="output"></div>
```

```
div {
  margin: 1rem 0;
}
```

js

```
const utf8encoder = new TextEncoder();
const text = "€";

const output = document.querySelector("#output");
const encodeButton = document.querySelector("#encode");
encodeButton.addEventListener("click", () => {
  output.textContent = utf8encoder.encode(text);
});

const resetButton = document.querySelector("#reset");
resetButton.addEventListener("click", () => {
  window.location.reload();
});
```

## [Specifications](#specifications)

Specification
[Encoding# interface-textencoder](https://encoding.spec.whatwg.org/#interface-textencoder)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [TextDecoder](/en-US/docs/Web/API/TextDecoder) interface describing the inverse operation.

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 28, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/TextEncoder/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/textencoder/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextEncoder&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftextencoder%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextEncoder%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftextencoder%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fccd1540ad8c51242b318bf437dfabe2e5315b3fa%0A*+Document+last+modified%3A+2025-06-28T10%3A28%3A50.000Z%0A%0A%3C%2Fdetails%3E)
