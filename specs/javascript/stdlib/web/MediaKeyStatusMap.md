# MediaKeyStatusMap

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2019⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaKeyStatusMap&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `MediaKeyStatusMap` interface of the [Encrypted Media Extensions API](/en-US/docs/Web/API/Encrypted_Media_Extensions_API) is a read-only map of media key statuses by key IDs.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[MediaKeyStatusMap.size](/en-US/docs/Web/API/MediaKeyStatusMap/size)Read only

Returns the number of key/value pairs in the status map.

## [Instance methods](#instance_methods)

[MediaKeyStatusMap.entries()](/en-US/docs/Web/API/MediaKeyStatusMap/entries)Read only

Returns a new `Iterator` object containing an array of `[key, value]` for each element in the status map, in insertion order.

[MediaKeyStatusMap.forEach()](/en-US/docs/Web/API/MediaKeyStatusMap/forEach)Read only

Calls `callback` once for each key-value pair in the status map, in insertion order. If `argument` is present it will be passed to the callback.

[MediaKeyStatusMap.get()](/en-US/docs/Web/API/MediaKeyStatusMap/get)Read only

Returns the value associated with the given key, or `undefined` if there is none.

[MediaKeyStatusMap.has()](/en-US/docs/Web/API/MediaKeyStatusMap/has)Read only

Returns a boolean asserting whether a value has been associated with the given key.

[MediaKeyStatusMap.keys()](/en-US/docs/Web/API/MediaKeyStatusMap/keys)Read only

Returns a new `Iterator` object containing keys for each element in the status map, in insertion order.

[MediaKeyStatusMap.values()](/en-US/docs/Web/API/MediaKeyStatusMap/values)Read only

Returns a new `Iterator` object containing values for each element in the status map, in insertion order.

[MediaKeyStatusMap[Symbol.iterator]() Read only](#mediakeystatusmapsymbol.iterator)

Returns a new `Iterator` object containing an array of `[key, value]` for each element in the status map, in insertion order.

## [Specifications](#specifications)

Specification
[Encrypted Media Extensions# mediakeystatusmap-interface](https://w3c.github.io/encrypted-media/#mediakeystatusmap-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/MediaKeyStatusMap/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mediakeystatusmap/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaKeyStatusMap&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmediakeystatusmap%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaKeyStatusMap%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmediakeystatusmap%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F73b2b6ee411ac094b9fc57dafac6f9c232fc20d9%0A*+Document+last+modified%3A+2024-07-26T02%3A14%3A04.000Z%0A%0A%3C%2Fdetails%3E)
