# FederatedCredential

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFederatedCredential&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `FederatedCredential` interface of the [Credential Management API](/en-US/docs/Web/API/Credential_Management_API) provides information about credentials from a federated identity provider. A federated identity provider is an entity that a website trusts to correctly authenticate a user, and that provides an API for that purpose. [OpenID Connect](https://openid.net/developers/specs/) is an example of a federated identity provider framework.

Note: The [Federated Credential Management API (FedCM)](/en-US/docs/Web/API/FedCM_API) provides a more complete solution for handling identity federation in the browser, and uses the [IdentityCredential](/en-US/docs/Web/API/IdentityCredential) type.

In browsers that support it, an instance of this interface may be passed in the `credential` member of the `init` object for global [fetch()](/en-US/docs/Web/API/Window/fetch).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[FederatedCredential()](/en-US/docs/Web/API/FederatedCredential/FederatedCredential)Experimental

Creates a new `FederatedCredential` object.

## [Instance properties](#instance_properties)

Inherits properties from its ancestor, [Credential](/en-US/docs/Web/API/Credential).

[FederatedCredential.provider](/en-US/docs/Web/API/FederatedCredential/provider)Read onlyExperimental

Returns a string containing a credential's federated identity provider.

[FederatedCredential.protocol](/en-US/docs/Web/API/FederatedCredential/protocol)Read onlyExperimental

Returns a string containing a credential's federated identity protocol.

## [Instance methods](#instance_methods)

None.

## [Examples](#examples)

js

```
const cred = new FederatedCredential({
  id,
  name,
  provider: "https://account.google.com",
  iconURL,
});

// Store it
navigator.credentials.store(cred).then(() => {
  // Do something else.
});
```

## [Specifications](#specifications)

Specification
[Credential Management Level 1# federated](https://w3c.github.io/webappsec-credential-management/#federated)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/FederatedCredential/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/federatedcredential/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFederatedCredential&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffederatedcredential%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFederatedCredential%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffederatedcredential%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd8f04d843dd81ab8cea1cfc0577ae3c5c9b77d5c%0A*+Document+last+modified%3A+2024-07-26T03%3A29%3A50.000Z%0A%0A%3C%2Fdetails%3E)
