# GeolocationPositionError

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2020⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGeolocationPositionError&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `GeolocationPositionError` interface represents the reason of an error occurring when using the geolocating device.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

The `GeolocationPositionError` interface doesn't inherit any property.

[GeolocationPositionError.code](/en-US/docs/Web/API/GeolocationPositionError/code)Read only

Returns an `unsigned short` representing the error code. The following values are possible:

ValueAssociated constantDescription`1``PERMISSION_DENIED`The acquisition of the geolocation information failed because the page didn't have the necessary permissions, for example because it is blocked by a [Permissions Policy](/en-US/docs/Web/HTTP/Guides/Permissions_Policy)`2``POSITION_UNAVAILABLE`The acquisition of the geolocation failed because at least one internal source of position returned an internal error.`3``TIMEOUT`The time allowed to acquire the geolocation was reached before the information was obtained.[GeolocationPositionError.message](/en-US/docs/Web/API/GeolocationPositionError/message)Read only

Returns a human-readable string describing the details of the error. Specifications note that this is primarily intended for debugging use and not to be shown directly in a user interface.

## [Instance methods](#instance_methods)

The `GeolocationPositionError` interface neither implements nor inherits any method.

## [Specifications](#specifications)

Specification
[Geolocation# position_error_interface](https://w3c.github.io/geolocation/#position_error_interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Geolocation API](/en-US/docs/Web/API/Geolocation_API/Using_the_Geolocation_API)
- [Geolocation](/en-US/docs/Web/API/Geolocation)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GeolocationPositionError/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/geolocationpositionerror/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGeolocationPositionError&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgeolocationpositionerror%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGeolocationPositionError%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgeolocationpositionerror%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
