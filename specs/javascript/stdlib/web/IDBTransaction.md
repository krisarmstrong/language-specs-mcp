# IDBTransaction

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBTransaction&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `IDBTransaction` interface of the [IndexedDB API](/en-US/docs/Web/API/IndexedDB_API) provides a static, asynchronous transaction on a database using event handler attributes. All reading and writing of data is done within transactions. You use [IDBDatabase](/en-US/docs/Web/API/IDBDatabase) to start transactions, `IDBTransaction` to set the mode of the transaction (e.g., is it `readonly` or `readwrite`), and you access an [IDBObjectStore](/en-US/docs/Web/API/IDBObjectStore) to make a request. You can also use an `IDBTransaction` object to abort transactions.

Transactions are started when the transaction is created, not when the first request is placed; for example consider this:

js

```
const trans1 = db.transaction("foo", "readwrite");
const trans2 = db.transaction("foo", "readwrite");
const objectStore2 = trans2.objectStore("foo");
const objectStore1 = trans1.objectStore("foo");
objectStore2.put("2", "key");
objectStore1.put("1", "key");
```

After the code is executed the object store should contain the value "2", since `trans2` should run after `trans1`.

A transaction alternates between active and inactive states between event loop tasks. It's active in the task when it was created, and in each task of the requests' [success](/en-US/docs/Web/API/IDBRequest/success_event) or [error](/en-US/docs/Web/API/IDBRequest/error_event) event handlers. It's inactive in all other tasks, in which case placing requests will fail. If no new requests are placed when the transaction is active, and there are no other outstanding requests, the transaction will automatically commit.

## In this article

- [Transaction failures](#transaction_failures)
- [Firefox durability guarantees](#firefox_durability_guarantees)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Mode constants](#mode_constants)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Transaction failures](#transaction_failures)

Transactions can fail for a fixed number of reasons, all of which (except the user agent crash) will trigger an abort callback:

- Abort due to bad requests, e.g., trying to `add()` the same key twice, or `put()` with the same index key with a uniqueness constraint. This causes an error on the request, which can bubble up to an error on the transaction, which aborts the transaction. This can be prevented by using `preventDefault()` on the error event on the request.
- An explicit `abort()` call from script.
- An uncaught exception in the request's `success`/`error` handler.
- An I/O error (e.g., an actual failure to write to disk, or other OS/hardware failure).
- Quota exceeded.
- A user agent crash.

## [Firefox durability guarantees](#firefox_durability_guarantees)

Note that as of Firefox 40, IndexedDB transactions have relaxed durability guarantees to increase performance (see [Firefox bug 1112702](https://bugzil.la/1112702).) Previously in a `readwrite` transaction, a [complete](/en-US/docs/Web/API/IDBTransaction/complete_event) event was fired only when all data was guaranteed to have been flushed to disk. In Firefox 40+ the `complete` event is fired after the OS has been told to write the data but potentially before that data has actually been flushed to disk. The `complete` event may thus be delivered quicker than before, however, there exists a small chance that the entire transaction will be lost if the OS crashes or there is a loss of system power before the data is flushed to disk. Since such catastrophic events are rare, most consumers should not need to concern themselves further.

If you must ensure durability for some reason (e.g., you're storing critical data that cannot be recomputed later) you can force a transaction to flush to disk before delivering the `complete` event by creating a transaction using the experimental (non-standard) `readwriteflush` mode (see [IDBDatabase.transaction](/en-US/docs/Web/API/IDBDatabase/transaction).

## [Instance properties](#instance_properties)

[IDBTransaction.db](/en-US/docs/Web/API/IDBTransaction/db)Read only

The database connection with which this transaction is associated.

[IDBTransaction.durability](/en-US/docs/Web/API/IDBTransaction/durability)Read only

Returns the durability hint the transaction was created with.

[IDBTransaction.error](/en-US/docs/Web/API/IDBTransaction/error)Read only

Returns a [DOMException](/en-US/docs/Web/API/DOMException) indicating the type of error that occurred when there is an unsuccessful transaction. This property is `null` if the transaction is not finished, is finished and successfully committed, or was aborted with the [IDBTransaction.abort()](/en-US/docs/Web/API/IDBTransaction/abort) function.

[IDBTransaction.mode](/en-US/docs/Web/API/IDBTransaction/mode)Read only

The mode for isolating access to data in the object stores that are in the scope of the transaction. The default value is `readonly`.

[IDBTransaction.objectStoreNames](/en-US/docs/Web/API/IDBTransaction/objectStoreNames)Read only

Returns a [DOMStringList](/en-US/docs/Web/API/DOMStringList) of the names of [IDBObjectStore](/en-US/docs/Web/API/IDBObjectStore) objects associated with the transaction.

## [Instance methods](#instance_methods)

Inherits from: [EventTarget](/en-US/docs/Web/API/EventTarget)

[IDBTransaction.abort()](/en-US/docs/Web/API/IDBTransaction/abort)

Rolls back all the changes to objects in the database associated with this transaction. If this transaction has been aborted or completed, this method fires an error event.

[IDBTransaction.objectStore()](/en-US/docs/Web/API/IDBTransaction/objectStore)

Returns an [IDBObjectStore](/en-US/docs/Web/API/IDBObjectStore) object representing an object store that is part of the scope of this transaction.

[IDBTransaction.commit()](/en-US/docs/Web/API/IDBTransaction/commit)

For an active transaction, commits the transaction. Note that this doesn't normally have to be called — a transaction will automatically commit when all outstanding requests have been satisfied and no new requests have been made. `commit()` can be used to start the commit process without waiting for events from outstanding requests to be dispatched.

## [Events](#events)

Listen to these events using `addEventListener()` or by assigning an event listener to the `oneventname` property of this interface.

[abort](/en-US/docs/Web/API/IDBTransaction/abort_event)

An event fired when the `IndexedDB` transaction is aborted. Also available via the `onabort` property; this event bubbles to [IDBDatabase](/en-US/docs/Web/API/IDBDatabase).

[complete](/en-US/docs/Web/API/IDBTransaction/complete_event)

An event fired when the transaction successfully completes. Also available via the `oncomplete` property.

[error](/en-US/docs/Web/API/IDBTransaction/error_event)

An event fired when a request returns an error and the event bubbles up to the connection object ([IDBDatabase](/en-US/docs/Web/API/IDBDatabase)). Also available via the `onerror` property.

## [Mode constants](#mode_constants)

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

Warning: These constants are no longer available — they were removed in Gecko 25. You should use the string constants directly instead. ([Firefox bug 888598](https://bugzil.la/888598))

Transactions can have one of three modes:

ConstantValueDescription`READ_ONLY`"readonly" (0 in Chrome)

Allows data to be read but not changed.

`READ_WRITE`"readwrite" (1 in Chrome) Allows reading and writing of data in existing data stores to be changed. `VERSION_CHANGE`"versionchange" (2 in Chrome) Allows any operation to be performed, including ones that delete and create object stores and indexes. Transactions of this mode cannot run concurrently with other transactions. Transactions in this mode are known as "upgrade transactions." 

Even if these constants are now deprecated, you can still use them to provide backward compatibility if required. You should code defensively in case the object is not available anymore:

js

```
const myIDBTransaction = window.IDBTransaction ||
  window.webkitIDBTransaction || { READ_WRITE: "readwrite" };
```

## [Examples](#examples)

In the following code snippet, we open a read/write transaction on our database and add some data to an object store. Note also the functions attached to transaction event handlers to report on the outcome of the transaction opening in the event of success or failure. For a full working example, see our [To-do Notifications](https://github.com/mdn/dom-examples/tree/main/to-do-notifications) app ([view example live](https://mdn.github.io/dom-examples/to-do-notifications/)).

js

```
const note = document.getElementById("notifications");

// an instance of a db object for us to store the IDB data in
let db;

// Let us open our database
const DBOpenRequest = window.indexedDB.open("toDoList", 4);

DBOpenRequest.onsuccess = (event) => {
  note.appendChild(document.createElement("li")).textContent =
    "Database initialized.";

  // store the result of opening the database in the db
  // variable. This is used a lot below
  db = DBOpenRequest.result;

  // Add the data to the database
  addData();
};

function addData() {
  // Create a new object to insert into the IDB
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

  // open a read/write db transaction, ready to add data
  const transaction = db.transaction(["toDoList"], "readwrite");

  // report on the success of opening the transaction
  transaction.oncomplete = (event) => {
    note.appendChild(document.createElement("li")).textContent =
      "Transaction completed: database modification finished.";
  };

  transaction.onerror = (event) => {
    note.appendChild(document.createElement("li")).textContent =
      "Transaction not opened due to error. Duplicate items not allowed.";
  };

  // create an object store on the transaction
  const objectStore = transaction.objectStore("toDoList");

  // add our newItem object to the object store
  const objectStoreRequest = objectStore.add(newItem[0]);

  objectStoreRequest.onsuccess = (event) => {
    // report the success of the request (this does not mean the item
    // has been stored successfully in the DB - for that you need transaction.oncomplete)
    note.appendChild(document.createElement("li")).textContent =
      "Request successful.";
  };
}
```

## [Specifications](#specifications)

Specification
[Indexed Database API 3.0# transaction](https://w3c.github.io/IndexedDB/#transaction)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using IndexedDB](/en-US/docs/Web/API/IndexedDB_API/Using_IndexedDB)
- Starting transactions: [IDBDatabase](/en-US/docs/Web/API/IDBDatabase)
- Setting a range of keys: [IDBKeyRange](/en-US/docs/Web/API/IDBKeyRange)
- Retrieving and making changes to your data: [IDBObjectStore](/en-US/docs/Web/API/IDBObjectStore)
- Using cursors: [IDBCursor](/en-US/docs/Web/API/IDBCursor)
- Reference example: [To-do Notifications](https://github.com/mdn/dom-examples/tree/main/to-do-notifications) ([View the example live](https://mdn.github.io/dom-examples/to-do-notifications/)).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 17, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/IDBTransaction/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/idbtransaction/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBTransaction&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fidbtransaction%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBTransaction%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fidbtransaction%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F09877330004e55244a9e8eee2ca04a750970f72d%0A*+Document+last+modified%3A+2025-06-17T07%3A50%3A47.000Z%0A%0A%3C%2Fdetails%3E)
