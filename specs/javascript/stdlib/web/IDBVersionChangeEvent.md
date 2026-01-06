# IDBVersionChangeEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBVersionChangeEvent&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `IDBVersionChangeEvent` interface of the [IndexedDB API](/en-US/docs/Web/API/IndexedDB_API) indicates that the version of the database has changed, as the result of an [onupgradeneeded](/en-US/docs/Web/API/IDBOpenDBRequest/upgradeneeded_event) event handler function.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[IDBVersionChangeEvent()](/en-US/docs/Web/API/IDBVersionChangeEvent/IDBVersionChangeEvent)

Creates and returns a new `IDBVersionChangeEvent` object which is used to represent when a version of the database has changed.

## [Instance properties](#instance_properties)

Also inherits properties from its parent, [Event](/en-US/docs/Web/API/Event) interface.

[IDBVersionChangeEvent.oldVersion](/en-US/docs/Web/API/IDBVersionChangeEvent/oldVersion)Read only

Returns the old version of the database.

[IDBVersionChangeEvent.newVersion](/en-US/docs/Web/API/IDBVersionChangeEvent/newVersion)Read only

Returns the new version of the database.

## [Instance methods](#instance_methods)

No specific method, but inherits methods from its parent, [Event](/en-US/docs/Web/API/Event) interface.

## [Example](#example)

In the following code snippet, we make a request to open a database, and include handlers for the success and error cases. Upon a version change (after an `upgradeneeded` event), the `success` event will implement the `IDBVersionChangeEvent` interface. For a full working example, see our [To-do Notifications](https://github.com/mdn/dom-examples/tree/main/to-do-notifications) app ([view example live](https://mdn.github.io/dom-examples/to-do-notifications/)).

js

```
const note = document.querySelector("ul");

// Let us open version 4 of our database
const DBOpenRequest = window.indexedDB.open("toDoList", 4);

// these two event handlers act on the database being opened successfully, or not
DBOpenRequest.onerror = (event) => {
  note.appendChild(document.createElement("li")).textContent =
    "Error loading database.";
};

DBOpenRequest.onsuccess = (event) => {
  note.appendChild(document.createElement("li")).textContent =
    "Database initialized.";

  // store the result of opening the database in the db variable. This is used a lot later on, for opening transactions and suchlike.
  const db = DBOpenRequest.result;
};
```

## [Specifications](#specifications)

Specification
[Indexed Database API 3.0# events](https://w3c.github.io/IndexedDB/#events)

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

 This page was last modified on ⁨Jul 19, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/IDBVersionChangeEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/idbversionchangeevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBVersionChangeEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fidbversionchangeevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBVersionChangeEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fidbversionchangeevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fff1e97da7ade9fcb05fb3de064011d4f05debe82%0A*+Document+last+modified%3A+2024-07-19T08%3A42%3A58.000Z%0A%0A%3C%2Fdetails%3E)
