# HTMLTableElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLTableElement&level=high)

The `HTMLTableElement` interface provides special properties and methods (beyond the regular [HTMLElement](/en-US/docs/Web/API/HTMLElement) object interface it also has available to it by inheritance) for manipulating the layout and presentation of tables in an HTML document.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLTableElement.caption](/en-US/docs/Web/API/HTMLTableElement/caption)

A [HTMLTableCaptionElement](/en-US/docs/Web/API/HTMLTableCaptionElement) representing the first [<caption>](/en-US/docs/Web/HTML/Reference/Elements/caption) that is a child of the element, or `null` if none is found. When set, if the object doesn't represent a `<caption>`, a [DOMException](/en-US/docs/Web/API/DOMException) with the `HierarchyRequestError` name is thrown. If a correct object is given, it is inserted in the tree as the first child of this element and the first `<caption>` that is a child of this element is removed from the tree, if any.

[HTMLTableElement.tHead](/en-US/docs/Web/API/HTMLTableElement/tHead)

A [HTMLTableSectionElement](/en-US/docs/Web/API/HTMLTableSectionElement) representing the first [<thead>](/en-US/docs/Web/HTML/Reference/Elements/thead) that is a child of the element, or `null` if none is found. When set, if the object doesn't represent a `<thead>`, a [DOMException](/en-US/docs/Web/API/DOMException) with the `HierarchyRequestError` name is thrown. If a correct object is given, it is inserted in the tree immediately before the first element that is neither a [<caption>](/en-US/docs/Web/HTML/Reference/Elements/caption), nor a [<colgroup>](/en-US/docs/Web/HTML/Reference/Elements/colgroup), or as the last child if there is no such element, and the first `<thead>` that is a child of this element is removed from the tree, if any.

[HTMLTableElement.tFoot](/en-US/docs/Web/API/HTMLTableElement/tFoot)

A [HTMLTableSectionElement](/en-US/docs/Web/API/HTMLTableSectionElement) representing the first [<tfoot>](/en-US/docs/Web/HTML/Reference/Elements/tfoot) that is a child of the element, or `null` if none is found. When set, if the object doesn't represent a `<tfoot>`, a [DOMException](/en-US/docs/Web/API/DOMException) with the `HierarchyRequestError` name is thrown. If a correct object is given, it is inserted in the tree immediately before the first element that is neither a [<caption>](/en-US/docs/Web/HTML/Reference/Elements/caption), a [<colgroup>](/en-US/docs/Web/HTML/Reference/Elements/colgroup), nor a [<thead>](/en-US/docs/Web/HTML/Reference/Elements/thead), or as the last child if there is no such element, and the first `<tfoot>` that is a child of this element is removed from the tree, if any.

[HTMLTableElement.rows](/en-US/docs/Web/API/HTMLTableElement/rows)Read only

Returns a live [HTMLCollection](/en-US/docs/Web/API/HTMLCollection) containing all the rows of the element, that is all [<tr>](/en-US/docs/Web/HTML/Reference/Elements/tr) that are a child of the element, or a child of one of its [<thead>](/en-US/docs/Web/HTML/Reference/Elements/thead), [<tbody>](/en-US/docs/Web/HTML/Reference/Elements/tbody) and [<tfoot>](/en-US/docs/Web/HTML/Reference/Elements/tfoot) children. The rows members of a `<thead>` appear first, in tree order, and those members of a `<tbody>` last, also in tree order. The `HTMLCollection` is live and is automatically updated when the `HTMLTableElement` changes.

[HTMLTableElement.tBodies](/en-US/docs/Web/API/HTMLTableElement/tBodies)Read only

Returns a live [HTMLCollection](/en-US/docs/Web/API/HTMLCollection) containing all the [<tbody>](/en-US/docs/Web/HTML/Reference/Elements/tbody) of the element. The `HTMLCollection` is live and is automatically updated when the `HTMLTableElement` changes.

### [Obsolete Properties](#obsolete_properties)

Warning: The following properties are obsolete. You should avoid using them.

[HTMLTableElement.align](/en-US/docs/Web/API/HTMLTableElement/align)Deprecated

A string containing an enumerated value reflecting the [align](/en-US/docs/Web/HTML/Reference/Elements/table#align) attribute. It indicates the alignment of the element's contents with respect to the surrounding context. The possible values are `"left"`, `"right"`, and `"center"`.

[HTMLTableElement.bgColor](/en-US/docs/Web/API/HTMLTableElement/bgColor)Deprecated

A string containing the background color of the cells. It reflects the obsolete [bgColor](/en-US/docs/Web/HTML/Reference/Elements/table#bgcolor) attribute.

[HTMLTableElement.border](/en-US/docs/Web/API/HTMLTableElement/border)Deprecated

A string containing the width in pixels of the border of the table. It reflects the obsolete [border](/en-US/docs/Web/HTML/Reference/Elements/table#border) attribute.

[HTMLTableElement.cellPadding](/en-US/docs/Web/API/HTMLTableElement/cellPadding)Deprecated

A string containing the width in pixels of the horizontal and vertical space between cell content and cell borders. It reflects the obsolete [cellpadding](/en-US/docs/Web/HTML/Reference/Elements/table#cellpadding) attribute.

[HTMLTableElement.cellSpacing](/en-US/docs/Web/API/HTMLTableElement/cellSpacing)Deprecated

A string containing the width in pixels of the horizontal and vertical separation between cells. It reflects the obsolete [cellspacing](/en-US/docs/Web/HTML/Reference/Elements/table#cellspacing) attribute.

[HTMLTableElement.frame](/en-US/docs/Web/API/HTMLTableElement/frame)Deprecated

A string containing the type of the external borders of the table. It reflects the obsolete [frame](/en-US/docs/Web/HTML/Reference/Elements/table#frame) attribute and can take one of the following values: `"void"`, `"above"`, `"below"`, `"hsides"`, `"vsides"`, `"lhs"`, `"rhs"`, `"box"`, or `"border"`.

[HTMLTableElement.rules](/en-US/docs/Web/API/HTMLTableElement/rules)Deprecated

A string containing the type of the internal borders of the table. It reflects the obsolete [rules](/en-US/docs/Web/HTML/Reference/Elements/table#rules) attribute and can take one of the following values: `"none"`, `"groups"`, `"rows"`, `"cols"`, or `"all"`.

[HTMLTableElement.summary](/en-US/docs/Web/API/HTMLTableElement/summary)Deprecated

A string containing a description of the purpose or the structure of the table. It reflects the obsolete [summary](/en-US/docs/Web/HTML/Reference/Elements/table#summary) attribute.

[HTMLTableElement.width](/en-US/docs/Web/API/HTMLTableElement/width)Deprecated

A string containing the length in pixels or in percentage of the desired width of the entire table. It reflects the obsolete [width](/en-US/docs/Web/HTML/Reference/Elements/table#width) attribute.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLTableElement.createTHead()](/en-US/docs/Web/API/HTMLTableElement/createTHead)

Returns an [HTMLTableSectionElement](/en-US/docs/Web/API/HTMLTableSectionElement) representing the first [<thead>](/en-US/docs/Web/HTML/Reference/Elements/thead) that is a child of the element. If none is found, a new one is created and inserted in the tree immediately before the first element that is neither a [<caption>](/en-US/docs/Web/HTML/Reference/Elements/caption), nor a [<colgroup>](/en-US/docs/Web/HTML/Reference/Elements/colgroup), or as the last child if there is no such element.

[HTMLTableElement.deleteTHead()](/en-US/docs/Web/API/HTMLTableElement/deleteTHead)

Removes the first [<thead>](/en-US/docs/Web/HTML/Reference/Elements/thead) that is a child of the element.

[HTMLTableElement.createTFoot()](/en-US/docs/Web/API/HTMLTableElement/createTFoot)

Returns an [HTMLTableSectionElement](/en-US/docs/Web/API/HTMLTableSectionElement) representing the first [<tfoot>](/en-US/docs/Web/HTML/Reference/Elements/tfoot) that is a child of the element. If none is found, a new one is created and inserted in the tree as the last child.

[HTMLTableElement.deleteTFoot()](/en-US/docs/Web/API/HTMLTableElement/deleteTFoot)

Removes the first [<tfoot>](/en-US/docs/Web/HTML/Reference/Elements/tfoot) that is a child of the element.

[HTMLTableElement.createTBody()](/en-US/docs/Web/API/HTMLTableElement/createTBody)

Returns a [HTMLTableSectionElement](/en-US/docs/Web/API/HTMLTableSectionElement) representing a new [<tbody>](/en-US/docs/Web/HTML/Reference/Elements/tbody) that is a child of the element. It is inserted in the tree after the last element that is a [<tbody>](/en-US/docs/Web/HTML/Reference/Elements/tbody), or as the last child if there is no such element.

[HTMLTableElement.createCaption()](/en-US/docs/Web/API/HTMLTableElement/createCaption)

Returns an [HTMLElement](/en-US/docs/Web/API/HTMLElement) representing the first [<caption>](/en-US/docs/Web/HTML/Reference/Elements/caption) that is a child of the element. If none is found, a new one is created and inserted in the tree as the first child of the [<table>](/en-US/docs/Web/HTML/Reference/Elements/table) element.

[HTMLTableElement.deleteCaption()](/en-US/docs/Web/API/HTMLTableElement/deleteCaption)

Removes the first [<caption>](/en-US/docs/Web/HTML/Reference/Elements/caption) that is a child of the element.

[HTMLTableElement.insertRow()](/en-US/docs/Web/API/HTMLTableElement/insertRow)

Returns an [HTMLTableRowElement](/en-US/docs/Web/API/HTMLTableRowElement) representing a new row of the table. It inserts it in the rows collection immediately before the [<tr>](/en-US/docs/Web/HTML/Reference/Elements/tr) element at the given `index` position. If necessary a [<tbody>](/en-US/docs/Web/HTML/Reference/Elements/tbody) is created. If the `index` is `-1`, the new row is appended to the collection. If the `index` is smaller than `-1` or greater than the number of rows in the collection, a [DOMException](/en-US/docs/Web/API/DOMException) with the value `IndexSizeError` is raised.

[HTMLTableElement.deleteRow()](/en-US/docs/Web/API/HTMLTableElement/deleteRow)

Removes the row corresponding to the `index` given in parameter. If the `index` value is `-1` the last row is removed; if it is smaller than `-1` or greater than the amount of rows in the collection, a [DOMException](/en-US/docs/Web/API/DOMException) with the value `IndexSizeError` is raised.

## [Examples](#examples)

### [Using the DOM Table Interface](#using_the_dom_table_interface)

The `HTMLTableElement` interface provides some convenience methods for creating and manipulating tables. Two frequently used methods are [HTMLTableElement.insertRow](/en-US/docs/Web/API/HTMLTableElement/insertRow) and [HTMLTableRowElement.insertCell](/en-US/docs/Web/API/HTMLTableRowElement/insertCell).

To add a row and some cells to an existing table:

html

```
<table id="table0">
  <tbody>
    <tr>
      <td>Row 0 Cell 0</td>
      <td>Row 0 Cell 1</td>
    </tr>
  </tbody>
</table>
```

js

```
const table = document.getElementById("table0");
const row = table.insertRow(-1);

for (let i = 0; i < 2; i++) {
  const cell = row.insertCell(-1);
  const text = `Row ${row.rowIndex} Cell ${i}`;
  cell.appendChild(document.createTextNode(text));
}
```

## [Specifications](#specifications)

Specification
[HTML# htmltableelement](https://html.spec.whatwg.org/multipage/tables.html#htmltableelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The HTML element implementing this interface: [<table>](/en-US/docs/Web/HTML/Reference/Elements/table).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLTableElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmltableelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLTableElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmltableelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLTableElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmltableelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0b5859108411e47d228a4bb9f30a5556ab17f63c%0A*+Document+last+modified%3A+2025-11-03T18%3A14%3A11.000Z%0A%0A%3C%2Fdetails%3E)
