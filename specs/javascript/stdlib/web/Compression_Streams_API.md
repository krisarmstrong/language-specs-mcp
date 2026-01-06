# Compression Streams API

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨May 2023⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCompression_Streams_API&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The Compression Streams API provides a JavaScript API for compressing and decompressing streams of data using the gzip or deflate formats.

Built in compression means that JavaScript applications will not need to include a compression library, which makes the download size of the application smaller.

The Fetch API's [Response](/en-US/docs/Web/API/Response) can be used to convert streams to:

- [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)
- [Blob](/en-US/docs/Web/API/Blob)
- [Uint8Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array)
- [String](/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
- JSON

## In this article

- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Interfaces](#interfaces)

[CompressionStream](/en-US/docs/Web/API/CompressionStream)

Compresses a stream of data.

[DecompressionStream](/en-US/docs/Web/API/DecompressionStream)

Decompresses a stream of data.

## [Examples](#examples)

In this example a stream is compressed using gzip compression.

js

```
const compressedReadableStream = inputReadableStream.pipeThrough(
  new CompressionStream("gzip"),
);
```

In the following example a function decompresses a blob using gzip.

js

```
async function DecompressBlob(blob) {
  const ds = new DecompressionStream("gzip");
  const decompressedStream = blob.stream().pipeThrough(ds);
  return await new Response(decompressedStream).blob();
}
```

## [Specifications](#specifications)

Specification
[Compression# compression-stream](https://compression.spec.whatwg.org/#compression-stream)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 6, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Compression_Streams_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/compression_streams_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCompression_Streams_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcompression_streams_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCompression_Streams_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcompression_streams_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7d17bd76546fce1b3889f151876481507bce2a31%0A*+Document+last+modified%3A+2025-09-06T03%3A28%3A16.000Z%0A%0A%3C%2Fdetails%3E)
