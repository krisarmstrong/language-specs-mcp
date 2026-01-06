# ANGLE_instanced_arrays

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨June 2016⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FANGLE_instanced_arrays&level=high)

The `ANGLE_instanced_arrays` extension is part of the [WebGL API](/en-US/docs/Web/API/WebGL_API) and allows to draw the same object, or groups of similar objects multiple times, if they share the same vertex data, primitive count and type.

WebGL extensions are available using the [WebGLRenderingContext.getExtension()](/en-US/docs/Web/API/WebGLRenderingContext/getExtension) method. For more information, see also [Using Extensions](/en-US/docs/Web/API/WebGL_API/Using_Extensions) in the [WebGL tutorial](/en-US/docs/Web/API/WebGL_API/Tutorial).

Note: This extension is only available to [WebGL1](/en-US/docs/Web/API/WebGLRenderingContext) contexts. In [WebGL2](/en-US/docs/Web/API/WebGL2RenderingContext), the functionality of this extension is available on the WebGL2 context by default and the constants and methods are available without the `ANGLE_` suffix.

Despite the name "ANGLE", this extension works on any device if the hardware supports it and not just on Windows when using the ANGLE library. "ANGLE" just indicates that this extension has been written by the ANGLE library authors.

## In this article

- [Constants](#constants)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constants](#constants)

This extension exposes one new constant, which can be used in the [gl.getVertexAttrib()](/en-US/docs/Web/API/WebGLRenderingContext/getVertexAttrib) method:

[ext.VERTEX_ATTRIB_ARRAY_DIVISOR_ANGLE](#ext.vertex_attrib_array_divisor_angle)

Returns a [GLint](/en-US/docs/Web/API/WebGL_API/Types) describing the frequency divisor used for instanced rendering when used in the [gl.getVertexAttrib()](/en-US/docs/Web/API/WebGLRenderingContext/getVertexAttrib) as the `pname` parameter.

## [Instance methods](#instance_methods)

This extension exposes three new methods.

[ext.drawArraysInstancedANGLE()](/en-US/docs/Web/API/ANGLE_instanced_arrays/drawArraysInstancedANGLE)

Behaves identically to [gl.drawArrays()](/en-US/docs/Web/API/WebGLRenderingContext/drawArrays) except that multiple instances of the range of elements are executed, and the instance advances for each iteration.

[ext.drawElementsInstancedANGLE()](/en-US/docs/Web/API/ANGLE_instanced_arrays/drawElementsInstancedANGLE)

Behaves identically to [gl.drawElements()](/en-US/docs/Web/API/WebGLRenderingContext/drawElements) except that multiple instances of the set of elements are executed and the instance advances between each set.

[ext.vertexAttribDivisorANGLE()](/en-US/docs/Web/API/ANGLE_instanced_arrays/vertexAttribDivisorANGLE)

Modifies the rate at which generic vertex attributes advance when rendering multiple instances of primitives with [ext.drawArraysInstancedANGLE()](/en-US/docs/Web/API/ANGLE_instanced_arrays/drawArraysInstancedANGLE) and [ext.drawElementsInstancedANGLE()](/en-US/docs/Web/API/ANGLE_instanced_arrays/drawElementsInstancedANGLE).

## [Examples](#examples)

The following example shows how to draw a given geometry multiple times with a single draw call.

Warning: The following is educational, not production level code. It should generally be avoided to construct data / buffers within the rendering loop or right before use.

js

```
// enable the extension
const ext = gl.getExtension("ANGLE_instanced_arrays");

// binding the geometry buffer as usual
gl.bindBuffer(gl.ARRAY_BUFFER, geometryVertexBuffer);
gl.enableVertexAttribArray(vertexPositionAttributeLocation);
gl.vertexAttribPointer(
  vertexPositionAttributeLocation,
  3,
  gl.FLOAT,
  false,
  0,
  0,
);

// build position buffer
const instancePositions = [];
for (const instance of instances) {
  instancePositions.push(
    instance.position.x,
    instance.position.y,
    instance.position.z,
  );
}
const instancePositionBuffer = createWebGLBufferFromData(instancePositions);

// binding the instance position buffer as you would with any attribute
gl.bindBuffer(gl.ARRAY_BUFFER, instancePositionBuffer);
gl.enableVertexAttribArray(instancePositionAttributeLocation);
gl.vertexAttribPointer(
  instancePositionAttributeLocation,
  3,
  gl.FLOAT,
  false,
  0,
  0,
);

// mark the attribute as instanced and advance it every single(1) instance rather than every vertex
ext.vertexAttribDivisorANGLE(instancePositionAttributeLocation, 1);

// draw geometry for each instance
ext.drawArraysInstancedANGLE(
  gl.TRIANGLES,
  0,
  numGeometryVertices,
  instances.length,
);
```

## [Specifications](#specifications)

Specification[WebGL ANGLE_instanced_arrays Khronos Ratified Extension Specification](https://registry.khronos.org/webgl/extensions/ANGLE_instanced_arrays/)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebGLRenderingContext.getExtension()](/en-US/docs/Web/API/WebGLRenderingContext/getExtension)
- [WebGL2RenderingContext.drawArraysInstanced()](/en-US/docs/Web/API/WebGL2RenderingContext/drawArraysInstanced)
- [WebGL2RenderingContext.drawElementsInstanced()](/en-US/docs/Web/API/WebGL2RenderingContext/drawElementsInstanced)
- [WebGL2RenderingContext.vertexAttribDivisor()](/en-US/docs/Web/API/WebGL2RenderingContext/vertexAttribDivisor)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 24, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/ANGLE_instanced_arrays/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/angle_instanced_arrays/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FANGLE_instanced_arrays&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fangle_instanced_arrays%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FANGLE_instanced_arrays%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fangle_instanced_arrays%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fdcbb1d99185118360cc84b3a0e935e77fe0a03e3%0A*+Document+last+modified%3A+2024-09-24T13%3A57%3A44.000Z%0A%0A%3C%2Fdetails%3E)
