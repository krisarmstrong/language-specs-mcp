# URLSearchParams

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2018⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FURLSearchParams&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `URLSearchParams` interface defines utility methods to work with the query string of a URL.

`URLSearchParams` objects are [iterable](/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterable_protocol), so they can directly be used in a [for...of](/en-US/docs/Web/JavaScript/Reference/Statements/for...of) structure to iterate over key/value pairs in the same order as they appear in the query string, for example the following two lines are equivalent:

js

```
for (const [key, value] of mySearchParams) {
}
for (const [key, value] of mySearchParams.entries()) {
}
```

Although `URLSearchParams` is functionally similar to a [Map](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map), when iterating, it may suffer from some [pitfalls](/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#concurrent_modifications_when_iterating) that `Map` doesn't encounter due to how it's implemented.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[URLSearchParams()](/en-US/docs/Web/API/URLSearchParams/URLSearchParams)

Returns a `URLSearchParams` object instance.

## [Instance properties](#instance_properties)

[size](/en-US/docs/Web/API/URLSearchParams/size)Read only

Indicates the total number of search parameter entries.

## [Instance methods](#instance_methods)

[URLSearchParams[Symbol.iterator]()](#urlsearchparamssymbol.iterator)

Returns an [iterator](/en-US/docs/Web/JavaScript/Reference/Iteration_protocols) allowing iteration through all key/value pairs contained in this object in the same order as they appear in the query string.

[URLSearchParams.append()](/en-US/docs/Web/API/URLSearchParams/append)

Appends a specified key/value pair as a new search parameter.

[URLSearchParams.delete()](/en-US/docs/Web/API/URLSearchParams/delete)

Deletes search parameters that match a name, and optional value, from the list of all search parameters.

[URLSearchParams.entries()](/en-US/docs/Web/API/URLSearchParams/entries)

Returns an [iterator](/en-US/docs/Web/JavaScript/Reference/Iteration_protocols) allowing iteration through all key/value pairs contained in this object in the same order as they appear in the query string.

[URLSearchParams.forEach()](/en-US/docs/Web/API/URLSearchParams/forEach)

Allows iteration through all values contained in this object via a callback function.

[URLSearchParams.get()](/en-US/docs/Web/API/URLSearchParams/get)

Returns the first value associated with the given search parameter.

[URLSearchParams.getAll()](/en-US/docs/Web/API/URLSearchParams/getAll)

Returns all the values associated with a given search parameter.

[URLSearchParams.has()](/en-US/docs/Web/API/URLSearchParams/has)

Returns a boolean value indicating if a given parameter, or parameter and value pair, exists.

[URLSearchParams.keys()](/en-US/docs/Web/API/URLSearchParams/keys)

Returns an [iterator](/en-US/docs/Web/JavaScript/Reference/Iteration_protocols) allowing iteration through all keys of the key/value pairs contained in this object.

[URLSearchParams.set()](/en-US/docs/Web/API/URLSearchParams/set)

Sets the value associated with a given search parameter to the given value. If there are several values, the others are deleted.

[URLSearchParams.sort()](/en-US/docs/Web/API/URLSearchParams/sort)

Sorts all key/value pairs, if any, by their keys.

[URLSearchParams.toString()](/en-US/docs/Web/API/URLSearchParams/toString)

Returns a string containing a query string suitable for use in a URL.

[URLSearchParams.values()](/en-US/docs/Web/API/URLSearchParams/values)

Returns an [iterator](/en-US/docs/Web/JavaScript/Reference/Iteration_protocols) allowing iteration through all values of the key/value pairs contained in this object.

## [Examples](#examples)

### [Using URLSearchParams](#using_urlsearchparams)

js

```
const paramsString = "q=URLUtils.searchParams&topic=api";
const searchParams = new URLSearchParams(paramsString);

// Iterating the search parameters
for (const p of searchParams) {
  console.log(p);
}

console.log(searchParams.has("topic")); // true
console.log(searchParams.has("topic", "fish")); // false
console.log(searchParams.get("topic") === "api"); // true
console.log(searchParams.getAll("topic")); // ["api"]
console.log(searchParams.get("foo") === null); // true
console.log(searchParams.append("topic", "webdev"));
console.log(searchParams.toString()); // "q=URLUtils.searchParams&topic=api&topic=webdev"
console.log(searchParams.set("topic", "More webdev"));
console.log(searchParams.toString()); // "q=URLUtils.searchParams&topic=More+webdev"
console.log(searchParams.delete("topic"));
console.log(searchParams.toString()); // "q=URLUtils.searchParams"
```

Search parameters can also be an object.

js

```
const paramsObj = { foo: "bar", baz: "bar" };
const searchParams = new URLSearchParams(paramsObj);

console.log(searchParams.toString()); // "foo=bar&baz=bar"
console.log(searchParams.has("foo")); // true
console.log(searchParams.get("foo")); // "bar"
```

### [Parsing window.location](#parsing_window.location)

Unlike [URL](/en-US/docs/Web/API/URL), the [Location](/en-US/docs/Web/API/Location) interface does not provide a readily-available `searchParams` property. We can parse `location.search` with `URLSearchParams`.

js

```
// Assume page has location:
// https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams?foo=a
const paramsString = window.location.search;
const searchParams = new URLSearchParams(paramsString);
console.log(searchParams.get("foo")); // a
```

### [Duplicate search parameters](#duplicate_search_parameters)

js

```
const paramStr = "foo=bar&foo=baz";
const searchParams = new URLSearchParams(paramStr);

console.log(searchParams.toString()); // "foo=bar&foo=baz"
console.log(searchParams.has("foo")); // true
console.log(searchParams.get("foo")); // bar, only returns the first value
console.log(searchParams.getAll("foo")); // ["bar", "baz"]
```

### [No URL parsing](#no_url_parsing)

The `URLSearchParams` constructor does not parse full URLs. However, it will strip an initial leading `?` off of a string, if present.

js

```
const paramsString1 = "http://example.com/search?query=%40";
const searchParams1 = new URLSearchParams(paramsString1);

console.log(searchParams1.has("query")); // false
console.log(searchParams1.has("http://example.com/search?query")); // true

console.log(searchParams1.get("query")); // null
console.log(searchParams1.get("http://example.com/search?query")); // "@" (equivalent to decodeURIComponent('%40'))

const paramsString2 = "?query=value";
const searchParams2 = new URLSearchParams(paramsString2);
console.log(searchParams2.has("query")); // true

const url = new URL("http://example.com/search?query=%40");
const searchParams3 = new URLSearchParams(url.search);
console.log(searchParams3.has("query")); // true
```

### [Percent encoding](#percent_encoding)

`URLSearchParams` objects [percent-encode](/en-US/docs/Glossary/Percent-encoding) anything in the [application/x-www-form-urlencoded percent-encode set](https://url.spec.whatwg.org/#application-x-www-form-urlencoded-percent-encode-set) (which contains all code points except ASCII alphanumeric, `*`, `-`, `.`, and `_`), and encode U+0020 SPACE as `+`. However, it only handles percent-encoding when serializing and deserializing full URL search params syntax. When interacting with individual keys and values, you always use the unencoded version.

js

```
// Creation from parsing a string: percent-encoding is decoded
const params = new URLSearchParams("%24%25%26=%28%29%2B");
// Retrieving all keys/values: only decoded values are returned
console.log([...params]); // [["$%&", "()+"]]
// Getting an individual value: use the decoded key and get the decoded value
console.log(params.get("$%&")); // "()+"
console.log(params.get("%24%25%26")); // null
// Setting an individual value: use the unencoded key and value
params.append("$%&$#@+", "$#&*@#()+");
// Serializing: percent-encoding is applied
console.log(params.toString());
// "%24%25%26=%28%29%2B&%24%25%26%24%23%40%2B=%24%23%26*%40%23%28%29%2B"
```

If you append a key/value pair with a percent-encoded key, that key is treated as unencoded and is encoded again.

js

```
const params = new URLSearchParams();

params.append("%24%26", "value");
params.toString(); // "%2524%2526=value"
```

### [Preserving plus signs](#preserving_plus_signs)

The `URLSearchParams` constructor interprets plus signs (`+`) as spaces, which might cause problems. In the example below, we use [hexadecimal escape sequences](/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#hexadecimal_escape_sequences) to mimic a string containing binary data (where every byte carries information) that needs to be stored in the URL search params. Note how the encoded string produced by `btoa()` contains `+` and isn't preserved by `URLSearchParams`.

js

```
const rawData = "\x13à\x17@\x1F\x80";
const base64Data = btoa(rawData); // 'E+AXQB+A'

const searchParams = new URLSearchParams(`bin=${base64Data}`); // 'bin=E+AXQB+A'
const binQuery = searchParams.get("bin"); // 'E AXQB A', '+' is replaced by spaces

console.log(atob(binQuery) === rawData); // false
```

Never construct `URLSearchParams` objects using dynamically interpolated strings. Instead, use the `append()` method, which as mentioned above, interprets all characters as-is.

js

```
const rawData = "\x13à\x17@\x1F\x80";
const base64Data = btoa(rawData); // 'E+AXQB+A'

const searchParams = new URLSearchParams();
searchParams.append("bin", base64Data); // 'bin=E%2BAXQB%2BA'
const binQuery = searchParams.get("bin"); // 'E+AXQB+A'

console.log(atob(binQuery) === rawData); // true
```

### [Interaction with URL.searchParams](#interaction_with_url.searchparams)

The [URL.searchParams](/en-US/docs/Web/API/URL/searchParams) property exposes the URL's [search](/en-US/docs/Web/API/URL/search) string as a `URLSearchParams` object. When updating this `URLSearchParams`, the URL's `search` is updated with its serialization. However, `URL.search` encodes a subset of characters that `URLSearchParams` does, and encodes spaces as `%20` instead of `+`. This may cause some surprising interactions—if you update `searchParams`, even with the same values, the URL may be serialized differently.

js

```
const url = new URL("https://example.com/?a=b ~");
console.log(url.href); // "https://example.com/?a=b%20~"
console.log(url.searchParams.toString()); // "a=b+%7E"
// This should be a no-op, but it changes the URL's query to the
// serialization of its searchParams
url.searchParams.sort();
console.log(url.href); // "https://example.com/?a=b+%7E"

const url2 = new URL("https://example.com?search=1234&param=my%20param");
console.log(url2.search); // "?search=1234&param=my%20param"
url2.searchParams.delete("search");
console.log(url2.search); // "?param=my+param"
```

### [Empty value vs. no value](#empty_value_vs._no_value)

`URLSearchParams` doesn't distinguish between a parameter with nothing after the `=`, and a parameter that doesn't have a `=` altogether.

js

```
const emptyVal = new URLSearchParams("foo=&bar=baz");
console.log(emptyVal.get("foo")); // returns ''
const noEquals = new URLSearchParams("foo&bar=baz");
console.log(noEquals.get("foo")); // also returns ''
console.log(noEquals.toString()); // 'foo=&bar=baz'
```

## [Specifications](#specifications)

Specification
[URL# urlsearchparams](https://url.spec.whatwg.org/#urlsearchparams)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Polyfill of URLSearchParams in core-js](https://github.com/zloirock/core-js#url-and-urlsearchparams)
- The [URL](/en-US/docs/Web/API/URL) interface.
- [Google Developers: Easy URL manipulation with URLSearchParams](https://developer.chrome.com/blog/urlsearchparams/)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 26, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/URLSearchParams/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/urlsearchparams/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FURLSearchParams&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Furlsearchparams%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FURLSearchParams%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Furlsearchparams%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9e678bc410c390f66218d9485ba95b60058dcbd6%0A*+Document+last+modified%3A+2025-02-26T17%3A42%3A53.000Z%0A%0A%3C%2Fdetails%3E)
