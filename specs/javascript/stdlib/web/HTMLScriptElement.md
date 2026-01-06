# HTMLScriptElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLScriptElement&level=high)

HTML [<script>](/en-US/docs/Web/HTML/Reference/Elements/script) elements expose the `HTMLScriptElement` interface, which provides special properties and methods for manipulating the behavior and execution of `<script>` elements (beyond the inherited [HTMLElement](/en-US/docs/Web/API/HTMLElement) interface).

JavaScript files should be served with the `text/javascript`[MIME type](/en-US/docs/Web/HTTP/Guides/MIME_types), but browsers are lenient and block them only if the script is served with an image type (`image/*`), video type (`video/*`), audio type (`audio/*`), or `text/csv`. If the script is blocked, its element receives an [error](/en-US/docs/Web/API/HTMLElement/error_event) event; otherwise, it receives a [load](/en-US/docs/Web/API/Window/load_event) event.

Note: When inserted using the [Document.write()](/en-US/docs/Web/API/Document/write) method, [<script>](/en-US/docs/Web/HTML/Reference/Elements/script) elements execute (typically synchronously), but when inserted using [Element.innerHTML](/en-US/docs/Web/API/Element/innerHTML) or [Element.outerHTML](/en-US/docs/Web/API/Element/outerHTML), they do not execute at all.

## In this article

- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLScriptElement.attributionSrc](/en-US/docs/Web/API/HTMLScriptElement/attributionSrc)Secure contextDeprecated

Gets and sets the [attributionsrc](/en-US/docs/Web/HTML/Reference/Elements/script#attributionsrc) attribute on a [<script>](/en-US/docs/Web/HTML/Reference/Elements/script) element programmatically, reflecting the value of that attribute. `attributionsrc` specifies that you want the browser to send an [Attribution-Reporting-Eligible](/en-US/docs/Web/HTTP/Reference/Headers/Attribution-Reporting-Eligible) header along with the script resource request. On the server-side this is used to trigger sending an [Attribution-Reporting-Register-Source](/en-US/docs/Web/HTTP/Reference/Headers/Attribution-Reporting-Register-Source) or [Attribution-Reporting-Register-Trigger](/en-US/docs/Web/HTTP/Reference/Headers/Attribution-Reporting-Register-Trigger) header in the response, to register a JavaScript-based [attribution source](/en-US/docs/Web/API/Attribution_Reporting_API/Registering_sources#javascript-based_event_sources) or [attribution trigger](/en-US/docs/Web/API/Attribution_Reporting_API/Registering_triggers#javascript-based_attribution_triggers), respectively.

[HTMLScriptElement.async](/en-US/docs/Web/API/HTMLScriptElement/async)

A boolean value that controls how the script should be executed. For classic scripts, if the `async` property is set to `true`, the external script will be fetched in parallel to parsing and evaluated as soon as it is available. For [module scripts](/en-US/docs/Web/JavaScript/Guide/Modules), if the `async` property is set to `true`, the script and all their dependencies will be fetched in parallel to parsing and evaluated as soon as they are available.

[HTMLScriptElement.blocking](/en-US/docs/Web/API/HTMLScriptElement/blocking)

A string indicating that certain operations should be blocked on the fetching of the script. It reflects the `blocking` attribute of the [<script>](/en-US/docs/Web/HTML/Reference/Elements/script) element.

[HTMLScriptElement.charset 
Deprecated](#htmlscriptelement.charset)

A string representing the character encoding of an external script. It reflects the [charset](/en-US/docs/Web/HTML/Reference/Elements/script#charset) attribute.

[HTMLScriptElement.crossOrigin](/en-US/docs/Web/API/HTMLScriptElement/crossOrigin)

A string reflecting the [CORS setting](/en-US/docs/Web/HTML/Reference/Attributes/crossorigin) for the script element. For classic scripts from other [origins](/en-US/docs/Glossary/Origin), this controls if error information will be exposed.

[HTMLScriptElement.defer](/en-US/docs/Web/API/HTMLScriptElement/defer)

A boolean value that controls how the script should be executed. For classic scripts, if the `defer` property is set to `true`, the external script will be executed after the document has been parsed, but before firing [DOMContentLoaded](/en-US/docs/Web/API/Document/DOMContentLoaded_event) event. For [module scripts](/en-US/docs/Web/JavaScript/Guide/Modules), the `defer` property has no effect.

[HTMLScriptElement.event 
Deprecated](#htmlscriptelement.event)

A string; an obsolete way of registering event handlers on elements in an HTML document.

[HTMLScriptElement.fetchPriority](/en-US/docs/Web/API/HTMLScriptElement/fetchPriority)

An optional string representing a hint given to the browser on how it should prioritize fetching of an external script relative to other external scripts. If this value is provided, it must be one of the possible permitted values: `high` to fetch at a high priority, `low` to fetch at a low priority, or `auto` to indicate no preference (which is the default). It reflects the `fetchpriority` attribute of the [<script>](/en-US/docs/Web/HTML/Reference/Elements/script) element.

[HTMLScriptElement.innerText](/en-US/docs/Web/API/HTMLScriptElement/innerText)

A property that represents the inline text content of the [<script>](/en-US/docs/Web/HTML/Reference/Elements/script) element as though it were rendered text. The property accepts either a [TrustedScript](/en-US/docs/Web/API/TrustedScript) object or a string.

[HTMLScriptElement.integrity](/en-US/docs/Web/API/HTMLScriptElement/integrity)

A string that contains inline metadata that a browser can use to verify that a fetched resource has been delivered without unexpected manipulation. It reflects the `integrity` attribute of the [<script>](/en-US/docs/Web/HTML/Reference/Elements/script) element.

[HTMLScriptElement.noModule](/en-US/docs/Web/API/HTMLScriptElement/noModule)

A boolean value that if true, stops the script's execution in browsers that support [ES modules](/en-US/docs/Web/JavaScript/Guide/Modules) — used to run fallback scripts in older browsers that do not support JavaScript modules.

[HTMLScriptElement.referrerPolicy](/en-US/docs/Web/API/HTMLScriptElement/referrerPolicy)

A string that reflects the [referrerPolicy](/en-US/docs/Web/HTML/Reference/Elements/script#referrerpolicy) HTML attribute indicating which referrer to use when fetching the script, and fetches done by that script.

[HTMLScriptElement.src](/en-US/docs/Web/API/HTMLScriptElement/src)

A [TrustedScriptURL](/en-US/docs/Web/API/TrustedScriptURL) or string representing the URL of an external script; this can be used as an alternative to embedding a script directly within a document. It reflects the `src` attribute of the [<script>](/en-US/docs/Web/HTML/Reference/Elements/script) element.

[HTMLScriptElement.text](/en-US/docs/Web/API/HTMLScriptElement/text)

A property that represents the inline text content of the [<script>](/en-US/docs/Web/HTML/Reference/Elements/script) element. The property accepts either a [TrustedScript](/en-US/docs/Web/API/TrustedScript) object or a string. It acts the same way as the [textContent](/en-US/docs/Web/API/HTMLScriptElement/textContent) property.

[HTMLScriptElement.textContent](/en-US/docs/Web/API/HTMLScriptElement/textContent)

A property that represents the inline text content of the [<script>](/en-US/docs/Web/HTML/Reference/Elements/script) element. The property is redefined from [Node](/en-US/docs/Web/API/Node/textContent) to support [TrustedScript](/en-US/docs/Web/API/TrustedScript) as an input. On this element it behaves exactly like the [text](/en-US/docs/Web/API/HTMLScriptElement/text) property.

[HTMLScriptElement.type](/en-US/docs/Web/API/HTMLScriptElement/type)

A string representing the type of the script. It reflects the `type` attribute of the [<script>](/en-US/docs/Web/HTML/Reference/Elements/script) element.

## [Static methods](#static_methods)

[HTMLScriptElement.supports()](/en-US/docs/Web/API/HTMLScriptElement/supports_static)

Returns `true` if the browser supports scripts of the specified type and `false` otherwise. This method provides a simple and unified method for script-related feature detection.

## [Instance methods](#instance_methods)

No specific methods; inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

## [Events](#events)

No specific events; inherits events from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

## [Examples](#examples)

### [Dynamically importing scripts](#dynamically_importing_scripts)

Let's create a function that imports new scripts within a document creating a [<script>](/en-US/docs/Web/HTML/Reference/Elements/script) node immediately before the [<script>](/en-US/docs/Web/HTML/Reference/Elements/script) that hosts the following code (through [document.currentScript](/en-US/docs/Web/API/Document/currentScript)). These scripts will be asynchronously executed. For more details, see the [defer](/en-US/docs/Web/API/HTMLScriptElement/defer) and [async](/en-US/docs/Web/API/HTMLScriptElement/async) properties.

js

```
function loadError(oError) {
  throw new URIError(`The script ${oError.target.src} didn't load correctly.`);
}

function prefixScript(url, onloadFunction) {
  const newScript = document.createElement("script");
  newScript.onerror = loadError;
  if (onloadFunction) {
    newScript.onload = onloadFunction;
  }
  document.currentScript.parentNode.insertBefore(
    newScript,
    document.currentScript,
  );
  newScript.src = url;
}
```

This next function, instead of prepending the new scripts immediately before the [document.currentScript](/en-US/docs/Web/API/Document/currentScript) element, appends them as children of the [<head>](/en-US/docs/Web/HTML/Reference/Elements/head) tag.

js

```
function loadError(oError) {
  throw new URIError(`The script ${oError.target.src} didn't load correctly.`);
}

function affixScriptToHead(url, onloadFunction) {
  const newScript = document.createElement("script");
  newScript.onerror = loadError;
  if (onloadFunction) {
    newScript.onload = onloadFunction;
  }
  document.head.appendChild(newScript);
  newScript.src = url;
}
```

Sample usage:

js

```
affixScriptToHead("myScript1.js");
affixScriptToHead("myScript2.js", () => {
  alert('The script "myScript2.js" has been correctly loaded.');
});
```

### [Checking if a script type is supported](#checking_if_a_script_type_is_supported)

[HTMLScriptElement.supports()](/en-US/docs/Web/API/HTMLScriptElement/supports_static) provides a unified mechanism for checking whether a browser supports particular types of scripts.

The example below shows how to check for module support, using the existence of the `noModule` attribute as a fallback.

js

```
function checkModuleSupport() {
  if ("supports" in HTMLScriptElement) {
    return HTMLScriptElement.supports("module");
  }
  return "noModule" in document.createElement("script");
}
```

Classic scripts are assumed to be supported on all browsers.

## [Specifications](#specifications)

Specification
[HTML# htmlscriptelement](https://html.spec.whatwg.org/multipage/scripting.html#htmlscriptelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- HTML [<script>](/en-US/docs/Web/HTML/Reference/Elements/script) element
- HTML [<noscript>](/en-US/docs/Web/HTML/Reference/Elements/noscript) element
- [document.currentScript](/en-US/docs/Web/API/Document/currentScript)
- [Web Workers](/en-US/docs/Web/API/Web_Workers_API/Using_web_workers) (code snippets similar to scripts but executed in [another global context](/en-US/docs/Web/API/DedicatedWorkerGlobalScope))

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLScriptElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlscriptelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLScriptElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlscriptelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLScriptElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlscriptelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe936e7271df947f25184a5ba8a21445bbd4d056c%0A*+Document+last+modified%3A+2025-12-13T02%3A55%3A18.000Z%0A%0A%3C%2Fdetails%3E)
