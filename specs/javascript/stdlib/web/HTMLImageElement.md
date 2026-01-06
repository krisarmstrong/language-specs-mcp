# HTMLImageElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLImageElement&level=high)

The `HTMLImageElement` interface represents an HTML [<img>](/en-US/docs/Web/HTML/Reference/Elements/img) element, providing the properties and methods used to manipulate image elements.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Obsolete properties](#obsolete_properties)
- [Instance methods](#instance_methods)
- [Errors](#errors)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[Image()](/en-US/docs/Web/API/HTMLImageElement/Image)

The `Image()` constructor creates and returns a new `HTMLImageElement` object representing an HTML [<img>](/en-US/docs/Web/HTML/Reference/Elements/img) element which is not attached to any DOM tree. It accepts optional width and height parameters. When called without parameters, `new Image()` is equivalent to calling [document.createElement('img')](/en-US/docs/Web/API/Document/createElement).

## [Instance properties](#instance_properties)

Inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLImageElement.alt](/en-US/docs/Web/API/HTMLImageElement/alt)

A string that reflects the [alt](/en-US/docs/Web/HTML/Reference/Elements/img#alt) HTML attribute, thus indicating the alternate fallback content to be displayed if the image has not been loaded.

[HTMLImageElement.attributionSrc](/en-US/docs/Web/API/HTMLImageElement/attributionSrc)Secure contextDeprecated

Gets and sets the [attributionsrc](/en-US/docs/Web/HTML/Reference/Elements/img#attributionsrc) attribute on an [<img>](/en-US/docs/Web/HTML/Reference/Elements/img) element programmatically, reflecting the value of that attribute. `attributionsrc` specifies that you want the browser to send an [Attribution-Reporting-Eligible](/en-US/docs/Web/HTTP/Reference/Headers/Attribution-Reporting-Eligible) header along with the image request. On the server-side this is used to trigger sending an [Attribution-Reporting-Register-Source](/en-US/docs/Web/HTTP/Reference/Headers/Attribution-Reporting-Register-Source) or [Attribution-Reporting-Register-Trigger](/en-US/docs/Web/HTTP/Reference/Headers/Attribution-Reporting-Register-Trigger) header in the response, to register an image-based [attribution source](/en-US/docs/Web/API/Attribution_Reporting_API/Registering_sources#html-based_event_sources) or [attribution trigger](/en-US/docs/Web/API/Attribution_Reporting_API/Registering_triggers#html-based_attribution_triggers), respectively.

[HTMLImageElement.complete](/en-US/docs/Web/API/HTMLImageElement/complete)Read only

Returns a boolean value that is `true` if the browser has finished fetching the image, whether successful or not. That means this value is also `true` if the image has no [src](/en-US/docs/Web/API/HTMLImageElement/src) value indicating an image to load.

[HTMLImageElement.crossOrigin](/en-US/docs/Web/API/HTMLImageElement/crossOrigin)

A string specifying the CORS setting for this image element. See [CORS settings attributes](/en-US/docs/Web/HTML/Reference/Attributes/crossorigin) for further details. This may be `null` if CORS is not used.

[HTMLImageElement.currentSrc](/en-US/docs/Web/API/HTMLImageElement/currentSrc)Read only

Returns a string representing the URL from which the currently displayed image was loaded. This may change as the image is adjusted due to changing conditions, as directed by any [media queries](/en-US/docs/Web/CSS/Guides/Media_queries) which are in place.

[HTMLImageElement.decoding](/en-US/docs/Web/API/HTMLImageElement/decoding)

An optional string representing a hint given to the browser on how it should decode the image. If this value is provided, it must be one of the possible permitted values: `sync` to decode the image synchronously, `async` to decode it asynchronously, or `auto` to indicate no preference (which is the default). Read the [decoding](/en-US/docs/Web/API/HTMLImageElement/decoding) page for details on the implications of this property's values.

[HTMLImageElement.fetchPriority](/en-US/docs/Web/API/HTMLImageElement/fetchPriority)

An optional string representing a hint given to the browser on how it should prioritize fetching of the image relative to other images. If this value is provided, it must be one of the possible permitted values: `high` to fetch at a high priority, `low` to fetch at a low priority, or `auto` to indicate no preference (which is the default).

[HTMLImageElement.height](/en-US/docs/Web/API/HTMLImageElement/height)

An integer value that reflects the [height](/en-US/docs/Web/HTML/Reference/Elements/img#height) HTML attribute, indicating the rendered height of the image in CSS pixels.

[HTMLImageElement.isMap](/en-US/docs/Web/API/HTMLImageElement/isMap)

A boolean value that reflects the [ismap](/en-US/docs/Web/HTML/Reference/Elements/img#ismap) HTML attribute, indicating that the image is part of a server-side image map. This is different from a client-side image map, specified using an `<img>` element and a corresponding [<map>](/en-US/docs/Web/HTML/Reference/Elements/map) which contains [<area>](/en-US/docs/Web/HTML/Reference/Elements/area) elements indicating the clickable areas in the image. The image must be contained within an [<a>](/en-US/docs/Web/HTML/Reference/Elements/a) element; see the `ismap` page for details.

[HTMLImageElement.loading](/en-US/docs/Web/API/HTMLImageElement/loading)

A string providing a hint to the browser used to optimize loading the document by determining whether to load the image immediately (`eager`) or on an as-needed basis (`lazy`).

[HTMLImageElement.naturalHeight](/en-US/docs/Web/API/HTMLImageElement/naturalHeight)Read only

Returns an integer value representing the intrinsic height of the image in CSS pixels, if it is available; else, it shows `0`. This is the height the image would be if it were rendered at its natural full size.

[HTMLImageElement.naturalWidth](/en-US/docs/Web/API/HTMLImageElement/naturalWidth)Read only

An integer value representing the intrinsic width of the image in CSS pixels, if it is available; otherwise, it will show `0`. This is the width the image would be if it were rendered at its natural full size.

[HTMLImageElement.referrerPolicy](/en-US/docs/Web/API/HTMLImageElement/referrerPolicy)

A string that reflects the [referrerpolicy](/en-US/docs/Web/HTML/Reference/Elements/img#referrerpolicy) HTML attribute, which tells the [user agent](/en-US/docs/Glossary/User_agent) how to decide which referrer to use in order to fetch the image. Read this article for details on the possible values of this string.

[HTMLImageElement.sizes](/en-US/docs/Web/API/HTMLImageElement/sizes)

A string reflecting the [sizes](/en-US/docs/Web/HTML/Reference/Elements/img#sizes) HTML attribute. This string specifies a list of comma-separated conditional sizes for the image; that is, for a given viewport size, a particular image size is to be used. Read the documentation on the [sizes](/en-US/docs/Web/API/HTMLImageElement/sizes) page for details on the format of this string.

[HTMLImageElement.src](/en-US/docs/Web/API/HTMLImageElement/src)

A string that reflects the [src](/en-US/docs/Web/HTML/Reference/Elements/img#src) HTML attribute, which contains the full URL of the image including base URI. You can load a different image into the element by changing the URL in the `src` attribute.

[HTMLImageElement.srcset](/en-US/docs/Web/API/HTMLImageElement/srcset)

A string reflecting the [srcset](/en-US/docs/Web/HTML/Reference/Elements/img#srcset) HTML attribute. This specifies a list of candidate images, separated by commas (`',', U+002C COMMA`). Each candidate image is a URL followed by a space, followed by a specially-formatted string indicating the size of the image. The size may be specified either the width or a size multiple. Read the [srcset](/en-US/docs/Web/API/HTMLImageElement/srcset) page for specifics on the format of the size substring.

[HTMLImageElement.useMap](/en-US/docs/Web/API/HTMLImageElement/useMap)

A string reflecting the [usemap](/en-US/docs/Web/HTML/Reference/Elements/img#usemap) HTML attribute, containing the page-local URL of the [<map>](/en-US/docs/Web/HTML/Reference/Elements/map) element describing the image map to use. The page-local URL is a pound (hash) symbol (`#`) followed by the `name` of the `<map>` element, such as `#my-map-element`. The `<map>` in turn contains [<area>](/en-US/docs/Web/HTML/Reference/Elements/area) elements indicating the clickable areas in the image.

[HTMLImageElement.width](/en-US/docs/Web/API/HTMLImageElement/width)

An integer value that reflects the [width](/en-US/docs/Web/HTML/Reference/Elements/img#width) HTML attribute, indicating the rendered width of the image in CSS pixels.

[HTMLImageElement.x](/en-US/docs/Web/API/HTMLImageElement/x)Read only

An integer indicating the horizontal offset of the left border edge of the image's CSS layout box relative to the origin of the [<html>](/en-US/docs/Web/HTML/Reference/Elements/html) element's containing block.

[HTMLImageElement.y](/en-US/docs/Web/API/HTMLImageElement/y)Read only

The integer vertical offset of the top border edge of the image's CSS layout box relative to the origin of the [<html>](/en-US/docs/Web/HTML/Reference/Elements/html) element's containing block.

## [Obsolete properties](#obsolete_properties)

[HTMLImageElement.align](/en-US/docs/Web/API/HTMLImageElement/align)Deprecated

A string indicating the alignment of the image with respect to the surrounding context. The possible values are `"left"`, `"right"`, `"justify"`, and `"center"`. This is obsolete; you should instead use CSS (such as [text-align](/en-US/docs/Web/CSS/Reference/Properties/text-align), which works with images despite its name) to specify the alignment.

[HTMLImageElement.border](/en-US/docs/Web/API/HTMLImageElement/border)Deprecated

A string which defines the width of the border surrounding the image. This is deprecated; use the CSS [border](/en-US/docs/Web/CSS/Reference/Properties/border) property instead.

[HTMLImageElement.hspace](/en-US/docs/Web/API/HTMLImageElement/hspace)Deprecated

An integer value which specifies the amount of space (in pixels) to leave empty on the left and right sides of the image.

[HTMLImageElement.longDesc](/en-US/docs/Web/API/HTMLImageElement/longDesc)Deprecated

A string specifying the URL at which a long description of the image's contents may be found. This is used to turn the image into a hyperlink automatically. Modern HTML should instead place an `<img>` inside an [<a>](/en-US/docs/Web/HTML/Reference/Elements/a) element defining the hyperlink.

[HTMLImageElement.name](/en-US/docs/Web/API/HTMLImageElement/name)Deprecated

A string representing the name of the element.

[HTMLImageElement.vspace](/en-US/docs/Web/API/HTMLImageElement/vspace)Deprecated

An integer value specifying the amount of empty space, in pixels, to leave above and below the image.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLImageElement.decode()](/en-US/docs/Web/API/HTMLImageElement/decode)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when the image is decoded and it's safe to append the image to the DOM. This prevents rendering of the next frame from having to pause to decode the image, as would happen if an undecoded image were added to the DOM.

## [Errors](#errors)

If an error occurs while trying to load or render the image, and an `onerror` event handler has been configured to handle the [error](/en-US/docs/Web/API/HTMLElement/error_event) event, that event handler will get called. This can happen in a number of situations, including:

- The [src](/en-US/docs/Web/HTML/Reference/Elements/img#src) attribute is empty or `null`.
- The specified `src` URL is the same as the URL of the page the user is currently on.
- The specified image is corrupted in some way that prevents it from being loaded.
- The specified image's metadata is corrupted in such a way that it's impossible to retrieve its dimensions, and no dimensions were specified in the `<img>` element's attributes.
- The specified image is in a format not supported by the [user agent](/en-US/docs/Glossary/User_agent).

## [Examples](#examples)

### [Creating and inserting an image element](#creating_and_inserting_an_image_element)

js

```
const img1 = new Image(); // Image constructor
img1.src = "image1.png";
img1.alt = "alt";
document.body.appendChild(img1);

const img2 = document.createElement("img"); // Use DOM HTMLImageElement
img2.src = "image2.jpg";
img2.alt = "alt text";
document.body.appendChild(img2);

// using first image in the document
alert(document.images[0].src);
```

### [Getting width and height](#getting_width_and_height)

The following example shows the use of the `height` and `width` properties alongside images of varying dimensions:

html

```
<p>
  Image 1: no height, width, or style
  <img id="image1" src="https://www.mozilla.org/images/mozilla-banner.gif" />
</p>

<p>
  Image 2: height="50", width="500", but no style
  <img
    id="image2"
    src="https://www.mozilla.org/images/mozilla-banner.gif"
    height="50"
    width="500" />
</p>

<p>
  Image 3: no height, width, but style="height: 50px; width: 500px;"
  <img
    id="image3"
    src="https://www.mozilla.org/images/mozilla-banner.gif"
    style="height: 50px; width: 500px;" />
</p>

<div id="output"></div>
```

js

```
const arrImages = [
  document.getElementById("image1"),
  document.getElementById("image2"),
  document.getElementById("image3"),
];

const objOutput = document.getElementById("output");
let strHtml = "<ul>";

for (let i = 0; i < arrImages.length; i++) {
  const img = arrImages[i];
  strHtml += `<li>image${i + 1}: height=${img.height}, width=${img.width}, style.height=${img.style.height}, style.width=${img.style.width}</li>`;
}

strHtml += "</ul>";

objOutput.innerHTML = strHtml;
```

## [Specifications](#specifications)

Specification
[HTML# htmlimageelement](https://html.spec.whatwg.org/multipage/embedded-content.html#htmlimageelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The HTML element implementing this interface: [<img>](/en-US/docs/Web/HTML/Reference/Elements/img)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLImageElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlimageelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLImageElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlimageelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLImageElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlimageelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe936e7271df947f25184a5ba8a21445bbd4d056c%0A*+Document+last+modified%3A+2025-12-13T02%3A55%3A18.000Z%0A%0A%3C%2Fdetails%3E)
