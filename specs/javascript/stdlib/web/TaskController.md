# TaskController

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTaskController&level=not)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `TaskController` interface of the [Prioritized Task Scheduling API](/en-US/docs/Web/API/Prioritized_Task_Scheduling_API) represents a controller object that can be used to both abort and change the [priority](/en-US/docs/Web/API/Prioritized_Task_Scheduling_API#task_priorities) of one or more prioritized tasks. If there is no need to change task priorities, then [AbortController](/en-US/docs/Web/API/AbortController) can be used instead.

A new `TaskController` instance is created using the [TaskController()](/en-US/docs/Web/API/TaskController/TaskController) constructor, optionally specifying a [priority](/en-US/docs/Web/API/Prioritized_Task_Scheduling_API#task_priorities) for its associated signal (a [TaskSignal](/en-US/docs/Web/API/TaskSignal)). If not specified, the signal will have a priority of ["user-visible"](/en-US/docs/Web/API/Prioritized_Task_Scheduling_API#user-visible) by default.

The controller's signal can be passed as an argument to the [Scheduler.postTask()](/en-US/docs/Web/API/Scheduler/postTask) method for one or more tasks. For [mutable tasks](/en-US/docs/Web/API/Prioritized_Task_Scheduling_API#mutable_and_immutable_task_priority) (only) the task is initialized with the signal priority, and can later be changed by calling [TaskController.setPriority()](/en-US/docs/Web/API/TaskController/setPriority). For immutable tasks, any priority initialized or set by the controller is ignored.

Tasks can be aborted by calling [abort()](/en-US/docs/Web/API/AbortController/abort) on the controller.

## In this article

- [Constructor](#constructor)
- [Instance methods](#instance_methods)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[TaskController()](/en-US/docs/Web/API/TaskController/TaskController)

Creates a new `TaskController` object, optionally specifying the priority of its associated [signal](#taskcontroller.signal).

## [Instance methods](#instance_methods)

This interface also inherits the methods of its parent, [AbortController](/en-US/docs/Web/API/AbortController).

[TaskController.setPriority()](/en-US/docs/Web/API/TaskController/setPriority)

Sets the priority of the controller's [signal](#taskcontroller.signal), and hence the priority of any tasks with which it is associated. This notifies observers of the priority change by dispatching a [prioritychange](/en-US/docs/Web/API/TaskSignal/prioritychange_event) event.

## [Instance properties](#instance_properties)

This interface also inherits the properties of its parent, [AbortController](/en-US/docs/Web/API/AbortController).

[TaskController.signal Read only](#taskcontroller.signal)

Returns a [TaskSignal](/en-US/docs/Web/API/TaskSignal) object instance. The signal is passed to tasks so that they can be aborted or re-prioritized by the controller. The property is inherited from [AbortController](/en-US/docs/Web/API/AbortController/signal).

## [Examples](#examples)

Note: Additional "live" examples can be found in: [Prioritized Task Scheduling API Examples](/en-US/docs/Web/API/Prioritized_Task_Scheduling_API#examples).

First we create a task controller, setting the priority of its associated signal to `user-blocking`.

js

```
// Create a TaskController, setting its signal priority to 'user-blocking'
const controller = new TaskController({ priority: "user-blocking" });
```

We then add an event listener for [prioritychange](/en-US/docs/Web/API/TaskSignal/prioritychange_event) events (here `addEventListener()` is called, but we could instead assign a handler to `TaskSignal.onprioritychange`). The handler uses [previousPolicy](/en-US/docs/Web/API/TaskPriorityChangeEvent/previousPriority) on the event to get the original priority and [TaskSignal.priority](/en-US/docs/Web/API/TaskSignal/priority) on the event target to get the new priority.

js

```
// Listen for 'prioritychange' events on the controller's signal.
controller.signal.addEventListener("prioritychange", (event) => {
  const previousPriority = event.previousPriority;
  const newPriority = event.target.priority;
  console.log(`Priority changed from ${previousPriority} to ${newPriority}.`);
});
```

We can also listen for [abort](/en-US/docs/Web/API/AbortSignal/abort_event) events as shown below. This same approach would be used if the controller was an `AbortController`.

js

```
controller.signal.addEventListener(
  "abort",
  (event) => {
    console.log("Task aborted");
  },
  { once: true },
);
```

Next we post the task, passing the controller signal in the optional argument. In this case the task is just an arrow function that resolves the promise by returning some text. We use `then` and `catch` to handle when the task resolves or is rejected, logging the return text or the error in each case. Note that in a later code block we abort the task, so only the `catch()` block will actually be run!

js

```
// Post task using the controller's signal.
// The signal priority sets the initial priority of the task
scheduler
  .postTask(() => "Task execute", { signal: controller.signal })
  .then((taskResult) => {
    console.log(`${taskResult}`);
  }) // Aborted (won't run)
  .catch((error) => {
    console.log(`Catch error: ${error}`);
  }); // Log error
```

We can use the controller to manage the task. Here we can change the priority using [TaskController.setPriority()](/en-US/docs/Web/API/TaskController/setPriority). This will trigger the associated `prioritychange` event.

js

```
// Change the priority to 'background' using the controller
controller.setPriority("background");
```

Finally, the task can be aborted by calling [abort()](/en-US/docs/Web/API/AbortController/abort) on the controller.

js

```
// Abort the task
controller.abort();
```

The console output of this example would be:

```
The priority changed from user-blocking to background.
Task aborted
Catch error: AbortError
```

## [Specifications](#specifications)

Specification
[Prioritized Task Scheduling# sec-task-controller](https://wicg.github.io/scheduling-apis/#sec-task-controller)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 12, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/TaskController/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/taskcontroller/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTaskController&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftaskcontroller%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTaskController%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftaskcontroller%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4854b2e695bd40ec2a124e15bf57b032f96e493d%0A*+Document+last+modified%3A+2025-12-12T22%3A10%3A35.000Z%0A%0A%3C%2Fdetails%3E)
