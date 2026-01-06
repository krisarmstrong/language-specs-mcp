# Metadata

Non-standard: This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `Metadata` interface contains information about a file system entry. This metadata includes the file's size and modification date and time.

Note: This interface isn't available through the global scope; instead, you obtain a `Metadata` object describing a [FileSystemEntry](/en-US/docs/Web/API/FileSystemEntry) using the method [FileSystemEntry.getMetadata()](/en-US/docs/Web/API/FileSystemEntry/getMetadata).

## In this article

- [Instance properties](#instance_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[modificationTime](/en-US/docs/Web/API/Metadata/modificationTime)Read onlyExperimentalNon-standard

A [Date](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) object indicating the date and time the entry was modified.

[size](/en-US/docs/Web/API/Metadata/size)Read onlyExperimentalNon-standard

A 64-bit unsigned integer indicating the size of the entry in bytes.

## [Specifications](#specifications)

This feature has been removed from all specification and is not in the process of being standardized.

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [File and Directory Entries API](/en-US/docs/Web/API/File_and_Directory_Entries_API)
- [FileSystemEntry](/en-US/docs/Web/API/FileSystemEntry)
- [FileSystemFileEntry](/en-US/docs/Web/API/FileSystemFileEntry) and [FileSystemDirectoryEntry](/en-US/docs/Web/API/FileSystemDirectoryEntry)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 20, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Metadata/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/metadata/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMetadata&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmetadata%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMetadata%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmetadata%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcbe4c570701052c120808ea54c24c46ec9734084%0A*+Document+last+modified%3A+2025-02-20T00%3A01%3A52.000Z%0A%0A%3C%2Fdetails%3E)
