# Storage

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStorage&level=high)

The `Storage` interface of the [Web Storage API](/en-US/docs/Web/API/Web_Storage_API) provides access to a particular domain's session or local storage. It allows, for example, the addition, modification, or deletion of stored data items.

To manipulate, for instance, the session storage for a domain, a call to [Window.sessionStorage](/en-US/docs/Web/API/Window/sessionStorage) is made; whereas for local storage the call is made to [Window.localStorage](/en-US/docs/Web/API/Window/localStorage).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[Storage.length](/en-US/docs/Web/API/Storage/length)Read only

Returns an integer representing the number of data items stored in the `Storage` object.

## [Instance methods](#instance_methods)

[Storage.key()](/en-US/docs/Web/API/Storage/key)

When passed a number `n`, this method will return the name of the nth key in the storage.

[Storage.getItem()](/en-US/docs/Web/API/Storage/getItem)

When passed a key name, will return that key's value.

[Storage.setItem()](/en-US/docs/Web/API/Storage/setItem)

When passed a key name and value, will add that key to the storage, or update that key's value if it already exists.

[Storage.removeItem()](/en-US/docs/Web/API/Storage/removeItem)

When passed a key name, will remove that key from the storage.

[Storage.clear()](/en-US/docs/Web/API/Storage/clear)

When invoked, will empty all keys out of the storage.

## [Examples](#examples)

Here we access a `Storage` object by calling `localStorage`. We first test whether the local storage contains data items using `!localStorage.getItem('bgcolor')`. If it does, we run a function called `setStyles()` that grabs the data items using [Storage.getItem()](/en-US/docs/Web/API/Storage/getItem) and uses those values to update page styles. If it doesn't, we run another function, `populateStorage()`, which uses [Storage.setItem()](/en-US/docs/Web/API/Storage/setItem) to set the item values, then runs `setStyles()`.

js

```
if (!localStorage.getItem("bgcolor")) {
  populateStorage();
} else {
  setStyles();
}

function populateStorage() {
  localStorage.setItem("bgcolor", document.getElementById("bgcolor").value);
  localStorage.setItem("font", document.getElementById("font").value);
  localStorage.setItem("image", document.getElementById("image").value);

  setStyles();
}

function setStyles() {
  const currentColor = localStorage.getItem("bgcolor");
  const currentFont = localStorage.getItem("font");
  const currentImage = localStorage.getItem("image");

  document.getElementById("bgcolor").value = currentColor;
  document.getElementById("font").value = currentFont;
  document.getElementById("image").value = currentImage;

  htmlElem.style.backgroundColor = `#${currentColor}`;
  pElem.style.fontFamily = currentFont;
  imgElem.setAttribute("src", currentImage);
}
```

Note: To see this running as a complete working example, see our [Web Storage Demo](https://mdn.github.io/dom-examples/web-storage/).

## [Specifications](#specifications)

Specification
[HTML# storage](https://html.spec.whatwg.org/multipage/webstorage.html#storage)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Storage API](/en-US/docs/Web/API/Web_Storage_API/Using_the_Web_Storage_API)
- [Window.localStorage](/en-US/docs/Web/API/Window/localStorage)
- [Window.sessionStorage](/en-US/docs/Web/API/Window/sessionStorage)
- [CacheStorage](/en-US/docs/Web/API/CacheStorage)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Storage/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/storage/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStorage&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fstorage%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStorage%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fstorage%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F22080a7cc403f7f45c8e85065b182c9f0d4d383c%0A*+Document+last+modified%3A+2024-07-26T15%3A28%3A56.000Z%0A%0A%3C%2Fdetails%3E)
