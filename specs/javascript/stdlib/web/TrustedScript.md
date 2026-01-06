# TrustedScript

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTrustedScript&level=not)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `TrustedScript` interface of the [Trusted Types API](/en-US/docs/Web/API/Trusted_Types_API) represents a string with an uncompiled script body that a developer can insert into an [injection sink](/en-US/docs/Web/API/Trusted_Types_API#concepts_and_usage) that might execute the script. These objects are created via [TrustedTypePolicy.createScript()](/en-US/docs/Web/API/TrustedTypePolicy/createScript) and therefore have no constructor.

The value of a TrustedScript object is set when the object is created and cannot be changed by JavaScript as there is no setter exposed.

## In this article

- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

[TrustedScript.toJSON()](/en-US/docs/Web/API/TrustedScript/toJSON)

Returns a JSON representation of the stored data.

[TrustedScript.toString()](/en-US/docs/Web/API/TrustedScript/toString)

A string containing the sanitized script.

## [Examples](#examples)

The constant `sanitized` is an object created via a Trusted Types policy.

js

```
const sanitized = scriptPolicy.createScript("eval('2 + 2')");
console.log(sanitized); /* a TrustedScript object */
```

## [Specifications](#specifications)

Specification
[Trusted Types# trusted-script](https://w3c.github.io/trusted-types/dist/spec/#trusted-script)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Prevent DOM-based cross-site scripting vulnerabilities with Trusted Types](https://web.dev/articles/trusted-types)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 10, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/TrustedScript/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/trustedscript/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTrustedScript&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftrustedscript%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTrustedScript%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftrustedscript%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3ceedbd90089cfb6970c9bf63ff9e6f3801fcbc5%0A*+Document+last+modified%3A+2025-03-10T22%3A50%3A18.000Z%0A%0A%3C%2Fdetails%3E)
