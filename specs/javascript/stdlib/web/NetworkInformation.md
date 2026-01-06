# NetworkInformation

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNetworkInformation&level=not)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `NetworkInformation` interface of the [Network Information API](/en-US/docs/Web/API/Network_Information_API) provides information about the connection a device is using to communicate with the network and provides a means for scripts to be notified if the connection type changes. The `NetworkInformation` interface cannot be instantiated. It is instead accessed through the `connection` property of the [Navigator](/en-US/docs/Web/API/Navigator) interface or the [WorkerNavigator](/en-US/docs/Web/API/WorkerNavigator) interface.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface also inherits properties of its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[NetworkInformation.downlink](/en-US/docs/Web/API/NetworkInformation/downlink)Read only

Returns the effective bandwidth estimate in megabits per second, rounded to the nearest multiple of 25 kilobits per seconds.

[NetworkInformation.downlinkMax](/en-US/docs/Web/API/NetworkInformation/downlinkMax)Read onlyExperimental

Returns the maximum downlink speed, in megabits per second (Mbps), for the underlying connection technology.

[NetworkInformation.effectiveType](/en-US/docs/Web/API/NetworkInformation/effectiveType)Read only

Returns the effective type of the connection meaning one of 'slow-2g', '2g', '3g', or '4g'. This value is determined using a combination of recently observed round-trip time and downlink values.

[NetworkInformation.rtt](/en-US/docs/Web/API/NetworkInformation/rtt)Read only

Returns the estimated effective round-trip time of the current connection, rounded to the nearest multiple of 25 milliseconds.

[NetworkInformation.saveData](/en-US/docs/Web/API/NetworkInformation/saveData)Read only

Returns `true` if the user has set a reduced data usage option on the user agent.

[NetworkInformation.type](/en-US/docs/Web/API/NetworkInformation/type)Read onlyExperimental

Returns the type of connection a device is using to communicate with the network. It will be one of the following values:

- `bluetooth`
- `cellular`
- `ethernet`
- `none`
- `wifi`
- `wimax`
- `other`
- `unknown`

## [Instance methods](#instance_methods)

This interface also inherits methods of its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

## [Events](#events)

[change](/en-US/docs/Web/API/NetworkInformation/change_event)

The event that's fired when connection information changes.

## [Specifications](#specifications)

Specification
[Network Information API# networkinformation-interface](https://wicg.github.io/netinfo/#networkinformation-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Online and offline events](/en-US/docs/Web/API/Navigator/onLine)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/NetworkInformation/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/networkinformation/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNetworkInformation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fnetworkinformation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNetworkInformation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fnetworkinformation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
