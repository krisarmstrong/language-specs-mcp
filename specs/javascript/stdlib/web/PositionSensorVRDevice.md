# PositionSensorVRDevice

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

Non-standard: This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The `PositionSensorVRDevice` interface of the [WebVR API](/en-US/docs/Web/API/WebVR_API) represents VR hardware's position sensor. You can access information such as the current position and orientation of the sensor in relation to the head mounted display through the [PositionSensorVRDevice.getState()](/en-US/docs/Web/API/PositionSensorVRDevice/getState) method.

## In this article

- [Instance methods](#instance_methods)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

[PositionSensorVRDevice.getState()](/en-US/docs/Web/API/PositionSensorVRDevice/getState)DeprecatedNon-standard

Returns the current state of the position sensor for the current frame (e.g., within the current [window.requestAnimationFrame](/en-US/docs/Web/API/Window/requestAnimationFrame) callback) or for the previous frame, contained with a [VRPose](/en-US/docs/Web/API/VRPose) object. This is the method you'd normally want to use, versus `getImmediateState()`.

[PositionSensorVRDevice.getImmediateState()](/en-US/docs/Web/API/PositionSensorVRDevice/getImmediateState)DeprecatedNon-standard

Returns the current instantaneous position sensor state. This is intended to only be used rarely, for certain special uses, for example sampling the immediate position of a hand orientation sensor — or at least it will be, in the future.

[PositionSensorVRDevice.resetSensor()](/en-US/docs/Web/API/PositionSensorVRDevice/resetSensor)DeprecatedNon-standard

Can be used to reset the sensor if desired, returning the position and orientation values to zero.

## [Instance properties](#instance_properties)

This interface doesn't define any properties of its own, but it does inherit the properties of its parent interface, [VRDisplay](/en-US/docs/Web/API/VRDisplay).

[VRDisplay.displayId](/en-US/docs/Web/API/VRDisplay/displayId)Read only

Returns the ID for this specific `VRDevice`. The ID shouldn't change across browser restarts, allowing configuration data to be saved based on it.

[VRDisplay.displayName](/en-US/docs/Web/API/VRDisplay/displayName)Read only

A human-readable name to identify the `VRDevice`.

## [Examples](#examples)

The following example uses the WebVR API to update the view of a simple [2D canvas](/en-US/docs/Web/API/CanvasRenderingContext2D) scene on each frame of a [requestAnimationFrame](/en-US/docs/Web/API/Window/requestAnimationFrame) loop.

js

```
function setView() {
  const posState = gPositionSensor.getState();
  if (posState.hasPosition) {
    posPara.textContent = `Position: x${roundToTwo(
      posState.position.x,
    )} y${roundToTwo(posState.position.y)} z${roundToTwo(posState.position.z)}`;
    xPos = -posState.position.x * WIDTH * 2;
    yPos = posState.position.y * HEIGHT * 2;
    zPos = -posState.position.z > 0.01 ? -posState.position.z : 0.01;
  }

  if (posState.hasOrientation) {
    orientPara.textContent = `Orientation: x${roundToTwo(
      posState.orientation.x,
    )} y${roundToTwo(posState.orientation.y)} z${roundToTwo(
      posState.orientation.z,
    )}`;
    xOrient = posState.orientation.x * WIDTH;
    yOrient = -posState.orientation.y * HEIGHT * 2;
    zOrient = posState.orientation.z * 180;
  }
}
```

Here we are grabbing a [VRPose](/en-US/docs/Web/API/VRPose) object using [PositionSensorVRDevice.getState()](/en-US/docs/Web/API/PositionSensorVRDevice/getState) and storing it in `posState`. We then check to make sure that position and orientation info is present in the current frame using [VRPose.position](/en-US/docs/Web/API/VRPose/position) and [VRPose.orientation](/en-US/docs/Web/API/VRPose/orientation) (these return `null` if, for example the head mounted display is turned off or not pointing at the position sensor, which would cause an error.)

We then output the x, y and z position and orientation values for informational purposes, and use those values to update the `xPos`, `yPos`, `zPos`, `xOrient`, `yOrient`, and `zOrient` variables, which are used to update the scene rendering on each frame.

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebVR API](/en-US/docs/Web/API/WebVR_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/PositionSensorVRDevice/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/positionsensorvrdevice/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPositionSensorVRDevice&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpositionsensorvrdevice%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPositionSensorVRDevice%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpositionsensorvrdevice%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F702cd9e4d2834e13aea345943efc8d0c03d92ec9%0A*+Document+last+modified%3A+2025-04-03T04%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
