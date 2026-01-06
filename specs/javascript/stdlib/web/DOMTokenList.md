# DOMTokenList

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMTokenList&level=high)

The `DOMTokenList` interface represents a set of space-separated tokens. Such a set is returned by [Element.classList](/en-US/docs/Web/API/Element/classList) or [HTMLLinkElement.relList](/en-US/docs/Web/API/HTMLLinkElement/relList), and many others.

A `DOMTokenList` is indexed beginning with `0` as with JavaScript [Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) objects. `DOMTokenList` is always case-sensitive.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Trimming of whitespace and removal of duplicates](#trimming_of_whitespace_and_removal_of_duplicates)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[DOMTokenList.length](/en-US/docs/Web/API/DOMTokenList/length)Read only

An `integer` representing the number of objects stored in the object.

[DOMTokenList.value](/en-US/docs/Web/API/DOMTokenList/value)

A [stringifier](/en-US/docs/Glossary/Stringifier) property that returns the value of the list as a string.

## [Instance methods](#instance_methods)

[DOMTokenList.item()](/en-US/docs/Web/API/DOMTokenList/item)

Returns the item in the list by its index, or `null` if the index is greater than or equal to the list's `length`.

[DOMTokenList.contains()](/en-US/docs/Web/API/DOMTokenList/contains)

Returns `true` if the list contains the given token, otherwise `false`.

[DOMTokenList.add()](/en-US/docs/Web/API/DOMTokenList/add)

Adds the specified tokens to the list.

[DOMTokenList.remove()](/en-US/docs/Web/API/DOMTokenList/remove)

Removes the specified tokens from the list.

[DOMTokenList.replace()](/en-US/docs/Web/API/DOMTokenList/replace)

Replaces the token with another one.

[DOMTokenList.supports()](/en-US/docs/Web/API/DOMTokenList/supports)

Returns `true` if the given token is in the associated attribute's supported tokens.

[DOMTokenList.toggle()](/en-US/docs/Web/API/DOMTokenList/toggle)

Removes the token from the list if it exists, or adds it to the list if it doesn't. Returns a boolean indicating whether the token is in the list after the operation.

[DOMTokenList.entries()](/en-US/docs/Web/API/DOMTokenList/entries)

Returns an [iterator](/en-US/docs/Web/JavaScript/Reference/Iteration_protocols), allowing you to go through all key/value pairs contained in this object.

[DOMTokenList.forEach()](/en-US/docs/Web/API/DOMTokenList/forEach)

Executes a provided callback function once for each `DOMTokenList` element.

[DOMTokenList.keys()](/en-US/docs/Web/API/DOMTokenList/keys)

Returns an [iterator](/en-US/docs/Web/JavaScript/Reference/Iteration_protocols), allowing you to go through all keys of the key/value pairs contained in this object.

[DOMTokenList.toString()](/en-US/docs/Web/API/DOMTokenList/toString)

Returns the [DOMTokenList.value](/en-US/docs/Web/API/DOMTokenList/value), the space-separated values of the list as a string.

[DOMTokenList.values()](/en-US/docs/Web/API/DOMTokenList/values)

Returns an [iterator](/en-US/docs/Web/JavaScript/Reference/Iteration_protocols), allowing you to go through all values of the key/value pairs contained in this object.

## [Examples](#examples)

In the following simple example, we retrieve the list of classes set on a [<p>](/en-US/docs/Web/HTML/Reference/Elements/p) element as a `DOMTokenList` using [Element.classList](/en-US/docs/Web/API/Element/classList), add a class using [DOMTokenList.add()](/en-US/docs/Web/API/DOMTokenList/add), and then update the [Node.textContent](/en-US/docs/Web/API/Node/textContent) of the `<p>` to equal the `DOMTokenList`.

First, the HTML:

html

```
<p class="a b c"></p>
```

Now the JavaScript:

js

```
let para = document.querySelector("p");
let classes = para.classList;
para.classList.add("d");
para.textContent = `paragraph classList is "${classes}"`;
```

The output looks like this:

## [Trimming of whitespace and removal of duplicates](#trimming_of_whitespace_and_removal_of_duplicates)

Methods that modify the `DOMTokenList` (such as [DOMTokenList.add()](/en-US/docs/Web/API/DOMTokenList/add)) automatically trim any excess [Whitespace](/en-US/docs/Glossary/Whitespace) and remove duplicate values from the list. For example:

html

```
<span class="    d   d e f"></span>
```

js

```
let span = document.querySelector("span");
let classes = span.classList;
span.classList.add("x");
span.textContent = `span classList is "${classes}"`;
```

The output looks like this:

## [Specifications](#specifications)

Specification
[DOM# interface-domtokenlist](https://dom.spec.whatwg.org/#interface-domtokenlist)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 21, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/DOMTokenList/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/domtokenlist/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMTokenList&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdomtokenlist%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMTokenList%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdomtokenlist%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F494edeb208c312a26b7f5efb0902799d89a2bb33%0A*+Document+last+modified%3A+2024-12-21T04%3A29%3A05.000Z%0A%0A%3C%2Fdetails%3E)
