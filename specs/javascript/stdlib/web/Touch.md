# Touch

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTouch&level=not)

The `Touch` interface represents a single contact point on a touch-sensitive device. The contact point is commonly a finger or stylus and the device may be a touchscreen or trackpad.

The [Touch.radiusX](/en-US/docs/Web/API/Touch/radiusX), [Touch.radiusY](/en-US/docs/Web/API/Touch/radiusY), and [Touch.rotationAngle](/en-US/docs/Web/API/Touch/rotationAngle) describe the area of contact between the user and the screen, the touch area. This can be helpful when dealing with imprecise pointing devices such as fingers. These values are set to describe an ellipse that as closely as possible matches the entire area of contact (such as the user's fingertip).

Note: Many of the properties' values are hardware-dependent; for example, if the device doesn't have a way to detect the amount of pressure placed on the surface, the `force` value will always be 0. This may also be the case for `radiusX` and `radiusY`; if the hardware reports only a single point, these values will be 1.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[Touch()](/en-US/docs/Web/API/Touch/Touch)

Creates a Touch object.

## [Instance properties](#instance_properties)

This interface has no parent, and doesn't inherit or implement other properties.

### [Basic properties](#basic_properties)

[Touch.identifier](/en-US/docs/Web/API/Touch/identifier)Read only

Returns a unique identifier for this `Touch` object. A given touch point (say, by a finger) will have the same identifier for the duration of its movement around the surface. This lets you ensure that you're tracking the same touch all the time.

[Touch.screenX](/en-US/docs/Web/API/Touch/screenX)Read only

Returns the X coordinate of the touch point relative to the left edge of the screen.

[Touch.screenY](/en-US/docs/Web/API/Touch/screenY)Read only

Returns the Y coordinate of the touch point relative to the top edge of the screen.

[Touch.clientX](/en-US/docs/Web/API/Touch/clientX)Read only

Returns the X coordinate of the touch point relative to the left edge of the browser viewport, not including any scroll offset.

[Touch.clientY](/en-US/docs/Web/API/Touch/clientY)Read only

Returns the Y coordinate of the touch point relative to the top edge of the browser viewport, not including any scroll offset.

[Touch.pageX](/en-US/docs/Web/API/Touch/pageX)Read only

Returns the X coordinate of the touch point relative to the left edge of the document. Unlike `clientX`, this value includes the horizontal scroll offset, if any.

[Touch.pageY](/en-US/docs/Web/API/Touch/pageY)Read only

Returns the Y coordinate of the touch point relative to the top of the document. Unlike `clientY`, this value includes the vertical scroll offset, if any.

[Touch.target](/en-US/docs/Web/API/Touch/target)Read only

Returns the [Element](/en-US/docs/Web/API/Element) on which the touch point started when it was first placed on the surface, even if the touch point has since moved outside the interactive area of that element or even been removed from the document.

### [Touch area](#touch_area)

[Touch.radiusX](/en-US/docs/Web/API/Touch/radiusX)Read only

Returns the X radius of the ellipse that most closely circumscribes the area of contact with the screen. The value is in pixels of the same scale as `screenX`.

[Touch.radiusY](/en-US/docs/Web/API/Touch/radiusY)Read only

Returns the Y radius of the ellipse that most closely circumscribes the area of contact with the screen. The value is in pixels of the same scale as `screenY`.

[Touch.rotationAngle](/en-US/docs/Web/API/Touch/rotationAngle)Read only

Returns the angle (in degrees) that the ellipse described by radiusX and radiusY must be rotated, clockwise, to most accurately cover the area of contact between the user and the surface.

[Touch.force](/en-US/docs/Web/API/Touch/force)Read only

Returns the amount of pressure being applied to the surface by the user, as a `float` between `0.0` (no pressure) and `1.0` (maximum pressure).

## [Instance methods](#instance_methods)

This interface has no methods and no parent, and doesn't inherit or implement any methods.

## [Specifications](#specifications)

Specification
[Touch Events# touch-interface](https://w3c.github.io/touch-events/#touch-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Touch events](/en-US/docs/Web/API/Touch_events)
- [Document.createTouch()](/en-US/docs/Web/API/Document/createTouch)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Touch/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/touch/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTouch&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftouch%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTouch%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftouch%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F22080a7cc403f7f45c8e85065b182c9f0d4d383c%0A*+Document+last+modified%3A+2024-07-26T15%3A28%3A56.000Z%0A%0A%3C%2Fdetails%3E)
