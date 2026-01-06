# PushSubscription

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2023⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPushSubscription&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `PushSubscription` interface of the [Push API](/en-US/docs/Web/API/Push_API) provides a subscription's URL endpoint along with the public key and secrets that should be used for encrypting push messages to this subscription. This information must be passed to the application server, using any desired application-specific method.

The interface also provides information about when the subscription will expire, and a method to unsubscribe from the subscription.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Description](#description)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[PushSubscription.endpoint](/en-US/docs/Web/API/PushSubscription/endpoint)Read only

A string containing the endpoint associated with the push subscription.

[PushSubscription.expirationTime](/en-US/docs/Web/API/PushSubscription/expirationTime)Read only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) of the subscription expiration time associated with the push subscription, if there is one, or null otherwise.

[PushSubscription.options](/en-US/docs/Web/API/PushSubscription/options)Read only

An object containing the options used to create the subscription.

[PushSubscription.subscriptionId](/en-US/docs/Web/API/PushSubscription/subscriptionId)DeprecatedRead onlyNon-standard

A string containing the subscription ID associated with the push subscription.

## [Instance methods](#instance_methods)

[PushSubscription.getKey()](/en-US/docs/Web/API/PushSubscription/getKey)

Returns an [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) which contains the client's public key, which can then be sent to a server and used in encrypting push message data.

[PushSubscription.toJSON()](/en-US/docs/Web/API/PushSubscription/toJSON)

Standard serializer — returns a JSON representation of the subscription properties.

[PushSubscription.unsubscribe()](/en-US/docs/Web/API/PushSubscription/unsubscribe)

Starts the asynchronous process of unsubscribing from the push service, returning a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to a boolean value when the current subscription is successfully unregistered.

## [Description](#description)

Each browser uses a particular push service. A service worker can use [PushManager.subscribe()](/en-US/docs/Web/API/PushManager/subscribe) to subscribe to the supported service, and use the returned `PushSubscription` to discover the endpoint where push messages should be sent.

The `PushSubscription` is also used to get the public key and secret that the application server must use to encrypt the messages that it sends to the push service. Note that the private keys used to decrypt push messages are not shared by the browser, and are used to decrypt messages before they are passed to the service worker. This ensures that push messages remain private as they pass through the push server infrastructure.

The service worker doesn't need to know anything about the endpoints or encryption, other than to pass the relevant information onto the application server. Any mechanism may be used to share the information with the application server.

## [Example](#example)

### [Sending coding information to the server](#sending_coding_information_to_the_server)

The [p256dh](/en-US/docs/Web/API/PushSubscription/getKey#p256dh) public key and [auth](/en-US/docs/Web/API/PushSubscription/getKey#auth) secret used for encrypting the message are provided to the service worker via its push subscription, using the [PushSubscription.getKey()](/en-US/docs/Web/API/PushSubscription/getKey) method, along with the target endpoint for sending push messages in [PushSubscription.endpoint](/en-US/docs/Web/API/PushSubscription/endpoint). The coding that should be used for encryption is provided by the [PushManager.supportedContentEncodings](/en-US/docs/Web/API/PushManager/supportedContentEncodings_static) static property.

This example shows how you might put the needed information from `PushSubscription` and `supportedContentEncodings` into a JSON object, serialize it using [JSON.stringify()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify), and post the result to the application server.

js

```
// Get a PushSubscription object
const pushSubscription =
  await serviceWorkerRegistration.pushManager.subscribe();

// Create an object containing the information needed by the app server
const subscriptionObject = {
  endpoint: pushSubscription.endpoint,
  keys: {
    p256dh: pushSubscription.getKey("p256dh"),
    auth: pushSubscription.getKey("auth"),
  },
  encoding: PushManager.supportedContentEncodings,
  /* other app-specific data, such as user identity */
};

// Stringify the object and post to the app server
fetch("https://example.com/push/", {
  method: "post",
  body: JSON.stringify(subscriptionObject),
});
```

### [Unsubscribing from a push manager](#unsubscribing_from_a_push_manager)

js

```
navigator.serviceWorker.ready
  .then((reg) => reg.pushManager.getSubscription())
  .then((subscription) => subscription.unsubscribe())
  .then((successful) => {
    // You've successfully unsubscribed
  })
  .catch((e) => {
    // Unsubscribing failed
  });
```

## [Specifications](#specifications)

Specification
[Push API# pushsubscription-interface](https://w3c.github.io/push-api/#pushsubscription-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Push API](/en-US/docs/Web/API/Push_API)
- [Service Worker API](/en-US/docs/Web/API/Service_Worker_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/PushSubscription/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/pushsubscription/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPushSubscription&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpushsubscription%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPushSubscription%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpushsubscription%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fcf79b60471db6f148fa4ba36f2cdeafbbeb70%0A*+Document+last+modified%3A+2025-10-30T21%3A49%3A49.000Z%0A%0A%3C%2Fdetails%3E)
