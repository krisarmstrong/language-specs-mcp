# BarProp

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBarProp&level=high)

The `BarProp` interface of the [Document Object Model](/en-US/docs/Web/API/Document_Object_Model) represents the web browser user interface elements that are exposed to scripts in web pages. Each of the following interface elements are represented by a `BarProp` object.

[Window.locationbar](/en-US/docs/Web/API/Window/locationbar)

The browser location bar.

[Window.menubar](/en-US/docs/Web/API/Window/menubar)

The browser menu bar.

[Window.personalbar](/en-US/docs/Web/API/Window/personalbar)

The browser personal bar.

[Window.scrollbars](/en-US/docs/Web/API/Window/scrollbars)

The browser scrollbars.

[Window.statusbar](/en-US/docs/Web/API/Window/statusbar)

The browser status bar.

[Window.toolbar](/en-US/docs/Web/API/Window/toolbar)

The browser toolbar.

The `BarProp` interface is not accessed directly, but via one of these elements.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[BarProp.visible](/en-US/docs/Web/API/BarProp/visible)Read only

A [Boolean](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean), which is true if the bar represented by the used interface element is visible.

## [Examples](#examples)

The following example prints a `BarProp` object to the console that represents the location bar.

js

```
console.log(window.locationbar);
```

## [Specifications](#specifications)

Specification
[HTML# barprop](https://html.spec.whatwg.org/multipage/nav-history-apis.html#barprop)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 25, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/BarProp/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/barprop/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBarProp&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbarprop%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBarProp%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbarprop%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4675b9077ae32f989c7ecac94f454db2653c4fc%0A*+Document+last+modified%3A+2024-07-25T22%3A06%3A52.000Z%0A%0A%3C%2Fdetails%3E)
