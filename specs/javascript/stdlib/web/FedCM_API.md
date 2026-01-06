# Federated Credential Management (FedCM) API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFedCM_API&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The Federated Credential Management API (or FedCM API) provides a standard mechanism for [identity providers](/en-US/docs/Glossary/Identity_provider) (IdPs) to make identity federation services available on the web in a privacy-preserving way, without the need for [third-party cookies](/en-US/docs/Web/Privacy/Guides/Third-party_cookies) and redirects. This includes a JavaScript API that enables the use of federated authentication for activities such as signing in or signing up on a website.

## In this article

- [FedCM concepts](#fedcm_concepts)
- [Permissions Policy integration and <iframe> support](#permissions_policy_integration_and_iframe_support)
- [Interfaces](#interfaces)
- [Extensions to other interfaces](#extensions_to_other_interfaces)
- [HTTP headers](#http_headers)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [FedCM concepts](#fedcm_concepts)

Identity federation is the delegation of user authentication from a website requiring user sign-up or sign-in, such as an e-commerce or social networking site (also known as a [relying party](/en-US/docs/Glossary/Relying_party) or RP), to a trusted third-party identity provider (IdP) such as Google, Facebook/Meta, GitHub, etc.

RPs can integrate with IdPs, allowing users to sign-in using the accounts they have registered with the IdP. Identity federation via a small set of dedicated IdPs has improved web authentication in terms of security, consumer confidence, and user experience, as compared to each site managing its own sign-in needs with separate usernames and passwords.

The problem is that traditional identity federation relies on [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe)s, redirects, and third-party cookies, which are also used for third-party tracking. Browsers are limiting the usage of these features in an effort to preserve user privacy, but a side effect is that this makes valid, non-tracking uses more difficult to implement, which includes identity federation.

This affects federated sign-in in general, as well as more specific identity federation use cases:

- [OIDC front-channel logout](https://openid.net/specs/openid-connect-frontchannel-1_0.html): This flow requires the IDP to embed several RP `<iframe>`s, which rely on RP cookies.
- Social Widgets: In order to provide social widgets, the IdP third-party cookie must be provided from the RP top-level origin.
- Personalized buttons: The display of personalized sign in information on a [<button>](/en-US/docs/Web/HTML/Reference/Elements/button) in the RP origin is implemented as an IdP `<iframe>` that requires third party cookies.
- Session Refresh without top-level navigation or popups.

FedCM aims to work around this problem, providing a dedicated mechanism for federated identity flows on the web, and enabling supporting browsers to provide special UI elements on RPs, allowing users to choose an IdP account to use for sign-in.

There are two parts to using the FedCM API, which are covered in the linked guides below:

1. [IdP integration with FedCM](/en-US/docs/Web/API/FedCM_API/IDP_integration) — what an identity provider needs to provide so that an RP can integrate with it.
2. [RP federated sign-in](/en-US/docs/Web/API/FedCM_API/RP_sign-in) — the FedCM functionality an RP needs to use to sign a user in using their IdP account. A FedCM sign-in request is initiated using the [navigator.credentials.get()](/en-US/docs/Web/API/CredentialsContainer/get) method.

Note:[Google Sign In](https://developers.google.com/identity/gsi/web/guides/overview) is an example of an IdP that already supports FedCM. [Migrate to FedCM](https://developers.google.com/identity/gsi/web/guides/fedcm-migration) provides instructions for RPs wishing to migrate existing apps using Google Sign In to federated sign-in.

## [Permissions Policy integration and <iframe> support](#permissions_policy_integration_and_iframe_support)

The [identity-credentials-get](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/identity-credentials-get)[Permissions-Policy](/en-US/docs/Web/HTTP/Guides/Permissions_Policy) can be used to control permission to use FedCM. More specifically, it permits usage of the following methods:

- [CredentialsContainer.get()](/en-US/docs/Web/API/CredentialsContainer/get)
- [IdentityCredential.disconnect()](/en-US/docs/Web/API/IdentityCredential/disconnect_static)
- [IdentityProvider.getUserInfo()](/en-US/docs/Web/API/IdentityProvider/getUserInfo_static)

Developers can explicitly grant permission for an [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe) to use FedCM via the `allow` attribute:

html

```
<iframe src="3rd-party.example" allow="identity-credentials-get"></iframe>
```

The availability of FedCM within `<iframe>`s enables a couple of use cases:

- Larger sites won't want a third-party sign-in script to gain control over the top-level frame; instead they will want to add that script and invoke FedCM from within an [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe).
- Some `<iframes>` may themselves require federated authentication.

## [Interfaces](#interfaces)

[IdentityCredential](/en-US/docs/Web/API/IdentityCredential)

Represents a user identity credential arising from successful federated authentication. A successful [navigator.credentials.get()](/en-US/docs/Web/API/CredentialsContainer/get) call that includes an `identity` option fulfills with an [IdentityCredential](/en-US/docs/Web/API/IdentityCredential) instance.

[IdentityCredentialError](/en-US/docs/Web/API/IdentityCredentialError)

Represents an authentication error indicating that the user agent did not receive an identity assertion after the user has asked to authenticate using a federated credential.

[IdentityProvider](/en-US/docs/Web/API/IdentityProvider)

Represents an IdP and provides access to related information and functionality.

[NavigatorLogin](/en-US/docs/Web/API/NavigatorLogin)

Defines login functionality for IdPs, including the [Navigator.login.setStatus()](/en-US/docs/Web/API/NavigatorLogin/setStatus) method for [updating IdP login status](/en-US/docs/Web/API/FedCM_API/IDP_integration#update_login_status_using_the_login_status_api).

## [Extensions to other interfaces](#extensions_to_other_interfaces)

[CredentialsContainer.get()](/en-US/docs/Web/API/CredentialsContainer/get), the `identity` option.

`identity` is an object containing details of federated IdPs that a relying party (RP) website can use to sign users in. It causes a `get()` call to initiate a request for a user to sign in to an RP with an IdP.

[Navigator.login](/en-US/docs/Web/API/Navigator/login)

Provides access to the browser's [NavigatorLogin](/en-US/docs/Web/API/NavigatorLogin) object.

## [HTTP headers](#http_headers)

[Set-Login](/en-US/docs/Web/HTTP/Reference/Headers/Set-Login)

Provides an HTTP mechanism for [updating login status](/en-US/docs/Web/API/FedCM_API/IDP_integration#update_login_status_using_the_login_status_api) via HTTP.

## [Examples](#examples)

For example code, see:

- [Implement an identity solution with FedCM on the Identity Provider side](https://developer.chrome.com/docs/identity/fedcm/implement/identity-provider) on developer.chrome.com (2025)
- [Implement an identity solution with FedCM on the Relying Party side](https://developer.chrome.com/docs/identity/fedcm/implement/relying-party) on developer.chrome.com (2025)

## [Specifications](#specifications)

Specification
[Federated Credential Management API# browser-api-identity-credential-interface](https://w3c-fedid.github.io/FedCM/#browser-api-identity-credential-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Federated Credential Management API](https://developer.chrome.com/docs/identity/fedcm/overview)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/FedCM_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/fedcm_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFedCM_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffedcm_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFedCM_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffedcm_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6722199b4d63fad3c33db1146af380fc98b6c202%0A*+Document+last+modified%3A+2025-10-27T09%3A17%3A57.000Z%0A%0A%3C%2Fdetails%3E)
