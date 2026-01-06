# Encrypted Media Extensions API

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2019⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEncrypted_Media_Extensions_API&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The Encrypted Media Extensions API provides interfaces for controlling the playback of content which is subject to a digital restrictions management scheme.

Access to this API is provided through [Navigator.requestMediaKeySystemAccess()](/en-US/docs/Web/API/Navigator/requestMediaKeySystemAccess).

## In this article

- [Interfaces](#interfaces)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Interfaces](#interfaces)

[MediaEncryptedEvent](/en-US/docs/Web/API/MediaEncryptedEvent)

Represents a specific [encrypted](/en-US/docs/Web/API/HTMLMediaElement/encrypted_event) event thrown when a [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement) encounters some initialization data.

[MediaKeyMessageEvent](/en-US/docs/Web/API/MediaKeyMessageEvent)

Contains the content and related data when the content decryption module (CDM) generates a message for the session.

[MediaKeys](/en-US/docs/Web/API/MediaKeys)

Represents a set of keys that an associated [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement) can use for decryption of media data during playback.

[MediaKeySession](/en-US/docs/Web/API/MediaKeySession)

Represents a context for message exchange with a content decryption module (CDM).

[MediaKeyStatusMap](/en-US/docs/Web/API/MediaKeyStatusMap)

A read-only map of media key statuses by key IDs.

[MediaKeySystemAccess](/en-US/docs/Web/API/MediaKeySystemAccess)

Provides access to a key system for decryption and/or a content protection provider.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

The Encrypted Media Extensions API extends the following APIs, adding the listed features.

#### HTMLMediaElement

[HTMLMediaElement.mediaKeys](/en-US/docs/Web/API/HTMLMediaElement/mediaKeys)Read only

Provides a [MediaKeys](/en-US/docs/Web/API/MediaKeys) object that represents the set of keys that the element can use for decryption of media data during playback.

[HTMLMediaElement.setMediaKeys()](/en-US/docs/Web/API/HTMLMediaElement/setMediaKeys)

Sets the [MediaKeys](/en-US/docs/Web/API/MediaKeys) that will be used to decrypt media during playback.

[encrypted event](/en-US/docs/Web/API/HTMLMediaElement/encrypted_event)

Event that is fired on a [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement) when initialization data is encountered in the media, indicating that it is encrypted.

#### Navigator

[Navigator.requestMediaKeySystemAccess()](/en-US/docs/Web/API/Navigator/requestMediaKeySystemAccess)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfils to a [MediaKeySystemAccess](/en-US/docs/Web/API/MediaKeySystemAccess) object that can be used to access a particular media key system, which can in turn be used to create keys for decrypting a media stream.

## [Specifications](#specifications)

Specification
[Encrypted Media Extensions# navigator-extension-requestmediakeysystemaccess](https://w3c.github.io/encrypted-media/#navigator-extension-requestmediakeysystemaccess)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 19, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Encrypted_Media_Extensions_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/encrypted_media_extensions_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEncrypted_Media_Extensions_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fencrypted_media_extensions_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEncrypted_Media_Extensions_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fencrypted_media_extensions_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7b565c5f4610bea19c844f35532853624d87cde3%0A*+Document+last+modified%3A+2024-07-19T03%3A42%3A38.000Z%0A%0A%3C%2Fdetails%3E)
