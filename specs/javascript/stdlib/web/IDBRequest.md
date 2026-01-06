# IDBRequest

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBRequest&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `IDBRequest` interface of the IndexedDB API provides access to results of asynchronous requests to databases and database objects using event handler attributes. Each reading and writing operation on a database is done using a request.

The request object does not initially contain any information about the result of the operation, but once information becomes available, an event is fired on the request, and the information becomes available through the properties of the `IDBRequest` instance.

All asynchronous operations immediately return an `IDBRequest` instance. Each request has a `readyState` that is set to the `'pending'` state; this changes to `'done'` when the request is completed or fails. When the state is set to `done`, every request returns a `result` and an `error`, and an event is fired on the request. When the state is still `pending`, any attempt to access the `result` or `error` raises an `InvalidStateError` exception.

In plain words, all asynchronous methods return a request object. If the request has been completed successfully, the result is made available through the `result` property and an event indicating success is fired at the request ([success](/en-US/docs/Web/API/IDBRequest/success_event)). If an error occurs while performing the operation, the exception is made available through the `error` property and an error event is fired ([error](/en-US/docs/Web/API/IDBRequest/error_event)).

The interface [IDBOpenDBRequest](/en-US/docs/Web/API/IDBOpenDBRequest) is derived from `IDBRequest`.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Also inherits properties from [EventTarget](/en-US/docs/Web/API/EventTarget).

[IDBRequest.error](/en-US/docs/Web/API/IDBRequest/error)Read only

Returns a [DOMException](/en-US/docs/Web/API/DOMException) in the event of an unsuccessful request, indicating what went wrong.

[IDBRequest.result](/en-US/docs/Web/API/IDBRequest/result)Read only

Returns the result of the request. If the request is not completed, the result is not available and an `InvalidStateError` exception is thrown.

[IDBRequest.source](/en-US/docs/Web/API/IDBRequest/source)Read only

The source of the request, such as an [IDBIndex](/en-US/docs/Web/API/IDBIndex) or an [IDBObjectStore](/en-US/docs/Web/API/IDBObjectStore). If no source exists (such as when calling [IDBFactory.open](/en-US/docs/Web/API/IDBFactory/open)), it returns null.

[IDBRequest.readyState](/en-US/docs/Web/API/IDBRequest/readyState)Read only

The state of the request. Every request starts in the `pending` state. The state changes to `done` when the request completes successfully or when an error occurs.

[IDBRequest.transaction](/en-US/docs/Web/API/IDBRequest/transaction)Read only

The transaction for the request. This property can be null for certain requests, for example those returned from [IDBFactory.open](/en-US/docs/Web/API/IDBFactory/open) unless an upgrade is needed. (You're just connecting to a database, so there is no transaction to return).

## [Instance methods](#instance_methods)

No methods, but inherits methods from [EventTarget](/en-US/docs/Web/API/EventTarget).

## [Events](#events)

Listen to these events using `addEventListener()` or by assigning an event listener to the `oneventname` property of this interface.

[error](/en-US/docs/Web/API/IDBRequest/error_event)

Fired when an error caused a request to fail.

[success](/en-US/docs/Web/API/IDBRequest/success_event)

Fired when an `IDBRequest` succeeds.

## [Example](#example)

In the following code snippet, we open a database asynchronously and make a request; `onerror` and `onsuccess` functions are included to handle the success and error cases. For a full working example, see our [To-do Notifications](https://github.com/mdn/dom-examples/tree/main/to-do-notifications) app ([view example live](https://mdn.github.io/dom-examples/to-do-notifications/).)

js

```
let db;

// Let us open our database
const DBOpenRequest = window.indexedDB.open("toDoList", 4);

// these two event handlers act on the database being
// opened successfully, or not
DBOpenRequest.onerror = (event) => {
  note.appendChild(document.createElement("li")).textContent =
    "Error loading database.";
};

DBOpenRequest.onsuccess = (event) => {
  note.appendChild(document.createElement("li")).textContent =
    "Database initialized.";

  // store the result of opening the database.
  db = DBOpenRequest.result;
};
```

## [Specifications](#specifications)

Specification
[Indexed Database API 3.0# request-api](https://w3c.github.io/IndexedDB/#request-api)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using IndexedDB](/en-US/docs/Web/API/IndexedDB_API/Using_IndexedDB)
- Starting transactions: [IDBDatabase](/en-US/docs/Web/API/IDBDatabase)
- Using transactions: [IDBTransaction](/en-US/docs/Web/API/IDBTransaction)
- Setting a range of keys: [IDBKeyRange](/en-US/docs/Web/API/IDBKeyRange)
- Retrieving and making changes to your data: [IDBObjectStore](/en-US/docs/Web/API/IDBObjectStore)
- Using cursors: [IDBCursor](/en-US/docs/Web/API/IDBCursor)
- Reference example: [To-do Notifications](https://github.com/mdn/dom-examples/tree/main/to-do-notifications) ([View the example live](https://mdn.github.io/dom-examples/to-do-notifications/)).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 24, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/IDBRequest/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/idbrequest/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBRequest&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fidbrequest%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBRequest%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fidbrequest%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F32305cc3cf274fbfdcc73a296bbd400a26f38296%0A*+Document+last+modified%3A+2024-07-24T20%3A47%3A46.000Z%0A%0A%3C%2Fdetails%3E)
