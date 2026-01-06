# MathMLElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2023⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMathMLElement&level=high)

The `MathMLElement` interface represents any [MathML](/en-US/docs/Web/MathML) element.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Also inherits properties from its parent, [Element](/en-US/docs/Web/API/Element).

[MathMLElement.attributeStyleMap](/en-US/docs/Web/API/MathMLElement/attributeStyleMap)Read only

A [StylePropertyMap](/en-US/docs/Web/API/StylePropertyMap) representing the declarations of the element's `style` attribute.

[MathMLElement.autofocus](/en-US/docs/Web/API/MathMLElement/autofocus)

Whether the control should be focused when the page loads, or when a [<dialog>](/en-US/docs/Web/HTML/Reference/Elements/dialog) or [popover](/en-US/docs/Web/HTML/Reference/Global_attributes/popover) become shown.

[MathMLElement.dataset](/en-US/docs/Web/API/MathMLElement/dataset)Read only

A [DOMStringMap](/en-US/docs/Web/API/DOMStringMap) object which provides a list of key/value pairs of named data attributes which correspond to [custom data attributes](/en-US/docs/Web/HTML/How_to/Use_data_attributes) attached to the element. These correspond to MathML's [data-*](/en-US/docs/Web/MathML/Reference/Global_attributes/data-*) global attributes.

[MathMLElement.style](/en-US/docs/Web/API/MathMLElement/style)

A [CSSStyleDeclaration](/en-US/docs/Web/API/CSSStyleDeclaration) representing the declarations of the element's `style` attribute.

[MathMLElement.tabIndex](/en-US/docs/Web/API/MathMLElement/tabIndex)

The position of the element in the tabbing order.

## [Instance methods](#instance_methods)

This interface also inherits methods from its parent, [Element](/en-US/docs/Web/API/Element).

[MathMLElement.blur()](/en-US/docs/Web/API/MathMLElement/blur)

Removes keyboard focus from the currently focused element.

[MathMLElement.focus()](/en-US/docs/Web/API/MathMLElement/focus)

Makes the element the current keyboard focus.

## [Examples](#examples)

### [MathML](#mathml)

html

```
<math>
  <msqrt>
    <mi>x</mi>
  </msqrt>
</math>
```

### [JavaScript](#javascript)

js

```
document.querySelector("msqrt").constructor.name; // MathMLElement
```

## [Specifications](#specifications)

Specification
[MathML Core# dom-mathmlelement](https://w3c.github.io/mathml-core/#dom-mathmlelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Element](/en-US/docs/Web/API/Element)
- [HTMLElement](/en-US/docs/Web/API/HTMLElement)
- [SVGElement](/en-US/docs/Web/API/SVGElement)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 9, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/MathMLElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mathmlelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMathMLElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmathmlelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMathMLElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmathmlelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5f4ef6f614202ab1b748708d3e1d95e396f6ee63%0A*+Document+last+modified%3A+2025-10-09T02%3A46%3A39.000Z%0A%0A%3C%2Fdetails%3E)
