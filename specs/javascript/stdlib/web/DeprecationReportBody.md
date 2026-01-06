# DeprecationReportBody

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDeprecationReportBody&level=not)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `DeprecationReportBody` interface of the [Reporting API](/en-US/docs/Web/API/Reporting_API) represents the body of a deprecation report.

A deprecation report is generated when a deprecated feature (for example a deprecated API method) is used on a document being observed by a [ReportingObserver](/en-US/docs/Web/API/ReportingObserver). In addition to the support of this API, receiving useful deprecation warnings relies on browser vendors adding these warnings for deprecated features.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

An instance of `DeprecationReportBody` is returned as the value of [Report.body](/en-US/docs/Web/API/Report/body) when [Report.Type](/en-US/docs/Web/API/Report/type) is `deprecation`. The interface has no constructor.

## [Instance properties](#instance_properties)

This interface also inherits properties from [ReportBody](/en-US/docs/Web/API/ReportBody).

[DeprecationReportBody.id](/en-US/docs/Web/API/DeprecationReportBody/id)Experimental

A string representing the feature or API that is deprecated, for example `NavigatorGetUserMedia`. This can be used to group reports by deprecated feature.

[DeprecationReportBody.anticipatedRemoval](/en-US/docs/Web/API/DeprecationReportBody/anticipatedRemoval)Experimental

A [Date](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) object (rendered as a string) representing the date when the feature is expected to be removed from the current browser. If the date is not known, this property will return `null`.

[DeprecationReportBody.message](/en-US/docs/Web/API/DeprecationReportBody/message)Experimental

A string containing a human-readable description of the deprecation, including information such as what newer feature has superseded it, if any. This typically matches the message a browser will display in its DevTools console when a deprecated feature is used, if one is available.

[DeprecationReportBody.sourceFile](/en-US/docs/Web/API/DeprecationReportBody/sourceFile)Experimental

A string containing the path to the source file where the deprecated feature was used, if known, or `null` otherwise.

[DeprecationReportBody.lineNumber](/en-US/docs/Web/API/DeprecationReportBody/lineNumber)Experimental

A number representing the line in the source file in which the deprecated feature was used, if known, or `null` otherwise.

[DeprecationReportBody.columnNumber](/en-US/docs/Web/API/DeprecationReportBody/columnNumber)Experimental

A number representing the column in the source file in which the deprecated feature was used, if known, or `null` otherwise.

## [Instance methods](#instance_methods)

This interface also inherits methods from [ReportBody](/en-US/docs/Web/API/ReportBody).

[DeprecationReportBody.toJSON()](/en-US/docs/Web/API/DeprecationReportBody/toJSON)Experimental

A serializer which returns a JSON representation of the `InterventionReportBody` object.

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

Because of the event handler we set up inside the `ReportingObserver()` constructor, we can now click the button to display the report details.

The report details are displayed via the `displayReports()` function, which takes the observer callback's `reports` parameter as its parameter:

js

```
function displayReports(reports) {
  const outputElem = document.querySelector(".output");
  const list = document.createElement("ul");
  outputElem.appendChild(list);

  reports.forEach((report, i) => {
    const listItem = document.createElement("li");
    const textNode = document.createTextNode(
      `Report ${i + 1}, type: ${report.type}`,
    );
    listItem.appendChild(textNode);
    const innerList = document.createElement("ul");
    listItem.appendChild(innerList);
    list.appendChild(listItem);

    for (const [key, value] of Object.entries(report.body)) {
      const innerListItem = document.createElement("li");
      innerListItem.textContent = `${key}: ${value}`;
      innerList.appendChild(innerListItem);
    }
  });
}
```

The `reports` parameter contains an array of all the reports in the observer's report queue. We loop over each report using a basic [for](/en-US/docs/Web/JavaScript/Reference/Statements/for) loop, then iterate over each entry of in the report's body (a `DeprecationReportBody` instance) using a [for...in](/en-US/docs/Web/JavaScript/Reference/Statements/for...in) structure, displaying each key/value pair inside a list item.

## [Specifications](#specifications)

Specification
[Deprecation Reporting# deprecationreportbody](https://wicg.github.io/deprecation-reporting/#deprecationreportbody)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Reporting API](/en-US/docs/Web/API/Reporting_API)
- [The Reporting API](https://developer.chrome.com/docs/capabilities/web-apis/reporting-api)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/DeprecationReportBody/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/deprecationreportbody/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDeprecationReportBody&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdeprecationreportbody%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDeprecationReportBody%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdeprecationreportbody%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa7d66cf8b1251dc43f4b35c8060b95df69f58a0a%0A*+Document+last+modified%3A+2024-10-08T19%3A31%3A51.000Z%0A%0A%3C%2Fdetails%3E)
