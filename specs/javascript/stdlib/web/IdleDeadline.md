# IdleDeadline

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIdleDeadline&level=not)

The `IdleDeadline` interface is used as the data type of the input parameter to idle callbacks established by calling [Window.requestIdleCallback()](/en-US/docs/Web/API/Window/requestIdleCallback). It offers a method, [timeRemaining()](/en-US/docs/Web/API/IdleDeadline/timeRemaining), which lets you determine how much longer the user agent estimates it will remain idle and a property, [didTimeout](/en-US/docs/Web/API/IdleDeadline/didTimeout), which lets you determine if your callback is executing because its timeout duration expired.

To learn more about how request callbacks work, see [Collaborative Scheduling of Background Tasks](/en-US/docs/Web/API/Background_Tasks_API).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[IdleDeadline.didTimeout](/en-US/docs/Web/API/IdleDeadline/didTimeout)Read only

A Boolean whose value is `true` if the callback is being executed because the timeout specified when the idle callback was installed has expired.

## [Instance methods](#instance_methods)

[IdleDeadline.timeRemaining()](/en-US/docs/Web/API/IdleDeadline/timeRemaining)

Returns a [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp), which is a floating-point value providing an estimate of the number of milliseconds remaining in the current idle period. If the idle period is over, the value is 0. Your callback can call this repeatedly to see if there's enough time left to do more work before returning.

## [Example](#example)

See our [complete example](/en-US/docs/Web/API/Background_Tasks_API#example) in the article [Cooperative Scheduling of Background Tasks API](/en-US/docs/Web/API/Background_Tasks_API).

## [Specifications](#specifications)

Specification
[requestIdleCallback()# the-idledeadline-interface](https://w3c.github.io/requestidlecallback/#the-idledeadline-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Cooperative Scheduling of Background Tasks API](/en-US/docs/Web/API/Background_Tasks_API)
- [Window.requestIdleCallback()](/en-US/docs/Web/API/Window/requestIdleCallback)
- [Window.cancelIdleCallback()](/en-US/docs/Web/API/Window/cancelIdleCallback)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 20, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/IdleDeadline/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/idledeadline/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIdleDeadline&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fidledeadline%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIdleDeadline%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fidledeadline%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F387d0d4d8690c0d2c9db1b85eae28ffea0f3ac1f%0A*+Document+last+modified%3A+2023-02-20T04%3A32%3A55.000Z%0A%0A%3C%2Fdetails%3E)
