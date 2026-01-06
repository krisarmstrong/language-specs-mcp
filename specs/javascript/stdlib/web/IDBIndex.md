# IDBIndex

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBIndex&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

`IDBIndex` interface of the [IndexedDB API](/en-US/docs/Web/API/IndexedDB_API) provides asynchronous access to an [index](/en-US/docs/Web/API/IndexedDB_API/Basic_Terminology#index) in a database. An index is a kind of object store for looking up records in another object store, called the referenced object store. You use this interface to retrieve data.

You can retrieve records in an object store through the primary key or by using an index. An index lets you look up records in an object store using properties of the values in the object stores records other than the primary key

The index is a persistent key-value storage where the value part of its records is the key part of a record in the referenced object store. The records in an index are automatically populated whenever records in the referenced object store are inserted, updated, or deleted. Each record in an index can point to only one record in its referenced object store, but several indexes can reference the same object store. When the object store changes, all indexes that refers to the object store are automatically updated.

You can grab a set of keys within a range. To learn more, see [IDBKeyRange](/en-US/docs/Web/API/IDBKeyRange).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[IDBIndex.isAutoLocale](/en-US/docs/Web/API/IDBIndex/isAutoLocale)Read onlyNon-standardDeprecated

Returns a boolean value indicating whether the index had a `locale` value of `auto` specified upon its creation (see the [options](/en-US/docs/Web/API/IDBObjectStore/createIndex#options) parameter to [IDBObjectStore.createIndex()](/en-US/docs/Web/API/IDBObjectStore/createIndex).)

[IDBIndex.locale](/en-US/docs/Web/API/IDBIndex/locale)Read onlyNon-standardDeprecated

Returns the locale of the index (for example `en-US`, or `pl`) if it had a `locale` value specified upon its creation (see the [options](/en-US/docs/Web/API/IDBObjectStore/createIndex#options) parameter to [IDBObjectStore.createIndex()](/en-US/docs/Web/API/IDBObjectStore/createIndex).)

[IDBIndex.name](/en-US/docs/Web/API/IDBIndex/name)

The name of this index.

[IDBIndex.objectStore](/en-US/docs/Web/API/IDBIndex/objectStore)Read only

The name of the object store referenced by this index.

[IDBIndex.keyPath](/en-US/docs/Web/API/IDBIndex/keyPath)Read only

The [key path](/en-US/docs/Web/API/IndexedDB_API/Basic_Terminology#key_path) of this index. If null, this index is not auto-populated.

[IDBIndex.multiEntry](/en-US/docs/Web/API/IDBIndex/multiEntry)Read only

Affects how the index behaves when the result of evaluating the index's key path yields an array. If `true`, there is one record in the index for each item in an array of keys. If `false`, then there is one record for each key that is an array.

[IDBIndex.unique](/en-US/docs/Web/API/IDBIndex/unique)Read only

If `true`, this index does not allow duplicate values for a key.

## [Instance methods](#instance_methods)

Inherits from: [EventTarget](/en-US/docs/Web/API/EventTarget)

[IDBIndex.count()](/en-US/docs/Web/API/IDBIndex/count)

Returns an [IDBRequest](/en-US/docs/Web/API/IDBRequest) object and, in a separate thread, returns the number of records within a key range.

[IDBIndex.get()](/en-US/docs/Web/API/IDBIndex/get)

Returns an [IDBRequest](/en-US/docs/Web/API/IDBRequest) object and, in a separate thread, finds either the value in the referenced object store that corresponds to the given key or the first corresponding value, if `key` is an [IDBKeyRange](/en-US/docs/Web/API/IDBKeyRange).

[IDBIndex.getKey()](/en-US/docs/Web/API/IDBIndex/getKey)

Returns an [IDBRequest](/en-US/docs/Web/API/IDBRequest) object and, in a separate thread, finds either the given key or the primary key, if `key` is an [IDBKeyRange](/en-US/docs/Web/API/IDBKeyRange).

[IDBIndex.getAll()](/en-US/docs/Web/API/IDBIndex/getAll)

Returns an [IDBRequest](/en-US/docs/Web/API/IDBRequest) object and, in a separate thread, finds all matching values in the referenced object store that correspond to the given key or are in range, if `key` is an [IDBKeyRange](/en-US/docs/Web/API/IDBKeyRange).

[IDBIndex.getAllKeys()](/en-US/docs/Web/API/IDBIndex/getAllKeys)

Returns an [IDBRequest](/en-US/docs/Web/API/IDBRequest) object and, in a separate thread, finds all matching keys in the referenced object store that correspond to the given key or are in range, if `key` is an [IDBKeyRange](/en-US/docs/Web/API/IDBKeyRange).

[IDBIndex.getAllRecords()](/en-US/docs/Web/API/IDBIndex/getAllRecords)Experimental

Returns an [IDBRequest](/en-US/docs/Web/API/IDBRequest) object and, in a separate thread, finds all matching records in the referenced object store (including index keys, primary keys, and values) that correspond to the given key or are in range, if `key` is an [IDBKeyRange](/en-US/docs/Web/API/IDBKeyRange).

[IDBIndex.openCursor()](/en-US/docs/Web/API/IDBIndex/openCursor)

Returns an [IDBRequest](/en-US/docs/Web/API/IDBRequest) object and, in a separate thread, creates a [cursor](/en-US/docs/Web/API/IndexedDB_API/Basic_Terminology#cursor) over the specified key range.

[IDBIndex.openKeyCursor()](/en-US/docs/Web/API/IDBIndex/openKeyCursor)

Returns an [IDBRequest](/en-US/docs/Web/API/IDBRequest) object and, in a separate thread, creates a cursor over the specified key range, as arranged by this index.

## [Example](#example)

In the following example we open a transaction and an object store, then get the index `lName` from a simple contacts database. We then open a basic cursor on the index using [IDBIndex.openCursor](/en-US/docs/Web/API/IDBIndex/openCursor) — this works the same as opening a cursor directly on an `ObjectStore` using [IDBObjectStore.openCursor](/en-US/docs/Web/API/IDBObjectStore/openCursor) except that the returned records are sorted based on the index, not the primary key.

Finally, we iterate through each record, and insert the data into an HTML table. For a complete working example, see our [IndexedDB-examples demo repo](https://github.com/mdn/dom-examples/tree/main/indexeddb-examples/idbindex) ([View the example live](https://mdn.github.io/dom-examples/indexeddb-examples/idbindex/).)

js

```
function displayDataByIndex() {
  tableEntry.textContent = "";
  const transaction = db.transaction(["contactsList"], "readonly");
  const objectStore = transaction.objectStore("contactsList");

  const myIndex = objectStore.index("lName");
  myIndex.openCursor().onsuccess = (event) => {
    const cursor = event.target.result;
    if (cursor) {
      const tableRow = document.createElement("tr");
      for (const cell of [
        cursor.value.id,
        cursor.value.lName,
        cursor.value.fName,
        cursor.value.jTitle,
        cursor.value.company,
        cursor.value.eMail,
        cursor.value.phone,
        cursor.value.age,
      ]) {
        const tableCell = document.createElement("td");
        tableCell.textContent = cell;
        tableRow.appendChild(tableCell);
      }
      tableEntry.appendChild(tableRow);

      cursor.continue();
    } else {
      console.log("Entries all displayed.");
    }
  };
}
```

## [Specifications](#specifications)

Specification
[Indexed Database API 3.0# index-interface](https://w3c.github.io/IndexedDB/#index-interface)

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

 This page was last modified on ⁨Oct 24, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/IDBIndex/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/idbindex/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBIndex&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fidbindex%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBIndex%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fidbindex%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F55bb65bb6a84808896ed0f6c83e57c60dbd8480e%0A*+Document+last+modified%3A+2025-10-24T17%3A09%3A42.000Z%0A%0A%3C%2Fdetails%3E)
