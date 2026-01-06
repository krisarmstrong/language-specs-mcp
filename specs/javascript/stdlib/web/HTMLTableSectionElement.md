# HTMLTableSectionElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLTableSectionElement&level=high)

The `HTMLTableSectionElement` interface provides special properties and methods (beyond the [HTMLElement](/en-US/docs/Web/API/HTMLElement) interface it also has available to it by inheritance) for manipulating the layout and presentation of sections, that is headers, footers and bodies ([<thead>](/en-US/docs/Web/HTML/Reference/Elements/thead), [<tfoot>](/en-US/docs/Web/HTML/Reference/Elements/tfoot), and [<tbody>](/en-US/docs/Web/HTML/Reference/Elements/tbody), respectively) in an HTML table.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLTableSectionElement.align](/en-US/docs/Web/API/HTMLTableSectionElement/align)Deprecated

A string containing an enumerated value reflecting the [align](/en-US/docs/Web/HTML/Reference/Elements/tr#align) attribute. It indicates the alignment of the element's contents with respect to the surrounding context. The possible values are `"left"`, `"right"`, and `"center"`.

[HTMLTableSectionElement.rows](/en-US/docs/Web/API/HTMLTableSectionElement/rows)Read only

Returns a live [HTMLCollection](/en-US/docs/Web/API/HTMLCollection) containing the rows in the section. The `HTMLCollection` is live and is automatically updated when rows are added or removed.

[HTMLTableSectionElement.ch](/en-US/docs/Web/API/HTMLTableSectionElement/ch)Deprecated

A string containing one single character. This character is the one to align all the cell of a column on. It reflects the [char](/en-US/docs/Web/HTML/Reference/Elements/tr#char) and default to the decimal points associated with the language, e.g., `'.'` for English, or `','` for French. This property was optional and was not very well supported.

[HTMLTableSectionElement.chOff](/en-US/docs/Web/API/HTMLTableSectionElement/chOff)Deprecated

A string containing an integer indicating how many characters must be left at the right (for left-to-right scripts; or at the left for right-to-left scripts) of the character defined by `HTMLTableRowElement.ch`. This property was optional and was not very well supported.

[HTMLTableSectionElement.vAlign](/en-US/docs/Web/API/HTMLTableSectionElement/vAlign)Deprecated

A string representing an enumerated value indicating how the content of the cell must be vertically aligned. It reflects the [valign](/en-US/docs/Web/HTML/Reference/Elements/tr#valign) attribute and can have one of the following values: `"top"`, `"middle"`, `"bottom"`, or `"baseline"`.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLTableSectionElement.deleteRow()](/en-US/docs/Web/API/HTMLTableSectionElement/deleteRow)

Removes the row, corresponding to the `index` given in parameter, in the section. If the `index` value is `-1` the last row is removed; if it smaller than `-1` or greater than the amount of rows in the collection, a [DOMException](/en-US/docs/Web/API/DOMException) with the value `IndexSizeError` is raised.

[HTMLTableSectionElement.insertRow()](/en-US/docs/Web/API/HTMLTableSectionElement/insertRow)

Returns an [HTMLTableRowElement](/en-US/docs/Web/API/HTMLTableRowElement) representing a new row of the section. It inserts it in the rows collection immediately before the [<tr>](/en-US/docs/Web/HTML/Reference/Elements/tr) element at the given `index` position. If the `index` is `-1`, the new row is appended to the collection. If the `index` is smaller than `-1` or greater than the number of rows in the collection, a [DOMException](/en-US/docs/Web/API/DOMException) with the value `IndexSizeError` is raised.

## [Specifications](#specifications)

Specification
[HTML# htmltablesectionelement](https://html.spec.whatwg.org/multipage/tables.html#htmltablesectionelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The HTML elements implementing this interface: [<tfoot>](/en-US/docs/Web/HTML/Reference/Elements/tfoot), [<thead>](/en-US/docs/Web/HTML/Reference/Elements/thead), and [<tbody>](/en-US/docs/Web/HTML/Reference/Elements/tbody).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 10, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLTableSectionElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmltablesectionelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLTableSectionElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmltablesectionelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLTableSectionElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmltablesectionelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe9b6cd1b7fa8612257b72b2a85a96dd7d45c0200%0A*+Document+last+modified%3A+2025-04-10T14%3A56%3A07.000Z%0A%0A%3C%2Fdetails%3E)
