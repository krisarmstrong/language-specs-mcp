# StorageEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStorageEvent&level=high)

The `StorageEvent` interface is implemented by the [storage](/en-US/docs/Web/API/Window/storage_event) event, which is sent to a window when a storage area the window has access to is changed within the context of another document.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[StorageEvent()](/en-US/docs/Web/API/StorageEvent/StorageEvent)

Returns a newly constructed `StorageEvent` object.

## [Instance properties](#instance_properties)

In addition to the properties listed below, this interface inherits the properties of its parent interface, [Event](/en-US/docs/Web/API/Event).

[key](/en-US/docs/Web/API/StorageEvent/key)Read only

Returns a string with the key for the storage item that was changed. The `key` attribute is `null` when the change is caused by the storage `clear()` method.

[newValue](/en-US/docs/Web/API/StorageEvent/newValue)Read only

Returns a string with the new value of the storage item that was changed. This value is `null` when the change has been invoked by storage `clear()` method, or the storage item has been removed from the storage.

[oldValue](/en-US/docs/Web/API/StorageEvent/oldValue)Read only

Returns a string with the original value of the storage item that was changed. This value is `null` when the storage item has been newly added and therefore doesn't have any previous value.

[storageArea](/en-US/docs/Web/API/StorageEvent/storageArea)Read only

Returns a [Storage](/en-US/docs/Web/API/Storage) object that represents the storage object that was affected.

[url](/en-US/docs/Web/API/StorageEvent/url)Read only

Returns string with the URL of the document whose storage changed.

## [Instance methods](#instance_methods)

In addition to the methods listed below, this interface inherits the methods of its parent interface, [Event](/en-US/docs/Web/API/Event).

[initStorageEvent()](/en-US/docs/Web/API/StorageEvent/initStorageEvent)Deprecated

Initializes the event in a manner analogous to the similarly-named [initEvent()](/en-US/docs/Web/API/Event/initEvent) method in the DOM Events interfaces. Use the constructor instead.

## [Specifications](#specifications)

Specification
[HTML# the-storageevent-interface](https://html.spec.whatwg.org/multipage/webstorage.html#the-storageevent-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Web Storage API](/en-US/docs/Web/API/Web_Storage_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 29, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/StorageEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/storageevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStorageEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fstorageevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStorageEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fstorageevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcec2a003b670c686f1df5dba16d3b02073ad6711%0A*+Document+last+modified%3A+2023-11-29T14%3A16%3A37.000Z%0A%0A%3C%2Fdetails%3E)
