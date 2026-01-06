# LargestContentfulPaint

 Baseline  2025 Newly available

 Since ⁨December 2025⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FLargestContentfulPaint&level=low)

The `LargestContentfulPaint` interface provides timing information about the largest image or text paint before user input on a web page.

## In this article

- [Description](#description)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Description](#description)

The key moment this API provides is the [Largest Contentful Paint](/en-US/docs/Glossary/Largest_contentful_paint) (LCP) metric. It provides the render time of the largest image or text block visible within the viewport, recorded from when the page first begins to load. The following elements are considered when determining the LCP:

- [<img>](/en-US/docs/Web/HTML/Reference/Elements/img) elements.
- [<image>](/en-US/docs/Web/SVG/Reference/Element/image) elements inside an SVG.
- The poster images of [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) elements.
- Elements with a [background-image](/en-US/docs/Web/CSS/Reference/Properties/background-image).
- Groups of text nodes, such as [<p>](/en-US/docs/Web/HTML/Reference/Elements/p).

To measure render times of other elements, use the [PerformanceElementTiming](/en-US/docs/Web/API/PerformanceElementTiming) API.

Additional key paint moments are provided by the [PerformancePaintTiming](/en-US/docs/Web/API/PerformancePaintTiming) API:

- [First Paint](/en-US/docs/Glossary/First_paint) (FP): Time when anything is rendered. Note that the marking of the first paint is optional, not all user agents report it.
- [First Contentful Paint](/en-US/docs/Glossary/First_contentful_paint) (FCP): Time when the first bit of DOM text or image content is rendered.

`LargestContentfulPaint` inherits from [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry).

To get an accurate measurement of render time for cross-origin resources, set the [Timing-Allow-Origin](/en-US/docs/Web/HTTP/Reference/Headers/Timing-Allow-Origin) header.

Developers should use `startTime` instead of `renderTime` as the LCP value, as the `renderTime` may not be set in some browsers.

See [Cross-origin image render time](/en-US/docs/Web/API/LargestContentfulPaint/renderTime#cross-origin_image_render_time) and [Use startTime over renderTime](/en-US/docs/Web/API/LargestContentfulPaint/renderTime#use_starttime_over_rendertime) for more details.

## [Instance properties](#instance_properties)

This interface extends the following [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry) properties by qualifying and constraining the properties as follows:

[PerformanceEntry.entryType](/en-US/docs/Web/API/PerformanceEntry/entryType)Read onlyExperimental

Returns `"largest-contentful-paint"`.

[PerformanceEntry.name](/en-US/docs/Web/API/PerformanceEntry/name)Read onlyExperimental

Always returns an empty string.

[PerformanceEntry.startTime](/en-US/docs/Web/API/PerformanceEntry/startTime)Read onlyExperimental

Returns the value of this entry's [renderTime](/en-US/docs/Web/API/LargestContentfulPaint/renderTime) if it is not `0`, otherwise the value of this entry's [loadTime](/en-US/docs/Web/API/LargestContentfulPaint/loadTime).

[PerformanceEntry.duration](/en-US/docs/Web/API/PerformanceEntry/duration)Read onlyExperimental

Returns `0`, as `duration` is not applicable to this interface.

It also supports the following properties:

[LargestContentfulPaint.element](/en-US/docs/Web/API/LargestContentfulPaint/element)Read only

The element that is the current largest contentful paint.

[LargestContentfulPaint.renderTime](/en-US/docs/Web/API/LargestContentfulPaint/renderTime)Read only

The time the element was rendered to the screen. May be a coarsened value or `0` if the element is a cross-origin image loaded without the `Timing-Allow-Origin` header.

[LargestContentfulPaint.loadTime](/en-US/docs/Web/API/LargestContentfulPaint/loadTime)Read only

The time the element was loaded.

[LargestContentfulPaint.size](/en-US/docs/Web/API/LargestContentfulPaint/size)Read only

The intrinsic size of the element returned as the area (width * height).

[LargestContentfulPaint.id](/en-US/docs/Web/API/LargestContentfulPaint/id)Read only

The id of the element. This property returns an empty string when there is no id.

[LargestContentfulPaint.url](/en-US/docs/Web/API/LargestContentfulPaint/url)Read only

If the element is an image, the request url of the image.

## [Instance methods](#instance_methods)

This interface also inherits methods from [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry).

[LargestContentfulPaint.toJSON()](/en-US/docs/Web/API/LargestContentfulPaint/toJSON)

Returns a JSON representation of the `LargestContentfulPaint` object.

## [Examples](#examples)

### [Observing the largest contentful paint](#observing_the_largest_contentful_paint)

In the following example, an observer is registered to get the largest contentful paint while the page is loading. The `buffered` flag is used to access data from before observer creation.

The LCP API analyzes all content it finds (including content that is removed from the DOM). When new largest content is found, it creates a new entry. It stops searching for larger content when scroll or input events occur, since these events likely introduce new content on the website. Thus the LCP is the last performance entry reported by the observer.

js

```
const observer = new PerformanceObserver((list) => {
  const entries = list.getEntries();
  const lastEntry = entries[entries.length - 1]; // Use the latest LCP candidate
  console.log("LCP:", lastEntry.startTime);
  console.log(lastEntry);
});
observer.observe({ type: "largest-contentful-paint", buffered: true });
```

## [Specifications](#specifications)

Specification
[Largest Contentful Paint# sec-largest-contentful-paint-interface](https://w3c.github.io/largest-contentful-paint/#sec-largest-contentful-paint-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Largest Contentful Paint](/en-US/docs/Glossary/Largest_contentful_paint)
- [First Contentful Paint](/en-US/docs/Glossary/First_contentful_paint)
- [First Paint](/en-US/docs/Glossary/First_paint)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 17, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/LargestContentfulPaint/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/largestcontentfulpaint/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FLargestContentfulPaint&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Flargestcontentfulpaint%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FLargestContentfulPaint%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Flargestcontentfulpaint%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6e96f90bcaf87173bae82bde6f04c61d0bb21119%0A*+Document+last+modified%3A+2025-09-17T00%3A36%3A01.000Z%0A%0A%3C%2Fdetails%3E)
