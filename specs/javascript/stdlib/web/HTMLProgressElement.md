# HTMLProgressElement

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLProgressElement&level=high)

The `HTMLProgressElement` interface provides special properties and methods (beyond the regular [HTMLElement](/en-US/docs/Web/API/HTMLElement) interface it also has available to it by inheritance) for manipulating the layout and presentation of [<progress>](/en-US/docs/Web/HTML/Reference/Elements/progress) elements.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLProgressElement.max](/en-US/docs/Web/API/HTMLProgressElement/max)

A `double` value reflecting the content attribute of the same name, limited to numbers greater than zero. Its default value is `1.0`.

[HTMLProgressElement.position](/en-US/docs/Web/API/HTMLProgressElement/position)Read only

Returns a `double` value returning the result of dividing the current value (`value`) by the maximum value (`max`); if the progress bar is an indeterminate progress bar, it returns `-1`.

[HTMLProgressElement.value](/en-US/docs/Web/API/HTMLProgressElement/value)

A `double` value that reflects the current value; if the progress bar is an indeterminate progress bar, it returns `0`.

[HTMLProgressElement.labels](/en-US/docs/Web/API/HTMLProgressElement/labels)Read only

Returns [NodeList](/en-US/docs/Web/API/NodeList) containing the list of [<label>](/en-US/docs/Web/HTML/Reference/Elements/label) elements that are labels for this element.

## [Instance methods](#instance_methods)

No specific method; inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

## [Specifications](#specifications)

Specification
[HTML# htmlprogresselement](https://html.spec.whatwg.org/multipage/form-elements.html#htmlprogresselement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The HTML element implementing this interface: [<progress>](/en-US/docs/Web/HTML/Reference/Elements/progress)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 20, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLProgressElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlprogresselement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLProgressElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlprogresselement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLProgressElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlprogresselement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F387d0d4d8690c0d2c9db1b85eae28ffea0f3ac1f%0A*+Document+last+modified%3A+2023-02-20T04%3A32%3A55.000Z%0A%0A%3C%2Fdetails%3E)
