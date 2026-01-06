# WebTransportError

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebTransportError&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `WebTransportError` interface of the [WebTransport API](/en-US/docs/Web/API/WebTransport_API) represents an error related to the API, which can arise from server errors, network connection problems, or client-initiated abort operations (for example, arising from a [WritableStream.abort()](/en-US/docs/Web/API/WritableStream/abort) call).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[WebTransportError()](/en-US/docs/Web/API/WebTransportError/WebTransportError)

Creates a new `WebTransportError` object instance.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [DOMException](/en-US/docs/Web/API/DOMException).

[source](/en-US/docs/Web/API/WebTransportError/source)Read only

Returns an enumerated value indicating the source of the error—can be either `stream` or `session`.

[streamErrorCode](/en-US/docs/Web/API/WebTransportError/streamErrorCode)Read only

Returns a number in the range 0-255 indicating the application protocol error code for this error, or `null` if one is not available.

## [Examples](#examples)

js

```
const url = "not-a-url";

async function initTransport(url) {
  try {
    // Initialize transport connection
    const transport = new WebTransport(url);

    // The connection can be used once ready fulfills
    await transport.ready;

    // …
  } catch (error) {
    const msg = `Transport initialization failed.
                 Reason: ${error.message}.
                 Source: ${error.source}.
                 Error code: ${error.streamErrorCode}.`;
    console.log(msg);
  }
}
```

## [Specifications](#specifications)

Specification
[WebTransport# webtransporterror](https://w3c.github.io/webtransport/#webtransporterror)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using WebTransport](https://developer.chrome.com/docs/capabilities/web-apis/webtransport)
- [WebSockets API](/en-US/docs/Web/API/WebSockets_API)
- [Streams API](/en-US/docs/Web/API/Streams_API)
- [WebTransport over HTTP/3](https://datatracker.ietf.org/doc/html/draft-ietf-webtrans-http3/)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 28, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/WebTransportError/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/webtransporterror/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebTransportError&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwebtransporterror%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebTransportError%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwebtransporterror%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F759102220c07fb140b3e06971cd5981d8f0f134f%0A*+Document+last+modified%3A+2025-04-28T15%3A45%3A41.000Z%0A%0A%3C%2Fdetails%3E)
