# IdentityCredential

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIdentityCredential&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `IdentityCredential` interface of the [Federated Credential Management API (FedCM)](/en-US/docs/Web/API/FedCM_API) represents a user identity credential arising from a successful federated sign-in.

A successful [navigator.credentials.get()](/en-US/docs/Web/API/CredentialsContainer/get) call that includes an `identity` option fulfills with an `IdentityCredential` instance.

## In this article

- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its ancestor, [Credential](/en-US/docs/Web/API/Credential).

[IdentityCredential.configURL](/en-US/docs/Web/API/IdentityCredential/configURL)Read onlyExperimental

A string specifying the [config file](/en-US/docs/Web/API/FedCM_API/IDP_integration#provide_a_config_file_and_endpoints) URL of the [IdP](/en-US/docs/Glossary/Identity_provider) used for sign-in.

[IdentityCredential.isAutoSelected](/en-US/docs/Web/API/IdentityCredential/isAutoSelected)Read onlyExperimental

A boolean value that indicates whether the federated sign-in was carried out using [auto-reauthentication](/en-US/docs/Web/API/FedCM_API/RP_sign-in#auto-reauthentication) (i.e., without user mediation) or not.

[IdentityCredential.token](/en-US/docs/Web/API/IdentityCredential/token)Experimental

Returns the token used to validate the associated sign-in.

## [Static methods](#static_methods)

[IdentityCredential.disconnect()](/en-US/docs/Web/API/IdentityCredential/disconnect_static)Experimental

Disconnects the federated sign-in account used to obtain the credential.

## [Examples](#examples)

### [Basic federated sign-in](#basic_federated_sign-in)

[Relying parties](/en-US/docs/Glossary/Relying_party) (RPs) can call `navigator.credentials.get()` with the `identity` option to make a request for users to sign in to the RP via an identity provider (IdP), using identity federation. A typical request would look like this:

js

```
async function signIn() {
  const identityCredential = await navigator.credentials.get({
    identity: {
      providers: [
        {
          configURL: "https://accounts.idp.example/config.json",
          clientId: "********",
          params: {
            /* IdP-specific parameters */
          },
        },
      ],
    },
  });
}
```

If successful, this call will fulfill with an `IdentityCredential` instance. From this, you could return the [IdentityCredential.token](/en-US/docs/Web/API/IdentityCredential/token) value, for example:

js

```
console.log(identityCredential.token);
```

Check out [Federated Credential Management API (FedCM)](/en-US/docs/Web/API/FedCM_API) for more details on how this works. This call will start off the sign-in flow described in [FedCM sign-in flow](/en-US/docs/Web/API/FedCM_API/RP_sign-in#fedcm_sign-in_flow).

## [Specifications](#specifications)

Specification
[Federated Credential Management API# browser-api-identity-credential-interface](https://w3c-fedid.github.io/FedCM/#browser-api-identity-credential-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Federated Credential Management API](https://developer.chrome.com/docs/identity/fedcm/overview)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 19, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/IdentityCredential/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/identitycredential/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIdentityCredential&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fidentitycredential%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIdentityCredential%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fidentitycredential%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F798f5efbce403e2366323afea025e5729b902e46%0A*+Document+last+modified%3A+2025-12-19T00%3A53%3A07.000Z%0A%0A%3C%2Fdetails%3E)
