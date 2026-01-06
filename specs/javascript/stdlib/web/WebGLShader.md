# WebGLShader

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLShader&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The WebGLShader is part of the [WebGL API](/en-US/docs/Web/API/WebGL_API) and can either be a vertex or a fragment shader. A [WebGLProgram](/en-US/docs/Web/API/WebGLProgram) requires both types of shaders.

## In this article

- [Description](#description)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Description](#description)

To create a WebGLShader use [WebGLRenderingContext.createShader](/en-US/docs/Web/API/WebGLRenderingContext/createShader), then hook up the GLSL source code using [WebGLRenderingContext.shaderSource()](/en-US/docs/Web/API/WebGLRenderingContext/shaderSource), and finally invoke [WebGLRenderingContext.compileShader()](/en-US/docs/Web/API/WebGLRenderingContext/compileShader) to finish and compile the shader. At this point the WebGLShader is still not in a usable form and must still be attached to a [WebGLProgram](/en-US/docs/Web/API/WebGLProgram).

js

```
function createShader(gl, sourceCode, type) {
  // Compiles either a shader of type gl.VERTEX_SHADER or gl.FRAGMENT_SHADER
  const shader = gl.createShader(type);
  gl.shaderSource(shader, sourceCode);
  gl.compileShader(shader);

  if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
    const info = gl.getShaderInfoLog(shader);
    throw new Error(`Could not compile WebGL program. \n\n${info}`);
  }
  return shader;
}
```

See [WebGLProgram](/en-US/docs/Web/API/WebGLProgram) for information on attaching the shaders.

## [Examples](#examples)

### [Creating a vertex shader](#creating_a_vertex_shader)

Note that there are many other strategies for writing and accessing shader source code strings. These example are for illustration purposes only.

js

```
const vertexShaderSource =
  "attribute vec4 position;\n" +
  "void main() {\n" +
  "  gl_Position = position;\n" +
  "}\n";

// Use the createShader function from the example above
const vertexShader = createShader(gl, vertexShaderSource, gl.VERTEX_SHADER);
```

### [Creating a fragment shader](#creating_a_fragment_shader)

js

```
const fragmentShaderSource = `void main() {
  gl_FragColor = vec4(1.0, 1.0, 1.0, 1.0);
}
`;

// Use the createShader function from the example above
const fragmentShader = createShader(
  gl,
  fragmentShaderSource,
  gl.FRAGMENT_SHADER,
);
```

## [Specifications](#specifications)

Specification
[WebGL Specification# 5.8](https://registry.khronos.org/webgl/specs/latest/1.0/#5.8)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebGLProgram](/en-US/docs/Web/API/WebGLProgram)
- [WebGLRenderingContext.attachShader()](/en-US/docs/Web/API/WebGLRenderingContext/attachShader)
- [WebGLRenderingContext.bindAttribLocation()](/en-US/docs/Web/API/WebGLRenderingContext/bindAttribLocation)
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

 This page was last modified on ⁨May 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/WebGLShader/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/webglshader/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLShader&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwebglshader%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLShader%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwebglshader%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff2dc3d5367203c860cf1a71ce0e972f018523849%0A*+Document+last+modified%3A+2025-05-23T13%3A53%3A05.000Z%0A%0A%3C%2Fdetails%3E)
