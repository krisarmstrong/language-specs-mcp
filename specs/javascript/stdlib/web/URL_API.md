# URL API

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The URL API is a component of the URL standard, which defines what constitutes a valid [Uniform Resource Locator](/en-US/docs/Glossary/URL) and the API that accesses and manipulates URLs. The URL standard also defines concepts such as domains, hosts, and IP addresses, and also attempts to describe in a standard way the legacy `application/x-www-form-urlencoded`[MIME type](/en-US/docs/Glossary/MIME_type) used to submit web forms' contents as a set of key/value pairs.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

The majority of the URL standard is taken up by the [definition of a URL](/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL) and how it is structured and parsed. Also covered are definitions of various terms related to addressing of computers on a network, and the algorithms for parsing IP addresses and DOM addresses are specified. More interesting to most developers is the API itself.

### [Accessing URL components](#accessing_url_components)

Creating an [URL](/en-US/docs/Web/API/URL) object for a given URL parses the URL and provides quick access to its constituent parts through its properties.

js

```
let addr = new URL("https://developer.mozilla.org/en-US/docs/Web/API/URL_API");
let host = addr.host;
let path = addr.pathname;
```

The snippet above creates a `URL` object for the article you're reading right now, then fetches the [host](/en-US/docs/Web/API/URL/host) and [pathname](/en-US/docs/Web/API/URL/pathname) properties. In this case, those strings are `developer.mozilla.org` and `/en-US/docs/Web/API/URL_API`, respectively.

### [Changing the URL](#changing_the_url)

Most of the properties of `URL` are settable; you can write new values to them to alter the URL represented by the object. For example, to create a URL and set its username:

js

```
let myUsername = "some-guy";
let addr = new URL("https://example.com/login");
addr.username = myUsername;
```

Setting the value of [username](/en-US/docs/Web/API/URL/username) not only sets that property's value, but it updates the overall URL. After executing the code snippet above, the value returned by [href](/en-US/docs/Web/API/URL/href) is `https://some-guy@example.com/login`. This is true for any of the writable properties.

### [Queries](#queries)

The [search](/en-US/docs/Web/API/URL/search) property on a `URL` contains the query string portion of the URL. For example, if the URL is `https://example.com/login?user=some-guy&page=news`, then the value of the `search` property is `?user=some-guy&page=news`. You can also look up the values of individual parameters with the [URLSearchParams](/en-US/docs/Web/API/URLSearchParams) object's [get()](/en-US/docs/Web/API/URLSearchParams/get) method:

js

```
let addr = new URL("https://example.com/login?user=some-guy&page=news");
try {
  loginUser(addr.searchParams.get("user"));
  gotoPage(addr.searchParams.get("page"));
} catch (err) {
  showErrorMessage(err);
}
```

For example, in the above snippet, the username and target page are taken from the query and passed to appropriate functions that are used by the site's code to log in and route the user to their desired destination within the site.

Other functions within `URLSearchParams` let you change the value of keys, add and delete keys and their values, and even sort the list of parameters.

## [Interfaces](#interfaces)

The URL API is a simple one, with only a couple of interfaces to its name:

[URL](/en-US/docs/Web/API/URL)

Can be used to parse, construct, normalize, and encode [URLs](/en-US/docs/Glossary/URL).

[URLSearchParams](/en-US/docs/Web/API/URLSearchParams)

Defines utility methods to work with the query string of a URL.

## [Examples](#examples)

### [Parsing URL parameters using the URL API](#parsing_url_parameters_using_the_url_api)

You could process URL parameters by parsing a URL as a string, splitting it on certain characters or using regular expressions, but it's much easier to create a new `URL` object for this. The example below gets the document URL from [document.location.href](/en-US/docs/Web/API/Document/location), sorts the parameters using [URLSearchParams.sort()](/en-US/docs/Web/API/URLSearchParams/sort), then extracts the keys using `URLSearchParams.keys`.

For each key in the document URL, we add rows to a [<table>](/en-US/docs/Web/HTML/Reference/Elements/table) element, one for each key found in the parameters, with the first column containing the key's name, and the second column containing the value:

js

```
const table = document.querySelector(".param-table");

const url = new URL(document.location.href);
url.searchParams.sort();
const keys = url.searchParams.keys();

for (let key of keys) {
  let val = url.searchParams.get(key);
  let row = document.createElement("tr");
  let cell = document.createElement("td");
  cell.innerText = key;
  row.appendChild(cell);
  cell = document.createElement("td");
  cell.innerText = val;
  row.appendChild(cell);
  table.appendChild(row);
}
```

You can try a [live version of this example](https://mdn.github.io/dom-examples/url-params/) and [view the full source code on GitHub](https://github.com/mdn/dom-examples/tree/main/url-params).

## [Specifications](#specifications)

Specification
[URL# api](https://url.spec.whatwg.org/#api)

## [Browser compatibility](#browser_compatibility)

### [api.URL](#api.URL)

### [api.URLSearchParams](#api.URLSearchParams)

## [See also](#see_also)

- [Fetch API](/en-US/docs/Web/API/Fetch_API)
- CSS [<url>](/en-US/docs/Web/CSS/Reference/Values/url_value) type
- [encodeURI()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI)
- [encodeURIComponent()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 4, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/URL_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/url_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FURL_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Furl_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FURL_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Furl_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F11c356e4d1021b204c0d3e4bc41a571877215367%0A*+Document+last+modified%3A+2025-07-04T12%3A22%3A42.000Z%0A%0A%3C%2Fdetails%3E)
