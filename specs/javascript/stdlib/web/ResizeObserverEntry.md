# ResizeObserverEntry

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FResizeObserverEntry&level=high)

The `ResizeObserverEntry` interface represents the object passed to the [ResizeObserver()](/en-US/docs/Web/API/ResizeObserver/ResizeObserver) constructor's callback function, which allows you to access the new dimensions of the [Element](/en-US/docs/Web/API/Element) or [SVGElement](/en-US/docs/Web/API/SVGElement) being observed.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[ResizeObserverEntry.borderBoxSize](/en-US/docs/Web/API/ResizeObserverEntry/borderBoxSize)Read only

An array of objects containing the new border box size of the observed element when the callback is run.

[ResizeObserverEntry.contentBoxSize](/en-US/docs/Web/API/ResizeObserverEntry/contentBoxSize)Read only

An array of objects containing the new content box size of the observed element when the callback is run.

[ResizeObserverEntry.devicePixelContentBoxSize](/en-US/docs/Web/API/ResizeObserverEntry/devicePixelContentBoxSize)Read only

An array of objects containing the new content box size in [device pixels](/en-US/docs/Glossary/Device_pixel) of the observed element when the callback is run.

[ResizeObserverEntry.contentRect](/en-US/docs/Web/API/ResizeObserverEntry/contentRect)Read only

A [DOMRectReadOnly](/en-US/docs/Web/API/DOMRectReadOnly) object containing the new size of the observed element when the callback is run. Note that this is now a legacy property that is retained in the spec for backward-compatibility reasons only.

[ResizeObserverEntry.target](/en-US/docs/Web/API/ResizeObserverEntry/target)Read only

A reference to the [Element](/en-US/docs/Web/API/Element) or [SVGElement](/en-US/docs/Web/API/SVGElement) being observed.

Note: The content box is the box in which content can be placed, meaning the border box minus the padding and border width. The border box encompasses the content, padding, and border. See [The box model](/en-US/docs/Learn_web_development/Core/Styling_basics/Box_model) for further explanation.

## [Instance methods](#instance_methods)

None.

## [Examples](#examples)

The following snippet is taken from the [resize-observer-text.html](https://mdn.github.io/dom-examples/resize-observer/resize-observer-text.html) ([see source](https://github.com/mdn/dom-examples/blob/main/resize-observer/resize-observer-text.html)) example.

Note that the code covers three different compatibility cases:

- Some old browsers may support `contentRect` but not `contentBoxSize`.
- Old versions of Firefox support `contentBoxSize`, but incorrectly implemented it as a single object rather than an array.
- Modern browsers support `contentBoxSize` as an array of objects, to enable them to report box sizes for fragmented elements (for example, in a multi-column scenario).

js

```
const resizeObserver = new ResizeObserver((entries) => {
  for (const entry of entries) {
    if (entry.contentBoxSize) {
      // The standard makes contentBoxSize an array...
      if (entry.contentBoxSize[0]) {
        h1Elem.style.fontSize = `${Math.max(1.5, entry.contentBoxSize[0].inlineSize / 200)}rem`;
        pElem.style.fontSize = `${Math.max(1, entry.contentBoxSize[0].inlineSize / 600)}rem`;
      } else {
        // … but old versions of Firefox treat it as a single item
        h1Elem.style.fontSize = `${Math.max(1.5, entry.contentBoxSize.inlineSize / 200)}rem`;
        pElem.style.fontSize = `${Math.max(1, entry.contentBoxSize.inlineSize / 600)}rem`;
      }
    } else {
      h1Elem.style.fontSize = `${Math.max(1.5, entry.contentRect.width / 200)}rem`;
      pElem.style.fontSize = `${Math.max(1, entry.contentRect.width / 600)}rem`;
    }
  }
  console.log("Size changed");
});

resizeObserver.observe(divElem);
```

## [Specifications](#specifications)

Specification
[Resize Observer# resize-observer-entry-interface](https://drafts.csswg.org/resize-observer/#resize-observer-entry-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ResizeObserverEntry/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/resizeobserverentry/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FResizeObserverEntry&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fresizeobserverentry%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FResizeObserverEntry%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fresizeobserverentry%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6d2000984203c51f1aad49107ebcebe14d3c1238%0A*+Document+last+modified%3A+2025-05-30T14%3A29%3A57.000Z%0A%0A%3C%2Fdetails%3E)
