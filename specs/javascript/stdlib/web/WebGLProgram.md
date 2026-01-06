# WebGLProgram

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLProgram&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `WebGLProgram` is part of the [WebGL API](/en-US/docs/Web/API/WebGL_API) and is a combination of two compiled [WebGLShader](/en-US/docs/Web/API/WebGLShader)s consisting of a vertex shader and a fragment shader (both written in GLSL).

To create a `WebGLProgram`, call the GL context's [createProgram()](/en-US/docs/Web/API/WebGLRenderingContext/createProgram) function. After attaching the shader programs using [attachShader()](/en-US/docs/Web/API/WebGLRenderingContext/attachShader), you link them into a usable program. This is shown in the code below.

js

```
const program = gl.createProgram();

// Attach pre-existing shaders
gl.attachShader(program, vertexShader);
gl.attachShader(program, fragmentShader);

gl.linkProgram(program);

if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
  const info = gl.getProgramInfoLog(program);
  throw new Error(`Could not compile WebGL program. \n\n${info}`);
}
```

See [WebGLShader](/en-US/docs/Web/API/WebGLShader) for information on creating the `vertexShader` and `fragmentShader` in the above example.

## In this article

- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Examples](#examples)

### [Using the program](#using_the_program)

The steps to actually do some work with the program involve telling the GPU to use the program, bind the appropriate data and configuration options, and finally draw something to the screen.

js

```
// Use the program
gl.useProgram(program);

// Bind existing attribute data
gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
gl.enableVertexAttribArray(attributeLocation);
gl.vertexAttribPointer(attributeLocation, 3, gl.FLOAT, false, 0, 0);

// Draw a single triangle
gl.drawArrays(gl.TRIANGLES, 0, 3);
```

### [Deleting the program](#deleting_the_program)

If there is an error linking the program or you wish to delete an existing program, then it is as simple as running [WebGLRenderingContext.deleteProgram()](/en-US/docs/Web/API/WebGLRenderingContext/deleteProgram). This frees the memory of the linked program.

js

```
gl.deleteProgram(program);
```

## [Specifications](#specifications)

Specification
[WebGL Specification# 5.6](https://registry.khronos.org/webgl/specs/latest/1.0/#5.6)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebGLShader](/en-US/docs/Web/API/WebGLShader)
- [WebGLRenderingContext.attachShader()](/en-US/docs/Web/API/WebGLRenderingContext/attachShader)
- [WebGLRenderingContext.compileShader()](/en-US/docs/Web/API/WebGLRenderingContext/compileShader)
- [WebGLRenderingContext.createProgram()](/en-US/docs/Web/API/WebGLRenderingContext/createProgram)
- [WebGLRenderingContext.createShader()](/en-US/docs/Web/API/WebGLRenderingContext/createShader)
- [WebGLRenderingContext.deleteProgram()](/en-US/docs/Web/API/WebGLRenderingContext/deleteProgram)
- [WebGLRenderingContext.deleteShader()](/en-US/docs/Web/API/WebGLRenderingContext/deleteShader)
- [WebGLRenderingContext.detachShader()](/en-US/docs/Web/API/WebGLRenderingContext/detachShader)
- [WebGLRenderingContext.getAttachedShaders()](/en-US/docs/Web/API/WebGLRenderingContext/getAttachedShaders)
- [WebGLRenderingContext.getProgramParameter()](/en-US/docs/Web/API/WebGLRenderingContext/getProgramParameter)
- [WebGLRenderingContext.getProgramInfoLog()](/en-US/docs/Web/API/WebGLRenderingContext/getProgramInfoLog)
- [WebGLRenderingContext.getShaderParameter()](/en-US/docs/Web/API/WebGLRenderingContext/getShaderParameter)
- [WebGLRenderingContext.getShaderPrecisionFormat()](/en-US/docs/Web/API/WebGLRenderingContext/getShaderPrecisionFormat)
- [WebGLRenderingContext.getShaderInfoLog()](/en-US/docs/Web/API/WebGLRenderingContext/getShaderInfoLog)
- [WebGLRenderingContext.getShaderSource()](/en-US/docs/Web/API/WebGLRenderingContext/getShaderSource)
- [WebGLRenderingContext.isProgram()](/en-US/docs/Web/API/WebGLRenderingContext/isProgram)
- [WebGLRenderingContext.isShader()](/en-US/docs/Web/API/WebGLRenderingContext/isShader)
- [WebGLRenderingContext.linkProgram()](/en-US/docs/Web/API/WebGLRenderingContext/linkProgram)
- [WebGLRenderingContext.shaderSource()](/en-US/docs/Web/API/WebGLRenderingContext/shaderSource)
- [WebGLRenderingContext.useProgram()](/en-US/docs/Web/API/WebGLRenderingContext/useProgram)
- [WebGLRenderingContext.validateProgram()](/en-US/docs/Web/API/WebGLRenderingContext/validateProgram)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/WebGLProgram/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/webglprogram/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLProgram&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwebglprogram%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLProgram%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwebglprogram%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff2dc3d5367203c860cf1a71ce0e972f018523849%0A*+Document+last+modified%3A+2025-05-23T13%3A53%3A05.000Z%0A%0A%3C%2Fdetails%3E)
