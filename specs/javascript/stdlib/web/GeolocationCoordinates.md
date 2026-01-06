# GeolocationCoordinates

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGeolocationCoordinates&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `GeolocationCoordinates` interface represents the position and altitude of the device on Earth, as well as the accuracy with which these properties are calculated. The geographic position information is provided in terms of World Geodetic System coordinates (WGS84).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

The `GeolocationCoordinates` interface doesn't inherit any properties.

[GeolocationCoordinates.latitude](/en-US/docs/Web/API/GeolocationCoordinates/latitude)Read only

Returns a `double` representing the position's latitude in decimal degrees.

[GeolocationCoordinates.longitude](/en-US/docs/Web/API/GeolocationCoordinates/longitude)Read only

Returns a `double` representing the position's longitude in decimal degrees.

[GeolocationCoordinates.altitude](/en-US/docs/Web/API/GeolocationCoordinates/altitude)Read only

Returns a `double` representing the position's altitude in meters, relative to nominal sea level. This value can be `null` if the implementation cannot provide the data.

[GeolocationCoordinates.accuracy](/en-US/docs/Web/API/GeolocationCoordinates/accuracy)Read only

Returns a `double` representing the accuracy of the `latitude` and `longitude` properties, expressed in meters.

[GeolocationCoordinates.altitudeAccuracy](/en-US/docs/Web/API/GeolocationCoordinates/altitudeAccuracy)Read only

Returns a `double` representing the accuracy of the `altitude` expressed in meters. This value can be `null` if the implementation cannot provide the data.

[GeolocationCoordinates.heading](/en-US/docs/Web/API/GeolocationCoordinates/heading)Read only

Returns a `double` representing the direction towards which the device is facing. This value, specified in degrees, indicates how far off from heading true north the device is. `0` degrees represents true north, and the direction is determined clockwise (which means that east is `90` degrees and west is `270` degrees). If `speed` is `0` or the device is unable to provide `heading` information, `heading` is `null`.

[GeolocationCoordinates.speed](/en-US/docs/Web/API/GeolocationCoordinates/speed)Read only

Returns a `double` representing the velocity of the device in meters per second. This value can be `null`.

## [Instance methods](#instance_methods)

The `GeolocationCoordinates` interface doesn't inherit any methods.

[GeolocationCoordinates.toJSON()](/en-US/docs/Web/API/GeolocationCoordinates/toJSON)

Returns a JSON representation of the `GeolocationCoordinates` object and enables serialization with [JSON.stringify()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify).

## [Specifications](#specifications)

Specification
[Geolocation# coordinates_interface](https://w3c.github.io/geolocation/#coordinates_interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Geolocation API](/en-US/docs/Web/API/Geolocation_API/Using_the_Geolocation_API)
- [Geolocation](/en-US/docs/Web/API/Geolocation)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 24, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/GeolocationCoordinates/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/geolocationcoordinates/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGeolocationCoordinates&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgeolocationcoordinates%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGeolocationCoordinates%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgeolocationcoordinates%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F68c5b12ed1e9a55b86cd32e242216f1b88a8ccc7%0A*+Document+last+modified%3A+2024-08-24T02%3A27%3A51.000Z%0A%0A%3C%2Fdetails%3E)
