# ScreenOrientation

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2023⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScreenOrientation&level=high)

The `ScreenOrientation` interface of the [Screen Orientation API](/en-US/docs/Web/API/Screen_Orientation_API) provides information about the current orientation of the document.

A `ScreenOrientation` instance object can be retrieved using the [screen.orientation](/en-US/docs/Web/API/Screen/orientation) property.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[ScreenOrientation.type](/en-US/docs/Web/API/ScreenOrientation/type)Read only

Returns the document's current orientation type, one of `portrait-primary`, `portrait-secondary`, `landscape-primary`, or `landscape-secondary`.

[ScreenOrientation.angle](/en-US/docs/Web/API/ScreenOrientation/angle)Read only

Returns the document's current orientation angle.

## [Instance methods](#instance_methods)

[ScreenOrientation.lock()](/en-US/docs/Web/API/ScreenOrientation/lock)

Locks the orientation of the containing document to its default orientation and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise).

[ScreenOrientation.unlock()](/en-US/docs/Web/API/ScreenOrientation/unlock)

Unlocks the orientation of the containing document from its default orientation.

## [Events](#events)

Listen to these events using `addEventListener()` or by assigning an event listener to the `oneventname` property of this interface.

[change](/en-US/docs/Web/API/ScreenOrientation/change_event)

Fired whenever the screen changes orientation.

## [Example](#example)

In the following example, we listen for an orientation [change](/en-US/docs/Web/API/ScreenOrientation/change_event) event and log the new [screen orientation type](/en-US/docs/Web/API/ScreenOrientation/type) and [angle](/en-US/docs/Web/API/ScreenOrientation/angle).

js

```
screen.orientation.addEventListener("change", (event) => {
  const type = event.target.type;
  const angle = event.target.angle;
  console.log(`ScreenOrientation change: ${type}, ${angle} degrees.`);
});
```

## [Specifications](#specifications)

Specification
[Screen Orientation# screenorientation-interface](https://w3c.github.io/screen-orientation/#screenorientation-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 9, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/ScreenOrientation/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/screenorientation/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScreenOrientation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fscreenorientation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScreenOrientation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fscreenorientation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85ceac6cab16f46ba87007f5d60a920b26d105b1%0A*+Document+last+modified%3A+2023-11-09T10%3A08%3A38.000Z%0A%0A%3C%2Fdetails%3E)
