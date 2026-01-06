# MediaKeyMessageEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2019⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaKeyMessageEvent&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `MediaKeyMessageEvent` interface of the [Encrypted Media Extensions API](/en-US/docs/Web/API/Encrypted_Media_Extensions_API) contains the content and related data when the content decryption module generates a message for the session.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[MediaKeyMessageEvent()](/en-US/docs/Web/API/MediaKeyMessageEvent/MediaKeyMessageEvent)

Creates a new instance of `MediaKeyMessageEvent`.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [Event](/en-US/docs/Web/API/Event).

[MediaKeyMessageEvent.message](/en-US/docs/Web/API/MediaKeyMessageEvent/message)Read only

Returns an [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) with a message from the content decryption module. Messages vary by key system.

[MediaKeyMessageEvent.messageType](/en-US/docs/Web/API/MediaKeyMessageEvent/messageType)Read only

Indicates the type of message. May be one of `license-request`, `license-renewal`, `license-release`, or `individualization-request`.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [Event](/en-US/docs/Web/API/Event).

## [Examples](#examples)

js

```
// TBD
```

## [Specifications](#specifications)

Specification
[Encrypted Media Extensions# mediakeymessageevent](https://w3c.github.io/encrypted-media/#mediakeymessageevent)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 17, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/MediaKeyMessageEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mediakeymessageevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaKeyMessageEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmediakeymessageevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaKeyMessageEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmediakeymessageevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fba9a6bebd0e7bf1dd6b5c4eed156d8f1748ade0f%0A*+Document+last+modified%3A+2024-06-17T11%3A12%3A50.000Z%0A%0A%3C%2Fdetails%3E)
