# EyeDropper API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEyeDropper_API&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The EyeDropper API provides a mechanism for creating an eyedropper tool. Using this tool, users can sample colors from their screens, including outside of the browser window.

## In this article

- [Concept](#concept)
- [Security and privacy measures](#security_and_privacy_measures)
- [Interfaces](#interfaces)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concept](#concept)

Creative applications often allow users to sample colors from drawings or shapes in the application to reuse. Web applications can use the EyeDropper API to provide a similar eyedropper mode, provided by the browser.

Using the API, a web application can start the eyedropper mode. Once started, the cursor changes to indicate to the user that the mode is active. The user can then either select a color from anywhere on the screen, or dismiss the eyedropper mode by pressing Escape.

## [Security and privacy measures](#security_and_privacy_measures)

To prevent malicious websites from getting pixel data from a user's screen without them realizing, the EyeDropper API implements the following measures:

- The API doesn't let the eyedropper mode start without user intent. The [EyeDropper.open()](/en-US/docs/Web/API/EyeDropper/open) method can only be called in response to a user action (such as a button click).
- No pixel information can be retrieved without user intent. The promise returned by [EyeDropper.open()](/en-US/docs/Web/API/EyeDropper/open) only resolves to a color value in response to a user action (clicking on a pixel). So the eyedropper cannot be used in the background without the user noticing it.
- To help users notice the eyedropper mode more easily, it is made obvious by browsers. The normal mouse cursor disappears after a short delay and a magnifying glass appears instead. There is also a delay between when the eyedropper mode starts and when the user can select a pixel to ensure the user has had time to see the magnifying glass.
- Users are also able to cancel the eyedropper mode at any time (by pressing the Escape key).

## [Interfaces](#interfaces)

[EyeDropper](/en-US/docs/Web/API/EyeDropper)Experimental

The `EyeDropper` interface represents an instance of an eyedropper tool that can be opened and used by the user to select colors from the screen.

## [Specifications](#specifications)

Specification
[EyeDropper API# eyedropper-interface](https://wicg.github.io/eyedropper-api/#eyedropper-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Picking colors of any pixel on the screen with the EyeDropper API](https://developer.chrome.com/docs/capabilities/web-apis/eyedropper)
- [The EyeDropper API W3C/SMPTE Joint Workshop](https://www.w3.org/2021/03/media-production-workshop/talks/patrick-brosset-eyedropper-api.html)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/EyeDropper_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/eyedropper_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEyeDropper_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Feyedropper_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEyeDropper_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Feyedropper_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
