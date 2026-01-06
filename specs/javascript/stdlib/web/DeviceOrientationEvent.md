# DeviceOrientationEvent

 Baseline  2023  * Newly available

 Since ⁨September 2023⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDeviceOrientationEvent&level=low)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `DeviceOrientationEvent` interface of the [Device Orientation Events](/en-US/docs/Web/API/Device_orientation_events) provides web developers with information from the physical orientation of the device running the web page.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[DeviceOrientationEvent.DeviceOrientationEvent()](/en-US/docs/Web/API/DeviceOrientationEvent/DeviceOrientationEvent)

Creates a new `DeviceOrientationEvent`.

## [Instance properties](#instance_properties)

[DeviceOrientationEvent.absolute](/en-US/docs/Web/API/DeviceOrientationEvent/absolute)Read only

A boolean that indicates whether or not the device is providing orientation data absolutely.

[DeviceOrientationEvent.alpha](/en-US/docs/Web/API/DeviceOrientationEvent/alpha)Read only

A number representing the motion of the device around the z axis, express in degrees with values ranging from 0 (inclusive) to 360 (exclusive).

[DeviceOrientationEvent.beta](/en-US/docs/Web/API/DeviceOrientationEvent/beta)Read only

A number representing the motion of the device around the x axis, express in degrees with values ranging from -180 (inclusive) to 180 (exclusive). This represents a front to back motion of the device.

[DeviceOrientationEvent.gamma](/en-US/docs/Web/API/DeviceOrientationEvent/gamma)Read only

A number representing the motion of the device around the y axis, express in degrees with values ranging from -90 (inclusive) to 90 (exclusive). This represents a left to right motion of the device.

[DeviceOrientationEvent.webkitCompassHeading 
Non-standard
 Read only](#deviceorientationevent.webkitcompassheading)

A number represents the difference between the motion of the device around the z axis of the world system and the direction of the north, express in degrees with values ranging from 0 to 360.

[DeviceOrientationEvent.webkitCompassAccuracy 
Non-standard
 Read only](#deviceorientationevent.webkitcompassaccuracy)

The accuracy of the compass means that the deviation is positive or negative. It's usually 10.

## [Example](#example)

js

```
window.addEventListener("deviceorientation", (event) => {
  console.log(`${event.alpha} : ${event.beta} : ${event.gamma}`);
});
```

## [Specifications](#specifications)

Specification
[Device Orientation and Motion# deviceorientation](https://w3c.github.io/deviceorientation/#deviceorientation)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Detecting device orientation](/en-US/docs/Web/API/Device_orientation_events/Detecting_device_orientation)
- [Orientation and motion data explained](/en-US/docs/Web/API/Device_orientation_events/Orientation_and_motion_data_explained)
- [DeviceMotionEvent](/en-US/docs/Web/API/DeviceMotionEvent)
- [devicemotion](/en-US/docs/Web/API/Window/devicemotion_event) event
- [deviceorientation](/en-US/docs/Web/API/Window/deviceorientation_event) event
- [deviceorientationabsolute](/en-US/docs/Web/API/Window/deviceorientationabsolute_event) event

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 16, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/DeviceOrientationEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/deviceorientationevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDeviceOrientationEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdeviceorientationevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDeviceOrientationEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdeviceorientationevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F358fa889eb017b3495e93d8b5aa6990752deb939%0A*+Document+last+modified%3A+2023-12-16T12%3A34%3A25.000Z%0A%0A%3C%2Fdetails%3E)
