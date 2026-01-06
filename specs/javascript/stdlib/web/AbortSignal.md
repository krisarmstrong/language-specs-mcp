# AbortSignal

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2018⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAbortSignal&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `AbortSignal` interface represents a signal object that allows you to communicate with an asynchronous operation (such as a fetch request) and abort it if required via an [AbortController](/en-US/docs/Web/API/AbortController) object.

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

Also inherits properties from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[AbortSignal.aborted](/en-US/docs/Web/API/AbortSignal/aborted)Read only

A [Boolean](/en-US/docs/Glossary/Boolean) that indicates whether the request(s) the signal is communicating with is/are aborted (`true`) or not (`false`).

[AbortSignal.reason](/en-US/docs/Web/API/AbortSignal/reason)Read only

A JavaScript value providing the abort reason, once the signal has aborted.

## [Static methods](#static_methods)

Also inherits methods from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[AbortSignal.abort()](/en-US/docs/Web/API/AbortSignal/abort_static)

Returns an `AbortSignal` instance that is already set as aborted.

[AbortSignal.any()](/en-US/docs/Web/API/AbortSignal/any_static)

Returns an `AbortSignal` that aborts when any of the given abort signals abort.

[AbortSignal.timeout()](/en-US/docs/Web/API/AbortSignal/timeout_static)

Returns an `AbortSignal` instance that will automatically abort after a specified time.

## [Instance methods](#instance_methods)

Also inherits methods from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[AbortSignal.throwIfAborted()](/en-US/docs/Web/API/AbortSignal/throwIfAborted)

Throws the signal's abort [reason](/en-US/docs/Web/API/AbortSignal/reason) if the signal has been aborted; otherwise it does nothing.

## [Events](#events)

Also inherits events from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

Listen to this event using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface.

[abort](/en-US/docs/Web/API/AbortSignal/abort_event)

Invoked when the asynchronous operations the signal is communicating with is/are aborted. Also available via the `onabort` property.

## [Examples](#examples)

### [Aborting a fetch operation using an explicit signal](#aborting_a_fetch_operation_using_an_explicit_signal)

The following snippet shows how we might use a signal to abort downloading a video using the [Fetch API](/en-US/docs/Web/API/Fetch_API).

We first define a variable for our `AbortController`.

Before each [fetch request](/en-US/docs/Web/API/Window/fetch) we create a new controller using the [AbortController()](/en-US/docs/Web/API/AbortController/AbortController) constructor, then grab a reference to its associated `AbortSignal` object using the [AbortController.signal](/en-US/docs/Web/API/AbortController/signal) property.

Note: An `AbortSignal` can only be used once. After it is aborted, any fetch call using the same signal will be immediately rejected.

When the [fetch request](/en-US/docs/Web/API/Window/fetch) is initiated, we pass in the `AbortSignal` as an option inside the request's options object (the `{ signal }` below). This associates the signal and controller with the fetch request and allows us to abort it by calling [AbortController.abort()](/en-US/docs/Web/API/AbortController/abort), as seen below in the second event listener.

When `abort()` is called, the `fetch()` promise rejects with a `DOMException` named `AbortError`.

js

```
let controller;
const url = "video.mp4";

const downloadBtn = document.querySelector(".download");
const abortBtn = document.querySelector(".abort");

downloadBtn.addEventListener("click", fetchVideo);

abortBtn.addEventListener("click", () => {
  if (controller) {
    controller.abort();
    console.log("Download aborted");
  }
});

async function fetchVideo() {
  controller = new AbortController();
  const signal = controller.signal;

  try {
    const response = await fetch(url, { signal });
    console.log("Download complete", response);
    // process response further
  } catch (err) {
    console.error(`Download error: ${err.message}`);
  }
}
```

If the request is aborted after the `fetch()` call has been fulfilled but before the response body has been read, then attempting to read the response body will reject with an `AbortError` exception.

js

```
async function get() {
  const controller = new AbortController();
  const request = new Request("https://example.org/get", {
    signal: controller.signal,
  });

  const response = await fetch(request);
  controller.abort();
  // The next line will throw `AbortError`
  const text = await response.text();
  console.log(text);
}
```

You can find a [full working example on GitHub](https://github.com/mdn/dom-examples/tree/main/abort-api); you can also see it [running live](https://mdn.github.io/dom-examples/abort-api/).

### [Aborting a fetch operation with a timeout](#aborting_a_fetch_operation_with_a_timeout)

If you need to abort the operation on timeout then you can use the static [AbortSignal.timeout()](/en-US/docs/Web/API/AbortSignal/timeout_static) method. This returns an `AbortSignal` that will automatically timeout after a certain number of milliseconds.

The code snippet below shows how you would either succeed in downloading a file, or handle a timeout error after 5 seconds. Note that when there is a timeout the `fetch()` promise rejects with a `TimeoutError``DOMException`. This allows code to differentiate between timeouts (for which user notification is probably required), and user aborts.

js

```
const url = "video.mp4";

try {
  const res = await fetch(url, { signal: AbortSignal.timeout(5000) });
  const result = await res.blob();
  // …
} catch (err) {
  if (err.name === "TimeoutError") {
    console.error("Timeout: It took more than 5 seconds to get the result!");
  } else if (err.name === "AbortError") {
    console.error(
      "Fetch aborted by user action (browser stop button, closing tab, etc.",
    );
  } else {
    // A network error, or some other problem.
    console.error(`Error: type: ${err.name}, message: ${err.message}`);
  }
}
```

### [Aborting a fetch with timeout or explicit abort](#aborting_a_fetch_with_timeout_or_explicit_abort)

If you want to abort from multiple signals, you can use [AbortSignal.any()](/en-US/docs/Web/API/AbortSignal/any_static) to combine them into a single signal. The following example shows this using [fetch](/en-US/docs/Web/API/Window/fetch):

js

```
try {
  const controller = new AbortController();
  const timeoutSignal = AbortSignal.timeout(5000);
  const res = await fetch(url, {
    // This will abort the fetch when either signal is aborted
    signal: AbortSignal.any([controller.signal, timeoutSignal]),
  });
  const body = await res.json();
} catch (e) {
  if (e.name === "AbortError") {
    // Notify the user of abort.
  } else if (e.name === "TimeoutError") {
    // Notify the user of timeout
  } else {
    // A network error, or some other problem.
    console.log(`Type: ${e.name}, Message: ${e.message}`);
  }
}
```

Note: Unlike when using [AbortSignal.timeout()](/en-US/docs/Web/API/AbortSignal/timeout_static), there is no way to tell whether the final abort was caused by a timeout.

### [Implementing an abortable API](#implementing_an_abortable_api)

An API that needs to support aborting can accept an `AbortSignal` object, and use its state to trigger abort signal handling when needed.

A [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)-based API should respond to the abort signal by rejecting any unsettled promise with the `AbortSignal` abort [reason](/en-US/docs/Web/API/AbortSignal/reason). For example, consider the following `myCoolPromiseAPI`, which takes a signal and returns a promise. The promise is rejected immediately if the signal is already aborted, or if the abort event is detected. Otherwise it completes normally and then resolves the promise.

js

```
function myCoolPromiseAPI(/* …, */ { signal }) {
  return new Promise((resolve, reject) => {
    // If the signal is already aborted, immediately throw in order to reject the promise.
    signal.throwIfAborted();

    // Perform the main purpose of the API
    // Call resolve(result) when done.

    // Watch for 'abort' signals
    // Passing `once: true` ensures the Promise can be garbage collected after abort is called
    signal.addEventListener(
      "abort",
      () => {
        // Stop the main operation
        // Reject the promise with the abort reason.
        reject(signal.reason);
      },
      { once: true },
    );
  });
}
```

The API might then be used as shown. Note that [AbortController.abort()](/en-US/docs/Web/API/AbortController/abort) is called to abort the operation.

js

```
const controller = new AbortController();
const signal = controller.signal;

startSpinner();

myCoolPromiseAPI({ /* …, */ signal })
  .then((result) => {})
  .catch((err) => {
    if (err.name === "AbortError") return;
    showUserErrorMessage();
  })
  .then(() => stopSpinner());

controller.abort();
```

APIs that do not return promises might react in a similar manner. In some cases it may make sense to absorb the signal.

## [Specifications](#specifications)

Specification
[DOM# interface-AbortSignal](https://dom.spec.whatwg.org/#interface-AbortSignal)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Fetch API](/en-US/docs/Web/API/Fetch_API)
- [Abortable Fetch](https://developer.chrome.com/blog/abortable-fetch/) by Jake Archibald

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 12, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/AbortSignal/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/abortsignal/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAbortSignal&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fabortsignal%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAbortSignal%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fabortsignal%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4854b2e695bd40ec2a124e15bf57b032f96e493d%0A*+Document+last+modified%3A+2025-12-12T22%3A10%3A35.000Z%0A%0A%3C%2Fdetails%3E)
