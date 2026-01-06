# Ink API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInk_API&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The Ink API allows browsers to directly make use of available OS-level compositors when drawing pen strokes in an inking app feature, thereby reducing latency and increasing performance.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Concepts and usage](#concepts_and_usage)

Inking on the web refers to app features that involve using [pointer events](/en-US/docs/Web/API/Pointer_events) to draw a smooth pen stroke — for example, a drawing app or document signing feature.

Pointers events are usually sent first to the browser process, which then forwards these events to the JavaScript event loop to execute the associated handler functions and render the result in the app. The time delay between the start and finish of this process can be significant, resulting in latency between the user initiating drawing (for example, with a stylus or mouse), and the stroke showing up on the screen.

The Ink API significantly reduces this latency by allowing browsers to bypass the JavaScript event loop entirely. Where possible, browsers will pass such rendering instructions directly to OS-level compositors. If the underlying operating system does not have a specialized OS-level compositor to use for this purpose, browsers will use their own optimized rendering code. This is not as powerful as a compositor, but it still confers some improvements.

Note: Compositors are part of the rendering machinery that draws the UI to the screen in a browser or operating system. See [Inside look at modern web browser (part 3)](https://developer.chrome.com/blog/inside-browser-part3/) for some interesting insights into how a compositor functions inside a web browser.

The entry point is the [Navigator.ink](/en-US/docs/Web/API/Navigator/ink) property, which returns an [Ink](/en-US/docs/Web/API/Ink) object for the current document. The [Ink.requestPresenter()](/en-US/docs/Web/API/Ink/requestPresenter) method returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with a [DelegatedInkTrailPresenter](/en-US/docs/Web/API/DelegatedInkTrailPresenter) object instance. This instructs the OS-level compositor to render ink strokes between pointer event dispatches in the next available frame in each case.

## [Interfaces](#interfaces)

[Ink](/en-US/docs/Web/API/Ink)Experimental

Provides access to [DelegatedInkTrailPresenter](/en-US/docs/Web/API/DelegatedInkTrailPresenter) objects for the application to use to render the strokes.

[DelegatedInkTrailPresenter](/en-US/docs/Web/API/DelegatedInkTrailPresenter)Experimental

Instructs the OS-level compositor to render ink strokes between pointer event dispatches.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[Navigator.ink](/en-US/docs/Web/API/Navigator/ink)Read onlyExperimental

Returns an [Ink](/en-US/docs/Web/API/Ink) object for the current document.

## [Examples](#examples)

### [Drawing an ink trail](#drawing_an_ink_trail)

In this example, we draw a trail onto a 2D canvas. Near the start of the code, we call [Ink.requestPresenter()](/en-US/docs/Web/API/Ink/requestPresenter), passing it the canvas as the presentation area for it to take care of and storing the promise it returns in the `presenter` variable.

Later on, in the `pointermove` event listener, the new position of the trailhead is drawn onto the canvas each time the event fires. In addition, the [DelegatedInkTrailPresenter](/en-US/docs/Web/API/DelegatedInkTrailPresenter) object returned when the `presenter` promise fulfills has its [updateInkTrailStartPoint()](/en-US/docs/Web/API/DelegatedInkTrailPresenter/updateInkTrailStartPoint) method invoked; this is passed:

- The last trusted pointer event representing the rendering point for the current frame.
- A `style` object containing color and diameter settings.

The result is that a delegated ink trail is drawn ahead of the default browser rendering on the app's behalf, in the specified style, until the next time it receives a `pointermove` event.

#### HTML

html

```
<canvas id="canvas"></canvas>
<div id="div">Delegated ink trail should match the color of this div.</div>
```

#### CSS

css

```
div {
  background-color: lime;
  position: fixed;
  top: 1rem;
  left: 1rem;
}
```

#### JavaScript

js

```
const ctx = canvas.getContext("2d");
const presenter = navigator.ink.requestPresenter({ presentationArea: canvas });
let moveCnt = 0;
let style = { color: "lime", diameter: 10 };

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

canvas.addEventListener("pointermove", async (evt) => {
  const pointSize = 10;
  ctx.fillStyle = style.color;
  ctx.fillRect(evt.pageX, evt.pageY, pointSize, pointSize);
  if (moveCnt === 20) {
    const r = getRandomInt(0, 255);
    const g = getRandomInt(0, 255);
    const b = getRandomInt(0, 255);

    style = { color: `rgb(${r} ${g} ${b} / 100%)`, diameter: 10 };
    moveCnt = 0;
    document.getElementById("div").style.backgroundColor =
      `rgb(${r} ${g} ${b} / 60%)`;
  }
  moveCnt += 1;
  (await presenter).updateInkTrailStartPoint(evt, style);
});

window.addEventListener("pointerdown", () => {
  ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
});

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
```

#### Result

## [Specifications](#specifications)

Specification
[Ink API# ink-interface](https://wicg.github.io/ink-enhancement/#ink-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Ink_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/ink_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInk_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fink_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInk_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fink_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff336c5b6795a562c64fe859aa9ee2becf223ad8a%0A*+Document+last+modified%3A+2025-11-03T18%3A29%3A25.000Z%0A%0A%3C%2Fdetails%3E)
