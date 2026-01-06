# UserActivation

 Baseline  2023 Newly available

 Since ⁨November 2023⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUserActivation&level=low)

The `UserActivation` interface provides information about whether a user is currently interacting with the page, or has completed an interaction since page load.

This API is only available in the window context and not exposed to workers.

## In this article

- [Instance properties](#instance_properties)
- [Description](#description)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[UserActivation.hasBeenActive](/en-US/docs/Web/API/UserActivation/hasBeenActive)Read only

Indicates whether the current window has sticky user activation.

[UserActivation.isActive](/en-US/docs/Web/API/UserActivation/isActive)Read only

Indicates whether the current window has transient user activation.

## [Description](#description)

An object of this type is accessed via the [navigator.userActivation](/en-US/docs/Web/API/Navigator/userActivation) property, and can be used to query information about a window's user activation state.

A user activation either implies that the user is currently interacting with the page, or has completed an interaction since page load. User activation can be triggered by a button click, pointer touch, or some other user interaction with the page.

There are two kinds of window user activation states:

- [Transient activation](/en-US/docs/Glossary/Transient_activation) (user is currently interacting with the page) and
- [Sticky activation](/en-US/docs/Glossary/Sticky_activation) (user has interacted at least once since page load).

See [Features gated by user activation](/en-US/docs/Web/Security/Defenses/User_activation) for more information and a list of APIs that require either sticky or transient user activation.

## [Examples](#examples)

### [Checking if a user gesture was recently performed](#checking_if_a_user_gesture_was_recently_performed)

Use [navigator.userActivation](/en-US/docs/Web/API/Navigator/userActivation) to access the `UserActivation` object, and then [UserActivation.isActive](/en-US/docs/Web/API/UserActivation/isActive) to check whether the user is currently interacting with the page ([Transient activation](/en-US/docs/Glossary/Transient_activation)).

js

```
if (navigator.userActivation.isActive) {
  // proceed to request playing media, for example
}
```

### [Checking if a user gesture was ever performed](#checking_if_a_user_gesture_was_ever_performed)

Use [UserActivation.hasBeenActive](/en-US/docs/Web/API/UserActivation/hasBeenActive) to check whether the user has ever interacted with the page ([Sticky activation](/en-US/docs/Glossary/Sticky_activation)).

js

```
if (navigator.userActivation.hasBeenActive) {
  // proceed with auto-playing an animation, for example
}
```

## [Specifications](#specifications)

Specification
[HTML# the-useractivation-interface](https://html.spec.whatwg.org/multipage/interaction.html#the-useractivation-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [navigator.userActivation](/en-US/docs/Web/API/Navigator/userActivation)
- [Features gated by user activation](/en-US/docs/Web/Security/Defenses/User_activation)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/UserActivation/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/useractivation/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUserActivation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fuseractivation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUserActivation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fuseractivation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca26363fcc6fc861103d40ac0205e5c5b79eb2fa%0A*+Document+last+modified%3A+2025-11-30T02%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
