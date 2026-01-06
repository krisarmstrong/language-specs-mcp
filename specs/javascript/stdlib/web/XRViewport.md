# XRViewport

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRViewport&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The WebXR Device API's `XRViewport` interface provides properties used to describe the size and position of the current viewport within the [XRWebGLLayer](/en-US/docs/Web/API/XRWebGLLayer) being used to render the 3D scene.

## In this article

- [Instance properties](#instance_properties)
- [Usage notes](#usage_notes)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[height](/en-US/docs/Web/API/XRViewport/height)Read only

The height, in pixels, of the viewport.

[width](/en-US/docs/Web/API/XRViewport/width)Read only

The width, in pixels, of the viewport.

[x](/en-US/docs/Web/API/XRViewport/x)Read only

The offset from the origin of the destination graphics surface (typically a [XRWebGLLayer](/en-US/docs/Web/API/XRWebGLLayer)) to the left edge of the viewport, in pixels.

[y](/en-US/docs/Web/API/XRViewport/y)Read only

The offset from the origin of the viewport to the bottom edge of the viewport; WebGL's coordinate system places (0, 0) at the bottom left corner of the surface.

## [Usage notes](#usage_notes)

Currently, the only type of surface available is the [XRWebGLLayer](/en-US/docs/Web/API/XRWebGLLayer). The precise orientation of the coordinate system may vary with other surface types, but in WebGL, the origin (0, 0) is located at the bottom-left corner of the surface. Thus the values specified in an `XRViewport` define a rectangle whose bottom-left corner is at (`x`, `y`) and which extends `width` pixels toward the left and `height` pixels upward.

These values may be passed directly into the [WebGLRenderingContext.viewport()](/en-US/docs/Web/API/WebGLRenderingContext/viewport) method:

js

```
const xrViewport = xrWebGLLayer.getViewport(xrView);
gl.viewport(xrViewport.x, xrViewport.y, xrViewport.width, xrViewport.height);
```

## [Example](#example)

This example sets up an animation frame callback using [requestAnimationFrame()](/en-US/docs/Web/API/XRSession/requestAnimationFrame). After initial setup, it iterates over each of the views within the viewer's pose, configuring the viewport as dictated by the [XRWebGLLayer](/en-US/docs/Web/API/XRWebGLLayer).

js

```
xrSession.requestAnimationFrame((time, xrFrame) => {
  const viewerPose = xrFrame.getViewerPose(xrReferenceSpace);

  gl.bindFramebuffer(xrWebGLLayer.framebuffer);

  for (const xrView of viewerPose.views) {
    const xrViewport = xrWebGLLayer.getViewport(xrView);
    gl.viewport(
      xrViewport.x,
      xrViewport.y,
      xrViewport.width,
      xrViewport.height,
    );

    // Now we can use WebGL to draw into a viewport matching
    // the viewer's needs
  }
});
```

## [Specifications](#specifications)

Specification
[WebXR Device API# xrviewport-interface](https://immersive-web.github.io/webxr/#xrviewport-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 7, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/XRViewport/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrviewport/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRViewport&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrviewport%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRViewport%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrviewport%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Facfe8c9f1f4145f77653a2bc64a9744b001358dc%0A*+Document+last+modified%3A+2023-07-07T07%3A19%3A19.000Z%0A%0A%3C%2Fdetails%3E)
