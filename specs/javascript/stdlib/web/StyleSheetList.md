# StyleSheetList

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStyleSheetList&level=high)

The `StyleSheetList` interface represents a list of [CSSStyleSheet](/en-US/docs/Web/API/CSSStyleSheet) objects. An instance of this object can be returned by [Document.styleSheets](/en-US/docs/Web/API/Document/styleSheets).

It is an array-like object but can't be iterated over using [Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) methods. However it can be iterated over in a standard [for](/en-US/docs/Web/JavaScript/Reference/Statements/for) loop over its indices, or converted to an [Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array).

Note: Typically list interfaces like `StyleSheetList` wrap around [Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) types, so you can use `Array` methods on them. This is not the case here for [historical reasons](https://stackoverflow.com/questions/74630989/why-use-domstringlist-rather-than-an-array/74641156#74641156). However, you can convert `StyleSheetList` to an `Array` in order to use those methods (see the example below).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[StyleSheetList.length](/en-US/docs/Web/API/StyleSheetList/length)Read only

Returns the number of [CSSStyleSheet](/en-US/docs/Web/API/CSSStyleSheet) objects in the collection.

## [Instance methods](#instance_methods)

[StyleSheetList.item()](/en-US/docs/Web/API/StyleSheetList/item)

Returns the [CSSStyleSheet](/en-US/docs/Web/API/CSSStyleSheet) object at the index passed in, or `null` if no item exists for that index.

## [Examples](#examples)

### [Get CSSStyleSheet objects with for loop](#get_cssstylesheet_objects_with_for_loop)

js

```
for (const styleSheet of document.styleSheets) {
  console.log(styleSheet); // A CSSStyleSheet object
}
```

### [Get all CSS rules for the document using Array methods](#get_all_css_rules_for_the_document_using_array_methods)

js

```
const allCSS = [...document.styleSheets]
  .map((styleSheet) => {
    try {
      return [...styleSheet.cssRules].map((rule) => rule.cssText).join("");
    } catch (e) {
      console.log(
        "Access to stylesheet %s is denied. Ignoring…",
        styleSheet.href,
      );
      return undefined;
    }
  })
  .filter(Boolean)
  .join("\n");
```

## [Specifications](#specifications)

Specification
[CSS Object Model (CSSOM)# the-stylesheetlist-interface](https://drafts.csswg.org/cssom/#the-stylesheetlist-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/StyleSheetList/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/stylesheetlist/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStyleSheetList&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fstylesheetlist%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStyleSheetList%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fstylesheetlist%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb5437b737639d6952d18b95ebd1045ed73e4bfa7%0A*+Document+last+modified%3A+2025-05-27T11%3A11%3A59.000Z%0A%0A%3C%2Fdetails%3E)
