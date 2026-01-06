# IDBDatabase

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBDatabase&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `IDBDatabase` interface of the IndexedDB API provides a [connection to a database](/en-US/docs/Web/API/IndexedDB_API/Basic_Terminology#database_connection); you can use an `IDBDatabase` object to open a [transaction](/en-US/docs/Web/API/IndexedDB_API/Basic_Terminology#transaction) on your database then create, manipulate, and delete objects (data) in that database. The interface provides the only way to get and manage versions of the database.

Note: Everything you do in IndexedDB always happens in the context of a [transaction](/en-US/docs/Web/API/IndexedDB_API/Basic_Terminology#transaction), representing interactions with data in the database. All objects in IndexedDB — including object stores, indexes, and cursors — are tied to a particular transaction. Thus, you cannot execute commands, access data, or open anything outside of a transaction.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[IDBDatabase.name](/en-US/docs/Web/API/IDBDatabase/name)Read only

A string that contains the name of the connected database.

[IDBDatabase.version](/en-US/docs/Web/API/IDBDatabase/version)Read only

A 64-bit integer that contains the version of the connected database. When a database is first created, this attribute is an empty string.

[IDBDatabase.objectStoreNames](/en-US/docs/Web/API/IDBDatabase/objectStoreNames)Read only

A [DOMStringList](/en-US/docs/Web/API/DOMStringList) that contains a list of the names of the [object stores](/en-US/docs/Web/API/IndexedDB_API/Basic_Terminology#object_store) currently in the connected database.

## [Instance methods](#instance_methods)

Inherits from: [EventTarget](/en-US/docs/Web/API/EventTarget)

[IDBDatabase.close()](/en-US/docs/Web/API/IDBDatabase/close)

Returns immediately and closes the connection to a database in a separate thread.

[IDBDatabase.createObjectStore()](/en-US/docs/Web/API/IDBDatabase/createObjectStore)

Creates and returns a new object store or index.

[IDBDatabase.deleteObjectStore()](/en-US/docs/Web/API/IDBDatabase/deleteObjectStore)

Destroys the object store with the given name in the connected database, along with any indexes that reference it.

[IDBDatabase.transaction()](/en-US/docs/Web/API/IDBDatabase/transaction)

Immediately returns a transaction object ([IDBTransaction](/en-US/docs/Web/API/IDBTransaction)) containing the [IDBTransaction.objectStore](/en-US/docs/Web/API/IDBTransaction/objectStore) method, which you can use to access your object store. Runs in a separate thread.

## [Events](#events)

Listen to these events using `addEventListener()` or by assigning an event listener to the `oneventname` property of this interface.

[close](/en-US/docs/Web/API/IDBDatabase/close_event)

An event fired when the database connection is unexpectedly closed.

[versionchange](/en-US/docs/Web/API/IDBDatabase/versionchange_event)

An event fired when a database structure change was requested.

The following events are available to `IDBDatabase` via event bubbling from [IDBTransaction](/en-US/docs/Web/API/IDBTransaction):

`IDBTransaction`[abort](/en-US/docs/Web/API/IDBTransaction/abort_event)

An event fired when a transaction is aborted.

`IDBTransaction`[error](/en-US/docs/Web/API/IDBTransaction/error_event)

An event fired when a request returns an error and the event bubbles up to the connection object.

## [Example](#example)

In the following code snippet, we open a database asynchronously ([IDBFactory](/en-US/docs/Web/API/IDBFactory)), handle success and error cases, and create a new object store in the case that an upgrade is needed (`IDBDatabase`). For a complete working example, see our [To-do Notifications](https://github.com/mdn/dom-examples/tree/main/to-do-notifications) app ([view example live](https://mdn.github.io/dom-examples/to-do-notifications/)).

js

```
// Let us open our database
const DBOpenRequest = window.indexedDB.open("toDoList", 4);

// these two event handlers act on the IDBDatabase object,
// when the database is opened successfully, or not
DBOpenRequest.onerror = (event) => {
  note.appendChild(document.createElement("li")).textContent =
    "Error loading database.";
};

DBOpenRequest.onsuccess = (event) => {
  node.appendChild(document.createElement("li")).textContent =
    "Database initialized.";

  // store the result of opening the database in the db
  // variable. This is used a lot later on
  db = DBOpenRequest.result;

  // Run the displayData() function to populate the task
  // list with all the to-do list data already in the IDB
  displayData();
};

// This event handles the event whereby a new version of
// the database needs to be created Either one has not
// been created before, or a new version number has been
// submitted via the window.indexedDB.open line above

DBOpenRequest.onupgradeneeded = (event) => {
  const db = event.target.result;

  db.onerror = (event) => {
    note.appendChild(document.createElement("li")).textContent =
      "Error loading database.";
  };

  // Create an objectStore for this database using
  // IDBDatabase.createObjectStore

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

  note.appendChild(document.createElement("li")).textContent =
    "Object store created.";
};
```

This next line opens up a transaction on the Database, then opens an object store that we can then manipulate the data inside of.

js

```
const objectStore = db
  .transaction("toDoList", "readwrite")
  .objectStore("toDoList");
```

## [Specifications](#specifications)

Specification
[Indexed Database API 3.0# database-interface](https://w3c.github.io/IndexedDB/#database-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using IndexedDB](/en-US/docs/Web/API/IndexedDB_API/Using_IndexedDB)
- Using transactions: [IDBTransaction](/en-US/docs/Web/API/IDBTransaction)
- Setting a range of keys: [IDBKeyRange](/en-US/docs/Web/API/IDBKeyRange)
- Retrieving and making changes to your data: [IDBObjectStore](/en-US/docs/Web/API/IDBObjectStore)
- Using cursors: [IDBCursor](/en-US/docs/Web/API/IDBCursor)
- Reference example: [To-do Notifications](https://github.com/mdn/dom-examples/tree/main/to-do-notifications) ([View the example live](https://mdn.github.io/dom-examples/to-do-notifications/)).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/IDBDatabase/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/idbdatabase/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBDatabase&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fidbdatabase%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBDatabase%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fidbdatabase%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
