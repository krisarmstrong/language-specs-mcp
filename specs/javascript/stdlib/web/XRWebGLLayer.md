# XRWebGLLayer

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRWebGLLayer&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `XRWebGLLayer` interface of the WebXR Device API provides a linkage between the WebXR device (or simulated XR device, in the case of an inline session) and a WebGL context used to render the scene for display on the device. In particular, it provides access to the WebGL framebuffer and viewport to ease access to the context.

Although `XRWebGLLayer` is currently the only type of framebuffer layer supported by [WebGL](/en-US/docs/Web/API/WebGL_API), it's entirely possible that future updates to the WebXR specification may allow for other layer types and corresponding image sources.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[XRWebGLLayer()](/en-US/docs/Web/API/XRWebGLLayer/XRWebGLLayer)Experimental

Creates and returns a new `XRWebGLLayer` object for use by the specified [XRSession](/en-US/docs/Web/API/XRSession), using a particular [WebGLRenderingContext](/en-US/docs/Web/API/WebGLRenderingContext) or [WebGL2RenderingContext](/en-US/docs/Web/API/WebGL2RenderingContext) as the destination context.

## [Instance properties](#instance_properties)

[antialias](/en-US/docs/Web/API/XRWebGLLayer/antialias)Read onlyExperimental

A Boolean value indicating whether or not the WebGL context's framebuffer supports anti-aliasing. The specific type of anti-aliasing is determined by the [user agent](/en-US/docs/Glossary/User_agent).

[fixedFoveation](/en-US/docs/Web/API/XRWebGLLayer/fixedFoveation)Experimental

A number indicating the amount of foveation used by the XR compositor. Fixed Foveated Rendering (FFR) renders the edges of the eye textures at a lower resolution than the center and reduces the GPU load.

[framebuffer](/en-US/docs/Web/API/XRWebGLLayer/framebuffer)Read onlyExperimental

Returns a [WebGLFramebuffer](/en-US/docs/Web/API/WebGLFramebuffer) suitable for passing into the [bindFrameBuffer()](/en-US/docs/Web/API/WebGLRenderingContext/bindFramebuffer) method.

[framebufferWidth](/en-US/docs/Web/API/XRWebGLLayer/framebufferWidth)Read onlyExperimental

Returns the width of the `XRWebGLLayer`'s framebuffer.

[framebufferHeight](/en-US/docs/Web/API/XRWebGLLayer/framebufferHeight)Read onlyExperimental

Returns the height of the layer's framebuffer.

[ignoreDepthValues](/en-US/docs/Web/API/XRWebGLLayer/ignoreDepthValues)Read onlyExperimental

A Boolean which Indicates whether or not the [WebXR compositor](/en-US/docs/Web/API/WebXR_Device_API/Fundamentals#the_webxr_compositor) should make use of the contents of the layer's depth buffer while compositing the scene.

## [Static methods](#static_methods)

[getNativeFramebufferScaleFactor()](/en-US/docs/Web/API/XRWebGLLayer/getNativeFramebufferScaleFactor_static)Experimental

Returns the scaling factor that can be used to scale the resolution of the recommended WebGL framebuffer resolution to the rendering device's native resolution.

## [Instance methods](#instance_methods)

[getViewport()](/en-US/docs/Web/API/XRWebGLLayer/getViewport)Experimental

Returns a new [XRViewport](/en-US/docs/Web/API/XRViewport) instance representing the position, width, and height to which the [WebGL context's viewport](/en-US/docs/Web/API/WebGLRenderingContext/viewport) must be set to contain drawing to the area of the framebuffer designated for the specified view's contents. In this way, for example, the rendering of the left eye's point of view and of the right eye's point of view are each placed into the correct parts of the framebuffer.

## [Examples](#examples)

### [Binding the layer to a WebGL context](#binding_the_layer_to_a_webgl_context)

This snippet, taken from [Drawing a frame](/en-US/docs/Web/API/WebXR_Device_API/Movement_and_motion#drawing_a_frame) in our "Movement and motion" WebXR example, shows how the `XRWebGLLayer` is obtained from the [XRSession](/en-US/docs/Web/API/XRSession) object's rendering state and is then bound as the current rendering WebGL framebuffer by calling the WebGL [bindFrameBuffer()](/en-US/docs/Web/API/WebGLRenderingContext/bindFramebuffer) function.

js

```
let glLayer = xrSession.renderState.baseLayer;
gl.bindFrameBuffer(gl.FRAMEBUFFER, glLayer.framebuffer);
```

### [Rendering every view in a frame](#rendering_every_view_in_a_frame)

Each time the GPU is ready to render the scene to the XR device, the XR runtime calls the function you specified when you called the [XRSession](/en-US/docs/Web/API/XRSession) method [requestAnimationFrame()](/en-US/docs/Web/API/XRSession/requestAnimationFrame) to ask to render the frame.

That function receives as input an [XRFrame](/en-US/docs/Web/API/XRFrame) which encapsulates the data needed to render the frame. This information includes the pose (an [XRViewerPose](/en-US/docs/Web/API/XRViewerPose) object) that describes the position and facing direction of the viewer within the scene as well as a list of [XRView](/en-US/docs/Web/API/XRView) objects, each representing one perspective on the scene. In current WebXR implementations, there will never be more than two entries in this list: one describing the position and viewing angle of the left eye and another doing the same for the right.

js

```
let pose = xrFrame.getViewerPose(xrReferenceSpace);

if (pose) {
  const glLayer = xrSession.renderState.baseLayer;
  gl.bindFrameBuffer(gl.FRAMEBUFFER, glLayer.framebuffer);

  for (const view of pose.views) {
    const viewport = glLayer.getViewport(view);
    gl.viewport(viewport.x, viewport.y, viewport.width, viewport.height);

    /* Render the view */
  }
}
```

## [Specifications](#specifications)

Specification
[WebXR Device API# xrwebgllayer-interface](https://immersive-web.github.io/webxr/#xrwebgllayer-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API)
- [Getting started with WebGL](/en-US/docs/Web/API/WebGL_API/Tutorial/Getting_started_with_WebGL)
- [WebGLRenderingContext](/en-US/docs/Web/API/WebGLRenderingContext) and [WebGL2RenderingContext](/en-US/docs/Web/API/WebGL2RenderingContext)
- [Drawing a frame](/en-US/docs/Web/API/WebXR_Device_API/Movement_and_motion#drawing_a_frame) in our "Movement and motion" WebXR example

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 28, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/XRWebGLLayer/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrwebgllayer/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRWebGLLayer&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrwebgllayer%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRWebGLLayer%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrwebgllayer%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9a4005caa5cc13f5174e3b8981eeec5631ed83d1%0A*+Document+last+modified%3A+2024-10-28T12%3A46%3A03.000Z%0A%0A%3C%2Fdetails%3E)
