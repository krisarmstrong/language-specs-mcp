# OverconstrainedError

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FOverconstrainedError&level=not)

The `OverconstrainedError` interface of the [Media Capture and Streams API](/en-US/docs/Web/API/Media_Capture_and_Streams_API) indicates that the set of desired capabilities for the current [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) cannot currently be met. When this event is thrown on a MediaStreamTrack, it is muted until either the current constraints can be established or until satisfiable constraints are applied.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[OverconstrainedError()](/en-US/docs/Web/API/OverconstrainedError/OverconstrainedError)

Creates a new `OverconstrainedError` object.

## [Instance properties](#instance_properties)

Also inherits properties from its parent interface, [DOMException](/en-US/docs/Web/API/DOMException).

[OverconstrainedError.constraint](/en-US/docs/Web/API/OverconstrainedError/constraint)Read only

Returns the constraint that was supplied in the constructor, meaning the constraint that was not satisfied.

## [Instance methods](#instance_methods)

Also inherits methods from its parent interface, [DOMException](/en-US/docs/Web/API/DOMException).

## [Specifications](#specifications)

Specification
[Media Capture and Streams# overconstrainederror-interface](https://w3c.github.io/mediacapture-main/#overconstrainederror-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 17, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/OverconstrainedError/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/overconstrainederror/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FOverconstrainedError&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Foverconstrainederror%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FOverconstrainedError%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Foverconstrainederror%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3178e38ae397032bd9c44d5ec6f8192ee391b56a%0A*+Document+last+modified%3A+2023-12-17T06%3A53%3A42.000Z%0A%0A%3C%2Fdetails%3E)
