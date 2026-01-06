# NavigatorUAData

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigatorUAData&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `NavigatorUAData` interface of the [User-Agent Client Hints API](/en-US/docs/Web/API/User-Agent_Client_Hints_API) returns information about the browser and operating system of a user.

An instance of this object is returned by calling [Navigator.userAgentData](/en-US/docs/Web/API/Navigator/userAgentData) or [WorkerNavigator.userAgentData](/en-US/docs/Web/API/WorkerNavigator/userAgentData). Therefore, this interface has no constructor.

Note: The terms high entropy and low entropy refer to the amount of information these values reveal about the browser. The values returned as properties are deemed low entropy, and unlikely to identify a user. The values returned by [NavigatorUAData.getHighEntropyValues()](/en-US/docs/Web/API/NavigatorUAData/getHighEntropyValues) could potentially reveal more information. These values are therefore retrieved via a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), allowing time for the browser to request user permission, or make other checks.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[NavigatorUAData.brands](/en-US/docs/Web/API/NavigatorUAData/brands)Read onlyExperimental

Returns an array of brand information containing the browser name and version.

[NavigatorUAData.mobile](/en-US/docs/Web/API/NavigatorUAData/mobile)Read onlyExperimental

Returns `true` if the user-agent is running on a mobile device.

[NavigatorUAData.platform](/en-US/docs/Web/API/NavigatorUAData/platform)Read onlyExperimental

Returns the platform brand the user-agent is running on.

## [Instance methods](#instance_methods)

[NavigatorUAData.getHighEntropyValues()](/en-US/docs/Web/API/NavigatorUAData/getHighEntropyValues)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with a dictionary object containing the high entropy values the user-agent returns.

[NavigatorUAData.toJSON()](/en-US/docs/Web/API/NavigatorUAData/toJSON)Experimental

A serializer that returns a JSON representation of the low entropy properties of the `NavigatorUAData` object.

## [Examples](#examples)

### [Getting the brands](#getting_the_brands)

The following example prints the value of [NavigatorUAData.brands](/en-US/docs/Web/API/NavigatorUAData/brands) to the console.

js

```
console.log(navigator.userAgentData.brands);
```

### [Returning high entropy values](#returning_high_entropy_values)

In the following value a number of hints are requested using the [NavigatorUAData.getHighEntropyValues()](/en-US/docs/Web/API/NavigatorUAData/getHighEntropyValues) method. When the promise resolves, this information is printed to the console.

js

```
navigator.userAgentData
  .getHighEntropyValues([
    "architecture",
    "model",
    "platform",
    "platformVersion",
    "fullVersionList",
  ])
  .then((ua) => {
    console.log(ua);
  });
```

## [Specifications](#specifications)

Specification
[User-Agent Client Hints# navigatoruadata](https://wicg.github.io/ua-client-hints/#navigatoruadata)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Improving user privacy and developer experience with User-Agent Client Hints](https://developer.chrome.com/docs/privacy-security/user-agent-client-hints)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/NavigatorUAData/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/navigatoruadata/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigatorUAData&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fnavigatoruadata%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigatorUAData%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fnavigatoruadata%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcfb7587e3e3122630ad6cbd94d834ecadbe0a746%0A*+Document+last+modified%3A+2024-07-26T03%3A44%3A38.000Z%0A%0A%3C%2Fdetails%3E)
