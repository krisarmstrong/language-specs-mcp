# Compute Pressure API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCompute_Pressure_API&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API), except for [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The Compute Pressure API is a JavaScript API that enables you to observe the pressure of system resources such as the CPU.

## In this article

- [Use cases](#use_cases)
- [Concepts and usage](#concepts_and_usage)
- [Reference](#reference)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Use cases](#use_cases)

In real-time applications, such as video conferencing web apps, the Compute Pressure API lets you detect which pressure the system is currently facing. The system will handle any stress as well as it can, but a collaboration between system and app is useful to handle the pressure best. This API notifies you of high-level pressure state changes, so you can adjust your workloads and still offer a pleasant user experience. The signal is proactively delivered when the system pressure trend is either rising or easing to allow timely adaptation.

You can use these pressure change signals, for example, to reduce or increase the video quality or the number of video feeds shown simultaneously to avoid dropping video frames, audio cuts, or delaying other critical parts of the application. The quality of service of your web app can vary, also due to pressure from external factors and apps at unexpected times, but ideally that does not lead to a total system failure, input delay, or unresponsiveness. Instead, the set of enabled features and their quality level is balanced against the resource pressure of the end-user device. It is similar to network pressure in which case a streaming app adapts to the available bandwidth.

More use cases are:

- Web games, for which you could balance the quality and amount of 3D assets, change the framerate, resolution, depth of field etc., to ensure low latency and stable frame rate.
- User interfaces, for which you could render placeholders instead of real data while the system is under pressure, and render the real content once the pressure has eased.

## [Concepts and usage](#concepts_and_usage)

Fast and delightful web applications should balance workloads when the system's computing resources are used at (near) full capacity. The Compute Pressure API's goal is to prevent, rather than mitigate, bad user experience in the web app itself and also for the user's device to not become too hot, too loud, or to drain the battery at an unacceptable rate. Therefore, it is advised to prefer this API over feedback mechanisms or singular performance adjustments (for example, by lowering the frequency of [window.requestAnimationFrame](/en-US/docs/Web/API/Window/requestAnimationFrame)) where bad user experience might be mitigated, but not proactively avoided. For measuring and segmenting the performance of user sessions after the fact, the [PerformanceLongTaskTiming](/en-US/docs/Web/API/PerformanceLongTaskTiming) API is better suited to analyze tasks that occupy the UI thread for 50 milliseconds or more (see also [Performance API](/en-US/docs/Web/API/Performance_API) for additional performance measurement APIs).

### [Pressure source types](#pressure_source_types)

In your web app or website, different tasks are fighting for the processing time of different processing units (CPU, GPU, and other specialized processing units). The current version of the Compute Pressure API specification defines two main source types that can be queried to gather pressure information:

- `"thermals"` represents the global thermal state of the entire system.
- `"cpu"` represents the average pressure of the central processing unit (CPU) across all its cores. This state can be affected by other apps and sites than the observing site.

The list of supported sources varies per browser, operating system, and hardware, and is evolving. Use the static [PressureObserver.knownSources](/en-US/docs/Web/API/PressureObserver/knownSources_static) hint to see which source types are available to your browser. Note that availability can also vary by your operating system and your hardware. Call [observe()](/en-US/docs/Web/API/PressureObserver/observe) and check for a `NotSupportedError` to see if pressure observation is possible.

The Compute Pressure API is available in the following contexts:

- [Window](/en-US/docs/Web/API/Window) (main thread)
- [Worker](/en-US/docs/Web/API/Worker)
- [SharedWorker](/en-US/docs/Web/API/SharedWorker)
- [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe) (if a suitable [Permissions-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/compute-pressure) is provided)

### [Pressure states](#pressure_states)

The Compute Pressure API exposes high-level pressure states which abstract away complexities of system bottlenecks that cannot be adequately explained with low-level metrics such as processor clock speed and utilization. In fact, metrics for CPU utilization are often [misleading](https://www.brendangregg.com/blog/2017-05-09/cpu-utilization-is-wrong.html). Therefore, the Compute Pressure API uses human-readable pressure states with the following semantics (see also the [specification](https://w3c.github.io/compute-pressure/#pressure-states)):

- ⚪ `"nominal"`: The conditions of the target device are at an acceptable level with no noticeable adverse effects on the user.
- 🟢 `"fair"`: Target device pressure, temperature and/or energy usage are slightly elevated, potentially resulting in reduced battery-life, as well as fans (or systems with fans) becoming active and audible. Apart from that the target device is running flawlessly and can take on additional work.
- 🟡 `"serious"`: Target device pressure, temperature and/or energy usage is consistently highly elevated. The system may be throttling as a countermeasure to reduce thermals.
- 🔴 `"critical"`: The temperature of the target device or system is significantly elevated and it requires cooling down to avoid any potential issues.

The contributing factors (that is, the underlying system metrics) for the pressure states above are not defined by the specification and can vary depending on the underlying hardware and platform behavior. However, the specification requires that the change in contributing factors must be substantial to avoid flip-flopping between states. This means you can expect the API to not report different states overly often as they aren't responding to just one fluctuating system metric.

### [Security and privacy considerations](#security_and_privacy_considerations)

The Compute Pressure API is [policy-controlled](/en-US/docs/Web/HTTP/Guides/Permissions_Policy) by the `"compute-pressure"` directive. Its default allowlist is `'self'` which allows usage in same-origin nested frames but prevents third-party content from using the feature.

## [Reference](#reference)

### [Interfaces](#interfaces)

The following interfaces are present in the Compute Pressure API and the API surface is similar to other observers, such as [IntersectionObserver](/en-US/docs/Web/API/IntersectionObserver), [MutationObserver](/en-US/docs/Web/API/MutationObserver), or [PerformanceObserver](/en-US/docs/Web/API/PerformanceObserver).

[PressureObserver](/en-US/docs/Web/API/PressureObserver)Experimental

Notifies when the system's pressure changes for a specified number of sources (e.g., the CPU) at a predefined sample interval.

[PressureRecord](/en-US/docs/Web/API/PressureRecord)

Describes the pressure trend at a specific moment of transition.

### [Permissions-Policy directive](#permissions-policy_directive)

[Permissions-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy); the [compute-pressure](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/compute-pressure) directive

Controls access to the Compute Pressure API.

## [Examples](#examples)

### [Log current pressure](#log_current_pressure)

This example creates a [PressureObserver](/en-US/docs/Web/API/PressureObserver) and takes action whenever there is a pressure change. The sample interval is set to 1000ms, meaning that there will be updates at most every second.

js

```
function callback(records) {
  const lastRecord = records[records.length - 1];
  console.log(`Current pressure ${lastRecord.state}`);
  if (lastRecord.state === "critical") {
    // disable video feeds
  } else if (lastRecord.state === "serious") {
    // disable video filter effects
  } else {
    // enable all video feeds and filter effects
  }
}

try {
  const observer = new PressureObserver(callback);
  await observer.observe("cpu", {
    sampleInterval: 1000, // 1000ms
  });
} catch (error) {
  // report error setting up the observer
}
```

## [Specifications](#specifications)

Specification
[Compute Pressure Level 1# the-pressureobserver-object](https://w3c.github.io/compute-pressure/#the-pressureobserver-object)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Compute Pressure demo](https://w3c.github.io/compute-pressure/demo/), which uses Mandelbrot sets and workers to create artificial pressure for test purposes.

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 11, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Compute_Pressure_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/compute_pressure_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCompute_Pressure_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcompute_pressure_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCompute_Pressure_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcompute_pressure_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4f8c4b31478742a2a39fdb03993d08fc1c90bbea%0A*+Document+last+modified%3A+2025-07-11T02%3A19%3A30.000Z%0A%0A%3C%2Fdetails%3E)
