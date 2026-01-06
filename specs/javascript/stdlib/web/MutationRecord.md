# MutationRecord

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMutationRecord&level=high)

The `MutationRecord` is a read-only interface that represents an individual DOM mutation observed by a [MutationObserver](/en-US/docs/Web/API/MutationObserver). It is the object inside the array passed to the callback of a [MutationObserver](/en-US/docs/Web/API/MutationObserver).

## In this article

- [Instance properties](#instance_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[MutationRecord.addedNodes](/en-US/docs/Web/API/MutationRecord/addedNodes)Read only

The nodes added by a mutation. Will be an empty [NodeList](/en-US/docs/Web/API/NodeList) if no nodes were added.

[MutationRecord.attributeName](/en-US/docs/Web/API/MutationRecord/attributeName)Read only

The name of the changed attribute as a string, or `null`.

[MutationRecord.attributeNamespace](/en-US/docs/Web/API/MutationRecord/attributeNamespace)Read only

The namespace of the changed attribute as a string, or `null`.

[MutationRecord.nextSibling](/en-US/docs/Web/API/MutationRecord/nextSibling)Read only

The next sibling of the added or removed nodes, or `null`.

[MutationRecord.oldValue](/en-US/docs/Web/API/MutationRecord/oldValue)Read only

The value depends on the [MutationRecord.type](/en-US/docs/Web/API/MutationRecord/type):

- For `attributes`, it is the value of the changed attribute before the change.
- For `characterData`, it is the data of the changed node before the change.
- For `childList`, it is `null`.

[MutationRecord.previousSibling](/en-US/docs/Web/API/MutationRecord/previousSibling)Read only

The previous sibling of the added or removed nodes, or `null`.

[MutationRecord.removedNodes](/en-US/docs/Web/API/MutationRecord/removedNodes)Read only

The nodes removed by a mutation. Will be an empty [NodeList](/en-US/docs/Web/API/NodeList) if no nodes were removed.

[MutationRecord.target](/en-US/docs/Web/API/MutationRecord/target)Read only

The node the mutation affected, depending on the `MutationRecord.type`.

- For `attributes`, it is the element whose attribute changed.
- For `characterData`, it is the `CharacterData` node.
- For `childList`, it is the node whose children changed.

[MutationRecord.type](/en-US/docs/Web/API/MutationRecord/type)Read only

A string representing the type of mutation: `attributes` if the mutation was an attribute mutation, `characterData` if it was a mutation to a `CharacterData` node, and `childList` if it was a mutation to the tree of nodes.

## [Specifications](#specifications)

Specification
[DOM# interface-mutationrecord](https://dom.spec.whatwg.org/#interface-mutationrecord)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 24, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/MutationRecord/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mutationrecord/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMutationRecord&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmutationrecord%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMutationRecord%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmutationrecord%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F32305cc3cf274fbfdcc73a296bbd400a26f38296%0A*+Document+last+modified%3A+2024-07-24T20%3A47%3A46.000Z%0A%0A%3C%2Fdetails%3E)
