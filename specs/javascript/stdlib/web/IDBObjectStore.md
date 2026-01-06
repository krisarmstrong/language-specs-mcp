# IDBObjectStore

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBObjectStore&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `IDBObjectStore` interface of the [IndexedDB API](/en-US/docs/Web/API/IndexedDB_API) represents an object store in a database. Records within an object store are sorted according to their keys. This sorting enables fast insertion, look-up, and ordered retrieval.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[IDBObjectStore.indexNames](/en-US/docs/Web/API/IDBObjectStore/indexNames)Read only

A list of the names of [indexes](/en-US/docs/Web/API/IndexedDB_API/Basic_Terminology#index) on objects in this object store.

[IDBObjectStore.keyPath](/en-US/docs/Web/API/IDBObjectStore/keyPath)Read only

The [key path](/en-US/docs/Web/API/IndexedDB_API/Basic_Terminology#key_path) of this object store. If this attribute is `null`, the application must provide a key for each modification operation.

[IDBObjectStore.name](/en-US/docs/Web/API/IDBObjectStore/name)

The name of this object store.

[IDBObjectStore.transaction](/en-US/docs/Web/API/IDBObjectStore/transaction)Read only

The [IDBTransaction](/en-US/docs/Web/API/IDBTransaction) object to which this object store belongs.

[IDBObjectStore.autoIncrement](/en-US/docs/Web/API/IDBObjectStore/autoIncrement)Read only

The value of the auto increment flag for this object store.

## [Instance methods](#instance_methods)

[IDBObjectStore.add()](/en-US/docs/Web/API/IDBObjectStore/add)

Returns an [IDBRequest](/en-US/docs/Web/API/IDBRequest) object and, in a separate thread, creates a [structured clone](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#structured-clone) of the `value`, and stores the cloned value in the object store. This is for adding new records to an object store.

[IDBObjectStore.clear()](/en-US/docs/Web/API/IDBObjectStore/clear)

Creates and immediately returns an [IDBRequest](/en-US/docs/Web/API/IDBRequest) object, and clears this object store in a separate thread. This is for deleting all current records out of an object store.

[IDBObjectStore.count()](/en-US/docs/Web/API/IDBObjectStore/count)

Returns an [IDBRequest](/en-US/docs/Web/API/IDBRequest) object and, in a separate thread, returns the total number of records that match the provided key or [IDBKeyRange](/en-US/docs/Web/API/IDBKeyRange). If no arguments are provided, it returns the total number of records in the store.

[IDBObjectStore.createIndex()](/en-US/docs/Web/API/IDBObjectStore/createIndex)

Creates a new index during a version upgrade, returning a new [IDBIndex](/en-US/docs/Web/API/IDBIndex) object in the connected database.

[IDBObjectStore.delete()](/en-US/docs/Web/API/IDBObjectStore/delete)

returns an [IDBRequest](/en-US/docs/Web/API/IDBRequest) object and, in a separate thread, deletes the store object selected by the specified key. This is for deleting individual records out of an object store.

[IDBObjectStore.deleteIndex()](/en-US/docs/Web/API/IDBObjectStore/deleteIndex)

Destroys the specified index in the connected database, used during a version upgrade.

[IDBObjectStore.get()](/en-US/docs/Web/API/IDBObjectStore/get)

Returns an [IDBRequest](/en-US/docs/Web/API/IDBRequest) object and, in a separate thread, returns the store object store selected by the specified key. This is for retrieving specific records from an object store.

[IDBObjectStore.getKey()](/en-US/docs/Web/API/IDBObjectStore/getKey)

Returns an [IDBRequest](/en-US/docs/Web/API/IDBRequest) object and, in a separate thread, retrieves and returns the record key for the object in the object stored matching the specified parameter.

[IDBObjectStore.getAll()](/en-US/docs/Web/API/IDBObjectStore/getAll)

Returns an [IDBRequest](/en-US/docs/Web/API/IDBRequest) object and, in a separate thread, retrieves all objects in the object store matching the specified parameter or all objects in the store if no parameters are given.

[IDBObjectStore.getAllKeys()](/en-US/docs/Web/API/IDBObjectStore/getAllKeys)

Returns an [IDBRequest](/en-US/docs/Web/API/IDBRequest) object and, in a separate thread, retrieves record keys for all objects in the object store matching the specified parameter or all objects in the store if no parameters are given.

[IDBObjectStore.getAllRecords()](/en-US/docs/Web/API/IDBObjectStore/getAllRecords)Experimental

Returns an [IDBRequest](/en-US/docs/Web/API/IDBRequest) object and, in a separate thread, finds all matching records in the object store (including primary keys and values) that correspond to the given key or are in range, if `key` is an [IDBKeyRange](/en-US/docs/Web/API/IDBKeyRange).

[IDBObjectStore.index()](/en-US/docs/Web/API/IDBObjectStore/index)

Opens an index from this object store after which it can, for example, be used to return a sequence of records sorted by that index using a cursor.

[IDBObjectStore.openCursor()](/en-US/docs/Web/API/IDBObjectStore/openCursor)

Returns an [IDBRequest](/en-US/docs/Web/API/IDBRequest) object and, in a separate thread, returns a new [IDBCursorWithValue](/en-US/docs/Web/API/IDBCursorWithValue) object. Used for iterating through an object store by primary key with a cursor.

[IDBObjectStore.openKeyCursor()](/en-US/docs/Web/API/IDBObjectStore/openKeyCursor)

Returns an [IDBRequest](/en-US/docs/Web/API/IDBRequest) object and, in a separate thread, returns a new [IDBCursor](/en-US/docs/Web/API/IDBCursor). Used for iterating through an object store with a key.

[IDBObjectStore.put()](/en-US/docs/Web/API/IDBObjectStore/put)

Returns an [IDBRequest](/en-US/docs/Web/API/IDBRequest) object and, in a separate thread, creates a [structured clone](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#structured-clone) of the `value`, and stores the cloned value in the object store. This is for updating existing records in an object store when the transaction's mode is `readwrite`.

## [Example](#example)

This example shows a variety of different uses of object stores, from updating the data structure with [IDBObjectStore.createIndex](/en-US/docs/Web/API/IDBObjectStore/createIndex) inside an `onupgradeneeded` function, to adding a new item to our object store with [IDBObjectStore.add](/en-US/docs/Web/API/IDBObjectStore/add). For a full working example, see our [To-do Notifications](https://github.com/mdn/dom-examples/tree/main/to-do-notifications) app ([view example live](https://mdn.github.io/dom-examples/to-do-notifications/)).

js

```
// Let us open our database
const DBOpenRequest = window.indexedDB.open("toDoList", 4);

DBOpenRequest.onsuccess = (event) => {
  note.appendChild(document.createElement("li")).textContent =
    "Database initialized.";

  // store the result of opening the database in db.
  db = DBOpenRequest.result;
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

  note.appendChild(document.createElement("li")).textContent =
    "Object store created.";
};

// Create a new item to add in to the object store
const newItem = [
  {
    taskTitle: "Walk dog",
    hours: 19,
    minutes: 30,
    day: 24,
    month: "December",
    year: 2013,
    notified: "no",
  },
];

// open a read/write db transaction, ready for adding the data
const transaction = db.transaction(["toDoList"], "readwrite");

// report on the success of the transaction completing, when everything is done
transaction.oncomplete = (event) => {
  note.appendChild(document.createElement("li")).textContent =
    "Transaction completed.";
};

transaction.onerror = (event) => {
  note.appendChild(document.createElement("li")).textContent =
    "Transaction not opened due to error. Duplicate items not allowed.";
};

// create an object store on the transaction
const objectStore = transaction.objectStore("toDoList");
// make a request to add our newItem object to the object store
const objectStoreRequest = objectStore.add(newItem[0]);

objectStoreRequest.onsuccess = (event) => {
  note.appendChild(document.createElement("li")).textContent =
    "Request successful.";
};
```

## [Specifications](#specifications)

Specification
[Indexed Database API 3.0# object-store-interface](https://w3c.github.io/IndexedDB/#object-store-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using IndexedDB](/en-US/docs/Web/API/IndexedDB_API/Using_IndexedDB)
- Starting transactions: [IDBDatabase](/en-US/docs/Web/API/IDBDatabase)
- Using transactions: [IDBTransaction](/en-US/docs/Web/API/IDBTransaction)
- Setting a range of keys: [IDBKeyRange](/en-US/docs/Web/API/IDBKeyRange)
- Using cursors: [IDBCursor](/en-US/docs/Web/API/IDBCursor)
- Reference example: [To-do Notifications](https://github.com/mdn/dom-examples/tree/main/to-do-notifications) ([View the example live](https://mdn.github.io/dom-examples/to-do-notifications/)).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 24, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/IDBObjectStore/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/idbobjectstore/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBObjectStore&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fidbobjectstore%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBObjectStore%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fidbobjectstore%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F55bb65bb6a84808896ed0f6c83e57c60dbd8480e%0A*+Document+last+modified%3A+2025-10-24T17%3A09%3A42.000Z%0A%0A%3C%2Fdetails%3E)
