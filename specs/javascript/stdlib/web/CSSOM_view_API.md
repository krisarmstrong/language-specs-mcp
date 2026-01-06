# CSSOM view API

The CSSOM view API lets you manipulate the visual view of a document, including getting the position of element layout boxes, obtaining the width or height of the viewport through script, and also scrolling an element.

## In this article

- [Guides](#guides)
- [Interfaces](#interfaces)
- [Extensions to other interfaces](#extensions_to_other_interfaces)
- [Specifications](#specifications)
- [See also](#see_also)

## [Guides](#guides)

[Coordinate systems](/en-US/docs/Web/API/CSSOM_view_API/Coordinate_systems)

The coordinate systems used to specify a position in a display context such as a window on a monitor, a viewport on a mobile device, or a position on a sheet of paper when printing.

[Viewport concepts](/en-US/docs/Web/CSS/Guides/CSSOM_view/Viewport_concepts)

The concept of the viewport — what it is, its impact in terms of CSS, SVG, and mobile devices — and the difference between the visual viewport and the layout viewport.

## [Interfaces](#interfaces)

- [MediaQueryList](/en-US/docs/Web/API/MediaQueryList)
- [MediaQueryListEvent](/en-US/docs/Web/API/MediaQueryListEvent)
- [Screen](/en-US/docs/Web/API/Screen)
- [CaretPosition](/en-US/docs/Web/API/CaretPosition)
- [VisualViewport](/en-US/docs/Web/API/VisualViewport)

## [Extensions to other interfaces](#extensions_to_other_interfaces)

This module adds properties, methods, and events to interfaces defined in other specifications.

### [Extensions to Window](#extensions_to_window)

- [devicePixelRatio](/en-US/docs/Web/API/Window/devicePixelRatio)
- [innerHeight](/en-US/docs/Web/API/Window/innerHeight)
- [innerWidth](/en-US/docs/Web/API/Window/innerWidth)
- [matchMedia()](/en-US/docs/Web/API/Window/matchMedia)
- [moveBy()](/en-US/docs/Web/API/Window/moveBy)
- [moveTo()](/en-US/docs/Web/API/Window/moveTo)
- [outerHeight](/en-US/docs/Web/API/Window/outerHeight)
- [outerWidth](/en-US/docs/Web/API/Window/outerWidth)
- `pageXOffset` (see [scrollX](/en-US/docs/Web/API/Window/scrollX))
- `pageYOffset` (see [scrollY](/en-US/docs/Web/API/Window/scrollY))
- [resizeBy()](/en-US/docs/Web/API/Window/resizeBy)
- [resizeTo()](/en-US/docs/Web/API/Window/resizeTo)
- [screen](/en-US/docs/Web/API/Window/screen)
- [screenLeft](/en-US/docs/Web/API/Window/screenLeft)
- [screenTop](/en-US/docs/Web/API/Window/screenTop)
- [screenX](/en-US/docs/Web/API/Window/screenX)
- [screenY](/en-US/docs/Web/API/Window/screenY)
- [visualViewport](/en-US/docs/Web/API/Window/visualViewport)
- [scroll()](/en-US/docs/Web/API/Window/scroll)
- [scrollBy()](/en-US/docs/Web/API/Window/scrollBy)
- [scrollTo()](/en-US/docs/Web/API/Window/scrollTo)
- [scrollX](/en-US/docs/Web/API/Window/scrollX)
- [scrollY](/en-US/docs/Web/API/Window/scrollY)
- [resize](/en-US/docs/Web/API/Window/resize_event) event

### [Extensions to Document](#extensions_to_document)

- [elementFromPoint()](/en-US/docs/Web/API/Document/elementFromPoint)
- [caretPositionFromPoint()](/en-US/docs/Web/API/Document/caretPositionFromPoint)
- [scrollingElement](/en-US/docs/Web/API/Document/scrollingElement)
- [scroll](/en-US/docs/Web/API/Document/scroll_event) event
- [scrollend](/en-US/docs/Web/API/Document/scrollend_event) event

### [Extensions to Element](#extensions_to_element)

- [checkVisibility()](/en-US/docs/Web/API/Element/checkVisibility)
- [clientHeight](/en-US/docs/Web/API/Element/clientHeight)
- [clientLeft](/en-US/docs/Web/API/Element/clientLeft)
- [clientTop](/en-US/docs/Web/API/Element/clientTop)
- [clientWidth](/en-US/docs/Web/API/Element/clientWidth)
- [currentCSSZoom](/en-US/docs/Web/API/Element/currentCSSZoom)
- [getBoundingClientRect()](/en-US/docs/Web/API/Element/getBoundingClientRect)
- [getClientRects()](/en-US/docs/Web/API/Element/getClientRects)
- [scroll()](/en-US/docs/Web/API/Element/scroll)
- [scrollBy()](/en-US/docs/Web/API/Element/scrollBy)
- [scrollHeight](/en-US/docs/Web/API/Element/scrollHeight)
- [scrollIntoView()](/en-US/docs/Web/API/Element/scrollIntoView)
- [scrollLeft](/en-US/docs/Web/API/Element/scrollLeft)
- [scrollTo()](/en-US/docs/Web/API/Element/scrollTo)
- [scrollTop](/en-US/docs/Web/API/Element/scrollTop)
- [scrollWidth](/en-US/docs/Web/API/Element/scrollWidth)
- [scroll](/en-US/docs/Web/API/Element/scroll_event) event
- [scrollend](/en-US/docs/Web/API/Element/scrollend_event) event

### [Extensions to HTMLElement](#extensions_to_htmlelement)

- [offsetHeight](/en-US/docs/Web/API/HTMLElement/offsetHeight)
- [offsetLeft](/en-US/docs/Web/API/HTMLElement/offsetLeft)
- [offsetParent](/en-US/docs/Web/API/HTMLElement/offsetParent)
- [offsetTop](/en-US/docs/Web/API/HTMLElement/offsetTop)
- [offsetWidth](/en-US/docs/Web/API/HTMLElement/offsetWidth)

### [Extensions to HTMLImageElement](#extensions_to_htmlimageelement)

- [x](/en-US/docs/Web/API/HTMLImageElement/x)
- [y](/en-US/docs/Web/API/HTMLImageElement/y)

### [Extensions to Range](#extensions_to_range)

- [getBoundingClientRect()](/en-US/docs/Web/API/Range/getBoundingClientRect)
- [getClientRects()](/en-US/docs/Web/API/Range/getClientRects)

### [Extensions to MouseEvent](#extensions_to_mouseevent)

- [clientX](/en-US/docs/Web/API/MouseEvent/clientX)
- [clientY](/en-US/docs/Web/API/MouseEvent/clientY)
- [offsetX](/en-US/docs/Web/API/MouseEvent/offsetX)
- [offsetY](/en-US/docs/Web/API/MouseEvent/offsetY)
- [pageX](/en-US/docs/Web/API/MouseEvent/pageX)
- [pageY](/en-US/docs/Web/API/MouseEvent/pageY)
- [screenY](/en-US/docs/Web/API/MouseEvent/screenY)
- [x](/en-US/docs/Web/API/MouseEvent/x)
- [y](/en-US/docs/Web/API/MouseEvent/y)

This module defines geometric utility methods that apply to the [Text](/en-US/docs/Web/API/Text), [Element](/en-US/docs/Web/API/Element), [CSSPseudoElement](/en-US/docs/Web/API/CSSPseudoElement), and [Document](/en-US/docs/Web/API/Document) interfaces. These `GeometryUtils` features are not yet implemented in any browser.

## [Specifications](#specifications)

Specification[CSSOM View Module](https://drafts.csswg.org/cssom-view/)

## [See also](#see_also)

- [CSS Object Model (CSSOM)](/en-US/docs/Web/API/CSS_Object_Model) API
- [CSSOM view](/en-US/docs/Web/CSS/Guides/CSSOM_view) module
- [CSS overflow](/en-US/docs/Web/CSS/Guides/Overflow) module
- [CSS overscroll behavior](/en-US/docs/Web/CSS/Guides/Overscroll_behavior) module
- [CSS scroll snap](/en-US/docs/Web/CSS/Guides/Scroll_snap) module
- [Viewport](/en-US/docs/Glossary/Viewport)
- [Layout viewport](/en-US/docs/Glossary/Layout_viewport)
- [Visual viewport](/en-US/docs/Glossary/Visual_Viewport)
- [zoom](/en-US/docs/Web/CSS/Reference/Properties/zoom)
- [CSSOM](/en-US/docs/Glossary/CSSOM)
- [CSS pixel](/en-US/docs/Glossary/CSS_pixel)
- [Scroll container](/en-US/docs/Glossary/Scroll_container)
- [<meta>](/en-US/docs/Web/HTML/Reference/Elements/meta)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSOM_view_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cssom_view_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSOM_view_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcssom_view_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSOM_view_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcssom_view_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
