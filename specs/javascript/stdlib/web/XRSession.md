# XRSession

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRSession&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `XRSession` interface of the [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API) represents an ongoing XR session, providing methods and properties used to interact with and control the session. To open a WebXR session, use the [XRSystem](/en-US/docs/Web/API/XRSystem) interface's [requestSession()](/en-US/docs/Web/API/XRSystem/requestSession) method.

With `XRSession` methods, you can poll the viewer's position and orientation (the [XRViewerPose](/en-US/docs/Web/API/XRViewerPose)), gather information about the user's environment, and present imagery to the user. `XRSession` supports both inline and immersive virtual and augmented reality modes.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

In addition to the properties listed below, `XRSession` inherits properties from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[depthDataFormat](/en-US/docs/Web/API/XRSession/depthDataFormat)ExperimentalRead only

Returns the depth-sensing data format with which the session was configured.

[depthUsage](/en-US/docs/Web/API/XRSession/depthUsage)ExperimentalRead only

Returns the depth-sensing usage with which the session was configured.

[domOverlayState](/en-US/docs/Web/API/XRSession/domOverlayState)ExperimentalRead only

Provides information about the DOM overlay, if the feature is enabled.

[enabledFeatures](/en-US/docs/Web/API/XRSession/enabledFeatures)ExperimentalRead only

Returns an array of granted [session features](/en-US/docs/Web/API/XRSystem/requestSession#session_features).

[environmentBlendMode](/en-US/docs/Web/API/XRSession/environmentBlendMode)ExperimentalRead only

Returns this session's blend mode which denotes how much of the real-world environment is visible through the XR device and how the device will blend the device imagery with it.

[inputSources](/en-US/docs/Web/API/XRSession/inputSources)ExperimentalRead only

Returns a list of this session's [XRInputSource](/en-US/docs/Web/API/XRInputSource)s, each representing an input device used to control the camera and/or scene.

[interactionMode](/en-US/docs/Web/API/XRSession/interactionMode)ExperimentalRead only

Returns this session's interaction mode, which describes the best space (according to the user agent) for the application to draw interactive UI for the current session.

[preferredReflectionFormat](/en-US/docs/Web/API/XRSession/preferredReflectionFormat)ExperimentalRead only

Returns this session's preferred reflection format used for lighting estimation texture data.

[renderState](/en-US/docs/Web/API/XRSession/renderState)ExperimentalRead only

An [XRRenderState](/en-US/docs/Web/API/XRRenderState) object which contains options affecting how the imagery is rendered. This includes things such as the near and far clipping planes (distances defining how close and how far away objects can be and still get rendered), as well as field of view information.

[visibilityState](/en-US/docs/Web/API/XRSession/visibilityState)ExperimentalRead only

A string indicating whether or not the session's imagery is visible to the user, and if so, if it's being visible but not currently the target for user events.

## [Instance methods](#instance_methods)

`XRSession` provides the following methods in addition to those inherited from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[cancelAnimationFrame()](/en-US/docs/Web/API/XRSession/cancelAnimationFrame)Experimental

Removes a callback from the animation frame painting callback from `XRSession`'s set of animation frame rendering callbacks, given the identifying handle returned by a previous call to [requestAnimationFrame()](/en-US/docs/Web/API/XRSession/requestAnimationFrame).

[end()](/en-US/docs/Web/API/XRSession/end)Experimental

Ends the WebXR session. Returns a [promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which resolves when the session has been shut down.

[requestAnimationFrame()](/en-US/docs/Web/API/XRSession/requestAnimationFrame)Experimental

Schedules the specified method to be called the next time the [user agent](/en-US/docs/Glossary/User_agent) is working on rendering an animation frame for the WebXR device. Returns an integer value which can be used to identify the request for the purposes of canceling the callback using `cancelAnimationFrame()`. This method is comparable to the [Window.requestAnimationFrame()](/en-US/docs/Web/API/Window/requestAnimationFrame) method.

[requestHitTestSource()](/en-US/docs/Web/API/XRSession/requestHitTestSource)Experimental

Requests an [XRHitTestSource](/en-US/docs/Web/API/XRHitTestSource) object that handles hit test subscription.

[requestHitTestSourceForTransientInput()](/en-US/docs/Web/API/XRSession/requestHitTestSourceForTransientInput)Experimental

Requests an [XRTransientInputHitTestSource](/en-US/docs/Web/API/XRTransientInputHitTestSource) object that handles hit test subscription for a transient input source.

[requestLightProbe()](/en-US/docs/Web/API/XRSession/requestLightProbe)Experimental

Requests an [XRLightProbe](/en-US/docs/Web/API/XRLightProbe) that estimates lighting information at a given point in the user's environment.

[requestReferenceSpace()](/en-US/docs/Web/API/XRSession/requestReferenceSpace)Experimental

Requests that a new [XRReferenceSpace](/en-US/docs/Web/API/XRReferenceSpace) of the specified type be created. Returns a promise which resolves with the `XRReferenceSpace` or [XRBoundedReferenceSpace](/en-US/docs/Web/API/XRBoundedReferenceSpace) which was requested, or throws a `NotSupportedError`[DOMException](/en-US/docs/Web/API/DOMException) if the requested space type isn't supported by the device.

[updateRenderState()](/en-US/docs/Web/API/XRSession/updateRenderState)Experimental

Updates the properties of the session's render state.

## [Events](#events)

The following events are delivered to `XRSession` objects.

[end](/en-US/docs/Web/API/XRSession/end_event)Experimental

Sent to the `XRSession` object after the WebXR session has ended and all hardware-related functions have completed. The event is represented by an object of type [XRSessionEvent](/en-US/docs/Web/API/XRSessionEvent). Also available through the `onend` event handler property.

[inputsourceschange](/en-US/docs/Web/API/XRSession/inputsourceschange_event)Experimental

An event of type [XRInputSourcesChangeEvent](/en-US/docs/Web/API/XRInputSourcesChangeEvent) sent to the `XRSession` when the list of active XR input sources has changed. Also available through the `oninputsourceschange` event handler property.

[select](/en-US/docs/Web/API/XRSession/select_event)Experimental

An event of type [XRInputSourceEvent](/en-US/docs/Web/API/XRInputSourceEvent) which is sent to the session when one of the session's input sources has successfully completed a [primary action](/en-US/docs/Web/API/WebXR_Device_API/Inputs#primary_action). This generally corresponds to the user pressing a trigger, touchpad, or button, speaks a command, or performs a recognizable gesture. The `select` event is sent after the `selectstart` event is sent and immediately before the `selectend` event is sent. If `select` is not sent, then the select action was aborted before being completed. Also available through the `onselect` event handler property.

[selectend](/en-US/docs/Web/API/XRSession/selectend_event)Experimental

An event of type [XRInputSourceEvent](/en-US/docs/Web/API/XRInputSourceEvent) which gets sent to the session object when one of its input devices finishes its primary action or gets disconnected while in the process of handling a primary action. For example: for button or trigger actions, this means the button has been released; for spoken commands, it means the user has finished speaking. This is the last of the three `select*` events to be sent. Also available through the `onselectend` event handler property.

[selectstart](/en-US/docs/Web/API/XRSession/selectstart_event)Experimental

An event of type [XRInputSourceEvent](/en-US/docs/Web/API/XRInputSourceEvent) which is sent to the session object when one of its input devices is first engaged by the user in such a way as to cause the primary action to begin. This is the first of the `session*` event to be sent. Also available through the `onselectstart` event handler property.

[squeeze](/en-US/docs/Web/API/XRSession/squeeze_event)Experimental

An [XRInputSourceEvent](/en-US/docs/Web/API/XRInputSourceEvent) sent to indicate that a [primary squeeze action](/en-US/docs/Web/API/WebXR_Device_API/Inputs#primary_squeeze_action) has successfully completed. This indicates that the device being squeezed has been released, and may represent dropping a grabbed object, for example. It is sent immediately before the `squeezeend` event is sent to indicate that the squeeze action is over. Also available through the `onsqueeze` event handler property.

[squeezeend](/en-US/docs/Web/API/XRSession/squeezeend_event)Experimental

An [XRInputSourceEvent](/en-US/docs/Web/API/XRInputSourceEvent) sent to the `XRSession` when the [primary squeeze action](/en-US/docs/Web/API/WebXR_Device_API/Inputs#primary_squeeze_action) ends, whether or not the action was successful. Also available using the `onsqueezeend` event handler property.

[squeezestart](/en-US/docs/Web/API/XRSession/squeezestart_event)Experimental

An event of type [XRInputSourceEvent](/en-US/docs/Web/API/XRInputSourceEvent) which is sent to the `XRSession` when the user initially squeezes a squeezable controller. This may be, for example, a trigger which is used to represent grabbing objects, or might represent actual squeezing when wearing a haptic glove. Also available through the `onsqueezestart` event handler property.

[visibilitychange](/en-US/docs/Web/API/XRSession/visibilitychange_event)Experimental

An [XRSessionEvent](/en-US/docs/Web/API/XRSessionEvent) which is sent to the session when its visibility state as indicated by the [visibilityState](/en-US/docs/Web/API/XRSession/visibilityState) changes. Also available through the `onvisibilitychange` event handler property.

## [Example](#example)

This example establishes a new `XRSession` in `inline` mode so that it can be displayed within an HTML element, avoiding the need for a dedicated AR or VR viewing device such as a headset.

js

```
const XR = navigator.xr;

if (XR) {
  XR.requestSession("inline").then((xrSession) => {
    xrSession.requestReferenceSpace("local").then((xrReferenceSpace) => {
      xrSession.requestAnimationFrame((time, xrFrame) => {
        const viewer = xrFrame.getViewerPose(xrReferenceSpace);

        gl.bindFramebuffer(xrWebGLLayer.framebuffer);

        for (const xrView of viewer.views) {
          const xrViewport = xrWebGLLayer.getViewport(xrView);
          gl.viewport(
            xrViewport.x,
            xrViewport.y,
            xrViewport.width,
            xrViewport.height,
          );
        }
      });
    });
  });
} else {
  /* WebXR is not available */
}
```

## [Specifications](#specifications)

Specification
[WebXR Device API# xrsession-interface](https://immersive-web.github.io/webxr/#xrsession-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 2, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/XRSession/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrsession/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRSession&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrsession%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRSession%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrsession%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F104ee33c990973514704bdf8227d15c05f59ebcb%0A*+Document+last+modified%3A+2025-07-02T23%3A40%3A39.000Z%0A%0A%3C%2Fdetails%3E)
