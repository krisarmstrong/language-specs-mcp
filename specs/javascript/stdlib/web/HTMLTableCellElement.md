# HTMLTableCellElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLTableCellElement&level=high)

The `HTMLTableCellElement` interface provides special properties and methods (beyond the regular [HTMLElement](/en-US/docs/Web/API/HTMLElement) interface it also has available to it by inheritance) for manipulating the layout and presentation of table cells, either header cells ([<th>](/en-US/docs/Web/HTML/Reference/Elements/th)) or data cells ([<td>](/en-US/docs/Web/HTML/Reference/Elements/td)), in an HTML document.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Deprecated properties](#deprecated_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLTableCellElement.abbr](/en-US/docs/Web/API/HTMLTableCellElement/abbr)

A string that can be used on `<th>` elements (not on [<td>](/en-US/docs/Web/HTML/Reference/Elements/td)), specifying an alternative label for the header cell. This alternate label can be used in other contexts, such as when describing the headers that apply to a data cell. This is used to offer a shorter term for use by screen readers in particular; and is a valuable accessibility tool. Usually, the value of `abbr` is an abbreviation or acronym, but can be any text that's appropriate contextually.

[HTMLTableCellElement.cellIndex](/en-US/docs/Web/API/HTMLTableCellElement/cellIndex)Read only

A number representing the cell's position in the [cells](/en-US/docs/Web/API/HTMLTableRowElement/cells) collection of the [<tr>](/en-US/docs/Web/HTML/Reference/Elements/tr) the cell is contained within. If the cell doesn't belong to a `<tr>`, it returns `-1`.

[HTMLTableCellElement.colSpan](/en-US/docs/Web/API/HTMLTableCellElement/colSpan)

A positive number indicating the number of columns this cell must span; this lets the cell occupy space across multiple columns of the table. It reflects the [colspan](/en-US/docs/Web/HTML/Reference/Elements/td#colspan) attribute.

[HTMLTableCellElement.headers](/en-US/docs/Web/API/HTMLTableCellElement/headers)Read only

A [DOMTokenList](/en-US/docs/Web/API/DOMTokenList) describing a list of `id` of [<th>](/en-US/docs/Web/HTML/Reference/Elements/th) elements that represent headers associated with the cell. It reflects the [headers](/en-US/docs/Web/HTML/Reference/Elements/td#headers) attribute.

[HTMLTableCellElement.rowSpan](/en-US/docs/Web/API/HTMLTableCellElement/rowSpan)

A positive number indicating the number of rows this cell must span; this lets a cell occupy space across multiple rows of the table. It reflects the [rowspan](/en-US/docs/Web/HTML/Reference/Elements/td#rowspan) attribute.

[HTMLTableCellElement.scope](/en-US/docs/Web/API/HTMLTableCellElement/scope)

A string indicating the scope of a [<th>](/en-US/docs/Web/HTML/Reference/Elements/th) cell. Possible values for `scope` are: `col`, `colgroup`, `row`, `rowgroup`, or the empty string (`""`).

## [Instance methods](#instance_methods)

No specific method; inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

## [Deprecated properties](#deprecated_properties)

Warning: These properties have been deprecated and should no longer be used. They are documented primarily to help understand older code bases.

[HTMLTableCellElement.align](/en-US/docs/Web/API/HTMLTableCellElement/align)Deprecated

A string containing the value of the [align](/en-US/docs/Web/HTML/Reference/Elements/td#align) attribute, if present, or empty string if not set. It can be used to set the alignment of the element's contents to the surrounding context of `"left"`, `"right"`, and `"center"`. Use the CSS [text-align](/en-US/docs/Web/CSS/Reference/Properties/text-align) property instead.

`HTMLTableCellElement.axis`Deprecated

A string containing a name grouping cells in virtual. It reflects the obsolete [axis](/en-US/docs/Web/HTML/Reference/Elements/td#axis) attribute.

[HTMLTableCellElement.bgColor](/en-US/docs/Web/API/HTMLTableCellElement/bgColor)Deprecated

A string containing the background color of the cells. It reflects the obsolete [bgColor](/en-US/docs/Web/HTML/Reference/Elements/td#bgcolor) attribute.

[HTMLTableCellElement.ch](/en-US/docs/Web/API/HTMLTableCellElement/ch)Deprecated

A string containing one single character. This character is the one to align all the cells of a column on. It reflects the [char](/en-US/docs/Web/HTML/Reference/Elements/td#char) and defaults to the decimal points associated with the language, e.g., `'.'` for English, or `','` for French. This property was optional and was not very well supported.

[HTMLTableCellElement.chOff](/en-US/docs/Web/API/HTMLTableCellElement/chOff)Deprecated

A string containing an integer indicating how many characters must be left at the right (for left-to-right scripts; or at the left for right-to-left scripts) of the character defined by `HTMLTableCellElement.ch`. This property was optional and was not very well supported.

`HTMLTableCellElement.height`Deprecated

A string containing a length of pixel of the hinted height of the cell. It reflects the obsolete [height](/en-US/docs/Web/HTML/Reference/Elements/td#height) attribute.

[HTMLTableCellElement.noWrap](/en-US/docs/Web/API/HTMLTableCellElement/noWrap)Deprecated

A boolean value reflecting the `nowrap` attribute and indicating if cell content can be broken into several lines.

[HTMLTableCellElement.vAlign](/en-US/docs/Web/API/HTMLTableCellElement/vAlign)Deprecated

A string representing an enumerated value indicating how the content of the cell must be vertically aligned. It reflects the [valign](/en-US/docs/Web/HTML/Reference/Elements/td#valign) attribute and can have one of the following values: `"top"`, `"middle"`, `"bottom"`, or `"baseline"`. Use the CSS [vertical-align](/en-US/docs/Web/CSS/Reference/Properties/vertical-align) property instead.

`HTMLTableCellElement.width`Deprecated

A string specifying the number of pixels wide the cell should be drawn, if possible. This property reflects the also obsolete [width](/en-US/docs/Web/HTML/Reference/Elements/td#width) attribute. Use the CSS [width](/en-US/docs/Web/CSS/Reference/Properties/width) property instead.

## [Specifications](#specifications)

Specification
[HTML# htmltablecellelement](https://html.spec.whatwg.org/multipage/tables.html#htmltablecellelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The HTML elements implementing this interface: [<th>](/en-US/docs/Web/HTML/Reference/Elements/th) and [<td>](/en-US/docs/Web/HTML/Reference/Elements/td).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 10, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLTableCellElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmltablecellelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLTableCellElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmltablecellelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLTableCellElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmltablecellelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe9b6cd1b7fa8612257b72b2a85a96dd7d45c0200%0A*+Document+last+modified%3A+2025-04-10T14%3A56%3A07.000Z%0A%0A%3C%2Fdetails%3E)
