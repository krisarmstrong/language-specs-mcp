# IndexedDB API

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

IndexedDB is a low-level API for client-side storage of significant amounts of structured data, including files/blobs. This API uses indexes to enable high-performance searches of this data. While [Web Storage](/en-US/docs/Web/API/Web_Storage_API) is useful for storing smaller amounts of data, it is less useful for storing larger amounts of structured data. IndexedDB provides a solution. This is the main landing page for MDN's IndexedDB coverage — here we provide links to the full API reference and usage guides, browser support details, and some explanation of key concepts.

## In this article

- [Key concepts and usage](#key_concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [See also](#see_also)

## [Key concepts and usage](#key_concepts_and_usage)

IndexedDB is a transactional database system, like an SQL-based Relational Database Management System (RDBMS). However, unlike SQL-based RDBMSes, which use fixed-column tables, IndexedDB is a JavaScript-based object-oriented database. IndexedDB lets you store and retrieve objects that are indexed with a key; any objects supported by the [structured clone algorithm](/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm) can be stored. You need to specify the database schema, open a connection to your database, and then retrieve and update data within a series of transactions.

- Read more about [IndexedDB key characteristics and basic terminology](/en-US/docs/Web/API/IndexedDB_API/Basic_Terminology).
- Learn to use IndexedDB asynchronously from first principles with our [Using IndexedDB](/en-US/docs/Web/API/IndexedDB_API/Using_IndexedDB) guide.
- See a complete step-by-step example in the [checking when a deadline is due](/en-US/docs/Web/API/IndexedDB_API/Checking_when_a_deadline_is_due) guide.

Note: Like most web storage solutions, IndexedDB follows a [same-origin policy](https://www.w3.org/Security/wiki/Same_Origin_Policy). So while you can access stored data within a domain, you cannot access data across different domains.

### [Synchronous and asynchronous](#synchronous_and_asynchronous)

Operations performed using IndexedDB are done asynchronously, so as not to block applications.

### [Storage limits and eviction criteria](#storage_limits_and_eviction_criteria)

There are a number of web technologies that store data of one kind or another on the client side (i.e., on your local disk). IndexedDB is most commonly talked about. The process by which the browser works out how much space to allocate to web data storage and what to delete when that limit is reached is not simple, and differs between browsers. [Browser storage quotas and eviction criteria](/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria) attempts to explain how this works, at least in the case of Firefox.

## [Interfaces](#interfaces)

To get access to a database, call [open()](/en-US/docs/Web/API/IDBFactory/open) on the [indexedDB](/en-US/docs/Web/API/Window/indexedDB) property of a [window](/en-US/docs/Web/API/Window) object. This method returns an [IDBRequest](/en-US/docs/Web/API/IDBRequest) object; asynchronous operations communicate to the calling application by firing events on [IDBRequest](/en-US/docs/Web/API/IDBRequest) objects.

### [Connecting to a database](#connecting_to_a_database)

[IDBFactory](/en-US/docs/Web/API/IDBFactory)

Provides access to a database. An object of this type is the value of the global [Window.indexedDB](/en-US/docs/Web/API/Window/indexedDB) and [WorkerGlobalScope.indexedDB](/en-US/docs/Web/API/WorkerGlobalScope/indexedDB) properties. It is therefore the entry point for the API.

[IDBOpenDBRequest](/en-US/docs/Web/API/IDBOpenDBRequest)

Represents a request to open a database.

[IDBDatabase](/en-US/docs/Web/API/IDBDatabase)

Represents a connection to a database. It's the only way to get a transaction on the database.

### [Retrieving and modifying data](#retrieving_and_modifying_data)

[IDBTransaction](/en-US/docs/Web/API/IDBTransaction)

Represents a transaction. You create a transaction on a database, specify the scope (such as which object stores you want to access), and determine the kind of access (read only or readwrite) that you want.

[IDBRequest](/en-US/docs/Web/API/IDBRequest)

Generic interface that handles database requests and provides access to results.

[IDBObjectStore](/en-US/docs/Web/API/IDBObjectStore)

Represents an object store that allows access to a set of data in an IndexedDB database, looked up via primary key.

[IDBIndex](/en-US/docs/Web/API/IDBIndex)

Also allows access to a subset of data in an IndexedDB database, but uses an index to retrieve the record(s) rather than the primary key. This is sometimes faster than using [IDBObjectStore](/en-US/docs/Web/API/IDBObjectStore).

[IDBCursor](/en-US/docs/Web/API/IDBCursor)

Iterates over object stores and indexes.

[IDBCursorWithValue](/en-US/docs/Web/API/IDBCursorWithValue)

Iterates over object stores and indexes and returns the cursor's current value.

[IDBKeyRange](/en-US/docs/Web/API/IDBKeyRange)

Defines a key range that can be used to retrieve data from a database in a certain range.

### [Custom event interfaces](#custom_event_interfaces)

This specification fires events with the following custom interface:

[IDBVersionChangeEvent](/en-US/docs/Web/API/IDBVersionChangeEvent)

The `IDBVersionChangeEvent` interface indicates that the version of the database has changed, as the result of an [IDBOpenDBRequest.onupgradeneeded](/en-US/docs/Web/API/IDBOpenDBRequest/upgradeneeded_event) event handler function.

## [Examples](#examples)

- [To-do Notifications](https://github.com/mdn/dom-examples/tree/main/to-do-notifications) ([view example live](https://mdn.github.io/dom-examples/to-do-notifications/)): The reference application for the examples in the reference docs.

## [Specifications](#specifications)

Specification[Indexed Database API 3.0](https://w3c.github.io/IndexedDB/)

## [See also](#see_also)

- [Web Storage API](/en-US/docs/Web/API/Web_Storage_API)
- [Window: localStorage property](/en-US/docs/Web/API/Window/localStorage)
- [Window: sessionStorage property](/en-US/docs/Web/API/Window/sessionStorage)
- [StorageEvent](/en-US/docs/Web/API/StorageEvent)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/IndexedDB_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/indexeddb_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIndexedDB_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Findexeddb_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIndexedDB_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Findexeddb_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F702cd9e4d2834e13aea345943efc8d0c03d92ec9%0A*+Document+last+modified%3A+2025-04-03T04%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
