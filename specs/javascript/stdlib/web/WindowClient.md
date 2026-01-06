# WindowClient

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2018⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWindowClient&level=high)

Note: This feature is only available in [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

The `WindowClient` interface of the [ServiceWorker API](/en-US/docs/Web/API/Service_Worker_API) represents the scope of a service worker client that is a document in a browsing context, controlled by an active worker. The service worker client independently selects and uses a service worker for its own loading and sub-resources.

## In this article

- [Instance methods](#instance_methods)
- [Instance properties](#instance_properties)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

`WindowClient` inherits methods from its parent interface, [Client](/en-US/docs/Web/API/Client).

[WindowClient.focus()](/en-US/docs/Web/API/WindowClient/focus)

Gives user input focus to the current client.

[WindowClient.navigate()](/en-US/docs/Web/API/WindowClient/navigate)

Loads a specified URL into a controlled client page.

## [Instance properties](#instance_properties)

`WindowClient` inherits properties from its parent interface, [Client](/en-US/docs/Web/API/Client).

[WindowClient.ancestorOrigins](/en-US/docs/Web/API/WindowClient/ancestorOrigins)Read onlyExperimental

An array of strings that indicates the ancestor origins of the browsing context represented by this `WindowClient` in reverse order.

[WindowClient.focused](/en-US/docs/Web/API/WindowClient/focused)Read only

A boolean that indicates whether the current client has focus.

[WindowClient.visibilityState](/en-US/docs/Web/API/WindowClient/visibilityState)Read only

Indicates the visibility of the current client. This value can be one of `"hidden"` or `"visible"`.

## [Example](#example)

js

```
self.addEventListener("notificationclick", (event) => {
  console.log("On notification click: ", event.notification.tag);
  event.notification.close();

  // This looks to see if the current is already open and
  // focuses if it is
  event.waitUntil(
    clients
      .matchAll({
        type: "window",
      })
      .then((clientList) => {
        for (const client of clientList) {
          if (client.url === "/" && "focus" in client) {
            client.focus();
            break;
          }
        }
        if (clients.openWindow) return clients.openWindow("/");
      }),
  );
});
```

## [Specifications](#specifications)

Specification
[Service Workers Nightly# windowclient](https://w3c.github.io/ServiceWorker/#windowclient)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using Service Workers](/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers)
- [Service workers basic code example](https://github.com/mdn/dom-examples/tree/main/service-worker/simple-service-worker)
- [Using web workers](/en-US/docs/Web/API/Web_Workers_API/Using_web_workers)
- [Channel Messaging API](/en-US/docs/Web/API/Channel_Messaging_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 9, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/WindowClient/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/windowclient/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWindowClient&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwindowclient%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWindowClient%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwindowclient%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4a1d696e78d9aa0a3ca571cbc0aab9ba90258235%0A*+Document+last+modified%3A+2025-09-09T12%3A39%3A48.000Z%0A%0A%3C%2Fdetails%3E)
