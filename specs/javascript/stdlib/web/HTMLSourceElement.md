# HTMLSourceElement

The `HTMLSourceElement` interface provides special properties (beyond the regular [HTMLElement](/en-US/docs/Web/API/HTMLElement) object interface it also has available to it by inheritance) for manipulating [<source>](/en-US/docs/Web/HTML/Reference/Elements/source) elements.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLSourceElement.height](/en-US/docs/Web/API/HTMLSourceElement/height)

A number that reflects the [height](/en-US/docs/Web/HTML/Reference/Elements/source#height) HTML attribute, indicating the height of the image resource in CSS pixels. The property has a meaning only if the parent of the current [<source>](/en-US/docs/Web/HTML/Reference/Elements/source) element is a [<picture>](/en-US/docs/Web/HTML/Reference/Elements/picture) element.

[HTMLSourceElement.media](/en-US/docs/Web/API/HTMLSourceElement/media)

A string reflecting the [media](/en-US/docs/Web/HTML/Reference/Elements/source#media) HTML attribute, containing the intended type of the media resource.

[HTMLSourceElement.sizes](/en-US/docs/Web/API/HTMLSourceElement/sizes)

A string representing image sizes between breakpoints

[HTMLSourceElement.src](/en-US/docs/Web/API/HTMLSourceElement/src)

A string reflecting the [src](/en-US/docs/Web/HTML/Reference/Elements/source#src) HTML attribute, containing the URL for the media resource. The [HTMLSourceElement.src](/en-US/docs/Web/API/HTMLSourceElement/src) property has a meaning only when the associated [<source>](/en-US/docs/Web/HTML/Reference/Elements/source) element is nested in a media element that is a [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) or an [<audio>](/en-US/docs/Web/HTML/Reference/Elements/audio) element. It has no meaning and is ignored when it is nested in a [<picture>](/en-US/docs/Web/HTML/Reference/Elements/picture) element.

Note: If the `src` property is updated (along with any siblings), the parent [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement)'s `load` method should be called when done, since `<source>` elements are not re-scanned automatically.

[HTMLSourceElement.srcset](/en-US/docs/Web/API/HTMLSourceElement/srcset)

A string reflecting the [srcset](/en-US/docs/Web/HTML/Reference/Elements/source#srcset) HTML attribute, containing a list of candidate images, separated by a comma (`',', U+002C COMMA`). A candidate image is a URL followed by a `'w'` with the width of the images, or an `'x'` followed by the pixel density.

[HTMLSourceElement.type](/en-US/docs/Web/API/HTMLSourceElement/type)

A string reflecting the [type](/en-US/docs/Web/HTML/Reference/Elements/source#type) HTML attribute, containing the type of the media resource.

[HTMLSourceElement.width](/en-US/docs/Web/API/HTMLSourceElement/width)

A number that reflects the [width](/en-US/docs/Web/HTML/Reference/Elements/source#width) HTML attribute, indicating the width of the image resource in CSS pixels. The property has a meaning only if the parent of the current [<source>](/en-US/docs/Web/HTML/Reference/Elements/source) element is a [<picture>](/en-US/docs/Web/HTML/Reference/Elements/picture) element.

## [Instance methods](#instance_methods)

No specific method; inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

## [Specifications](#specifications)

Specification
[HTML# htmlsourceelement](https://html.spec.whatwg.org/multipage/embedded-content.html#htmlsourceelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The HTML element implementing this interface: [<source>](/en-US/docs/Web/HTML/Reference/Elements/source).
- The HTML DOM APIs of the elements that can contain a [<source>](/en-US/docs/Web/HTML/Reference/Elements/source) element: [HTMLVideoElement](/en-US/docs/Web/API/HTMLVideoElement), [HTMLAudioElement](/en-US/docs/Web/API/HTMLAudioElement), [HTMLPictureElement](/en-US/docs/Web/API/HTMLPictureElement).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLSourceElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlsourceelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLSourceElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlsourceelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLSourceElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlsourceelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
