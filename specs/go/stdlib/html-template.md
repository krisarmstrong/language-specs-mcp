HTML Standardhttps://whatwg.org/

# HTML

Living Standard — Last Updated 17 December 2025[← 4.7 Edits](edits.html) — [Table of Contents](./) — [4.8.4 Images →](images.html)

1. 

  1. [4.8 Embedded content](embedded-content.html#embedded-content)

    1. [4.8.1 The picture element](embedded-content.html#the-picture-element)
    2. [4.8.2 The source element](embedded-content.html#the-source-element)
    3. [4.8.3 The img element](embedded-content.html#the-img-element)

### 4.8 Embedded content#embedded-content

#### 4.8.1 The `picture` element#the-picture-element

✔MDN

[Element/picture](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/picture)

Support in all current engines.Firefox38+Safari9.1+Chrome38+Opera?Edge79+Edge (Legacy)13+Internet ExplorerNoFirefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?✔MDN

[HTMLPictureElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLPictureElement)

Support in all current engines.Firefox38+Safari9.1+Chrome38+Opera?Edge79+Edge (Legacy)13+Internet ExplorerNoFirefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?[Categories](dom.html#concept-element-categories):[Flow content](dom.html#flow-content-2).[Phrasing content](dom.html#phrasing-content-2).[Embedded content](dom.html#embedded-content-category).[Palpable content](dom.html#palpable-content-2).[Contexts in which this element can be used](dom.html#concept-element-contexts):Where [embedded content](dom.html#embedded-content-category) is expected.[Content model](dom.html#concept-element-content-model):Zero or more [source](#the-source-element) elements, followed by one [img](#the-img-element) element, optionally intermixed with [script-supporting elements](dom.html#script-supporting-elements-2).[Tag omission in text/html](dom.html#concept-element-tag-omission):Neither tag is omissible.[Content attributes](dom.html#concept-element-attributes):[Global attributes](dom.html#global-attributes)[Accessibility considerations](dom.html#concept-element-accessibility-considerations):[For authors](https://w3c.github.io/html-aria/#el-picture).[For implementers](https://w3c.github.io/html-aam/#el-picture).[DOM interface](dom.html#concept-element-dom):

```
[Exposed=Window]
interface HTMLPictureElement : HTMLElementdom.html#htmlelement {
  [HTMLConstructordom.html#htmlconstructor] constructor();
};
```

The [picture](#the-picture-element) element is a container which provides multiple sources to its contained [img](#the-img-element) element to allow authors to declaratively control or give hints to the user agent about which image resource to use, based on the screen pixel density, [viewport](https://drafts.csswg.org/css2/#viewport) size, image format, and other factors. It [represents](dom.html#represents) its children.

The [picture](#the-picture-element) element is somewhat different from the similar-looking [video](media.html#the-video-element) and [audio](media.html#the-audio-element) elements. While all of them contain [source](#the-source-element) elements, the [source](#the-source-element) element's [src](#attr-source-src) attribute has no meaning when the element is nested within a [picture](#the-picture-element) element, and the resource selection algorithm is different. Also, the [picture](#the-picture-element) element itself does not display anything; it merely provides a context for its contained [img](#the-img-element) element that enables it to choose from multiple [URLs](https://url.spec.whatwg.org/#concept-url).

#### 4.8.2 The `source` element#the-source-element

✔MDN

[Element/source](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source)

Support in all current engines.Firefox3.5+Safari3.1+Chrome3+Opera?Edge79+Edge (Legacy)12+Internet Explorer9+Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?✔MDN

[HTMLSourceElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSourceElement)

Support in all current engines.Firefox3.5+Safari3.1+Chrome3+Opera12.1+Edge79+Edge (Legacy)12+Internet Explorer9+Firefox Android?Safari iOS?Chrome Android?WebView Android37+Samsung Internet?Opera Android12.1+[Categories](dom.html#concept-element-categories):None.[Contexts in which this element can be used](dom.html#concept-element-contexts):As a child of a [picture](#the-picture-element) element, before the [img](#the-img-element) element.As a child of a [media element](media.html#media-element), before any [flow content](dom.html#flow-content-2) or [track](media.html#the-track-element) elements.[Content model](dom.html#concept-element-content-model):[Nothing](dom.html#concept-content-nothing).[Tag omission in text/html](dom.html#concept-element-tag-omission):No [end tag](syntax.html#syntax-end-tag).[Content attributes](dom.html#concept-element-attributes):[Global attributes](dom.html#global-attributes)[type](#attr-source-type) — Type of embedded resource [media](#attr-source-media) — Applicable media [src](#attr-source-src) (in [audio](media.html#the-audio-element) or [video](media.html#the-video-element)) — Address of the resource [srcset](#attr-source-srcset) (in [picture](#the-picture-element)) — Images to use in different situations, e.g., high-resolution displays, small monitors, etc. [sizes](#attr-source-sizes) (in [picture](#the-picture-element)) — Image sizes for different page layouts [width](embedded-content-other.html#attr-dim-width) (in [picture](#the-picture-element)) — Horizontal dimension [height](embedded-content-other.html#attr-dim-height) (in [picture](#the-picture-element)) — Vertical dimension [Accessibility considerations](dom.html#concept-element-accessibility-considerations):[For authors](https://w3c.github.io/html-aria/#el-source).[For implementers](https://w3c.github.io/html-aam/#el-source).[DOM interface](dom.html#concept-element-dom):

```
[Exposed=Window]
interface HTMLSourceElement : HTMLElementdom.html#htmlelement {
  [HTMLConstructordom.html#htmlconstructor] constructor();

  [CEReactionscustom-elements.html#cereactions, ReflectURLcommon-dom-interfaces.html#xattr-reflecturl] attribute USVString src;
  [CEReactionscustom-elements.html#cereactions, Reflectcommon-dom-interfaces.html#xattr-reflect] attribute DOMString type;
  [CEReactionscustom-elements.html#cereactions, Reflectcommon-dom-interfaces.html#xattr-reflect] attribute USVString srcset;
  [CEReactionscustom-elements.html#cereactions, Reflectcommon-dom-interfaces.html#xattr-reflect] attribute DOMString sizes;
  [CEReactionscustom-elements.html#cereactions, Reflectcommon-dom-interfaces.html#xattr-reflect] attribute DOMString media;
  [CEReactionscustom-elements.html#cereactions, Reflectcommon-dom-interfaces.html#xattr-reflect] attribute unsigned long width;
  [CEReactionscustom-elements.html#cereactions, Reflectcommon-dom-interfaces.html#xattr-reflect] attribute unsigned long height;
};
```

The [source](#the-source-element) element allows authors to specify multiple alternative [source sets](images.html#source-set) for [img](#the-img-element) elements or multiple alternative [media resources](media.html#media-resource) for [media
  elements](media.html#media-element). It does not [represent](dom.html#represents) anything on its own.

The `type` attribute may be present. If present, the value must be a [valid MIME type string](https://mimesniff.spec.whatwg.org/#valid-mime-type).

The `media` attribute may also be present. If present, the value must contain a [valid media query
  list](common-microsyntaxes.html#valid-media-query-list). The user agent will skip to the next [source](#the-source-element) element if the value does not [match the environment](common-microsyntaxes.html#matches-the-environment).

The [media](#attr-source-media) attribute is only evaluated once during the [resource selection algorithm](media.html#concept-media-load-algorithm) for [media elements](media.html#media-element). In contrast, when using the [picture](#the-picture-element) element, the user agent will [react to
  changes in the environment](images.html#img-environment-changes).

The remainder of the requirements depend on whether the parent is a [picture](#the-picture-element) element or a [media element](media.html#media-element):

The [source](#the-source-element) element's parent is a [picture](#the-picture-element) element

The `srcset` attribute must be present, and is a [srcset attribute](images.html#srcset-attribute).

The [srcset](#attr-source-srcset) attribute contributes the [image sources](images.html#image-source) to the [source set](images.html#source-set), if the [source](#the-source-element) element is selected.

If the [srcset](#attr-source-srcset) attribute has any [image candidate strings](images.html#image-candidate-string) using a [width descriptor](images.html#width-descriptor), the [sizes](#attr-source-sizes) attribute may also be present. If, additionally, the following sibling [img](#the-img-element) element does not [allow
    auto-sizes](#allows-auto-sizes), the [sizes](#attr-source-sizes) attribute must be present. The `sizes` attribute is a [sizes attribute](images.html#sizes-attribute), which contributes the [source size](images.html#source-size-2) to the [source set](images.html#source-set), if the [source](#the-source-element) element is selected.

If the [img](#the-img-element) element [allows auto-sizes](#allows-auto-sizes), then the [sizes](#attr-source-sizes) attribute can be omitted on previous sibling [source](#the-source-element) elements. In such cases, it is equivalent to specifying [auto](images.html#valdef-sizes-auto).

The [source](#the-source-element) element supports [dimension attributes](embedded-content-other.html#dimension-attributes). The [img](#the-img-element) element can use the [width](embedded-content-other.html#attr-dim-width) and [height](embedded-content-other.html#attr-dim-height) attributes of a [source](#the-source-element) element, instead of those on the [img](#the-img-element) element itself, to determine its rendered dimensions and aspect-ratio, [as defined in the Rendering section](rendering.html#dimRendering).

The [type](#attr-source-type) attribute gives the type of the images in the [source set](images.html#source-set), to allow the user agent to skip to the next [source](#the-source-element) element if it does not support the given type.

If the [type](#attr-source-type) attribute is not specified, the user agent will not select a different [source](#the-source-element) element if it finds that it does not support the image format after fetching it.

When a [source](#the-source-element) element has a following sibling [source](#the-source-element) element or [img](#the-img-element) element with a [srcset](#attr-img-srcset) attribute specified, it must have at least one of the following:

- 

A [media](#attr-source-media) attribute specified with a value that, after [stripping leading and trailing
     ASCII whitespace](https://infra.spec.whatwg.org/#strip-leading-and-trailing-ascii-whitespace), is not the empty string and is not an [ASCII
     case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for the string "`all`".
- 

A [type](#attr-source-type) attribute specified.

The [src](#attr-source-src) attribute must not be present.

The [source](#the-source-element) element's parent is a [media element](media.html#media-element)

The `src` attribute gives the [URL](https://url.spec.whatwg.org/#concept-url) of the [media resource](media.html#media-resource). The value must be a [valid
    non-empty URL potentially surrounded by spaces](urls-and-fetching.html#valid-non-empty-url-potentially-surrounded-by-spaces). This attribute must be present.

The [type](#attr-source-type) attribute gives the type of the [media
    resource](media.html#media-resource), to help the user agent determine if it can play this [media
    resource](media.html#media-resource) before fetching it. The `codecs` parameter, which certain MIME types define, might be necessary to specify exactly how the resource is encoded. [[RFC6381]](references.html#refsRFC6381)

Dynamically modifying a [source](#the-source-element) element's [src](#attr-source-src) or [type](#attr-source-type) attribute when the element is already inserted in a [video](media.html#the-video-element) or [audio](media.html#the-audio-element) element will have no effect. To change what is playing, just use the [src](media.html#attr-media-src) attribute on the [media element](media.html#media-element) directly, possibly making use of the [canPlayType()](media.html#dom-navigator-canplaytype) method to pick from amongst available resources. Generally, manipulating [source](#the-source-element) elements manually after the document has been parsed is an unnecessarily complicated approach.

The following list shows some examples of how to use the `codecs=` MIME parameter in the [type](#attr-source-type) attribute.

H.264 Constrained baseline profile video (main and extended video compatible) level 3 and Low-Complexity AAC audio in MP4 container

```
<source src='video.mp4' type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"'>
```

H.264 Extended profile video (baseline-compatible) level 3 and Low-Complexity AAC audio in MP4 container

```
<source src='video.mp4' type='video/mp4; codecs="avc1.58A01E, mp4a.40.2"'>
```

H.264 Main profile video level 3 and Low-Complexity AAC audio in MP4 container

```
<source src='video.mp4' type='video/mp4; codecs="avc1.4D401E, mp4a.40.2"'>
```

H.264 'High' profile video (incompatible with main, baseline, or extended profiles) level 3 and Low-Complexity AAC audio in MP4 container

```
<source src='video.mp4' type='video/mp4; codecs="avc1.64001E, mp4a.40.2"'>
```

MPEG-4 Visual Simple Profile Level 0 video and Low-Complexity AAC audio in MP4 container

```
<source src='video.mp4' type='video/mp4; codecs="mp4v.20.8, mp4a.40.2"'>
```

MPEG-4 Advanced Simple Profile Level 0 video and Low-Complexity AAC audio in MP4 container

```
<source src='video.mp4' type='video/mp4; codecs="mp4v.20.240, mp4a.40.2"'>
```

MPEG-4 Visual Simple Profile Level 0 video and AMR audio in 3GPP container

```
<source src='video.3gp' type='video/3gpp; codecs="mp4v.20.8, samr"'>
```

Theora video and Vorbis audio in Ogg container

```
<source src='video.ogv' type='video/ogg; codecs="theora, vorbis"'>
```

Theora video and Speex audio in Ogg container

```
<source src='video.ogv' type='video/ogg; codecs="theora, speex"'>
```

Vorbis audio alone in Ogg container

```
<source src='audio.ogg' type='audio/ogg; codecs=vorbis'>
```

Speex audio alone in Ogg container

```
<source src='audio.spx' type='audio/ogg; codecs=speex'>
```

FLAC audio alone in Ogg container

```
<source src='audio.oga' type='audio/ogg; codecs=flac'>
```

Dirac video and Vorbis audio in Ogg container

```
<source src='video.ogv' type='video/ogg; codecs="dirac, vorbis"'>
```

The [srcset](#attr-source-srcset) and [sizes](#attr-source-sizes) attributes must not be present.

The [source](#the-source-element)[HTML element insertion steps](infrastructure.html#html-element-insertion-steps), given insertedNode, are:

1. 

Let parent be insertedNode's [parent](https://dom.spec.whatwg.org/#concept-tree-parent).
2. 

If parent is a [media element](media.html#media-element) that has no [src](media.html#attr-media-src) attribute and whose [networkState](media.html#dom-media-networkstate) has the value [NETWORK_EMPTY](media.html#dom-media-network_empty), then invoke that [media
   element](media.html#media-element)'s [resource selection
   algorithm](media.html#concept-media-load-algorithm).
3. 

If parent is a [picture](#the-picture-element) element, then [for each](https://infra.spec.whatwg.org/#list-iterate)child of parent's [children](https://dom.spec.whatwg.org/#concept-tree-child), if child is an [img](#the-img-element) element, then count this as a [relevant mutation](images.html#relevant-mutations) for child.

The [source](#the-source-element)[HTML element moving steps](infrastructure.html#html-element-moving-steps), given movedNode and oldParent, are:

1. 

If oldParent is a [picture](#the-picture-element) element, then [for each](https://infra.spec.whatwg.org/#list-iterate)child of oldParent's [children](https://dom.spec.whatwg.org/#concept-tree-child), if child is an [img](#the-img-element) element, then count this as a [relevant mutation](images.html#relevant-mutations) for child.

The [source](#the-source-element)[HTML element removing steps](infrastructure.html#html-element-removing-steps), given removedNode and oldParent, are:

1. 

If oldParent is a [picture](#the-picture-element) element, then [for each](https://infra.spec.whatwg.org/#list-iterate)child of oldParent's [children](https://dom.spec.whatwg.org/#concept-tree-child), if child is an [img](#the-img-element) element, then count this as a [relevant mutation](images.html#relevant-mutations) for child.

If the author isn't sure if user agents will all be able to render the media resources provided, the author can listen to the [error](indices.html#event-error) event on the last [source](#the-source-element) element and trigger fallback behavior:

```
<script>
 function fallback(video) {
   // replace <video> with its contents
   while (video.hasChildNodes()) {
     if (video.firstChild instanceof HTMLSourceElement)
       video.removeChild(video.firstChild);
     else
       video.parentNode.insertBefore(video.firstChild, video);
   }
   video.parentNode.removeChild(video);
 }
</script>
<video controls autoplay>
 <source src='video.mp4' type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"'>
 <source src='video.ogv' type='video/ogg; codecs="theora, vorbis"'
         onerror="fallback(parentNode)">
 ...
</video>
```

#### 4.8.3 The `img` element#the-img-element

✔MDN

[Element/img](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img)

Support in all current engines.Firefox1+Safari1+Chrome1+Opera?Edge79+Edge (Legacy)12+Internet ExplorerYesFirefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?✔MDN

[HTMLImageElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement)

Support in all current engines.Firefox1+Safari1+Chrome1+Opera8+Edge79+Edge (Legacy)12+Internet Explorer5.5+Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android10.1+

[HTMLImageElement/alt](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/alt)

Support in all current engines.Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+Internet Explorer5.5+Firefox Android?Safari iOS1+Chrome Android?WebView Android?Samsung Internet?Opera Android12.1+

[HTMLImageElement/srcset](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/srcset)

Support in all current engines.Firefox38+Safari8+Chrome34+Opera?Edge79+Edge (Legacy)12+Internet ExplorerNoFirefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[HTMLImageElement/sizes](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/sizes)

Support in all current engines.Firefox38+Safari9.1+Chrome38+Opera?Edge79+Edge (Legacy)13+Internet ExplorerNoFirefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[HTMLImageElement/useMap](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/useMap)

Support in all current engines.Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+Internet Explorer5.5+Firefox Android?Safari iOS1+Chrome Android?WebView Android?Samsung Internet?Opera Android12.1+

[HTMLImageElement/isMap](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/isMap)

Support in all current engines.Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+Internet Explorer5.5+Firefox Android?Safari iOS1+Chrome Android?WebView Android?Samsung Internet?Opera Android12.1+[Categories](dom.html#concept-element-categories):[Flow content](dom.html#flow-content-2).[Phrasing content](dom.html#phrasing-content-2).[Embedded content](dom.html#embedded-content-category).[Form-associated element](forms.html#form-associated-element).If the element has a [usemap](image-maps.html#attr-hyperlink-usemap) attribute: [Interactive content](dom.html#interactive-content-2).[Palpable content](dom.html#palpable-content-2).[Contexts in which this element can be used](dom.html#concept-element-contexts):Where [embedded content](dom.html#embedded-content-category) is expected.As a child of a [picture](#the-picture-element) element, after all [source](#the-source-element) elements.[Content model](dom.html#concept-element-content-model):[Nothing](dom.html#concept-content-nothing).[Tag omission in text/html](dom.html#concept-element-tag-omission):No [end tag](syntax.html#syntax-end-tag).[Content attributes](dom.html#concept-element-attributes):[Global attributes](dom.html#global-attributes)[alt](#attr-img-alt) — Replacement text for use when images are not available [src](#attr-img-src) — Address of the resource [srcset](#attr-img-srcset) — Images to use in different situations, e.g., high-resolution displays, small monitors, etc. [sizes](#attr-img-sizes) — Image sizes for different page layouts [crossorigin](#attr-img-crossorigin) — How the element handles crossorigin requests [usemap](image-maps.html#attr-hyperlink-usemap) — Name of [image map](image-maps.html#image-map) to use [ismap](#attr-img-ismap) — Whether the image is a server-side image map [width](embedded-content-other.html#attr-dim-width) — Horizontal dimension [height](embedded-content-other.html#attr-dim-height) — Vertical dimension [referrerpolicy](#attr-img-referrerpolicy) — [Referrer policy](https://w3c.github.io/webappsec-referrer-policy/#referrer-policy) for [fetches](https://fetch.spec.whatwg.org/#concept-fetch) initiated by the element [decoding](#attr-img-decoding) — Decoding hint to use when processing this image for presentation [loading](#attr-img-loading) — Used when determining loading deferral [fetchpriority](#attr-img-fetchpriority) — Sets the [priority](https://fetch.spec.whatwg.org/#request-priority) for [fetches](https://fetch.spec.whatwg.org/#concept-fetch) initiated by the element [Accessibility considerations](dom.html#concept-element-accessibility-considerations):If the element has a non-empty [alt](#attr-img-alt) attribute: [for authors](https://w3c.github.io/html-aria/#el-img); [for implementers](https://w3c.github.io/html-aam/#el-img).Otherwise: [for authors](https://w3c.github.io/html-aria/#el-img-empty-alt); [for implementers](https://w3c.github.io/html-aam/#el-img-empty-alt).[DOM interface](dom.html#concept-element-dom):

```
[Exposed=Window,
 LegacyFactoryFunctionhttps://webidl.spec.whatwg.org/#LegacyFactoryFunction=Image#dom-image(optional unsigned long width, optional unsigned long height)]
interface HTMLImageElement : HTMLElementdom.html#htmlelement {
  [HTMLConstructordom.html#htmlconstructor] constructor();

  [CEReactionscustom-elements.html#cereactions, Reflectcommon-dom-interfaces.html#xattr-reflect] attribute DOMString alt;
  [CEReactionscustom-elements.html#cereactions, ReflectURLcommon-dom-interfaces.html#xattr-reflecturl] attribute USVString src;
  [CEReactionscustom-elements.html#cereactions, Reflectcommon-dom-interfaces.html#xattr-reflect] attribute USVString srcset;
  [CEReactionscustom-elements.html#cereactions, Reflectcommon-dom-interfaces.html#xattr-reflect] attribute DOMString sizes;
  [CEReactionscustom-elements.html#cereactions] attribute DOMString? crossOrigin#dom-img-crossorigin;
  [CEReactionscustom-elements.html#cereactions, Reflectcommon-dom-interfaces.html#xattr-reflect] attribute DOMString useMap;
  [CEReactionscustom-elements.html#cereactions, Reflectcommon-dom-interfaces.html#xattr-reflect] attribute boolean isMap;
  [CEReactionscustom-elements.html#cereactions, ReflectSettercommon-dom-interfaces.html#xattr-reflectsetter] attribute unsigned long width#dom-img-width;
  [CEReactionscustom-elements.html#cereactions, ReflectSettercommon-dom-interfaces.html#xattr-reflectsetter] attribute unsigned long height#dom-img-height;
  readonly attribute unsigned long naturalWidth#dom-img-naturalwidth;
  readonly attribute unsigned long naturalHeight#dom-img-naturalheight;
  readonly attribute boolean complete#dom-img-complete;
  readonly attribute USVString currentSrc#dom-img-currentsrc;
  [CEReactionscustom-elements.html#cereactions] attribute DOMString referrerPolicy#dom-img-referrerpolicy;
  [CEReactionscustom-elements.html#cereactions] attribute DOMString decoding#dom-img-decoding;
  [CEReactionscustom-elements.html#cereactions] attribute DOMString loading#dom-img-loading;
  [CEReactionscustom-elements.html#cereactions] attribute DOMString fetchPriority#dom-img-fetchpriority;

  Promisehttps://webidl.spec.whatwg.org/#idl-promise<undefined> decode#dom-img-decode();

  // also has obsolete membersobsolete.html#HTMLImageElement-partial
};
```

An [img](#the-img-element) element represents an image.

An [img](#the-img-element) element has a dimension attribute source, initially set to the element itself.

✔MDN

[HTMLImageElement/src](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/src)

Support in all current engines.Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+Internet Explorer5.5+Firefox Android?Safari iOS1+Chrome Android?WebView Android?Samsung Internet?Opera Android12.1+

[Element/img#attr-srcset](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-srcset)

Support in all current engines.Firefox38+Safari8+Chrome34+Opera?Edge79+Edge (Legacy)≤18+Internet ExplorerNoFirefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The image given by the `src` and `srcset` attributes, and any previous sibling [source](#the-source-element) elements' [srcset](#attr-source-srcset) attributes if the parent is a [picture](#the-picture-element) element, is the embedded content; the value of the `alt` attribute provides equivalent content for those who cannot process images or who have image loading disabled (i.e., it is the [img](#the-img-element) element's [fallback content](dom.html#fallback-content)).

The requirements on the [alt](#attr-img-alt) attribute's value are described [in a separate section](images.html#alt).

At least one of the [src](#attr-img-src) and [srcset](#attr-img-srcset) attributes must be present.

If the [src](#attr-img-src) attribute is present, it must contain a [valid non-empty URL potentially surrounded by spaces](urls-and-fetching.html#valid-non-empty-url-potentially-surrounded-by-spaces) referencing a non-interactive, optionally animated, image resource that is neither paged nor scripted.

The requirements above imply that images can be static bitmaps (e.g. PNGs, GIFs, JPEGs), single-page vector documents (single-page PDFs, XML files with an SVG document element), animated bitmaps (APNGs, animated GIFs), animated vector graphics (XML files with an SVG [document element](https://dom.spec.whatwg.org/#document-element) that use declarative SMIL animation), and so forth. However, these definitions preclude SVG files with script, multipage PDF files, interactive MNG files, HTML documents, plain text documents, and the like. [[PNG]](references.html#refsPNG)[[GIF]](references.html#refsGIF)[[JPEG]](references.html#refsJPEG)[[PDF]](references.html#refsPDF)[[XML]](references.html#refsXML)[[APNG]](references.html#refsAPNG)[[SVG]](references.html#refsSVG)[[MNG]](references.html#refsMNG)

The [srcset](#attr-img-srcset) attribute is a [srcset
  attribute](images.html#srcset-attribute).

The [srcset](#attr-img-srcset) attribute and the [src](#attr-img-src) attribute (if [width
  descriptors](images.html#width-descriptor) are not used) contribute the [image sources](images.html#image-source) to the [source set](images.html#source-set) (if no [source](#the-source-element) element was selected).

If the [srcset](#attr-img-srcset) attribute is present and has any [image candidate strings](images.html#image-candidate-string) using a [width
  descriptor](images.html#width-descriptor), the [sizes](#attr-img-sizes) attribute must also be present. If the [srcset](#attr-img-srcset) attribute is not specified, and the [loading](#attr-img-loading) attribute is in the [Lazy](urls-and-fetching.html#attr-loading-lazy-state) state, the [sizes](#attr-img-sizes) attribute may be specified with the value "`auto`" ([ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive)). The `sizes` attribute is a [sizes attribute](images.html#sizes-attribute), which contributes the [source size](images.html#source-size-2) to the [source set](images.html#source-set) (if no [source](#the-source-element) element was selected).

An [img](#the-img-element) element allows auto-sizes if:

- its [loading](#attr-img-loading) attribute is in the [Lazy](urls-and-fetching.html#attr-loading-lazy-state) state, and
- its [sizes](#attr-img-sizes) attribute's value is "`auto`" ([ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive)), or starts with "`auto,`" ([ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive)).

✔MDN

[Attributes/crossorigin](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/crossorigin)

Support in all current engines.Firefox8+Safari6+Chrome13+Opera?Edge79+Edge (Legacy)12+Internet ExplorerYesFirefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The `crossorigin` attribute is a [CORS settings attribute](urls-and-fetching.html#cors-settings-attribute). Its purpose is to allow images from third-party sites that allow cross-origin access to be used with [canvas](canvas.html#the-canvas-element).

The `referrerpolicy` attribute is a [referrer
  policy attribute](urls-and-fetching.html#referrer-policy-attribute). Its purpose is to set the [referrer policy](https://w3c.github.io/webappsec-referrer-policy/#referrer-policy) used when [fetching](https://fetch.spec.whatwg.org/#concept-fetch) the image. [[REFERRERPOLICY]](references.html#refsREFERRERPOLICY)

The `decoding` attribute indicates the preferred method to [decode](images.html#img-decoding-process) this image. The attribute, if present, must be an [image decoding hint](images.html#image-decoding-hint). This attribute's [missing value default](common-microsyntaxes.html#missing-value-default) and [invalid value default](common-microsyntaxes.html#invalid-value-default) are both the [Auto](images.html#attr-img-decoding-auto-state) state.

MDN

[HTMLImageElement/fetchPriority](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/fetchPriority)FirefoxNoSafari🔰 preview+Chrome102+Opera?Edge102+Edge (Legacy)?Internet ExplorerNoFirefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The `fetchpriority` attribute is a [fetch
  priority attribute](urls-and-fetching.html#fetch-priority-attribute). Its purpose is to set the [priority](https://fetch.spec.whatwg.org/#request-priority) used when [fetching](https://fetch.spec.whatwg.org/#concept-fetch) the image.

The `loading` attribute is a [lazy
  loading attribute](urls-and-fetching.html#lazy-loading-attribute). Its purpose is to indicate the policy for loading images that are outside the viewport.

When the [loading](#attr-img-loading) attribute's state is changed to the [Eager](urls-and-fetching.html#attr-loading-eager-state) state, the user agent must run these steps:

1. 

Let resumptionSteps be the [img](#the-img-element) element's [lazy load
   resumption steps](urls-and-fetching.html#lazy-load-resumption-steps).
2. 

If resumptionSteps is null, then return.
3. 

Set the [img](#the-img-element)'s [lazy load resumption steps](urls-and-fetching.html#lazy-load-resumption-steps) to null.
4. 

Invoke resumptionSteps.

```
<img src="1.jpeg" alt="1">
<img src="2.jpeg" loading=eager alt="2">
<img src="3.jpeg" loading=lazy alt="3">
<div id=very-large></div> <!-- Everything after this div is below the viewport -->
<img src="4.jpeg" alt="4">
<img src="5.jpeg" loading=lazy alt="5">
```

In the example above, the images load as follows:

`1.jpeg`, `2.jpeg`, `4.jpeg`

The images load eagerly and delay the window's load event.`3.jpeg`

The image loads when layout is known, due to being in the viewport, however it does not delay the window's load event.`5.jpeg`

The image loads only once scrolled into the viewport, and does not delay the window's load event.

Developers are encouraged to specify a preferred aspect ratio via [width](embedded-content-other.html#attr-dim-width) and [height](embedded-content-other.html#attr-dim-height) attributes on lazy loaded images, even if CSS sets the image's width and height properties, to prevent the page layout from shifting around after the image loads.

The [img](#the-img-element)[HTML element insertion steps](infrastructure.html#html-element-insertion-steps), given insertedNode, are:

1. 

If insertedNode's parent is a [picture](#the-picture-element) element, then, count this as a [relevant mutation](images.html#relevant-mutations) for insertedNode.

The [img](#the-img-element)[HTML element moving steps](infrastructure.html#html-element-moving-steps), given movedNode and oldParent, are:

1. 

If oldParent is a [picture](#the-picture-element) element, then, count this as a [relevant mutation](images.html#relevant-mutations) for movedNode.

The [img](#the-img-element)[HTML element removing steps](infrastructure.html#html-element-removing-steps), given removedNode and oldParent, are:

1. 

If oldParent is a [picture](#the-picture-element) element, then, count this as a [relevant mutation](images.html#relevant-mutations) for removedNode.

The [img](#the-img-element) element must not be used as a layout tool. In particular, [img](#the-img-element) elements should not be used to display transparent images, as such images rarely convey meaning and rarely add anything useful to the document.

What an [img](#the-img-element) element represents depends on the [src](#attr-img-src) attribute and the [alt](#attr-img-alt) attribute.

If the [src](#attr-img-src) attribute is set and the [alt](#attr-img-alt) attribute is set to the empty string

The image is either decorative or supplemental to the rest of the content, redundant with some other information in the document.

If the image is [available](images.html#img-available) and the user agent is configured to display that image, then the element [represents](dom.html#represents) the element's image data.

Otherwise, the element [represents](dom.html#represents) nothing, and may be omitted completely from the rendering. User agents may provide the user with a notification that an image is present but has been omitted from the rendering.

If the [src](#attr-img-src) attribute is set and the [alt](#attr-img-alt) attribute is set to a value that isn't empty

The image is a key part of the content; the [alt](#attr-img-alt) attribute gives a textual equivalent or replacement for the image.

If the image is [available](images.html#img-available) and the user agent is configured to display that image, then the element [represents](dom.html#represents) the element's image data.

Otherwise, the element [represents](dom.html#represents) the text given by the [alt](#attr-img-alt) attribute. User agents may provide the user with a notification that an image is present but has been omitted from the rendering.

If the [src](#attr-img-src) attribute is set and the [alt](#attr-img-alt) attribute is not

The image might be a key part of the content, and there is no textual equivalent of the image available.

In a conforming document, the absence of the [alt](#attr-img-alt) attribute indicates that the image is a key part of the content but that a textual replacement for the image was not available when the image was generated.

If the image is [available](images.html#img-available) and the user agent is configured to display that image, then the element [represents](dom.html#represents) the element's image data.

If the image has a [src](#attr-img-src) attribute whose value is the empty string, then the element [represents](dom.html#represents) nothing.

Otherwise, the user agent should display some sort of indicator that there is an image that is not being rendered, and may, if requested by the user, or if so configured, or when required to provide contextual information in response to navigation, provide caption information for the image, derived as follows:

1. 

If the image has a [title](dom.html#attr-title) attribute whose value is not the empty string, then return the value of that attribute.
2. 

If the image is a descendant of a [figure](grouping-content.html#the-figure-element) element that has a child [figcaption](grouping-content.html#the-figcaption-element) element, and, ignoring the [figcaption](grouping-content.html#the-figcaption-element) element and its descendants, the [figure](grouping-content.html#the-figure-element) element has no [flow content](dom.html#flow-content-2) descendants other than [inter-element whitespace](dom.html#inter-element-whitespace) and the [img](#the-img-element) element, then return the contents of the first such [figcaption](grouping-content.html#the-figcaption-element) element.
3. 

Return nothing. (There is no caption information.)

If the [src](#attr-img-src) attribute is not set and either the [alt](#attr-img-alt) attribute is set to the empty string or the [alt](#attr-img-alt) attribute is not set at all

The element [represents](dom.html#represents) nothing.

Otherwise

The element [represents](dom.html#represents) the text given by the [alt](#attr-img-alt) attribute.

The [alt](#attr-img-alt) attribute does not represent advisory information. User agents must not present the contents of the [alt](#attr-img-alt) attribute in the same way as content of the [title](dom.html#attr-title) attribute.

User agents may always provide the user with the option to display any image, or to prevent any image from being displayed. User agents may also apply heuristics to help the user make use of the image when the user is unable to see it, e.g. due to a visual disability or because they are using a text terminal with no graphics capabilities. Such heuristics could include, for instance, optical character recognition (OCR) of text found within the image.

While user agents are encouraged to repair cases of missing [alt](#attr-img-alt) attributes, authors must not rely on such behavior. [Requirements for providing text to act as an alternative for images](images.html#alt) are described in detail below.

The contents of [img](#the-img-element) elements, if any, are ignored for the purposes of rendering.

The [usemap](image-maps.html#attr-hyperlink-usemap) attribute, if present, can indicate that the image has an associated [image map](image-maps.html#image-map).

The `ismap` attribute, when used on an element that is a descendant of an [a](text-level-semantics.html#the-a-element) element with an [href](links.html#attr-hyperlink-href) attribute, indicates by its presence that the element provides access to a server-side image map. This affects how events are handled on the corresponding [a](text-level-semantics.html#the-a-element) element.

The [ismap](#attr-img-ismap) attribute is a [boolean attribute](common-microsyntaxes.html#boolean-attribute). The attribute must not be specified on an element that does not have an ancestor [a](text-level-semantics.html#the-a-element) element with an [href](links.html#attr-hyperlink-href) attribute.

The [usemap](image-maps.html#attr-hyperlink-usemap) and [ismap](#attr-img-ismap) attributes can result in confusing behavior when used together with [source](#the-source-element) elements with the [media](#attr-source-media) attribute specified in a [picture](#the-picture-element) element.

The [img](#the-img-element) element supports [dimension
  attributes](embedded-content-other.html#dimension-attributes).

✔MDN

[HTMLImageElement/crossOrigin](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/crossOrigin)

Support in all current engines.Firefox8+Safari6+Chrome13+Opera12.1+Edge79+Edge (Legacy)12+Internet Explorer11Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android12.1+

The `crossOrigin` IDL attribute must [reflect](common-dom-interfaces.html#reflect) the [crossorigin](#attr-img-crossorigin) content attribute, [limited to only known values](common-dom-interfaces.html#limited-to-only-known-values).

✔MDN

[HTMLImageElement/referrerPolicy](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/referrerPolicy)

Support in all current engines.Firefox50+Safari14+Chrome52+Opera?Edge79+Edge (Legacy)?Internet ExplorerNoFirefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The `referrerPolicy` IDL attribute must [reflect](common-dom-interfaces.html#reflect) the [referrerpolicy](#attr-img-referrerpolicy) content attribute, [limited to only known values](common-dom-interfaces.html#limited-to-only-known-values).

✔MDN

[HTMLImageElement/decoding](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/decoding)

Support in all current engines.Firefox63+Safari11.1+Chrome65+Opera?Edge79+Edge (Legacy)?Internet ExplorerNoFirefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[SVGImageElement/decoding](https://developer.mozilla.org/en-US/docs/Web/API/SVGImageElement/decoding)Firefox63+SafariNoChrome65+Opera?Edge79+Edge (Legacy)?Internet ExplorerNoFirefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The `decoding` IDL attribute must [reflect](common-dom-interfaces.html#reflect) the [decoding](#attr-img-decoding) content attribute, [limited to only known values](common-dom-interfaces.html#limited-to-only-known-values).

✔MDN

[HTMLImageElement/loading](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/loading)

Support in all current engines.Firefox75+Safari15.4+Chrome77+Opera?Edge79+Edge (Legacy)?Internet ExplorerNoFirefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The `loading` IDL attribute must [reflect](common-dom-interfaces.html#reflect) the [loading](#attr-img-loading) content attribute, [limited to only known values](common-dom-interfaces.html#limited-to-only-known-values).

The `fetchPriority` IDL attribute must [reflect](common-dom-interfaces.html#reflect) the [fetchpriority](#attr-img-fetchpriority) content attribute, [limited to only known values](common-dom-interfaces.html#limited-to-only-known-values).

[width](#dom-img-width)`image. [ = value ]`✔MDN

[HTMLImageElement/width](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/width)

Support in all current engines.Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+Internet Explorer5.5+Firefox Android?Safari iOS1+Chrome Android?WebView Android?Samsung Internet?Opera Android12.1+[height](#dom-img-height)`image. [ = value ]`✔MDN

[HTMLImageElement/height](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/height)

Support in all current engines.Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+Internet Explorer5.5+Firefox Android?Safari iOS1+Chrome Android?WebView Android?Samsung Internet?Opera Android12.1+

These attributes return the actual rendered dimensions of the image, or 0 if the dimensions are not known.

They can be set, to change the corresponding content attributes.

[naturalWidth](#dom-img-naturalwidth)`image.`✔MDN

[HTMLImageElement/naturalWidth](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/naturalWidth)

Support in all current engines.Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+Internet Explorer9+Firefox Android?Safari iOS1+Chrome Android?WebView Android?Samsung Internet?Opera Android12.1+[naturalHeight](#dom-img-naturalheight)`image.`✔MDN

[HTMLImageElement/naturalHeight](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/naturalHeight)

Support in all current engines.Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+Internet Explorer9+Firefox Android?Safari iOS1+Chrome Android?WebView Android?Samsung Internet?Opera Android12.1+

These attributes return the natural dimensions of the image, or 0 if the dimensions are not known.

[complete](#dom-img-complete)`image.`✔MDN

[HTMLImageElement/complete](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/complete)

Support in all current engines.Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+Internet Explorer5.5+Firefox Android?Safari iOS1+Chrome Android?WebView Android?Samsung Internet?Opera Android12.1+

Returns true if the image has been completely downloaded or if no image is specified; otherwise, returns false.

[currentSrc](#dom-img-currentsrc)`image.`✔MDN

[HTMLImageElement/currentSrc](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/currentSrc)

Support in all current engines.Firefox38+Safari9.1+Chrome38+Opera?Edge79+Edge (Legacy)13+Internet ExplorerNoFirefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

Returns the image's [absolute URL](https://url.spec.whatwg.org/#syntax-url-absolute).[decode](#dom-img-decode)`image.()`✔MDN

[HTMLImageElement/decode](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/decode)

Support in all current engines.Firefox68+Safari11.1+Chrome64+Opera?Edge79+Edge (Legacy)?Internet ExplorerNoFirefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[SVGImageElement/decode](https://developer.mozilla.org/en-US/docs/Web/API/SVGImageElement/decode)Firefox68+SafariNoChrome64+Opera?Edge79+Edge (Legacy)?Internet ExplorerNoFirefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

This method causes the user agent to [decode](images.html#img-decoding-process) the image [in parallel](infrastructure.html#in-parallel), returning a promise that fulfills when decoding is complete.

The promise will be rejected with an ["EncodingError"](https://webidl.spec.whatwg.org/#encodingerror)[DOMException](https://webidl.spec.whatwg.org/#dfn-DOMException) if the image cannot be decoded.

[Image](#dom-image)`image = new ([ width [, height ] ])`✔MDN

[HTMLImageElement/Image](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/Image)

Support in all current engines.Firefox1+Safari1+Chrome1+Opera8+Edge79+Edge (Legacy)12+Internet Explorer5.5+Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android10.1+

Returns a new [img](#the-img-element) element, with the [width](embedded-content-other.html#attr-dim-width) and [height](embedded-content-other.html#attr-dim-height) attributes set to the values passed in the relevant arguments, if applicable.

The IDL attributes `width` and `height` must return the rendered width and height of the image, in [CSS pixels](https://drafts.csswg.org/css-values/#px), if the image is [being rendered](rendering.html#being-rendered); or else the [density-corrected natural width and height](images.html#density-corrected-intrinsic-width-and-height) of the image, in [CSS pixels](https://drafts.csswg.org/css-values/#px), if the image has [density-corrected natural width and
  height](images.html#density-corrected-intrinsic-width-and-height) and is [available](images.html#img-available) but is not [being
  rendered](rendering.html#being-rendered); or else 0, if the image is not [available](images.html#img-available) or does not have [density-corrected natural width and height](images.html#density-corrected-intrinsic-width-and-height). [[CSS]](references.html#refsCSS)

The IDL attributes `naturalWidth` and `naturalHeight` must return the [density-corrected natural width and height](images.html#density-corrected-intrinsic-width-and-height) of the image, in [CSS pixels](https://drafts.csswg.org/css-values/#px), if the image has [density-corrected natural width and
  height](images.html#density-corrected-intrinsic-width-and-height) and is [available](images.html#img-available), or else 0. [[CSS]](references.html#refsCSS)

Since the [density-corrected natural width and height](images.html#density-corrected-intrinsic-width-and-height) of an image take into account any orientation specified in its metadata, [naturalWidth](#dom-img-naturalwidth) and [naturalHeight](#dom-img-naturalheight) reflect the dimensions after applying any rotation needed to correctly orient the image, regardless of the value of the ['image-orientation'](https://drafts.csswg.org/css-images-3/#the-image-orientation) property.

The `complete` getter steps are:

1. 

If any of the following are true:

  - 

both the [src](#attr-img-src) attribute and the [srcset](#attr-img-srcset) attribute are omitted;
  - 

the [srcset](#attr-img-srcset) attribute is omitted and the [src](#attr-img-src) attribute's value is the empty string;
  - 

the [img](#the-img-element) element's [current request](images.html#current-request)'s [state](images.html#img-req-state) is [completely available](images.html#img-all) and its [pending request](images.html#pending-request) is null; or
  - 

the [img](#the-img-element) element's [current request](images.html#current-request)'s [state](images.html#img-req-state) is [broken](images.html#img-error) and its [pending request](images.html#pending-request) is null,

then return true.

2. 

Return false.

The `currentSrc` IDL attribute must return the [img](#the-img-element) element's [current request](images.html#current-request)'s [current
  URL](images.html#img-req-url).

The `decode()` method, when invoked, must perform the following steps:

1. 

Let promise be a new promise.
2. 

[Queue a microtask](webappapis.html#queue-a-microtask) to perform the following steps:

This is done because [updating the image data](images.html#update-the-image-data) takes place in a microtask as well. Thus, to make code such as

```
img.src = "stars.jpg";
img.decode();
```

properly decode `stars.jpg`, we need to delay any processing by one microtask.

  1. 

Let global be [this](https://webidl.spec.whatwg.org/#this)'s [relevant global
     object](webappapis.html#concept-relevant-global).
  2. 

If any of the following are true:

    - 

[this](https://webidl.spec.whatwg.org/#this)'s [node document](https://dom.spec.whatwg.org/#concept-node-document) is not [fully active](document-sequences.html#fully-active); or
    - 

[this](https://webidl.spec.whatwg.org/#this)'s [current request](images.html#current-request)'s [state](images.html#img-req-state) is [broken](images.html#img-error),

then reject promise with an ["EncodingError"](https://webidl.spec.whatwg.org/#encodingerror)[DOMException](https://webidl.spec.whatwg.org/#dfn-DOMException).

  3. 

Otherwise, [in parallel](infrastructure.html#in-parallel), wait for one of the following cases to occur, and perform the corresponding actions:

This [img](#the-img-element) element's [node document](https://dom.spec.whatwg.org/#concept-node-document) stops being [fully
       active](document-sequences.html#fully-active)This [img](#the-img-element) element's [current request](images.html#current-request) changes or is mutatedThis [img](#the-img-element) element's [current request](images.html#current-request)'s [state](images.html#img-req-state) becomes [broken](images.html#img-error)

[Queue a global task](webappapis.html#queue-a-global-task) on the [DOM manipulation task source](webappapis.html#dom-manipulation-task-source) with global to reject promise with an ["EncodingError"](https://webidl.spec.whatwg.org/#encodingerror)[DOMException](https://webidl.spec.whatwg.org/#dfn-DOMException).This [img](#the-img-element) element's [current request](images.html#current-request)'s [state](images.html#img-req-state) becomes [completely
       available](images.html#img-all)

[Decode](images.html#img-decoding-process) the image.

If decoding does not need to be performed for this image (for example because it is a vector graphic) or the decoding process completes successfully, then [queue a global
        task](webappapis.html#queue-a-global-task) on the [DOM manipulation task source](webappapis.html#dom-manipulation-task-source) with global to resolve promise with undefined.

If decoding fails (for example due to invalid image data), then [queue a global
        task](webappapis.html#queue-a-global-task) on the [DOM manipulation task source](webappapis.html#dom-manipulation-task-source) with global to reject promise with an ["EncodingError"](https://webidl.spec.whatwg.org/#encodingerror)[DOMException](https://webidl.spec.whatwg.org/#dfn-DOMException).

User agents should ensure that the decoded media data stays readily available until at least the end of the next successful [update the rendering](webappapis.html#update-the-rendering) step in the [event loop](webappapis.html#event-loop). This is an important part of the API contract, and should not be broken if at all possible. (Typically, this would only be violated in low-memory situations that require evicting decoded image data, or when the image is too large to keep in decoded form for this period of time.)

Animated images will become [completely available](images.html#img-all) only after all their frames are loaded. Thus, even though an implementation could decode the first frame before that point, the above steps will not do so, instead waiting until all frames are available.

3. 

Return promise.

Without the [decode()](#dom-img-decode) method, the process of loading an [img](#the-img-element) element and then displaying it might look like the following:

```
const img = new Image();
img.src = "nebula.jpg";
img.onload = () => {
    document.body.appendChild(img);
};
img.onerror = () => {
    document.body.appendChild(new Text("Could not load the nebula :("));
};
```

However, this can cause notable dropped frames, as the paint that occurs after inserting the image into the DOM causes a synchronous decode on the main thread.

This can instead be rewritten using the [decode()](#dom-img-decode) method:

```
const img = new Image();
img.src = "nebula.jpg";
img.decode().then(() => {
    document.body.appendChild(img);
}).catch(() => {
    document.body.appendChild(new Text("Could not load the nebula :("));
});
```

This latter form avoids the dropped frames of the original, by allowing the user agent to decode the image [in parallel](infrastructure.html#in-parallel), and only inserting it into the DOM (and thus causing it to be painted) once the decoding process is complete.

Because the [decode()](#dom-img-decode) method attempts to ensure that the decoded image data is available for at least one frame, it can be combined with the [requestAnimationFrame()](imagebitmap-and-animations.html#dom-animationframeprovider-requestanimationframe) API. This means it can be used with coding styles or frameworks that ensure that all DOM modifications are batched together as [animation frame
   callbacks](imagebitmap-and-animations.html#list-of-animation-frame-callbacks):

```
const container = document.querySelector("#container");

const { containerWidth, containerHeight } = computeDesiredSize();
requestAnimationFrame(() => {
 container.style.width = containerWidth;
 container.style.height = containerHeight;
});

// ...

const img = new Image();
img.src = "supernova.jpg";
img.decode().then(() => {
    requestAnimationFrame(() => container.appendChild(img));
});
```

A legacy factory function is provided for creating [HTMLImageElement](#htmlimageelement) objects (in addition to the factory methods from DOM such as [createElement()](https://dom.spec.whatwg.org/#dom-document-createelement)): `Image(width, height)`. When invoked, the legacy factory function must perform the following steps:

1. 

Let document be the [current global object](webappapis.html#current-global-object)'s [associated Document](nav-history-apis.html#concept-document-window).
2. 

Let img be the result of [creating an
   element](https://dom.spec.whatwg.org/#concept-create-element) given document, "`img`", and the [HTML
   namespace](https://infra.spec.whatwg.org/#html-namespace).
3. 

If width is given, then [set
   an attribute value](https://dom.spec.whatwg.org/#concept-element-attributes-set-value) for img using "[width](embedded-content-other.html#attr-dim-width)" and width.
4. 

If height is given, then [set an attribute value](https://dom.spec.whatwg.org/#concept-element-attributes-set-value) for img using "[height](embedded-content-other.html#attr-dim-height)" and height.
5. 

Return img.

A single image can have different appropriate alternative text depending on the context.

In each of the following cases, the same image is used, yet the [alt](#attr-img-alt) text is different each time. The image is the coat of arms of the Carouge municipality in the canton Geneva in Switzerland.

Here it is used as a supplementary icon:

```
<p>I lived in <img src="carouge.svg" alt=""> Carouge.</p>
```

Here it is used as an icon representing the town:

```
<p>Home town: <img src="carouge.svg" alt="Carouge"></p>
```

Here it is used as part of a text on the town:

```
<p>Carouge has a coat of arms.</p>
<p><img src="carouge.svg" alt="The coat of arms depicts a lion, sitting in front of a tree."></p>
<p>It is used as decoration all over the town.</p>
```

Here it is used as a way to support a similar text where the description is given as well as, instead of as an alternative to, the image:

```
<p>Carouge has a coat of arms.</p>
<p><img src="carouge.svg" alt=""></p>
<p>The coat of arms depicts a lion, sitting in front of a tree.
It is used as decoration all over the town.</p>
```

Here it is used as part of a story:

```
<p>She picked up the folder and a piece of paper fell out.</p>
<p><img src="carouge.svg" alt="Shaped like a shield, the paper had a
red background, a green tree, and a yellow lion with its tongue
hanging out and whose tail was shaped like an S."></p>
<p>She stared at the folder. S! The answer she had been looking for all
this time was simply the letter S! How had she not seen that before? It all
came together now. The phone call where Hector had referred to a lion's tail,
the time Maria had stuck her tongue out...</p>
```

Here it is not known at the time of publication what the image will be, only that it will be a coat of arms of some kind, and thus no replacement text can be provided, and instead only a brief caption for the image is provided, in the [title](dom.html#attr-title) attribute:

```
<p>The last user to have uploaded a coat of arms uploaded this one:</p>
<p><img src="last-uploaded-coat-of-arms.cgi" title="User-uploaded coat of arms."></p>
```

Ideally, the author would find a way to provide real replacement text even in this case, e.g. by asking the previous user. Not providing replacement text makes the document more difficult to use for people who are unable to view images, e.g. blind users, or users or very low-bandwidth connections or who pay by the byte, or users who are forced to use a text-only web browser.

Here are some more examples showing the same picture used in different contexts, with different appropriate alternate texts each time.

```
<article>
 <h1>My cats</h1>
 <h2>Fluffy</h2>
 <p>Fluffy is my favorite.</p>
 <img src="fluffy.jpg" alt="She likes playing with a ball of yarn.">
 <p>She's just too cute.</p>
 <h2>Miles</h2>
 <p>My other cat, Miles just eats and sleeps.</p>
</article>
```

```
<article>
 <h1>Photography</h1>
 <h2>Shooting moving targets indoors</h2>
 <p>The trick here is to know how to anticipate; to know at what speed and
 what distance the subject will pass by.</p>
 <img src="fluffy.jpg" alt="A cat flying by, chasing a ball of yarn, can be
 photographed quite nicely using this technique.">
 <h2>Nature by night</h2>
 <p>To achieve this, you'll need either an extremely sensitive film, or
 immense flash lights.</p>
</article>
```

```
<article>
 <h1>About me</h1>
 <h2>My pets</h2>
 <p>I've got a cat named Fluffy and a dog named Miles.</p>
 <img src="fluffy.jpg" alt="Fluffy, my cat, tends to keep itself busy.">
 <p>My dog Miles and I like go on long walks together.</p>
 <h2>music</h2>
 <p>After our walks, having emptied my mind, I like listening to Bach.</p>
</article>
```

```
<article>
 <h1>Fluffy and the Yarn</h1>
 <p>Fluffy was a cat who liked to play with yarn. She also liked to jump.</p>
 <aside><img src="fluffy.jpg" alt="" title="Fluffy"></aside>
 <p>She would play in the morning, she would play in the evening.</p>
</article>
```

[← 4.7 Edits](edits.html) — [Table of Contents](./) — [4.8.4 Images →](images.html)
