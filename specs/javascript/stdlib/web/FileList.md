# FileList

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileList&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `FileList` interface represents an object of this type returned by the `files` property of the HTML [<input>](/en-US/docs/Web/HTML/Reference/Elements/input) element; this lets you access the list of files selected with the `<input type="file">` element. It's also used for a list of files dropped into web content when using the drag and drop API; see the [DataTransfer](/en-US/docs/Web/API/DataTransfer) object for details on this usage.

All `<input>` element nodes have a `files` attribute of type `FileList` on them which allows access to the items in this list. For example, if the HTML includes the following file input:

html

```
<input id="fileItem" type="file" />
```

The following line of code fetches the first file in the node's file list as a [File](/en-US/docs/Web/API/File) object:

js

```
const file = document.getElementById("fileItem").files[0];
```

This interface was an [attempt to create an unmodifiable list](https://stackoverflow.com/questions/74630989/why-use-domstringlist-rather-than-an-array/74641156#74641156) and only continues to be supported to not break code that's already using it. Modern APIs represent list structures using types based on JavaScript [arrays](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array), thus making many array methods available, and at the same time imposing additional semantics on their usage (such as making their items read-only).

These historical reasons do not mean that you as a developer should avoid `FileList`. You don't create `FileList` objects yourself, but you get them from APIs such as [HTMLInputElement.files](/en-US/docs/Web/API/HTMLInputElement/files), and these APIs are not deprecated. However, be careful of the semantic differences from a real array.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[length](/en-US/docs/Web/API/FileList/length)Read only

A read-only value indicating the number of files in the list.

## [Instance methods](#instance_methods)

[item()](/en-US/docs/Web/API/FileList/item)

Returns a [File](/en-US/docs/Web/API/File) object representing the file at the specified index in the file list.

## [Example](#example)

### [Logging filenames](#logging_filenames)

In this example, we log the names of all the files selected by the user.

#### HTML

html

```
<input id="myfiles" multiple type="file" />
<pre class="output">Selected files:</pre>
```

#### CSS

css

```
.output {
  overflow: scroll;
  margin: 1rem 0;
  height: 200px;
}
```

#### JavaScript

js

```
const output = document.querySelector(".output");
const fileInput = document.querySelector("#myfiles");

fileInput.addEventListener("change", () => {
  for (const file of fileInput.files) {
    output.innerText += `\n${file.name}`;
  }
});
```

#### Result

## [Specifications](#specifications)

Specification
[File API# filelist-section](https://w3c.github.io/FileAPI/#filelist-section)
[HTML# dom-input-files-dev](https://html.spec.whatwg.org/multipage/input.html#dom-input-files-dev)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using files from web applications](/en-US/docs/Web/API/File_API/Using_files_from_web_applications)
- [File](/en-US/docs/Web/API/File)
- [FileReader](/en-US/docs/Web/API/FileReader)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 21, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/FileList/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/filelist/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileList&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffilelist%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileList%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffilelist%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcfa628aedb53a83b315943ef19fa6c73298fb7d5%0A*+Document+last+modified%3A+2024-06-21T18%3A41%3A27.000Z%0A%0A%3C%2Fdetails%3E)
