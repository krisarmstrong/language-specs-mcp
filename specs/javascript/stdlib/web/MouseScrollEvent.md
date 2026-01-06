# MouseScrollEvent

Non-standard: This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

The `MouseScrollEvent` interface represents events that occur due to the user moving a mouse wheel or similar input device.

Warning: Do not use this interface for wheel events.

Like `MouseWheelEvent`, this interface is non-standard and deprecated. It was used in Gecko-based browsers only. Instead use the standard [WheelEvent](/en-US/docs/Web/API/WheelEvent).

## In this article

- [Method overview](#method_overview)
- [Attributes](#attributes)
- [Constants](#constants)
- [Instance methods](#instance_methods)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Method overview](#method_overview)

webidl

```
void initMouseScrollEvent(
  in DOMString typeArg,
  in boolean canBubbleArg,
  in boolean cancelableArg,
  in nsIDOMAbstractView viewArg,
  in long detailArg,
  in long screenXArg,
  in long screenYArg,
  in long clientXArg,
  in long clientYArg,
  in boolean ctrlKeyArg,
  in boolean altKeyArg,
  in boolean shiftKeyArg,
  in boolean metaKeyArg,
  in unsigned short buttonArg,
  in nsIDOMEventTarget relatedTargetArg,
  in long axis);
```

## [Attributes](#attributes)

AttributeTypeDescription`axis`Read only`long`Indicates scroll direction.

## [Constants](#constants)

### [Delta modes](#delta_modes)

ConstantValueDescription`HORIZONTAL_AXIS``0x01`The event is caused by horizontal wheel operation.`VERTICAL_AXIS``0x02`The event is caused by vertical wheel operation.

## [Instance methods](#instance_methods)

[initMouseScrollEvent()](#initmousescrollevent)

See `nsIDOMMouseScrollEvent::initMouseScrollEvent()`.

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- `DOMMouseScroll`
- `MozMousePixelScroll`
- Standardized mouse wheel event object: [WheelEvent](/en-US/docs/Web/API/WheelEvent)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/MouseScrollEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mousescrollevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMouseScrollEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmousescrollevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMouseScrollEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmousescrollevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcfb7587e3e3122630ad6cbd94d834ecadbe0a746%0A*+Document+last+modified%3A+2024-07-26T03%3A44%3A38.000Z%0A%0A%3C%2Fdetails%3E)
