# InterventionReportBody

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInterventionReportBody&level=not)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `InterventionReportBody` interface of the [Reporting API](/en-US/docs/Web/API/Reporting_API) represents the body of an intervention report.

An intervention report is generated when usage of a feature in a web document has been blocked by the browser for reasons such as security, performance, or user annoyance. So for example, a script was been stopped because it was significantly slowing down the browser, or the browser's autoplay policy blocked audio from playing without a user gesture to trigger it.

A deprecation report is generated when a deprecated feature (for example a deprecated API method) is used on a document being observed by a [ReportingObserver](/en-US/docs/Web/API/ReportingObserver). In addition to the support of this API, receiving useful intervention warnings relies on browser vendors adding these warnings for the relevant features.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

An instance of `InterventionReportBody` is returned as the value of [Report.body](/en-US/docs/Web/API/Report/body) when [Report.Type](/en-US/docs/Web/API/Report/type) is `intervention`. The interface has no constructor.

## [Instance properties](#instance_properties)

This interface also inherits properties from [ReportBody](/en-US/docs/Web/API/ReportBody).

[InterventionReportBody.id](/en-US/docs/Web/API/InterventionReportBody/id)ExperimentalRead only

A string representing the intervention that generated the report. This can be used to group reports.

[InterventionReportBody.message](/en-US/docs/Web/API/InterventionReportBody/message)ExperimentalRead only

A string containing a human-readable description of the intervention, including information such how the intervention could be avoided. This typically matches the message a browser will display in its DevTools console when an intervention is imposed, if one is available.

[InterventionReportBody.sourceFile](/en-US/docs/Web/API/InterventionReportBody/sourceFile)ExperimentalRead only

A string containing the path to the source file where the intervention occurred, if known, or `null` otherwise.

[InterventionReportBody.lineNumber](/en-US/docs/Web/API/InterventionReportBody/lineNumber)ExperimentalRead only

A string representing the line in the source file in which the intervention occurred, if known, or `null` otherwise.

[InterventionReportBody.columnNumber](/en-US/docs/Web/API/InterventionReportBody/columnNumber)ExperimentalRead only

A string representing the column in the source file in which the intervention occurred, if known, or `null` otherwise.

## [Instance methods](#instance_methods)

This interface also inherits methods from [ReportBody](/en-US/docs/Web/API/ReportBody).

[InterventionReportBody.toJSON()](/en-US/docs/Web/API/InterventionReportBody/toJSON)Experimental

A serializer which returns a JSON representation of the `InterventionReportBody` object.

## [Examples](#examples)

In this example we create a new [ReportingObserver](/en-US/docs/Web/API/ReportingObserver) to observe intervention reports, then print details of each property of the first report to the console.

js

```
const options = {
  types: ["intervention"],
  buffered: true,
};

const observer = new ReportingObserver((reports, observer) => {
  const firstReport = reports[0];
  console.log(firstReport.type); // intervention
  console.log(firstReport.body.id);
  console.log(firstReport.body.message);
  console.log(firstReport.body.sourceFile);
  console.log(firstReport.body.lineNumber);
  console.log(firstReport.body.columnNumber);
}, options);
```

## [Specifications](#specifications)

Specification
[Intervention Reporting# intervention-report](https://wicg.github.io/intervention-reporting/#intervention-report)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Reporting API](/en-US/docs/Web/API/Reporting_API)
- [The Reporting API](https://developer.chrome.com/docs/capabilities/web-apis/reporting-api)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/InterventionReportBody/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/interventionreportbody/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInterventionReportBody&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Finterventionreportbody%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInterventionReportBody%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Finterventionreportbody%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa7d66cf8b1251dc43f4b35c8060b95df69f58a0a%0A*+Document+last+modified%3A+2024-10-08T19%3A31%3A51.000Z%0A%0A%3C%2Fdetails%3E)
