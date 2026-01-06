# URL

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FURL&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `URL` interface is used to parse, construct, normalize, and encode [URLs](/en-US/docs/Glossary/URL). It works by providing properties which allow you to easily read and modify the components of a URL.

You normally create a new `URL` object by specifying the URL as a string when calling its constructor, or by providing a relative URL and a base URL. You can then easily read the parsed components of the URL or make changes to the URL.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Usage notes](#usage_notes)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[URL()](/en-US/docs/Web/API/URL/URL)

Creates and returns a `URL` object from a URL string and optional base URL string. Throws if the passed arguments don't define a valid URL.

## [Instance properties](#instance_properties)

[hash](/en-US/docs/Web/API/URL/hash)

A string containing a `'#'` followed by the fragment identifier of the URL.

[host](/en-US/docs/Web/API/URL/host)

A string containing the domain (that is the hostname) followed by (if a port was specified) a `':'` and the port of the URL.

[hostname](/en-US/docs/Web/API/URL/hostname)

A string containing the domain of the URL.

[href](/en-US/docs/Web/API/URL/href)

A [stringifier](/en-US/docs/Glossary/Stringifier) that returns a string containing the whole URL.

[origin](/en-US/docs/Web/API/URL/origin)Read only

Returns a string containing the origin of the URL, that is its scheme, its domain and its port.

[password](/en-US/docs/Web/API/URL/password)

A string containing the password specified before the domain name.

[pathname](/en-US/docs/Web/API/URL/pathname)

A string containing an initial `'/'` followed by the path of the URL, not including the query string or fragment.

[port](/en-US/docs/Web/API/URL/port)

A string containing the port number of the URL.

[protocol](/en-US/docs/Web/API/URL/protocol)

A string containing the protocol scheme of the URL, including the final `':'`.

[search](/en-US/docs/Web/API/URL/search)

A string indicating the URL's parameter string; if any parameters are provided, this string includes all of them, beginning with the leading `?` character.

[searchParams](/en-US/docs/Web/API/URL/searchParams)Read only

A [URLSearchParams](/en-US/docs/Web/API/URLSearchParams) object which can be used to access the individual query parameters found in `search`.

[username](/en-US/docs/Web/API/URL/username)

A string containing the username specified before the domain name.

## [Static methods](#static_methods)

[canParse()](/en-US/docs/Web/API/URL/canParse_static)

Returns a boolean indicating whether or not a URL defined from a URL string and optional base URL string is parsable and valid.

[createObjectURL()](/en-US/docs/Web/API/URL/createObjectURL_static)

Returns a string containing a unique blob URL, that is a URL with `blob:` as its scheme, followed by an opaque string uniquely identifying the object in the browser.

[parse()](/en-US/docs/Web/API/URL/parse_static)

Creates and returns a `URL` object from a URL string and optional base URL string, or returns `null` if the passed parameters define an invalid `URL`.

[revokeObjectURL()](/en-US/docs/Web/API/URL/revokeObjectURL_static)

Revokes an object URL previously created using [URL.createObjectURL()](/en-US/docs/Web/API/URL/createObjectURL_static).

## [Instance methods](#instance_methods)

[toString()](/en-US/docs/Web/API/URL/toString)

Returns a string containing the whole URL. It is a synonym for [URL.href](/en-US/docs/Web/API/URL/href), though it can't be used to modify the value.

[toJSON()](/en-US/docs/Web/API/URL/toJSON)

Returns a string containing the whole URL. It returns the same string as the `href` property.

## [Usage notes](#usage_notes)

The constructor takes a `url` parameter, and an optional `base` parameter to use as a base if the `url` parameter is a relative URL:

js

```
const url = new URL("../cats", "http://www.example.com/dogs");
console.log(url.hostname); // "www.example.com"
console.log(url.pathname); // "/cats"
```

The constructor will raise an exception if the URL cannot be parsed to a valid URL. You can either call the above code in a [try...catch](/en-US/docs/Web/JavaScript/Reference/Statements/try...catch) block or use the [canParse()](/en-US/docs/Web/API/URL/canParse_static) static method to first check the URL is valid:

js

```
if (URL.canParse("../cats", "http://www.example.com/dogs")) {
  const url = new URL("../cats", "http://www.example.com/dogs");
  console.log(url.hostname); // "www.example.com"
  console.log(url.pathname); // "/cats"
} else {
  console.log("Invalid URL");
}
```

URL properties can be set to construct the URL:

js

```
url.hash = "tabby";
console.log(url.href); // "http://www.example.com/cats#tabby"
```

URLs are encoded according to the rules found in [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986). For instance:

js

```
url.pathname = "démonstration.html";
console.log(url.href); // "http://www.example.com/d%C3%A9monstration.html"
```

The [URLSearchParams](/en-US/docs/Web/API/URLSearchParams) interface can be used to build and manipulate the URL query string.

To get the search params from the current window's URL, you can do this:

js

```
// https://some.site/?id=123
const parsedUrl = new URL(window.location.href);
console.log(parsedUrl.searchParams.get("id")); // "123"
```

The [toString()](/en-US/docs/Web/API/URL/toString) method of `URL` just returns the value of the [href](/en-US/docs/Web/API/URL/href) property, so the constructor can be used to normalize and encode a URL directly.

js

```
const response = await fetch(
  new URL("http://www.example.com/démonstration.html"),
);
```

## [Specifications](#specifications)

Specification
[URL# url](https://url.spec.whatwg.org/#url)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Polyfill of URL in core-js](https://github.com/zloirock/core-js#url-and-urlsearchparams)
- [URL API](/en-US/docs/Web/API/URL_API)
- [What is a URL?](/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL)
- [URLSearchParams](/en-US/docs/Web/API/URLSearchParams).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/URL/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/url/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FURL&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Furl%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FURL%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Furl%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F77d90a23ee0a3b5486a7963f68ad4e56efb06a7b%0A*+Document+last+modified%3A+2025-04-27T18%3A17%3A43.000Z%0A%0A%3C%2Fdetails%3E)
