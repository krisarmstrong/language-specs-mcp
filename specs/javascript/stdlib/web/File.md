# File

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFile&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `File` interface provides information about files and allows JavaScript in a web page to access their content.

`File` objects are generally retrieved from a [FileList](/en-US/docs/Web/API/FileList) object returned as a result of a user selecting files using the [<input>](/en-US/docs/Web/HTML/Reference/Elements/input) element, or from a drag and drop operation's [DataTransfer](/en-US/docs/Web/API/DataTransfer) object.

A `File` object is a specific kind of [Blob](/en-US/docs/Web/API/Blob), and can be used in any context that a Blob can. In particular, the following APIs accept both `Blob`s and `File` objects:

- [FileReader](/en-US/docs/Web/API/FileReader)
- [URL.createObjectURL()](/en-US/docs/Web/API/URL/createObjectURL_static)
- [Window.createImageBitmap()](/en-US/docs/Web/API/Window/createImageBitmap) and [WorkerGlobalScope.createImageBitmap()](/en-US/docs/Web/API/WorkerGlobalScope/createImageBitmap)
- the [body](/en-US/docs/Web/API/RequestInit#body) option to [fetch()](/en-US/docs/Web/API/Window/fetch)
- [XMLHttpRequest.send()](/en-US/docs/Web/API/XMLHttpRequest/send)

See [Using files from web applications](/en-US/docs/Web/API/File_API/Using_files_from_web_applications) for more information and examples.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[File()](/en-US/docs/Web/API/File/File)

Returns a newly constructed `File`.

## [Instance properties](#instance_properties)

The `File` interface also inherits properties from the [Blob](/en-US/docs/Web/API/Blob) interface.

[File.lastModified](/en-US/docs/Web/API/File/lastModified)Read only

Returns the last modified time of the file, in millisecond since the UNIX epoch (January 1st, 1970 at Midnight).

[File.lastModifiedDate](/en-US/docs/Web/API/File/lastModifiedDate)DeprecatedRead onlyNon-standard

Returns the last modified [Date](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) of the file referenced by the `File` object.

[File.name](/en-US/docs/Web/API/File/name)Read only

Returns the name of the file referenced by the `File` object.

[File.webkitRelativePath](/en-US/docs/Web/API/File/webkitRelativePath)Read only

Returns the path the URL of the `File` is relative to.

## [Instance methods](#instance_methods)

The `File` interface also inherits methods from the [Blob](/en-US/docs/Web/API/Blob) interface.

## [Specifications](#specifications)

Specification
[File API# file-section](https://w3c.github.io/FileAPI/#file-section)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using files from web applications](/en-US/docs/Web/API/File_API/Using_files_from_web_applications)
- [FileReader](/en-US/docs/Web/API/FileReader)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 2, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/File/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/file/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFile&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffile%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFile%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffile%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0a24354d9ac0cac0b9c6f47de27cbf758c9f32f4%0A*+Document+last+modified%3A+2024-10-02T14%3A01%3A42.000Z%0A%0A%3C%2Fdetails%3E)
