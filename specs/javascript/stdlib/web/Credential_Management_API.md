# Credential Management API

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The Credential Management API enables a website to create, store, and retrieve [credentials](/en-US/docs/Glossary/Credential). A credential is an item which enables a system to make an [authentication](/en-US/docs/Glossary/Authentication) decision: for example, to decide whether to sign a user into an account. We can think of it as a piece of evidence that a user presents to a website to demonstrate that they really are the person they are claiming to be.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

The central interface is the [CredentialsContainer](/en-US/docs/Web/API/CredentialsContainer), which is accessed through the [navigator.credentials](/en-US/docs/Web/API/Navigator/credentials) property and provides three main functions:

- [create()](/en-US/docs/Web/API/CredentialsContainer/create): create a new credential.
- [store()](/en-US/docs/Web/API/CredentialsContainer/store): store a new credential locally.
- [get()](/en-US/docs/Web/API/CredentialsContainer/get): retrieve a credential, which can then be used to log a user in.

The API supports four different types of credential, which are all represented as subclasses of [Credential](/en-US/docs/Web/API/Credential):

TypeInterfacePassword[PasswordCredential](/en-US/docs/Web/API/PasswordCredential)Federated identity[IdentityCredential](/en-US/docs/Web/API/IdentityCredential), [FederatedCredential](/en-US/docs/Web/API/FederatedCredential) (deprecated)One-time password (OTP)[OTPCredential](/en-US/docs/Web/API/OTPCredential)Web Authentication[PublicKeyCredential](/en-US/docs/Web/API/PublicKeyCredential)

The guide page [Credential types](/en-US/docs/Web/API/Credential_Management_API/Credential_types) gives an overview of the different credential types and how they are used.

## [Interfaces](#interfaces)

[Credential](/en-US/docs/Web/API/Credential)

Provides information about an entity as a prerequisite to a trust decision.

[CredentialsContainer](/en-US/docs/Web/API/CredentialsContainer)

Exposes methods to request credentials and notify the user agent when interesting events occur such as successful sign in or sign out. This interface is accessible from `navigator.credentials`.

[FederatedCredential](/en-US/docs/Web/API/FederatedCredential)

Provides information about credentials from a federated identity provider, which is an entity that a website trusts to correctly authenticate a user, and which provides an API for that purpose. [OpenID Connect](https://openid.net/developers/specs/) is an example of such a framework.

[PasswordCredential](/en-US/docs/Web/API/PasswordCredential)

Provides information about a username/password pair.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[Navigator.credentials](/en-US/docs/Web/API/Navigator/credentials)Read only

Returns the [CredentialsContainer](/en-US/docs/Web/API/CredentialsContainer) interface which exposes methods to request credentials and notify the user agent when interesting events occur such as successful sign in or sign out.

## [Specifications](#specifications)

Specification[Credential Management Level 1](https://w3c.github.io/webappsec-credential-management/)

## [Browser compatibility](#browser_compatibility)

### [api.Credential](#api.Credential)

### [api.CredentialsContainer](#api.CredentialsContainer)

### [api.FederatedCredential](#api.FederatedCredential)

### [api.PasswordCredential](#api.PasswordCredential)

## [See also](#see_also)

- [Web Authentication API](/en-US/docs/Web/API/Web_Authentication_API)
- [WebOTP API](/en-US/docs/Web/API/WebOTP_API)
- [Federated Credential Management (FedCM) API](/en-US/docs/Web/API/FedCM_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 4, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Credential_Management_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/credential_management_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCredential_Management_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcredential_management_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCredential_Management_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcredential_management_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb22d69df86326c4fb5bc0e4c310f4933080ab3da%0A*+Document+last+modified%3A+2024-06-04T08%3A44%3A01.000Z%0A%0A%3C%2Fdetails%3E)
