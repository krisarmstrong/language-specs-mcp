# IdentityProvider

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `IdentityProvider` interface of the [Federated Credential Management (FedCM) API](/en-US/docs/Web/API/FedCM_API) represents an [IdP](/en-US/docs/Glossary/Identity_provider) and provides access to related information and functionality.

## In this article

- [Static methods](#static_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Static methods](#static_methods)

[close()](/en-US/docs/Web/API/IdentityProvider/close_static)Experimental

Provides a manual signal to the browser that an IdP sign-in flow is finished. This is needed to, for example, close the IdP sign-in dialog when sign-in is completely finished and the IdP has finished collecting data from the user.

[getUserInfo()](/en-US/docs/Web/API/IdentityProvider/getUserInfo_static)Experimental

Returns information about a previously-signed in user on their return to an IdP, which can be used to provide a personalized welcome message and sign-in button.

## [Examples](#examples)

### [Basic IdentityProvider.getUserInfo() usage](#basic_identityprovider.getuserinfo_usage)

The following example shows how the [getUserInfo()](/en-US/docs/Web/API/IdentityProvider/getUserInfo_static) method can be used to return information on a previously-signed in user from a specific IdP.

js

```
// Iframe displaying a page from the https://idp.example origin
const userInfo = await IdentityProvider.getUserInfo({
  configURL: "https://idp.example/fedcm.json",
  clientId: "client1234",
});

// IdentityProvider.getUserInfo() returns an array of user information.
if (userInfo.length > 0) {
  // Returning accounts should be first, so the first account received
  // is guaranteed to be a returning account
  const name = userInfo[0].name;
  const givenName = userInfo[0].given_name;
  const displayName = givenName || name;
  const picture = userInfo[0].picture;
  const email = userInfo[0].email;

  // …

  // Render a personalized sign-in button using the information returned above
}
```

## [Specifications](#specifications)

Specification
[Federated Credential Management API# browser-api-identity-provider-interface](https://w3c-fedid.github.io/FedCM/#browser-api-identity-provider-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Federated Credential Management API](https://developer.chrome.com/docs/identity/fedcm/overview) on developer.chrome.com (2023)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/IdentityProvider/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/identityprovider/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIdentityProvider&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fidentityprovider%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIdentityProvider%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fidentityprovider%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6722199b4d63fad3c33db1146af380fc98b6c202%0A*+Document+last+modified%3A+2025-10-27T09%3A17%3A57.000Z%0A%0A%3C%2Fdetails%3E)
