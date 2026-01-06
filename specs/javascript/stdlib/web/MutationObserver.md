# MutationObserver

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMutationObserver&level=high)

The `MutationObserver` interface provides the ability to watch for changes being made to the [DOM](/en-US/docs/Web/API/Document_Object_Model) tree. It is designed as a replacement for the older [Mutation Events](/en-US/docs/Web/API/MutationEvent) feature, which was part of the DOM3 Events specification.

## In this article

- [Constructor](#constructor)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[MutationObserver()](/en-US/docs/Web/API/MutationObserver/MutationObserver)

Creates and returns a new `MutationObserver` which will invoke a specified callback function when DOM changes occur.

## [Instance methods](#instance_methods)

[disconnect()](/en-US/docs/Web/API/MutationObserver/disconnect)

Stops the `MutationObserver` instance from receiving further notifications until and unless [observe()](/en-US/docs/Web/API/MutationObserver/observe) is called again.

[observe()](/en-US/docs/Web/API/MutationObserver/observe)

Configures the `MutationObserver` to begin receiving notifications through its callback function when DOM changes matching the given options occur.

[takeRecords()](/en-US/docs/Web/API/MutationObserver/takeRecords)

Removes all pending notifications from the `MutationObserver`'s notification queue and returns them in a new [Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) of [MutationRecord](/en-US/docs/Web/API/MutationRecord) objects.

## [Example](#example)

The following example was adapted from [this blog post](https://hacks.mozilla.org/2012/05/dom-mutationobserver-reacting-to-dom-changes-without-killing-browser-performance/).

js

```
// Select the node that will be observed for mutations
const targetNode = document.getElementById("some-id");

// Options for the observer (which mutations to observe)
const config = { attributes: true, childList: true, subtree: true };

// Callback function to execute when mutations are observed
const callback = (mutationList, observer) => {
  for (const mutation of mutationList) {
    if (mutation.type === "childList") {
      console.log("A child node has been added or removed.");
    } else if (mutation.type === "attributes") {
      console.log(`The ${mutation.attributeName} attribute was modified.`);
    }
  }
};

// Create an observer instance linked to the callback function
const observer = new MutationObserver(callback);

// Start observing the target node for configured mutations
observer.observe(targetNode, config);

// Later, you can stop observing
observer.disconnect();
```

## [Specifications](#specifications)

Specification
[DOM# interface-mutationobserver](https://dom.spec.whatwg.org/#interface-mutationobserver)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [PerformanceObserver](/en-US/docs/Web/API/PerformanceObserver)
- [ResizeObserver](/en-US/docs/Web/API/ResizeObserver)
- [IntersectionObserver](/en-US/docs/Web/API/IntersectionObserver)
- [A brief overview](https://developer.chrome.com/blog/detect-dom-changes-with-mutation-observers/)
- [A more in-depth discussion](https://hacks.mozilla.org/2012/05/dom-mutationobserver-reacting-to-dom-changes-without-killing-browser-performance/)
- [A screencast by Chromium developer Rafael Weinstein](https://www.youtube.com/watch?v=eRZ4pO0gVWw)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 10, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/MutationObserver/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mutationobserver/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMutationObserver&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmutationobserver%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMutationObserver%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmutationobserver%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2f5cd95b4402a869bb6f79d6fa01b95ffec9df41%0A*+Document+last+modified%3A+2025-06-10T08%3A27%3A00.000Z%0A%0A%3C%2Fdetails%3E)
