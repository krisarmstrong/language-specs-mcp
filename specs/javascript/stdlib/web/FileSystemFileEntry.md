# FileSystemFileEntry

The `FileSystemFileEntry` interface of the [File and Directory Entries API](/en-US/docs/Web/API/File_and_Directory_Entries_API) represents a file in a file system. It offers properties describing the file's attributes, as well as the [file()](/en-US/docs/Web/API/FileSystemFileEntry/file) method, which creates a [File](/en-US/docs/Web/API/File) object that can be used to read the file.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits the properties of its parent interface, [FileSystemEntry](/en-US/docs/Web/API/FileSystemEntry), but has no properties unique to this interface.

## [Instance methods](#instance_methods)

[createWriter()](/en-US/docs/Web/API/FileSystemFileEntry/createWriter)DeprecatedNon-standard

Returns a `FileWriter` object which can be used to write data into the file represented by the directory entry.

[file()](/en-US/docs/Web/API/FileSystemFileEntry/file)

Creates a new [File](/en-US/docs/Web/API/File) object which can be used to read the file.

## [Specifications](#specifications)

Specification
[File and Directory Entries API# api-fileentry](https://wicg.github.io/entries-api/#api-fileentry)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [File and Directory Entries API](/en-US/docs/Web/API/File_and_Directory_Entries_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 20, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/FileSystemFileEntry/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/filesystemfileentry/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileSystemFileEntry&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffilesystemfileentry%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileSystemFileEntry%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffilesystemfileentry%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcbe4c570701052c120808ea54c24c46ec9734084%0A*+Document+last+modified%3A+2025-02-20T00%3A01%3A52.000Z%0A%0A%3C%2Fdetails%3E)
