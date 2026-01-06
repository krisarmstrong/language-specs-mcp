# PictureInPictureWindow

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPictureInPictureWindow&level=not)

The `PictureInPictureWindow` interface represents an object able to programmatically obtain the `width` and `height` and `resize event` of the floating video window.

An object with this interface is obtained using the [HTMLVideoElement.requestPictureInPicture()](/en-US/docs/Web/API/HTMLVideoElement/requestPictureInPicture) promise return value.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

The `PictureInPictureWindow` interface doesn't inherit any properties.

[PictureInPictureWindow.width](/en-US/docs/Web/API/PictureInPictureWindow/width)Read only

Determines the width of the floating video window.

[PictureInPictureWindow.height](/en-US/docs/Web/API/PictureInPictureWindow/height)Read only

Determines the height of the floating video window.

## [Instance methods](#instance_methods)

The `PictureInPictureWindow` interface doesn't inherit any methods.

## [Events](#events)

The `PictureInPictureWindow` interface doesn't inherit any events.

[resize](/en-US/docs/Web/API/PictureInPictureWindow/resize_event)

Sent to a `PictureInPictureWindow` when the floating video window is resized.

## [Examples](#examples)

Given a `<button>` and a `<video>`, clicking the button will make the video enter the picture-in-picture mode; we then attach an event to print the floating video window dimensions to the console.

js

```
const button = document.querySelector("button");
const video = document.querySelector("video");

function printPipWindowDimensions(evt) {
  const pipWindow = evt.target;
  console.log(
    `The floating window dimensions are: ${pipWindow.width}x${pipWindow.height}px`,
  );
  // will print:
  // The floating window dimensions are: 640x360px
}

button.onclick = () => {
  video.requestPictureInPicture().then((pictureInPictureWindow) => {
    pictureInPictureWindow.onresize = printPipWindowDimensions;
  });
};
```

## [Specifications](#specifications)

Specification
[Picture-in-Picture# interface-picture-in-picture-window](https://w3c.github.io/picture-in-picture/#interface-picture-in-picture-window)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Picture-in-Picture API](/en-US/docs/Web/API/Picture-in-Picture_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/PictureInPictureWindow/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/pictureinpicturewindow/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPictureInPictureWindow&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpictureinpicturewindow%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPictureInPictureWindow%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpictureinpicturewindow%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F73b2b6ee411ac094b9fc57dafac6f9c232fc20d9%0A*+Document+last+modified%3A+2024-07-26T02%3A14%3A04.000Z%0A%0A%3C%2Fdetails%3E)
