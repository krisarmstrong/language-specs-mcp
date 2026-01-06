# DOMError

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

The `DOMError` interface describes an error object that contains an error name.

## In this article

- [Instance properties](#instance_properties)
- [Error types](#error_types)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

`DOMError.name`Read onlyDeprecated

Returns a string representing one of the error type names (see below).

`DOMError.message`Read onlyDeprecated

Returns a string representing a message or description associated with the given error type name.

## [Error types](#error_types)

TypeDescription`IndexSizeError`The index is not in the allowed range (e.g., thrown in a [range](/en-US/docs/Web/API/Range) object).`HierarchyRequestError`The node tree hierarchy is not correct.`WrongDocumentError`The object is in the wrong [document](/en-US/docs/Web/API/Document).`InvalidCharacterError`The string contains invalid characters.`NoModificationAllowedError`The object can not be modified.`NotFoundError`The object can not be found here.`NotSupportedError`The operation is not supported`InvalidStateError`The object is in an invalid state.`SyntaxError`The string did not match the expected pattern.`InvalidModificationError`The object can not be modified in this way.`NamespaceError`The operation is not allowed by Namespaces in XML`InvalidAccessError`The object does not support the operation or argument.`TypeMismatchError`The type of the object does not match the expected type.`SecurityError`The operation is insecure.`NetworkError`A network error occurred.`AbortError`The operation was aborted.`URLMismatchError`The given URL does not match another URL.`TimeoutError`The operation timed out.`InvalidNodeTypeError`The node is incorrect or has an incorrect ancestor for this operation.`DataCloneError`The object can not be cloned.

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [DOMException](/en-US/docs/Web/API/DOMException)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 19, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/DOMError/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/domerror/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMError&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdomerror%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMError%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdomerror%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7cac5cc51350b7688903656bb36d79152f82d01f%0A*+Document+last+modified%3A+2025-08-19T19%3A45%3A56.000Z%0A%0A%3C%2Fdetails%3E)
