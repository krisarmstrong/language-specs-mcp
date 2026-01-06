# WebGLQuery

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2021⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLQuery&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `WebGLQuery` interface is part of the [WebGL 2](/en-US/docs/Web/API/WebGL_API) API and provides ways to asynchronously query for information. By default, occlusion queries and primitive queries are available.

Another kind of queries are disjoint timer queries, which allow you to measure performance and profiling of your GPU. Disjoint timer queries are available with the [EXT_disjoint_timer_query](/en-US/docs/Web/API/EXT_disjoint_timer_query) extension only.

When working with `WebGLQuery` objects, the following methods of the [WebGL2RenderingContext](/en-US/docs/Web/API/WebGL2RenderingContext) are useful:

- [WebGL2RenderingContext.createQuery()](/en-US/docs/Web/API/WebGL2RenderingContext/createQuery)
- [WebGL2RenderingContext.deleteQuery()](/en-US/docs/Web/API/WebGL2RenderingContext/deleteQuery)
- [WebGL2RenderingContext.isQuery()](/en-US/docs/Web/API/WebGL2RenderingContext/isQuery)
- [WebGL2RenderingContext.beginQuery()](/en-US/docs/Web/API/WebGL2RenderingContext/beginQuery)
- [WebGL2RenderingContext.endQuery()](/en-US/docs/Web/API/WebGL2RenderingContext/endQuery)
- [WebGL2RenderingContext.getQuery()](/en-US/docs/Web/API/WebGL2RenderingContext/getQuery)
- [WebGL2RenderingContext.getQueryParameter()](/en-US/docs/Web/API/WebGL2RenderingContext/getQueryParameter)

## In this article

- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Examples](#examples)

### [Creating a WebGLQuery object](#creating_a_webglquery_object)

in this example, `gl` must be a [WebGL2RenderingContext](/en-US/docs/Web/API/WebGL2RenderingContext). `WebGLQuery` objects are not available in WebGL 1.

js

```
const query = gl.createQuery();
```

## [Specifications](#specifications)

Specification
[WebGL 2.0 Specification# 3.2](https://registry.khronos.org/webgl/specs/latest/2.0/#3.2)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [EXT_disjoint_timer_query](/en-US/docs/Web/API/EXT_disjoint_timer_query)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 28, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/WebGLQuery/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/webglquery/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLQuery&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwebglquery%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLQuery%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwebglquery%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2b942f0d8f84641c233d701cb5d1f4e6c23120ff%0A*+Document+last+modified%3A+2024-09-28T05%3A28%3A22.000Z%0A%0A%3C%2Fdetails%3E)
