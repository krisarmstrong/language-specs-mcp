# NavigatorLogin

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `NavigatorLogin` interface of the [Federated Credential Management (FedCM) API](/en-US/docs/Web/API/FedCM_API) defines login functionality for federated identity providers (IdPs). Specifically, it enables a federated identity provider (IdP) to set its login status when a user signs into or out of the IdP.

See [Update login status using the Login Status API](/en-US/docs/Web/API/FedCM_API/IDP_integration#update_login_status_using_the_login_status_api) for more details of how this is used.

`NavigatorLogin` is accessed via the [Navigator.login](/en-US/docs/Web/API/Navigator/login) property.

## In this article

- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

[setStatus()](/en-US/docs/Web/API/NavigatorLogin/setStatus)

Sets the login status of a federated identity provider (IdP), when called from the IdP's origin. By "login status", we mean "whether any users are logged into the IdP on the current browser or not".

## [Examples](#examples)

js

```
/* Set logged-in status */
navigator.login.setStatus("logged-in");

/* Set logged-out status */
navigator.login.setStatus("logged-out");
```

## [Specifications](#specifications)

Specification
[Login Status API# navigatorlogin](https://w3c-fedid.github.io/login-status/#navigatorlogin)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Federated Credential Management (FedCM) API](/en-US/docs/Web/API/FedCM_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/NavigatorLogin/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/navigatorlogin/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigatorLogin&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fnavigatorlogin%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigatorLogin%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fnavigatorlogin%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F43f272adb6ac15537cff3728c78ddf234485fff8%0A*+Document+last+modified%3A+2025-04-03T04%3A28%3A47.000Z%0A%0A%3C%2Fdetails%3E)
