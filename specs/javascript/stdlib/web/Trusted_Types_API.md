# Trusted Types API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTrusted_Types_API&level=not)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The Trusted Types API gives web developers a way to ensure that input has been passed through a user-specified transformation function before being passed to an API that might execute that input. This can help to protect against client-side [cross-site scripting (XSS)](/en-US/docs/Web/Security/Attacks/XSS) attacks. Most commonly the transformation function [sanitizes](/en-US/docs/Web/Security/Attacks/XSS#sanitization) the input.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

Client-side, or DOM-based, XSS attacks happen when data crafted by an attacker is passed to a browser API that executes that data as code. These APIs are known as [injection sinks](#injection_sink_interfaces).

The Trusted Types API distinguishes three sorts of injection sinks:

- HTML sinks: APIs that interpret their input as HTML, such as [Element.innerHTML](/en-US/docs/Web/API/Element/innerHTML) or [document.write()](/en-US/docs/Web/API/Document/write). These APIs could execute JavaScript if it is embedded in the HTML, for example in [<script>](/en-US/docs/Web/HTML/Reference/Elements/script) tags or event handler attributes.
- JavaScript sinks: APIs that interpret their input as JavaScript, such as [eval()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval) or [HTMLScriptElement.text](/en-US/docs/Web/API/HTMLScriptElement/text).
- JavaScript URL sinks: APIs that interpret their input as the URL of a script, such as [HTMLScriptElement.src](/en-US/docs/Web/API/HTMLScriptElement/src).

One of the main defenses against DOM-based XSS attacks is to ensure that input is made safe before being passed to an injection sink.

In the Trusted Types API, a developer defines a policy object, which contains methods that transform input bound for an injection sink so as to make it safe. The policy can define different methods for the different types of sink:

- For HTML sinks, the transformation function typically [sanitizes](/en-US/docs/Web/Security/Attacks/XSS#sanitization) the input, for example by using a library like [DOMPurify](https://github.com/cure53/DOMPurify).
- For JavaScript and JavaScript URL sinks, the policy may turn off the sinks entirely or allow certain predefined inputs (for example, specific URLs).

The Trusted Types API will then ensure that input is passed through the appropriate transformation function before being passed into the sink.

That is, the API enables you to define your policy in one place and then be assured that any data passed to an injection sink has been passed through the policy.

Note:

The Trusted Types API does not itself supply a policy or any transformation functions: the developer defines their own policy, which contains the transformations that they wish to apply.

The API has two main parts:

- A JavaScript API enables a developer to sanitize data before passing it to an injection sink.
- Two [CSP](/en-US/docs/Web/HTTP/Guides/CSP) directives enforce and control the usage of the JavaScript API.

### [The Trusted Types JavaScript API](#the_trusted_types_javascript_api)

In the Trusted Types API:

- The `trustedTypes` global property, available in both [Window](/en-US/docs/Web/API/Window/trustedTypes) and [Worker](/en-US/docs/Web/API/WorkerGlobalScope/trustedTypes) contexts, is used to create [TrustedTypePolicy](/en-US/docs/Web/API/TrustedTypePolicy) objects.
- A [TrustedTypePolicy](/en-US/docs/Web/API/TrustedTypePolicy) object is used to create trusted type objects: it will do this by passing the data through a transformation function.
- Trusted type objects represent data that has been through the policy, and can therefore be safely passed to an injection sink. There are three sorts of trusted type, corresponding to the different sort of injection sink: 

  - [TrustedHTML](/en-US/docs/Web/API/TrustedHTML) is for passing to a sink that will render the data as HTML.
  - [TrustedScript](/en-US/docs/Web/API/TrustedScript) is for passing to a sink that will execute the data as JavaScript.
  - [TrustedScriptURL](/en-US/docs/Web/API/TrustedScriptURL) is for passing to a sink that will parse the data as a URL to a script.

With this API, instead of passing a string to an injection sink like `innerHTML`, you use a `TrustedTypePolicy` to create a `TrustedHTML` object from the string, then pass that into the sink, and can be sure that the string has been passed through a transformation function.

For example, this code creates a `TrustedTypePolicy` that can create `TrustedHTML` objects by sanitizing the input strings with the [DOMPurify](https://github.com/cure53/DOMPurify) library:

js

```
const policy = trustedTypes.createPolicy("my-policy", {
  createHTML: (input) => DOMPurify.sanitize(input),
});
```

Next, you can use this `policy` object to create a `TrustedHTML` object, and pass that object into the injection sink:

js

```
const userInput = "<p>I might be XSS</p>";
const element = document.querySelector("#container");

const trustedHTML = policy.createHTML(userInput);
element.innerHTML = trustedHTML;
```

### [Using a CSP to enforce trusted types](#using_a_csp_to_enforce_trusted_types)

The API described above enables you to sanitize data, but it doesn't ensure that your code never passes input directly to an injection sink: that is, it doesn't stop you passing a string into `innerHTML`.

In order to enforce that a trusted type must always be passed, you include the [require-trusted-types-for](/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/require-trusted-types-for) directive in your [CSP](/en-US/docs/Web/HTTP/Guides/CSP). With this directive set, passing strings into injection sinks will result in a `TypeError` exception:

js

```
const userInput = "<p>I might be XSS</p>";
const element = document.querySelector("#container");

element.innerHTML = userInput; // Throws a TypeError
```

Additionally, the [trusted-types](/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/trusted-types) CSP directive can be used to control which policies your code is allowed to create. When you create a policy using [trustedTypes.createPolicy()](/en-US/docs/Web/API/TrustedTypePolicyFactory/createPolicy), you pass a name for the policy. The `trusted-types` CSP directive lists acceptable policy names, so `createPolicy()` will throw an exception if it is passed a name which was not listed in `trusted-types`. This prevents some code in your web application from creating a policy that you were not expecting.

### [The default policy](#the_default_policy)

In the Trusted Types API, you can define a default policy. This helps you find any places in your code where you're still passing strings into injection sinks, so you can rewrite the code to create and pass trusted types instead.

If you create a policy named `"default"`, and your CSP enforces the use of trusted types, then any string argument passed into injection sinks will be automatically passed to this policy. For example, suppose we create a policy like this:

js

```
trustedTypes.createPolicy("default", {
  createHTML(value) {
    console.log("Please refactor this code");
    return sanitize(value);
  },
});
```

With this policy, if your code assigns a string to `innerHTML`, the browser will call the policy's `createHTML()` method and assign its result to the sink:

js

```
const userInput = "<p>I might be XSS</p>";
const element = document.querySelector("#container");

element.innerHTML = userInput;
// Logs "Please refactor this code"
// Assigns the result of sanitize(userInput)
```

If the default policy returned `null` or `undefined`, then the browser will throw a `TypeError` when assigning the result to the sink:

js

```
trustedTypes.createPolicy("default", {
  createHTML(value) {
    console.log("Please refactor this code");
    return null;
  },
});

const userInput = "<p>I might be XSS</p>";
const element = document.querySelector("#container");

element.innerHTML = userInput;
// Logs "Please refactor this code"
// Throws a TypeError
```

Note: It's recommended that you use the default policy only while you are transitioning from legacy code that passes input directly to injection sinks, to code that uses trusted types explicitly.

### [Injection sink interfaces](#injection_sink_interfaces)

This section provides a list of "direct" injection sink interfaces.

Note that there are cases where untrusted strings may be "indirectly injected", such as when an untrusted string is added as the child node of a script element, and then the element is added to the document. These cases are evaluated the untrusted script is added to the document.

#### TrustedHTML

- [Document.execCommand()](/en-US/docs/Web/API/Document/execCommand) with a `commandName` of ["insertHTML"](/en-US/docs/Web/API/Document/execCommand#inserthtml)
- [Document.parseHTMLUnsafe()](/en-US/docs/Web/API/Document/parseHTMLUnsafe_static)
- [Document.write()](/en-US/docs/Web/API/Document/write)
- [Document.writeln()](/en-US/docs/Web/API/Document/writeln)
- [DOMParser.parseFromString()](/en-US/docs/Web/API/DOMParser/parseFromString)
- [Element.innerHTML](/en-US/docs/Web/API/Element/innerHTML)
- [Element.insertAdjacentHTML](/en-US/docs/Web/API/Element/insertAdjacentHTML)
- [Element.outerHTML](/en-US/docs/Web/API/Element/outerHTML)
- [Element.setHTMLUnsafe()](/en-US/docs/Web/API/Element/setHTMLUnsafe)
- [HTMLIFrameElement.srcdoc](/en-US/docs/Web/API/HTMLIFrameElement/srcdoc)
- [Range.createContextualFragment()](/en-US/docs/Web/API/Range/createContextualFragment)
- [ShadowRoot.innerHTML](/en-US/docs/Web/API/ShadowRoot/innerHTML)
- [ShadowRoot.setHTMLUnsafe()](/en-US/docs/Web/API/ShadowRoot/setHTMLUnsafe)

#### TrustedScript

- [eval()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval)
- [Element.setAttribute()](/en-US/docs/Web/API/Element/setAttribute#value) (`value` argument)
- [Element.setAttributeNS()](/en-US/docs/Web/API/Element/setAttributeNS#value) (`value` argument)
- [Function() constructor](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function)
- [HTMLScriptElement.innerText](/en-US/docs/Web/API/HTMLScriptElement/innerText)
- [HTMLScriptElement.textContent](/en-US/docs/Web/API/HTMLScriptElement/textContent)
- [HTMLScriptElement.text](/en-US/docs/Web/API/HTMLScriptElement/text)
- [window.setTimeout()](/en-US/docs/Web/API/Window/setTimeout#code) and [WorkerGlobalScope.setTimeout()](/en-US/docs/Web/API/WorkerGlobalScope/setTimeout#code) (`code` argument)
- [window.setInterval()](/en-US/docs/Web/API/Window/setInterval#code) and [WorkerGlobalScope.setInterval()](/en-US/docs/Web/API/WorkerGlobalScope/setInterval#code) (`code` argument)

#### TrustedScriptURL

- [HTMLScriptElement.src](/en-US/docs/Web/API/HTMLScriptElement/src)
- [ServiceWorkerContainer.register()](/en-US/docs/Web/API/ServiceWorkerContainer/register)
- [SvgAnimatedString.baseVal](/en-US/docs/Web/API/SVGAnimatedString/baseVal)
- [WorkerGlobalScope.importScripts()](/en-US/docs/Web/API/WorkerGlobalScope/importScripts)
- `url` argument to [Worker() constructor](/en-US/docs/Web/API/Worker/Worker#url)
- `url` argument to [SharedWorker() constructor](/en-US/docs/Web/API/SharedWorker/SharedWorker#url)

### [Cross-browser support for trusted types](#cross-browser_support_for_trusted_types)

The Trusted Types API is not yet available in all modern browsers, but it is usable everywhere today thanks to [compatibility aids created by the W3C](https://github.com/w3c/trusted-types/tree/main?tab=readme-ov-file#polyfill).

- The [full polyfill](https://github.com/w3c/trusted-types/blob/main/src/polyfill/full.js) defines the JavaScript API, attempts to infer the CSP from the current document, and enforces the use of trusted types based on the inferred CSP.
- The [API only polyfill](https://github.com/w3c/trusted-types/blob/main/src/polyfill/api_only.js) defines only the JavaScript API, and does not include the ability to enforce the use of trusted types using a CSP.

As well as these two polyfills, the W3C provides what it calls a tinyfill, which we'll explain in more detail below.

Note that as long as you have tested your code on a supporting browser with CSP enforcement enabled, then you don't need to use the full polyfill above on other browsers — you can get the same benefits using the API only polyfill or the tinyfill.

This is because the enforcement forces you to refactor your code to ensure that all data is passed through the Trusted Types API (and therefore has been through a sanitization function) before being passed to an injection sink. If you then run the refactored code in a different browser without enforcement, it will still go through the same code paths, and give you the same protection.

#### Trusted Types tinyfill

In this section we'll look at how the trusted types tinyfill can protect a website, even though it doesn't add support for trusted types at all.

The trusted types tinyfill is just this:

js

```
if (typeof trustedTypes === "undefined")
  trustedTypes = { createPolicy: (n, rules) => rules };
```

It provides an implementation of `trustedTypes.createPolicy()` which just returns the [policyOptions](/en-US/docs/Web/API/TrustedTypePolicyFactory/createPolicy#policyoptions) object it was passed. The `policyOptions` object defines sanitization functions for data, and these functions are expected to return strings.

With this tinyfill in place, suppose we create a policy:

js

```
const policy = trustedTypes.createPolicy("my-policy", {
  createHTML: (input) => DOMPurify.sanitize(input),
});
```

In browsers that support trusted types, this will return a `TrustedTypePolicy` which will create a `TrustedHTML` object when we call `policy.createHTML()`. The `TrustedHTML` object can then be passed to an injection sink, and we can enforce that the sink received a trusted type, rather than a string.

In browsers that don't support trusted types, this code will return an object with a `createHTML()` function that sanitizes its input and returns it as a string. The sanitized string can then be passed to an injection sink.

js

```
const userInput = "I might be XSS";
const element = document.querySelector("#container");

const trustedHTML = policy.createHTML(userInput);
// In supporting browsers, trustedHTML is a TrustedHTML object.
// In non-supporting browsers, trustedHTML is a string.

element.innerHTML = trustedHTML;
// In supporting browsers, this will throw if trustedHTML
// is not a TrustedHTML object.
```

Either way, the injection sink gets sanitized data, and because we could enforce the use of the policy in the supporting browser, we know that this code path goes through the sanitization function in the non-supporting browser, too.

## [Interfaces](#interfaces)

[TrustedHTML](/en-US/docs/Web/API/TrustedHTML)

Represents a string to insert into an injection sink that will render it as HTML.

[TrustedScript](/en-US/docs/Web/API/TrustedScript)

Represents a string to insert into an injection sink that could lead to the script being executed.

[TrustedScriptURL](/en-US/docs/Web/API/TrustedScriptURL)

Represents a string to insert into an injection sink that will parse it as a URL of an external script resource.

[TrustedTypePolicy](/en-US/docs/Web/API/TrustedTypePolicy)

Defines the functions used to create the above Trusted Type objects.

[TrustedTypePolicyFactory](/en-US/docs/Web/API/TrustedTypePolicyFactory)

Creates policies and verifies that Trusted Type object instances were created via one of the policies.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[Window.trustedTypes](/en-US/docs/Web/API/Window/trustedTypes)

Returns the [TrustedTypePolicyFactory](/en-US/docs/Web/API/TrustedTypePolicyFactory) object associated with the global object in the main thread. This is the entry point for using the API in the Window thread.

[WorkerGlobalScope.trustedTypes](/en-US/docs/Web/API/WorkerGlobalScope/trustedTypes).

Returns the [TrustedTypePolicyFactory](/en-US/docs/Web/API/TrustedTypePolicyFactory) object associated with the global object in a worker.

### [Extensions to HTTP](#extensions_to_http)

#### `Content-Security-Policy` directives

[require-trusted-types-for](/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/require-trusted-types-for)

Enforces that Trusted Types are passed to DOM XSS [injection sinks](#concepts_and_usage).

[trusted-types](/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/trusted-types)

Used to specify an allowlist of Trusted Types policy names.

#### `Content-Security-Policy` keywords

[trusted-types-eval](/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy#trusted-types-eval)

Allows [eval()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval) and similar functions to be used but only when Trusted Types are supported and enforced.

## [Examples](#examples)

In the below example we create a policy that will create [TrustedHTML](/en-US/docs/Web/API/TrustedHTML) objects using [TrustedTypePolicyFactory.createPolicy()](/en-US/docs/Web/API/TrustedTypePolicyFactory/createPolicy). We can then use [TrustedTypePolicy.createHTML()](/en-US/docs/Web/API/TrustedTypePolicy/createHTML) to create a sanitized HTML string to be inserted into the document.

The sanitized value can then be used with [Element.innerHTML](/en-US/docs/Web/API/Element/innerHTML) to ensure that no new HTML elements can be injected.

html

```
<div id="myDiv"></div>
```

js

```
const escapeHTMLPolicy = trustedTypes.createPolicy("myEscapePolicy", {
  createHTML: (string) =>
    string
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&apos;"),
});

let el = document.getElementById("myDiv");
const escaped = escapeHTMLPolicy.createHTML("<img src=x onerror=alert(1)>");
console.log(escaped instanceof TrustedHTML); // true
el.innerHTML = escaped;
```

Read more about this example, and discover other ways to sanitize input in the article [Prevent DOM-based cross-site scripting vulnerabilities with Trusted Types](https://web.dev/articles/trusted-types).

## [Specifications](#specifications)

Specification[Trusted Types](https://w3c.github.io/trusted-types/dist/spec/)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Prevent DOM-based cross-site scripting vulnerabilities with Trusted Types](https://web.dev/articles/trusted-types)
- [Trusted Types polyfill](https://github.com/w3c/trusted-types#polyfill) (also available as an [npm package](https://www.npmjs.com/package/trusted-types))

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 17, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Trusted_Types_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/trusted_types_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTrusted_Types_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftrusted_types_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTrusted_Types_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftrusted_types_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F754b68246f4e69e404309fee4a1699e047e43994%0A*+Document+last+modified%3A+2025-11-17T16%3A52%3A01.000Z%0A%0A%3C%2Fdetails%3E)
