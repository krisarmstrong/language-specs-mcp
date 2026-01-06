# URLPattern

 Baseline  2025 Newly available

 Since ⁨September 2025⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FURLPattern&level=low)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `URLPattern` interface of the [URL Pattern API](/en-US/docs/Web/API/URL_Pattern_API) matches URLs or parts of URLs against a pattern. The pattern can contain capturing groups that extract parts of the matched URL.

More information about the syntax of patterns can be found on the API overview page: [URL Pattern API](/en-US/docs/Web/API/URL_Pattern_API).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[URLPattern()](/en-US/docs/Web/API/URLPattern/URLPattern)

Returns a new `URLPattern` object based on the given pattern and base URL.

## [Instance properties](#instance_properties)

[hash](/en-US/docs/Web/API/URLPattern/hash)Read only

A string containing a pattern to match the hash part of a URL.

[hasRegExpGroups](/en-US/docs/Web/API/URLPattern/hasRegExpGroups)Read only

A boolean indicating whether or not any of the `URLPattern` components contain [regular expression capturing groups](/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Groups_and_backreferences).

[hostname](/en-US/docs/Web/API/URLPattern/hostname)Read only

A string containing a pattern to match the hostname part of a URL.

[password](/en-US/docs/Web/API/URLPattern/password)Read only

A string containing a pattern to match the password part of a URL.

[pathname](/en-US/docs/Web/API/URLPattern/pathname)Read only

A string containing a pattern to match the pathname part of a URL.

[port](/en-US/docs/Web/API/URLPattern/port)Read only

A string containing a pattern to match the port part of a URL.

[protocol](/en-US/docs/Web/API/URLPattern/protocol)Read only

A string containing a pattern to match the protocol part of a URL.

[search](/en-US/docs/Web/API/URLPattern/search)Read only

A string containing a pattern to match the search part of a URL.

[username](/en-US/docs/Web/API/URLPattern/username)Read only

A string containing a pattern to match the username part of a URL.

## [Instance methods](#instance_methods)

[exec()](/en-US/docs/Web/API/URLPattern/exec)

Returns an object with the matched parts of the URL or `null` if the URL does not match.

[test()](/en-US/docs/Web/API/URLPattern/test)

Returns `true` if the URL matches the given pattern, `false` otherwise.

## [Specifications](#specifications)

Specification
[URL Pattern# urlpattern](https://urlpattern.spec.whatwg.org/#urlpattern)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- A polyfill of `URLPattern` is available [on GitHub](https://github.com/kenchris/urlpattern-polyfill)
- The pattern syntax used by URLPattern is similar to the syntax used by [path-to-regexp](https://github.com/pillarjs/path-to-regexp)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/URLPattern/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/urlpattern/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FURLPattern&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Furlpattern%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FURLPattern%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Furlpattern%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Faafad07220c63481570e43cc66a5d9fb7b985ffc%0A*+Document+last+modified%3A+2025-07-03T23%3A37%3A37.000Z%0A%0A%3C%2Fdetails%3E)
