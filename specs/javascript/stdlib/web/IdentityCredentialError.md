# IdentityCredentialError

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `IdentityCredentialError` interface of the [FedCM API](/en-US/docs/Web/API/FedCM_API) describes an authentication error indicating that the user agent did not receive an identity assertion after the user has requested to use a federated account. This can happen if the client is unauthorized or if the server is temporarily unavailable, for example.

Browsers can use this error type to show the error message in the user interface.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[IdentityCredentialError()](/en-US/docs/Web/API/IdentityCredentialError/IdentityCredentialError)Experimental

Creates a new `IdentityCredentialError` object instance.

## [Instance properties](#instance_properties)

In addition to the properties below, `IdentityCredentialError` inherits properties from its parent, [DOMException](/en-US/docs/Web/API/DOMException).

[error](/en-US/docs/Web/API/IdentityCredentialError/error)ExperimentalRead only

A string. This can be either one of the values listed in the [OAuth 2.0 specified error list](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1.2.1) or an arbitrary string.

[url](/en-US/docs/Web/API/IdentityCredentialError/url)ExperimentalRead only

A URL pointing to human-readable information about the error to display to users, such as how to fix the error or contact customer service.

## [Examples](#examples)

js

```
try {
  const cred = await navigator.credentials.get({
    identity: {
      providers: [
        {
          configURL: "https://idp.example/manifest.json",
          clientId: "1234",
        },
      ],
    },
  });
} catch (e) {
  const error = e.error;
  const url = e.url;
}
```

## [Specifications](#specifications)

Specification
[Federated Credential Management API# browser-api-identity-credential-error-interface](https://w3c-fedid.github.io/FedCM/#browser-api-identity-credential-error-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [CredentialsContainer.get()](/en-US/docs/Web/API/CredentialsContainer/get)
- [ID assertion error responses](/en-US/docs/Web/API/FedCM_API/IDP_integration#id_assertion_error_responses)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 4, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/IdentityCredentialError/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/identitycredentialerror/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIdentityCredentialError&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fidentitycredentialerror%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIdentityCredentialError%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fidentitycredentialerror%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff1251a98115e7a6d566331512256dcbbc4cf7c24%0A*+Document+last+modified%3A+2025-09-04T01%3A14%3A52.000Z%0A%0A%3C%2Fdetails%3E)
