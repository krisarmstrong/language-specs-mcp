# LaunchParams

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FLaunchParams&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `LaunchParams` interface of the [Launch Handler API](/en-US/docs/Web/API/Launch_Handler_API) is used when implementing custom launch navigation handling in a PWA. When [window.launchQueue.setConsumer()](/en-US/docs/Web/API/LaunchQueue/setConsumer) is invoked to set up the launch navigation handling functionality, the callback function inside `setConsumer()` is passed a `LaunchParams` object instance.

Such custom navigation handling is initiated via [Window.launchQueue](/en-US/docs/Web/API/Window/launchQueue) when a PWA has been launched with a [launch_handler](/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/launch_handler)`client_mode` value of `focus-existing`, `navigate-new`, or `navigate-existing`.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[LaunchParams.files](/en-US/docs/Web/API/LaunchParams/files)Read onlyExperimental

Returns a read-only array of [FileSystemHandle](/en-US/docs/Web/API/FileSystemHandle) objects representing any files passed along with the launch navigation via the [POST](/en-US/docs/Web/HTTP/Reference/Methods/POST) method.

[LaunchParams.targetURL](/en-US/docs/Web/API/LaunchParams/targetURL)Read onlyExperimental

Returns the target URL of the launch.

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

## [Specifications](#specifications)

Specification
[Web App Launch Handler API# launchparams-interface](https://wicg.github.io/web-app-launch/#launchparams-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Launch Handler API: Control how your app is launched](https://developer.chrome.com/docs/web-platform/launch-handler/)
- [Window.launchQueue](/en-US/docs/Web/API/Window/launchQueue)
- [Musicr 2.0](https://mdn.github.io/dom-examples/launch-handler/) demo app

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/LaunchParams/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/launchparams/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FLaunchParams&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Flaunchparams%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FLaunchParams%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Flaunchparams%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F57b594763d8e34b8346ee7ea206bfc2e59238fb1%0A*+Document+last+modified%3A+2025-09-08T21%3A59%3A22.000Z%0A%0A%3C%2Fdetails%3E)
