# XPathEvaluator

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXPathEvaluator&level=high)

The `XPathEvaluator` interface allows to compile and evaluate [XPath](/en-US/docs/Glossary/XPath) expressions.

## In this article

- [Constructor](#constructor)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[XPathEvaluator()](/en-US/docs/Web/API/XPathEvaluator/XPathEvaluator)

Creates a new `XPathEvaluator` object.

## [Instance methods](#instance_methods)

[XPathEvaluator.createExpression()](/en-US/docs/Web/API/XPathEvaluator/createExpression)

Creates a parsed XPath expression with resolved namespaces.

[XPathEvaluator.createNSResolver()](/en-US/docs/Web/API/XPathEvaluator/createNSResolver)Deprecated

Returns the input as-is.

[XPathEvaluator.evaluate()](/en-US/docs/Web/API/XPathEvaluator/evaluate)

Evaluates an XPath expression string and returns a result of the specified type if possible.

## [Example](#example)

### [Count the number of <div> elements](#count_the_number_of_div_elements)

The following example shows the use of the `XPathEvaluator` interface.

#### HTML

html

```
<div>XPath example</div>
<div>Number of &lt;div&gt; elements: <output></output></div>
```

#### JavaScript

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

#### Result

## [Specifications](#specifications)

Specification
[DOM# interface-xpathevaluator](https://dom.spec.whatwg.org/#interface-xpathevaluator)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [document.createExpression()](/en-US/docs/Web/API/Document/createExpression)
- [XPathExpression](/en-US/docs/Web/API/XPathExpression)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 25, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/XPathEvaluator/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xpathevaluator/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXPathEvaluator&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxpathevaluator%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXPathEvaluator%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxpathevaluator%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa7265fc3effa7c25b9997135104370c057a65293%0A*+Document+last+modified%3A+2025-09-25T16%3A11%3A52.000Z%0A%0A%3C%2Fdetails%3E)
