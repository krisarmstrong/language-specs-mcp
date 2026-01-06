# AuthenticatorAssertionResponse

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2021⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAuthenticatorAssertionResponse&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `AuthenticatorAssertionResponse` interface of the [Web Authentication API](/en-US/docs/Web/API/Web_Authentication_API) contains a [digital signature](/en-US/docs/Glossary/Signature/Security) from the private key of a particular WebAuthn credential. The relying party's server can verify this signature to authenticate a user, for example when they sign in.

An `AuthenticatorAssertionResponse` object instance is available in the [response](/en-US/docs/Web/API/PublicKeyCredential/response) property of a [PublicKeyCredential](/en-US/docs/Web/API/PublicKeyCredential) object returned by a successful [navigator.credentials.get()](/en-US/docs/Web/API/CredentialsContainer/get) call.

This interface inherits from [AuthenticatorResponse](/en-US/docs/Web/API/AuthenticatorResponse).

Note: This interface is restricted to top-level contexts. Use from within an [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe) element will not have any effect.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Also inherits properties from its parent, [AuthenticatorResponse](/en-US/docs/Web/API/AuthenticatorResponse).

[AuthenticatorAssertionResponse.authenticatorData](/en-US/docs/Web/API/AuthenticatorAssertionResponse/authenticatorData)Read only

An [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) containing information from the authenticator such as the Relying Party ID Hash (rpIdHash), a signature counter, test of user presence and user verification flags, and any extensions processed by the authenticator.

[AuthenticatorResponse.clientDataJSON](/en-US/docs/Web/API/AuthenticatorResponse/clientDataJSON)Read only

Contains the JSON-compatible serialization of the data passed from the browser to the authenticator in order to authenticate with this credential — i.e., when [CredentialsContainer.get()](/en-US/docs/Web/API/CredentialsContainer/get) is called with a `publicKey` option. This data contains some information from the options passed into the `get()` call, and some information controlled by the browser.

[AuthenticatorAssertionResponse.signature](/en-US/docs/Web/API/AuthenticatorAssertionResponse/signature)Read only

An assertion signature over [AuthenticatorAssertionResponse.authenticatorData](/en-US/docs/Web/API/AuthenticatorAssertionResponse/authenticatorData) and [AuthenticatorResponse.clientDataJSON](/en-US/docs/Web/API/AuthenticatorResponse/clientDataJSON). The assertion signature is created with the private key of the key pair that was created during the originating [navigator.credentials.create()](/en-US/docs/Web/API/CredentialsContainer/create) call and verified using the public key of that same key pair.

[AuthenticatorAssertionResponse.userHandle](/en-US/docs/Web/API/AuthenticatorAssertionResponse/userHandle)Read only

An [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) containing an opaque user identifier, specified as `user.id` in the options passed to the originating [navigator.credentials.create()](/en-US/docs/Web/API/CredentialsContainer/create) call.

## [Instance methods](#instance_methods)

None.

## [Examples](#examples)

See [Retrieving a public key credential](/en-US/docs/Web/API/CredentialsContainer/get#retrieving_a_public_key_credential) for a detailed example.

## [Specifications](#specifications)

Specification
[Web Authentication: An API for accessing Public Key Credentials - Level 3# iface-authenticatorassertionresponse](https://w3c.github.io/webauthn/#iface-authenticatorassertionresponse)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [AuthenticatorAttestationResponse](/en-US/docs/Web/API/AuthenticatorAttestationResponse): the interface for the type of response given when creating a new credential
- [AuthenticatorResponse](/en-US/docs/Web/API/AuthenticatorResponse): the parent interface

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 25, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/AuthenticatorAssertionResponse/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/authenticatorassertionresponse/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAuthenticatorAssertionResponse&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fauthenticatorassertionresponse%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAuthenticatorAssertionResponse%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fauthenticatorassertionresponse%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F515d03ad8572b96e88916888156444626dcba193%0A*+Document+last+modified%3A+2025-03-25T03%3A39%3A37.000Z%0A%0A%3C%2Fdetails%3E)
