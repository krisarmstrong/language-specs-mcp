# NDEFRecord

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNDEFRecord&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `NDEFRecord` interface of the [Web NFC API](/en-US/docs/Web/API/Web_NFC_API) provides data that can be read from, or written to, compatible NFC devices, e.g., NFC tags supporting NDEF.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[NDEFRecord()](/en-US/docs/Web/API/NDEFRecord/NDEFRecord)Experimental

Returns a new `NDEFRecord`.

## [Instance properties](#instance_properties)

[NDEFRecord.recordType](/en-US/docs/Web/API/NDEFRecord/recordType)ExperimentalRead only

Returns the record type of the record. Records must have either a standardized well-known type name such as `"empty"`, `"text"`, `"url"`, `"smart-poster"`, `"absolute-url"`, `"mime"`, or `"unknown"` or else an external type name, which consists of a domain name and custom type name separated by a colon (":").

[NDEFRecord.mediaType](/en-US/docs/Web/API/NDEFRecord/mediaType)ExperimentalRead only

Returns the [MIME type](/en-US/docs/Glossary/MIME_type) of the record. This value will be `null` if `recordType` is not equal to `"mime"`.

[NDEFRecord.id](/en-US/docs/Web/API/NDEFRecord/id)ExperimentalRead only

Returns the record identifier, which is an absolute or relative URL used to identify the record.

Note: The uniqueness of the identifier is enforced only by the generator of the record.

[NDEFRecord.data](/en-US/docs/Web/API/NDEFRecord/data)ExperimentalRead only

Returns a [DataView](/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView) containing the raw bytes of the record's payload.

[NDEFRecord.encoding](/en-US/docs/Web/API/NDEFRecord/encoding)ExperimentalRead only

Returns the encoding of a textual payload, or `null` otherwise.

[NDEFRecord.lang](/en-US/docs/Web/API/NDEFRecord/lang)ExperimentalRead only

Returns the language of a textual payload, or `null` if one was not supplied.

## [Instance methods](#instance_methods)

[NDEFRecord.toRecords()](/en-US/docs/Web/API/NDEFRecord/toRecords)Experimental

Converts [NDEFRecord.data](/en-US/docs/Web/API/NDEFRecord/data) to a sequence of records. This allows parsing the payloads of record types which may contain nested records, such as smart poster and external type records.

## [Specifications](#specifications)

Specification
[Web NFC# dom-ndefrecord](https://w3c.github.io/web-nfc/#dom-ndefrecord)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/NDEFRecord/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/ndefrecord/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNDEFRecord&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fndefrecord%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNDEFRecord%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fndefrecord%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F702cd9e4d2834e13aea345943efc8d0c03d92ec9%0A*+Document+last+modified%3A+2025-04-03T04%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
