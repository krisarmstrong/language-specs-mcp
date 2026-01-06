# WebXR Device API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebXR_Device_API&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

WebXR is a group of standards which are used together to support rendering 3D scenes to hardware designed for presenting virtual worlds (virtual reality, or VR), or for adding graphical imagery to the real world, (augmented reality, or AR). The WebXR Device API implements the core of the WebXR feature set, managing the selection of output devices, render the 3D scene to the chosen device at the appropriate frame rate, and manage motion vectors created using input controllers.

WebXR-compatible devices include fully-immersive 3D headsets with motion and orientation tracking, eyeglasses which overlay graphics atop the real-world scene passing through the frames, and handheld mobile phones which augment reality by capturing the world with a camera and augment that scene with computer-generated imagery.

To accomplish these things, the WebXR Device API provides the following key capabilities:

- Find compatible VR or AR output devices
- Render a 3D scene to the device at an appropriate frame rate
- (Optionally) mirror the output to a 2D display
- Create vectors representing the movements of input controls

At the most basic level, a scene is presented in 3D by computing the perspective to apply to the scene in order to render it from the viewpoint of each of the user's eyes by computing the position of each eye and rendering the scene from that position, looking in the direction the user is currently facing. Each of these two images is rendered into a single framebuffer, with the left eye's rendered image on the left and the right eye's viewpoint rendered into the right half of the buffer. Once both eyes' perspectives on the scene have been rendered, the resulting framebuffer is delivered to the WebXR device to be presented to the user through their headset or other appropriate display device.

While the older [WebVR API](/en-US/docs/Web/API/WebVR_API) was designed solely to support Virtual Reality (VR), WebXR provides support for both VR and Augmented Reality (AR) on the web. Support for AR functionality is added by the WebXR Augmented Reality Module.

A typical XR device can have either 3 or 6 degrees of freedom and might or might not have an external positional sensor.

The equipment may also include an accelerometer, barometer, or other sensors which are used to sense when the user moves through space, rotates their head, or the like.

## In this article

- [WebXR reference docs](#webxr_reference_docs)
- [Guides and tutorials](#guides_and_tutorials)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [WebXR reference docs](#webxr_reference_docs)

### Initialization

- [navigator.xr](/en-US/docs/Web/API/Navigator/xr)
- [XRSystem](/en-US/docs/Web/API/XRSystem)
- `XRPermissionStatus`
- `Permissions-Policy`: [xr-spatial-tracking](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/xr-spatial-tracking)

### Session

- [XRSession](/en-US/docs/Web/API/XRSession)
- [XRSessionEvent](/en-US/docs/Web/API/XRSessionEvent)
- [XRRenderState](/en-US/docs/Web/API/XRRenderState)

### Frame loop

- [XRFrame](/en-US/docs/Web/API/XRFrame)

### Spaces

- [XRSpace](/en-US/docs/Web/API/XRSpace)
- [XRReferenceSpace](/en-US/docs/Web/API/XRReferenceSpace)
- [XRBoundedReferenceSpace](/en-US/docs/Web/API/XRBoundedReferenceSpace)
- [XRReferenceSpaceEvent](/en-US/docs/Web/API/XRReferenceSpaceEvent)
- [XRJointSpace](/en-US/docs/Web/API/XRJointSpace)

### Views

- [XRView](/en-US/docs/Web/API/XRView)
- [XRViewport](/en-US/docs/Web/API/XRViewport)

### Geometric primitives

- [XRRigidTransform](/en-US/docs/Web/API/XRRigidTransform)

### Pose

- [XRPose](/en-US/docs/Web/API/XRPose)
- [XRJointPose](/en-US/docs/Web/API/XRJointPose)
- [XRViewerPose](/en-US/docs/Web/API/XRViewerPose)

### Input

- [XRHand](/en-US/docs/Web/API/XRHand)
- [XRInputSource](/en-US/docs/Web/API/XRInputSource)
- [XRInputSourceArray](/en-US/docs/Web/API/XRInputSourceArray)
- [XRInputSourceEvent](/en-US/docs/Web/API/XRInputSourceEvent)
- [XRInputSourcesChangeEvent](/en-US/docs/Web/API/XRInputSourcesChangeEvent)

### Layers

- [XRLayer](/en-US/docs/Web/API/XRLayer)
- [XRLayerEvent](/en-US/docs/Web/API/XRLayerEvent)
- [XRCompositionLayer](/en-US/docs/Web/API/XRCompositionLayer)
- [XRCubeLayer](/en-US/docs/Web/API/XRCubeLayer)
- [XRCylinderLayer](/en-US/docs/Web/API/XRCylinderLayer)
- [XREquirectLayer](/en-US/docs/Web/API/XREquirectLayer)
- [XRProjectionLayer](/en-US/docs/Web/API/XRProjectionLayer)
- [XRQuadLayer](/en-US/docs/Web/API/XRQuadLayer)
- [XRMediaBinding](/en-US/docs/Web/API/XRMediaBinding)

### WebGL binding

- [XRWebGLBinding](/en-US/docs/Web/API/XRWebGLBinding)
- [WebGLRenderingContext.makeXRCompatible()](/en-US/docs/Web/API/WebGLRenderingContext/makeXRCompatible)
- [XRWebGLLayer](/en-US/docs/Web/API/XRWebGLLayer)
- [XRSubImage](/en-US/docs/Web/API/XRSubImage)
- [XRWebGLSubImage](/en-US/docs/Web/API/XRWebGLSubImage)

### Anchors

- [XRAnchor](/en-US/docs/Web/API/XRAnchor)
- [XRAnchorSet](/en-US/docs/Web/API/XRAnchorSet)

### Depth sensing

- [XRDepthInformation](/en-US/docs/Web/API/XRDepthInformation)
- [XRCPUDepthInformation](/en-US/docs/Web/API/XRCPUDepthInformation)
- [XRWebGLDepthInformation](/en-US/docs/Web/API/XRWebGLDepthInformation)

### Hit testing

- [XRHitTestSource](/en-US/docs/Web/API/XRHitTestSource)
- [XRTransientInputHitTestSource](/en-US/docs/Web/API/XRTransientInputHitTestSource)
- [XRHitTestResult](/en-US/docs/Web/API/XRHitTestResult)
- [XRTransientInputHitTestResult](/en-US/docs/Web/API/XRTransientInputHitTestResult)
- [XRRay](/en-US/docs/Web/API/XRRay)

### Lighting estimation

- [XRLightEstimate](/en-US/docs/Web/API/XRLightEstimate)
- [XRLightProbe](/en-US/docs/Web/API/XRLightProbe)

## [Guides and tutorials](#guides_and_tutorials)

The following guides and tutorials are a great resource to learn how to comprehend WebXR and the underlying 3D and VR/AR graphics concepts.

### Foundations and basics

- [Fundamentals of WebXR](/en-US/docs/Web/API/WebXR_Device_API/Fundamentals)
- [Matrix math for the web](/en-US/docs/Web/API/WebGL_API/Matrix_math_for_the_web)
- [WebXR application life cycle](/en-US/docs/Web/API/WebXR_Device_API/Lifecycle)

### Creating a mixed reality experience

- [Starting up and shutting down a WebXR session](/en-US/docs/Web/API/WebXR_Device_API/Startup_and_shutdown)
- [Geometry and reference spaces in WebXR](/en-US/docs/Web/API/WebXR_Device_API/Geometry)
- [Spatial tracking in WebXR](/en-US/docs/Web/API/WebXR_Device_API/Spatial_tracking)
- [Rendering and the WebXR frame animation callback](/en-US/docs/Web/API/WebXR_Device_API/Rendering)
- [Viewpoints and viewers: Simulating cameras in WebXR](/en-US/docs/Web/API/WebXR_Device_API/Cameras)
- [A perspective retrospective for WebXR developers](/en-US/docs/Web/API/WebXR_Device_API/Perspective)
- [Lighting a WebXR setting](/en-US/docs/Web/API/WebXR_Device_API/Lighting)
- [Using bounded reference spaces](/en-US/docs/Web/API/WebXR_Device_API/Bounded_reference_spaces)

### Making it interactive

- [Movement, orientation, and motion: A WebXR example](/en-US/docs/Web/API/WebXR_Device_API/Movement_and_motion)
- [Inputs and input sources](/en-US/docs/Web/API/WebXR_Device_API/Inputs)
- [Targeting and hit detection](/en-US/docs/Web/API/WebXR_Device_API/Targeting)

### Performance and security

- [WebXR performance guide](/en-US/docs/Web/API/WebXR_Device_API/Performance)
- [Permissions and security for WebXR](/en-US/docs/Web/API/WebXR_Device_API/Permissions_and_security)

## [Specifications](#specifications)

Specification[WebXR Device API](https://immersive-web.github.io/webxr/)[WebXR Anchors Module](https://immersive-web.github.io/anchors/)[WebXR Augmented Reality Module - Level 1](https://immersive-web.github.io/webxr-ar-module/)[WebXR Depth Sensing Module](https://immersive-web.github.io/depth-sensing/)[WebXR DOM Overlays Module](https://immersive-web.github.io/dom-overlays/)[WebXR Gamepads Module - Level 1](https://immersive-web.github.io/webxr-gamepads-module/)[WebXR Hand Input Module - Level 1](https://immersive-web.github.io/webxr-hand-input/)[WebXR Hit Test Module](https://immersive-web.github.io/hit-test/)[WebXR Layers API Level 1](https://immersive-web.github.io/layers/)[WebXR Lighting Estimation API Level 1](https://immersive-web.github.io/lighting-estimation/)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Drawing graphics](/en-US/docs/Learn_web_development/Extensions/Client-side_APIs/Drawing_graphics)
- [WebGL API](/en-US/docs/Web/API/WebGL_API): Accelerated 2D and 3D graphics on the web
- [Canvas API](/en-US/docs/Web/API/Canvas_API): 2D drawing for the web
- [Canvas tutorial](/en-US/docs/Web/API/Canvas_API/Tutorial)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 4, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/WebXR_Device_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/webxr_device_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebXR_Device_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwebxr_device_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebXR_Device_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwebxr_device_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F832bcb292fdf15ce9ba842f9a5025b5593454a65%0A*+Document+last+modified%3A+2025-04-04T17%3A12%3A19.000Z%0A%0A%3C%2Fdetails%3E)
