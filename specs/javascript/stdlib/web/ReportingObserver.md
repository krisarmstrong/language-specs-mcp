# ReportingObserver

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReportingObserver&level=not)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `ReportingObserver` interface of the [Reporting API](/en-US/docs/Web/API/Reporting_API) allows you to collect and access reports.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[ReportingObserver()](/en-US/docs/Web/API/ReportingObserver/ReportingObserver)

Creates a new `ReportingObserver` object instance, which can be used to collect and access reports.

## [Instance properties](#instance_properties)

This interface has no properties defined on it.

## [Instance methods](#instance_methods)

[ReportingObserver.disconnect()](/en-US/docs/Web/API/ReportingObserver/disconnect)

Stops a reporting observer that had previously started observing from collecting reports.

[ReportingObserver.observe()](/en-US/docs/Web/API/ReportingObserver/observe)

Instructs a reporting observer to start collecting reports in its report queue.

[ReportingObserver.takeRecords()](/en-US/docs/Web/API/ReportingObserver/takeRecords)

Returns the current list of reports contained in the observer's report queue, and empties the queue.

## [Events](#events)

This interface has no events that fire on it.

## [Examples](#examples)

In our [deprecation_report.html](https://mdn.github.io/dom-examples/reporting-api/deprecation_report.html) example, we create a simple reporting observer to observe usage of deprecated features on our web page:

js

```
const options = {
  types: ["deprecation"],
  buffered: true,
};

const observer = new ReportingObserver((reports, observer) => {
  reportBtn.onclick = () => displayReports(reports);
}, options);
```

We then tell it to start observing reports using [ReportingObserver.observe()](/en-US/docs/Web/API/ReportingObserver/observe); this tells the observer to start collecting reports in its report queue, and runs the callback function specified inside the constructor:

js

```
observer.observe();
```

Later on in the example we deliberately use the deprecated version of [MediaDevices.getUserMedia()](/en-US/docs/Web/API/MediaDevices/getUserMedia):

js

```
if (navigator.mozGetUserMedia) {
  navigator.mozGetUserMedia(constraints, success, failure);
} else {
  navigator.getUserMedia(constraints, success, failure);
}
```

This causes a deprecation report to be generated; because of the event handler we set up inside the `ReportingObserver()` constructor, we can now click the button to display the report details.

Note: If you look at the [complete source code](https://github.com/mdn/dom-examples/blob/main/reporting-api/deprecation_report.html), you'll notice that we actually call the deprecated `getUserMedia()` method twice. After the first time we call [ReportingObserver.takeRecords()](/en-US/docs/Web/API/ReportingObserver/takeRecords), which returns the first generated report and empties the queue. Because of this, when the button is pressed only the second report is listed.

## [Specifications](#specifications)

Specification
[Reporting API# interface-reporting-observer](https://w3c.github.io/reporting/#interface-reporting-observer)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Reporting API](/en-US/docs/Web/API/Reporting_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/ReportingObserver/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/reportingobserver/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReportingObserver&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Freportingobserver%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReportingObserver%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Freportingobserver%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa7d66cf8b1251dc43f4b35c8060b95df69f58a0a%0A*+Document+last+modified%3A+2024-10-08T19%3A31%3A51.000Z%0A%0A%3C%2Fdetails%3E)
