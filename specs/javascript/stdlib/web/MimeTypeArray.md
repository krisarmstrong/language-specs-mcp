# MimeTypeArray

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

The `MimeTypeArray` interface returns an array of [MimeType](/en-US/docs/Web/API/MimeType) instances, each of which contains information about a supported browser plugins. This object is returned by the deprecated [Navigator.mimeTypes](/en-US/docs/Web/API/Navigator/mimeTypes) property.

This interface was an [attempt to create an unmodifiable list](https://stackoverflow.com/questions/74630989/why-use-domstringlist-rather-than-an-array/74641156#74641156) and only continues to be supported to not break code that's already using it. Modern APIs represent list structures using types based on JavaScript [arrays](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array), thus making many array methods available, and at the same time imposing additional semantics on their usage (such as making their items read-only).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

`MimeTypeArray.length`Deprecated

The number of items in the array.

## [Instance methods](#instance_methods)

`MimeTypeArray.item()`Deprecated

Returns the `MimeType` object with the specified index.

`MimeTypeArray.namedItem()`Deprecated

Returns the `MimeType` object with the specified name.

## [Example](#example)

The following example tests whether a plugin is available for the 'application/pdf' mime type and if so, logs its description.

js

```
const mimeTypes = navigator.mimeTypes;
const pdf = mimeTypes.namedItem("application/pdf");

if (pdf) {
  console.log(pdf.description);
}
```

## [Specifications](#specifications)

Specification
[HTML# mimetypearray](https://html.spec.whatwg.org/multipage/system-state.html#mimetypearray)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 21, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/MimeTypeArray/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mimetypearray/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMimeTypeArray&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmimetypearray%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMimeTypeArray%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmimetypearray%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcfa628aedb53a83b315943ef19fa6c73298fb7d5%0A*+Document+last+modified%3A+2024-06-21T18%3A41%3A27.000Z%0A%0A%3C%2Fdetails%3E)
