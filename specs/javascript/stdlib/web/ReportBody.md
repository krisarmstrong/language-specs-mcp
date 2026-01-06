# ReportBody

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `ReportBody` interface of the [Reporting API](/en-US/docs/Web/API/Reporting_API) represents the body of a report. Individual report types inherit from this interface, adding specific attributes relevant to the particular report.

The following interfaces inherit from `ReportBody`:

- [CSPViolationReportBody](/en-US/docs/Web/API/CSPViolationReportBody)
- [DeprecationReportBody](/en-US/docs/Web/API/DeprecationReportBody)
- [InterventionReportBody](/en-US/docs/Web/API/InterventionReportBody)

An instance of `ReportBody` is returned as the value of [Report.body](/en-US/docs/Web/API/Report/body). The interface has no constructor.

## In this article

- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance methods](#instance_methods)

[ReportBody.toJSON()](/en-US/docs/Web/API/ReportBody/toJSON)Deprecated

A serializer which returns a JSON representation of the `ReportBody` object.

## [Examples](#examples)

In this example we create a new [ReportingObserver](/en-US/docs/Web/API/ReportingObserver) to observe intervention reports. The [InterventionReportBody](/en-US/docs/Web/API/InterventionReportBody) interface inherits from `ReportBody`.

js

```
const options = {
  types: ["intervention"],
  buffered: true,
};

const observer = new ReportingObserver(([firstReport], observer) => {
  console.log(firstReport.type); // intervention
}, options);
```

## [Specifications](#specifications)

Specification
[Reporting API# reportbody](https://w3c.github.io/reporting/#reportbody)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ReportBody/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/reportbody/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReportBody&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Freportbody%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReportBody%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Freportbody%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0c81cbce5f95a0be935724bcd936f5592774eb3a%0A*+Document+last+modified%3A+2025-11-13T20%3A10%3A50.000Z%0A%0A%3C%2Fdetails%3E)
