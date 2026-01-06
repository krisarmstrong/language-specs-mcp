# Console API

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FConsole_API&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The Console API provides functionality to allow developers to perform debugging tasks, such as logging messages or the values of variables at set points in your code, or timing how long an operation takes to complete.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

The Console API started as a largely proprietary API, with different browsers implementing it, albeit in inconsistent ways. [The Console API spec](https://console.spec.whatwg.org/) was created to define consistent behavior, and all modern browsers eventually settled on implementing this behavior — although some implementations still have their own additional proprietary functions. Find out about these at:

- [Google Chrome DevTools implementation](https://developer.chrome.com/docs/devtools/console/api/)
- [Safari DevTools implementation](https://webkit.org/web-inspector/console-object-api/)

Usage is very simple — the [console](/en-US/docs/Web/API/console) object contains many methods that you can call to perform rudimentary debugging tasks, generally focused around logging various values to the browser's [Web Console](https://firefox-source-docs.mozilla.org/devtools-user/web_console/index.html).

By far the most commonly-used method is [console.log()](/en-US/docs/Web/API/console/log_static), which is used to log the current value contained inside a specific variable.

## [Interfaces](#interfaces)

[console](/en-US/docs/Web/API/console)

Provides rudimentary debugging functionality, including logging, stack traces, timers, and counters.

## [Examples](#examples)

js

```
let myString = "Hello world";

// Output "Hello world" to the console
console.log(myString);
```

See the [console](/en-US/docs/Web/API/console) reference page for more examples.

## [Specifications](#specifications)

Specification
[Console# console-namespace](https://console.spec.whatwg.org/#console-namespace)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Tools](https://firefox-source-docs.mozilla.org/devtools-user/index.html)
- [Web Console](https://firefox-source-docs.mozilla.org/devtools-user/web_console/index.html) — how the Web Console in Firefox handles console API calls
- [about:debugging](https://firefox-source-docs.mozilla.org/devtools-user/about_colon_debugging/index.html) — how to see console output when the debugging target is a mobile device

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 25, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Console_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/console_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FConsole_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fconsole_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FConsole_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fconsole_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F534dcf8cc401ead0b9514f8a2f1fa4c8cf5b5e64%0A*+Document+last+modified%3A+2024-10-25T05%3A14%3A16.000Z%0A%0A%3C%2Fdetails%3E)
