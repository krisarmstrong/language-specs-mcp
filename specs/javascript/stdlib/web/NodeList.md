# NodeList

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNodeList&level=high)

`NodeList` objects are collections of [nodes](/en-US/docs/Web/API/Node), usually returned by properties such as [Node.childNodes](/en-US/docs/Web/API/Node/childNodes) and methods such as [document.querySelectorAll()](/en-US/docs/Web/API/Document/querySelectorAll).

This interface was an [attempt to create an unmodifiable list](https://stackoverflow.com/questions/74630989/why-use-domstringlist-rather-than-an-array/74641156#74641156) and only continues to be supported to not break code that's already using it. Modern APIs represent list structures using types based on JavaScript [arrays](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array), thus making many array methods available, and at the same time imposing additional semantics on their usage (such as making their items read-only).

These historical reasons do not mean that you as a developer should avoid `NodeList`. You don't create `NodeList` objects yourself, but you get them from APIs such as [Document.querySelectorAll()](/en-US/docs/Web/API/Document/querySelectorAll), and these APIs are not deprecated. However, be careful of the semantic differences from a real array.

Although `NodeList` is not an `Array`, it is possible to iterate over it with `forEach()`. It can also be converted to a real `Array` using [Array.from()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from).

## In this article

- [Live vs. Static NodeLists](#live_vs._static_nodelists)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Live vs. Static NodeLists](#live_vs._static_nodelists)

Although they are both considered `NodeList` objects, there are 2 varieties of NodeList: live and static.

In most cases, the `NodeList` is live, which means that changes in the DOM automatically update the collection.

For example, [Node.childNodes](/en-US/docs/Web/API/Node/childNodes) is live:

js

```
const parent = document.getElementById("parent");
let childNodes = parent.childNodes;
console.log(childNodes.length); // let's assume "2"
parent.appendChild(document.createElement("div"));
console.log(childNodes.length); // outputs "3"
```

In other cases, the `NodeList` is static, where any changes in the DOM do not affect the content of the collection. The ubiquitous [document.querySelectorAll()](/en-US/docs/Web/API/Document/querySelectorAll) method is the only API that returns a static`NodeList`.

It's good to keep this distinction in mind when you choose how to iterate over the items in the `NodeList`, and whether you should cache the list's `length`.

## [Instance properties](#instance_properties)

[NodeList.length](/en-US/docs/Web/API/NodeList/length)Read only

The number of nodes in the `NodeList`.

## [Instance methods](#instance_methods)

[NodeList.item()](/en-US/docs/Web/API/NodeList/item)

Returns an item in the list by its index, or `null` if the index is out-of-bounds.

An alternative to accessing `nodeList[i]` (which instead returns `undefined` when `i` is out-of-bounds). This is mostly useful for non-JavaScript DOM implementations.

[NodeList.entries()](/en-US/docs/Web/API/NodeList/entries)

Returns an [iterator](/en-US/docs/Web/JavaScript/Reference/Iteration_protocols), allowing code to go through all key/value pairs contained in the collection. (In this case, the keys are integers starting from `0` and the values are nodes.)

[NodeList.forEach()](/en-US/docs/Web/API/NodeList/forEach)

Executes a provided function once per `NodeList` element, passing the element as an argument to the function.

[NodeList.keys()](/en-US/docs/Web/API/NodeList/keys)

Returns an [iterator](/en-US/docs/Web/JavaScript/Reference/Iteration_protocols), allowing code to go through all the keys of the key/value pairs contained in the collection. (In this case, the keys are integers starting from `0`.)

[NodeList.values()](/en-US/docs/Web/API/NodeList/values)

Returns an [iterator](/en-US/docs/Web/JavaScript/Reference/Iteration_protocols) allowing code to go through all values (nodes) of the key/value pairs contained in the collection.

## [Example](#example)

It's possible to loop over the items in a `NodeList` using a [for](/en-US/docs/Web/JavaScript/Reference/Statements/for) loop:

js

```
for (let i = 0; i < myNodeList.length; i++) {
  let item = myNodeList[i];
}
```

Don't use [for...in](/en-US/docs/Web/JavaScript/Reference/Statements/for...in) to enumerate the items in `NodeList`s, since they will also enumerate its `length` and `item` properties and cause errors if your script assumes it only has to deal with [element](/en-US/docs/Web/API/Element) objects. Also, `for...in` is not guaranteed to visit the properties in any particular order.

[for...of](/en-US/docs/Web/JavaScript/Reference/Statements/for...of) loops over `NodeList` objects correctly:

js

```
const list = document.querySelectorAll("input[type=checkbox]");
for (const checkbox of list) {
  checkbox.checked = true;
}
```

Browsers also support the iterator method ([forEach()](/en-US/docs/Web/API/NodeList/forEach)) as well as [entries()](/en-US/docs/Web/API/NodeList/entries), [values()](/en-US/docs/Web/API/NodeList/values), and [keys()](/en-US/docs/Web/API/NodeList/keys).

## [Specifications](#specifications)

Specification
[DOM# interface-nodelist](https://dom.spec.whatwg.org/#interface-nodelist)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 10, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/NodeList/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/nodelist/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNodeList&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fnodelist%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNodeList%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fnodelist%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4df1c84eb714ea19f7e5ebaa740d0f00c73d8cb4%0A*+Document+last+modified%3A+2025-08-10T13%3A51%3A16.000Z%0A%0A%3C%2Fdetails%3E)
