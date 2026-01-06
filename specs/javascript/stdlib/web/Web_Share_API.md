# Web Share API

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The Web Share API provides a mechanism for sharing text, links, files, and other content to an arbitrary share target selected by the user.

Note: This API is not available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API) (not exposed via [WorkerNavigator](/en-US/docs/Web/API/WorkerNavigator)).

Note: This API should not be confused with the [Web Share Target API](/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/share_target), which allows a website to specify itself as a share target.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

The Web Share API allows a site to share text, links, files, and other content to user-selected share targets, utilizing the sharing mechanisms of the underlying operating system. These share targets typically include the system clipboard, email, contacts or messaging applications, and Bluetooth or Wi-Fi channels.

The API has just two methods. The [navigator.canShare()](/en-US/docs/Web/API/Navigator/canShare) method may be used to first validate whether some data is "shareable", prior to passing it to [navigator.share()](/en-US/docs/Web/API/Navigator/share) for sending.

The [navigator.share()](/en-US/docs/Web/API/Navigator/share) method invokes the native sharing mechanism of the underlying operating system and passes the specified data. It requires [transient activation](/en-US/docs/Glossary/Transient_activation), and hence must be triggered off a UI event like a button click. Further, the method must specify valid data that is supported for sharing by the native implementation.

The Web Share API is gated by the [web-share](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/web-share) Permissions Policy. If the policy is supported but has not been granted, both methods will indicate that the data is not shareable.

## [Interfaces](#interfaces)

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[navigator.canShare()](/en-US/docs/Web/API/Navigator/canShare)

Returns a boolean indicating whether the specified data is shareable.

[navigator.share()](/en-US/docs/Web/API/Navigator/share)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves if the passed data was successfully sent to a share target. This method must be called on a button click or other user activation (requires [transient activation](/en-US/docs/Glossary/Transient_activation)).

## [Example](#example)

The code below shows how you can share a link using [navigator.share()](/en-US/docs/Web/API/Navigator/share), triggered off a button click.

js

```
const shareData = {
  title: "MDN",
  text: "Learn web development on MDN!",
  url: "https://developer.mozilla.org",
};

const btn = document.querySelector("button");
const resultPara = document.querySelector(".result");

// Share must be triggered by "user activation"
btn.addEventListener("click", async () => {
  try {
    await navigator.share(shareData);
    resultPara.textContent = "MDN shared successfully";
  } catch (err) {
    resultPara.textContent = `Error: ${err}`;
  }
});
```

The above example is taken from our [Web share test](https://mdn.github.io/dom-examples/web-share/) ([see the source code](https://github.com/mdn/dom-examples/blob/main/web-share/index.html)). You can also see this as a live example in [navigator.share()](/en-US/docs/Web/API/Navigator/share).

## [Specifications](#specifications)

Specification[Web Share API](https://w3c.github.io/web-share/)

## [Browser compatibility](#browser_compatibility)

### [api.Navigator.share](#api.Navigator.share)

### [api.Navigator.canShare](#api.Navigator.canShare)

## [See also](#see_also)

- [Web Share Target API](/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/share_target)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Web_Share_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/web_share_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_Share_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fweb_share_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_Share_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fweb_share_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4d929bb0a021c7130d5a71a4bf505bcb8070378d%0A*+Document+last+modified%3A+2025-03-13T12%3A48%3A23.000Z%0A%0A%3C%2Fdetails%3E)
