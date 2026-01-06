# Device orientation events

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Device orientation events are events that allow you to [detect a device's physical orientation](/en-US/docs/Web/API/Device_orientation_events/Detecting_device_orientation#processing_orientation_events), as well as allowing you to [detect the device's motion](/en-US/docs/Web/API/Device_orientation_events/Detecting_device_orientation#processing_motion_events).

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

Mobile devices commonly have sensors such as gyroscopes, compasses, and accelerometers that can enable applications running on the device to detect the device's orientation and motion.

The device orientation events enable you to write web applications that can change their behavior based on the orientation of the user's device, and that can react when the user moves their device.

Some typical features for which you might want to use the device orientation events include:

- 

in web-based games, to enable the user to control the motion of characters or objects in the game by tilting and moving the device

- 

in mapping applications, to re-orient a map based on the device's position, or to provide turn-by-turn directions that update with the user's movements

- 

for gesture recognition — for example, recognizing a "shake" gesture and using it to perform some action such as clearing an input area when the user shakes the device

Note: This API is widely supported on mobile browsers. While some desktop-only browsers may have limitations due to hardware differences, these constraints are rarely significant given the API's primary usage on sensor-equipped devices.

## [Interfaces](#interfaces)

[DeviceMotionEvent](/en-US/docs/Web/API/DeviceMotionEvent)

Represents changes in the acceleration of a device, as well as the rotation rate.

[DeviceMotionEventAcceleration](/en-US/docs/Web/API/DeviceMotionEventAcceleration)

Represents the amount of acceleration the device is experiencing along all three axes

[DeviceMotionEventRotationRate](/en-US/docs/Web/API/DeviceMotionEventRotationRate)

Represents the rate at which the device is rotating around all three axes.

[DeviceOrientationEvent](/en-US/docs/Web/API/DeviceOrientationEvent)

Represents changes in the physical orientation of a device.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[devicemotion](/en-US/docs/Web/API/Window/devicemotion_event) event

Fired at a regular interval to indicate the amount of physical force of acceleration the device is receiving at that time, and the rate of rotation of the device.

[deviceorientation](/en-US/docs/Web/API/Window/deviceorientation_event) event

Fired when fresh data is available from the device about the current orientation of the device as compared to the Earth coordinate frame.

[deviceorientationabsolute](/en-US/docs/Web/API/Window/deviceorientationabsolute_event) event

Fired when absolute device orientation changes.

## [Specifications](#specifications)

Specification[Device Orientation and Motion](https://w3c.github.io/deviceorientation/)

## [Browser compatibility](#browser_compatibility)

### [api.Window.deviceorientation_event](#api.Window.deviceorientation_event)

### [api.Window.devicemotion_event](#api.Window.devicemotion_event)

### [api.Window.deviceorientationabsolute_event](#api.Window.deviceorientationabsolute_event)

### [api.DeviceOrientationEvent](#api.DeviceOrientationEvent)

### [api.DeviceMotionEvent](#api.DeviceMotionEvent)

### [api.DeviceMotionEventAcceleration](#api.DeviceMotionEventAcceleration)

### [api.DeviceMotionEventRotationRate](#api.DeviceMotionEventRotationRate)

## [See also](#see_also)

- [Device Orientation & Motion](https://web.dev/articles/device-orientation) at web.dev

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Device_orientation_events/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/device_orientation_events/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDevice_orientation_events&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdevice_orientation_events%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDevice_orientation_events%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdevice_orientation_events%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbe8f7f155a48e11b30c240f8731afb1845f85378%0A*+Document+last+modified%3A+2024-07-26T03%3A28%3A38.000Z%0A%0A%3C%2Fdetails%3E)
