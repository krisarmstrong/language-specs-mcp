# IDBFactory

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBFactory&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `IDBFactory` interface of the [IndexedDB API](/en-US/docs/Web/API/IndexedDB_API) lets applications asynchronously access the indexed databases. The object that implements the interface is `window.indexedDB`. You open — that is, create and access — and delete a database with this object, and not directly with `IDBFactory`.

## In this article

- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

[IDBFactory.open()](/en-US/docs/Web/API/IDBFactory/open)

Requests opening a [connection to a database](/en-US/docs/Web/API/IndexedDB_API/Basic_Terminology#database_connection).

[IDBFactory.deleteDatabase()](/en-US/docs/Web/API/IDBFactory/deleteDatabase)

Requests the deletion of a database.

[IDBFactory.cmp()](/en-US/docs/Web/API/IDBFactory/cmp)

Compares two keys and returns a result indicating which one is greater in value.

[IDBFactory.databases()](/en-US/docs/Web/API/IDBFactory/databases)

Returns a promise that fulfills with an array of all available databases, including their names and versions.

## [Example](#example)

In the following code snippet, we make a request to open a database, and include handlers for the success and error cases. For a full working example, see our [To-do Notifications](https://github.com/mdn/dom-examples/tree/main/to-do-notifications) app ([view example live](https://mdn.github.io/dom-examples/to-do-notifications/)).

js

```
// Let us open version 4 of our database
const DBOpenRequest = window.indexedDB.open("toDoList", 4);

// these two event handlers act on the database being opened successfully, or not
DBOpenRequest.onerror = (event) => {
  console.error("Error loading database.");
};

DBOpenRequest.onsuccess = (event) => {
  console.info("Database initialized.");

  // store the result of opening the database in the db variable. This is used a lot later on, for opening transactions and suchlike.
  db = DBOpenRequest.result;
};
```

## [Specifications](#specifications)

Specification
[Indexed Database API 3.0# factory-interface](https://w3c.github.io/IndexedDB/#factory-interface)

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

 This page was last modified on ⁨May 5, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/IDBFactory/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/idbfactory/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBFactory&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fidbfactory%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBFactory%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fidbfactory%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fdbd4ba01220a5031d3a26a3ac1490d3269210124%0A*+Document+last+modified%3A+2024-05-05T22%3A36%3A40.000Z%0A%0A%3C%2Fdetails%3E)
