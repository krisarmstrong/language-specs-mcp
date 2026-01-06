# WebGL: 2D and 3D graphics for the web

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

WebGL (Web Graphics Library) is a JavaScript API for rendering high-performance interactive 3D and 2D graphics within any compatible web browser without the use of plug-ins. WebGL does so by introducing an API that closely conforms to OpenGL ES 2.0 that can be used in HTML [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) elements. This conformance makes it possible for the API to take advantage of hardware graphics acceleration provided by the user's device.

Support for WebGL is present in all modern browsers (see the [compatibility tables](#browser_compatibility) below); however, the user's device must also have hardware that supports these features.

The [WebGL 2](#webgl_2) API introduces support for much of the OpenGL ES 3.0 feature set; it's provided through the [WebGL2RenderingContext](/en-US/docs/Web/API/WebGL2RenderingContext) interface.

The [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) element is also used by the [Canvas API](/en-US/docs/Web/API/Canvas_API) to do 2D graphics on web pages.

## In this article

- [Reference](#reference)
- [Guides and tutorials](#guides_and_tutorials)
- [Resources](#resources)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Reference](#reference)

### [Standard interfaces](#standard_interfaces)

- [WebGLRenderingContext](/en-US/docs/Web/API/WebGLRenderingContext)
- [WebGL2RenderingContext](/en-US/docs/Web/API/WebGL2RenderingContext)
- [WebGLActiveInfo](/en-US/docs/Web/API/WebGLActiveInfo)
- [WebGLBuffer](/en-US/docs/Web/API/WebGLBuffer)
- [WebGLContextEvent](/en-US/docs/Web/API/WebGLContextEvent)
- [WebGLFramebuffer](/en-US/docs/Web/API/WebGLFramebuffer)
- [WebGLProgram](/en-US/docs/Web/API/WebGLProgram)
- [WebGLQuery](/en-US/docs/Web/API/WebGLQuery)
- [WebGLRenderbuffer](/en-US/docs/Web/API/WebGLRenderbuffer)
- [WebGLSampler](/en-US/docs/Web/API/WebGLSampler)
- [WebGLShader](/en-US/docs/Web/API/WebGLShader)
- [WebGLShaderPrecisionFormat](/en-US/docs/Web/API/WebGLShaderPrecisionFormat)
- [WebGLSync](/en-US/docs/Web/API/WebGLSync)
- [WebGLTexture](/en-US/docs/Web/API/WebGLTexture)
- [WebGLTransformFeedback](/en-US/docs/Web/API/WebGLTransformFeedback)
- [WebGLUniformLocation](/en-US/docs/Web/API/WebGLUniformLocation)
- [WebGLVertexArrayObject](/en-US/docs/Web/API/WebGLVertexArrayObject)

### [Extensions](#extensions)

- [ANGLE_instanced_arrays](/en-US/docs/Web/API/ANGLE_instanced_arrays)
- [EXT_blend_minmax](/en-US/docs/Web/API/EXT_blend_minmax)
- [EXT_color_buffer_float](/en-US/docs/Web/API/EXT_color_buffer_float)
- [EXT_color_buffer_half_float](/en-US/docs/Web/API/EXT_color_buffer_half_float)
- [EXT_disjoint_timer_query](/en-US/docs/Web/API/EXT_disjoint_timer_query)
- [EXT_float_blend](/en-US/docs/Web/API/EXT_float_blend)Experimental
- [EXT_frag_depth](/en-US/docs/Web/API/EXT_frag_depth)
- [EXT_shader_texture_lod](/en-US/docs/Web/API/EXT_shader_texture_lod)
- [EXT_sRGB](/en-US/docs/Web/API/EXT_sRGB)
- [EXT_texture_compression_bptc](/en-US/docs/Web/API/EXT_texture_compression_bptc)
- [EXT_texture_compression_rgtc](/en-US/docs/Web/API/EXT_texture_compression_rgtc)
- [EXT_texture_filter_anisotropic](/en-US/docs/Web/API/EXT_texture_filter_anisotropic)
- [EXT_texture_norm16](/en-US/docs/Web/API/EXT_texture_norm16)
- [KHR_parallel_shader_compile](/en-US/docs/Web/API/KHR_parallel_shader_compile)
- [OES_draw_buffers_indexed](/en-US/docs/Web/API/OES_draw_buffers_indexed)
- [OES_element_index_uint](/en-US/docs/Web/API/OES_element_index_uint)
- [OES_fbo_render_mipmap](/en-US/docs/Web/API/OES_fbo_render_mipmap)
- [OES_standard_derivatives](/en-US/docs/Web/API/OES_standard_derivatives)
- [OES_texture_float](/en-US/docs/Web/API/OES_texture_float)
- [OES_texture_float_linear](/en-US/docs/Web/API/OES_texture_float_linear)
- [OES_texture_half_float](/en-US/docs/Web/API/OES_texture_half_float)
- [OES_texture_half_float_linear](/en-US/docs/Web/API/OES_texture_half_float_linear)
- [OES_vertex_array_object](/en-US/docs/Web/API/OES_vertex_array_object)
- [OVR_multiview2](/en-US/docs/Web/API/OVR_multiview2)
- [WEBGL_color_buffer_float](/en-US/docs/Web/API/WEBGL_color_buffer_float)
- [WEBGL_compressed_texture_astc](/en-US/docs/Web/API/WEBGL_compressed_texture_astc)
- [WEBGL_compressed_texture_etc](/en-US/docs/Web/API/WEBGL_compressed_texture_etc)
- [WEBGL_compressed_texture_etc1](/en-US/docs/Web/API/WEBGL_compressed_texture_etc1)
- [WEBGL_compressed_texture_pvrtc](/en-US/docs/Web/API/WEBGL_compressed_texture_pvrtc)
- [WEBGL_compressed_texture_s3tc](/en-US/docs/Web/API/WEBGL_compressed_texture_s3tc)
- [WEBGL_compressed_texture_s3tc_srgb](/en-US/docs/Web/API/WEBGL_compressed_texture_s3tc_srgb)
- [WEBGL_debug_renderer_info](/en-US/docs/Web/API/WEBGL_debug_renderer_info)
- [WEBGL_debug_shaders](/en-US/docs/Web/API/WEBGL_debug_shaders)
- [WEBGL_depth_texture](/en-US/docs/Web/API/WEBGL_depth_texture)
- [WEBGL_draw_buffers](/en-US/docs/Web/API/WEBGL_draw_buffers)
- [WEBGL_lose_context](/en-US/docs/Web/API/WEBGL_lose_context)
- [WEBGL_multi_draw](/en-US/docs/Web/API/WEBGL_multi_draw)

### [Events](#events)

- [webglcontextlost](/en-US/docs/Web/API/HTMLCanvasElement/webglcontextlost_event)
- [webglcontextrestored](/en-US/docs/Web/API/HTMLCanvasElement/webglcontextrestored_event)
- [webglcontextcreationerror](/en-US/docs/Web/API/HTMLCanvasElement/webglcontextcreationerror_event)

### [Constants and types](#constants_and_types)

- [WebGL constants](/en-US/docs/Web/API/WebGL_API/Constants)
- [WebGL types](/en-US/docs/Web/API/WebGL_API/Types)

### [WebGL 2](#webgl_2)

WebGL 2 is a major update to WebGL which is provided through the [WebGL2RenderingContext](/en-US/docs/Web/API/WebGL2RenderingContext) interface. It is based on OpenGL ES 3.0 and new features include:

- [3D textures](/en-US/docs/Web/API/WebGL2RenderingContext/texImage3D),
- [Sampler objects](/en-US/docs/Web/API/WebGLSampler),
- [Uniform Buffer objects](/en-US/docs/Web/API/WebGL2RenderingContext#uniform_buffer_objects),
- [Sync objects](/en-US/docs/Web/API/WebGLSync),
- [Query objects](/en-US/docs/Web/API/WebGLQuery),
- [Transform Feedback objects](/en-US/docs/Web/API/WebGLTransformFeedback),
- Promoted extensions that are now core to WebGL 2: [Vertex Array objects](/en-US/docs/Web/API/WebGLVertexArrayObject), [instancing](/en-US/docs/Web/API/WebGL2RenderingContext/drawArraysInstanced), [multiple render targets](/en-US/docs/Web/API/WebGL2RenderingContext/drawBuffers), [fragment depth](/en-US/docs/Web/API/EXT_frag_depth).

See also the blog post ["WebGL 2 lands in Firefox"](https://hacks.mozilla.org/2017/01/webgl-2-lands-in-firefox/) and [webglsamples.org/WebGL2Samples](https://webglsamples.org/WebGL2Samples/) for a few demos.

## [Guides and tutorials](#guides_and_tutorials)

Below, you'll find an assortment of guides to help you learn WebGL concepts and tutorials that offer step-by-step lessons and examples.

### [Guides](#guides)

[Data in WebGL](/en-US/docs/Web/API/WebGL_API/Data)

A guide to variables, buffers, and other types of data used when writing WebGL code.

[WebGL best practices](/en-US/docs/Web/API/WebGL_API/WebGL_best_practices)

Tips and suggestions to help you improve the quality, performance, and reliability of your WebGL content.

[Using extensions](/en-US/docs/Web/API/WebGL_API/Using_Extensions)

A guide to using WebGL extensions.

### [Tutorials](#tutorials)

[WebGL tutorial](/en-US/docs/Web/API/WebGL_API/Tutorial)

A beginner's guide to WebGL core concepts. A good place to start if you don't have previous WebGL experience.

### [Examples](#examples)

[A basic 2D WebGL animation example](/en-US/docs/Web/API/WebGL_API/Basic_2D_animation_example)

This example demonstrates the simple animation of a one-color shape. Topics examined are adapting to [aspect ratio](/en-US/docs/Glossary/Aspect_ratio) differences, a function to build shader programs from sets of multiple shaders, and the basics of drawing in WebGL.

[WebGL by example](/en-US/docs/Web/API/WebGL_API/By_example)

A series of live samples with short explanations that showcase WebGL concepts and capabilities. The examples are sorted according to topic and level of difficulty, covering the WebGL rendering context, shader programming, textures, geometry, user interaction, and more.

### [Advanced tutorials](#advanced_tutorials)

[Compressed texture formats](/en-US/docs/Web/API/WebGL_API/Compressed_texture_formats)

How to enable and use compressed texture formats for better memory performance.

[WebGL model view projection](/en-US/docs/Web/API/WebGL_API/WebGL_model_view_projection)

A detailed explanation of the three core matrices that are typically used to represent a 3D object view: the model, view and projection matrices.

[Matrix math for the web](/en-US/docs/Web/API/WebGL_API/Matrix_math_for_the_web)

A useful guide to how 3D transform matrices work, and can be used on the web — both for WebGL calculations and in CSS transforms.

## [Resources](#resources)

- [Khronos WebGL site](https://www.khronos.org/webgl/) The main website for WebGL at the Khronos Group.
- [WebGL Fundamentals](https://web.dev/articles/webgl-fundamentals) A basic tutorial with fundamentals of WebGL.
- [Raw WebGL: An introduction to WebGL](https://www.youtube.com/embed/H4c8t6myAWU/?feature=player_detailpage) A talk by Nick Desaulniers that introduces the basics of WebGL.
- [WebGL Academy](https://www.webglacademy.com/) An HTML/JavaScript editor with tutorials to learn basics of webgl programming.
- [WebGL Stats](https://webglreport.com/) A site with statistics about WebGL capabilities in browsers on different platforms.

### [Libraries](#libraries)

- [three.js](https://threejs.org/) is an open-source, fully featured 3D WebGL library.
- [Babylon.js](https://www.babylonjs.com/) is a powerful, simple, and open game and 3D rendering engine packed into a friendly JavaScript framework.
- [Pixi.js](https://pixijs.com/) is a fast, open-source 2D WebGL renderer.
- [Phaser](https://phaser.io/) is a fast, free and fun open source framework for Canvas and WebGL powered browser games.
- [PlayCanvas](https://playcanvas.com/) is an open-source game engine.
- [glMatrix](https://github.com/toji/gl-matrix) is a JavaScript matrix and vector library for high-performance WebGL apps.
- [twgl](https://twgljs.org/) is a library for making webgl less verbose.
- [RedGL](https://github.com/redcamel/RedGL2) is an open-source 3D WebGL library.
- [vtk.js](https://kitware.github.io/vtk-js/) is a JavaScript library for scientific visualization in your browser.
- [webgl-lint](https://greggman.github.io/webgl-lint/) will help find errors in your WebGL code and provide useful info

## [Specifications](#specifications)

Specification
[WebGL Specification# 5.14](https://registry.khronos.org/webgl/specs/latest/1.0/#5.14)
[WebGL 2.0 Specification# 3.7](https://registry.khronos.org/webgl/specs/latest/2.0/#3.7)

## [Browser compatibility](#browser_compatibility)

### [api.WebGLRenderingContext](#api.WebGLRenderingContext)

### [api.WebGL2RenderingContext](#api.WebGL2RenderingContext)

### [Compatibility notes](#compatibility_notes)

In addition to the browser, the GPU itself also needs to support the feature. So, for example, S3 Texture Compression (S3TC) is only available on Tegra-based tablets. Most browsers make the WebGL context available through the `webgl` context name, but older ones need `experimental-webgl` as well. In addition, the upcoming [WebGL 2](/en-US/docs/Web/API/WebGL2RenderingContext) is fully backwards-compatible and will have the context name `webgl2`.

### [Gecko notes](#gecko_notes)

#### WebGL debugging and testing

Firefox provides two preferences available which let you control the capabilities of WebGL for testing purposes:

[webgl.min_capability_mode](#webgl.min_capability_mode)

A Boolean property that, when `true`, enables a minimum capability mode. When in this mode, WebGL is configured to only support the bare minimum feature set and capabilities required by the WebGL specification. This lets you ensure that your WebGL code will work on any device or browser, regardless of their capabilities. This is `false` by default.

[webgl.disable_extensions](#webgl.disable_extensions)

A Boolean property that, when `true`, disables all WebGL extensions. This is `false` by default.

## [See also](#see_also)

- [Canvas API](/en-US/docs/Web/API/Canvas_API)
- [Compatibility info about WebGL extensions](/en-US/docs/Web/API/WebGLRenderingContext/getSupportedExtensions#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 15, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/WebGL_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/webgl_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGL_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwebgl_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGL_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwebgl_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd8a5165fd3c3b35ea9d07a914459e8d468f62276%0A*+Document+last+modified%3A+2025-07-15T12%3A14%3A04.000Z%0A%0A%3C%2Fdetails%3E)
