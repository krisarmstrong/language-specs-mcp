# MediaEncryptedEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2019⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaEncryptedEvent&level=high)

The `MediaEncryptedEvent` interface of the [Encrypted Media Extensions API](/en-US/docs/Web/API/Encrypted_Media_Extensions_API) contains the information associated with an [encrypted](/en-US/docs/Web/API/HTMLMediaElement/encrypted_event) event sent to a [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement) when some initialization data is encountered in the media.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[MediaEncryptedEvent()](/en-US/docs/Web/API/MediaEncryptedEvent/MediaEncryptedEvent)

Creates a new instance of a `MediaEncryptedEvent` object.

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent, [Event](/en-US/docs/Web/API/Event).

[MediaEncryptedEvent.initDataType](/en-US/docs/Web/API/MediaEncryptedEvent/initDataType)Read only

Returns a case-sensitive string with the type of the format of the initialization data found.

[MediaEncryptedEvent.initData](/en-US/docs/Web/API/MediaEncryptedEvent/initData)Read only

Returns an [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) containing the initialization data found. If there is no initialization data associated with the format, it returns `null`.

## [Instance methods](#instance_methods)

This interface doesn't provide any specific methods, but inherits methods from its parent, [Event](/en-US/docs/Web/API/Event).

## [Specifications](#specifications)

Specification
[Encrypted Media Extensions# mediaencryptedevent](https://w3c.github.io/encrypted-media/#mediaencryptedevent)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 17, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/MediaEncryptedEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mediaencryptedevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaEncryptedEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmediaencryptedevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaEncryptedEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmediaencryptedevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fba9a6bebd0e7bf1dd6b5c4eed156d8f1748ade0f%0A*+Document+last+modified%3A+2024-06-17T11%3A12%3A50.000Z%0A%0A%3C%2Fdetails%3E)
