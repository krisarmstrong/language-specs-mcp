# PushMessageData

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2023⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPushMessageData&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is only available in [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

The `PushMessageData` interface of the [Push API](/en-US/docs/Web/API/Push_API) provides methods which let you retrieve the push data sent by a server in various formats.

Unlike the similar methods in the [Fetch API](/en-US/docs/Web/API/Fetch_API), which only allow the method to be invoked once, these methods can be called multiple times.

Messages received through the Push API are sent encrypted by push services and then automatically decrypted by browsers before they are made accessible through the methods of the `PushMessageData` interface.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

None.

## [Instance methods](#instance_methods)

[PushMessageData.arrayBuffer()](/en-US/docs/Web/API/PushMessageData/arrayBuffer)

Extracts the data as an [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) object.

[PushMessageData.blob()](/en-US/docs/Web/API/PushMessageData/blob)

Extracts the data as a [Blob](/en-US/docs/Web/API/Blob) object.

[PushMessageData.bytes()](/en-US/docs/Web/API/PushMessageData/bytes)

Extracts the data as a [Uint8Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) object.

[PushMessageData.json()](/en-US/docs/Web/API/PushMessageData/json)

Extracts the data as a [JSON](/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON) object.

[PushMessageData.text()](/en-US/docs/Web/API/PushMessageData/text)

Extracts the data as a plain text string.

## [Examples](#examples)

js

```
self.addEventListener("push", (event) => {
  const obj = event.data.json();

  if (obj.action === "subscribe" || obj.action === "unsubscribe") {
    fireNotification(obj, event);
    port.postMessage(obj);
  } else if (obj.action === "init" || obj.action === "chatMsg") {
    port.postMessage(obj);
  }
});
```

## [Specifications](#specifications)

Specification
[Push API# pushmessagedata-interface](https://w3c.github.io/push-api/#pushmessagedata-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 13, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/PushMessageData/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/pushmessagedata/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPushMessageData&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpushmessagedata%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPushMessageData%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpushmessagedata%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fde2ef1e9950eebbacdd55f072dfe03014d113bbd%0A*+Document+last+modified%3A+2024-07-13T01%3A34%3A51.000Z%0A%0A%3C%2Fdetails%3E)
