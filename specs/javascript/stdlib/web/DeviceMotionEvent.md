# DeviceMotionEvent

 Baseline  2023  * Newly available

 Since ⁨September 2023⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDeviceMotionEvent&level=low)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `DeviceMotionEvent` interface of the [Device Orientation Events](/en-US/docs/Web/API/Device_orientation_events) provides web developers with information about the speed of changes for the device's position and orientation.

Warning: Currently, Firefox and Chrome do not handle the coordinates the same way. Take care about this while using them.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[DeviceMotionEvent()](/en-US/docs/Web/API/DeviceMotionEvent/DeviceMotionEvent)

Creates a new `DeviceMotionEvent`.

## [Instance properties](#instance_properties)

[DeviceMotionEvent.acceleration](/en-US/docs/Web/API/DeviceMotionEvent/acceleration)Read only

An object giving the acceleration of the device on the three axis X, Y and Z. Acceleration is expressed in [m/s²](https://en.wikipedia.org/wiki/Meter_per_second_squared).

[DeviceMotionEvent.accelerationIncludingGravity](/en-US/docs/Web/API/DeviceMotionEvent/accelerationIncludingGravity)Read only

An object giving the acceleration of the device on the three axis X, Y and Z with the effect of gravity. Acceleration is expressed in [m/s²](https://en.wikipedia.org/wiki/Meter_per_second_squared).

[DeviceMotionEvent.rotationRate](/en-US/docs/Web/API/DeviceMotionEvent/rotationRate)Read only

An object giving the rate of change of the device's orientation on the three orientation axis alpha, beta and gamma. Rotation rate is expressed in degrees per seconds.

[DeviceMotionEvent.interval](/en-US/docs/Web/API/DeviceMotionEvent/interval)Read only

A number representing the interval of time, in milliseconds, at which data is obtained from the device.

## [Example](#example)

js

```
window.addEventListener("devicemotion", (event) => {
  console.log(`${event.acceleration.x} m/s2`);
});
```

## [Specifications](#specifications)

Specification
[Device Orientation and Motion# devicemotion](https://w3c.github.io/deviceorientation/#devicemotion)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Detecting device orientation](/en-US/docs/Web/API/Device_orientation_events/Detecting_device_orientation)
- [Orientation and motion data explained](/en-US/docs/Web/API/Device_orientation_events/Orientation_and_motion_data_explained)
- [DeviceOrientationEvent](/en-US/docs/Web/API/DeviceOrientationEvent)
- [deviceorientation](/en-US/docs/Web/API/Window/deviceorientation_event) event
- [deviceorientationabsolute](/en-US/docs/Web/API/Window/deviceorientationabsolute_event) event
- [devicemotion](/en-US/docs/Web/API/Window/devicemotion_event) event
- [Accelerometer](/en-US/docs/Web/API/Accelerometer)
- [LinearAccelerationSensor](/en-US/docs/Web/API/LinearAccelerationSensor)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/DeviceMotionEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/devicemotionevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDeviceMotionEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdevicemotionevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDeviceMotionEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdevicemotionevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbe8f7f155a48e11b30c240f8731afb1845f85378%0A*+Document+last+modified%3A+2024-07-26T03%3A28%3A38.000Z%0A%0A%3C%2Fdetails%3E)
