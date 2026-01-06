# CSSPageRule

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSPageRule&level=high)

`CSSPageRule` represents a single CSS [@page](/en-US/docs/Web/CSS/Reference/At-rules/@page) rule.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

Inherits properties from its ancestors [CSSGroupingRule](/en-US/docs/Web/API/CSSGroupingRule) and [CSSRule](/en-US/docs/Web/API/CSSRule).

[CSSPageRule.selectorText](/en-US/docs/Web/API/CSSPageRule/selectorText)

Represents the text of the page selector associated with the at-rule.

[CSSPageRule.style](/en-US/docs/Web/API/CSSPageRule/style)Read only

Returns the [declaration block](/en-US/docs/Web/API/CSS_Object_Model/CSS_Declaration_Block) associated with the at-rule.

## [Instance methods](#instance_methods)

Inherits methods from its ancestors [CSSGroupingRule](/en-US/docs/Web/API/CSSGroupingRule) and [CSSRule](/en-US/docs/Web/API/CSSRule).

## [Examples](#examples)

### [Filtering for page rules](#filtering_for_page_rules)

This example shows how you can find `CSSPageRule` objects for [@page](/en-US/docs/Web/CSS/Reference/At-rules/@page) rules loaded by the document.

```
<pre id="log"></pre>
```

```
const logElement = document.querySelector("#log");
function log(text) {
  logElement.innerText = `${logElement.innerText}${text}\n`;
  logElement.scrollTop = logElement.scrollHeight;
}
```

```
#log {
  height: 220px;
  overflow: scroll;
  padding: 0.5rem;
  border: 1px solid black;
}
```

#### CSS

Below we define styles for the page using a [@page](/en-US/docs/Web/CSS/Reference/At-rules/@page) rule.

css

```
@page {
  margin: 1cm;
}
```

#### JavaScript

The code iterates through all the sheets in the document, and through all the `cssRules` in each sheet, logging the sheet index, the number of rules, and the type of each rule object. We then detect `CSSPageRule` objects using their type (doing nothing with the information).

js

```
for (
  let sheetCount = 0;
  sheetCount < document.styleSheets.length;
  sheetCount++
) {
  const sheet = document.styleSheets[sheetCount].cssRules;
  log(`styleSheet: ${sheetCount}`);

  const myRules = document.styleSheets[sheetCount].cssRules;
  log(`rules: ${myRules.length}`);
  for (const rule of myRules) {
    log(`rule: ${rule}`);
    if (rule instanceof CSSPageRule) {
      // Do something with CSSPageRule
    }
  }
}
```

#### Results

The results are shown below. As you can see there are a two sheets, corresponding to this main document and the example code frame, and each have a number of rules, only one of which is our `CSSPageRule`.

## [Specifications](#specifications)

Specification
[CSS Object Model (CSSOM)# the-csspagerule-interface](https://drafts.csswg.org/cssom/#the-csspagerule-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSPageRule/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/csspagerule/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSPageRule&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcsspagerule%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSPageRule%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcsspagerule%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb5437b737639d6952d18b95ebd1045ed73e4bfa7%0A*+Document+last+modified%3A+2025-05-27T11%3A11%3A59.000Z%0A%0A%3C%2Fdetails%3E)
