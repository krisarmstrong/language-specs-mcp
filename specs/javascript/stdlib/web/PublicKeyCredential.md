# PublicKeyCredential

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2021⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPublicKeyCredential&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `PublicKeyCredential` interface provides information about a public key / private key pair, which is a credential for logging in to a service using an un-phishable and data-breach resistant asymmetric key pair instead of a password. It inherits from [Credential](/en-US/docs/Web/API/Credential), and is part of the [Web Authentication API](/en-US/docs/Web/API/Web_Authentication_API) extension to the [Credential Management API](/en-US/docs/Web/API/Credential_Management_API).

Note: This API is restricted to top-level contexts. Use from within an [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe) element will not have any effect.

## In this article

- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[PublicKeyCredential.authenticatorAttachment](/en-US/docs/Web/API/PublicKeyCredential/authenticatorAttachment)Read only

A string that indicates the mechanism by which the WebAuthn implementation is attached to the authenticator at the time the associated [navigator.credentials.create()](/en-US/docs/Web/API/CredentialsContainer/create) or [navigator.credentials.get()](/en-US/docs/Web/API/CredentialsContainer/get) call completes.

[PublicKeyCredential.id](/en-US/docs/Web/API/PublicKeyCredential/id)Read only

Inherited from [Credential](/en-US/docs/Web/API/Credential) and overridden to be the [base64url encoding](/en-US/docs/Glossary/Base64) of [PublicKeyCredential.rawId](/en-US/docs/Web/API/PublicKeyCredential/rawId).

[PublicKeyCredential.rawId](/en-US/docs/Web/API/PublicKeyCredential/rawId)Read only

An [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) that holds the globally unique identifier for this `PublicKeyCredential`. This identifier can be used to look up credentials for future calls to [navigator.credentials.get()](/en-US/docs/Web/API/CredentialsContainer/get).

[PublicKeyCredential.response](/en-US/docs/Web/API/PublicKeyCredential/response)Read only

An instance of an [AuthenticatorResponse](/en-US/docs/Web/API/AuthenticatorResponse) object. It is either of type [AuthenticatorAttestationResponse](/en-US/docs/Web/API/AuthenticatorAttestationResponse) if the `PublicKeyCredential` was the results of a [navigator.credentials.create()](/en-US/docs/Web/API/CredentialsContainer/create) call, or of type [AuthenticatorAssertionResponse](/en-US/docs/Web/API/AuthenticatorAssertionResponse) if the `PublicKeyCredential` was the result of a [navigator.credentials.get()](/en-US/docs/Web/API/CredentialsContainer/get) call.

[PublicKeyCredential.type Read only](#publickeycredential.type)

Inherited from [Credential](/en-US/docs/Web/API/Credential). Always set to `public-key` for `PublicKeyCredential` instances.

## [Static methods](#static_methods)

[PublicKeyCredential.getClientCapabilities()](/en-US/docs/Web/API/PublicKeyCredential/getClientCapabilities_static)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with an object that can be used to check whether or not particular WebAuthn capabilities and [extensions](/en-US/docs/Web/API/Web_Authentication_API/WebAuthn_extensions) are supported.

[PublicKeyCredential.isConditionalMediationAvailable()](/en-US/docs/Web/API/PublicKeyCredential/isConditionalMediationAvailable_static)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which resolves to `true` if conditional mediation is available.

[PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable()](/en-US/docs/Web/API/PublicKeyCredential/isUserVerifyingPlatformAuthenticatorAvailable_static)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which resolves to `true` if an authenticator bound to the platform is capable of verifying the user.

[PublicKeyCredential.parseCreationOptionsFromJSON()](/en-US/docs/Web/API/PublicKeyCredential/parseCreationOptionsFromJSON_static)

Convenience method for deserializing server-sent credential registration data when [registering a user with credentials](/en-US/docs/Web/API/Web_Authentication_API#creating_a_key_pair_and_registering_a_user).

[PublicKeyCredential.parseRequestOptionsFromJSON()](/en-US/docs/Web/API/PublicKeyCredential/parseRequestOptionsFromJSON_static)

Convenience method for deserializing server-sent credential request data when [authenticating a (registered) user](/en-US/docs/Web/API/Web_Authentication_API#authenticating_a_user).

[PublicKeyCredential.signalAllAcceptedCredentials()](/en-US/docs/Web/API/PublicKeyCredential/signalAllAcceptedCredentials_static)

Signals to the authenticator all of the valid [credential IDs](/en-US/docs/Web/API/PublicKeyCredentialRequestOptions#id) that the [relying party](https://en.wikipedia.org/wiki/Relying_party) server still holds for a particular user.

[PublicKeyCredential.signalCurrentUserDetails()](/en-US/docs/Web/API/PublicKeyCredential/signalCurrentUserDetails_static)

Signals to the authenticator that a particular user has updated their user name and/or display name.

[PublicKeyCredential.signalUnknownCredential()](/en-US/docs/Web/API/PublicKeyCredential/signalUnknownCredential_static)

Signals to the authenticator that a [credential ID](/en-US/docs/Web/API/PublicKeyCredentialRequestOptions#id) was not recognized by the [relying party](https://en.wikipedia.org/wiki/Relying_party) server, for example because it was deleted.

## [Instance methods](#instance_methods)

[PublicKeyCredential.getClientExtensionResults()](/en-US/docs/Web/API/PublicKeyCredential/getClientExtensionResults)

If any extensions were requested, this method will return the results of processing those extensions.

[PublicKeyCredential.toJSON()](/en-US/docs/Web/API/PublicKeyCredential/toJSON)

Convenience method for creating a JSON string representation of a `PublicKeyCredential` for sending to the server when [registering a user with credentials](/en-US/docs/Web/API/Web_Authentication_API#creating_a_key_pair_and_registering_a_user) and [authenticating a registered user](/en-US/docs/Web/API/Web_Authentication_API#authenticating_a_user).

## [Examples](#examples)

### [Creating a new instance of PublicKeyCredential](#creating_a_new_instance_of_publickeycredential)

Here, we use [navigator.credentials.create()](/en-US/docs/Web/API/CredentialsContainer/create) to generate a new credential.

js

```
const createCredentialOptions = {
  publicKey: {
    challenge: new Uint8Array([
      21, 31, 105 /* 29 more random bytes generated by the server */,
    ]),
    rp: {
      name: "Example CORP",
      id: "login.example.com",
    },
    user: {
      id: new Uint8Array(16),
      name: "canand@example.com",
      displayName: "Carina Anand",
    },
    pubKeyCredParams: [
      {
        type: "public-key",
        alg: -7,
      },
    ],
  },
};

navigator.credentials
  .create(createCredentialOptions)
  .then((newCredentialInfo) => {
    const response = newCredentialInfo.response;
    const clientExtensionsResults =
      newCredentialInfo.getClientExtensionResults();
  })
  .catch((err) => {
    console.error(err);
  });
```

### [Getting an existing instance of PublicKeyCredential](#getting_an_existing_instance_of_publickeycredential)

Here, we fetch an existing credential from an authenticator, using [navigator.credentials.get()](/en-US/docs/Web/API/CredentialsContainer/get).

js

```
const requestCredentialOptions = {
  publicKey: {
    challenge: new Uint8Array([
      /* bytes sent from the server */
    ]),
  },
};

navigator.credentials
  .get(requestCredentialOptions)
  .then((credentialInfoAssertion) => {
    // send assertion response back to the server
    // to proceed with the control of the credential
  })
  .catch((err) => {
    console.error(err);
  });
```

## [Specifications](#specifications)

Specification
[Web Authentication: An API for accessing Public Key Credentials - Level 3# iface-pkcredential](https://w3c.github.io/webauthn/#iface-pkcredential)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The parent interface [Credential](/en-US/docs/Web/API/Credential)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/PublicKeyCredential/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/publickeycredential/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPublicKeyCredential&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpublickeycredential%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPublicKeyCredential%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpublickeycredential%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
