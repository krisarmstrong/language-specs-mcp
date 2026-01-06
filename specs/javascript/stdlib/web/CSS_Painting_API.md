# CSS Painting API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSS_Painting_API&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The CSS Painting API — part of the [CSS Houdini](/en-US/docs/Web/API/Houdini_APIs) umbrella of APIs — allows developers to write JavaScript functions that can draw directly into an element's background, border, or content.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

Essentially, the CSS Painting API contains functionality allowing developers to create custom values for [paint()](/en-US/docs/Web/CSS/Reference/Values/image/paint), a CSS [<image>](/en-US/docs/Web/CSS/Reference/Values/image) function. You can then apply these values to properties like [background-image](/en-US/docs/Web/CSS/Reference/Properties/background-image) to set complex custom backgrounds on an element.

For example:

css

```
aside {
  background-image: paint(my-painted-image);
}
```

The API defines a [worklet](/en-US/docs/Web/API/Worklet) that can be used to programmatically generate an image that responds to computed style changes. To find out more about how this is used, consult [Using the CSS Painting API](/en-US/docs/Web/API/CSS_Painting_API/Guide).

## [Interfaces](#interfaces)

[PaintWorkletGlobalScope](/en-US/docs/Web/API/PaintWorkletGlobalScope)

The global execution context of the paint worklet.

[PaintRenderingContext2D](/en-US/docs/Web/API/PaintRenderingContext2D)

The rendering context for the CSS Painting API's rendering context for drawing to the bitmap.

[PaintSize](/en-US/docs/Web/API/PaintSize)

Represents the size of the output bitmap that the author should draw.

## [Examples](#examples)

The following example creates a list of items with a background image that rotates between three different colors and three widths. In [a supporting browser](#browser_compatibility) you will see something like the image below.

To achieve this we'll define two custom CSS properties, `--box-color` and `--width-subtractor`.

### [The paint worklet](#the_paint_worklet)

The worklet is an external JavaScript file (in this case we've called it `boxbg.js`) which defines a paint [worklet](/en-US/docs/Web/API/Worklet). Using the worklet, we can access CSS properties (and custom properties) of elements:

js

```
registerPaint(
  "boxbg",
  class {
    static get contextOptions() {
      return { alpha: true };
    }
    /*
      Retrieve any custom properties (or regular properties,
      such as 'height') defined for the element, and return
      them as an array.
    */
    static get inputProperties() {
      return ["--box-color", "--width-subtractor"];
    }

    paint(ctx, size, props) {
      /*
        ctx -> drawing context
        size -> paintSize: width and height
        props -> properties: get() method
      */
      ctx.fillStyle = props.get("--box-color");
      ctx.fillRect(
        0,
        size.height / 3,
        size.width * 0.4 - props.get("--width-subtractor"),
        size.height * 0.6,
      );
    }
  },
);
```

We used the `inputProperties()` method in the `registerPaint()` class to get the values of two custom properties set on an element that has `boxbg` applied to it and then used those within our `paint()` function. The `inputProperties()` method can return all properties affecting the element, not just custom properties.

### [Using the paint worklet](#using_the_paint_worklet)

#### HTML

html

```
<ul>
  <li>item 1</li>
  <li>item 2</li>
  <li>item 3</li>
  <li>item 4</li>
  <li>item 5</li>
  <li>item 6</li>
  <li>item 7</li>
  <li>item 8</li>
  <li>item 9</li>
  <li>item 10</li>
  <li>item N</li>
</ul>
```

#### CSS

In our CSS, we define the `--box-color` and `--width-subtractor` custom properties.

css

```
body {
  font: 1.2em / 1.2 sans-serif;
}
li {
  background-image: paint(boxbg);
  --box-color: hsl(55 90% 60%);
}

li:nth-of-type(3n) {
  --box-color: hsl(155 90% 60%);
  --width-subtractor: 20;
}

li:nth-of-type(3n + 1) {
  --box-color: hsl(255 90% 60%);
  --width-subtractor: 40;
}
```

#### JavaScript

The setup and logic of the paint worklet is in the external script. To register the worklet, we need to call [addModule()](/en-US/docs/Web/API/Worklet/addModule) from our main script:

js

```
CSS.paintWorklet.addModule(
  "https://mdn.github.io/houdini-examples/cssPaint/intro/worklets/boxbg.js",
);
```

In this example, the worklet is hosted at `https://mdn.github.io/`, but your worklet may be a relative resource like so:

js

```
CSS.paintWorklet.addModule("boxbg.js");
```

#### Result

While you can't play with the worklet's script, you can alter the custom property values in DevTools to change the colors and width of the background image.

## [Specifications](#specifications)

Specification
[CSS Painting API Level 1# paintworkletglobalscope](https://drafts.css-houdini.org/css-paint-api/#paintworkletglobalscope)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the CSS Painting API](/en-US/docs/Web/API/CSS_Painting_API/Guide)
- [CSS Typed Object Model API](/en-US/docs/Web/API/CSS_Typed_OM_API)
- [Houdini APIs](/en-US/docs/Web/API/Houdini_APIs)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 5, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSS_Painting_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/css_painting_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSS_Painting_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcss_painting_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSS_Painting_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcss_painting_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F635820782735cd00f71ce3929ff9377b091f8995%0A*+Document+last+modified%3A+2025-08-05T14%3A01%3A02.000Z%0A%0A%3C%2Fdetails%3E)
