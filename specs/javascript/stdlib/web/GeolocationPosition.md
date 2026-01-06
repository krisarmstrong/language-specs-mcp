# GeolocationPosition

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGeolocationPosition&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `GeolocationPosition` interface represents the position of the concerned device at a given time. The position, represented by a [GeolocationCoordinates](/en-US/docs/Web/API/GeolocationCoordinates) object, comprehends the 2D position of the device, on a spheroid representing the Earth, but also its altitude and its speed.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

The `GeolocationPosition` interface doesn't inherit any properties.

[GeolocationPosition.coords](/en-US/docs/Web/API/GeolocationPosition/coords)Read only

Returns a [GeolocationCoordinates](/en-US/docs/Web/API/GeolocationCoordinates) object defining the current location.

[GeolocationPosition.timestamp](/en-US/docs/Web/API/GeolocationPosition/timestamp)Read only

Returns a timestamp, given as [Unix time](/en-US/docs/Glossary/Unix_time) in milliseconds, representing the time at which the location was retrieved.

## [Instance methods](#instance_methods)

The `GeolocationPosition` interface doesn't inherit any methods.

[GeolocationPosition.toJSON()](/en-US/docs/Web/API/GeolocationPosition/toJSON)

Returns a JSON representation of the `GeolocationPosition` object and enables serialization with [JSON.stringify()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify).

## [Specifications](#specifications)

Specification
[Geolocation# position_interface](https://w3c.github.io/geolocation/#position_interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Geolocation API](/en-US/docs/Web/API/Geolocation_API/Using_the_Geolocation_API)
- [Geolocation](/en-US/docs/Web/API/Geolocation)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 19, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/GeolocationPosition/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/geolocationposition/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGeolocationPosition&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgeolocationposition%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGeolocationPosition%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgeolocationposition%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4558d208395a5b1df4db44b0c8ef4e9a0f8adbbf%0A*+Document+last+modified%3A+2024-06-19T05%3A39%3A51.000Z%0A%0A%3C%2Fdetails%3E)
