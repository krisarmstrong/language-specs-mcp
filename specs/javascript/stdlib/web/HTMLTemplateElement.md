# HTMLTemplateElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨November 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLTemplateElement&level=high)

The `HTMLTemplateElement` interface enables access to the contents of an HTML [<template>](/en-US/docs/Web/HTML/Reference/Elements/template) element.

Note: An HTML parser can create either an `HTMLTemplateElement` or a [ShadowRoot](/en-US/docs/Web/API/ShadowRoot) when it parses a [<template>](/en-US/docs/Web/HTML/Reference/Elements/template) element, depending on the `<template>` attributes. If an `HTMLTemplateElement` is created the "shadow" attributes are reflected from the template. However these are not useful, because an `HTMLTemplateElement` is not a shadow root and cannot subsequently be changed to a shadow root.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

This interface inherits the properties of [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[content](/en-US/docs/Web/API/HTMLTemplateElement/content)Read only

A read-only [DocumentFragment](/en-US/docs/Web/API/DocumentFragment) which contains the DOM subtree representing the [<template>](/en-US/docs/Web/HTML/Reference/Elements/template) element's template contents.

[shadowRootMode](/en-US/docs/Web/API/HTMLTemplateElement/shadowRootMode)

A string that reflects the value of the [shadowrootmode](/en-US/docs/Web/HTML/Reference/Elements/template#shadowrootmode) attribute of the associated `<template>` element.

[shadowRootDelegatesFocus](/en-US/docs/Web/API/HTMLTemplateElement/shadowRootDelegatesFocus)

A boolean that reflects the value of the [shadowrootdelegatesfocus](/en-US/docs/Web/HTML/Reference/Elements/template#shadowrootdelegatesfocus) attribute of the associated `<template>` element.

[shadowRootClonable](/en-US/docs/Web/API/HTMLTemplateElement/shadowRootClonable)

A boolean that reflects the value of the [shadowrootclonable](/en-US/docs/Web/HTML/Reference/Elements/template#shadowrootclonable) attribute of the associated `<template>` element.

[shadowRootSerializable](/en-US/docs/Web/API/HTMLTemplateElement/shadowRootSerializable)

A boolean that reflects the value of the [shadowrootserializable](/en-US/docs/Web/HTML/Reference/Elements/template#shadowrootserializable) attribute of the associated `<template>` element.

## [Instance methods](#instance_methods)

This interface inherits the methods of [HTMLElement](/en-US/docs/Web/API/HTMLElement).

## [Specifications](#specifications)

Specification
[HTML# htmltemplateelement](https://html.spec.whatwg.org/multipage/scripting.html#htmltemplateelement)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 10, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLTemplateElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmltemplateelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLTemplateElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmltemplateelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLTemplateElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmltemplateelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe9b6cd1b7fa8612257b72b2a85a96dd7d45c0200%0A*+Document+last+modified%3A+2025-04-10T14%3A56%3A07.000Z%0A%0A%3C%2Fdetails%3E)
