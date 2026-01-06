# OrientationSensor

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FOrientationSensor&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `OrientationSensor` interface of the [Sensor APIs](/en-US/docs/Web/API/Sensor_APIs) is the base class for orientation sensors. This interface cannot be used directly. Instead it provides properties and methods accessed by interfaces that inherit from it.

This feature may be blocked by a [Permissions Policy](/en-US/docs/Web/HTTP/Guides/Permissions_Policy) set on your server.

## In this article

- [Interfaces based on OrientationSensor](#interfaces_based_on_orientationsensor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Interfaces based on OrientationSensor](#interfaces_based_on_orientationsensor)

Below is a list of interfaces based on the OrientationSensor interface.

- [AbsoluteOrientationSensor](/en-US/docs/Web/API/AbsoluteOrientationSensor)
- [RelativeOrientationSensor](/en-US/docs/Web/API/RelativeOrientationSensor)

## [Instance properties](#instance_properties)

[OrientationSensor.quaternion](/en-US/docs/Web/API/OrientationSensor/quaternion)Read only

Returns a four element [Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) whose elements contain the components of the unit quaternion representing the device's orientation.

## [Instance methods](#instance_methods)

[OrientationSensor.populateMatrix()](/en-US/docs/Web/API/OrientationSensor/populateMatrix)

Populates the given object with the rotation matrix based on the latest sensor reading.

## [Examples](#examples)

### [Basic Example](#basic_example)

The following example, which is loosely based on [Intel's Orientation Phone demo](https://intel.github.io/generic-sensor-demos/orientation-phone/), instantiates an `AbsoluteOrientationSensor` with a frequency of 60 times a second. On each reading it uses [OrientationSensor.quaternion](/en-US/docs/Web/API/OrientationSensor/quaternion) to rotate a visual model of a phone.

js

```
const options = { frequency: 60, referenceFrame: "device" };
const sensor = new AbsoluteOrientationSensor(options);

sensor.addEventListener("reading", () => {
  // model is a Three.js object instantiated elsewhere.
  model.quaternion.fromArray(sensor.quaternion).inverse();
});
sensor.addEventListener("error", (error) => {
  if (event.error.name === "NotReadableError") {
    console.log("Sensor is not available.");
  }
});
sensor.start();
```

### [Permissions Example](#permissions_example)

Using orientation sensors requires requesting permissions for multiple device sensors. Because the [Permissions](/en-US/docs/Web/API/Permissions) interface uses promises, a good way to request permissions is to use [Promise.all](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all).

js

```
const sensor = new AbsoluteOrientationSensor();
Promise.all([
  navigator.permissions.query({ name: "accelerometer" }),
  navigator.permissions.query({ name: "magnetometer" }),
  navigator.permissions.query({ name: "gyroscope" }),
]).then((results) => {
  if (results.every((result) => result.state === "granted")) {
    sensor.start();
    // …
  } else {
    console.log("No permissions to use AbsoluteOrientationSensor.");
  }
});
```

## [Specifications](#specifications)

Specification
[Orientation Sensor# orientationsensor-interface](https://w3c.github.io/orientation-sensor/#orientationsensor-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/OrientationSensor/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/orientationsensor/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FOrientationSensor&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Forientationsensor%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FOrientationSensor%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Forientationsensor%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4d929bb0a021c7130d5a71a4bf505bcb8070378d%0A*+Document+last+modified%3A+2025-03-13T12%3A48%3A23.000Z%0A%0A%3C%2Fdetails%3E)
