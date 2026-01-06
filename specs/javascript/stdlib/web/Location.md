# Location

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FLocation&level=high)

The `Location` interface represents the location (URL) of the object it is linked to. Changes done on it are reflected on the object it relates to. Both the [Document](/en-US/docs/Web/API/Document) and [Window](/en-US/docs/Web/API/Window) interface have such a linked `Location`, accessible via [Document.location](/en-US/docs/Web/API/Document/location) and [Window.location](/en-US/docs/Web/API/Window/location) respectively.

## In this article

- [Location anatomy](#location_anatomy)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Location anatomy](#location_anatomy)

Hover over the URL segments below to highlight their meaning:

```
<span id="href" title="href"
  ><span id="origin" title="origin"
    ><span id="protocol" title="protocol">https:</span>//<span
      id="host"
      title="host"
      ><span id="hostname" title="hostname">example.org</span>:<span
        id="port"
        title="port"
        >8080</span
      ></span
    ></span
  ><span id="pathname" title="pathname">/foo/bar</span
  ><span id="search" title="search">?q=baz</span
  ><span id="hash" title="hash">#bang</span></span
>
```

```
html {
  display: table;
  width: 100%;
}

body {
  display: table-cell;
  text-align: center;
  vertical-align: middle;
  font-family: "Georgia";
  font-size: 200%;
  line-height: 1em;
  white-space: nowrap;
}

[title] {
  position: relative;
  display: inline-block;
  box-sizing: border-box;
  line-height: 2em;
  cursor: pointer;
  color: gray;
}

[title]::before {
  content: attr(title);
  font-family: monospace;
  position: absolute;
  top: 100%;
  width: 100%;
  left: 50%;
  margin-left: -50%;
  font-size: 50%;
  line-height: 1.5;
  background: black;
}

[title]:hover::before,
:target::before {
  background: black;
  color: yellow;
}

[title] [title]::before {
  margin-top: 1.5em;
}

[title] [title] [title]::before {
  margin-top: 3em;
}

[title] [title] [title] [title]::before {
  margin-top: 4.5em;
}

[title]:hover,
:target {
  position: relative;
  z-index: 1;
  outline: 50em solid rgb(255 255 255 / 80%);
}
```

```
document.body.addEventListener("click", (event) => {
  event.preventDefault();

  window.location.hash = event.target.hasAttribute("id")
    ? `#${event.target.getAttribute("id")}`
    : "";
});
```

## [Instance properties](#instance_properties)

[Location.ancestorOrigins](/en-US/docs/Web/API/Location/ancestorOrigins)Read only

A static [DOMStringList](/en-US/docs/Web/API/DOMStringList) containing, in reverse order, the origins of all ancestor browsing contexts of the document associated with the given `Location` object.

[Location.href](/en-US/docs/Web/API/Location/href)

A [stringifier](/en-US/docs/Glossary/Stringifier) that returns a string containing the entire URL. If changed, the associated document navigates to the new page. It can be set from a different origin than the associated document.

[Location.protocol](/en-US/docs/Web/API/Location/protocol)

A string containing the protocol scheme of the URL, including the final `':'`.

[Location.host](/en-US/docs/Web/API/Location/host)

A string containing the host, that is the hostname, a `':'`, and the port of the URL.

[Location.hostname](/en-US/docs/Web/API/Location/hostname)

A string containing the domain of the URL.

[Location.port](/en-US/docs/Web/API/Location/port)

A string containing the port number of the URL.

[Location.pathname](/en-US/docs/Web/API/Location/pathname)

A string containing an initial `'/'` followed by the path of the URL, not including the query string or fragment.

[Location.search](/en-US/docs/Web/API/Location/search)

A string containing a `'?'` followed by the parameters or "query string" of the URL. Modern browsers provide [URLSearchParams](/en-US/docs/Web/API/URLSearchParams/get) and [URL.searchParams](/en-US/docs/Web/API/URL/searchParams) to make it easy to parse out the parameters from the query string.

[Location.hash](/en-US/docs/Web/API/Location/hash)

A string containing a `'#'` followed by the fragment identifier of the URL.

[Location.origin](/en-US/docs/Web/API/Location/origin)Read only

Returns a string containing the canonical form of the origin of the specific location.

## [Instance methods](#instance_methods)

[Location.assign()](/en-US/docs/Web/API/Location/assign)

Loads the resource at the URL provided in parameter.

[Location.reload()](/en-US/docs/Web/API/Location/reload)

Reloads the current URL, like the Refresh button.

[Location.replace()](/en-US/docs/Web/API/Location/replace)

Replaces the current resource with the one at the provided URL (redirects to the provided URL). The difference from the `assign()` method and setting the `href` property is that after using `replace()` the current page will not be saved in session [History](/en-US/docs/Web/API/History), meaning the user won't be able to use the back button to navigate to it.

[Location.toString()](/en-US/docs/Web/API/Location/toString)

Returns a string containing the whole URL. It is a synonym for [Location.href](/en-US/docs/Web/API/Location/href), though it can't be used to modify the value.

## [Examples](#examples)

js

```
// location: https://developer.mozilla.org:8080/en-US/search?q=URL#search-results-close-container
const loc = document.location;
console.log(loc.href); // https://developer.mozilla.org:8080/en-US/search?q=URL#search-results-close-container
console.log(loc.protocol); // https:
console.log(loc.host); // developer.mozilla.org:8080
console.log(loc.hostname); // developer.mozilla.org
console.log(loc.port); // 8080
console.log(loc.pathname); // /en-US/search
console.log(loc.search); // ?q=URL
console.log(loc.hash); // #search-results-close-container
console.log(loc.origin); // https://developer.mozilla.org:8080

location.assign("http://another.site"); // load another page
```

## [Specifications](#specifications)

Specification
[HTML# the-location-interface](https://html.spec.whatwg.org/multipage/nav-history-apis.html#the-location-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- Two `Location` properties: [Window.location](/en-US/docs/Web/API/Window/location) and [Document.location](/en-US/docs/Web/API/Document/location).
- URL manipulation interfaces: [URL](/en-US/docs/Web/API/URL) and [URLSearchParams](/en-US/docs/Web/API/URLSearchParams).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Location/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/location/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FLocation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Flocation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FLocation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Flocation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9cfc2285428932f448a1747e347b1e35a3e0172b%0A*+Document+last+modified%3A+2025-10-13T00%3A33%3A39.000Z%0A%0A%3C%2Fdetails%3E)
