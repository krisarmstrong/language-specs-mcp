# TaskPriorityChangeEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTaskPriorityChangeEvent&level=not)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `TaskPriorityChangeEvent` is the interface for the [prioritychange](/en-US/docs/Web/API/TaskSignal/prioritychange_event) event.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[TaskPriorityChangeEvent()](/en-US/docs/Web/API/TaskPriorityChangeEvent/TaskPriorityChangeEvent)

Creates a new `TaskPriorityChangeEvent` object, setting an event name and previous priority.

## [Instance properties](#instance_properties)

This interface also inherits the properties of its parent, [Event](/en-US/docs/Web/API/Event).

[TaskPriorityChangeEvent.previousPriority](/en-US/docs/Web/API/TaskPriorityChangeEvent/previousPriority)Read only

Returns the [priority](/en-US/docs/Web/API/Prioritized_Task_Scheduling_API#task_priorities) of the corresponding [TaskSignal](/en-US/docs/Web/API/TaskSignal)before this [prioritychange](/en-US/docs/Web/API/TaskSignal/prioritychange_event) event.

## [Instance methods](#instance_methods)

This interface has no methods of its own, but inherits the methods of its parent, [Event](/en-US/docs/Web/API/Event).

## [Examples](#examples)

An object of this type is returned in the handler for a `prioritychange` event. The code below shows a handler in which the `newPriority` and `previousPriority` are logged.

js

```
// Listen for 'prioritychange' events on the controller's signal.
controller.signal.addEventListener("prioritychange", (event) => {
  const previousPriority = event.previousPriority;
  const newPriority = event.target.priority;
  console.log(`Priority changed from ${previousPriority} to ${newPriority}.`);
});
```

A more complete live example can be found in [prioritychange event > Examples](/en-US/docs/Web/API/TaskSignal/prioritychange_event).

## [Specifications](#specifications)

Specification
[Prioritized Task Scheduling# sec-task-priority-change-event](https://wicg.github.io/scheduling-apis/#sec-task-priority-change-event)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [prioritychange](/en-US/docs/Web/API/TaskSignal/prioritychange_event) event

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 25, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/TaskPriorityChangeEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/taskprioritychangeevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTaskPriorityChangeEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftaskprioritychangeevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTaskPriorityChangeEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftaskprioritychangeevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F33313b7c9e37253c0141e22558e298d08c060be5%0A*+Document+last+modified%3A+2024-09-25T06%3A09%3A20.000Z%0A%0A%3C%2Fdetails%3E)
