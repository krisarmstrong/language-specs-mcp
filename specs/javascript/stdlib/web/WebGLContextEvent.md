# WebGLContextEvent

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2016⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLContextEvent&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The WebGLContextEvent interface is part of the [WebGL API](/en-US/docs/Web/API/WebGL_API) and is an interface for an event that is generated in response to a status change to the WebGL rendering context.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[WebGLContextEvent()](/en-US/docs/Web/API/WebGLContextEvent/WebGLContextEvent)

Creates a new `WebGLContextEvent` object.

## [Instance properties](#instance_properties)

This interface inherits properties from its parent interface, [Event](/en-US/docs/Web/API/Event).

[WebGLContextEvent.statusMessage](/en-US/docs/Web/API/WebGLContextEvent/statusMessage)

A read-only property containing additional information about the event.

## [Instance methods](#instance_methods)

This interface doesn't define any own methods, but inherits methods from its parent interface, [Event](/en-US/docs/Web/API/Event).

## [Examples](#examples)

With the help of the [WEBGL_lose_context](/en-US/docs/Web/API/WEBGL_lose_context) extension, you can simulate the [webglcontextlost](/en-US/docs/Web/API/HTMLCanvasElement/webglcontextlost_event) and [webglcontextrestored](/en-US/docs/Web/API/HTMLCanvasElement/webglcontextrestored_event) events:

js

```
const canvas = document.getElementById("canvas");
const gl = canvas.getContext("webgl");

canvas.addEventListener("webglcontextlost", (e) => {
  console.log(e);
});

gl.getExtension("WEBGL_lose_context").loseContext();

// WebGLContextEvent event with type "webglcontextlost" is logged.
```

## [Specifications](#specifications)

Specification
[WebGL Specification# 5.15](https://registry.khronos.org/webgl/specs/latest/1.0/#5.15)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebGLRenderingContext.isContextLost()](/en-US/docs/Web/API/WebGLRenderingContext/isContextLost)
- [WEBGL_lose_context](/en-US/docs/Web/API/WEBGL_lose_context), [WEBGL_lose_context.loseContext()](/en-US/docs/Web/API/WEBGL_lose_context/loseContext), [WEBGL_lose_context.restoreContext()](/en-US/docs/Web/API/WEBGL_lose_context/restoreContext)
- Events: [webglcontextlost](/en-US/docs/Web/API/HTMLCanvasElement/webglcontextlost_event), [webglcontextrestored](/en-US/docs/Web/API/HTMLCanvasElement/webglcontextrestored_event), [webglcontextcreationerror](/en-US/docs/Web/API/HTMLCanvasElement/webglcontextcreationerror_event)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 19, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/WebGLContextEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/webglcontextevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLContextEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwebglcontextevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLContextEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwebglcontextevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff71683f74da0078d9371c4d0c1ff9d3898fc7b59%0A*+Document+last+modified%3A+2025-09-19T15%3A38%3A24.000Z%0A%0A%3C%2Fdetails%3E)
