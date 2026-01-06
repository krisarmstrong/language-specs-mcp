# Selection API

Note: This API is not available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API) (not exposed via [WorkerNavigator](/en-US/docs/Web/API/WorkerNavigator)).

The Selection API enables developers to access and manipulate the portion of a document selected by the user.

The [Window.getSelection()](/en-US/docs/Web/API/Window/getSelection) and [Document.getSelection()](/en-US/docs/Web/API/Document/getSelection) methods return a [Selection](/en-US/docs/Web/API/Selection) object representing the portion of the document selected by the user. A `Selection` object provides methods to:

- access the currently selected nodes
- modify the current selection, expanding or collapsing it or selecting an entirely different part of the document
- delete parts of the current selection from the DOM.

The Selection API also provides two events, both firing on [Document](/en-US/docs/Web/API/Document):

- the [selectstart](/en-US/docs/Web/API/Node/selectstart_event) event is fired when the user starts to make a new selection
- the [selectionchange](/en-US/docs/Web/API/Document/selectionchange_event) event is fired when the current selection changes.

## In this article

- [Interfaces](#interfaces)
- [Specifications](#specifications)

## [Interfaces](#interfaces)

[Selection](/en-US/docs/Web/API/Selection)

An interface which represents the part of the document selected by the user or the current position of the caret.

[Document.getSelection()](/en-US/docs/Web/API/Document/getSelection)

A method returning a `Selection` object representing the current selection or current position of the caret.

[Window.getSelection()](/en-US/docs/Web/API/Window/getSelection)

A method returning a `Selection` object representing the current selection or current position of the caret.

[Document.selectionchange](/en-US/docs/Web/API/Document/selectionchange_event)

An event which is fired when the current selection is changed.

[Node.selectstart](/en-US/docs/Web/API/Node/selectstart_event)

An event which is fired when a user starts a new selection.

## [Specifications](#specifications)

Specification
[Selection API# selection-interface](https://w3c.github.io/selection-api/#selection-interface)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Selection_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/selection_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSelection_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fselection_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSelection_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fselection_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4f35a8237ee0842beb9cfef3354e05464ad7ce1a%0A*+Document+last+modified%3A+2024-07-26T03%3A46%3A04.000Z%0A%0A%3C%2Fdetails%3E)
