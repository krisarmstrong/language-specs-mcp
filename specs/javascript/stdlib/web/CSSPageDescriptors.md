# CSSPageDescriptors

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSPageDescriptors&level=not)

The `CSSPageDescriptors` interface represents a CSS declaration block for an [@page](/en-US/docs/Web/CSS/Reference/At-rules/@page)[at-rule](/en-US/docs/Web/CSS/Guides/Syntax/At-rules).

The interface exposes style information and various style-related methods and properties for the page. Each multi-word property has versions in camel- and snake-case. This means, for example, that you can access the `margin-top` CSS property using the syntax `style["margin-top"]` or `style.marginTop` (where `style` is a `CSSPageDescriptor`).

A `CSSPageDescriptors` object is accessed through the [style](/en-US/docs/Web/API/CSSPageRule/style) property of the `CSSPageRule` interface, which can in turn be found using the [CSSStyleSheet](/en-US/docs/Web/API/CSSStyleSheet) API.

## In this article

- [Attributes](#attributes)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Attributes](#attributes)

This interface also inherits properties of its parent, [CSSStyleDeclaration](/en-US/docs/Web/API/CSSStyleDeclaration).

[margin](#margin)

A string representing the `margin` property of the corresponding `@page` at-rule.

[margin-top](#margin-top)

A string representing the `margin-top` property of the corresponding `@page` at-rule.

[marginTop](#margintop)

A string representing the `margin-top` property of the corresponding `@page` at-rule.

[margin-right](#margin-right)

A string representing the `margin-right` property of the corresponding `@page` at-rule.

[marginRight](#marginright)

A string representing the `margin-right` property of the corresponding `@page` at-rule.

[margin-bottom](#margin-bottom)

A string representing the `margin-bottom` property of the corresponding `@page` at-rule.

[marginBottom](#marginbottom)

A string representing the `margin-bottom` property of the corresponding `@page` at-rule.

[margin-left](#margin-left)

A string representing the `margin-left` property of the corresponding `@page` at-rule.

[marginLeft](#marginleft)

A string representing the `margin-left` property of the corresponding `@page` at-rule.

[page-orientation 
Experimental](#page-orientation)

A string representing the `page-orientation` property of the corresponding `@page` at-rule.

[pageOrientation 
Experimental](#pageorientation)

A string representing the `page-orientation` property of the corresponding `@page` at-rule.

[size](#size)

A string representing the `size` property of the corresponding `@page` at-rule.

## [Instance methods](#instance_methods)

This interface inherits the methods of its parent, [CSSStyleDeclaration](/en-US/docs/Web/API/CSSStyleDeclaration).

## [Examples](#examples)

### [Inspecting a page at-rule](#inspecting_a_page_at-rule)

This example gets the `CSSPageDescriptors` for a [@page](/en-US/docs/Web/CSS/Reference/At-rules/@page) at-rule, if the object is supported on the browser, and then logs its properties.

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
  height: 280px;
  overflow: scroll;
  padding: 0.5rem;
  border: 1px solid black;
}
```

#### CSS

Below we define styles for the page using a [@page](/en-US/docs/Web/CSS/Reference/At-rules/@page) at-rule. We assign different values for each margin property using the `margin` shorthand, and also specify the `size`. We don't set the `page-orientation`. This allows us to see how the properties map in the Web API object.

css

```
@page {
  margin: 1cm 2px 3px 4px;
  /* page-orientation: upright; */
  size: A4;
}
```

#### JavaScript

First we check if `CSSPageDescriptors` is defined on the global window object, and if not we log that the interface is not supported.

If `CSSPageDescriptors` is supported, we get the target stylesheet, and then gets the `cssRules` defined in that stylesheet. We need to get this stylesheet because the example is embedded in a separate frame with its own sheet (index `0` is the CSS for this page).

We then iterate through the rules defined for the live example and match any that are of type `CSSPageRule`, as these correspond to `@page` rules. For the matching objects we then log the `style` and all its values.

js

```
if (typeof window.CSSPageDescriptors === "undefined") {
  log("CSSPageDescriptors is not supported on this browser.");
} else {
  // Get stylesheets for example and then get its cssRules
  const myRules = document.getElementById("css-output").sheet.cssRules;
  for (const rule of myRules) {
    if (rule instanceof CSSPageRule) {
      log(`${rule.style}`);
      log(`margin: ${rule.style.margin}`);

      // Access properties using CamelCase syntax
      log(`marginTop: ${rule.style.marginTop}`);
      log(`marginRight: ${rule.style.marginRight}`);
      log(`marginBottom: ${rule.style.marginBottom}`);
      log(`marginLeft: ${rule.style.marginLeft}`);
      log(`pageOrientation: ${rule.style.pageOrientation}`);

      // Access properties using snake-case syntax
      log(`margin-top: ${rule.style["margin-top"]}`);
      log(`margin-right: ${rule.style["margin-right"]}`);
      log(`margin-left: ${rule.style["margin-left"]}`);
      log(`margin-bottom: ${rule.style["margin-bottom"]}`);
      log(`page-orientation: ${rule.style["page-orientation"]}`);

      log(`size: ${rule.style.size}`);

      // Log the original CSS text using inherited property: cssText
      log(`cssText: ${rule.style.cssText}`);
      log("\n");
    }
  }
}
```

#### Results

The results are shown below. Note that the `style` object displayed at the top of the log should be a `CSSPageDescriptors` to match the current specification, but may be a `CSSStyleDeclaration` in some browsers. Note also that the corresponding values for properties in camel- and snake-case match each other and the `@page` declaration, and that `page-orientation` is the empty string `""` because it is not defined in `@page`.

## [Specifications](#specifications)

Specification
[CSS Object Model (CSSOM)# csspagedescriptors](https://drafts.csswg.org/cssom/#csspagedescriptors)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSPageDescriptors/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/csspagedescriptors/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSPageDescriptors&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcsspagedescriptors%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSPageDescriptors%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcsspagedescriptors%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
