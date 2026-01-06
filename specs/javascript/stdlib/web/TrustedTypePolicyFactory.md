# TrustedTypePolicyFactory

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTrustedTypePolicyFactory&level=not)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `TrustedTypePolicyFactory` interface of the [Trusted Types API](/en-US/docs/Web/API/Trusted_Types_API) creates policies and allows the verification of Trusted Type objects against created policies.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[TrustedTypePolicyFactory.emptyHTML](/en-US/docs/Web/API/TrustedTypePolicyFactory/emptyHTML)Read only

Returns a [TrustedHTML](/en-US/docs/Web/API/TrustedHTML) object containing an empty string.

[TrustedTypePolicyFactory.emptyScript](/en-US/docs/Web/API/TrustedTypePolicyFactory/emptyScript)Read only

Returns a [TrustedScript](/en-US/docs/Web/API/TrustedScript) object containing an empty string.

[TrustedTypePolicyFactory.defaultPolicy](/en-US/docs/Web/API/TrustedTypePolicyFactory/defaultPolicy)Read only

Returns the default [TrustedTypePolicy](/en-US/docs/Web/API/TrustedTypePolicy) or null if this is empty.

## [Instance methods](#instance_methods)

[TrustedTypePolicyFactory.createPolicy()](/en-US/docs/Web/API/TrustedTypePolicyFactory/createPolicy)

Creates a [TrustedTypePolicy](/en-US/docs/Web/API/TrustedTypePolicy) object that implements the rules passed as `policyOptions`.

[TrustedTypePolicyFactory.isHTML()](/en-US/docs/Web/API/TrustedTypePolicyFactory/isHTML)

When passed a value checks that it is a valid [TrustedHTML](/en-US/docs/Web/API/TrustedHTML) object.

[TrustedTypePolicyFactory.isScript()](/en-US/docs/Web/API/TrustedTypePolicyFactory/isScript)

When passed a value checks that it is a valid [TrustedScript](/en-US/docs/Web/API/TrustedScript) object.

[TrustedTypePolicyFactory.isScriptURL()](/en-US/docs/Web/API/TrustedTypePolicyFactory/isScriptURL)

When passed a value checks that it is a valid [TrustedScriptURL](/en-US/docs/Web/API/TrustedScriptURL) object.

[TrustedTypePolicyFactory.getAttributeType()](/en-US/docs/Web/API/TrustedTypePolicyFactory/getAttributeType)

Allows web developers to check whether a Trusted Type is required for an element and attribute, and if so which one.

[TrustedTypePolicyFactory.getPropertyType()](/en-US/docs/Web/API/TrustedTypePolicyFactory/getPropertyType)

Allows web developers to check whether a Trusted Type is required for a property, and if so which one.

## [Examples](#examples)

The below code creates a policy with the name `"myEscapePolicy"` with a function defined for `createHTML()` which sanitizes HTML.

We then use the policy to sanitize a string, creating a [TrustedHTML](/en-US/docs/Web/API/TrustedHTML) object, `escaped`. This object can be tested with [isHTML()](/en-US/docs/Web/API/TrustedTypePolicyFactory/isHTML) to ensure that it was created by one of our policies.

js

```
const escapeHTMLPolicy = trustedTypes.createPolicy("myEscapePolicy", {
  createHTML: (string) => string.replace(/</g, "&lt;"),
});

const escaped = escapeHTMLPolicy.createHTML("<img src=x onerror=alert(1)>");

console.log(trustedTypes.isHTML(escaped)); // true;
```

## [Specifications](#specifications)

Specification
[Trusted Types# trusted-type-policy-factory](https://w3c.github.io/trusted-types/dist/spec/#trusted-type-policy-factory)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 3, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/TrustedTypePolicyFactory/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/trustedtypepolicyfactory/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTrustedTypePolicyFactory&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftrustedtypepolicyfactory%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTrustedTypePolicyFactory%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftrustedtypepolicyfactory%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc7d5004cd6c5d5b1318f626425fcb06cb2c6a509%0A*+Document+last+modified%3A+2024-08-03T00%3A24%3A59.000Z%0A%0A%3C%2Fdetails%3E)
