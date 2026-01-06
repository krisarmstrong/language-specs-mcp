# Credential

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2019⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCredential&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `Credential` interface of the [Credential Management API](/en-US/docs/Web/API/Credential_Management_API) provides information about an entity (usually a user) normally as a prerequisite to a trust decision.

`Credential` objects may be of the following types:

- [FederatedCredential](/en-US/docs/Web/API/FederatedCredential)
- [IdentityCredential](/en-US/docs/Web/API/IdentityCredential)
- [PasswordCredential](/en-US/docs/Web/API/PasswordCredential)
- [PublicKeyCredential](/en-US/docs/Web/API/PublicKeyCredential)
- [OTPCredential](/en-US/docs/Web/API/OTPCredential)

## In this article

- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[Credential.id](/en-US/docs/Web/API/Credential/id)Read only

Returns a string containing the credential's identifier. This might be any one of a GUID, username, or email address.

[Credential.type](/en-US/docs/Web/API/Credential/type)Read only

Returns a string containing the credential's type. Valid values are `password`, `federated`, `public-key`, `identity` and `otp`. (For [PasswordCredential](/en-US/docs/Web/API/PasswordCredential), [FederatedCredential](/en-US/docs/Web/API/FederatedCredential), [PublicKeyCredential](/en-US/docs/Web/API/PublicKeyCredential), [IdentityCredential](/en-US/docs/Web/API/IdentityCredential) and [OTPCredential](/en-US/docs/Web/API/OTPCredential))

## [Static methods](#static_methods)

[Credential.isConditionalMediationAvailable()](/en-US/docs/Web/API/Credential/isConditionalMediationAvailable_static)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which always resolves to `false`. Subclasses may override this value.

## [Examples](#examples)

js

```
const pwdCredential = new PasswordCredential({
  id: "example-username", // Username/ID
  name: "Carina Anand", // Display name
  password: "correct horse battery staple", // Password
});

console.assert(pwdCredential.type === "password");
```

## [Specifications](#specifications)

Specification
[Credential Management Level 1# the-credential-interface](https://w3c.github.io/webappsec-credential-management/#the-credential-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 9, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Credential/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/credential/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCredential&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcredential%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCredential%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcredential%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F463cfc7f25a083241b06a5f5a9a927924f48ca6e%0A*+Document+last+modified%3A+2025-09-09T07%3A59%3A33.000Z%0A%0A%3C%2Fdetails%3E)
