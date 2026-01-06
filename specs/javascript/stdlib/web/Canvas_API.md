# Canvas API

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCanvas_API&level=high)

The Canvas API provides a means for drawing graphics via [JavaScript](/en-US/docs/Web/JavaScript) and the [HTML](/en-US/docs/Web/HTML)[<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) element. Among other things, it can be used for animation, game graphics, data visualization, photo manipulation, and real-time video processing.

The Canvas API largely focuses on 2D graphics. The [WebGL API](/en-US/docs/Web/API/WebGL_API), which also uses the `<canvas>` element, draws hardware-accelerated 2D and 3D graphics.

## In this article

- [Basic example](#basic_example)
- [Reference](#reference)
- [Guides and tutorials](#guides_and_tutorials)
- [Libraries](#libraries)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Basic example](#basic_example)

This simple example draws a green rectangle onto a canvas.

### [HTML](#html)

html

```
<canvas id="canvas"></canvas>
```

### [JavaScript](#javascript)

The [Document.getElementById()](/en-US/docs/Web/API/Document/getElementById) method gets a reference to the HTML `<canvas>` element. Next, the [HTMLCanvasElement.getContext()](/en-US/docs/Web/API/HTMLCanvasElement/getContext) method gets that element's context—the thing onto which the drawing will be rendered.

The actual drawing is done using the [CanvasRenderingContext2D](/en-US/docs/Web/API/CanvasRenderingContext2D) interface. The [fillStyle](/en-US/docs/Web/API/CanvasRenderingContext2D/fillStyle) property makes the rectangle green. The [fillRect()](/en-US/docs/Web/API/CanvasRenderingContext2D/fillRect) method places its top-left corner at (10, 10), and gives it a size of 150 units wide by 100 tall.

js

```
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

ctx.fillStyle = "green";
ctx.fillRect(10, 10, 150, 100);
```

### [Result](#result)

## [Reference](#reference)

- [HTMLCanvasElement](/en-US/docs/Web/API/HTMLCanvasElement)
- [CanvasRenderingContext2D](/en-US/docs/Web/API/CanvasRenderingContext2D)
- [CanvasGradient](/en-US/docs/Web/API/CanvasGradient)
- [CanvasPattern](/en-US/docs/Web/API/CanvasPattern)
- [ImageBitmap](/en-US/docs/Web/API/ImageBitmap)
- [ImageData](/en-US/docs/Web/API/ImageData)
- [TextMetrics](/en-US/docs/Web/API/TextMetrics)
- [OffscreenCanvas](/en-US/docs/Web/API/OffscreenCanvas)
- [Path2D](/en-US/docs/Web/API/Path2D)Experimental
- [ImageBitmapRenderingContext](/en-US/docs/Web/API/ImageBitmapRenderingContext)Experimental

Note: The interfaces related to the `WebGLRenderingContext` are referenced under [WebGL](/en-US/docs/Web/API/WebGL_API).

Note:[OffscreenCanvas](/en-US/docs/Web/API/OffscreenCanvas) is also available in web workers.

[CanvasCaptureMediaStreamTrack](/en-US/docs/Web/API/CanvasCaptureMediaStreamTrack) is a related interface.

## [Guides and tutorials](#guides_and_tutorials)

[Canvas tutorial](/en-US/docs/Web/API/Canvas_API/Tutorial)

A comprehensive tutorial covering both the basic usage of the Canvas API and its advanced features.

[HTML5 Canvas Deep Dive](https://joshondesign.com/p/books/canvasdeepdive/title.html)

A hands-on, book-length introduction to the Canvas API and WebGL.

[Canvas Handbook](https://bucephalus.org/text/CanvasHandbook/CanvasHandbook.html)

A handy reference for the Canvas API.

[Manipulating video using canvas](/en-US/docs/Web/API/Canvas_API/Manipulating_video_using_canvas)

Combining [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) and [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) to manipulate video data in real time.

## [Libraries](#libraries)

The Canvas API is extremely powerful, but not always simple to use. The libraries listed below can make the creation of canvas-based projects faster and easier.

- [EaselJS](https://createjs.com/easeljs) is an open-source canvas library that makes creating games, generative art, and other highly graphical experiences easy.
- [Fabric.js](https://fabricjs.com/) is an open-source canvas library with SVG parsing capabilities.
- [heatmap.js](https://www.patrick-wied.at/static/heatmapjs/) is an open-source library for creating canvas-based data heat maps.
- [JavaScript InfoVis Toolkit](https://philogb.github.io/jit/) creates interactive data visualizations.
- [Konva.js](https://konvajs.org/) is a 2D canvas library for desktop and mobile applications.
- [p5.js](https://p5js.org/) has a full set of canvas drawing functionality for artists, designers, educators, and beginners.
- [Phaser](https://phaser.io/) is a fast, free and fun open source framework for Canvas and WebGL powered browser games.
- [Pts.js](https://ptsjs.org/) is a library for creative coding and visualization in canvas and SVG.
- [Rekapi](https://github.com/jeremyckahn/rekapi) is an animation key-framing API for Canvas.
- [Scrawl-canvas](https://scrawl.rikweb.org.uk/) is an open-source JavaScript library for creating and manipulating 2D canvas elements.
- The [ZIM](https://zimjs.com/) framework provides conveniences, components, and controls for coding creativity on the canvas — includes accessibility and hundreds of colorful tutorials.
- [Sprig](https://github.com/hackclub/sprig) is a beginner-friendly, open-source, tile-based game development library that uses Canvas.

Note: See the [WebGL API](/en-US/docs/Web/API/WebGL_API) for 2D and 3D libraries that use WebGL.

## [Specifications](#specifications)

Specification
[HTML# the-canvas-element](https://html.spec.whatwg.org/multipage/canvas.html#the-canvas-element)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebGL](/en-US/docs/Web/API/WebGL_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 17, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Canvas_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/canvas_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCanvas_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcanvas_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCanvas_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcanvas_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F03d5115691a7a9fa3df3b6ebd20a0c7eed213252%0A*+Document+last+modified%3A+2025-07-17T10%3A30%3A33.000Z%0A%0A%3C%2Fdetails%3E)
