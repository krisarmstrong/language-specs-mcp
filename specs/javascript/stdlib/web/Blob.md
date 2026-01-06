# Blob

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBlob&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `Blob` interface represents a blob, which is a file-like object of immutable, raw data; they can be read as text or binary data, or converted into a [ReadableStream](/en-US/docs/Web/API/ReadableStream) so its methods can be used for processing the data.

Blobs can represent data that isn't necessarily in a JavaScript-native format. The [File](/en-US/docs/Web/API/File) interface is based on `Blob`, inheriting blob functionality and expanding it to support files on the user's system.

## In this article

- [Using blobs](#using_blobs)
- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Using blobs](#using_blobs)

To construct a `Blob` from other non-blob objects and data, use the [Blob()](/en-US/docs/Web/API/Blob/Blob) constructor. To create a blob that contains a subset of another blob's data, use the [slice()](/en-US/docs/Web/API/Blob/slice) method. To obtain a `Blob` object for a file on the user's file system, see the [File](/en-US/docs/Web/API/File) documentation.

The APIs accepting `Blob` objects are also listed in the [File](/en-US/docs/Web/API/File) documentation.

## [Constructor](#constructor)

[Blob()](/en-US/docs/Web/API/Blob/Blob)

Returns a newly created `Blob` object which contains a concatenation of all of the data in the array passed into the constructor.

## [Instance properties](#instance_properties)

[Blob.size](/en-US/docs/Web/API/Blob/size)Read only

The size, in bytes, of the data contained in the `Blob` object.

[Blob.type](/en-US/docs/Web/API/Blob/type)Read only

A string indicating the MIME type of the data contained in the `Blob`. If the type is unknown, this string is empty.

## [Instance methods](#instance_methods)

[Blob.arrayBuffer()](/en-US/docs/Web/API/Blob/arrayBuffer)

Returns a promise that resolves with an [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) containing the entire contents of the `Blob` as binary data.

[Blob.bytes()](/en-US/docs/Web/API/Blob/bytes)

Returns a promise that resolves with a [Uint8Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) containing the contents of the `Blob`.

[Blob.slice()](/en-US/docs/Web/API/Blob/slice)

Returns a new `Blob` object containing the data in the specified range of bytes of the blob on which it's called.

[Blob.stream()](/en-US/docs/Web/API/Blob/stream)

Returns a [ReadableStream](/en-US/docs/Web/API/ReadableStream) that can be used to read the contents of the `Blob`.

[Blob.text()](/en-US/docs/Web/API/Blob/text)

Returns a promise that resolves with a string containing the entire contents of the `Blob` interpreted as UTF-8 text.

## [Examples](#examples)

### [Creating a blob](#creating_a_blob)

The [Blob()](/en-US/docs/Web/API/Blob/Blob) constructor can create blobs from other objects. For example, to construct a blob from a JSON string:

js

```
const obj = { hello: "world" };
const blob = new Blob([JSON.stringify(obj, null, 2)], {
  type: "application/json",
});
```

### [Creating a URL representing the contents of a typed array](#creating_a_url_representing_the_contents_of_a_typed_array)

The following example creates a JavaScript [typed array](/en-US/docs/Web/JavaScript/Guide/Typed_arrays) and creates a new `Blob` containing the typed array's data. It then calls [URL.createObjectURL()](/en-US/docs/Web/API/URL/createObjectURL_static) to convert the blob into a [URL](/en-US/docs/Glossary/URL).

html

```
<p>
  This example creates a typed array containing the ASCII codes for the space
  character through the letter Z, then converts it to an object URL. A link to
  open that object URL is created. Click the link to see the decoded object URL.
</p>
```

The main piece of this code for example purposes is the `typedArrayToURL()` function, which creates a `Blob` from the given typed array and returns an object URL for it. Having converted the data into an object URL, it can be used in a number of ways, including as the value of the [<img>](/en-US/docs/Web/HTML/Reference/Elements/img) element's [src](/en-US/docs/Web/HTML/Reference/Elements/img#src) attribute (assuming the data contains an image, of course).

js

```
function showViewLiveResultButton() {
  if (window.self !== window.top) {
    // Ensure that if our document is in a frame, we get the user
    // to first open it in its own tab or window. Otherwise, this
    // example won't work.
    const p = document.querySelector("p");
    p.textContent = "";
    const button = document.createElement("button");
    button.textContent = "View live result of the example code above";
    p.append(button);
    button.addEventListener("click", () => window.open(location.href));
    return true;
  }
  return false;
}

if (!showViewLiveResultButton()) {
  function typedArrayToURL(typedArray, mimeType) {
    return URL.createObjectURL(
      new Blob([typedArray.buffer], { type: mimeType }),
    );
  }
  const bytes = new Uint8Array(59);

  for (let i = 0; i < 59; i++) {
    bytes[i] = 32 + i;
  }

  const url = typedArrayToURL(bytes, "text/plain");
  const link = document.createElement("a");

  link.href = url;
  link.innerText = "Open the array URL";
  document.body.appendChild(link);
}
```

### [Extracting data from a blob](#extracting_data_from_a_blob)

One way to read content from a `Blob` is to use a [FileReader](/en-US/docs/Web/API/FileReader). The following code reads the content of a `Blob` as a typed array:

js

```
const reader = new FileReader();
reader.addEventListener("loadend", () => {
  // reader.result contains the contents of blob as a typed array
});
reader.readAsArrayBuffer(blob);
```

Another way to read content from a `Blob` is to use a [Response](/en-US/docs/Web/API/Response). The following code reads the content of a `Blob` as text:

js

```
const text = await new Response(blob).text();
```

Or by using [Blob.text()](/en-US/docs/Web/API/Blob/text):

js

```
const text = await blob.text();
```

By using other methods of `FileReader`, it is possible to read the contents of a Blob as a string or a data URL.

## [Specifications](#specifications)

Specification
[File API# blob-section](https://w3c.github.io/FileAPI/#blob-section)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [FileReader](/en-US/docs/Web/API/FileReader)
- [File](/en-US/docs/Web/API/File)
- [URL.createObjectURL()](/en-US/docs/Web/API/URL/createObjectURL_static)
- [Using files from web applications](/en-US/docs/Web/API/File_API/Using_files_from_web_applications)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Blob/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/blob/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBlob&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fblob%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBlob%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fblob%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F562051c4ad20e9ecb5faf905286cdfca545a340d%0A*+Document+last+modified%3A+2025-11-07T03%3A38%3A04.000Z%0A%0A%3C%2Fdetails%3E)
