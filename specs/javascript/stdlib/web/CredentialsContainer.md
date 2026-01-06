# CredentialsContainer

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2019⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCredentialsContainer&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `CredentialsContainer` interface of the [Credential Management API](/en-US/docs/Web/API/Credential_Management_API) exposes methods to request credentials and notify the user agent when events such as successful sign in or sign out happen. This interface is accessible from [Navigator.credentials](/en-US/docs/Web/API/Navigator/credentials).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

None.

## [Instance methods](#instance_methods)

[CredentialsContainer.create()](/en-US/docs/Web/API/CredentialsContainer/create)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with a new [Credential](/en-US/docs/Web/API/Credential) instance based on the provided options, or `null` if no `Credential` object can be created. In exceptional circumstances, the [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) may reject.

[CredentialsContainer.get()](/en-US/docs/Web/API/CredentialsContainer/get)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with the [Credential](/en-US/docs/Web/API/Credential) instance that matches the provided parameters.

[CredentialsContainer.preventSilentAccess()](/en-US/docs/Web/API/CredentialsContainer/preventSilentAccess)

Sets a flag that specifies whether automatic log in is allowed for future visits to the current origin, then returns an empty [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise). For example, you might call this, after a user signs out of a website to ensure that they aren't automatically signed in on the next site visit. Earlier versions of the spec called this method `requireUserMediation()`. See [Browser compatibility](#browser_compatibility) for support details.

[CredentialsContainer.store()](/en-US/docs/Web/API/CredentialsContainer/store)

Stores a set of credentials for a user, inside a provided [Credential](/en-US/docs/Web/API/Credential) instance and returns that instance in a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise).

## [Specifications](#specifications)

Specification
[Credential Management Level 1# credentialscontainer](https://w3c.github.io/webappsec-credential-management/#credentialscontainer)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 5, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/CredentialsContainer/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/credentialscontainer/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCredentialsContainer&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcredentialscontainer%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCredentialsContainer%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcredentialscontainer%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc91c87d7da181194f3786abfcb2f27d2b885fb91%0A*+Document+last+modified%3A+2024-02-05T23%3A02%3A38.000Z%0A%0A%3C%2Fdetails%3E)
