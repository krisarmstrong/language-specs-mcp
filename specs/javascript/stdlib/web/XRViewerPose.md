# XRViewerPose

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRViewerPose&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The WebXR Device API interface `XRViewerPose` represents the pose (the position and orientation) of a viewer's point of view on the scene. Each `XRViewerPose` can have multiple views to represent, for example, the slight separation between the left and right eye.

This view can represent anything from the point-of-view of a user's XR headset to the viewpoint represented by a player's movement of an avatar using mouse and keyboard, presented on the screen, to a virtual camera capturing the scene for a spectator.

## In this article

- [Instance properties](#instance_properties)
- [Usage notes](#usage_notes)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

In addition to the properties inherited from [XRPose](/en-US/docs/Web/API/XRPose), `XRViewerPose` includes the following:

[views](/en-US/docs/Web/API/XRViewerPose/views)Read only

An array of [XRView](/en-US/docs/Web/API/XRView) objects, one for each viewpoint on the scene which is needed to represent the scene to the user. A typical headset provides a viewer pose with two views whose [eye](/en-US/docs/Web/API/XRView/eye) property is either `left` or `right`, indicating which eye that view represents. Taken together, these views can reproduce the 3D effect when displayed on the XR device.

## [Usage notes](#usage_notes)

The `XRViewerPose` object is used to describe the state of a viewer of a WebXR scene as it's tracked by the user's XR hardware. The viewer may be the virtual representation of the user, or it may represent another device or interface which may serve as the source of a position and orientation that make up a view upon the scene. For example, every player in a MMORPG might have an instance of `XRViewerPose` to provide a way to calculate what they can see; if the game provides a mechanism that tells the player if another player sees them, or that they see another player, this information becomes crucial.

An `XRViewerPose` is always obtained and referenced relative to an existing [XRReferenceSpace](/en-US/docs/Web/API/XRReferenceSpace). This ensures that positions and orientations are reported using the expected relative coordinate system.

To render a scene using the `XRViewerPose` representing the user's head, one would iterate over the views in the [views](/en-US/docs/Web/API/XRViewerPose/views) array, rendering them one after another. By calling [viewport()](/en-US/docs/Web/API/WebGLRenderingContext/viewport) on the WebGL context, specifying the `XRView` as input, you can get the viewport to use when rendering in order to draw the frame for that eye into the correct part of the drawing surface.

Also, when rendering the scene for spectators or other players in a multiplayer game, the [transform](/en-US/docs/Web/API/XRPose/transform) of the `XRViewerPose` can be used to determine both placement and facing direction of the other players in the game, so that they can be drawn in the correct place with the correct facing.

The viewer's pose for the animation frame represented by [XRFrame](/en-US/docs/Web/API/XRFrame) can be obtained by calling the frame's [getViewerPose()](/en-US/docs/Web/API/XRFrame/getViewerPose) method, specifying the reference space in which the origin's position should be computed. The returned `XRViewerPose` tells you where the viewer is and what direction they're facing at the time at which the frame takes place.

## [Examples](#examples)

In this example—part of the code to render an [XRFrame](/en-US/docs/Web/API/XRFrame), `getViewerPose()` is called to get an `XRViewerPose` using the same reference space the code is using as its base reference space. If a valid pose is returned, the frame is rendered by clearing the backbuffer and then rendering each of the views in the pose; these are most likely the views for the left and right eyes.

js

```
const pose = frame.getViewerPose(xrReferenceSpace);

if (pose) {
  const glLayer = xrSession.renderState.baseLayer;

  gl.bindFrameBuffer(gl.FRAMEBUFFER, glLayer.framebuffer);
  gl.clearColor(0, 0, 0, 1);
  gl.clearDepth(1);
  gl.clear(gl.COLOR_BUFFER_BIT, gl.DEPTH_BUFFER_BIT);

  for (const view of pose.views) {
    const viewport = glLayer.getViewport(view);
    gl.viewport(viewport.x, viewport.y, viewport.width, viewport.height);

    /* render the scene for the eye view.eye */
  }
}
```

Passing each `view` to [getViewport()](/en-US/docs/Web/API/XRWebGLLayer/getViewport) returns the WebGL viewport to apply in order to cause the rendered output to be positioned correctly in the framebuffer for rendering to the corresponding eye on the output device.

This code is derived from [Drawing a frame](/en-US/docs/Web/API/WebXR_Device_API/Movement_and_motion#drawing_a_frame) in our "Movement and motion" WebXR example. You can see more context and see much more on that page.

## [Specifications](#specifications)

Specification
[WebXR Device API# xrviewerpose-interface](https://immersive-web.github.io/webxr/#xrviewerpose-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API)
- [Movement, orientation, and motion](/en-US/docs/Web/API/WebXR_Device_API/Movement_and_motion)
- [XRPose](/en-US/docs/Web/API/XRPose) and [XRView](/en-US/docs/Web/API/XRView)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 5, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/XRViewerPose/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrviewerpose/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRViewerPose&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrviewerpose%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRViewerPose%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrviewerpose%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F89c435da452257b944b403cc9e45036fcb22590e%0A*+Document+last+modified%3A+2024-02-05T10%3A15%3A39.000Z%0A%0A%3C%2Fdetails%3E)
