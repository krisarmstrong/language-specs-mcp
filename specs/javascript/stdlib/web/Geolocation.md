# Geolocation

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGeolocation&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `Geolocation` interface represents an object able to obtain the position of the device programmatically. It gives Web content access to the location of the device. This allows a website or app to offer customized results based on the user's location.

An object with this interface is obtained using the [navigator.geolocation](/en-US/docs/Web/API/Navigator/geolocation) property implemented by the [Navigator](/en-US/docs/Web/API/Navigator) object.

Note: For security reasons, when a web page tries to access location information, the user is notified and asked to grant permission. Be aware that each browser has its own policies and methods for requesting this permission.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

The `Geolocation` interface neither implements, nor inherits any property.

## [Instance methods](#instance_methods)

The `Geolocation` interface doesn't inherit any method.

[Geolocation.getCurrentPosition()](/en-US/docs/Web/API/Geolocation/getCurrentPosition)

Determines the device's current location and gives back a [GeolocationPosition](/en-US/docs/Web/API/GeolocationPosition) object with the data.

[Geolocation.watchPosition()](/en-US/docs/Web/API/Geolocation/watchPosition)

Returns a `long` value representing the newly established callback function to be invoked whenever the device location changes.

[Geolocation.clearWatch()](/en-US/docs/Web/API/Geolocation/clearWatch)

Removes the particular handler previously installed using `watchPosition()`.

## [Specifications](#specifications)

Specification
[Geolocation# geolocation_interface](https://w3c.github.io/geolocation/#geolocation_interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using geolocation](/en-US/docs/Web/API/Geolocation_API/Using_the_Geolocation_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Geolocation/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/geolocation/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGeolocation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgeolocation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGeolocation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgeolocation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd8f04d843dd81ab8cea1cfc0577ae3c5c9b77d5c%0A*+Document+last+modified%3A+2024-07-26T03%3A29%3A50.000Z%0A%0A%3C%2Fdetails%3E)
