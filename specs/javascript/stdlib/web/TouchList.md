# TouchList

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTouchList&level=not)

The `TouchList` interface represents a list of contact points on a touch surface. For example, if the user has three fingers on the touch surface (such as a screen or trackpad), the corresponding `TouchList` object would have one [Touch](/en-US/docs/Web/API/Touch) object for each finger, for a total of three entries.

This interface was an [attempt to create an unmodifiable list](https://stackoverflow.com/questions/74630989/why-use-domstringlist-rather-than-an-array/74641156#74641156) and only continues to be supported to not break code that's already using it. Modern APIs represent list structures using types based on JavaScript [arrays](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array), thus making many array methods available, and at the same time imposing additional semantics on their usage (such as making their items read-only).

These historical reasons do not mean that you as a developer should avoid `TouchList`. You don't create `TouchList` objects yourself, but you get them from APIs such as [TouchEvent.targetTouches](/en-US/docs/Web/API/TouchEvent/targetTouches), and these APIs are not deprecated. However, be careful of the semantic differences from a real array.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[TouchList.length](/en-US/docs/Web/API/TouchList/length)Read only

The number of [Touch](/en-US/docs/Web/API/Touch) objects in the `TouchList`.

## [Instance methods](#instance_methods)

[TouchList.item()](/en-US/docs/Web/API/TouchList/item)

Returns the [Touch](/en-US/docs/Web/API/Touch) object at the specified index in the list.

## [Example](#example)

See the [example on the main Touch events article](/en-US/docs/Web/API/Touch_events#examples).

## [Specifications](#specifications)

Specification
[Touch Events# touchlist-interface](https://w3c.github.io/touch-events/#touchlist-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Touch events](/en-US/docs/Web/API/Touch_events)
- [Document.createTouchList()](/en-US/docs/Web/API/Document/createTouchList)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 21, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/TouchList/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/touchlist/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTouchList&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftouchlist%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTouchList%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftouchlist%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F36761819df2ebdd4e3dcc9ae6007029dec71fac0%0A*+Document+last+modified%3A+2025-10-21T22%3A19%3A42.000Z%0A%0A%3C%2Fdetails%3E)
