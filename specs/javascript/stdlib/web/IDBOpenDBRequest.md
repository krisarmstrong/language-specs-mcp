# IDBOpenDBRequest

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBOpenDBRequest&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `IDBOpenDBRequest` interface of the IndexedDB API provides access to the results of requests to open or delete databases (performed using [IDBFactory.open](/en-US/docs/Web/API/IDBFactory/open) and [IDBFactory.deleteDatabase](/en-US/docs/Web/API/IDBFactory/deleteDatabase)), using specific event handler attributes.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Also inherits properties from its parents [IDBRequest](/en-US/docs/Web/API/IDBRequest) and [EventTarget](/en-US/docs/Web/API/EventTarget).

## [Instance methods](#instance_methods)

No methods, but inherits methods from its parents [IDBRequest](/en-US/docs/Web/API/IDBRequest) and [EventTarget](/en-US/docs/Web/API/EventTarget).

## [Events](#events)

Events defined on parent interfaces, [IDBRequest](/en-US/docs/Web/API/IDBRequest) and [EventTarget](/en-US/docs/Web/API/EventTarget), can also be dispatched on `IDBOpenDBRequest` objects.

Listen to these generic and specific events using `addEventListener()` or by assigning an event listener to the `oneventname` property of this interface.

Events specific to this interface are:

[blocked](/en-US/docs/Web/API/IDBOpenDBRequest/blocked_event)

Fired when an open connection to a database is blocking a `versionchange` transaction on the same database. Also available via the [onblocked](/en-US/docs/Web/API/IDBOpenDBRequest/blocked_event) property.

[upgradeneeded](/en-US/docs/Web/API/IDBOpenDBRequest/upgradeneeded_event)

Fired when an attempt was made to open a database with a version number higher than its current version. Also available via the [onupgradeneeded](/en-US/docs/Web/API/IDBOpenDBRequest/upgradeneeded_event) property.

## [Example](#example)

In the following example you can see the onupgradeneeded handler being used to update the database structure if a database with a higher version number is loaded. For a full working example, see our [To-do Notifications](https://github.com/mdn/dom-examples/tree/main/to-do-notifications) app ([view example live](https://mdn.github.io/dom-examples/to-do-notifications/).)

js

```
let db;

// Let us open our database
const DBOpenRequest = window.indexedDB.open("toDoList", 4);

// these event handlers act on the database being opened.
DBOpenRequest.onerror = (event) => {
  note.appendChild(document.createElement("li")).textContent =
    "Error loading database.";
};

DBOpenRequest.onsuccess = (event) => {
  note.appendChild(document.createElement("li")).textContent =
    "Database initialized.";

  // store the result of opening the database in the db
  // variable. This is used a lot below
  db = DBOpenRequest.result;

  // Run the displayData() function to populate the task
  // list with all the to-do list data already in the IDB
  displayData();
};

// This event handles the event whereby a new version of
// the database needs to be created Either one has not
// been created before, or a new version number has been
// submitted via the window.indexedDB.open line above
// it is only implemented in recent browsers
DBOpenRequest.onupgradeneeded = (event) => {
  const db = event.target.result;

  db.onerror = (event) => {
    note.appendChild(document.createElement("li")).textContent =
      "Error loading database.";
  };

  // Create an objectStore for this database
  const objectStore = db.createObjectStore("toDoList", {
    keyPath: "taskTitle",
  });

  // define what data items the objectStore will contain

  objectStore.createIndex("hours", "hours", { unique: false });
  objectStore.createIndex("minutes", "minutes", { unique: false });
  objectStore.createIndex("day", "day", { unique: false });
  objectStore.createIndex("month", "month", { unique: false });
  objectStore.createIndex("year", "year", { unique: false });
  objectStore.createIndex("notified", "notified", { unique: false });
};
```

## [Specifications](#specifications)

Specification
[Indexed Database API 3.0# idbopendbrequest](https://w3c.github.io/IndexedDB/#idbopendbrequest)

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

 This page was last modified on ⁨Jul 19, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/IDBOpenDBRequest/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/idbopendbrequest/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBOpenDBRequest&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fidbopendbrequest%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBOpenDBRequest%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fidbopendbrequest%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fff1e97da7ade9fcb05fb3de064011d4f05debe82%0A*+Document+last+modified%3A+2024-07-19T08%3A42%3A58.000Z%0A%0A%3C%2Fdetails%3E)
