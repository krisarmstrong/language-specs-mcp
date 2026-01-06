# PerformanceElementTiming

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceElementTiming&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `PerformanceElementTiming` interface contains render timing information for image and text node elements the developer annotated with an [elementtiming](/en-US/docs/Web/HTML/Reference/Attributes/elementtiming) attribute for observation.

## In this article

- [Description](#description)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Description](#description)

The aim of the Element Timing API is to give web developers or analytics tools the ability to measure rendering timestamps of critical elements on a page.

The API supports timing information on the following elements:

- [<img>](/en-US/docs/Web/HTML/Reference/Elements/img) elements,
- [<image>](/en-US/docs/Web/SVG/Reference/Element/image) elements inside an [<svg>](/en-US/docs/Web/SVG/Reference/Element/svg),
- [poster](/en-US/docs/Web/HTML/Reference/Elements/video#poster) images of [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) elements,
- elements which have a contentful [background-image](/en-US/docs/Web/CSS/Reference/Properties/background-image) property with a URL value for a resource that is actually available, and
- groups of text nodes, such as a [<p>](/en-US/docs/Web/HTML/Reference/Elements/p).

The author flags an element for observation by adding the [elementtiming](/en-US/docs/Web/HTML/Reference/Attributes/elementtiming) attribute on the element.

`PerformanceElementTiming` inherits from [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry).

## [Instance properties](#instance_properties)

This interface extends the following [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry) properties for event timing performance entry types by qualifying them as follows:

[PerformanceEntry.duration](/en-US/docs/Web/API/PerformanceEntry/duration)Read onlyExperimental

Always returns `0` as `duration` does not apply to this interface.

[PerformanceEntry.entryType](/en-US/docs/Web/API/PerformanceEntry/entryType)Read onlyExperimental

Always returns `"element"`.

[PerformanceEntry.name](/en-US/docs/Web/API/PerformanceEntry/name)Read onlyExperimental

Returns `"image-paint"` for images and `"text-paint"` for text.

[PerformanceEntry.startTime](/en-US/docs/Web/API/PerformanceEntry/startTime)Read onlyExperimental

Returns the value of this entry's [renderTime](/en-US/docs/Web/API/PerformanceElementTiming/renderTime) if it is not `0`, otherwise the value of this entry's [loadTime](/en-US/docs/Web/API/PerformanceElementTiming/loadTime).

This interface also supports the following properties:

[PerformanceElementTiming.element](/en-US/docs/Web/API/PerformanceElementTiming/element)Read onlyExperimental

An [Element](/en-US/docs/Web/API/Element) representing the element we are returning information about.

[PerformanceElementTiming.id](/en-US/docs/Web/API/PerformanceElementTiming/id)Read onlyExperimental

A string which is the [id](/en-US/docs/Web/HTML/Reference/Global_attributes/id) of the element.

[PerformanceElementTiming.identifier](/en-US/docs/Web/API/PerformanceElementTiming/identifier)Read onlyExperimental

A string which is the value of the [elementtiming](/en-US/docs/Web/HTML/Reference/Attributes/for) attribute on the element.

[PerformanceElementTiming.intersectionRect](/en-US/docs/Web/API/PerformanceElementTiming/intersectionRect)Read onlyExperimental

A [DOMRectReadOnly](/en-US/docs/Web/API/DOMRectReadOnly) which is the rectangle of the element within the viewport.

[PerformanceElementTiming.loadTime](/en-US/docs/Web/API/PerformanceElementTiming/loadTime)Read onlyExperimental

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) with the loadTime of the element.

[PerformanceElementTiming.naturalHeight](/en-US/docs/Web/API/PerformanceElementTiming/naturalHeight)Read onlyExperimental

An unsigned 32-bit integer (unsigned long) which is the intrinsic height of the image if this is applied to an image, 0 for text.

[PerformanceElementTiming.naturalWidth](/en-US/docs/Web/API/PerformanceElementTiming/naturalWidth)Read onlyExperimental

An unsigned 32-bit integer (unsigned long) which is the intrinsic width of the image if this is applied to an image, 0 for text.

[PerformanceElementTiming.renderTime](/en-US/docs/Web/API/PerformanceElementTiming/renderTime)Read onlyExperimental

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) with the renderTime of the element.

[PerformanceElementTiming.url](/en-US/docs/Web/API/PerformanceElementTiming/url)Read onlyExperimental

A string which is the initial URL of the resources request for images, 0 for text.

## [Instance methods](#instance_methods)

[PerformanceElementTiming.toJSON()](/en-US/docs/Web/API/PerformanceElementTiming/toJSON)Experimental

Returns a JSON representation of the `PerformanceElementTiming` object.

## [Examples](#examples)

### [Observing render time of specific elements](#observing_render_time_of_specific_elements)

In this example two elements are being observed by adding the [elementtiming](/en-US/docs/Web/HTML/Reference/Attributes/elementtiming) attribute. A [PerformanceObserver](/en-US/docs/Web/API/PerformanceObserver) is registered to get all performance entries of type `"element"` and the `buffered` flag is used to access data from before observer creation.

html

```
<img src="image.jpg" elementtiming="big-image" />
<p elementtiming="text" id="text-id">text here</p>
```

js

```
const observer = new PerformanceObserver((list) => {
  list.getEntries().forEach((entry) => {
    console.log(entry);
  });
});
observer.observe({ type: "element", buffered: true });
```

Two entries will be output to the console. The first containing details of the image, the second with details of the text node.

## [Specifications](#specifications)

Specification
[Element Timing API# sec-performance-element-timing](https://w3c.github.io/element-timing/#sec-performance-element-timing)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [elementtiming](/en-US/docs/Web/HTML/Reference/Attributes/elementtiming) HTML attribute

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 10, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/PerformanceElementTiming/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/performanceelementtiming/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceElementTiming&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fperformanceelementtiming%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceElementTiming%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fperformanceelementtiming%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe9b6cd1b7fa8612257b72b2a85a96dd7d45c0200%0A*+Document+last+modified%3A+2025-04-10T14%3A56%3A07.000Z%0A%0A%3C%2Fdetails%3E)
