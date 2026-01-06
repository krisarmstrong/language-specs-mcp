# WebVR API

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

Non-standard: This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

Note: WebVR API is replaced by [WebXR API](/en-US/docs/Web/API/WebXR_Device_API). WebVR was never ratified as a standard, was implemented and enabled by default in very few browsers and supported a small number of devices.

WebVR provides support for exposing virtual reality devices — for example, head-mounted displays like the Oculus Rift or HTC Vive — to web apps, enabling developers to translate position and movement information from the display into movement around a 3D scene. This has numerous, interesting applications, from virtual product tours and interactive training apps to immersive first-person games.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [WebVR interfaces](#webvr_interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

Any VR devices attached to your computer will be returned by the [Navigator.getVRDisplays()](/en-US/docs/Web/API/Navigator/getVRDisplays) method; each one will be represented by a [VRDisplay](/en-US/docs/Web/API/VRDisplay) object.

[VRDisplay](/en-US/docs/Web/API/VRDisplay) is the central interface in the WebVR API — via its properties and methods you can access functionality to:

- Retrieve useful information to allow us to identify the display, what capabilities it has, controllers associated with it, and more.
- Retrieve [frame data](/en-US/docs/Web/API/VRFrameData) for each frame of content you want to present in a display, and submit those frames for display at a consistent rate.
- Start and stop presenting to the display.

A typical (simple) WebVR app would work like so:

1. [Navigator.getVRDisplays()](/en-US/docs/Web/API/Navigator/getVRDisplays) is used to get a reference to your VR display.
2. [VRDisplay.requestPresent()](/en-US/docs/Web/API/VRDisplay/requestPresent) is used to start presenting to the VR display.
3. WebVR's dedicated [VRDisplay.requestAnimationFrame()](/en-US/docs/Web/API/VRDisplay/requestAnimationFrame) method is used to run the app's rendering loop at the correct refresh rate for the display.
4. Inside the rendering loop, you grab the data required to display the current frame ([VRDisplay.getFrameData()](/en-US/docs/Web/API/VRDisplay/getFrameData)), draw the displayed scene twice — once for the view in each eye, then submit the rendered view to the display to show to the user ([VRDisplay.submitFrame()](/en-US/docs/Web/API/VRDisplay/submitFrame)).

In addition, WebVR 1.1 adds a number of events on the [Window](/en-US/docs/Web/API/Window) object to allow JavaScript to respond to changes to the status of the display.

Note: You can find a lot more out about how the API works in our [Using the WebVR API](/en-US/docs/Web/API/WebVR_API/Using_the_WebVR_API) and [WebVR Concepts](/en-US/docs/Web/API/WebVR_API/Concepts) articles.

### [API availability](#api_availability)

The WebVR API, which was never ratified as a web standard, has been deprecated in favor of the [WebXR API](/en-US/docs/Web/API/WebXR_Device_API), which is well on track toward finishing the standardization process. As such, you should try to update existing code to use the newer API instead. Generally the transition should be fairly painless.

Additionally, on some devices and/or browsers, WebVR requires that the page be loaded using a secure context, over an HTTPS connection. If the page is not fully secure, the WebVR methods and functions will not be available. You can easily test for this by checking to see if the [Navigator](/en-US/docs/Web/API/Navigator) method [getVRDisplays()](/en-US/docs/Web/API/Navigator/getVRDisplays) is `NULL`:

js

```
if (!navigator.getVRDisplays) {
  console.error("WebVR is not available");
} else {
  /* Use WebVR */
}
```

### [Using controllers: Combining WebVR with the Gamepad API](#using_controllers_combining_webvr_with_the_gamepad_api)

Many WebVR hardware setups feature controllers that go along with the headset. These can be used in WebVR apps via the [Gamepad API](/en-US/docs/Web/API/Gamepad_API), and specifically the [Gamepad Extensions API](/en-US/docs/Web/API/Gamepad_API#experimental_gamepad_extensions) that adds API features for accessing [controller pose](/en-US/docs/Web/API/GamepadPose), [haptic actuators](/en-US/docs/Web/API/GamepadHapticActuator), and more.

Note: Our [Using VR controllers with WebVR](/en-US/docs/Web/API/WebVR_API/Using_VR_controllers_with_WebVR) article explains the basics of how to use VR controllers with WebVR apps.

## [WebVR interfaces](#webvr_interfaces)

[VRDisplay](/en-US/docs/Web/API/VRDisplay)

Represents any VR device supported by this API. It includes generic information such as device IDs and descriptions, as well as methods for starting to present a VR scene, retrieving eye parameters and display capabilities, and other important functionality.

[VRDisplayCapabilities](/en-US/docs/Web/API/VRDisplayCapabilities)

Describes the capabilities of a [VRDisplay](/en-US/docs/Web/API/VRDisplay) — its features can be used to perform VR device capability tests, for example can it return position information.

[VRDisplayEvent](/en-US/docs/Web/API/VRDisplayEvent)

Represents the event object of WebVR-related events (see the [window events](#window_events) listed below).

[VRFrameData](/en-US/docs/Web/API/VRFrameData)

Represents all the information needed to render a single frame of a VR scene; constructed by [VRDisplay.getFrameData()](/en-US/docs/Web/API/VRDisplay/getFrameData).

[VRPose](/en-US/docs/Web/API/VRPose)

Represents the position state at a given timestamp (which includes orientation, position, velocity, and acceleration).

[VREyeParameters](/en-US/docs/Web/API/VREyeParameters)

Provides access to all the information required to correctly render a scene for each given eye, including field of view information.

[VRFieldOfView](/en-US/docs/Web/API/VRFieldOfView)

Represents a field of view defined by 4 different degree values describing the view from a center point.

[VRLayerInit](/en-US/docs/Web/API/VRLayerInit)

Represents a layer to be presented in a [VRDisplay](/en-US/docs/Web/API/VRDisplay).

[VRStageParameters](/en-US/docs/Web/API/VRStageParameters)

Represents the values describing the stage area for devices that support room-scale experiences.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

The WebVR API extends the following APIs, adding the listed features.

#### Gamepad

[Gamepad.displayId](/en-US/docs/Web/API/Gamepad/displayId)Read only

Returns the [VRDisplay.displayId](/en-US/docs/Web/API/VRDisplay/displayId) of the associated [VRDisplay](/en-US/docs/Web/API/VRDisplay) — the `VRDisplay` that the gamepad is controlling the displayed scene of.

#### Navigator

[Navigator.activeVRDisplays](/en-US/docs/Web/API/Navigator/activeVRDisplays)Read only

Returns an array containing every [VRDisplay](/en-US/docs/Web/API/VRDisplay) object that is currently presenting ([VRDisplay.isPresenting](/en-US/docs/Web/API/VRDisplay/isPresenting) is `true`).

[Navigator.getVRDisplays()](/en-US/docs/Web/API/Navigator/getVRDisplays)

Returns a promise that resolves to an array of [VRDisplay](/en-US/docs/Web/API/VRDisplay) objects representing any available VR displays connected to the computer.

#### Window events

[vrdisplaypresentchange](/en-US/docs/Web/API/Window/vrdisplaypresentchange_event)

Fired when the presenting state of a VR display changes — i.e., goes from presenting to not presenting or vice versa.

[vrdisplayconnect](/en-US/docs/Web/API/Window/vrdisplayconnect_event)

Fired when a compatible VR display has been connected to the computer.

[vrdisplaydisconnect](/en-US/docs/Web/API/Window/vrdisplaydisconnect_event)

Fired when a compatible VR display has been disconnected from the computer.

[vrdisplayactivate](/en-US/docs/Web/API/Window/vrdisplayactivate_event)

Fired when a display is able to be presented to.

[vrdisplaydeactivate](/en-US/docs/Web/API/Window/vrdisplaydeactivate_event)

Fired when a display can no longer be presented to.

## [Examples](#examples)

You can find a number of examples at these locations:

- [webvr-tests](https://github.com/mdn/webvr-tests) — very simple examples to accompany the MDN WebVR documentation.
- [Carmel starter kit](https://github.com/facebookarchive/Carmel-Starter-Kit) — nice simple, well-commented examples that go along with Carmel, Facebook's WebVR browser.
- [WebVR.info samples](https://webvr.info/samples/) — slightly more in-depth examples plus source code
- [A-Frame homepage](https://aframe.io/) — examples showing A-Frame usage

## [Specifications](#specifications)

This API was specified in the old [WebVR API](https://immersive-web.github.io/webvr/spec/1.1/) that has been superseded by the [WebXR Device API](https://immersive-web.github.io/webxr/). It is no longer on track to becoming a standard.

Until all browsers have implemented the new [WebXR APIs](/en-US/docs/Web/API/WebXR_Device_API/Fundamentals), it is recommended to rely on frameworks, like [A-Frame](https://aframe.io/), [Babylon.js](https://www.babylonjs.com/), or [Three.js](https://threejs.org/), or a [polyfill](https://github.com/immersive-web/webxr-polyfill), to develop WebXR applications that will work across all browsers. Read [Meta's Porting from WebVR to WebXR](https://developers.meta.com/horizon/documentation/web/port-vr-xr/) guide for more information.

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [A-Frame](https://aframe.io/) — Open source web framework for building VR experiences.
- [webvr.info](https://webvr.info/) — Up-to-date information about WebVR, browser setup, and community.
- [threejs-vr-boilerplate](https://github.com/MozillaReality/vr-web-examples/tree/master/threejs-vr-boilerplate) — A useful starter template for writing WebVR apps into.
- [Web VR polyfill](https://github.com/immersive-web/webvr-polyfill) — JavaScript implementation of WebVR.
- [WebVR Directory](https://webvr.directory/) — List of quality WebVR sites.

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/WebVR_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/webvr_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebVR_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwebvr_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebVR_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwebvr_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F702cd9e4d2834e13aea345943efc8d0c03d92ec9%0A*+Document+last+modified%3A+2025-04-03T04%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
