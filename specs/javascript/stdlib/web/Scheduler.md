# Scheduler

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScheduler&level=not)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `Scheduler` interface of the [Prioritized Task Scheduling API](/en-US/docs/Web/API/Prioritized_Task_Scheduling_API) provides methods for scheduling prioritized tasks.

A `Scheduler` can be accessed from the global object using [Window.scheduler](/en-US/docs/Web/API/Window/scheduler) or [WorkerGlobalScope.scheduler](/en-US/docs/Web/API/WorkerGlobalScope/scheduler) within a worker.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

None.

## [Instance methods](#instance_methods)

[Scheduler.postTask()](/en-US/docs/Web/API/Scheduler/postTask)

Adds a task to the scheduler as a callback, optionally specifying a priority, delay, and/or a signal for aborting the task.

[Scheduler.yield()](/en-US/docs/Web/API/Scheduler/yield)

Yields control of the main thread back to the browser, returning a promise that resolves to continue execution where it left off.

## [Examples](#examples)

If the feature is defined, an instance of this object is returned by the [globalThis](/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis) property in both workers and the main thread.

The code below shows a simple task that resolves with the text 'Task executing'. This text is logged on success. The code also shows a `catch` block, which would be required in more complex code to handle when a task is aborted or throws an error.

js

```
if ("scheduler" in this) {
  // Post task with default priority: 'user-visible' (no other options)
  // When the task resolves, Promise.then() logs the result.
  scheduler
    .postTask(() => "Task executing")
    .then((taskResult) => console.log(`${taskResult}`)) // Log result
    .catch((error) => console.error(`Error: ${error}`)); // Log errors
}
```

For more comprehensive example code see [Prioritized Task Scheduling API > Examples](/en-US/docs/Web/API/Prioritized_Task_Scheduling_API#examples).

## [Specifications](#specifications)

Specification
[Prioritized Task Scheduling# scheduler](https://wicg.github.io/scheduling-apis/#scheduler)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 28, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Scheduler/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/scheduler/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScheduler&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fscheduler%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScheduler%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fscheduler%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F66f1ba7918610f1145cde4a1d2d7ecb3baea5f65%0A*+Document+last+modified%3A+2025-07-28T03%3A22%3A33.000Z%0A%0A%3C%2Fdetails%3E)
