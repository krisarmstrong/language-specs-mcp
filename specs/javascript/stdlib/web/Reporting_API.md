# Reporting API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReporting_API&level=not)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The Reporting API provides a generic reporting mechanism for web applications to use to make reports available based on various platform features (for example [Content Security Policy](/en-US/docs/Web/HTTP/Guides/CSP), [Permissions-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy), or feature deprecation reports) in a consistent manner.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Related HTTP Headers](#related_http_headers)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

There are several different features and problems on the web platform that generate information useful to web developers when they are trying to fix bugs or improve their websites in other ways. Such information can include:

- [Content Security Policy](/en-US/docs/Web/HTTP/Guides/CSP) violations.
- [Permissions-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy) violations.
- [Integrity-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Integrity-Policy) violations.
- Deprecated feature usage (when you are using something that will stop working soon in browsers).
- Occurrence of crashes.
- Occurrence of user-agent interventions (when the browser blocks something your code is trying to do because it is deemed a security risk for example, or just plain annoying, like auto-playing audio).

The purpose of the Reporting API is to provide a consistent reporting mechanism that can be used to make such information available to developers in the form of reports represented by JavaScript objects. There are a few ways to use it, which are detailed in the sections below.

### [Reporting server endpoints](#reporting_server_endpoints)

Each unique origin you want to get reports for can be given a series of "endpoints", which are named URLs (or groups of URLs) that can be sent reports from a user agent. A reporting server at these endpoints can collect the reports, and process and present them as needed by your application.

The [Reporting-Endpoints](/en-US/docs/Web/HTTP/Reference/Headers/Reporting-Endpoints) HTTP header is used to specify details about the different endpoints that a user-agent has available to it for delivering reports. The `report-to` directive can then be used on particular HTTP response headers to indicate the specific endpoint that will be used for the associated report. For example, the CSP [report-to](/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/report-to) directive can be used on the [Content-Security-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy) or [Content-Security-Policy-Report-Only](/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy-Report-Only) HTTP headers to specify the endpoint that CSP violation reports should be sent to.

Note: There is no absolute guarantee of report delivery — a report could still fail to be collected if a serious error occurs.

The reports themselves are sent to the target endpoint by the user agent in a `POST` operation with a [Content-Type](/en-US/docs/Web/HTTP/Reference/Headers/Content-Type) of `application/reports+json`. They are serializations of [Report](/en-US/docs/Web/API/Report) objects, where the `type` indicates the type of report, the `url` indicates the origin of the report, and the `body` contains a serialization of the API interface that corresponds to the report type. For example, CSP violation reports have a `type` of `csp-violation` and a `body` that is a serialization of a [CSPViolationReportBody](/en-US/docs/Web/API/CSPViolationReportBody) object.

Reports sent to endpoints can be retrieved independently of the running of the websites they relate to, which is useful — a crash for example could bring down a website and stop anything running, but a report could still be obtained to give the developer some clues as to why it happened.

### [Reporting observers](#reporting_observers)

Reports can also be obtained via [ReportingObserver](/en-US/docs/Web/API/ReportingObserver) objects created via JavaScript inside the website you are aiming to get reports on. This method is not as failsafe as sending reports to the server because any page crash could stop you retrieving the reports — but it is easier to set up, and more flexible.

A `ReportingObserver` object is created using the [ReportingObserver()](/en-US/docs/Web/API/ReportingObserver/ReportingObserver) constructor, which is passed two parameters:

- A callback function with two parameters — an array of the reports available in the observer's report queue and a copy of the same `ReportingObserver` object, which allows observation to be controlled directly from inside the callback. The callback runs when observation starts.
- An options dictionary that allows you to specify the type of reports to collect, and whether reports generated before the observer was created should be observable (`buffered: true`).

Methods are then available on the observer to start collecting reports ([ReportingObserver.observe()](/en-US/docs/Web/API/ReportingObserver/observe)), retrieve the reports currently in the report queue ([ReportingObserver.takeRecords()](/en-US/docs/Web/API/ReportingObserver/takeRecords)), and disconnect the observer so it can no longer collect records ([ReportingObserver.disconnect()](/en-US/docs/Web/API/ReportingObserver/disconnect)).

### [Report types](#report_types)

Reports sent to reporting endpoints and reporting observers are essentially the same: they have an origin `url`, a `type`, and a `body` that is an instance of the interface corresponding with that type. The only difference is that server reports are JSON serializations of the objects.

The mapping of report `type` to `body` is shown below.

`type``body`Items reported`deprecation`[DeprecationReportBody](/en-US/docs/Web/API/DeprecationReportBody)Deprecated features used by the site.`integrity-violation`[IntegrityViolationReportBody](/en-US/docs/Web/API/IntegrityViolationReportBody)Violations of the page's integrity policy.`intervention`[InterventionReportBody](/en-US/docs/Web/API/InterventionReportBody)Features blocked by the user agent, for example, if permissions are not granted.`csp-violation`[CSPViolationReportBody](/en-US/docs/Web/API/CSPViolationReportBody)Violations of the site's CSP policy.

### [Generating reports via WebDriver](#generating_reports_via_webdriver)

The Reporting API spec also defines a Generate Test Report [WebDriver](/en-US/docs/Web/WebDriver) extension, which allows you to simulate report generation during automation. Reports generated via WebDriver are observed by any registered `ReportObserver` objects present in the loaded website. This is not yet documented.

## [Interfaces](#interfaces)

[DeprecationReportBody](/en-US/docs/Web/API/DeprecationReportBody)

Contains details of deprecated web platform features that a website is using.

[InterventionReportBody](/en-US/docs/Web/API/InterventionReportBody)

Contains details of an intervention report, which is generated when a request made by the website has been denied by the browser; e.g., for security reasons.

[Report](/en-US/docs/Web/API/Report)

An object representing a single report.

[ReportingObserver](/en-US/docs/Web/API/ReportingObserver)

An object that can be used to collect and access reports as they are generated.

### [Related interfaces](#related_interfaces)

These interfaces are defined as part of the HTTP [Content Security Policy (CSP)](/en-US/docs/Web/HTTP/Guides/CSP) specifications:

[CSPViolationReportBody](/en-US/docs/Web/API/CSPViolationReportBody)

Contains details of a CSP violation.

[SecurityPolicyViolationEvent](/en-US/docs/Web/API/SecurityPolicyViolationEvent)

Represents the event object of a `securitypolicyviolation` event fired on an element, document, or worker when its CSP is violated.

This interface is defined as part of the [Subresource Integrity](/en-US/docs/Web/Security/Defenses/Subresource_Integrity) specification:

[IntegrityViolationReportBody](/en-US/docs/Web/API/IntegrityViolationReportBody)

Contains information about a resource that was blocked because it did not meet the Subresource Integrity guarantees required by its [Integrity-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Integrity-Policy), or that would be blocked for report-only policies set using [Integrity-Policy-Report-Only](/en-US/docs/Web/HTTP/Reference/Headers/Integrity-Policy-Report-Only).

## [Related HTTP Headers](#related_http_headers)

These HTTP response headers define the endpoints where reports are sent.

[Reporting-Endpoints](/en-US/docs/Web/HTTP/Reference/Headers/Reporting-Endpoints)

Sets the name and URL of reporting endpoints. These endpoints can be used in the `report-to` directive, which may be used with a number of HTTP headers including [Content-Security-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy) and or [Content-Security-Policy-Report-Only](/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy-Report-Only).

[Report-To](/en-US/docs/Web/HTTP/Reference/Headers/Report-To)Deprecated

No longer part of the Reporting API but still supported by some browsers. This sets the name and URL of reporting endpoint groups, which may be used with a number of HTTP headers especially for [Network Error Logging](/en-US/docs/Web/HTTP/Guides/Network_Error_Logging) that has not yet been updated to support `Reporting-Endpoints`. Other Reporting API reports should use `Reporting-Endpoints` instead for better future support.

Report endpoints can be set for the following reports using the [report-to](/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/report-to) directive on the corresponding headers:

[CSP violations](#csp_violations)

[Content-Security-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy) or [Content-Security-Policy-Report-Only](/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy-Report-Only).

Report endpoints can be set for the following reports using the [endpoints](/en-US/docs/Web/HTTP/Reference/Headers/Integrity-Policy#endpoints) field in a structured dictionary on the corresponding headers:

[Integrity-Policy violations](#integrity-policy_violations)

[Integrity-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Integrity-Policy) or [Integrity-Policy-Report-Only](/en-US/docs/Web/HTTP/Reference/Headers/Integrity-Policy-Report-Only).

## [Examples](#examples)

### [Reporting deprecated features](#reporting_deprecated_features)

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
[Reporting API# intro](https://w3c.github.io/reporting/#intro)
[Content Security Policy Level 3# cspviolationreportbody](https://w3c.github.io/webappsec-csp/#cspviolationreportbody)
[Deprecation Reporting# deprecationreportbody](https://wicg.github.io/deprecation-reporting/#deprecationreportbody)
[Intervention Reporting# intervention-report](https://wicg.github.io/intervention-reporting/#intervention-report)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Content Security Policy](/en-US/docs/Web/HTTP/Guides/CSP)
- [Permissions-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Reporting_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/reporting_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReporting_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Freporting_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReporting_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Freporting_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca26363fcc6fc861103d40ac0205e5c5b79eb2fa%0A*+Document+last+modified%3A+2025-11-30T02%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
