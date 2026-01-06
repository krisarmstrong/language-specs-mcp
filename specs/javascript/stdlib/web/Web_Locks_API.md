# Web Locks API

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The Web Locks API allows scripts running in one tab or worker to asynchronously acquire a lock, hold it while work is performed, then release it. While held, no other script executing in the same origin can acquire the same lock, which allows a web app running in multiple tabs or workers to coordinate work and the use of resources.

## In this article

- [Concepts and Usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Concepts and Usage](#concepts_and_usage)

A lock is an abstract concept representing some potentially shared resource, identified by a name chosen by the web app. For example, if a web app running in multiple tabs wants to ensure that only one tab is syncing data between the network and Indexed DB, each tab could try to acquire a "my_net_db_sync" lock, but only one tab will succeed (the [leader election pattern](https://en.wikipedia.org/wiki/Leader_election).)

The API is used as follows:

1. The lock is requested.
2. Work is done while holding the lock in an asynchronous task.
3. The lock is automatically released when the task completes.

js

```
navigator.locks.request("my_resource", async (lock) => {
  // The lock has been acquired.
  await do_something();
  await do_something_else();
  // Now the lock will be released.
});
```

While a lock is held, requests for the same lock from this execution context, or from other tabs/workers, will be queued. The first queued request will be granted only when the lock is released.

The API provides optional functionality that may be used as needed, including:

- returning values from the asynchronous task
- shared and exclusive lock modes
- conditional acquisition
- diagnostics to query the state of locks in an origin
- an escape hatch to protect against deadlocks

Locks are scoped to origins; the locks acquired by a tab from `https://example.com` have no effect on the locks acquired by a tab from `https://example.org:8080` as they are separate origins.

The main entry point is [navigator.locks.request()](/en-US/docs/Web/API/LockManager/request) which requests a lock. It takes a lock name, an optional set of options, and a callback. The callback is invoked when the lock is granted. The lock is automatically released when the callback returns, so usually the callback is an async function, which causes the lock to be released only when the async function has completely finished.

The `request()` method itself returns a promise which resolves once the lock has been released; within an async function, a script can `await` the call to make the asynchronous code flow linearly. For example:

js

```
await do_something_without_lock();

// Request the lock.
await navigator.locks.request("my_resource", async (lock) => {
  // The lock has been acquired.
  await do_something_with_lock();
  await do_something_else_with_lock();
  // Now the lock will be released.
});
// The lock has been released.

await do_something_else_without_lock();
```

### [Options](#options)

Several options can be passed when requesting a lock:

- `mode`: The default mode is "exclusive", but "shared" can be specified. There can be only one "exclusive" holder of a lock, but multiple "shared" requests can be granted at the same time. This can be used to implement the [readers-writer pattern](https://en.wikipedia.org/wiki/Readers%E2%80%93writer_lock).
- `ifAvailable`: If specified, the lock request will fail if the lock cannot be granted immediately without waiting. The callback is invoked with `null`.
- `steal`: If specified, then any held locks with the same name will be released, and the request will be granted, preempting any queued requests for it.
- `signal`: An [AbortSignal](/en-US/docs/Web/API/AbortSignal) can be passed in, allowing a lock request to be aborted. This can be used to implement a timeout on requests.

### [Monitoring](#monitoring)

The [navigator.locks.query()](/en-US/docs/Web/API/LockManager/query) method can be used by scripts to introspect the state of the lock manager for the origin. This can be useful when debugging, for example, identifying why a lock could not be acquired. The results are a snapshot of the lock manager state, which identifies held and requested locks and some additional data (e.g., mode) about each, at the time the snapshot was taken.

### [Advanced use](#advanced_use)

For more complicated cases, such as holding the lock for an arbitrary amount of time, the callback can return a promise explicitly resolved by the script:

js

```
// Capture promise control functions:
const { promise, resolve, reject } = Promise.withResolvers();

// Request the lock:
navigator.locks.request(
  "my_resource",
  // Lock is acquired.
  (lock) => promise, // Now lock will be held until either resolve() or reject() is called.
);
```

### [Deadlocks](#deadlocks)

A deadlock occurs when a process can no longer make progress because each part is waiting on a request that cannot be satisfied. This can occur with this API in complex use-cases, for example, if multiple locks are requested out-of-order. If tab 1 holds lock A and tab 2 holds lock B, then tab 1 attempts to also acquire lock B and tab 2 attempts to also acquire lock A, neither request can be granted. Web applications can avoid this through several strategies, such as ensuring lock requests are not nested, or are always well ordered, or have timeouts. Note that such deadlocks only affect the locks themselves and code depending on them; the browser, other tabs, and other script in the page is not affected.

## [Interfaces](#interfaces)

[Lock](/en-US/docs/Web/API/Lock)

Provides the name and mode of a previously requested lock, which is received in the callback to [LockManager.request()](/en-US/docs/Web/API/LockManager/request).

[LockManager](/en-US/docs/Web/API/LockManager)

Provides methods for requesting a new [Lock](/en-US/docs/Web/API/Lock) object and querying for an existing [Lock](/en-US/docs/Web/API/Lock) object. To get an instance of [LockManager](/en-US/docs/Web/API/LockManager), call [navigator.locks](/en-US/docs/Web/API/Navigator/locks).

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[Navigator.locks](/en-US/docs/Web/API/Navigator/locks)Read only

Returns a [LockManager](/en-US/docs/Web/API/LockManager) object that provides methods for requesting a new [Lock](/en-US/docs/Web/API/Lock) object and querying for an existing [Lock](/en-US/docs/Web/API/Lock) object.

[WorkerNavigator.locks](/en-US/docs/Web/API/WorkerNavigator/locks)Read only

Returns a [LockManager](/en-US/docs/Web/API/LockManager) object which provides methods for requesting a new [Lock](/en-US/docs/Web/API/Lock) object and querying for an existing [Lock](/en-US/docs/Web/API/Lock) object.

## [Specifications](#specifications)

Specification[Web Locks API](https://w3c.github.io/web-locks/)

## [Browser compatibility](#browser_compatibility)

### [api.LockManager](#api.LockManager)

### [api.Lock](#api.Lock)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Web_Locks_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/web_locks_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_Locks_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fweb_locks_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_Locks_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fweb_locks_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F702cd9e4d2834e13aea345943efc8d0c03d92ec9%0A*+Document+last+modified%3A+2025-04-03T04%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
