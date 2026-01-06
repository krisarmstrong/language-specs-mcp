# FileSystemWritableFileStream

 Baseline  2025 Newly available

 Since ⁨September 2025⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileSystemWritableFileStream&level=low)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `FileSystemWritableFileStream` interface of the [File System API](/en-US/docs/Web/API/File_System_API) is a [WritableStream](/en-US/docs/Web/API/WritableStream) object with additional convenience methods, which operates on a single file on disk. The interface is accessed through the [FileSystemFileHandle.createWritable()](/en-US/docs/Web/API/FileSystemFileHandle/createWritable) method.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [WritableStream](/en-US/docs/Web/API/WritableStream).

## [Instance methods](#instance_methods)

Inherits methods from its parent, [WritableStream](/en-US/docs/Web/API/WritableStream).

[FileSystemWritableFileStream.write()](/en-US/docs/Web/API/FileSystemWritableFileStream/write)

Writes content into the file the method is called on, at the current file cursor offset.

[FileSystemWritableFileStream.seek()](/en-US/docs/Web/API/FileSystemWritableFileStream/seek)

Updates the current file cursor offset to the position (in bytes) specified.

[FileSystemWritableFileStream.truncate()](/en-US/docs/Web/API/FileSystemWritableFileStream/truncate)

Resizes the file associated with the stream to be the specified size in bytes.

## [Examples](#examples)

The following asynchronous function opens the 'Save File' picker, which returns a [FileSystemFileHandle](/en-US/docs/Web/API/FileSystemFileHandle) once a file is selected. From this, a writable stream is created using the [FileSystemFileHandle.createWritable()](/en-US/docs/Web/API/FileSystemFileHandle/createWritable) method.

A text string is then written to the stream, which is subsequently closed.

js

```
async function saveFile() {
  // create a new handle
  const newHandle = await window.showSaveFilePicker();

  // create a FileSystemWritableFileStream to write to
  const writableStream = await newHandle.createWritable();

  // write our file
  await writableStream.write("This is my file content");

  // close the file and write the contents to disk.
  await writableStream.close();
}
```

The following examples show different options that can be passed into the `write()` method.

js

```
// just pass in the data (no options)
writableStream.write(data);

// writes the data to the stream from the determined position
writableStream.write({ type: "write", position, data });

// updates the current file cursor offset to the position specified
writableStream.write({ type: "seek", position });

// resizes the file to be size bytes long
writableStream.write({ type: "truncate", size });
```

## [Specifications](#specifications)

Specification
[File System# api-filesystemwritablefilestream](https://fs.spec.whatwg.org/#api-filesystemwritablefilestream)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [File System API](/en-US/docs/Web/API/File_System_API)
- [The File System Access API: simplifying access to local files](https://developer.chrome.com/docs/capabilities/web-apis/file-system-access)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 5, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/FileSystemWritableFileStream/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/filesystemwritablefilestream/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileSystemWritableFileStream&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffilesystemwritablefilestream%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileSystemWritableFileStream%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffilesystemwritablefilestream%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff10fbe2d2dc4857bf29ce955689a7ba7c1ffac8b%0A*+Document+last+modified%3A+2024-04-05T07%3A23%3A55.000Z%0A%0A%3C%2Fdetails%3E)
