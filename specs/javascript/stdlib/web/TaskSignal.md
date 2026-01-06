# TaskSignal

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTaskSignal&level=not)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `TaskSignal` interface of the [Prioritized Task Scheduling API](/en-US/docs/Web/API/Prioritized_Task_Scheduling_API) represents a signal object that allows you to communicate with a prioritized task, and abort it or change the [priority](/en-US/docs/Web/API/Prioritized_Task_Scheduling_API#task_priorities) (if required) via a [TaskController](/en-US/docs/Web/API/TaskController) object.

An object of this type is created, and associated with, a [TaskController](/en-US/docs/Web/API/TaskController). The initial priority of the signal may be set by specifying it as an argument to the [TaskController()](/en-US/docs/Web/API/TaskController/TaskController) constructor (by default it is `"user-visible"`). The priority can be changed by calling [TaskController.setPriority()](/en-US/docs/Web/API/TaskController/setPriority) on the controller.

The signal may be passed as the `options.signal` argument in [Scheduler.postTask()](/en-US/docs/Web/API/Scheduler/postTask), after which its associated controller can be used to abort the task. If the [task priority is mutable](/en-US/docs/Web/API/Prioritized_Task_Scheduling_API#mutable_and_immutable_task_priority), the controller can also be used to change the task's priority. Abortable tasks that do not need the priority to change may instead specify an [AbortSignal](/en-US/docs/Web/API/AbortSignal) as the `options.signal` argument.

## In this article

- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

The `TaskSignal` interface also inherits properties from its parent interface, [AbortSignal](/en-US/docs/Web/API/AbortSignal).

[TaskSignal.priority](/en-US/docs/Web/API/TaskSignal/priority)Read only

Returns the priority of the signal.

## [Static methods](#static_methods)

The `TaskSignal` interface inherits methods from its parent interface, [AbortSignal](/en-US/docs/Web/API/AbortSignal).

[TaskSignal.any()](/en-US/docs/Web/API/TaskSignal/any_static)

Returns a `TaskSignal` that aborts when any of the given abort signals abort.

## [Instance methods](#instance_methods)

The `TaskSignal` interface inherits methods from its parent interface, [AbortSignal](/en-US/docs/Web/API/AbortSignal).

## [Events](#events)

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface.

[prioritychange](/en-US/docs/Web/API/TaskSignal/prioritychange_event)

Fired when the priority is changed. This is triggered by calling [TaskController.setPriority()](/en-US/docs/Web/API/TaskController/setPriority) on the associated controller.

## [Examples](#examples)

Examples for how the `TaskSignal` is created and used for prioritizing and aborting tasks can be found here:

- [Prioritized Task Scheduling API > Examples](/en-US/docs/Web/API/Prioritized_Task_Scheduling_API#examples)
- [TaskController > Examples](/en-US/docs/Web/API/TaskController#examples)
- [TaskSignal: prioritychange event > Examples](/en-US/docs/Web/API/TaskSignal/prioritychange_event#examples)

## [Specifications](#specifications)

Specification
[Prioritized Task Scheduling# tasksignal](https://wicg.github.io/scheduling-apis/#tasksignal)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/TaskSignal/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/tasksignal/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTaskSignal&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftasksignal%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTaskSignal%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftasksignal%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fcf79b60471db6f148fa4ba36f2cdeafbbeb70%0A*+Document+last+modified%3A+2025-10-30T21%3A49%3A49.000Z%0A%0A%3C%2Fdetails%3E)
