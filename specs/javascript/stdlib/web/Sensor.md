# Sensor

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSensor&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `Sensor` interface of the [Sensor APIs](/en-US/docs/Web/API/Sensor_APIs) is the base class for all the other sensor interfaces. This interface cannot be used directly. Instead it provides properties, event handlers, and methods accessed by interfaces that inherit from it.

This feature may be blocked by a [Permissions Policy](/en-US/docs/Web/HTTP/Guides/Permissions_Policy) set on your server.

When initially created, the `Sensor` object is idle, meaning it does not take measures. Once the [start()](/en-US/docs/Web/API/Sensor/start) method is called, it prepares itself to read data and, once ready, the [activate](/en-US/docs/Web/API/Sensor/activate_event) event is sent and the sensor becomes activated. It then sends a [reading](/en-US/docs/Web/API/Sensor/reading_event) event each time new data is available.

In case of an error, the [error](/en-US/docs/Web/API/Sensor/error_event) event is sent, reading stops, and the `Sensor` object becomes idle again. The [start()](/en-US/docs/Web/API/Sensor/start) method needs to be called again before it can read further data.

## In this article

- [Interfaces based on Sensor](#interfaces_based_on_sensor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Interfaces based on Sensor](#interfaces_based_on_sensor)

Below is a list of interfaces based on the `Sensor` interface.

- [Accelerometer](/en-US/docs/Web/API/Accelerometer)
- [AmbientLightSensor](/en-US/docs/Web/API/AmbientLightSensor)
- [GravitySensor](/en-US/docs/Web/API/GravitySensor)
- [Gyroscope](/en-US/docs/Web/API/Gyroscope)
- [LinearAccelerationSensor](/en-US/docs/Web/API/LinearAccelerationSensor)
- [Magnetometer](/en-US/docs/Web/API/Magnetometer)
- [OrientationSensor](/en-US/docs/Web/API/OrientationSensor)

## [Instance properties](#instance_properties)

[Sensor.activated](/en-US/docs/Web/API/Sensor/activated)Read only

Returns a boolean value indicating whether the sensor is active.

[Sensor.hasReading](/en-US/docs/Web/API/Sensor/hasReading)Read only

Returns a boolean value indicating whether the sensor has a reading.

[Sensor.timestamp](/en-US/docs/Web/API/Sensor/timestamp)Read only

Returns the timestamp of the latest sensor reading.

## [Instance methods](#instance_methods)

[Sensor.start()](/en-US/docs/Web/API/Sensor/start)

Activates one of the sensors based on `Sensor`.

[Sensor.stop()](/en-US/docs/Web/API/Sensor/stop)

Deactivates one of the sensors based on `Sensor`.

## [Events](#events)

[activate](/en-US/docs/Web/API/Sensor/activate_event)

Fired when a sensor becomes activated.

[error](/en-US/docs/Web/API/Sensor/error_event)

Fired when an exception occurs on a sensor.

[reading](/en-US/docs/Web/API/Sensor/reading_event)

Fired when a new reading is available on a sensor.

## [Specifications](#specifications)

Specification
[Generic Sensor API# the-sensor-interface](https://w3c.github.io/sensors/#the-sensor-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Sensor/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/sensor/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSensor&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsensor%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSensor%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsensor%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4d929bb0a021c7130d5a71a4bf505bcb8070378d%0A*+Document+last+modified%3A+2025-03-13T12%3A48%3A23.000Z%0A%0A%3C%2Fdetails%3E)
