# Report

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `Report` interface of the [Reporting API](/en-US/docs/Web/API/Reporting_API) represents a single report.

Reports can be accessed in a number of ways:

- Via the [ReportingObserver.takeRecords()](/en-US/docs/Web/API/ReportingObserver/takeRecords) method — this returns all reports in an observer's report queue, and then empties the queue.
- Via the `reports` parameter of the callback function passed into the [ReportingObserver()](/en-US/docs/Web/API/ReportingObserver/ReportingObserver) constructor upon creation of a new observer instance. This contains the list of reports currently contained in the observer's report queue.
- By sending requests to the endpoints defined via the [Reporting-Endpoints](/en-US/docs/Web/HTTP/Reference/Headers/Reporting-Endpoints) HTTP header.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[Report.body](/en-US/docs/Web/API/Report/body)Read only

The body of the report, which is a `ReportBody` object containing the detailed report information.

[Report.type](/en-US/docs/Web/API/Report/type)Read only

The type of report generated, e.g., `deprecation` or `intervention`.

[Report.url](/en-US/docs/Web/API/Report/url)Read only

The URL of the document that generated the report.

## [Instance methods](#instance_methods)

This interface has no methods defined on it.

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

Because of the event handler we set up inside the `ReportingObserver()` constructor, we can now click the button to display the report details.

The report details are displayed via the `displayReports()` function, which takes the observer callback's `reports` parameter as its parameter:

js

```
function displayReports(reports) {
  const outputElem = document.querySelector(".output");
  const list = document.createElement("ul");
  outputElem.appendChild(list);

  reports.forEach((report, i) => {
    let listItem = document.createElement("li");
    let textNode = document.createTextNode(
      `Report ${i + 1}, type: ${report.type}`,
    );
    listItem.appendChild(textNode);
    let innerList = document.createElement("ul");
    listItem.appendChild(innerList);
    list.appendChild(listItem);

    for (const key in report.body) {
      const innerListItem = document.createElement("li");
      const keyValue = report.body[key];
      innerListItem.textContent = `${key}: ${keyValue}`;
      innerList.appendChild(innerListItem);
    }
  });
}
```

The `reports` parameter contains an array of all the reports in the observer's report queue. We loop over each report using a [forEach()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach) loop, then iterate over each entry of in the report's body using a [for...in](/en-US/docs/Web/JavaScript/Reference/Statements/for...in) structure, displaying each key/value pair inside a list item.

## [Specifications](#specifications)

Specification
[Reporting API# dom-report](https://w3c.github.io/reporting/#dom-report)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Reporting API](/en-US/docs/Web/API/Reporting_API)
- [Report-To](/en-US/docs/Web/HTTP/Reference/Headers/Report-To) HTTP header

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Report/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/report/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReport&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Freport%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReport%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Freport%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F702cd9e4d2834e13aea345943efc8d0c03d92ec9%0A*+Document+last+modified%3A+2025-04-03T04%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
