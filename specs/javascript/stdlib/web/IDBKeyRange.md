# IDBKeyRange

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBKeyRange&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `IDBKeyRange` interface of the [IndexedDB API](/en-US/docs/Web/API/IndexedDB_API) represents a continuous interval over some data type that is used for keys. Records can be retrieved from [IDBObjectStore](/en-US/docs/Web/API/IDBObjectStore) and [IDBIndex](/en-US/docs/Web/API/IDBIndex) objects using keys or a range of keys. You can limit the range using lower and upper bounds. For example, you can iterate over all values of a key in the value range A–Z.

A key range can be a single value or a range with upper and lower bounds or endpoints. If the key range has both upper and lower bounds, then it is bounded; if it has no bounds, it is unbounded. A bounded key range can either be open (the endpoints are excluded) or closed (the endpoints are included). To retrieve all keys within a certain range, you can use the following code constructs:

RangeCodeAll keys ≥ x`IDBKeyRange.lowerBound(x)`All keys > x`IDBKeyRange.lowerBound(x, true)`All keys ≤ y`IDBKeyRange.upperBound(y)`All keys < y`IDBKeyRange.upperBound(y, true)`All keys ≥ x && ≤ y`IDBKeyRange.bound(x, y)`All keys > x &&< y`IDBKeyRange.bound(x, y, true, true)`All keys > x && ≤ y`IDBKeyRange.bound(x, y, true, false)`All keys ≥ x &&< y`IDBKeyRange.bound(x, y, false, true)`The key = z`IDBKeyRange.only(z)`

A key is in a key range if the following conditions are true:

- 

The lower value of the key range is one of the following:

  - `undefined`
  - Less than key value
  - Equal to key value if `lowerOpen` is `false`.

- 

The upper value of the key range is one of the following:

  - `undefined`
  - Greater than key value
  - Equal to key value if `upperOpen` is `false`.

## In this article

- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[IDBKeyRange.lower](/en-US/docs/Web/API/IDBKeyRange/lower)Read only

Lower bound of the key range.

[IDBKeyRange.upper](/en-US/docs/Web/API/IDBKeyRange/upper)Read only

Upper bound of the key range.

[IDBKeyRange.lowerOpen](/en-US/docs/Web/API/IDBKeyRange/lowerOpen)Read only

Returns false if the lower-bound value is included in the key range.

[IDBKeyRange.upperOpen](/en-US/docs/Web/API/IDBKeyRange/upperOpen)Read only

Returns false if the upper-bound value is included in the key range.

## [Static methods](#static_methods)

[IDBKeyRange.bound()](/en-US/docs/Web/API/IDBKeyRange/bound_static)

Creates a new key range with upper and lower bounds.

[IDBKeyRange.only()](/en-US/docs/Web/API/IDBKeyRange/only_static)

Creates a new key range containing a single value.

[IDBKeyRange.lowerBound()](/en-US/docs/Web/API/IDBKeyRange/lowerBound_static)

Creates a new key range with only a lower bound.

[IDBKeyRange.upperBound()](/en-US/docs/Web/API/IDBKeyRange/upperBound_static)

Creates a new upper-bound key range.

## [Instance methods](#instance_methods)

[IDBKeyRange.includes()](/en-US/docs/Web/API/IDBKeyRange/includes)

Returns a boolean indicating whether a specified key is inside the key range.

## [Examples](#examples)

The following example illustrates how you'd use a key range. Here we declare a `keyRangeValue` as a range between values of `"A"` and `"F"`. We open a transaction (using [IDBTransaction](/en-US/docs/Web/API/IDBTransaction)) and an object store, and open a cursor with [IDBObjectStore.openCursor](/en-US/docs/Web/API/IDBObjectStore/openCursor), declaring `keyRangeValue` as its optional key range value. This means that the cursor will only retrieve records with keys inside that range. This range includes the values `"A"` and `"F"`, as we haven't declared that they should be open bounds. If we used `IDBKeyRange.bound("A", "F", true, true);`, then the range would not include `"A"` and `"F"`, only the values between them.

Note: For a more complete example allowing you to experiment with key range, have a look at our [IDBKeyRange-example](https://github.com/mdn/dom-examples/tree/main/indexeddb-examples/idbkeyrange) repo ([view the example live too](https://mdn.github.io/dom-examples/indexeddb-examples/idbkeyrange/).)

js

```
function displayData() {
  const keyRangeValue = IDBKeyRange.bound("A", "F");

  const transaction = db.transaction(["fThings"], "readonly");
  const objectStore = transaction.objectStore("fThings");

  objectStore.openCursor(keyRangeValue).onsuccess = (event) => {
    const cursor = event.target.result;
    if (cursor) {
      const listItem = document.createElement("li");
      listItem.textContent = `${cursor.value.fThing}, ${cursor.value.fRating}`;
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
[Indexed Database API 3.0# keyrange](https://w3c.github.io/IndexedDB/#keyrange)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using IndexedDB](/en-US/docs/Web/API/IndexedDB_API/Using_IndexedDB)
- Starting transactions: [IDBDatabase](/en-US/docs/Web/API/IDBDatabase)
- Using transactions: [IDBTransaction](/en-US/docs/Web/API/IDBTransaction)
- Retrieving and making changes to your data: [IDBObjectStore](/en-US/docs/Web/API/IDBObjectStore)
- Using cursors: [IDBCursor](/en-US/docs/Web/API/IDBCursor)
- Reference example: [To-do Notifications](https://github.com/mdn/dom-examples/tree/main/to-do-notifications) ([View the example live](https://mdn.github.io/dom-examples/to-do-notifications/)).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/IDBKeyRange/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/idbkeyrange/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBKeyRange&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fidbkeyrange%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIDBKeyRange%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fidbkeyrange%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
