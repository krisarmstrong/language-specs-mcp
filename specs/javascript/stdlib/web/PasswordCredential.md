# PasswordCredential

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPasswordCredential&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `PasswordCredential` interface of the [Credential Management API](/en-US/docs/Web/API/Credential_Management_API) provides information about a username/password pair. In supporting browsers an instance of this class may be passed in the `credential` member of the `init` object for global [fetch()](/en-US/docs/Web/API/Window/fetch).

Note: This interface is restricted to top-level contexts and cannot be used from an [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[PasswordCredential()](/en-US/docs/Web/API/PasswordCredential/PasswordCredential)Experimental

Creates a new `PasswordCredential` object.

## [Instance properties](#instance_properties)

Inherits properties from its ancestor, [Credential](/en-US/docs/Web/API/Credential).

[PasswordCredential.iconURL](/en-US/docs/Web/API/PasswordCredential/iconURL)Read onlyExperimental

A string containing a URL pointing to an image for an icon. This image is intended for display in a credential chooser. The URL must be accessible without authentication.

[PasswordCredential.name](/en-US/docs/Web/API/PasswordCredential/name)Read onlyExperimental

A human-readable string that provides public name for display in a credential chooser.

[PasswordCredential.password](/en-US/docs/Web/API/PasswordCredential/password)Read onlyExperimental

A string containing the password of the credential.

## [Instance methods](#instance_methods)

None.

## [Examples](#examples)

js

```
const cred = new PasswordCredential({
  id,
  password,
  name,
  iconURL,
});

navigator.credentials.store(cred).then(() => {
  // Do something else.
});
```

## [Specifications](#specifications)

Specification
[Credential Management Level 1# passwordcredential-interface](https://w3c.github.io/webappsec-credential-management/#passwordcredential-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/PasswordCredential/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/passwordcredential/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPasswordCredential&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpasswordcredential%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPasswordCredential%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpasswordcredential%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Faa8fa82a902746b0bd97839180fc2b5397088140%0A*+Document+last+modified%3A+2024-07-26T02%3A56%3A16.000Z%0A%0A%3C%2Fdetails%3E)
