# XPathExpression

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXPathExpression&level=high)

This interface is a compiled XPath expression that can be evaluated on a document or specific node to return information from its [DOM](/en-US/docs/Glossary/DOM) tree.

This is useful when an expression will be reused in an application, because it is just compiled once and all namespace prefixes which occur within the expression are preresolved.

Objects of this type are created by calling [XPathEvaluator.createExpression()](/en-US/docs/Web/API/XPathEvaluator/createExpression).

## In this article

- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

[XPathExpression.evaluate()](/en-US/docs/Web/API/XPathExpression/evaluate)

Evaluates the XPath expression on the given node or document.

## [Example](#example)

The following example shows the use of the `XPathExpression` interface.

### [HTML](#html)

html

```
<div>XPath example</div>
<div>Number of &lt;div&gt;s: <output></output></div>
```

### [JavaScript](#javascript)

js

```
const xpath = "//div";
const evaluator = new XPathEvaluator();
const expression = evaluator.createExpression(xpath);
const result = expression.evaluate(
  document,
  XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,
);
document.querySelector("output").textContent = result.snapshotLength;
```

### [Result](#result)

## [Specifications](#specifications)

Specification
[DOM# interface-xpathexpression](https://dom.spec.whatwg.org/#interface-xpathexpression)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [document.createExpression()](/en-US/docs/Web/API/Document/createExpression)
- [XPathResult](/en-US/docs/Web/API/XPathResult)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 7, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/XPathExpression/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xpathexpression/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXPathExpression&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxpathexpression%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXPathExpression%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxpathexpression%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Facfe8c9f1f4145f77653a2bc64a9744b001358dc%0A*+Document+last+modified%3A+2023-07-07T07%3A19%3A19.000Z%0A%0A%3C%2Fdetails%3E)
