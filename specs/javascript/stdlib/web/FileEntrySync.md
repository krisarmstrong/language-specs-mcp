# FileEntrySync

Non-standard: This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

The `FileEntrySync` interface represents a file in a file system. It lets you write content to a file.

Warning: This interface is deprecated and is no more on the standard track. Do not use it anymore. Use the [File and Directory Entries API](/en-US/docs/Web/API/File_and_Directory_Entries_API) instead.

## In this article

- [Basic concepts](#basic_concepts)
- [Method overview](#method_overview)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Basic concepts](#basic_concepts)

To write content to file, create a FileWriter object by calling [createWriter()](#createwriter).

## [Method overview](#method_overview)

[createWriter](#createwriter)`FileWriterSync  ();`[file](#file)`File  ();`

## [Instance methods](#instance_methods)

### [createWriter()](#createwriter)

Creates a new `FileWriter` associated with the file that the `FileEntry` represents.

js

```
createWriter()
```

#### Parameters

None.

#### Return value

A `FileWriterSync` object.

#### Exceptions

This method can raise a [DOMException](/en-US/docs/Web/API/DOMException) with the following codes:

ExceptionDescription`NOT_FOUND_ERR`The file does not exist.`INVALID_STATE_ERR`The file is no longer valid for some reason other than it having been deleted.

### [file()](#file)

Returns a File that represents the current state of the file that this `FileEntry` represents.

js

```
file()
```

#### Parameters

None.

#### Return value

A `File` object.

#### Exceptions

This method can raise a [DOMException](/en-US/docs/Web/API/DOMException) with the following codes:

ExceptionDescription`NOT_FOUND_ERR`The file does not exist.`INVALID_STATE_ERR`The file is no longer valid for some reason other than it having been deleted.

## [Specifications](#specifications)

This feature is not part of any specification anymore. It is no longer on track to become a standard.

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [File and Directory Entries API](/en-US/docs/Web/API/File_and_Directory_Entries_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 4, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/FileEntrySync/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/fileentrysync/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileEntrySync&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffileentrysync%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileEntrySync%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffileentrysync%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F20cff31570e35c6da44ddd84158fcebd9f4f42d9%0A*+Document+last+modified%3A+2025-04-04T02%3A05%3A49.000Z%0A%0A%3C%2Fdetails%3E)
