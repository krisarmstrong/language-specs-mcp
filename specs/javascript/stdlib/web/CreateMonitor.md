# CreateMonitor

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `CreateMonitor` interface provides information on the progress of an AI model download or some fine-tuning data for the model.

It can be used via:

- [Summarizer.create()](/en-US/docs/Web/API/Summarizer/create_static)
- [LanguageDetector.create()](/en-US/docs/Web/API/LanguageDetector/create_static)
- [Translator.create()](/en-US/docs/Web/API/Translator/create_static)

## In this article

- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Events](#events)

Inherits events from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[downloadprogress](/en-US/docs/Web/API/CreateMonitor/downloadprogress_event)Experimental

Fired when progress is made on the AI model download.

## [Examples](#examples)

### [Basic CreateMonitor usage](#basic_createmonitor_usage)

A `CreateMonitor` instance is used via the `monitor` property of an AI API's `create()` method ([Summarizer.create()](/en-US/docs/Web/API/Summarizer/create_static) is shown below). The `monitor` property takes a callback function as a value, the argument of which is the `CreateMonitor` instance. You can then monitor download progress via the instance's [downloadprogress](/en-US/docs/Web/API/CreateMonitor/downloadprogress_event) event.

js

```
const summarizer = await Summarizer.create({
  sharedContext:
    "A general summary to help a user decide if the text is worth reading",
  monitor(monitor) {
    monitor.addEventListener("downloadprogress", (e) => {
      console.log(`download progress: ${e.loaded}/${e.total}`);
    });
  },
});

const summary = await summarizer.summarize(myText);
```

## [Specifications](#specifications)

Specification
[Writing Assistance APIs# createmonitor](https://webmachinelearning.github.io/writing-assistance-apis/#createmonitor)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Summarizer API](/en-US/docs/Web/API/Summarizer_API/Using)
- [Web AI demos](https://chrome.dev/web-ai-demos/) on chrome.dev.

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CreateMonitor/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/createmonitor/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCreateMonitor&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcreatemonitor%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCreateMonitor%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcreatemonitor%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Faed56607fa2bc1f0678ea0846a1b62bd9571ff7b%0A*+Document+last+modified%3A+2025-07-13T23%3A54%3A28.000Z%0A%0A%3C%2Fdetails%3E)
