# TrustedTypePolicy

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTrustedTypePolicy&level=not)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `TrustedTypePolicy` interface of the [Trusted Types API](/en-US/docs/Web/API/Trusted_Types_API) defines a group of functions which create `TrustedType` objects.

A `TrustedTypePolicy` object is created by [TrustedTypePolicyFactory.createPolicy()](/en-US/docs/Web/API/TrustedTypePolicyFactory/createPolicy) to define a policy for enforcing security rules on input. Therefore, `TrustedTypePolicy` has no constructor.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[TrustedTypePolicy.name](/en-US/docs/Web/API/TrustedTypePolicy/name)Read only

A string containing the name of the policy.

## [Instance methods](#instance_methods)

[TrustedTypePolicy.createHTML()](/en-US/docs/Web/API/TrustedTypePolicy/createHTML)

Creates a [TrustedHTML](/en-US/docs/Web/API/TrustedHTML) object.

[TrustedTypePolicy.createScript()](/en-US/docs/Web/API/TrustedTypePolicy/createScript)

Creates a [TrustedScript](/en-US/docs/Web/API/TrustedScript) object.

[TrustedTypePolicy.createScriptURL()](/en-US/docs/Web/API/TrustedTypePolicy/createScriptURL)

Creates a [TrustedScriptURL](/en-US/docs/Web/API/TrustedScriptURL) object.

## [Examples](#examples)

In the below example we create a policy that will create [TrustedHTML](/en-US/docs/Web/API/TrustedHTML) objects using [TrustedTypePolicyFactory.createPolicy()](/en-US/docs/Web/API/TrustedTypePolicyFactory/createPolicy). We can then use [TrustedTypePolicy.createHTML](/en-US/docs/Web/API/TrustedTypePolicy/createHTML) to create a sanitized HTML string to be inserted into the document.

The sanitized value can then be used with [Element.innerHTML](/en-US/docs/Web/API/Element/innerHTML) to ensure that no new HTML elements can be injected.

html

```
<div id="myDiv"></div>
```

js

```
const escapeHTMLPolicy = trustedTypes.createPolicy("myEscapePolicy", {
  createHTML: (string) => string.replace(/</g, "&lt;"),
});

let el = document.getElementById("myDiv");
const escaped = escapeHTMLPolicy.createHTML("<img src=x onerror=alert(1)>");
console.log(escaped instanceof TrustedHTML); // true
el.innerHTML = escaped;
```

## [Specifications](#specifications)

Specification
[Trusted Types# trusted-type-policy](https://w3c.github.io/trusted-types/dist/spec/#trusted-type-policy)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 3, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/TrustedTypePolicy/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/trustedtypepolicy/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTrustedTypePolicy&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftrustedtypepolicy%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTrustedTypePolicy%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftrustedtypepolicy%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc7d5004cd6c5d5b1318f626425fcb06cb2c6a509%0A*+Document+last+modified%3A+2024-08-03T00%3A24%3A59.000Z%0A%0A%3C%2Fdetails%3E)
