# FileReaderSync

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileReaderSync&level=high)

Note: This feature is only available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API), except for [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

The `FileReaderSync` interface allows to read [File](/en-US/docs/Web/API/File) or [Blob](/en-US/docs/Web/API/Blob) objects synchronously. This interface is [only available](/en-US/docs/Web/API/Web_Workers_API/Functions_and_classes_available_to_workers) in [workers](/en-US/docs/Web/API/Worker) as it enables synchronous I/O that could potentially block.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[FileReaderSync()](/en-US/docs/Web/API/FileReaderSync/FileReaderSync)

Returns a new `FileReaderSync` object.

## [Instance properties](#instance_properties)

This interface does not have any properties.

## [Instance methods](#instance_methods)

[FileReaderSync.readAsArrayBuffer()](/en-US/docs/Web/API/FileReaderSync/readAsArrayBuffer)

This method converts a specified [Blob](/en-US/docs/Web/API/Blob) or a [File](/en-US/docs/Web/API/File) into an [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) representing the input data as a binary string.

[FileReaderSync.readAsBinaryString()](/en-US/docs/Web/API/FileReaderSync/readAsBinaryString)Deprecated

This method converts a specified [Blob](/en-US/docs/Web/API/Blob) or a [File](/en-US/docs/Web/API/File) into a string representing the input data as a binary string. This method is deprecated, consider using `readAsArrayBuffer()` instead.

[FileReaderSync.readAsText()](/en-US/docs/Web/API/FileReaderSync/readAsText)

This method converts a specified [Blob](/en-US/docs/Web/API/Blob) or a [File](/en-US/docs/Web/API/File) into a string representing the input data as a text string. The optional `encoding` parameter indicates the encoding to be used (e.g., iso-8859-1 or UTF-8). If not present, the method will apply a detection algorithm for it.

[FileReaderSync.readAsDataURL()](/en-US/docs/Web/API/FileReaderSync/readAsDataURL)

This method converts a specified [Blob](/en-US/docs/Web/API/Blob) or a [File](/en-US/docs/Web/API/File) into a string representing the input data as a data URL.

## [Specifications](#specifications)

Specification
[File API# FileReaderSync](https://w3c.github.io/FileAPI/#FileReaderSync)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [FileReader](/en-US/docs/Web/API/FileReader)
- [Blob](/en-US/docs/Web/API/Blob)
- [File](/en-US/docs/Web/API/File)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 3, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/FileReaderSync/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/filereadersync/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileReaderSync&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffilereadersync%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileReaderSync%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffilereadersync%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1dad49fff047729e8dcca313a45ccb4cc2d2526f%0A*+Document+last+modified%3A+2024-04-03T16%3A40%3A29.000Z%0A%0A%3C%2Fdetails%3E)
