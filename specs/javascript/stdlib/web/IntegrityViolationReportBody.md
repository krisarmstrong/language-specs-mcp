# IntegrityViolationReportBody

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `IntegrityViolationReportBody` dictionary is an extension of the [Reporting API](/en-US/docs/Web/API/Reporting_API) that represents the body of an [Integrity Policy](/en-US/docs/Web/HTTP/Reference/Headers/Integrity-Policy) violation report.

Integrity violation reports can be reported to [reporting server endpoints](/en-US/docs/Web/API/Reporting_API#reporting_server_endpoints) or via a [ReportingObserver](/en-US/docs/Web/API/ReportingObserver). They have a [type](/en-US/docs/Web/API/Report/type) of `"integrity-violation"`, a [url](/en-US/docs/Web/API/Report/url) indicating the document that contains the violation, and a [body](/en-US/docs/Web/API/Report/body) property that is an object matching this dictionary.

## In this article

- [Instance properties](#instance_properties)
- [Description](#description)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[blockedURL Read only](#blockedurl)

A string representing the URL of the resource blocked by an enforced integrity policy (or just reported for a [reportOnly](#reportonly) policy).

[documentURL Read only](#documenturl)

A string representing the URL of the document that is attempting to load the resource.

[destination Read only](#destination)

A string indicating the [Request.destination](/en-US/docs/Web/API/Request/destination#script) of the resource that was blocked. This can currently only be `"script"`.

[reportOnly Read only](#reportonly)

A boolean: `false` if the policy was enforced, and `true` if the violation was only reported.

## [Description](#description)

Integrity Policy violations are reported when a document attempts to load a resource that does not meet the [Subresource Integrity](/en-US/docs/Web/Security/Defenses/Subresource_Integrity) guarantees of a policy set using either the [Integrity-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Integrity-Policy) or [Integrity-Policy-Report-Only](/en-US/docs/Web/HTTP/Reference/Headers/Integrity-Policy-Report-Only) HTTP headers.

Specifically, a report is sent when a document attempts to load a [<script>](/en-US/docs/Web/HTML/Reference/Elements/script) resource (or other [request destination](/en-US/docs/Web/API/Request/destination) listed in the policy) that does not have valid integrity metadata, or to make a request in [no-cors](/en-US/docs/Web/API/Request/mode#no-cors) mode.

Violation reports may be obtained in a violating document using a [ReportingObserver](/en-US/docs/Web/API/ReportingObserver) callback (defined in the [ReportingObserver()](/en-US/docs/Web/API/ReportingObserver/ReportingObserver) constructor), filtering on report objects that have a `type` of `"integrity-violation"`.

Violation reports may also be sent as JSON objects in `POST` requests to the [endpoints](/en-US/docs/Web/HTTP/Reference/Headers/Integrity-Policy#endpoints) specified in the [Integrity-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Integrity-Policy) and [Integrity-Policy-Report-Only](/en-US/docs/Web/HTTP/Reference/Headers/Integrity-Policy-Report-Only) headers. The JSON report objects are a serialization of the reports returned in the [ReportingObserver](/en-US/docs/Web/API/ReportingObserver), and therefore also have a `type` of `"integrity-violation"`, and a `body` property that is a serialization of this object. Note that endpoint values set in the policy must map to identifiers set using the [Reporting-Endpoints](/en-US/docs/Web/HTTP/Reference/Headers/Reporting-Endpoints) header.

## [Examples](#examples)

### [Reporting using the API](#reporting_using_the_api)

This example shows how you can obtain Integrity Policy violation reports using a [ReportingObserver](/en-US/docs/Web/API/ReportingObserver).

First we set a page's integrity policy using the [Integrity-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Integrity-Policy). The policy below reports and blocks resource loading of any [<script>](/en-US/docs/Web/HTML/Reference/Elements/script) element or [HTMLScriptElement](/en-US/docs/Web/API/HTMLScriptElement) object that does not specify an `integrity` attribute, or when a script resource is requested in [no-cors](/en-US/docs/Web/API/Request/mode#no-cors) mode. Note that for this example we're only interested in reporting the violations using the API, so we're omitting the reporting endpoints:

http

```
Integrity-Policy: blocked-destinations=(script)
```

Next, we'll assume that our page includes the following element to load a script. Because we want to trigger a violation, it omits the `integrity` attribute used to check the script matches our expected version. We could also omit the `cross-origin` attribute so the request is sent in `no-cors` mode.

html

```
<script
  src="https://example.com/example-framework.js"
  crossorigin="anonymous"></script>
```

Note: A script that complies with the policy might look like this:

html

```
<script
  src="https://example.com/example-framework.js"
  integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8wC"
  crossorigin="anonymous"></script>
```

To observe violations within the page, we construct a new [ReportingObserver](/en-US/docs/Web/API/ReportingObserver) object to listen for reports with the type `"integrity-violation"`, passing a callback that will receive and log the reports. This code needs to be loaded before the script that causes the violation, in the same page:

js

```
const observer = new ReportingObserver(
  (reports, observer) => {
    reports.forEach((violation) => {
      console.log(violation);
      console.log(JSON.stringify(violation));
    });
  },
  {
    types: ["integrity-violation"],
    buffered: true,
  },
);

observer.observe();
```

Above, we log each violation report object and a JSON-string version of the object, which might look similar to the object below.

json

```
{
  "type": "integrity-violation",
  "url": "https://example.com",
  "body": {
    "documentURL": "https://example.com",
    "blockedURL": "https://example.com/example-framework.js",
    "destination": "script",
    "reportOnly": false
  }
}
```

### [Sending a report to a reporting endpoint](#sending_a_report_to_a_reporting_endpoint)

Configuring a web page to send an Integrity Policy violation report to a [reporting server endpoint](/en-US/docs/Web/API/Reporting_API#reporting_server_endpoints) is very similar to the previous example.

The main difference is that we need to specify one or more reporting endpoints where we want the reports to be sent, using the [Reporting-Endpoints](/en-US/docs/Web/HTTP/Reference/Headers/Reporting-Endpoints) response header, and then reference these in the `endpoints` field when setting the policy.

You can see this below, where we first define two endpoints — `integrity-endpoint` and `backup-integrity-endpoint` — and then reference them in our policy:

http

```
Reporting-Endpoints: integrity-endpoint=https://example.com/integrity, backup-integrity-endpoint=https://report-provider.example/integrity
Integrity-Policy: blocked-destinations=(script), endpoints=(integrity-endpoint, backup-integrity-endpoint)
```

We can trigger a violation by loading an external script from the page that does not meet the subresource integrity guidelines. Just to differ from the previous example, here we send the request in `no-cors` mode:

html

```
<script
  src="https://example.com/example-framework.js"
  integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8wC"></script>
```

The violation report will then be sent to the indicated endpoint as a JSON file. As you can see from the example below, the `type` is `"integrity-violation"` and the `body` property is a serialization of this `IntegrityViolationReportBody` object:

The report in this case would look the same as our JSON report in the previous example.

json

```
{
  "type": "integrity-violation",
  "url": "https://example.com",
  "body": {
    "documentURL": "https://example.com",
    "blockedURL": "https://example.com/example-framework.js",
    "destination": "script",
    "reportOnly": false
  }
}
```

## [Specifications](#specifications)

Specification
[Subresource Integrity# report-violations](https://w3c.github.io/webappsec-subresource-integrity/#report-violations)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [ReportingObserver](/en-US/docs/Web/API/ReportingObserver)
- [Integrity-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Integrity-Policy)
- [Integrity-Policy-Report-Only](/en-US/docs/Web/HTTP/Reference/Headers/Integrity-Policy-Report-Only)
- [Reporting-Endpoints](/en-US/docs/Web/HTTP/Reference/Headers/Reporting-Endpoints)
- [Integrity Policy](/en-US/docs/Web/Security/Defenses/Subresource_Integrity#integrity_policy) in [Subresource Integrity](/en-US/docs/Web/Security/Defenses/Subresource_Integrity#integrity_policy)
- [Reporting API](/en-US/docs/Web/API/Reporting_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/IntegrityViolationReportBody/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/integrityviolationreportbody/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIntegrityViolationReportBody&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fintegrityviolationreportbody%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIntegrityViolationReportBody%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fintegrityviolationreportbody%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca26363fcc6fc861103d40ac0205e5c5b79eb2fa%0A*+Document+last+modified%3A+2025-11-30T02%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
