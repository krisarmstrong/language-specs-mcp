# DOMHighResTimeStamp

The `DOMHighResTimeStamp` type is a `double` and is used to store a time value in milliseconds.

This type can be used to describe a discrete point in time or a time interval (the difference in time between two discrete points in time). The starting time can be either a specific time determined by the script for a site or app, or the [time origin](/en-US/docs/Web/API/Performance/timeOrigin).

The time, given in milliseconds, should be accurate to 5 µs (microseconds), with the fractional part of the number indicating fractions of a millisecond. However, if the browser is unable to provide a time value accurate to 5 µs (due, for example, to hardware or software constraints), the browser can represent the value as a time in milliseconds accurate to a millisecond. Also note the section below on reduced time precision controlled by browser preferences to avoid timing attacks and [fingerprinting](/en-US/docs/Glossary/Fingerprinting).

Further, if the device or operating system the user agent is running on doesn't have a clock accurate to the microsecond level, they may only be accurate to the millisecond.

## In this article

- [Security requirements](#security_requirements)
- [Specifications](#specifications)
- [See also](#see_also)

## [Security requirements](#security_requirements)

To offer protection against timing attacks and [fingerprinting](/en-US/docs/Glossary/Fingerprinting), `DOMHighResTimeStamp` types are coarsened based on site isolation status.

- Resolution in isolated contexts: 5 microseconds
- Resolution in non-isolated contexts: 100 microseconds

Cross-origin isolate your site using the [Cross-Origin-Opener-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Opener-Policy) and [Cross-Origin-Embedder-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Embedder-Policy) headers:

http

```
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Embedder-Policy: require-corp
```

These headers ensure a top-level document does not share a browsing context group with cross-origin documents. COOP process-isolates your document and potential attackers can't access to your global object if they were opening it in a popup, preventing a set of cross-origin attacks dubbed [XS-Leaks](https://github.com/xsleaks/xsleaks).

## [Specifications](#specifications)

Specification
[High Resolution Time# dom-domhighrestimestamp](https://w3c.github.io/hr-time/#dom-domhighrestimestamp)

## [See also](#see_also)

- [performance.now()](/en-US/docs/Web/API/Performance/now)
- [performance.timeOrigin](/en-US/docs/Web/API/Performance/timeOrigin)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 19, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/DOMHighResTimeStamp/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/domhighrestimestamp/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMHighResTimeStamp&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdomhighrestimestamp%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMHighResTimeStamp%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdomhighrestimestamp%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0496bb2fcef13172325e1cc25a5fc71410506557%0A*+Document+last+modified%3A+2024-08-19T02%3A57%3A14.000Z%0A%0A%3C%2Fdetails%3E)
