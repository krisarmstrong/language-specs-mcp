# Selection

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSelection&level=high)

A `Selection` object represents the range of text selected by the user or the current position of the caret. Each [document](/en-US/docs/Web/API/Document) is associated with a unique selection object, which can be retrieved by [document.getSelection()](/en-US/docs/Web/API/Document/getSelection) or [window.getSelection()](/en-US/docs/Web/API/Window/getSelection) and then be examined and modified.

A user may make a selection from left to right (in document order) or right to left (reverse of document order). The anchor is where the user began the selection and the focus is where the user ends the selection. If you make a selection with a desktop mouse, the anchor is placed where you pressed the mouse button, and the focus is placed where you released the mouse button.

Note:Anchor and focus should not be confused with the start and end positions of a selection. The anchor can be placed before the focus or vice versa, depending on the direction you made your selection.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Notes](#notes)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[Selection.anchorNode](/en-US/docs/Web/API/Selection/anchorNode)Read only

Returns the [Node](/en-US/docs/Web/API/Node) in which the selection begins. Can return `null` if selection never existed in the document (e.g., an iframe that was never clicked on).

[Selection.anchorOffset](/en-US/docs/Web/API/Selection/anchorOffset)Read only

Returns a number representing the offset of the selection's anchor within the `anchorNode`. If `anchorNode` is a text node, this is the number of characters within anchorNode preceding the anchor. If `anchorNode` is an element, this is the number of child nodes of the `anchorNode` preceding the anchor.

[Selection.direction](/en-US/docs/Web/API/Selection/direction)Read only

A string describing the direction of the current selection.

[Selection.focusNode](/en-US/docs/Web/API/Selection/focusNode)Read only

Returns the [Node](/en-US/docs/Web/API/Node) in which the selection ends. Can return `null` if selection never existed in the document (e.g., an iframe that was never clicked on).

[Selection.focusOffset](/en-US/docs/Web/API/Selection/focusOffset)Read only

Returns a number representing the offset of the selection's focus within the `focusNode`. If `focusNode` is a text node, this is the number of characters within `focusNode` preceding the focus. If `focusNode` is an element, this is the number of child nodes of the `focusNode` preceding the focus.

[Selection.isCollapsed](/en-US/docs/Web/API/Selection/isCollapsed)Read only

Returns a Boolean indicating whether the selection's start and end points are at the same position.

[Selection.rangeCount](/en-US/docs/Web/API/Selection/rangeCount)Read only

Returns the number of ranges in the selection.

[Selection.type](/en-US/docs/Web/API/Selection/type)Read only

Returns a string describing the type of the current selection.

## [Instance methods](#instance_methods)

[Selection.addRange()](/en-US/docs/Web/API/Selection/addRange)

A [Range](/en-US/docs/Web/API/Range) object that will be added to the selection.

[Selection.collapse()](/en-US/docs/Web/API/Selection/collapse)

Collapses the current selection to a single point.

[Selection.collapseToEnd()](/en-US/docs/Web/API/Selection/collapseToEnd)

Collapses the selection to the end of the last range in the selection.

[Selection.collapseToStart()](/en-US/docs/Web/API/Selection/collapseToStart)

Collapses the selection to the start of the first range in the selection.

[Selection.containsNode()](/en-US/docs/Web/API/Selection/containsNode)

Indicates if a certain node is part of the selection.

[Selection.deleteFromDocument()](/en-US/docs/Web/API/Selection/deleteFromDocument)

Deletes the selection's content from the document.

[Selection.empty()](/en-US/docs/Web/API/Selection/empty)

Removes all ranges from the selection, leaving the [anchorNode](/en-US/docs/Web/API/Selection/anchorNode) and [focusNode](/en-US/docs/Web/API/Selection/focusNode) properties equal to `null` and nothing selected.

[Selection.extend()](/en-US/docs/Web/API/Selection/extend)

Moves the focus of the selection to a specified point.

[Selection.getComposedRanges()](/en-US/docs/Web/API/Selection/getComposedRanges)

Returns an array of [StaticRange](/en-US/docs/Web/API/StaticRange) objects, each that represents a selection that might cross shadow DOM boundaries.

[Selection.getRangeAt()](/en-US/docs/Web/API/Selection/getRangeAt)

Returns a [Range](/en-US/docs/Web/API/Range) object representing one of the ranges currently selected.

[Selection.modify()](/en-US/docs/Web/API/Selection/modify)

Changes the current selection.

[Selection.removeRange()](/en-US/docs/Web/API/Selection/removeRange)

Removes a range from the selection.

[Selection.removeAllRanges()](/en-US/docs/Web/API/Selection/removeAllRanges)

Removes all ranges from the selection.

[Selection.selectAllChildren()](/en-US/docs/Web/API/Selection/selectAllChildren)

Adds all the children of the specified node to the selection.

[Selection.setBaseAndExtent()](/en-US/docs/Web/API/Selection/setBaseAndExtent)

Sets the selection to be a range including all or parts of two specified DOM nodes, and any content located between them.

[Selection.setPosition()](/en-US/docs/Web/API/Selection/setPosition)

Collapses the current selection to a single point.

[Selection.toString()](/en-US/docs/Web/API/Selection/toString)

Returns a string currently being represented by the selection object, i.e., the currently selected text.

## [Notes](#notes)

### [String representation of a selection](#string_representation_of_a_selection)

Calling the [Selection.toString()](/en-US/docs/Web/API/Selection/toString) method returns the text contained within the selection, e.g.:

js

```
const selObj = window.getSelection();
window.alert(selObj);
```

Note that using a selection object as the argument to `window.alert` will call the object's `toString` method.

### [Multiple ranges in a selection](#multiple_ranges_in_a_selection)

A selection object represents the [Range](/en-US/docs/Web/API/Range)s that the user has selected. Typically, it holds only one range, accessed as follows:

js

```
const selObj = window.getSelection();
const range = selObj.getRangeAt(0);
```

- `selObj` is a Selection object
- `range` is a [Range](/en-US/docs/Web/API/Range) object

As the [Selection API specification notes](https://w3c.github.io/selection-api/#h-note-13), the Selection API was initially created by Netscape and allowed multiple ranges (for instance, to allow the user to select a column from a [<table>](/en-US/docs/Web/HTML/Reference/Elements/table)). However, browsers other than Gecko did not implement multiple ranges, and the specification also requires the selection to always have a single range.

### [Selection and input focus](#selection_and_input_focus)

Selection and input focus (indicated by [Document.activeElement](/en-US/docs/Web/API/Document/activeElement)) have a complex relationship that varies by browser. In cross-browser compatible code, it's better to handle them separately.

Safari and Chrome (unlike Firefox) currently focus the element containing selection when modifying the selection programmatically; it's possible that this may change in the future (see [W3C bug 14383](https://www.w3.org/Bugs/Public/show_bug.cgi?id=14383) and [WebKit bug 38696](https://webkit.org/b/38696)).

### [Behavior of Selection API in terms of editing host focus changes](#behavior_of_selection_api_in_terms_of_editing_host_focus_changes)

The Selection API has a common behavior (i.e., shared between browsers) that governs how focus behavior changes for editing hosts after certain methods are called.

The behavior is as follows:

1. An editing host gains focus if the previous selection was outside of it.
2. A Selection API method is called, causing a new selection to be made with the selection range inside the editing host.
3. Focus then moves to the editing host.

Note: The Selection API methods may only move focus to an editing host, not to other focusable elements (e.g., [<a>](/en-US/docs/Web/HTML/Reference/Elements/a)).

The above behavior applies to selections made using the following methods:

- [Selection.collapse()](/en-US/docs/Web/API/Selection/collapse)
- [Selection.collapseToStart()](/en-US/docs/Web/API/Selection/collapseToStart)
- [Selection.collapseToEnd()](/en-US/docs/Web/API/Selection/collapseToEnd)
- [Selection.extend()](/en-US/docs/Web/API/Selection/extend)
- [Selection.selectAllChildren()](/en-US/docs/Web/API/Selection/selectAllChildren)
- [Selection.addRange()](/en-US/docs/Web/API/Selection/addRange)
- [Selection.setBaseAndExtent()](/en-US/docs/Web/API/Selection/setBaseAndExtent)

And when the [Range](/en-US/docs/Web/API/Range) is modified using the following methods:

- [Range.setStart()](/en-US/docs/Web/API/Range/setStart)
- [Range.setEnd()](/en-US/docs/Web/API/Range/setEnd)
- [Range.setStartBefore()](/en-US/docs/Web/API/Range/setStartBefore)
- [Range.setStartAfter()](/en-US/docs/Web/API/Range/setStartAfter)
- [Range.setEndBefore()](/en-US/docs/Web/API/Range/setEndBefore)
- [Range.setEndAfter()](/en-US/docs/Web/API/Range/setEndAfter)
- [Range.collapse()](/en-US/docs/Web/API/Range/collapse)
- [Range.selectNode()](/en-US/docs/Web/API/Range/selectNode)
- [Range.selectNodeContents()](/en-US/docs/Web/API/Range/selectNodeContents)

### [Glossary](#glossary)

Other key terms used in this section.

[anchor](#anchor)

The anchor of a selection is the beginning point of the selection. When making a selection with a mouse, the anchor is where in the document the mouse button is initially pressed. As the user changes the selection using the mouse or the keyboard, the anchor does not move.

[editing host](#editing_host)

An editable element (e.g., an HTML element with [contenteditable](/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable) set, or the HTML child of a document that has [designMode](/en-US/docs/Web/API/Document/designMode) enabled).

[focus of a selection](#focus_of_a_selection)

The focus of a selection is the end point of the selection. When making a selection with a mouse, the focus is where in the document the mouse button is released. As the user changes the selection using the mouse or the keyboard, the focus is the end of the selection that moves.

Note: This is not the same as the focused element of the document, as returned by [document.activeElement](/en-US/docs/Web/API/Document/activeElement).

[range](#range)

A range is a contiguous part of a document. A range can contain entire nodes as well as portions of nodes (such as a portion of a text node). A user will normally only select a single range at a time, but it's possible for a user to select multiple ranges (e.g., by using the Control key). A range can be retrieved from a selection as a [range](/en-US/docs/Web/API/Range) object. Range objects can also be created via the DOM and programmatically added or removed from a selection.

## [Specifications](#specifications)

Specification
[Selection API# selection-interface](https://w3c.github.io/selection-api/#selection-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Window.getSelection](/en-US/docs/Web/API/Window/getSelection), [Document.getSelection](/en-US/docs/Web/API/Document/getSelection), [Range](/en-US/docs/Web/API/Range)
- Selection-related events: [selectionchange](/en-US/docs/Web/API/Document/selectionchange_event) and [selectstart](/en-US/docs/Web/API/Node/selectstart_event)
- HTML inputs provide simpler helper APIs for working with selection (see [HTMLInputElement.setSelectionRange()](/en-US/docs/Web/API/HTMLInputElement/setSelectionRange))
- [Document.activeElement](/en-US/docs/Web/API/Document/activeElement), [HTMLElement.focus](/en-US/docs/Web/API/HTMLElement/focus), and [HTMLElement.blur](/en-US/docs/Web/API/HTMLElement/blur)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 24, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Selection/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/selection/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSelection&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fselection%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSelection%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fselection%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa84b606ffd77c40a7306be6c932a74ab9ce6ab96%0A*+Document+last+modified%3A+2025-06-24T06%3A12%3A11.000Z%0A%0A%3C%2Fdetails%3E)
