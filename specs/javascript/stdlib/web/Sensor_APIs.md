# Sensor APIs

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The Sensor APIs are a set of interfaces built to a common design that expose device sensors in a consistent way to the web platform.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Concepts and usage](#concepts_and_usage)

Although the Generic Sensor API specification defines a [Sensor](/en-US/docs/Web/API/Sensor) interface, as a web developer you will never use it. Instead you'll use one of its subclasses to retrieve specific kinds of sensor data. For example, the [Accelerometer](/en-US/docs/Web/API/Accelerometer) interface returns the acceleration of the device along all three axes at the time it is read.

Sensors may or may not correspond exactly to a physical device sensor. For example, the [Gyroscope](/en-US/docs/Web/API/Gyroscope) interface corresponds exactly to a physical device interface. Alternatively, the [AbsoluteOrientationSensor](/en-US/docs/Web/API/AbsoluteOrientationSensor) interface provides information that is algorithmically aggregated from two or more device sensors. These sensor types are referred to as low-level and high-level respectively. The latter type of sensor is also called a fusion sensor (alternatively, virtual or synthetic sensors).

### [Feature detection](#feature_detection)

Sensor interfaces are only proxies for the underlying device sensors. Consequently, feature detection is more complicated for sensors than it is for other APIs. The presence of a sensor API does not tell you whether that API is connected to a real hardware sensor, whether that sensor works, if it's still connected, or even whether the user has granted access to it. Making all this information consistently available is costly to performance and battery life.

Therefore, feature detection for sensor APIs must include both detection of the APIs themselves and [defensive programming strategies (see below)](#defensive_programming).

The examples below show three methods for detecting sensor APIs. Additionally you can put object instantiation inside a [try...catch](/en-US/docs/Web/JavaScript/Reference/Statements/try...catch) block. Notice that detection through the [Navigator](/en-US/docs/Web/API/Navigator) interface is not one of the available options.

js

```
if (typeof Gyroscope === "function") {
  // run in circles…
}

if ("ProximitySensor" in window) {
  // watch out!
}

if (window.AmbientLightSensor) {
  // go dark…
}
```

### [Defensive programming](#defensive_programming)

As stated in Feature Detection, checking for a particular sensor API is insufficient for feature detection. The existence of an actual sensor must be confirmed as well. This is where defensive programming is needed. Defensive programming requires three strategies.

- Checking for thrown errors when instantiating a sensor object.
- Listening for errors thrown during its use.
- Handling the errors gracefully so that the user experience is enhanced rather than degraded.

The code example below illustrates these principles. The [try...catch](/en-US/docs/Web/JavaScript/Reference/Statements/try...catch) block catches errors thrown during sensor instantiation. It listens for [error](/en-US/docs/Web/API/Sensor/error_event) events to catch errors thrown during use. The only time anything is shown to the user is when [permissions](/en-US/docs/Web/API/Permissions_API) need to be requested and when the sensor type isn't supported by the device.

In addition, this feature may be blocked by a [Permissions Policy](/en-US/docs/Web/HTTP/Guides/Permissions_Policy) set on your server.

js

```
let accelerometer = null;
try {
  accelerometer = new Accelerometer({ referenceFrame: "device" });
  accelerometer.addEventListener("error", (event) => {
    // Handle runtime errors.
    if (event.error.name === "NotAllowedError") {
      // Branch to code for requesting permission.
    } else if (event.error.name === "NotReadableError") {
      console.log("Cannot connect to the sensor.");
    }
  });
  accelerometer.addEventListener("reading", () => reloadOnShake(accelerometer));
  accelerometer.start();
} catch (error) {
  // Handle construction errors.
  if (error.name === "SecurityError") {
    // See the note above about permissions policy.
    console.log("Sensor construction was blocked by a permissions policy.");
  } else if (error.name === "ReferenceError") {
    console.log("Sensor is not supported by the User Agent.");
  } else {
    throw error;
  }
}
```

### [Permissions and Permissions Policy](#permissions_and_permissions_policy)

Sensor readings may not be taken unless the user grants permission to a specific sensor type using the [Permissions API](/en-US/docs/Web/API/Permissions_API) and/or if access is not blocked by the server [Permissions-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy).

The example below shows how to request user-permission before attempting to use the sensor.

js

```
navigator.permissions.query({ name: "accelerometer" }).then((result) => {
  if (result.state === "denied") {
    console.log("Permission to use accelerometer sensor is denied.");
    return;
  }
  // Use the sensor.
});
```

An alternative approach is to attempt to use the sensor and listen for the `SecurityError`.

js

```
const sensor = new AbsoluteOrientationSensor();
sensor.start();
sensor.addEventListener("error", (error) => {
  if (event.error.name === "SecurityError")
    console.log("No permissions to use AbsoluteOrientationSensor.");
});
```

The following table describes for each sensor type, the name required for the Permissions API, the [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe) element's `allow` attribute and the [Permissions-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy) directive.

SensorPermission Policy Name`AbsoluteOrientationSensor``'accelerometer'`, `'gyroscope'`, and `'magnetometer'``Accelerometer``'accelerometer'``AmbientLightSensor``'ambient-light-sensor'``GravitySensor``'accelerometer'``Gyroscope``'gyroscope'``LinearAccelerationSensor``'accelerometer'``Magnetometer``'magnetometer'``RelativeOrientationSensor``'accelerometer'`, and `'gyroscope'`

### [Readings](#readings)

Sensor readings are received through the [reading](/en-US/docs/Web/API/Sensor/reading_event) event callback which is inherited by all sensor types. Reading frequency is decided by you, accomplished with an option passed to a sensor's constructor. The option is a number that specifies the number of readings per second. A whole number or decimal may be used, the latter for frequencies less than a second. The actual reading frequency depends on device hardware and consequently may be less than requested.

The following example illustrates this using the [Magnetometer](/en-US/docs/Web/API/Magnetometer) sensor.

js

```
let magSensor = new Magnetometer({ frequency: 60 });

magSensor.addEventListener("reading", (e) => {
  console.log(`Magnetic field along the X-axis ${magSensor.x}`);
  console.log(`Magnetic field along the Y-axis ${magSensor.y}`);
  console.log(`Magnetic field along the Z-axis ${magSensor.z}`);
});
magSensor.addEventListener("error", (event) => {
  console.log(event.error.name, event.error.message);
});
magSensor.start();
```

## [Interfaces](#interfaces)

[AbsoluteOrientationSensor](/en-US/docs/Web/API/AbsoluteOrientationSensor)

Describes the device's physical orientation in relation to the Earth's reference coordinate system.

[Accelerometer](/en-US/docs/Web/API/Accelerometer)

Provides the acceleration applied to the device along all three axes.

[AmbientLightSensor](/en-US/docs/Web/API/AmbientLightSensor)

Returns the current light level or illuminance of the ambient light around the hosting device.

[GravitySensor](/en-US/docs/Web/API/GravitySensor)

Provides the gravity applied to the device along all three axes.

[Gyroscope](/en-US/docs/Web/API/Gyroscope)

Provides the angular velocity of the device along all three axes.

[LinearAccelerationSensor](/en-US/docs/Web/API/LinearAccelerationSensor)

Provides the acceleration applied to the device along all three axes, but without the contribution of gravity.

[Magnetometer](/en-US/docs/Web/API/Magnetometer)

Provides information about the magnetic field as detected by the device's primary magnetometer sensor.

[OrientationSensor](/en-US/docs/Web/API/OrientationSensor)

The base class for the [AbsoluteOrientationSensor](/en-US/docs/Web/API/AbsoluteOrientationSensor). This interface cannot be used directly, instead it provides properties and methods accessed by interfaces that inherit from it.

[RelativeOrientationSensor](/en-US/docs/Web/API/RelativeOrientationSensor)

Describes the device's physical orientation without regard to the Earth's reference coordinate system.

[Sensor](/en-US/docs/Web/API/Sensor)

The base class for all the other sensor interfaces. This interface cannot be used directly. Instead, it provides properties, event handlers, and methods accessed by interfaces that inherit from it.

[SensorErrorEvent](/en-US/docs/Web/API/SensorErrorEvent)

Provides information about errors thrown by a [Sensor](/en-US/docs/Web/API/Sensor) or related interface.

## [Specifications](#specifications)

Specification[Generic Sensor API](https://w3c.github.io/sensors/)[Accelerometer](https://w3c.github.io/accelerometer/)[Orientation Sensor](https://w3c.github.io/orientation-sensor/)[Ambient Light Sensor](https://w3c.github.io/ambient-light/)[Gyroscope](https://w3c.github.io/gyroscope/)[Magnetometer](https://w3c.github.io/magnetometer/)

## [Browser compatibility](#browser_compatibility)

### [api.Sensor](#api.Sensor)

### [api.Accelerometer](#api.Accelerometer)

### [api.OrientationSensor](#api.OrientationSensor)

### [api.Gyroscope](#api.Gyroscope)

### [api.Magnetometer](#api.Magnetometer)

### [api.AmbientLightSensor](#api.AmbientLightSensor)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Sensor_APIs/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/sensor_apis/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSensor_APIs&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsensor_apis%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSensor_APIs%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsensor_apis%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4d929bb0a021c7130d5a71a4bf505bcb8070378d%0A*+Document+last+modified%3A+2025-03-13T12%3A48%3A23.000Z%0A%0A%3C%2Fdetails%3E)
