# Launch Handler API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FLaunch_Handler_API&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The Launch Handler API allows developers to control how a [progressive web app](/en-US/docs/Web/Progressive_web_apps) (PWA) is launched — for example if it uses an existing window or creates a new one, and how the app's target launch URL is handled.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Extensions to other interfaces](#extensions_to_other_interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

You can specify launch behavior for your app by adding the [launch_handler](/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/launch_handler) field to your web app manifest file. This has one sub-field, `client_mode`, which contains a string value specifying how the app should be launched and navigated to. For example:

json

```
{
  "launch_handler": {
    "client_mode": "focus-existing"
  }
}
```

If not specified, the default `client_mode` value is `auto`. Available values are:

[focus-existing](#focus-existing)

The most recently interacted with browsing context in a web app window is chosen to handle the launch. This will populate the target launch URL in the [targetURL](/en-US/docs/Web/API/LaunchParams/targetURL) property of the [LaunchParams](/en-US/docs/Web/API/LaunchParams) object passed into the [window.launchQueue.setConsumer()](/en-US/docs/Web/API/LaunchQueue/setConsumer)'s callback function. As you'll see below, this allows you to set custom launch handing functionality for your app.

[navigate-existing](#navigate-existing)

The most recently interacted with browsing context in a web app window is navigated to the target launch URL. The target URL is still made available via [window.launchQueue.setConsumer()](/en-US/docs/Web/API/LaunchQueue/setConsumer) to allow additional custom launch navigation handling to be implemented.

[navigate-new](#navigate-new)

A new browsing context is created in a web app window to load the target launch URL. The target URL is still made available via [window.launchQueue.setConsumer()](/en-US/docs/Web/API/LaunchQueue/setConsumer) to allow additional custom launch navigation handling to be implemented.

[auto](#auto)

The user agent decides what works best for the platform. For example, `navigate-existing` might make more sense on mobile, where single app instances are commonplace, whereas `navigate-new` might make more sense in a desktop context. This is the default value used if provided values are invalid.

When `focus-existing` is used, you can include code inside the [window.launchQueue.setConsumer()](/en-US/docs/Web/API/LaunchQueue/setConsumer)'s callback function to provide custom handling of the [targetURL](/en-US/docs/Web/API/LaunchParams/targetURL)

js

```
window.launchQueue.setConsumer((launchParams) => {
  // Do something with launchParams.targetURL
});
```

Note:[LaunchParams](/en-US/docs/Web/API/LaunchParams) also has a [LaunchParams.files](/en-US/docs/Web/API/LaunchParams/files) property, which returns a read-only array of [FileSystemHandle](/en-US/docs/Web/API/FileSystemHandle) objects representing any files passed along with the launch navigation via the [POST](/en-US/docs/Web/HTTP/Reference/Methods/POST) method. This allows custom file handling to be implemented.

## [Interfaces](#interfaces)

[LaunchParams](/en-US/docs/Web/API/LaunchParams)

Used when implementing custom launch navigation handling in a PWA. When [window.launchQueue.setConsumer()](/en-US/docs/Web/API/LaunchQueue/setConsumer) is invoked to set up the launch navigation handling functionality, the callback function inside `setConsumer()` is passed a `LaunchParams` object instance.

[LaunchQueue](/en-US/docs/Web/API/LaunchQueue)

When a [progressive web app](/en-US/docs/Web/Progressive_web_apps) (PWA) is launched with a [launch_handler](/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/launch_handler)`client_mode` value of `focus-existing`, `navigate-new`, or `navigate-existing`, `LaunchQueue` provides access to functionality that allows custom launch navigation handling to be implemented in the PWA. This functionality is controlled by the properties of the [LaunchParams](/en-US/docs/Web/API/LaunchParams) object passed into the [setConsumer()](/en-US/docs/Web/API/LaunchQueue/setConsumer) callback function.

## [Extensions to other interfaces](#extensions_to_other_interfaces)

[window.launchQueue](/en-US/docs/Web/API/Window/launchQueue)

Provides access to the [LaunchQueue](/en-US/docs/Web/API/LaunchQueue) class, which allows custom launch navigation handling to be implemented in a [progressive web app](/en-US/docs/Web/Progressive_web_apps) (PWA), with the handling context signified by the [launch_handler](/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/launch_handler) manifest field `client_mode` value.

## [Examples](#examples)

js

```
if ("launchQueue" in window) {
  window.launchQueue.setConsumer((launchParams) => {
    if (launchParams.targetURL) {
      const params = new URL(launchParams.targetURL).searchParams;

      // Assuming a music player app that gets a track passed to it to be played
      const track = params.get("track");
      if (track) {
        audio.src = track;
        title.textContent = new URL(track).pathname.slice(1);
        audio.play();
      }
    }
  });
}
```

This code is included in the PWA, and executed when the app loads, upon launch. The [window.launchQueue.setConsumer()](/en-US/docs/Web/API/LaunchQueue/setConsumer)'s callback function extracts the search param out of the [LaunchParams.targetURL](/en-US/docs/Web/API/LaunchParams/targetURL) and, if it finds a `track` param, uses it to populate an [<audio>](/en-US/docs/Web/HTML/Reference/Elements/audio) element's `src` and play the audio track that this points to.

See the [Musicr 2.0](https://mdn.github.io/dom-examples/launch-handler/) demo app for full working code.

## [Specifications](#specifications)

Specification
[Web App Launch Handler API# launchqueue-interface](https://wicg.github.io/web-app-launch/#launchqueue-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Launch Handler API: Control how your app is launched](https://developer.chrome.com/docs/web-platform/launch-handler/)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 14, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Launch_Handler_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/launch_handler_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FLaunch_Handler_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Flaunch_handler_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FLaunch_Handler_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Flaunch_handler_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6d363614de8a40c33d1afe92e4e846b75beea986%0A*+Document+last+modified%3A+2025-09-14T23%3A40%3A51.000Z%0A%0A%3C%2Fdetails%3E)
