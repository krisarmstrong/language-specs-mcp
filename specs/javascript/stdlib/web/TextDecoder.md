# TextDecoder

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextDecoder&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `TextDecoder` interface represents a decoder for a specific text encoding, such as `UTF-8`, `ISO-8859-2`, or `GBK`. A decoder takes an array of bytes as input and returns a JavaScript string.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[TextDecoder()](/en-US/docs/Web/API/TextDecoder/TextDecoder)

Creates and returns a new `TextDecoder`.

## [Instance properties](#instance_properties)

The `TextDecoder` interface doesn't inherit any properties.

[TextDecoder.encoding](/en-US/docs/Web/API/TextDecoder/encoding)Read only

A string containing the name of the character encoding system that this `TextDecoder` will use.

[TextDecoder.fatal](/en-US/docs/Web/API/TextDecoder/fatal)Read only

A boolean indicating whether the error mode is fatal.

[TextDecoder.ignoreBOM](/en-US/docs/Web/API/TextDecoder/ignoreBOM)Read only

A boolean indicating whether the [byte order mark](https://www.w3.org/International/questions/qa-byte-order-mark) is ignored.

## [Instance methods](#instance_methods)

The `TextDecoder` interface doesn't inherit any methods.

[TextDecoder.decode()](/en-US/docs/Web/API/TextDecoder/decode)

Decodes the given bytes into a JavaScript string and returns it.

## [Examples](#examples)

### [Decoding UTF-8 text](#decoding_utf-8_text)

This example shows how to decode the UTF-8 encoding of the character "𠮷".

html

```
<button id="decode">Decode</button>
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
const utf8decoder = new TextDecoder(); // default 'utf-8'
const encodedText = new Uint8Array([240, 160, 174, 183]);

const output = document.querySelector("#output");
const decodeButton = document.querySelector("#decode");
decodeButton.addEventListener("click", () => {
  output.textContent = utf8decoder.decode(encodedText);
});

const resetButton = document.querySelector("#reset");
resetButton.addEventListener("click", () => {
  window.location.reload();
});
```

### [Decoding non-UTF8 text](#decoding_non-utf8_text)

In this example, we decode the Russian text "Привет, мир!", which means "Hello, world." In our [TextDecoder()](/en-US/docs/Web/API/TextDecoder/TextDecoder) constructor, we specify the Windows-1251 character encoding.

html

```
<button id="decode">Decode</button>
<button id="reset">Reset</button>
<div id="decoded"></div>
```

```
div {
  margin: 1rem 0;
}
```

js

```
const win1251decoder = new TextDecoder("windows-1251");
const encodedText = new Uint8Array([
  207, 240, 232, 226, 229, 242, 44, 32, 236, 232, 240, 33,
]);

const decoded = document.querySelector("#decoded");
const decodeButton = document.querySelector("#decode");
decodeButton.addEventListener("click", () => {
  decoded.textContent = win1251decoder.decode(encodedText);
});

const resetButton = document.querySelector("#reset");
resetButton.addEventListener("click", () => {
  window.location.reload();
});
```

## [Specifications](#specifications)

Specification
[Encoding# interface-textdecoder](https://encoding.spec.whatwg.org/#interface-textdecoder)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [TextEncoder](/en-US/docs/Web/API/TextEncoder) interface describing the inverse operation.

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 28, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/TextDecoder/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/textdecoder/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextDecoder&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftextdecoder%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextDecoder%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftextdecoder%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fccd1540ad8c51242b318bf437dfabe2e5315b3fa%0A*+Document+last+modified%3A+2025-06-28T10%3A28%3A50.000Z%0A%0A%3C%2Fdetails%3E)
