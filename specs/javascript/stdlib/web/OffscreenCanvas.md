# OffscreenCanvas

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2023⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FOffscreenCanvas&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

When using the [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) element or the [Canvas API](/en-US/docs/Web/API/Canvas_API), rendering, animation, and user interaction usually happen on the main execution thread of a web application. The computation relating to canvas animations and rendering can have a significant impact on application performance.

The `OffscreenCanvas` interface provides a canvas that can be rendered off screen, decoupling the DOM and the Canvas API so that the [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) element is no longer entirely dependent on the DOM. Rendering operations can also be run inside a [worker](/en-US/docs/Web/API/Web_Workers_API) context, allowing you to run some tasks in a separate thread and avoid heavy work on the main thread.

`OffscreenCanvas` is a [transferable object](/en-US/docs/Web/API/Web_Workers_API/Transferable_objects).

## In this article

- [Constructors](#constructors)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructors](#constructors)

[OffscreenCanvas()](/en-US/docs/Web/API/OffscreenCanvas/OffscreenCanvas)

`OffscreenCanvas` constructor. Creates a new `OffscreenCanvas` object.

## [Instance properties](#instance_properties)

[OffscreenCanvas.height](/en-US/docs/Web/API/OffscreenCanvas/height)

The height of the offscreen canvas.

[OffscreenCanvas.width](/en-US/docs/Web/API/OffscreenCanvas/width)

The width of the offscreen canvas.

## [Instance methods](#instance_methods)

[OffscreenCanvas.getContext()](/en-US/docs/Web/API/OffscreenCanvas/getContext)

Returns a drawing context for the offscreen canvas, or [null](/en-US/docs/Web/JavaScript/Reference/Operators/null) if the context identifier is not supported, or the offscreen canvas has already been set to a different context mode.

[OffscreenCanvas.convertToBlob()](/en-US/docs/Web/API/OffscreenCanvas/convertToBlob)

Creates a [Blob](/en-US/docs/Web/API/Blob) object representing the image contained in the canvas.

[OffscreenCanvas.transferToImageBitmap()](/en-US/docs/Web/API/OffscreenCanvas/transferToImageBitmap)

Creates an [ImageBitmap](/en-US/docs/Web/API/ImageBitmap) object from the most recently rendered image of the `OffscreenCanvas`. See its reference for important notes on managing this [ImageBitmap](/en-US/docs/Web/API/ImageBitmap).

## [Events](#events)

Inherits events from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface.

[contextlost](/en-US/docs/Web/API/OffscreenCanvas/contextlost_event)

Fired if the browser detects that an [OffscreenCanvasRenderingContext2D](/en-US/docs/Web/API/OffscreenCanvasRenderingContext2D) context is lost.

[contextrestored](/en-US/docs/Web/API/OffscreenCanvas/contextrestored_event)

Fired if the browser successfully restores an [OffscreenCanvasRenderingContext2D](/en-US/docs/Web/API/OffscreenCanvasRenderingContext2D) context.

## [Examples](#examples)

### [Synchronous display of frames produced by an OffscreenCanvas](#synchronous_display_of_frames_produced_by_an_offscreencanvas)

One way to use the `OffscreenCanvas` API is to use a rendering context that has been obtained from an `OffscreenCanvas` object to generate new frames. Once a new frame has finished rendering in this context, the [transferToImageBitmap()](/en-US/docs/Web/API/OffscreenCanvas/transferToImageBitmap) method can be called to save the most recent rendered image. This method returns an [ImageBitmap](/en-US/docs/Web/API/ImageBitmap) object, which can be used in a variety of Web APIs and also in a second canvas without creating a transfer copy.

To display the `ImageBitmap`, you can use an [ImageBitmapRenderingContext](/en-US/docs/Web/API/ImageBitmapRenderingContext) context, which can be created by calling `canvas.getContext("bitmaprenderer")` on a (visible) canvas element. This context only provides functionality to replace the canvas's contents with the given `ImageBitmap`. A call to [ImageBitmapRenderingContext.transferFromImageBitmap()](/en-US/docs/Web/API/ImageBitmapRenderingContext/transferFromImageBitmap) with the previously rendered and saved `ImageBitmap` from the OffscreenCanvas, will display the `ImageBitmap` on the canvas and transfer its ownership to the canvas. A single `OffscreenCanvas` may transfer frames into an arbitrary number of other `ImageBitmapRenderingContext` objects.

Given these two [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) elements

html

```
<canvas id="one"></canvas> <canvas id="two"></canvas>
```

the following code will provide the rendering using `OffscreenCanvas` as described above.

js

```
const one = document.getElementById("one").getContext("bitmaprenderer");
const two = document.getElementById("two").getContext("bitmaprenderer");

const offscreen = new OffscreenCanvas(256, 256);
const gl = offscreen.getContext("webgl");

// Perform some drawing for the first canvas using the gl context
const bitmapOne = offscreen.transferToImageBitmap();
one.transferFromImageBitmap(bitmapOne);

// Perform some more drawing for the second canvas
const bitmapTwo = offscreen.transferToImageBitmap();
two.transferFromImageBitmap(bitmapTwo);
```

### [Asynchronous display of frames produced by an OffscreenCanvas](#asynchronous_display_of_frames_produced_by_an_offscreencanvas)

Another way to use the `OffscreenCanvas` API, is to call [transferControlToOffscreen()](/en-US/docs/Web/API/HTMLCanvasElement/transferControlToOffscreen) on a [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) element, either on a [worker](/en-US/docs/Web/API/Web_Workers_API) or the main thread, which will return an `OffscreenCanvas` object from an [HTMLCanvasElement](/en-US/docs/Web/API/HTMLCanvasElement) object from the main thread. Calling [getContext()](/en-US/docs/Web/API/OffscreenCanvas/getContext) will then obtain a rendering context from that `OffscreenCanvas`.

The `main.js` script (main thread) may look like this:

js

```
const htmlCanvas = document.getElementById("canvas");
const offscreen = htmlCanvas.transferControlToOffscreen();

const worker = new Worker("offscreen-canvas.js");
worker.postMessage({ canvas: offscreen }, [offscreen]);
```

While the `offscreen-canvas.js` script (worker thread) can look like this:

js

```
onmessage = (evt) => {
  const canvas = evt.data.canvas;
  const gl = canvas.getContext("webgl");
  // Perform some drawing using the gl context
};
```

It's also possible to use [requestAnimationFrame()](/en-US/docs/Web/API/Window/requestAnimationFrame) in workers:

js

```
onmessage = (evt) => {
  const canvas = evt.data.canvas;
  const gl = canvas.getContext("webgl");

  function render(time) {
    // Perform some drawing using the gl context
    requestAnimationFrame(render);
  }
  requestAnimationFrame(render);
};
```

For a full example, see the [OffscreenCanvas example source](https://github.com/mdn/dom-examples/tree/main/web-workers/offscreen-canvas-worker) on GitHub or run the [OffscreenCanvas example live](https://mdn.github.io/dom-examples/web-workers/offscreen-canvas-worker/).

## [Specifications](#specifications)

Specification
[HTML# the-offscreencanvas-interface](https://html.spec.whatwg.org/multipage/canvas.html#the-offscreencanvas-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [CanvasRenderingContext2D](/en-US/docs/Web/API/CanvasRenderingContext2D)
- [OffscreenCanvasRenderingContext2D](/en-US/docs/Web/API/OffscreenCanvasRenderingContext2D)
- [ImageBitmap](/en-US/docs/Web/API/ImageBitmap)
- [ImageBitmapRenderingContext](/en-US/docs/Web/API/ImageBitmapRenderingContext)
- [HTMLCanvasElement.transferControlToOffscreen()](/en-US/docs/Web/API/HTMLCanvasElement/transferControlToOffscreen)
- [requestAnimationFrame()](/en-US/docs/Web/API/Window/requestAnimationFrame)
- [WebGL Off the Main Thread – Mozilla Hacks](https://hacks.mozilla.org/2016/01/webgl-off-the-main-thread/) (2016)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/OffscreenCanvas/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/offscreencanvas/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FOffscreenCanvas&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Foffscreencanvas%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FOffscreenCanvas%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Foffscreencanvas%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F32f1bfc28a0704c9a743bc971df1b2563cc4ccc6%0A*+Document+last+modified%3A+2024-10-26T17%3A41%3A41.000Z%0A%0A%3C%2Fdetails%3E)
