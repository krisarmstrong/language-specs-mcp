# EventTarget

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEventTarget&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `EventTarget` interface is implemented by objects that can receive events and may have listeners for them. In other words, any target of events implements the three methods associated with this interface.

[Element](/en-US/docs/Web/API/Element), and its children, as well as [Document](/en-US/docs/Web/API/Document) and [Window](/en-US/docs/Web/API/Window), are the most common event targets, but other objects can be event targets, too. For example [IDBRequest](/en-US/docs/Web/API/IDBRequest), [AudioNode](/en-US/docs/Web/API/AudioNode), and [AudioContext](/en-US/docs/Web/API/AudioContext) are also event targets.

Many event targets (including elements, documents, and windows) also support [registering event handlers](/en-US/docs/Web/API/Document_Object_Model/Events#registering_event_handlers) via `onevent` properties and attributes.

## In this article

- [Constructor](#constructor)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[EventTarget()](/en-US/docs/Web/API/EventTarget/EventTarget)

Creates a new `EventTarget` object instance.

## [Instance methods](#instance_methods)

[EventTarget.addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener)

Registers an event handler of a specific event type on the `EventTarget`.

[EventTarget.removeEventListener()](/en-US/docs/Web/API/EventTarget/removeEventListener)

Removes an event listener from the `EventTarget`.

[EventTarget.dispatchEvent()](/en-US/docs/Web/API/EventTarget/dispatchEvent)

Dispatches an event to this `EventTarget`.

## [Specifications](#specifications)

Specification
[DOM# interface-eventtarget](https://dom.spec.whatwg.org/#interface-eventtarget)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Event index](/en-US/docs/Web/API/Document_Object_Model/Events#event_index)
- [Introduction to events](/en-US/docs/Learn_web_development/Core/Scripting/Events)
- [Event](/en-US/docs/Web/API/Event) interface

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 29, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/EventTarget/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/eventtarget/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEventTarget&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Feventtarget%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEventTarget%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Feventtarget%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff4c0e822eb6a1ea438c7342f43a3e4809adbd56a%0A*+Document+last+modified%3A+2025-07-29T01%3A48%3A17.000Z%0A%0A%3C%2Fdetails%3E)
