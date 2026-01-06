# IDBCursor

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBCursor&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

Note: Not to be confused with [IDBCursorWithValue](/en-US/docs/Web/API/IDBCursorWithValue) which is just an `IDBCursor` interface with an additional `value` property.

The `IDBCursor` interface of the [IndexedDB API](/en-US/docs/Web/API/IndexedDB_API) represents a [cursor](/en-US/docs/Web/API/IndexedDB_API/Basic_Terminology#cursor) for traversing or iterating over multiple records in a database.

The cursor has a source that indicates which index or object store it is iterating over. It has a position within the range, and moves in a direction that is increasing or decreasing in the order of record keys. The cursor enables an application to asynchronously process all the records in the cursor's range.

You can have an unlimited number of cursors at the same time. You always get the same `IDBCursor` object representing a given cursor. Operations are performed on the underlying index or object store.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Constants](#constants)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Note:[IDBCursorWithValue](/en-US/docs/Web/API/IDBCursorWithValue) is an `IDBCursor` interface with an additional `value` property.

[IDBCursor.source](/en-US/docs/Web/API/IDBCursor/source)Read only

Returns the [IDBObjectStore](/en-US/docs/Web/API/IDBObjectStore) or [IDBIndex](/en-US/docs/Web/API/IDBIndex) that the cursor is iterating. This function never returns null or throws an exception, even if the cursor is currently being iterated, has iterated past its end, or its transaction is not active.

[IDBCursor.direction](/en-US/docs/Web/API/IDBCursor/direction)Read only

Returns the direction of traversal of the cursor.

[IDBCursor.key](/en-US/docs/Web/API/IDBCursor/key)Read only

Returns the key for the record at the cursor's position. If the cursor is outside its range, this is set to `undefined`. The cursor's key can be any data type.

[IDBCursor.primaryKey](/en-US/docs/Web/API/IDBCursor/primaryKey)Read only

Returns the cursor's current effective primary key. If the cursor is currently being iterated or has iterated outside its range, this is set to `undefined`. The cursor's primary key can be any data type.

[IDBCursor.request](/en-US/docs/Web/API/IDBCursor/request)Read only

Returns the [IDBRequest](/en-US/docs/Web/API/IDBRequest) that was used to obtain the cursor.

## [Instance methods](#instance_methods)

[IDBCursor.advance()](/en-US/docs/Web/API/IDBCursor/advance)

Sets the number of times a cursor should move its position forward.

[IDBCursor.continue()](/en-US/docs/Web/API/IDBCursor/continue)

Advances the cursor to the next position along its direction, to the item whose key matches the optional `key` parameter.

[IDBCursor.continuePrimaryKey()](/en-US/docs/Web/API/IDBCursor/continuePrimaryKey)

Sets the cursor to the given index key and primary key given as arguments.

[IDBCursor.delete()](/en-US/docs/Web/API/IDBCursor/delete)

Returns an [IDBRequest](/en-US/docs/Web/API/IDBRequest) object, and, in a separate thread, deletes the record at the cursor's position, without changing the cursor's position. This can be used to delete specific records.

[IDBCursor.update()](/en-US/docs/Web/API/IDBCursor/update)

Returns an [IDBRequest](/en-US/docs/Web/API/IDBRequest) object, and, in a separate thread, updates the value at the current position of the cursor in the object store. This can be used to update specific records.

## [Constants](#constants)

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

Warning: These constants are no longer available — they were removed in Gecko 25. You should use the string constants directly instead. ([Firefox bug 891944](https://bugzil.la/891944))

- `NEXT`: `"next"` : The cursor shows all records, including duplicates. It starts at the lower bound of the key range and moves upwards (monotonically increasing in the order of keys).
- `NEXTUNIQUE` : `"nextunique"` : The cursor shows all records, excluding duplicates. If multiple records exist with the same key, only the first one iterated is retrieved. It starts at the lower bound of the key range and moves upwards.
- `PREV`: `"prev"` : The cursor shows all records, including duplicates. It starts at the upper bound of the key range and moves downwards (monotonically decreasing in the order of keys).
- `PREVUNIQUE`: `"prevunique"` : The cursor shows all records, excluding duplicates. If multiple records exist with the same key, only the first one iterated is retrieved. It starts at the upper bound of the key range and moves downwards.

## [Examples](#examples)

In this simple fragment we create a transaction, retrieve an object store, then use a cursor to iterate through all the records in the object store. The cursor does not require us to select the data based on a key; we can just grab all of it. Also note that in each iteration of the loop, you can grab data from the current record under the cursor object using `cursor.value.foo`. For a complete working example, see our [IDBCursor example](https://github.com/mdn/dom-examples/tree/main/indexeddb-examples/idbcursor) ([view example live](https://mdn.github.io/dom-examples/indexeddb-examples/idbcursor/).)

js

```
function displayData() {
  const transaction = db.transaction(["rushAlbumList"], "readonly");
  const objectStore = transaction.objectStore("rushAlbumList");

  objectStore.openCursor().onsuccess = (event) => {
    const cursor = event.target.result;
    if (cursor) {
      const listItem = document.createElement("li");
      listItem.textContent = `${cursor.value.albumTitle}, ${cursor.value.year}`;
      list.appendChild(listItem);

      cursor.continue();
    } else {
      console.log("Entries all displayed.");
    }
  };
}
```

## [Specifications](#specifications)

Specification
[Indexed Database API 3.0# cursor-interface](https://w3c.github.io/IndexedDB/#cursor-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using IndexedDB](/en-US/docs/Web/API/IndexedDB_API/Using_IndexedDB)
- Starting transactions: [IDBDatabase](/en-US/docs/Web/API/IDBDatabase)
- Using transactions: [IDBTransaction](/en-US/docs/Web/API/IDBTransaction)
- Setting a range of keys: [IDBKeyRange](/en-US/docs/Web/API/IDBKeyRange)
- Retrieving and making changes to your data: [IDBObjectStore](/en-US/docs/Web/API/IDBObjectStore)
- Reference example: [To-do Notifications](https://github.com/mdn/dom-examples/tree/main/to-do-notifications) ([view example live](https://mdn.github.io/dom-examples/to-do-notifications/)).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 24, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/IDBCursor/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/idbcursor/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBCursor&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fidbcursor%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBCursor%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fidbcursor%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa84b606ffd77c40a7306be6c932a74ab9ce6ab96%0A*+Document+last+modified%3A+2025-06-24T06%3A12%3A11.000Z%0A%0A%3C%2Fdetails%3E)
