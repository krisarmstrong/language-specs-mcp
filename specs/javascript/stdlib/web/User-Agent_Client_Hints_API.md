# User-Agent Client Hints API

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The User-Agent Client Hints API extends [Client Hints](/en-US/docs/Web/HTTP/Guides/Client_hints) to provide a way of exposing browser and platform information via User-Agent response and request headers, and a JavaScript API.

## In this article

- [Concepts and Usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and Usage](#concepts_and_usage)

Parsing the User-Agent string has historically been the way to get information about the user's browser or device. A typical user agent string looks like the following example, identifying Chrome 92 on Windows:

```
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36
```

User agent Client Hints aims to provide this information in a more privacy-preserving way by enforcing a model where the server requests a set of information. The browser decides what to return. This approach means that a user-agent could provide settings that allow a user to hide some of the information that could fingerprint them from such requests.

In order to decide what to return, the information accessed via this API is split into two groups—low entropy and high entropy hints. Low entropy hints are those that do not give away much information, the API makes these easily accessible with every request. High entropy hints have the potential to give away more information and therefore are gated in such a way that the browser can make a decision as to whether to provide them. This decision could potentially be based on user preferences, or behind a permission request.

### [Use cases for User-Agent Client Hints](#use_cases_for_user-agent_client_hints)

Potential use cases include:

- Providing custom-tailored polyfills to users on identifying that their browser lacked some web platform feature.
- Working around browser bugs.
- Recording browser analytics.
- Adapting content based on user-agent information. This includes serving different content to mobile devices, in particular devices identified as low-powered. It might also include adapting the design to tailor the interfaces to the user's OS, or providing links to OS-specific ones.
- Providing a notification when a user logs in from a different browser or device, as a security feature.
- Providing the correct binary executable, on a site offering a download.
- Collecting information about the browser and device to identify application errors.
- Blocking spammers, bots, and crawlers.

## [Interfaces](#interfaces)

[NavigatorUAData](/en-US/docs/Web/API/NavigatorUAData)

Provides properties and methods to access data about the user's browser and operating system.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[Navigator.userAgentData](/en-US/docs/Web/API/Navigator/userAgentData)Read only

Returns a [NavigatorUAData](/en-US/docs/Web/API/NavigatorUAData) object, which gives access to information about the browser and operating system of the user.

[WorkerNavigator.userAgentData](/en-US/docs/Web/API/WorkerNavigator/userAgentData)Read only

Returns a [NavigatorUAData](/en-US/docs/Web/API/NavigatorUAData) object, which gives access to information about the browser and operating system of the user.

## [Examples](#examples)

### [Getting the brands](#getting_the_brands)

The following example prints the value of [NavigatorUAData.brands](/en-US/docs/Web/API/NavigatorUAData/brands) to the console.

js

```
console.log(navigator.userAgentData.brands);
```

### [Returning high entropy values](#returning_high_entropy_values)

In the following example a number of hints are requested using the [NavigatorUAData.getHighEntropyValues()](/en-US/docs/Web/API/NavigatorUAData/getHighEntropyValues) method. When the promise resolves, this information is printed to the console.

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

Specification[User-Agent Client Hints](https://wicg.github.io/ua-client-hints/)

## [Browser compatibility](#browser_compatibility)

### [api.NavigatorUAData](#api.NavigatorUAData)

### [api.Navigator.userAgentData](#api.Navigator.userAgentData)

### [api.WorkerNavigator.userAgentData](#api.WorkerNavigator.userAgentData)

## [See also](#see_also)

- [Improving user privacy and developer experience with User-Agent Client Hints](https://developer.chrome.com/docs/privacy-security/user-agent-client-hints)
- [Migrate to User-Agent Client Hints](https://web.dev/articles/migrate-to-ua-ch)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/User-Agent_Client_Hints_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/user-agent_client_hints_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUser-Agent_Client_Hints_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fuser-agent_client_hints_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUser-Agent_Client_Hints_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fuser-agent_client_hints_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4d929bb0a021c7130d5a71a4bf505bcb8070378d%0A*+Document+last+modified%3A+2025-03-13T12%3A48%3A23.000Z%0A%0A%3C%2Fdetails%3E)
