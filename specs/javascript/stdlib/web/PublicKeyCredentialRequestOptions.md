# PublicKeyCredentialRequestOptions

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2019⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPublicKeyCredentialRequestOptions&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `PublicKeyCredentialRequestOptions` dictionary represents the object passed to [CredentialsContainer.get()](/en-US/docs/Web/API/CredentialsContainer/get) as the value of the `publicKey` option.

It is used to request a [PublicKeyCredential](/en-US/docs/Web/API/PublicKeyCredential) provided by an [authenticator](/en-US/docs/Glossary/Authenticator) that supports the [Web Authentication API](/en-US/docs/Web/API/Web_Authentication_API).

## In this article

- [Instance properties](#instance_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[allowCredentials Optional](#allowcredentials)

An array of objects used to restrict the list of acceptable credentials. An empty array indicates that any credential is acceptable.

Each object in the array will contain the following properties:

[id](#id)

An [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer), [TypedArray](/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray), or [DataView](/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView) representing the ID of the public key credential to retrieve. This value is mirrored by the [rawId](/en-US/docs/Web/API/PublicKeyCredential/rawId) property of the [PublicKeyCredential](/en-US/docs/Web/API/PublicKeyCredential) object returned by a successful `get()` call.

[transports Optional](#transports)

An array of strings providing hints as to the methods the client could use to communicate with the relevant authenticator of the public key credential to retrieve. Possible transports are: `"ble"`, `"hybrid"`, `"internal"`, `"nfc"`, and `"usb"`.

Note: This value is mirrored by the return value of the [PublicKeyCredential.response.getTransports()](/en-US/docs/Web/API/AuthenticatorAttestationResponse/getTransports) method of the [PublicKeyCredential](/en-US/docs/Web/API/PublicKeyCredential) object returned by the `create()` call that originally created the credential. At that point, it should be stored by the app for later use.

[type](#type)

A string defining the type of the public key credential to retrieve. This can currently take a single value, `"public-key"`, but more values may be added in the future. This value is mirrored by the [type](/en-US/docs/Web/API/Credential/type) property of the [PublicKeyCredential](/en-US/docs/Web/API/PublicKeyCredential) object returned by a successful `get()` call.

This value defaults to an empty array.

[challenge](#challenge)

An [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer), [TypedArray](/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray), or [DataView](/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView) originating from the relying party's server and used as a [cryptographic challenge](https://en.wikipedia.org/wiki/Challenge%E2%80%93response_authentication). This value will be signed by the authenticator and the signature will be sent back as part of the [AuthenticatorAssertionResponse.signature](/en-US/docs/Web/API/AuthenticatorAssertionResponse/signature) (available in the [response](/en-US/docs/Web/API/PublicKeyCredential/response) property of the [PublicKeyCredential](/en-US/docs/Web/API/PublicKeyCredential) object returned by a successful `get()` call).

[extensions Optional](#extensions)

An object containing properties representing the input values for any requested extensions. These extensions are used to specific additional processing by the client or authenticator during the authentication process. Examples include dealing with legacy FIDO API credentials, and evaluating outputs from a pseudo-random function (PRF) associated with a credential.

Extensions are optional and different browsers may recognize different extensions. Processing extensions is always optional for the client: if a browser does not recognize a given extension, it will just ignore it. For information on using extensions, and which ones are supported by which browsers, see [Web Authentication extensions](/en-US/docs/Web/API/Web_Authentication_API/WebAuthn_extensions).

[hints Optional 
Experimental](#hints)

An array of strings providing hints as to what UI the browser should provide for the user to authenticate with an existing public key credential.

The strings can be any of the following:

["security-key"](#security-key)

The UI should recommend requesting the credential from a separate physical security key (such as a YubiKey).

["client-device"](#client-device)

The UI should recommend requesting the credential from an authenticator available on the same device they are using to access the RP client.

["hybrid"](#hybrid)

The UI should recommend requesting the credential from a general-purpose authenticator, such as a smartphone-based authenticator app. This favors using a cross-device approach to handling authentication, relying on a combination of laptop and smartphone, for example.

When multiple strings are included in the array, their order denotes the order of preference, from high to low. Supporting browsers that respect the hints should use the first one that they understand.

Specified `hints` may contradict hints provided in the [transports](#transports) option. When the provided `hints` contradict this option, the `hints` take precedence. `hints` may also be ignored by the browser under specific circumstances, for example if a hinted authenticator type is not usable on the user's device.

For some specific code and UI examples, see [Introducing hints, Related Origin Requests and JSON serialization for WebAuthn in Chrome](https://developer.chrome.com/blog/passkeys-updates-chrome-129#hints).

[rpId Optional](#rpid)

A string that specifies the relying party's identifier (for example `"login.example.org"`). For security purposes:

- The browser verifies that `rpId` matches the relying party's origin or is a domain suffix of the relying party's origin (for example, `example.org`).
- The authenticator verifies that `rpId` matches the `rpId` of the credential used for the authentication ceremony.

This value defaults to the current origin's domain.

[timeout Optional](#timeout)

A numerical hint, in milliseconds, indicating the time the relying party is willing to wait for the retrieval operation to complete. This hint may be overridden by the browser.

[userVerification Optional](#userverification)

A string specifying the relying party's requirements for user verification of the authentication process. This verification is initiated by the authenticator, which will request the user to provide an available factor (for example a PIN or a biometric input of some kind).

The value can be one of the following:

["required"](#required)

The relying party requires user verification, and the operation will fail if it does not occur.

["preferred"](#preferred)

The relying party prefers user verification if possible, but the operation will not fail if it does not occur.

["discouraged"](#discouraged)

The relying party does not want user verification, in the interests of making user interaction as smooth as possible.

This value defaults to `"preferred"`.

## [Specifications](#specifications)

Specification
[Web Authentication: An API for accessing Public Key Credentials - Level 3# dictdef-publickeycredentialrequestoptions](https://w3c.github.io/webauthn/#dictdef-publickeycredentialrequestoptions)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 12, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/PublicKeyCredentialRequestOptions/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/publickeycredentialrequestoptions/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPublicKeyCredentialRequestOptions&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpublickeycredentialrequestoptions%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPublicKeyCredentialRequestOptions%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpublickeycredentialrequestoptions%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd8b42532527099c261c6a59a7e2f4f506e9a392e%0A*+Document+last+modified%3A+2025-12-12T12%3A41%3A30.000Z%0A%0A%3C%2Fdetails%3E)
