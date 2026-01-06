# WebGLSync

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2021⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLSync&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `WebGLSync` interface is part of the [WebGL 2](/en-US/docs/Web/API/WebGL_API) API and is used to synchronize activities between the GPU and the application.

When working with `WebGLSync` objects, the following methods of the [WebGL2RenderingContext](/en-US/docs/Web/API/WebGL2RenderingContext) are useful:

- [WebGL2RenderingContext.fenceSync()](/en-US/docs/Web/API/WebGL2RenderingContext/fenceSync)
- [WebGL2RenderingContext.deleteSync()](/en-US/docs/Web/API/WebGL2RenderingContext/deleteSync)
- [WebGL2RenderingContext.isSync()](/en-US/docs/Web/API/WebGL2RenderingContext/isSync)
- [WebGL2RenderingContext.clientWaitSync()](/en-US/docs/Web/API/WebGL2RenderingContext/clientWaitSync)
- [WebGL2RenderingContext.waitSync()](/en-US/docs/Web/API/WebGL2RenderingContext/waitSync)
- [WebGL2RenderingContext.getSyncParameter()](/en-US/docs/Web/API/WebGL2RenderingContext/getSyncParameter)

## In this article

- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Examples](#examples)

### [Creating a WebGLSync object](#creating_a_webglsync_object)

in this example, `gl` must be a [WebGL2RenderingContext](/en-US/docs/Web/API/WebGL2RenderingContext). `WebGLSync` objects are not available in WebGL 1.

js

```
const sync = gl.fenceSync(gl.SYNC_GPU_COMMANDS_COMPLETE, 0);
```

## [Specifications](#specifications)

Specification
[WebGL 2.0 Specification# 3.4](https://registry.khronos.org/webgl/specs/latest/2.0/#3.4)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebGLRenderingContext.finish()](/en-US/docs/Web/API/WebGLRenderingContext/finish)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 28, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/WebGLSync/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/webglsync/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLSync&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwebglsync%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLSync%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwebglsync%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2b942f0d8f84641c233d701cb5d1f4e6c23120ff%0A*+Document+last+modified%3A+2024-09-28T05%3A28%3A22.000Z%0A%0A%3C%2Fdetails%3E)
