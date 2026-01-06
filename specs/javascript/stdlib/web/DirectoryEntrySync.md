# DirectoryEntrySync

Non-standard: This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

The `DirectoryEntrySync` interface represents a directory in a file system. It includes methods for creating, reading, looking up, and recursively removing files in a directory.

Warning: This interface is deprecated and is no more on the standard track. Do not use it anymore. Use the [File and Directory Entries API](/en-US/docs/Web/API/File_and_Directory_Entries_API) instead.

## In this article

- [Basic concepts](#basic_concepts)
- [Method overview](#method_overview)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Basic concepts](#basic_concepts)

If you want to create subdirectories, you have to create each child directory in sequence. If you try to create a directory using a full path that includes parent directories that do not exist yet, you get an error. So create the hierarchy by recursively adding a new path after creating the parent directory.

### [Example](#example)

The `getFile()` method returns a `FileEntrySync`, which represents a file in the file system. The following creates an empty file called `logs.txt` in the root directory.

js

```
const fileEntry = fs.root.getFile("logs.txt", { create: true });
```

The `getDirectory()` method returns a `DirectoryEntrySync`, which represents a file in the file system. The following creates a new directory called `project_dir` in the root directory.

js

```
const dirEntry = fs.root.getDirectory("project_dir", { create: true });
```

## [Method overview](#method_overview)

- [createReader()](#createreader)
- [getFile()](#getfile)
- [getDirectory()](#getdirectory)
- [removeRecursively()](#removerecursively)

## [Instance methods](#instance_methods)

### [createReader()](#createreader)

Creates a new `DirectoryReaderSync` to read entries from this directory.

#### Syntax

js

```
createReader()
```

##### Parameters

None.

##### Return value

A [DirectoryReaderSync](/en-US/docs/Web/API/DirectoryReaderSync) object represents a directory in a file system.

##### Exceptions

This method can raise a [DOMException](/en-US/docs/Web/API/DOMException) with the following codes:

ExceptionDescription`NOT_FOUND_ERR`The directory does not exist.`SECURITY_ERR`The browser determined that it was not safe to look up the metadata. [ todo: Explain why ]

### [getFile()](#getfile)

Depending on how you've set the `options` parameter, the method either creates a file or looks up an existing file.

#### Syntax

js

```
getFile(path)
getFile(path, options)
```

##### Parameters

[path](#path)

Either an absolute path or a relative path from the directory to the file to be looked up or created. You cannot create a file whose immediate parent does not exist. Create the parent directory first.

[options](#options)

(optional) An object literal describing the behavior of the method. If the file does not exist, it is created.

Object literalConditionResult`create: true`
`exclusive: true`Path already existsAn error is thrown.`create: true`
`exclusive: false`Path doesn't exist and no other error occursA file is created. If a file already exists, no error is thrown.`create: false`
(`exclusive` is ignored) Path existsThe file is returned.`create: false`
(`exclusive` is ignored) Path doesn't existAn error is thrown.`create: false`
(`exclusive` is ignored) Path exists, but is a directoryAn error is thrown.

##### Return value

A [FileEntrySync](/en-US/docs/Web/API/FileEntrySync) object representing a file in a file system.

##### Exceptions

This method can raise a [DOMException](/en-US/docs/Web/API/DOMException) with the following codes:

ExceptionDescription`ENCODING_ERR`The path supplied is invalid.`NOT_FOUND_ERR`The path was structurally correct, but refers to a resource that does not exist.`NO_MODIFICATION_ALLOWED_ERR`This is a permission issue. The target directory or file is not writable.`PATH_EXISTS_ERR`The file already exists. You cannot create another one with the same path.`QUOTA_EXCEEDED_ERROR`The operation would cause the application to exceed its storage quota.`SECURITY_ERR`The application does not have permission to access the element referred to by path. [ todo: Explain why ]`TYPE_MISMATCH_ERR`The path supplied exists, but it is not a directory.

### [getDirectory()](#getdirectory)

Creates or looks up a directory. The method is similar to `getFile()` with DirectoryEntrySync being passed.

#### Syntax

js

```
getDirectory(path)
getDirectory(path, options)
```

##### Parameters

[path](#path_2)

Either an absolute path or a relative path from the directory to the file to be looked up or created. You cannot create a file whose immediate parent does not exist. Create the parent directory first.

[options](#options_2)

(optional) An object literal describing the behavior of the method if the file does not exist.

Object literalConditionResult`create: true`
`exclusive: true`Path already existsAn error is thrown.`create: true`
`exclusive: false`Path doesn't exist and no other error occurs A directory is created. If a file already exists, no error is thrown. `create: false`
(`exclusive` is ignored) Path existsThe directory is returned.`create: false`
(`exclusive` is ignored) Path doesn't existAn error is thrown.`create: false`
(`exclusive` is ignored) Path exists, but is a directoryAn error is thrown.

##### Return value

A [DirectoryEntrySync](/en-US/docs/Web/API/DirectoryReaderSync) object representing a directory in a file system.

##### Exceptions

This method can raise a [DOMException](/en-US/docs/Web/API/DOMException) with the following codes:

ExceptionDescription`ENCODING_ERR`The path supplied is invalid.`NOT_FOUND_ERR`The path was structurally correct, but refers to a resource that does not exist.`NO_MODIFICATION_ALLOWED_ERR`This is a permission issue. The target directory or file is not writable.`PATH_EXISTS_ERR`The file already exists. You cannot create another one with the same path.`QUOTA_EXCEEDED_ERROR`The operation would cause the application to exceed its storage quota.`SECURITY_ERR`The application does not have permission to access the element referred to by path. [ todo: Explain why ]`TYPE_MISMATCH_ERR`The path supplied exists, but it is not a directory.

### [removeRecursively()](#removerecursively)

Deletes a directory and all of its contents. You cannot delete the root directory of a file system.

If you delete a directory that contains a file that cannot be removed or if an error occurs while the deletion is in progress, some of the contents might not be deleted. Catch these cases with error callbacks and retry the deletion.

#### Syntax

js

```
removeRecursively()
```

##### Parameters

None.

##### Return value

[undefined](/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)

##### Exceptions

This method can raise a [DOMException](/en-US/docs/Web/API/DOMException) with the following codes:

ExceptionDescription`NOT_FOUND_ERR`The target directory does not exist.`INVALID_STATE_ERR` This directory is not longer valid for some reason other than being deleted. 

[todo: Explain more ]

`NO_MODIFICATION_ALLOWED_ERR` One of the following is not writable: the directory, its parent directory, and some of the content in the directory. `SECURITY_ERR` The application does not have permission to access the target directory, its parent, or some of its contents. 

## [Specifications](#specifications)

This feature is not part of any current specification. It is no longer on track to become a standard. Use the [File and Directory Entries API](/en-US/docs/Web/API/File_and_Directory_Entries_API) instead.

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [File and Directory Entries API](/en-US/docs/Web/API/File_and_Directory_Entries_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 17, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/DirectoryEntrySync/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/directoryentrysync/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDirectoryEntrySync&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdirectoryentrysync%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDirectoryEntrySync%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdirectoryentrysync%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F754b68246f4e69e404309fee4a1699e047e43994%0A*+Document+last+modified%3A+2025-11-17T16%3A52%3A01.000Z%0A%0A%3C%2Fdetails%3E)
