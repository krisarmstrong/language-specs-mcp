# FederatedCredentialInit

The `FederatedCredentialInit` dictionary represents the object passed to [CredentialsContainer.create()](/en-US/docs/Web/API/CredentialsContainer/create) as the value of the `federated` option: that is, when creating a [FederatedCredential](/en-US/docs/Web/API/FederatedCredential) object representing a credential associated with a federated identify provider.

Note: The [Federated Credential Management API (FedCM)](/en-US/docs/Web/API/FedCM_API) supersedes the [FederatedCredential](/en-US/docs/Web/API/FederatedCredential) interface in favor of the [IdentityCredential](/en-US/docs/Web/API/IdentityCredential) interface.

The `FederatedCredentialInit` dictionary is not used when working with the `IdentityCredential` interface.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)

## [Instance properties](#instance_properties)

[iconURL Optional](#iconurl)

A string representing the URL of an icon or avatar to be associated with the credential.

[id](#id)

A string representing a unique ID for the credential.

[name Optional](#name)

A string representing the credential username.

[origin](#origin)

A string representing the credential's origin. [FederatedCredential](/en-US/docs/Web/API/FederatedCredential) objects are origin-bound, which means that they will only be usable on the specified origin they were intended to be used on.

[protocol Optional](#protocol)

A string representing the protocol of the credentials' federated identity provider (for example, `"openidconnect"`).

[provider](#provider)

A string representing the credentials' federated identity provider (for example `"https://www.facebook.com"` or `"https://accounts.google.com"`).

## [Examples](#examples)

### [Creating a federated identity credential](#creating_a_federated_identity_credential)

js

```
const credInit = {
  id: "1234",
  name: "Serpentina",
  origin: "https://example.org",
  protocol: "openidconnect",
  provider: "https://provider.example.org",
};

const makeCredential = document.querySelector("#make-credential");

makeCredential.addEventListener("click", async () => {
  const cred = await navigator.credentials.create({
    federated: credInit,
  });
  console.log(cred.name);
  console.log(cred.provider);
});
```

## [Specifications](#specifications)

Specification
[Credential Management Level 1# dom-federatedcredential-federatedcredential](https://w3c.github.io/webappsec-credential-management/#dom-federatedcredential-federatedcredential)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 13, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/FederatedCredentialInit/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/federatedcredentialinit/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFederatedCredentialInit&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffederatedcredentialinit%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFederatedCredentialInit%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffederatedcredentialinit%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbb48907e64eb4bf60f17efd7d39b46c771d220a0%0A*+Document+last+modified%3A+2024-08-13T13%3A25%3A16.000Z%0A%0A%3C%2Fdetails%3E)
