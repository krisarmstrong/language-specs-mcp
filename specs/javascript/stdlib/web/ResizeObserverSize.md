# ResizeObserverSize

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2022⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FResizeObserverSize&level=high)

The `ResizeObserverSize` interface of the [Resize Observer API](/en-US/docs/Web/API/Resize_Observer_API) is used by the [ResizeObserverEntry](/en-US/docs/Web/API/ResizeObserverEntry) interface to access the box sizing properties of the element being observed.

Note: In [multi-column layout](/en-US/docs/Web/CSS/Guides/Multicol_layout), which is a fragmented context, the sizing returned by `ResizeObserverSize` will be the size of the first column.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[ResizeObserverSize.blockSize](/en-US/docs/Web/API/ResizeObserverSize/blockSize)Read only

The length of the observed element's border box in the block dimension. For boxes with a horizontal [writing-mode](/en-US/docs/Web/CSS/Reference/Properties/writing-mode), this is the vertical dimension, or height; if the writing-mode is vertical, this is the horizontal dimension, or width.

[ResizeObserverSize.inlineSize](/en-US/docs/Web/API/ResizeObserverSize/inlineSize)Read only

The length of the observed element's border box in the inline dimension. For boxes with a horizontal [writing-mode](/en-US/docs/Web/CSS/Reference/Properties/writing-mode), this is the horizontal dimension, or width; if the writing-mode is vertical, this is the vertical dimension, or height.

Note: For more explanation of writing modes and block and inline dimensions, read [Handling different text directions](/en-US/docs/Learn_web_development/Core/Styling_basics/Handling_different_text_directions).

## [Examples](#examples)

In this example the [ResizeObserverEntry.contentBoxSize](/en-US/docs/Web/API/ResizeObserverEntry/contentBoxSize) property returns a `ResizeObserverSize` object. This is an array containing the sizing information for the content box of the observed element.

js

```
const resizeObserver = new ResizeObserver((entries) => {
  for (const entry of entries) {
    console.log(entry.contentBoxSize[0]); // a ResizeObserverSize
  }
});

resizeObserver.observe(divElem);
```

## [Specifications](#specifications)

Specification
[Resize Observer# resizeobserversize](https://drafts.csswg.org/resize-observer/#resizeobserversize)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ResizeObserverSize/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/resizeobserversize/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FResizeObserverSize&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fresizeobserversize%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FResizeObserverSize%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fresizeobserversize%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
