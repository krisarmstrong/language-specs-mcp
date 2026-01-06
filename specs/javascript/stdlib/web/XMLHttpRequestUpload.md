# XMLHttpRequestUpload

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXMLHttpRequestUpload&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API), except for [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

The `XMLHttpRequestUpload` interface represents the upload process for a specific [XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest). It is an opaque object that represents the underlying, browser-dependent, upload process. It is an [XMLHttpRequestEventTarget](/en-US/docs/Web/API/XMLHttpRequestEventTarget) and can be obtained by calling [XMLHttpRequest.upload](/en-US/docs/Web/API/XMLHttpRequest/upload).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface has no specific property, but inherits the properties of [XMLHttpRequestEventTarget](/en-US/docs/Web/API/XMLHttpRequestEventTarget) and of [EventTarget](/en-US/docs/Web/API/EventTarget).

## [Instance methods](#instance_methods)

This interface has no specific method, but inherits the methods of [XMLHttpRequestEventTarget](/en-US/docs/Web/API/XMLHttpRequestEventTarget) and of [EventTarget](/en-US/docs/Web/API/EventTarget).

## [Events](#events)

This interface has no specific event, but inherits the events of [XMLHttpRequestEventTarget](/en-US/docs/Web/API/XMLHttpRequestEventTarget).

## [Examples](#examples)

### [Uploading a file with a timeout](#uploading_a_file_with_a_timeout)

This allows you to upload a file to a server; it displays a progress bar while the upload is happening as well as a message with the progress and the results, success or failure. An abort button allows to stop an upload.

#### HTML

html

```
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <title>XMLHttpRequestUpload test</title>
    <link rel="stylesheet" href="xhrupload_test.css" />
    <script src="xhrupload_test.js"></script>
  </head>
  <body>
    <main>
      <h1>Upload a file</h1>
      <p>
        <label for="file">File to upload</label><input type="file" id="file" />
      </p>
      <p>
        <progress></progress>
      </p>
      <p>
        <output></output>
      </p>
      <p>
        <button disabled id="abort">Abort</button>
      </p>
    </main>
  </body>
</html>
```

#### CSS

css

```
body {
  background-color: lightblue;
}

main {
  margin: 50px auto;
  text-align: center;
}

#file {
  display: none;
}

label[for="file"] {
  background-color: lightgrey;
  padding: 10px;
}

progress {
  display: none;
}

progress.visible {
  display: inline;
}
```

#### JavaScript

js

```
const fileInput = document.getElementById("file");
const progressBar = document.querySelector("progress");
const log = document.querySelector("output");
const abortButton = document.getElementById("abort");

fileInput.addEventListener("change", () => {
  const xhr = new XMLHttpRequest();
  xhr.timeout = 2000; // 2 seconds

  // Link abort button
  abortButton.addEventListener(
    "click",
    () => {
      xhr.abort();
    },
    { once: true },
  );

  // When the upload starts, we display the progress bar
  xhr.upload.addEventListener("loadstart", (event) => {
    progressBar.classList.add("visible");
    progressBar.value = 0;
    progressBar.max = event.total;
    log.textContent = "Uploading (0%)…";
    abortButton.disabled = false;
  });

  // Each time a progress event is received, we update the bar
  xhr.upload.addEventListener("progress", (event) => {
    progressBar.value = event.loaded;
    log.textContent = `Uploading (${(
      (event.loaded / event.total) *
      100
    ).toFixed(2)}%)…`;
  });

  // When the upload is finished, we hide the progress bar.
  xhr.upload.addEventListener("loadend", (event) => {
    progressBar.classList.remove("visible");
    if (event.loaded !== 0) {
      log.textContent = "Upload finished.";
    }
    abortButton.disabled = true;
  });

  // In case of an error, an abort, or a timeout, we hide the progress bar
  // Note that these events can be listened to on the xhr object too
  function errorAction(event) {
    progressBar.classList.remove("visible");
    log.textContent = `Upload failed: ${event.type}`;
  }
  xhr.upload.addEventListener("error", errorAction);
  xhr.upload.addEventListener("abort", errorAction);
  xhr.upload.addEventListener("timeout", errorAction);

  // Build the payload
  const fileData = new FormData();
  fileData.append("file", fileInput.files[0]);

  // Theoretically, event listeners could be set after the open() call
  // but browsers are buggy here
  xhr.open("POST", "upload_test.php", true);

  // Note that the event listener must be set before sending (as it is a preflighted request)
  xhr.send(fileData);
});
```

## [Specifications](#specifications)

Specification
[XMLHttpRequest# xmlhttprequestupload](https://xhr.spec.whatwg.org/#xmlhttprequestupload)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 11, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/XMLHttpRequestUpload/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xmlhttprequestupload/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXMLHttpRequestUpload&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxmlhttprequestupload%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXMLHttpRequestUpload%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxmlhttprequestupload%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F116577234db1d6275c74a8bb879fce54d944f4ed%0A*+Document+last+modified%3A+2025-09-11T16%3A42%3A02.000Z%0A%0A%3C%2Fdetails%3E)
