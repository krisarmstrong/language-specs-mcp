# Fence

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFence&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `Fence` interface of the [Fenced Frame API](/en-US/docs/Web/API/Fenced_frame_API) contains several functions relevant to [<fencedframe>](/en-US/docs/Web/HTML/Reference/Elements/fencedframe) functionality.

`Fence` objects are accessed through the [Window.fence](/en-US/docs/Web/API/Window/fence) property, but they are only available to documents embedded inside [<fencedframe>](/en-US/docs/Web/HTML/Reference/Elements/fencedframe)s (loaded via [FencedFrameConfig](/en-US/docs/Web/API/FencedFrameConfig)s) or [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe)s (loaded via opaque URNs).

Note: See [How do <fencedframe>s work?](/en-US/docs/Web/API/Fenced_frame_API#how_do_fencedframes_work) for some description around `FencedFrameConfig`s and opaque URNs.

## In this article

- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

[getNestedConfigs()](/en-US/docs/Web/API/Fence/getNestedConfigs)Experimental

Returns the [FencedFrameConfig](/en-US/docs/Web/API/FencedFrameConfig)s loaded into `<fencedframe>`s embedded inside the current `<fencedframe>`.

[reportEvent()](/en-US/docs/Web/API/Fence/reportEvent)Experimental

Triggers the submission of report data via a [beacon](/en-US/docs/Web/API/Beacon_API) to one ore more specific URLs registered via the `registerAdBeacon()` method of the [Protected Audience API](https://privacysandbox.google.com/private-advertising/protected-audience), for the purpose of collecting ad auction results.

[setReportEventDataForAutomaticBeacons()](/en-US/docs/Web/API/Fence/setReportEventDataForAutomaticBeacons)Experimental

Specifies event data that will be sent when a navigation occurs inside a `<fencedframe>`. This data will be sent via an automatic beacon to one or more specific URLs registered via the `registerAdBeacon()` method of the [Protected Audience API](https://privacysandbox.google.com/private-advertising/protected-audience), for the purpose of collecting reporting data for ad auction results.

## [Examples](#examples)

js

```
window.fence.reportEvent({
  eventType: "click",
  eventData: JSON.stringify({ clickX: "123", clickY: "456" }),
  destination: ["buyer", "seller"],
});
```

## [Specifications](#specifications)

Specification
[Fenced Frame# fence-interface](https://wicg.github.io/fenced-frame/#fence-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Fenced frames](https://privacysandbox.google.com/private-advertising/fenced-frame) on privacysandbox.google.com
- [The Privacy Sandbox](https://privacysandbox.google.com/) on privacysandbox.google.com

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 4, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Fence/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/fence/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFence&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffence%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFence%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffence%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa6c32a2d0add510c95ef74e85bd8e17551d508b6%0A*+Document+last+modified%3A+2025-04-04T01%3A11%3A05.000Z%0A%0A%3C%2Fdetails%3E)
