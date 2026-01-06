# FormData

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFormData&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `FormData` interface provides a way to construct a set of key/value pairs representing form fields and their values, which can be sent using the [fetch()](/en-US/docs/Web/API/Window/fetch), [XMLHttpRequest.send()](/en-US/docs/Web/API/XMLHttpRequest/send) or [navigator.sendBeacon()](/en-US/docs/Web/API/Navigator/sendBeacon) methods. It uses the same format a form would use if the encoding type were set to `"multipart/form-data"`.

You can also pass it directly to the [URLSearchParams](/en-US/docs/Web/API/URLSearchParams) constructor if you want to generate query parameters in the way a [<form>](/en-US/docs/Web/HTML/Reference/Elements/form) would do if it were using simple `GET` submission.

An object implementing `FormData` can directly be used in a [for...of](/en-US/docs/Web/JavaScript/Reference/Statements/for...of) structure, instead of [entries()](/en-US/docs/Web/API/FormData/entries): `for (const p of myFormData)` is equivalent to `for (const p of myFormData.entries())`.

## In this article

- [Constructor](#constructor)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[FormData()](/en-US/docs/Web/API/FormData/FormData)

Creates a new `FormData` object.

## [Instance methods](#instance_methods)

[FormData.append()](/en-US/docs/Web/API/FormData/append)

Appends a new value onto an existing key inside a `FormData` object, or adds the key if it does not already exist.

[FormData.delete()](/en-US/docs/Web/API/FormData/delete)

Deletes a key/value pair from a `FormData` object.

[FormData.entries()](/en-US/docs/Web/API/FormData/entries)

Returns an [iterator](/en-US/docs/Web/JavaScript/Reference/Iteration_protocols) that iterates through all key/value pairs contained in the `FormData`.

[FormData.get()](/en-US/docs/Web/API/FormData/get)

Returns the first value associated with a given key from within a `FormData` object.

[FormData.getAll()](/en-US/docs/Web/API/FormData/getAll)

Returns an array of all the values associated with a given key from within a `FormData`.

[FormData.has()](/en-US/docs/Web/API/FormData/has)

Returns whether a `FormData` object contains a certain key.

[FormData.keys()](/en-US/docs/Web/API/FormData/keys)

Returns an [iterator](/en-US/docs/Web/JavaScript/Reference/Iteration_protocols) iterates through all keys of the key/value pairs contained in the `FormData`.

[FormData.set()](/en-US/docs/Web/API/FormData/set)

Sets a new value for an existing key inside a `FormData` object, or adds the key/value if it does not already exist.

[FormData.values()](/en-US/docs/Web/API/FormData/values)

Returns an [iterator](/en-US/docs/Web/JavaScript/Reference/Iteration_protocols) that iterates through all values contained in the `FormData`.

## [Specifications](#specifications)

Specification
[XMLHttpRequest# interface-formdata](https://xhr.spec.whatwg.org/#interface-formdata)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using FormData objects](/en-US/docs/Web/API/XMLHttpRequest_API/Using_FormData_Objects)
- [<Form>](/en-US/docs/Web/HTML/Reference/Elements/form)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 24, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/FormData/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/formdata/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFormData&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fformdata%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFormData%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fformdata%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F58ad1df59f2ffb9ecab4e27fe1bdf1eb5a55f89b%0A*+Document+last+modified%3A+2024-07-24T01%3A12%3A06.000Z%0A%0A%3C%2Fdetails%3E)
