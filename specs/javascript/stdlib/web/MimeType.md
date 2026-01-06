# MimeType

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

The `MimeType` interface provides contains information about a MIME type associated with a particular plugin. [Navigator.mimeTypes](/en-US/docs/Web/API/Navigator/mimeTypes) returns an array of this object.

## In this article

- [Instance properties](#instance_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

`MimeType.type`Deprecated

Returns the MIME type of the associated plugin.

`MimeType.description`Deprecated

Returns a description of the associated plugin or an empty string if there is none.

`MimeType.suffixes`Deprecated

A string containing valid file extensions for the data displayed by the plugin, or an empty string if an extension is not valid for the particular module. For example, a browser's content decryption module may appear in the plugin list but support more file extensions than can be anticipated. It might therefore return an empty string.

`MimeType.enabledPlugin`Deprecated

Returns an instance of [Plugin](/en-US/docs/Web/API/Plugin) containing information about the plugin itself.

## [Specifications](#specifications)

Specification
[HTML# mimetype](https://html.spec.whatwg.org/multipage/system-state.html#mimetype)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 20, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/MimeType/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mimetype/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMimeType&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmimetype%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMimeType%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmimetype%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0d8d3980dc8b8267b60e899c41a76a2832556cbc%0A*+Document+last+modified%3A+2023-02-20T04%3A32%3A03.000Z%0A%0A%3C%2Fdetails%3E)
