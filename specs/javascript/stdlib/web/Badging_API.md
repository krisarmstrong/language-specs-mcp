# Badging API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBadging_API&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The Badging API gives web developers a method of setting a badge on a document or application, to act as a notification that state has changed without displaying a more distracting notification. A common use case for this would be an application with a messaging feature displaying a badge on the app icon to show that new messages have arrived.

## In this article

- [Concepts and Usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and Usage](#concepts_and_usage)

Web developers frequently update document favicons or titles in order to indicate status. The Badging API provides a more elegant way to show status, by providing a method which has meaning to the user agent and can therefore be displayed in a way that matches the rest of the UI.

### [Types of badges](#types_of_badges)

There are two types of badges:

- Document badges, which are typically shown in the browser tab near or on the page icon.
- App badges, which are associated with the icon of an installed web app. These may display on the app icon in the dock, shelf, or home screen depending on the device in use.

### [Badge states](#badge_states)

A badge can have one of three possible values, which are set internally:

[nothing](#nothing)

Indicating that no badge is currently set. A badge can be in this state due to it being cleared by the application, or being reset by the user agent.

[flag](#flag)

Indicating that the badge is set, but has no specific data to display. A badge will be in this state if the application has set a badge, but has not passed any value to the method.

[an integer](#an_integer)

A value passed when setting the badge. This value will never be `0`, passing a value of `0` when setting a badge will cause the user agent to clear the badge by setting it to `nothing`.

### [Setting badges](#setting_badges)

A badge is set with the methods `setAppBadge()` (for installed apps). If no parameters are passed to these methods then the badge value is flag. The user agent will display its notification badge, for example, a colored circle on the icon.

These methods can also be passed a parameter `contents`, which should be a number. This will then be displayed as part of the badge. User agents may change this value in some way. For example, if you pass a very large number such as 4000, the user agent may display this as 99+ in the badge. User agents may also ignore this data and display a marker instead.

### [Clearing badges](#clearing_badges)

Badges are cleared with the `clearAppBadge()` methods. These do not take any parameters and set the badge to the value `nothing`. Additionally, passing a value of `0` to `setAppBadge()` will set the badge to `nothing` and clear the badge.

## [Interfaces](#interfaces)

None.

### [Extensions to the Navigator interface](#extensions_to_the_navigator_interface)

[Navigator.setAppBadge()](/en-US/docs/Web/API/Navigator/setAppBadge)

Sets a badge on the icon associated with this app.

[Navigator.clearAppBadge()](/en-US/docs/Web/API/Navigator/clearAppBadge)

Clears the badge on the icon associated with this app.

### [Extensions to the WorkerNavigator interface](#extensions_to_the_workernavigator_interface)

[WorkerNavigator.setAppBadge()](/en-US/docs/Web/API/WorkerNavigator/setAppBadge)

Sets a badge on the icon associated with this app.

[WorkerNavigator.clearAppBadge()](/en-US/docs/Web/API/WorkerNavigator/clearAppBadge)

Clears the badge on the icon associated with this app.

## [Examples](#examples)

To set a notification badge on the current app with a value of 12:

js

```
navigator.setAppBadge(12);
```

To clear a notification badge on the current app:

js

```
navigator.clearAppBadge();
```

## [Specifications](#specifications)

Specification
[Badging API# setappbadge-method](https://w3c.github.io/badging/#setappbadge-method)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Badging for app icons](https://developer.chrome.com/docs/capabilities/web-apis/badging-api)
- [Badging API Explainer](https://github.com/w3c/badging/blob/main/explainer.md)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 25, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Badging_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/badging_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBadging_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbadging_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBadging_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbadging_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4675b9077ae32f989c7ecac94f454db2653c4fc%0A*+Document+last+modified%3A+2024-07-25T22%3A06%3A52.000Z%0A%0A%3C%2Fdetails%3E)
