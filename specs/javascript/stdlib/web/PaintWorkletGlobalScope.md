# PaintWorkletGlobalScope

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPaintWorkletGlobalScope&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `PaintWorkletGlobalScope` interface of the [CSS Painting API](/en-US/docs/Web/API/CSS_Painting_API) represents the global object available inside a paint [Worklet](/en-US/docs/Web/API/Worklet).

## In this article

- [Privacy concerns](#privacy_concerns)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Privacy concerns](#privacy_concerns)

To avoid leaking visited links, this feature is currently disabled in Chrome-based browsers for [<a>](/en-US/docs/Web/HTML/Reference/Elements/a) elements with an `href` attribute, and for children of such elements. For details, see the following:

- The CSS Painting API [Privacy Considerations section](https://drafts.css-houdini.org/css-paint-api/#privacy-considerations)
- The CSS Painting API spec issue ["CSS Paint API leaks browsing history"](https://github.com/w3c/css-houdini-drafts/issues/791)

## [Instance properties](#instance_properties)

This interface inherits properties from [WorkletGlobalScope](/en-US/docs/Web/API/WorkletGlobalScope).

[PaintWorkletGlobalScope.devicePixelRatio](/en-US/docs/Web/API/PaintWorkletGlobalScope/devicePixelRatio)Read onlyExperimental

Returns the current device's ratio of physical pixels to logical pixels.

## [Instance methods](#instance_methods)

This interface inherits methods from [WorkletGlobalScope](/en-US/docs/Web/API/WorkletGlobalScope).

[PaintWorkletGlobalScope.registerPaint()](/en-US/docs/Web/API/PaintWorkletGlobalScope/registerPaint)Experimental

Registers a class to programmatically generate an image where a CSS property expects a file.

## [Examples](#examples)

The following three examples go together to show creating, loading, and using a paint `Worklet`.

### [Create a paint worklet](#create_a_paint_worklet)

The following shows an example worklet module. This should be in a separate js file. Note that `registerPaint()` is called without a reference to a paint `Worklet`.

js

```
class CheckerboardPainter {
  paint(ctx, geom, properties) {
    // The global object here is a PaintWorkletGlobalScope
    // Methods and properties can be accessed directly
    // as global features or prefixed using self
    const dpr = self.devicePixelRatio;

    // Use `ctx` as if it was a normal canvas
    const colors = ["red", "green", "blue"];
    const size = 32;
    for (let y = 0; y < geom.height / size; y++) {
      for (let x = 0; x < geom.width / size; x++) {
        const color = colors[(x + y) % colors.length];
        ctx.beginPath();
        ctx.fillStyle = color;
        ctx.rect(x * size, y * size, size, size);
        ctx.fill();
      }
    }
  }
}

// Register our class under a specific name
registerPaint("checkerboard", CheckerboardPainter);
```

### [Load a paint worklet](#load_a_paint_worklet)

The following example demonstrates loading the above worklet from its js file and does so by feature detection.

js

```
if ("paintWorklet" in CSS) {
  CSS.paintWorklet.addModule("checkerboard.js");
}
```

### [Use a paint worklet](#use_a_paint_worklet)

This example shows how to use a paint `Worklet` in a stylesheet, including the simplest way to provide a fallback if `CSS.paintWorklet` isn't supported.

css

```
textarea {
  background-image: url("checkerboard.png"); /* Fallback */
  background-image: paint(checkerboard);
}
```

You can also use the [@supports](/en-US/docs/Web/CSS/Reference/At-rules/@supports) at-rule.

css

```
@supports (background: paint(id)) {
  textarea {
    background-image: paint(checkerboard);
  }
}
```

## [Specifications](#specifications)

Specification
[CSS Painting API Level 1# paintworkletglobalscope](https://drafts.css-houdini.org/css-paint-api/#paintworkletglobalscope)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the CSS Painting API](/en-US/docs/Web/API/CSS_Painting_API/Guide)
- [CSS Painting API](/en-US/docs/Web/API/CSS_Painting_API)
- [Houdini APIs](/en-US/docs/Web/API/Houdini_APIs)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 5, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/PaintWorkletGlobalScope/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/paintworkletglobalscope/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPaintWorkletGlobalScope&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpaintworkletglobalscope%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPaintWorkletGlobalScope%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpaintworkletglobalscope%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9944f7b12ef1a6aecd54d4b2f0c188a82fdeaaf0%0A*+Document+last+modified%3A+2025-08-05T13%3A32%3A56.000Z%0A%0A%3C%2Fdetails%3E)
