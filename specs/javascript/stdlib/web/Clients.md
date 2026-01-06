# Clients

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2018⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FClients&level=high)

Note: This feature is only available in [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

The `Clients` interface provides access to [Client](/en-US/docs/Web/API/Client) objects. Access it via [self](/en-US/docs/Web/API/ServiceWorkerGlobalScope)`.clients` within a [service worker](/en-US/docs/Web/API/Service_Worker_API).

## In this article

- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

[Clients.get()](/en-US/docs/Web/API/Clients/get)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) for a [Client](/en-US/docs/Web/API/Client) matching a given [id](/en-US/docs/Web/API/Client/id).

[Clients.matchAll()](/en-US/docs/Web/API/Clients/matchAll)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) for an array of [Client](/en-US/docs/Web/API/Client) objects. An options argument allows you to control the types of clients returned.

[Clients.openWindow()](/en-US/docs/Web/API/Clients/openWindow)

Opens a new browser window for a given URL and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) for the new [WindowClient](/en-US/docs/Web/API/WindowClient).

[Clients.claim()](/en-US/docs/Web/API/Clients/claim)

Allows an active service worker to set itself as the [controller](/en-US/docs/Web/API/ServiceWorkerContainer/controller) for all clients within its [scope](/en-US/docs/Web/API/ServiceWorkerRegistration/scope).

## [Examples](#examples)

The following example shows an existing chat window or creates a new one when the user clicks a notification.

js

```
addEventListener("notificationclick", (event) => {
  event.waitUntil(
    (async () => {
      const allClients = await clients.matchAll({
        includeUncontrolled: true,
      });

      let chatClient;

      // Let's see if we already have a chat window open:
      for (const client of allClients) {
        const url = new URL(client.url);

        if (url.pathname === "/chat/") {
          // Excellent, let's use it!
          client.focus();
          chatClient = client;
          break;
        }
      }

      // If we didn't find an existing chat window,
      // open a new one:
      chatClient ??= await clients.openWindow("/chat/");

      // Message the client:
      chatClient.postMessage("New chat messages!");
    })(),
  );
});
```

## [Specifications](#specifications)

Specification
[Service Workers Nightly# clients-interface](https://w3c.github.io/ServiceWorker/#clients-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using Service Workers](/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Clients/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/clients/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FClients&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fclients%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FClients%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fclients%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff2dc3d5367203c860cf1a71ce0e972f018523849%0A*+Document+last+modified%3A+2025-05-23T13%3A53%3A05.000Z%0A%0A%3C%2Fdetails%3E)
