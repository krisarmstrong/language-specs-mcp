# SecurityPolicyViolationEvent

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨October 2018⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSecurityPolicyViolationEvent&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `SecurityPolicyViolationEvent` interface inherits from [Event](/en-US/docs/Web/API/Event), and represents the event object of a `securitypolicyviolation` event sent on an [Element](/en-US/docs/Web/API/Element/securitypolicyviolation_event), [Document](/en-US/docs/Web/API/Document/securitypolicyviolation_event), or [worker](/en-US/docs/Web/API/WorkerGlobalScope/securitypolicyviolation_event) when its [Content Security Policy (CSP)](/en-US/docs/Web/HTTP/Guides/CSP) is violated.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[SecurityPolicyViolationEvent()](/en-US/docs/Web/API/SecurityPolicyViolationEvent/SecurityPolicyViolationEvent)

Creates a new `SecurityPolicyViolationEvent` object instance.

## [Instance properties](#instance_properties)

[SecurityPolicyViolationEvent.blockedURI](/en-US/docs/Web/API/SecurityPolicyViolationEvent/blockedURI)Read only

A string representing the URI of the resource that was blocked because it violates a policy.

[SecurityPolicyViolationEvent.columnNumber](/en-US/docs/Web/API/SecurityPolicyViolationEvent/columnNumber)Read only

The column number in the document or worker at which the violation occurred.

[SecurityPolicyViolationEvent.disposition](/en-US/docs/Web/API/SecurityPolicyViolationEvent/disposition)Read only

A string indicating whether the user agent is configured to enforce or just report the policy violation.

[SecurityPolicyViolationEvent.documentURI](/en-US/docs/Web/API/SecurityPolicyViolationEvent/documentURI)Read only

A string representing the URI of the document or worker in which the violation occurred.

[SecurityPolicyViolationEvent.effectiveDirective](/en-US/docs/Web/API/SecurityPolicyViolationEvent/effectiveDirective)Read only

A string representing the directive that was violated.

[SecurityPolicyViolationEvent.lineNumber](/en-US/docs/Web/API/SecurityPolicyViolationEvent/lineNumber)Read only

The line number in the document or worker at which the violation occurred.

[SecurityPolicyViolationEvent.originalPolicy](/en-US/docs/Web/API/SecurityPolicyViolationEvent/originalPolicy)Read only

A string containing the policy whose enforcement caused the violation.

[SecurityPolicyViolationEvent.referrer](/en-US/docs/Web/API/SecurityPolicyViolationEvent/referrer)Read only

A string representing the URL for the referrer of the resources whose policy was violated, or `null`.

[SecurityPolicyViolationEvent.sample](/en-US/docs/Web/API/SecurityPolicyViolationEvent/sample)Read only

A string representing a sample of the resource that caused the violation, usually the first 40 characters. This will only be populated if the resource is an inline script, event handler, or style — external resources causing a violation will not generate a sample.

[SecurityPolicyViolationEvent.sourceFile](/en-US/docs/Web/API/SecurityPolicyViolationEvent/sourceFile)Read only

If the violation occurred as a result of a script, this will be the URL of the script; otherwise, it will be `null`. Both `columnNumber` and `lineNumber` should have non-null values if this property is not `null`.

[SecurityPolicyViolationEvent.statusCode](/en-US/docs/Web/API/SecurityPolicyViolationEvent/statusCode)Read only

A number representing the HTTP status code of the document or worker in which the violation occurred.

[SecurityPolicyViolationEvent.violatedDirective](/en-US/docs/Web/API/SecurityPolicyViolationEvent/violatedDirective)Read only

A string representing the directive that was violated. This is a historical alias of [effectiveDirective](/en-US/docs/Web/API/SecurityPolicyViolationEvent/effectiveDirective).

## [Examples](#examples)

js

```
document.addEventListener("securitypolicyviolation", (e) => {
  console.log(e.blockedURI);
  console.log(e.violatedDirective);
  console.log(e.originalPolicy);
});
```

## [Specifications](#specifications)

Specification
[Content Security Policy Level 3# report-violation](https://w3c.github.io/webappsec-csp/#report-violation)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- HTTP [Content Security Policy (CSP)](/en-US/docs/Web/HTTP/Guides/CSP)
- [CSPViolationReportBody](/en-US/docs/Web/API/CSPViolationReportBody)
- The [securitypolicyviolation](/en-US/docs/Web/API/Element/securitypolicyviolation_event) event of the [Element](/en-US/docs/Web/API/Element) interface
- The [securitypolicyviolation](/en-US/docs/Web/API/Document/securitypolicyviolation_event) event of the [Document](/en-US/docs/Web/API/Document) interface
- The [securitypolicyviolation](/en-US/docs/Web/API/WorkerGlobalScope/securitypolicyviolation_event) event of the [WorkerGlobalScope](/en-US/docs/Web/API/WorkerGlobalScope) interface

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 25, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SecurityPolicyViolationEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/securitypolicyviolationevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSecurityPolicyViolationEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsecuritypolicyviolationevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSecurityPolicyViolationEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsecuritypolicyviolationevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F515d03ad8572b96e88916888156444626dcba193%0A*+Document+last+modified%3A+2025-03-25T03%3A39%3A37.000Z%0A%0A%3C%2Fdetails%3E)
