# FileReader

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileReader&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `FileReader` interface lets web applications asynchronously read the contents of files (or raw data buffers) stored on the user's computer, using [File](/en-US/docs/Web/API/File) or [Blob](/en-US/docs/Web/API/Blob) objects to specify the file or data to read.

File objects may be obtained from a [FileList](/en-US/docs/Web/API/FileList) object returned as a result of a user selecting files using the `<input type="file">` element, or from a drag and drop operation's [DataTransfer](/en-US/docs/Web/API/DataTransfer) object. `FileReader` can only access the contents of files that the user has explicitly selected; it cannot be used to read a file by pathname from the user's file system. To read files on the client's file system by pathname, use the [File System Access API](/en-US/docs/Web/API/File_System_API). To read server-side files, use [fetch()](/en-US/docs/Web/API/Window/fetch), with [CORS](/en-US/docs/Web/HTTP/Guides/CORS) permission if reading cross-origin.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[FileReader()](/en-US/docs/Web/API/FileReader/FileReader)

Returns a new `FileReader` object.

See [Using files from web applications](/en-US/docs/Web/API/File_API/Using_files_from_web_applications) for details and examples.

## [Instance properties](#instance_properties)

[FileReader.error](/en-US/docs/Web/API/FileReader/error)Read only

A [DOMException](/en-US/docs/Web/API/DOMException) representing the error that occurred while reading the file.

[FileReader.readyState](/en-US/docs/Web/API/FileReader/readyState)Read only

A number indicating the state of the `FileReader`. This is one of the following:

NameValueDescription`EMPTY``0`No data has been loaded yet.`LOADING``1`Data is currently being loaded.`DONE``2`The entire read request has been completed.[FileReader.result](/en-US/docs/Web/API/FileReader/result)Read only

The file's contents. This property is only valid after the read operation is complete, and the format of the data depends on which of the methods was used to initiate the read operation.

## [Instance methods](#instance_methods)

[FileReader.abort()](/en-US/docs/Web/API/FileReader/abort)

Aborts the read operation. Upon return, the `readyState` will be `DONE`.

[FileReader.readAsArrayBuffer()](/en-US/docs/Web/API/FileReader/readAsArrayBuffer)

Starts reading the contents of the specified [Blob](/en-US/docs/Web/API/Blob), once finished, the `result` attribute contains an [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) representing the file's data.

[FileReader.readAsBinaryString()](/en-US/docs/Web/API/FileReader/readAsBinaryString)Deprecated

Starts reading the contents of the specified [Blob](/en-US/docs/Web/API/Blob), once finished, the `result` attribute contains the raw binary data from the file as a string.

[FileReader.readAsDataURL()](/en-US/docs/Web/API/FileReader/readAsDataURL)

Starts reading the contents of the specified [Blob](/en-US/docs/Web/API/Blob), once finished, the `result` attribute contains a `data:` URL representing the file's data.

[FileReader.readAsText()](/en-US/docs/Web/API/FileReader/readAsText)

Starts reading the contents of the specified [Blob](/en-US/docs/Web/API/Blob), once finished, the `result` attribute contains the contents of the file as a text string. An optional encoding name can be specified.

## [Events](#events)

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface. Remove the event listeners with [removeEventListener()](/en-US/docs/Web/API/EventTarget/removeEventListener), once `FileReader` is no longer used, to avoid memory leaks.

[abort](/en-US/docs/Web/API/FileReader/abort_event)

Fired when a read has been aborted, for example because the program called [FileReader.abort()](/en-US/docs/Web/API/FileReader/abort).

[error](/en-US/docs/Web/API/FileReader/error_event)

Fired when the read failed due to an error.

[load](/en-US/docs/Web/API/FileReader/load_event)

Fired when a read has completed successfully.

[loadend](/en-US/docs/Web/API/FileReader/loadend_event)

Fired when a read has completed, successfully or not.

[loadstart](/en-US/docs/Web/API/FileReader/loadstart_event)

Fired when a read has started.

[progress](/en-US/docs/Web/API/FileReader/progress_event)

Fired periodically as data is read.

## [Examples](#examples)

### [Using FileReader](#using_filereader)

This example reads and displays the contents of a text file directly in the browser.

#### HTML

html

```
<h1>File Reader</h1>
<input type="file" id="file-input" />
<div id="message"></div>
<pre id="file-content"></pre>
```

#### JavaScript

js

```
const fileInput = document.getElementById("file-input");
const fileContentDisplay = document.getElementById("file-content");
const messageDisplay = document.getElementById("message");

fileInput.addEventListener("change", handleFileSelection);

function handleFileSelection(event) {
  const file = event.target.files[0];
  fileContentDisplay.textContent = ""; // Clear previous file content
  messageDisplay.textContent = ""; // Clear previous messages

  // Validate file existence and type
  if (!file) {
    showMessage("No file selected. Please choose a file.", "error");
    return;
  }

  if (!file.type.startsWith("text")) {
    showMessage("Unsupported file type. Please select a text file.", "error");
    return;
  }

  // Read the file
  const reader = new FileReader();
  reader.onload = () => {
    fileContentDisplay.textContent = reader.result;
  };
  reader.onerror = () => {
    showMessage("Error reading the file. Please try again.", "error");
  };
  reader.readAsText(file);
}

// Displays a message to the user
function showMessage(message, type) {
  messageDisplay.textContent = message;
  messageDisplay.style.color = type === "error" ? "red" : "green";
}
```

### [Result](#result)

## [Specifications](#specifications)

Specification
[File API# APIASynch](https://w3c.github.io/FileAPI/#APIASynch)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using files from web applications](/en-US/docs/Web/API/File_API/Using_files_from_web_applications)
- [File](/en-US/docs/Web/API/File)
- [Blob](/en-US/docs/Web/API/Blob)
- [FileReaderSync](/en-US/docs/Web/API/FileReaderSync)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/FileReader/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/filereader/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileReader&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffilereader%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileReader%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffilereader%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
