# HTMLMarqueeElement

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

The `HTMLMarqueeElement` interface provides methods to manipulate [<marquee>](/en-US/docs/Web/HTML/Reference/Elements/marquee) elements.

It inherits properties and methods from the [HTMLElement](/en-US/docs/Web/API/HTMLElement) interface.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLMarqueeElement.behavior 
Deprecated](#htmlmarqueeelement.behavior)

Sets how the text is scrolled within the marquee. Possible values are `scroll`, `slide` and `alternate`. If no value is specified, the default value is `scroll`.

[HTMLMarqueeElement.bgColor 
Deprecated](#htmlmarqueeelement.bgcolor)

Sets the background color through color name or hexadecimal value.

[HTMLMarqueeElement.direction 
Deprecated](#htmlmarqueeelement.direction)

Sets the direction of the scrolling within the marquee. Possible values are `left`, `right`, `up` and `down`. If no value is specified, the default value is `left`.

[HTMLMarqueeElement.height 
Deprecated](#htmlmarqueeelement.height)

Sets the height in pixels or percentage value.

[HTMLMarqueeElement.hspace 
Deprecated](#htmlmarqueeelement.hspace)

Sets the horizontal margin.

[HTMLMarqueeElement.loop 
Deprecated](#htmlmarqueeelement.loop)

Sets the number of times the marquee will scroll. If no value is specified, the default value is −1, which means the marquee will scroll continuously.

[HTMLMarqueeElement.scrollAmount 
Deprecated](#htmlmarqueeelement.scrollamount)

Sets the amount of scrolling at each interval in pixels. The default value is 6.

[HTMLMarqueeElement.scrollDelay 
Deprecated](#htmlmarqueeelement.scrolldelay)

Sets the interval between each scroll movement in milliseconds. The default value is 85. Note that any value smaller than 60 is ignored and the value 60 is used instead, unless `trueSpeed` is `true`.

[HTMLMarqueeElement.trueSpeed 
Deprecated](#htmlmarqueeelement.truespeed)

By default, `scrollDelay` values lower than 60 are ignored. If `trueSpeed` is `true`, then those values are not ignored.

["HTMLMarqueeElement.vspace 
Deprecated](#htmlmarqueeelement.vspace)

Sets the vertical margin.

[HTMLMarqueeElement.width 
Deprecated](#htmlmarqueeelement.width)

Sets the width in pixels or percentage value.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLMarqueeElement.start() 
Deprecated](#htmlmarqueeelement.start)

Starts scrolling of the marquee.

[HTMLMarqueeElement.stop() 
Deprecated](#htmlmarqueeelement.stop)

Stops scrolling of the marquee.

## [Events](#events)

[bounce 
Deprecated](#bounce)

Fires when the marquee has reached the end of its scroll position. It can only fire when the behavior attribute is set to `alternate`.

[finish 
Deprecated](#finish)

Fires when the marquee has finished the amount of scrolling that is set by the loop attribute. It can only fire when the loop attribute is set to some number that is greater than 0.

[start 
Deprecated](#start)

Fires when the marquee starts scrolling.

## [Specifications](#specifications)

Specification
[HTML# htmlmarqueeelement](https://html.spec.whatwg.org/multipage/obsolete.html#htmlmarqueeelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [<marquee>](/en-US/docs/Web/HTML/Reference/Elements/marquee)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 11, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLMarqueeElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlmarqueeelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLMarqueeElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlmarqueeelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLMarqueeElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlmarqueeelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7cd51a73ad94df604db79ccacbbe0513d0967650%0A*+Document+last+modified%3A+2025-06-11T15%3A52%3A08.000Z%0A%0A%3C%2Fdetails%3E)
