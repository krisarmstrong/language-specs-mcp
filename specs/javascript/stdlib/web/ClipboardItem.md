# ClipboardItem

 Baseline  2024  * Newly available

 Since ⁨June 2024⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FClipboardItem&level=low)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `ClipboardItem` interface of the [Clipboard API](/en-US/docs/Web/API/Clipboard_API) represents a single item format, used when reading or writing clipboard data using [Clipboard.read()](/en-US/docs/Web/API/Clipboard/read) and [Clipboard.write()](/en-US/docs/Web/API/Clipboard/write) respectively.

The `ClipboardItem` interface enables developers to use a single type to represent a range of different data formats.

Note: The `read()` and `write()` methods can be used to work with text strings and arbitrary data items represented by [Blob](/en-US/docs/Web/API/Blob) instances. However, if you are solely working with text, it is more convenient to use the [Clipboard.readText()](/en-US/docs/Web/API/Clipboard/readText) and [Clipboard.writeText()](/en-US/docs/Web/API/Clipboard/writeText) methods.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[ClipboardItem()](/en-US/docs/Web/API/ClipboardItem/ClipboardItem)

Creates a new `ClipboardItem` object, with the [MIME type](/en-US/docs/Glossary/MIME_type) as the key and the data as the value.

## [Instance properties](#instance_properties)

[types](/en-US/docs/Web/API/ClipboardItem/types)Read only

Returns an [Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) of MIME types available within the `ClipboardItem`.

[presentationStyle](/en-US/docs/Web/API/ClipboardItem/presentationStyle)Read only

Returns one of the following: `"unspecified"`, `"inline"` or `"attachment"`.

## [Static methods](#static_methods)

[ClipboardItem.supports()](/en-US/docs/Web/API/ClipboardItem/supports_static)

Checks whether a given [MIME type](/en-US/docs/Glossary/MIME_type) is supported by the clipboard. This enables a website to detect whether a MIME type is supported before attempting to write data.

## [Instance methods](#instance_methods)

[getType()](/en-US/docs/Web/API/ClipboardItem/getType)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with a [Blob](/en-US/docs/Web/API/Blob) of the requested [MIME type](/en-US/docs/Glossary/MIME_type), or an error if the MIME type is not found.

## [Examples](#examples)

### [Writing text to the clipboard](#writing_text_to_the_clipboard)

In this example we first define two constants containing references to a [<p>](/en-US/docs/Web/HTML/Reference/Elements/p) element containing some text and a [<button>](/en-US/docs/Web/HTML/Reference/Elements/button) element.

Next, we define a function called `copyToClipboard()`. This starts off by storing a `"text/plain"` MIME type in a constant, then creating an object called `clipboardItemData` that contains one property with a key equal to the MIME type and a value of the text we want to copy to the clipboard (the content of the `<p>` element, in this case). Because we are working with text, we can pass it in directly rather than having to create a [Blob](/en-US/docs/Web/API/Blob).

We construct a new `ClipboardItem` object using the [ClipboardItem()](/en-US/docs/Web/API/ClipboardItem/ClipboardItem) constructor, and pass it into the [Clipboard.write()](/en-US/docs/Web/API/Clipboard/write) method to copy the text to the clipboard.

Finally, we add an event listener to the `<button>` so that it runs the function when pressed.

js

```
const textSource = document.querySelector("p");
const copyBtn = document.querySelector("button");

async function copyToClipboard() {
  const type = "text/plain";
  const clipboardItemData = {
    [type]: textSource.textContent,
  };
  const clipboardItem = new ClipboardItem(clipboardItemData);
  await navigator.clipboard.write([clipboardItem]);
}

copyBtn.addEventListener("click", copyToClipboard);
```

### [Writing an image to the clipboard](#writing_an_image_to_the_clipboard)

Here we use [supports()](/en-US/docs/Web/API/ClipboardItem/supports_static) to check whether the `image/svg+xml` MIME data type is supported. If it is, we fetch an SVG image with the [Fetch API](/en-US/docs/Web/API/Fetch_API), and then read it into a [Blob](/en-US/docs/Web/API/Blob), which we can use to create a `ClipboardItem` that is written to the clipboard.

js

```
async function writeClipImg() {
  try {
    if (ClipboardItem.supports("image/svg+xml")) {
      const imgURL = "/my-image.svg";
      const data = await fetch(imgURL);
      const blob = await data.blob();
      await navigator.clipboard.write([
        new ClipboardItem({
          [blob.type]: blob,
        }),
      ]);
      console.log("Fetched image copied.");
    } else {
      console.log("SVG images are not supported by the clipboard.");
    }
  } catch (err) {
    console.error(err.name, err.message);
  }
}
```

### [Reading from the clipboard](#reading_from_the_clipboard)

Here we're returning all items on the clipboard via the [clipboard.read()](/en-US/docs/Web/API/Clipboard/read) method. Then utilizing the [ClipboardItem.types](/en-US/docs/Web/API/ClipboardItem/types) property to set the [getType()](/en-US/docs/Web/API/ClipboardItem/getType) argument and return the corresponding blob object.

js

```
async function getClipboardContents() {
  try {
    const clipboardItems = await navigator.clipboard.read();

    for (const clipboardItem of clipboardItems) {
      for (const type of clipboardItem.types) {
        const blob = await clipboardItem.getType(type);
        // we can now use blob here
      }
    }
  } catch (err) {
    console.error(err.name, err.message);
  }
}
```

## [Specifications](#specifications)

Specification
[Clipboard API and events# clipboarditem](https://w3c.github.io/clipboard-apis/#clipboarditem)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Clipboard API](/en-US/docs/Web/API/Clipboard_API)
- [Image support for Async Clipboard article](https://web.dev/articles/async-clipboard)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jan 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ClipboardItem/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/clipboarditem/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FClipboardItem&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fclipboarditem%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FClipboardItem%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fclipboarditem%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Feaa5b39f80d5fac0e5bf182679dc658b7083d15b%0A*+Document+last+modified%3A+2025-01-27T15%3A36%3A38.000Z%0A%0A%3C%2Fdetails%3E)
