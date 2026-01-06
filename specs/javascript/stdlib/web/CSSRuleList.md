# CSSRuleList

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSRuleList&level=high)

A `CSSRuleList` represents an ordered collection of read-only [CSSRule](/en-US/docs/Web/API/CSSRule) objects.

While the `CSSRuleList` object is read-only, and cannot be directly modified, it is considered a `live` object, as the content can change over time.

To edit the underlying rules returned by `CSSRule` objects, use [CSSStyleSheet.insertRule()](/en-US/docs/Web/API/CSSStyleSheet/insertRule) and [CSSStyleSheet.deleteRule()](/en-US/docs/Web/API/CSSStyleSheet/deleteRule), which are methods of [CSSStyleSheet](/en-US/docs/Web/API/CSSStyleSheet).

This interface was an [attempt to create an unmodifiable list](https://stackoverflow.com/questions/74630989/why-use-domstringlist-rather-than-an-array/74641156#74641156) and only continues to be supported to not break code that's already using it. Modern APIs represent list structures using types based on JavaScript [arrays](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array), thus making many array methods available, and at the same time imposing additional semantics on their usage (such as making their items read-only).

These historical reasons do not mean that you as a developer should avoid `CSSRuleList`. You don't create `CSSRuleList` objects yourself, but you get them from APIs such as [CSSStyleSheet.cssRules](/en-US/docs/Web/API/CSSStyleSheet/cssRules) and [CSSKeyframesRule.cssRules](/en-US/docs/Web/API/CSSKeyframesRule/cssRules), and these APIs are not deprecated. However, be careful of the semantic differences from a real array.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[CSSRuleList.length](/en-US/docs/Web/API/CSSRuleList/length)Read only

Returns an integer representing the number of [CSSRule](/en-US/docs/Web/API/CSSRule) objects in the collection.

## [Instance methods](#instance_methods)

[CSSRuleList.item()](/en-US/docs/Web/API/CSSRuleList/item)

Gets a single [CSSRule](/en-US/docs/Web/API/CSSRule).

## [Examples](#examples)

In the following example there is a stylesheet with three rules. Using [CSSStyleSheet.cssRules](/en-US/docs/Web/API/CSSStyleSheet/cssRules) returns a `CSSRuleList`, which is printed to the console.

The number of rules in the list is printed to the console using [CSSRuleList.length](/en-US/docs/Web/API/CSSRuleList/length). The first [CSSRule](/en-US/docs/Web/API/CSSRule) can be returned by using `0` as the parameter for [CSSRuleList.item](/en-US/docs/Web/API/CSSRuleList/item), in the example this will return the rules set for the `body` selector.

### [CSS](#css)

css

```
body {
  font-family:
    system-ui,
    -apple-system,
    sans-serif;
  margin: 2em;
}

.container {
  display: grid;
  grid-template-columns: repeat(auto-fill, 200px);
}

.container > * {
  background-color: #3740ff;
  color: white;
}
```

### [JavaScript](#javascript)

js

```
let myRules = document.styleSheets[0].cssRules;
console.log(myRules);
console.log(myRules.length);
console.log(myRules[0]);
```

## [Specifications](#specifications)

Specification
[CSS Object Model (CSSOM)# the-cssrulelist-interface](https://drafts.csswg.org/cssom/#the-cssrulelist-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [CSSRule](/en-US/docs/Web/API/CSSRule)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSRuleList/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cssrulelist/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSRuleList&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcssrulelist%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSRuleList%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcssrulelist%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5f2a755c4fa7d126f85b56fbca90b15c5f039eff%0A*+Document+last+modified%3A+2025-08-08T16%3A55%3A34.000Z%0A%0A%3C%2Fdetails%3E)
