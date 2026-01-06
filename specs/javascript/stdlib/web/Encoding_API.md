# Encoding API

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The Encoding API enables web developers to work with text that is represented in [character encodings](/en-US/docs/Glossary/Character_encoding) systems other than the encoding used internally by JavaScript strings. In particular, it enables developers to convert text between JavaScript strings and the [UTF-8](/en-US/docs/Glossary/UTF-8) encoding that is used for most documents on the web.

It provides two mechanisms:

- Encoding: taking a JavaScript string and converting it into an array of bytes representing the [UTF-8](/en-US/docs/Glossary/UTF-8) encoding of the string.
- Decoding: taking an array of bytes representing a particular character encoding of some text, and converting it into a JavaScript string.

Note that these operations are asymmetrical: encoding only encodes to UTF-8, while decoding can decode UTF-8 but also [many legacy encoding systems](/en-US/docs/Web/API/Encoding_API/Encodings).

The API provides synchronous interfaces for encoding and decoding, and also [stream-based](/en-US/docs/Web/API/Streams_API) encoders and decoders, which could be used to, for example, decode text as it arrives over a network connection.

## In this article

- [Interfaces](#interfaces)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Interfaces](#interfaces)

[TextDecoder](/en-US/docs/Web/API/TextDecoder)

A decoder to convert a byte array containing a particular encoding into a JavaScript string.

[TextDecoderStream](/en-US/docs/Web/API/TextDecoderStream)

A decoder to convert a byte stream containing a particular encoding into a stream of JavaScript strings.

[TextEncoder](/en-US/docs/Web/API/TextEncoder)

An encoder to convert a JavaScript string into an array of bytes representing the UTF-8 encoding of the string.

[TextEncoderStream](/en-US/docs/Web/API/TextEncoderStream)

An encoder to convert a stream of JavaScript strings into a stream of bytes representing the UTF-8 encoding of the strings.

## [Specifications](#specifications)

Specification[Encoding](https://encoding.spec.whatwg.org/)

## [Browser compatibility](#browser_compatibility)

### [api.TextDecoder](#api.TextDecoder)

### [api.TextEncoder](#api.TextEncoder)

### [api.TextEncoderStream](#api.TextEncoderStream)

### [api.TextDecoderStream](#api.TextDecoderStream)

## [See also](#see_also)

- [Encoding API Encodings](/en-US/docs/Web/API/Encoding_API/Encodings) - Encodings that must be supported for decoding text.

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Encoding_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/encoding_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEncoding_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fencoding_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEncoding_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fencoding_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fcf79b60471db6f148fa4ba36f2cdeafbbeb70%0A*+Document+last+modified%3A+2025-10-30T21%3A49%3A49.000Z%0A%0A%3C%2Fdetails%3E)
