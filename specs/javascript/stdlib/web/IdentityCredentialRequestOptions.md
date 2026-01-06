# IdentityCredentialRequestOptions

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIdentityCredentialRequestOptions&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `IdentityCredentialRequestOptions` dictionary represents the object passed to [CredentialsContainer.get()](/en-US/docs/Web/API/CredentialsContainer/get) as the value of the `identity` option.

When an `identity` option is provided in a `get()` call made on a [relying party](/en-US/docs/Glossary/Relying_party) (RP) website, the user is offered a list of [federated identity providers](/en-US/docs/Glossary/Identity_provider) (IdPs) as sign-in options. Once the user signs in successfully using one of these options, the promise returned by the `get()` call returns an [IdentityCredential](/en-US/docs/Web/API/IdentityCredential) object.

## In this article

- [Instance properties](#instance_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[context Optional](#context)

A string specifying the context in which the user is authenticating with FedCM. The browser uses this value to vary the text in its FedCM UI to better suit the context. Possible values are:

["continue"](#continue)

Suitable for situations where the user is choosing an identity to continue to the next page in the flow, which requires a sign-in. Browsers will provide a text string similar to:

Continue to <page-origin> with <IdP>

["signin"](#signin)

Suitable for general situations where the user is signing in with an IdP account they've already used on this origin. Browsers will provide a text string similar to:

Sign in to <page-origin> with <IdP>

["signup"](#signup)

An option for situations where the user is signing in to the origin with a new IdP account they've not used here before. Browsers will provide a text string similar to:

Sign up to <page-origin> with <IdP>

["use"](#use)

Suitable for situations where a different action, such as validating a payment, is being performed. Browsers will provide a text string similar to:

Use <page-origin> with <IdP>

The default value is `"signin"`.

[mode Optional](#mode)

A string specifying the UI mode to use for the sign-in flow. Possible values are:

[active](#active)

The sign-in flow must be initiated via a user action such as clicking a button. If `mode` is set to `active`, `providers` can only have a length of `1`, otherwise the `get()` promise will reject.

[passive](#passive)

The sign-in flow can be initiated without direct user interaction. This is the default value.

See [Active versus passive mode](/en-US/docs/Web/API/FedCM_API/RP_sign-in#active_versus_passive_mode) for more details of the difference between the two modes.

[providers](#providers)

An array of objects specifying details of the IdPs that the user should be presented with as options for signing in. These objects can contain the following properties:

[configURL](#configurl)

A string specifying the URL of the IdP's config file. See [Provide a config file](/en-US/docs/Web/API/FedCM_API/IDP_integration#provide_a_config_file_and_endpoints) for more information.

[clientId](#clientid)

A string specifying the RP client identifier. This information is issued by the IdP to the RP in a separate process that is specific to the IdP.

[domainHint Optional](#domainhint)

A string hinting at the domain of accounts that the RP is interested in. If provided, the user agent will only show accounts that match the domain hint value in their [domain_hints](/en-US/docs/Web/API/FedCM_API/IDP_integration#domain_hints) array. If `"any"` is specified, the RP will show any account that is associated with at least one domain hint.

[fields Optional](#fields)

An array of strings specifying user information that the RP wishes to obtain from the IdP for use in the sign-in process. The exact strings will vary by IdP, but tend to be similar to `"name"`, `"email"`, or `"profile-picture-url"`.

[loginHint Optional](#loginhint)

A string providing a hint about the account option(s) the browser should provide for the user to sign in with. This is useful in cases where the user has already signed in and the site asks them to reauthenticate. Otherwise, the reauthentication process can be confusing when a user has multiple accounts and can't remember which one they used to sign in previously. The value for the `loginHint` property can be taken from the user's previous sign-in, and is matched against the `login_hints` values provided by the IdP in the array of user information returned from the IdP's [accounts list endpoint](/en-US/docs/Web/API/FedCM_API/IDP_integration#the_accounts_list_endpoint).

[nonce Optional](#nonce)

A random string that can be included to ensure the response is issued specifically for this request and prevent [replay attacks](/en-US/docs/Glossary/Replay_attack).

Note: This property has been removed from the specification, because not all the protocols that use the FedCM API require a nonce. If the RP does need to include a nonce, it should be provided in the [params](#params) property.

[params Optional](#params)

Any additional parameters that the RP needs to pass to the IdP.

## [Specifications](#specifications)

Specification
[Federated Credential Management API# dictdef-identitycredentialrequestoptions](https://w3c-fedid.github.io/FedCM/#dictdef-identitycredentialrequestoptions)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 19, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/IdentityCredentialRequestOptions/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/identitycredentialrequestoptions/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIdentityCredentialRequestOptions&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fidentitycredentialrequestoptions%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIdentityCredentialRequestOptions%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fidentitycredentialrequestoptions%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F798f5efbce403e2366323afea025e5729b902e46%0A*+Document+last+modified%3A+2025-12-19T00%3A53%3A07.000Z%0A%0A%3C%2Fdetails%3E)
