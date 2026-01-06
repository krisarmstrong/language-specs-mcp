# ProgressEvent

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FProgressEvent&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `ProgressEvent` interface represents events that measure the progress of an underlying process, like an HTTP request (e.g., an `XMLHttpRequest`, or the loading of the underlying resource of an [<img>](/en-US/docs/Web/HTML/Reference/Elements/img), [<audio>](/en-US/docs/Web/HTML/Reference/Elements/audio), [<video>](/en-US/docs/Web/HTML/Reference/Elements/video), [<style>](/en-US/docs/Web/HTML/Reference/Elements/style) or [<link>](/en-US/docs/Web/HTML/Reference/Elements/link)).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[ProgressEvent()](/en-US/docs/Web/API/ProgressEvent/ProgressEvent)

Creates a `ProgressEvent` event with the given parameters.

## [Instance properties](#instance_properties)

Also inherits properties from its parent [Event](/en-US/docs/Web/API/Event).

[ProgressEvent.lengthComputable](/en-US/docs/Web/API/ProgressEvent/lengthComputable)Read only

A boolean flag indicating if the ratio between the size of the data already transmitted or processed (`loaded`), and the total size of the data (`total`), is calculable. In other words, it tells if the progress is measurable or not.

[ProgressEvent.loaded](/en-US/docs/Web/API/ProgressEvent/loaded)Read only

A number indicating the size of the data already transmitted or processed. For a `ProgressEvent` dispatched by the browser in HTTP messages, the value refers to the size, in bytes, of the message body, excluding headers and other overhead. In compressed messages of unknown total size, `loaded` might refer to the size of the compressed or uncompressed data, depending on the browser. As of 2024, it contains the size of the compressed data in Firefox, and the uncompressed data in Chrome. In a `ProgressEvent` you create yourself, you can assign any numeric value to `loaded` that represents the amount of work completed relative to the `total` value.

[ProgressEvent.total](/en-US/docs/Web/API/ProgressEvent/total)Read only

A number indicating the total size of the data being transmitted or processed. For `ProgressEvent`s dispatched by the browser in HTTP messages, the value refers to the size, in bytes, of a resource and is derived from the `Content-Length` header. In a `ProgressEvent` you create yourself, you may wish to normalize `total` to a value such as `100` or `1` if revealing the precise amount of bytes of a resource is a concern. If using `1` as a total, for example, then `loaded` would be a decimal value between `0` and `1`.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [Event](/en-US/docs/Web/API/Event).

## [Examples](#examples)

### [Showing the status of a request](#showing_the_status_of_a_request)

The following example adds a `ProgressEvent` to a new [XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest) and uses it to display the status of the request.

js

```
const progressBar = document.getElementById("p"),
  client = new XMLHttpRequest();
client.open("GET", "magical-unicorns");
client.onprogress = (pe) => {
  if (pe.lengthComputable) {
    progressBar.max = pe.total;
    progressBar.value = pe.loaded;
  }
};
client.onloadend = (pe) => {
  progressBar.value = pe.loaded;
};
client.send();
```

### [Using fractions in a ProgressEvent](#using_fractions_in_a_progressevent)

The total number of bytes of a resource may reveal too much information about a resource, so a number between 0 and 1 may be used in a [ProgressEvent()](/en-US/docs/Web/API/ProgressEvent/ProgressEvent) instead:

js

```
function updateProgress(loaded, total) {
  const progressEvent = new ProgressEvent("progress", {
    lengthComputable: true,
    loaded,
    total,
  });

  document.dispatchEvent(progressEvent);
}

document.addEventListener("progress", (event) => {
  console.log(`Progress: ${event.loaded}/${event.total}`);
});

updateProgress(0.123456, 1);
```

## [Specifications](#specifications)

Specification
[XMLHttpRequest# interface-progressevent](https://xhr.spec.whatwg.org/#interface-progressevent)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [Event](/en-US/docs/Web/API/Event) base interface.

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 2, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ProgressEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/progressevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FProgressEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fprogressevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FProgressEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fprogressevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F03ca44d7f71637a4cad71413fac4e31d5de66638%0A*+Document+last+modified%3A+2025-06-02T16%3A21%3A47.000Z%0A%0A%3C%2Fdetails%3E)
