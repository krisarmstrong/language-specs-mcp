# Summarizer API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSummarizer_API&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The Summarizer API summarizes a given body of text via a browser's internal AI model (which may differ between browsers).

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [HTTP headers](#http_headers)
- [Security considerations](#security_considerations)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

Writing a summary of a larger body of text is a common writing task, and one that AI is well-suited to. Typical use cases include:

- Providing a summary of a full article so the reader can judge whether to read the whole thing.
- Summarizing a meeting transcript so those joining the meeting late can get up to speed with what they've missed.
- Summarizing a set of product reviews to quickly communicate overall sentiment.

The Summarizer API provides an asynchronous ([Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)-based) mechanism for a website to feed a body of text into the browser's own internal AI model and request that it returns a summary of the text based on specified options.

This is done using the functionality made available by the [Summarizer](/en-US/docs/Web/API/Summarizer) interface, in a two-step process:

1. Create a `Summarizer` object instance using the [Summarizer.create()](/en-US/docs/Web/API/Summarizer/create_static) static method, specifying options for what kind of summary you want written. Options include length, type (for example, "tldr" or key points), format (plain text or markdown), and input and output languages. 

Note: If you want to check whether the browser AI model is able to support your preferences, you can do so with the [Summarizer.availability()](/en-US/docs/Web/API/Summarizer/availability_static) static method.

2. Run the [Summarizer.summarize()](/en-US/docs/Web/API/Summarizer/summarize) instance method to request the summary.

You can cancel a pending `create()` or `summarize()` operation using an [AbortController](/en-US/docs/Web/API/AbortController).

After a `Summarizer` instance has been created, you can release its assigned resources and stop any further activity by calling its [Summarizer.destroy()](/en-US/docs/Web/API/Summarizer/destroy) method. You are encouraged to do this after you've finished with the `Summarizer` object as it can consume a lot of resources.

See [Using the Summarizer API](/en-US/docs/Web/API/Summarizer_API/Using) for a walkthrough of how the API works.

## [Interfaces](#interfaces)

[Summarizer](/en-US/docs/Web/API/Summarizer)Experimental

Contains all the functionality for the Summarizer API, including checking AI model availability, creating a new `Summarizer` instance, using it to generate a new summary, and more.

## [HTTP headers](#http_headers)

[Permissions-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy); the [summarizer](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/summarizer) directive

Controls access to the Summarizer API. Where a policy specifically disallows the use of the Summarizer API, any attempts to call the API's methods will fail with a `NotAllowedError`[DOMException](/en-US/docs/Web/API/DOMException).

## [Security considerations](#security_considerations)

The specification requires that a user has recently interacted with the page when creating `Summarizer` objects ([transient user activation](/en-US/docs/Web/Security/Defenses/User_activation) is required).

In addition, the specification controls access to the API via [summarizer](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/summarizer)[Permissions-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy) directives.

## [Examples](#examples)

For a full example, see [Using the Summarizer API](/en-US/docs/Web/API/Summarizer_API/Using).

## [Specifications](#specifications)

Specification
[Writing Assistance APIs# summarizer-api](https://webmachinelearning.github.io/writing-assistance-apis/#summarizer-api)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Summarize with built-in AI](https://developer.chrome.com/docs/ai/summarizer-api) on developer.chrome.com (2025)
- [Web AI demos](https://chrome.dev/web-ai-demos/) on chrome.dev

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Summarizer_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/summarizer_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSummarizer_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsummarizer_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSummarizer_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsummarizer_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca26363fcc6fc861103d40ac0205e5c5b79eb2fa%0A*+Document+last+modified%3A+2025-11-30T02%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
