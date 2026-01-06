# DOMException

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMException&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `DOMException` interface represents an abnormal event (called an exception) that occurs as a result of calling a method or accessing a property of a web API. This is how error conditions are described in web APIs.

Each exception has a name, which is a short "PascalCase"-style string identifying the error or abnormal condition.

`DOMException` is a [Serializable object](/en-US/docs/Glossary/Serializable_object), so it can be cloned with [structuredClone()](/en-US/docs/Web/API/Window/structuredClone) or copied between [Workers](/en-US/docs/Web/API/Worker) using [postMessage()](/en-US/docs/Web/API/Worker/postMessage).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Error names](#error_names)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[DOMException()](/en-US/docs/Web/API/DOMException/DOMException)

Returns a `DOMException` object with a specified message and name.

## [Instance properties](#instance_properties)

[DOMException.code](/en-US/docs/Web/API/DOMException/code)DeprecatedRead only

Returns one of the legacy error code constants, or `0` if none match.

[DOMException.message](/en-US/docs/Web/API/DOMException/message)Read only

Returns a string representing a message or description associated with the given [error name](#error_names).

[DOMException.name](/en-US/docs/Web/API/DOMException/name)Read only

Returns a string that contains one of the strings associated with an [error name](#error_names).

## [Error names](#error_names)

Common error names are listed here. Some APIs define their own sets of names, so this is not necessarily a complete list.

The following deprecated historical errors don't have an error name but instead have only a legacy constant code value and a legacy constant name:

- Legacy code value: `2`, legacy constant name: `DOMSTRING_SIZE_ERR`
- Legacy code value: `6`, legacy constant name: `NO_DATA_ALLOWED_ERR`
- Legacy code value: `16`, legacy constant name: `VALIDATION_ERR`

Note: Because historically the errors were identified by a numeric value that corresponded with a named variable defined to have that value, some of the entries below indicate the legacy code value and constant name that were used in the past.

[IndexSizeError](#indexsizeerror)

The index is not in the allowed range. For example, this can be thrown by the [Range](/en-US/docs/Web/API/Range) object. (Legacy code value: `1` and legacy constant name: `INDEX_SIZE_ERR`)

[HierarchyRequestError](#hierarchyrequesterror)

The node tree hierarchy is not correct. (Legacy code value: `3` and legacy constant name: `HIERARCHY_REQUEST_ERR`)

[WrongDocumentError](#wrongdocumenterror)

The object is in the wrong [Document](/en-US/docs/Web/API/Document). (Legacy code value: `4` and legacy constant name: `WRONG_DOCUMENT_ERR`)

[InvalidCharacterError](#invalidcharactererror)

The string contains invalid characters. (Legacy code value: `5` and legacy constant name: `INVALID_CHARACTER_ERR`)

[NoModificationAllowedError](#nomodificationallowederror)

The object cannot be modified. (Legacy code value: `7` and legacy constant name: `NO_MODIFICATION_ALLOWED_ERR`)

[NotFoundError](#notfounderror)

The object cannot be found here. (Legacy code value: `8` and legacy constant name: `NOT_FOUND_ERR`)

[NotSupportedError](#notsupportederror)

The operation is not supported. (Legacy code value: `9` and legacy constant name: `NOT_SUPPORTED_ERR`)

[InUseAttributeError](#inuseattributeerror)

The attribute is in use. (Legacy code value: `10` and legacy constant name: `INUSE_ATTRIBUTE_ERR`)

[InvalidStateError](#invalidstateerror)

The object is in an invalid state. (Legacy code value: `11` and legacy constant name: `INVALID_STATE_ERR`)

[SyntaxError](#syntaxerror)

The string did not match the expected pattern. (Legacy code value: `12` and legacy constant name: `SYNTAX_ERR`)

[InvalidModificationError](#invalidmodificationerror)

The object cannot be modified in this way. (Legacy code value: `13` and legacy constant name: `INVALID_MODIFICATION_ERR`)

[NamespaceError](#namespaceerror)

The operation is not allowed by Namespaces in XML. (Legacy code value: `14` and legacy constant name: `NAMESPACE_ERR`)

[InvalidAccessError](#invalidaccesserror)

The object does not support the operation or argument. (Legacy code value: `15` and legacy constant name: `INVALID_ACCESS_ERR`)

[TypeMismatchError 
Deprecated](#typemismatcherror)

The type of the object does not match the expected type. (Legacy code value: `17` and legacy constant name: `TYPE_MISMATCH_ERR`) This value is deprecated; the JavaScript [TypeError](/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError) exception is now raised instead of a `DOMException` with this value.

[SecurityError](#securityerror)

The operation is insecure. (Legacy code value: `18` and legacy constant name: `SECURITY_ERR`)

[NetworkError 
Experimental](#networkerror)

A network error occurred. (Legacy code value: `19` and legacy constant name: `NETWORK_ERR`)

[AbortError 
Experimental](#aborterror)

The operation was aborted. (Legacy code value: `20` and legacy constant name: `ABORT_ERR`)

[URLMismatchError 
Experimental](#urlmismatcherror)

The given URL does not match another URL. (Legacy code value: `21` and legacy constant name: `URL_MISMATCH_ERR`)

[QuotaExceededError](/en-US/docs/Web/API/QuotaExceededError)

The quota has been exceeded. (Legacy code value: `22` and legacy constant name: `QUOTA_EXCEEDED_ERR`) It is a proper interface that derives from `DOMException`.

[TimeoutError](#timeouterror)

The operation timed out. (Legacy code value: `23` and legacy constant name: `TIMEOUT_ERR`)

[InvalidNodeTypeError 
Experimental](#invalidnodetypeerror)

The node is incorrect or has an incorrect ancestor for this operation. (Legacy code value: `24` and legacy constant name: `INVALID_NODE_TYPE_ERR`)

[DataCloneError 
Experimental](#datacloneerror)

The object can not be cloned. (Legacy code value: `25` and legacy constant name: `DATA_CLONE_ERR`)

[EncodingError 
Experimental](#encodingerror)

The encoding or decoding operation failed (No legacy code value and constant name).

[NotReadableError 
Experimental](#notreadableerror)

The input/output read operation failed (No legacy code value and constant name).

[UnknownError 
Experimental](#unknownerror)

The operation failed for an unknown transient reason (e.g., out of memory) (No legacy code value and constant name).

[ConstraintError 
Experimental](#constrainterror)

A mutation operation in a transaction failed because a constraint was not satisfied (No legacy code value and constant name).

[DataError 
Experimental](#dataerror)

Provided data is inadequate (No legacy code value and constant name).

[TransactionInactiveError 
Experimental](#transactioninactiveerror)

A request was placed against a transaction that is currently not active or is finished (No legacy code value and constant name).

[ReadOnlyError 
Experimental](#readonlyerror)

The mutating operation was attempted in a "readonly" transaction (No legacy code value and constant name).

[VersionError 
Experimental](#versionerror)

An attempt was made to open a database using a lower version than the existing version (No legacy code value and constant name).

[OperationError 
Experimental](#operationerror)

The operation failed for an operation-specific reason (No legacy code value and constant name).

[NotAllowedError](#notallowederror)

The request is not allowed by the user agent or the platform in the current context, possibly because the user denied permission (No legacy code value and constant name).

## [Specifications](#specifications)

Specification
[Web IDL# idl-DOMException](https://webidl.spec.whatwg.org/#idl-DOMException)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [A polyfill of DOMException](https://github.com/zloirock/core-js#domexception) is available in [core-js](https://github.com/zloirock/core-js)
- [DOMError](/en-US/docs/Web/API/DOMError)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 19, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/DOMException/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/domexception/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMException&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdomexception%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMException%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdomexception%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7cac5cc51350b7688903656bb36d79152f82d01f%0A*+Document+last+modified%3A+2025-08-19T19%3A45%3A56.000Z%0A%0A%3C%2Fdetails%3E)
