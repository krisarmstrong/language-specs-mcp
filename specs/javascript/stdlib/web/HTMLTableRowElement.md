# HTMLTableRowElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLTableRowElement&level=high)

The `HTMLTableRowElement` interface provides special properties and methods (beyond the [HTMLElement](/en-US/docs/Web/API/HTMLElement) interface it also has available to it by inheritance) for manipulating the layout and presentation of rows in an HTML table.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Deprecated properties](#deprecated_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLTableRowElement.cells](/en-US/docs/Web/API/HTMLTableRowElement/cells)Read only

Returns a live [HTMLCollection](/en-US/docs/Web/API/HTMLCollection) containing the cells in the row. The `HTMLCollection` is live and is automatically updated when cells are added or removed.

[HTMLTableRowElement.rowIndex](/en-US/docs/Web/API/HTMLTableRowElement/rowIndex)Read only

Returns a number that gives the logical position of the row within the entire table. If the row is not part of a table, returns `-1`.

[HTMLTableRowElement.sectionRowIndex](/en-US/docs/Web/API/HTMLTableRowElement/sectionRowIndex)Read only

Returns a number that gives the logical position of the row within the table section it belongs to. If the row is not part of a section, returns `-1`.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLTableRowElement.deleteCell()](/en-US/docs/Web/API/HTMLTableRowElement/deleteCell)

Removes the cell corresponding to `index`. If `index` is `-1`, the last cell of the row is removed. If `index` is less than `-1` or greater than the amount of cells in the collection, a [DOMException](/en-US/docs/Web/API/DOMException) with the value `IndexSizeError` is raised.

[HTMLTableRowElement.insertCell()](/en-US/docs/Web/API/HTMLTableRowElement/insertCell)

Returns an [HTMLTableCellElement](/en-US/docs/Web/API/HTMLTableCellElement) representing a new cell of the row. The cell is inserted in the collection of cells immediately before the given `index` position in the row. If `index` is `-1`, the new cell is appended to the collection. If `index` is less than `-1` or greater than the number of cells in the collection, a [DOMException](/en-US/docs/Web/API/DOMException) with the value `IndexSizeError` is raised.

## [Deprecated properties](#deprecated_properties)

Warning: These properties have been deprecated and should no longer be used. They are documented primarily to help understand older code bases.

[HTMLTableRowElement.align](/en-US/docs/Web/API/HTMLTableRowElement/align)Deprecated

A string containing an enumerated value reflecting the [align](/en-US/docs/Web/HTML/Reference/Elements/tr#align) attribute. It indicates the alignment of the element's contents to the surrounding context. The possible values are `"left"`, `"right"`, and `"center"`.

[HTMLTableRowElement.bgColor](/en-US/docs/Web/API/HTMLTableRowElement/bgColor)Deprecated

A string containing the background color of the cells. It reflects the obsolete [bgColor](/en-US/docs/Web/HTML/Reference/Elements/tr#bgcolor) attribute.

[HTMLTableRowElement.ch](/en-US/docs/Web/API/HTMLTableRowElement/ch)Deprecated

A string containing one single character. This character is the one to align all the cell of a column on. It reflects the [char](/en-US/docs/Web/HTML/Reference/Elements/tr#char) and defaults to the decimal points associated with the language, e.g., `'.'` for English, or `','` for French. This property was optional and was not very well supported.

[HTMLTableRowElement.chOff](/en-US/docs/Web/API/HTMLTableRowElement/chOff)Deprecated

A string containing an integer indicating how many characters must be left at the right (for left-to-right scripts; or at the left for right-to-left scripts) of the character defined by `HTMLTableRowElement.ch`. This property was optional and was not very well supported.

[HTMLTableRowElement.vAlign](/en-US/docs/Web/API/HTMLTableRowElement/vAlign)Deprecated

A string representing an enumerated value indicating how the content of the cell must be vertically aligned. It reflects the [valign](/en-US/docs/Web/HTML/Reference/Elements/tr#valign) attribute and can have one of the following values: `"top"`, `"middle"`, `"bottom"`, or `"baseline"`.

## [Specifications](#specifications)

Specification
[HTML# htmltablerowelement](https://html.spec.whatwg.org/multipage/tables.html#htmltablerowelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The HTML element implementing this interface: [<tr>](/en-US/docs/Web/HTML/Reference/Elements/tr).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 10, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLTableRowElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmltablerowelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLTableRowElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmltablerowelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLTableRowElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmltablerowelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe9b6cd1b7fa8612257b72b2a85a96dd7d45c0200%0A*+Document+last+modified%3A+2025-04-10T14%3A56%3A07.000Z%0A%0A%3C%2Fdetails%3E)
