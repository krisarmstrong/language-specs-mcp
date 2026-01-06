# Document

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDocument&level=high)

The `Document` interface represents any web page loaded in the browser and serves as an entry point into the web page's content, which is the [DOM tree](/en-US/docs/Web/API/Document_Object_Model#what_is_a_dom_tree).

The DOM tree includes elements such as [<body>](/en-US/docs/Web/HTML/Reference/Elements/body) and [<table>](/en-US/docs/Web/HTML/Reference/Elements/table), among [many others](/en-US/docs/Web/HTML/Reference/Elements). It provides functionality globally to the document, like how to obtain the page's URL and create new elements in the document.

The `Document` interface describes the common properties and methods for any kind of document. Depending on the document's type (e.g., [HTML](/en-US/docs/Web/HTML), [XML](/en-US/docs/Web/XML), SVG, …), a larger API is available: HTML documents, served with the `"text/html"` content type, also implement the [HTMLDocument](/en-US/docs/Web/API/HTMLDocument) interface, whereas XML and SVG documents implement the [XMLDocument](/en-US/docs/Web/API/XMLDocument) interface.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Static methods](#static_methods)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[Document()](/en-US/docs/Web/API/Document/Document)

Creates a new `Document` object.

## [Instance properties](#instance_properties)

This interface also inherits from the [Node](/en-US/docs/Web/API/Node) and [EventTarget](/en-US/docs/Web/API/EventTarget) interfaces.

[Document.activeElement](/en-US/docs/Web/API/Document/activeElement)Read only

Returns the [Element](/en-US/docs/Web/API/Element) that currently has focus.

[Document.activeViewTransition](/en-US/docs/Web/API/Document/activeViewTransition)Read only

Returns a [ViewTransition](/en-US/docs/Web/API/ViewTransition) instance representing the [view transition](/en-US/docs/Web/API/View_Transition_API) currently active on the document, or `null` if there is no active view transition.

[Document.adoptedStyleSheets](/en-US/docs/Web/API/Document/adoptedStyleSheets)

Add an array of constructed stylesheets to be used by the document. These stylesheets may also be shared with shadow DOM subtrees of the same document.

[Document.body](/en-US/docs/Web/API/Document/body)

Returns the [<body>](/en-US/docs/Web/HTML/Reference/Elements/body) or [<frameset>](/en-US/docs/Web/HTML/Reference/Elements/frameset) node of the current document.

[Document.characterSet](/en-US/docs/Web/API/Document/characterSet)Read only

Returns the character set being used by the document.

[Document.childElementCount](/en-US/docs/Web/API/Document/childElementCount)Read only

Returns the number of child elements of the current document.

[Document.children](/en-US/docs/Web/API/Document/children)Read only

Returns the child elements of the current document.

[Document.compatMode](/en-US/docs/Web/API/Document/compatMode)Read only

Indicates whether the document is rendered in quirks or strict mode.

[Document.contentType](/en-US/docs/Web/API/Document/contentType)Read only

Returns the Content-Type from the MIME Header of the current document.

[Document.currentScript](/en-US/docs/Web/API/Document/currentScript)Read only

Returns the [<script>](/en-US/docs/Web/HTML/Reference/Elements/script) element whose script is currently being processed and [isn't a JavaScript module](https://github.com/whatwg/html/issues/997).

[Document.doctype](/en-US/docs/Web/API/Document/doctype)Read only

Returns the Document Type Definition (DTD) of the current document.

[Document.documentElement](/en-US/docs/Web/API/Document/documentElement)Read only

Returns the [Element](/en-US/docs/Web/API/Element) that is a direct child of the document. For HTML documents, this is normally the [HTMLHtmlElement](/en-US/docs/Web/API/HTMLHtmlElement) object representing the document's [<html>](/en-US/docs/Web/HTML/Reference/Elements/html) element.

[Document.documentURI](/en-US/docs/Web/API/Document/documentURI)Read only

Returns the document location as a string.

[Document.embeds](/en-US/docs/Web/API/Document/embeds)Read only

Returns an [HTMLCollection](/en-US/docs/Web/API/HTMLCollection) of the embedded [<embed>](/en-US/docs/Web/HTML/Reference/Elements/embed) elements in the document.

[Document.featurePolicy](/en-US/docs/Web/API/Document/featurePolicy)ExperimentalRead only

Returns the [FeaturePolicy](/en-US/docs/Web/API/FeaturePolicy) interface with the feature policies applied to the document.

[Document.firstElementChild](/en-US/docs/Web/API/Document/firstElementChild)Read only

Returns the first child element of the current document.

[Document.fonts](/en-US/docs/Web/API/Document/fonts)

Returns the [FontFaceSet](/en-US/docs/Web/API/FontFaceSet) interface of the current document.

[Document.forms](/en-US/docs/Web/API/Document/forms)Read only

Returns an [HTMLCollection](/en-US/docs/Web/API/HTMLCollection) of the [<form>](/en-US/docs/Web/HTML/Reference/Elements/form) elements in the document.

[Document.fragmentDirective](/en-US/docs/Web/API/Document/fragmentDirective)Read only

Returns the [FragmentDirective](/en-US/docs/Web/API/FragmentDirective) for the current document.

[Document.fullscreenElement](/en-US/docs/Web/API/Document/fullscreenElement)Read only

The element that's currently in full screen mode for this document.

[Document.head](/en-US/docs/Web/API/Document/head)Read only

Returns the [<head>](/en-US/docs/Web/HTML/Reference/Elements/head) element of the current document.

[Document.hidden](/en-US/docs/Web/API/Document/hidden)Read only

Returns a Boolean value indicating if the page is considered hidden or not.

[Document.images](/en-US/docs/Web/API/Document/images)Read only

Returns an [HTMLCollection](/en-US/docs/Web/API/HTMLCollection) of the images in the document.

[Document.implementation](/en-US/docs/Web/API/Document/implementation)Read only

Returns the DOM implementation associated with the current document.

[Document.lastElementChild](/en-US/docs/Web/API/Document/lastElementChild)Read only

Returns the last child element of the current document.

[Document.links](/en-US/docs/Web/API/Document/links)Read only

Returns an [HTMLCollection](/en-US/docs/Web/API/HTMLCollection) of the hyperlinks in the document.

[Document.pictureInPictureElement](/en-US/docs/Web/API/Document/pictureInPictureElement)Read only

Returns the [Element](/en-US/docs/Web/API/Element) currently being presented in picture-in-picture mode in this document.

[Document.pictureInPictureEnabled](/en-US/docs/Web/API/Document/pictureInPictureEnabled)Read only

Returns true if the picture-in-picture feature is enabled.

[Document.plugins](/en-US/docs/Web/API/Document/plugins)Read only

Returns an [HTMLCollection](/en-US/docs/Web/API/HTMLCollection) of the available plugins.

[Document.pointerLockElement](/en-US/docs/Web/API/Document/pointerLockElement)Read only

Returns the element set as the target for mouse events while the pointer is locked. `null` if lock is pending, pointer is unlocked, or if the target is in another document.

[Document.prerendering](/en-US/docs/Web/API/Document/prerendering)Read onlyExperimental

Returns a boolean that indicates whether the document is currently in the process of prerendering, as initiated via the [Speculation Rules API](/en-US/docs/Web/API/Speculation_Rules_API).

[Document.scripts](/en-US/docs/Web/API/Document/scripts)Read only

Returns an [HTMLCollection](/en-US/docs/Web/API/HTMLCollection) of the [<script>](/en-US/docs/Web/HTML/Reference/Elements/script) elements in the document.

[Document.scrollingElement](/en-US/docs/Web/API/Document/scrollingElement)Read only

Returns a reference to the [Element](/en-US/docs/Web/API/Element) that scrolls the document.

[Document.styleSheets](/en-US/docs/Web/API/Document/styleSheets)Read only

Returns a [StyleSheetList](/en-US/docs/Web/API/StyleSheetList) of [CSSStyleSheet](/en-US/docs/Web/API/CSSStyleSheet) objects for stylesheets explicitly linked into, or embedded in a document.

[Document.timeline](/en-US/docs/Web/API/Document/timeline)Read only

Returns timeline as a special instance of [DocumentTimeline](/en-US/docs/Web/API/DocumentTimeline) that is automatically created on page load.

[Document.visibilityState](/en-US/docs/Web/API/Document/visibilityState)Read only

Returns a `string` denoting the visibility state of the document. Possible values are `visible`, `hidden`, and `unloaded`.

### [Extensions for HTMLDocument](#extensions_for_htmldocument)

The `Document` interface for HTML documents inherits from the [HTMLDocument](/en-US/docs/Web/API/HTMLDocument) interface or is extended for such documents.

[Document.cookie](/en-US/docs/Web/API/Document/cookie)

Returns a semicolon-separated list of the cookies for that document or sets a single cookie.

[Document.defaultView](/en-US/docs/Web/API/Document/defaultView)Read only

Returns a reference to the window object.

[Document.designMode](/en-US/docs/Web/API/Document/designMode)

Gets/sets the ability to edit the whole document.

[Document.dir](/en-US/docs/Web/API/Document/dir)

Gets/sets directionality (rtl/ltr) of the document.

[Document.fullscreenEnabled](/en-US/docs/Web/API/Document/fullscreenEnabled)Read only

Indicates whether fullscreen mode is available.

[Document.lastModified](/en-US/docs/Web/API/Document/lastModified)Read only

Returns the date on which the document was last modified.

[Document.location](/en-US/docs/Web/API/Document/location)Read only

Returns the URI of the current document.

[Document.readyState](/en-US/docs/Web/API/Document/readyState)Read only

Returns loading status of the document.

[Document.referrer](/en-US/docs/Web/API/Document/referrer)Read only

Returns the URI of the page that linked to this page.

[Document.title](/en-US/docs/Web/API/Document/title)

Sets or gets the title of the current document.

[Document.URL](/en-US/docs/Web/API/Document/URL)Read only

Returns the document location as a string.

[Named properties](#named_properties)

Some elements in the document are also exposed as properties:

- For each [<embed>](/en-US/docs/Web/HTML/Reference/Elements/embed), [<form>](/en-US/docs/Web/HTML/Reference/Elements/form), [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe), [<img>](/en-US/docs/Web/HTML/Reference/Elements/img), and [<object>](/en-US/docs/Web/HTML/Reference/Elements/object) element, its `name` (if non-empty) is exposed. For example, if the document contains `<form name="my_form">`, then `document["my_form"]` (and its equivalent `document.my_form`) returns a reference to that element.
- For each [<object>](/en-US/docs/Web/HTML/Reference/Elements/object) element, its `id` (if non-empty) is exposed.
- For each [<img>](/en-US/docs/Web/HTML/Reference/Elements/img) element with non-empty `name`, its `id` (if non-empty) is exposed.

If a property corresponds to a single element, that element is directly returned. If that single element is an iframe, then its [contentWindow](/en-US/docs/Web/API/HTMLIFrameElement/contentWindow) is returned instead. If the property corresponds to multiple elements, then an [HTMLCollection](/en-US/docs/Web/API/HTMLCollection) is returned containing all of them.

### [Deprecated properties](#deprecated_properties)

[Document.alinkColor](/en-US/docs/Web/API/Document/alinkColor)Deprecated

Returns or sets the color of active links in the document body.

[Document.all](/en-US/docs/Web/API/Document/all)Deprecated

Provides access to all elements in the document — it returns an [HTMLAllCollection](/en-US/docs/Web/API/HTMLAllCollection) rooted at the document node. This is a legacy, non-standard property and should not be used.

[Document.anchors](/en-US/docs/Web/API/Document/anchors)DeprecatedRead only

Returns a list of all of the anchors in the document.

[Document.applets](/en-US/docs/Web/API/Document/applets)DeprecatedRead only

Returns an empty [HTMLCollection](/en-US/docs/Web/API/HTMLCollection). Legacy property that used to return the list of applets within a document.

[Document.bgColor](/en-US/docs/Web/API/Document/bgColor)Deprecated

Gets/sets the background color of the current document.

[Document.charset](/en-US/docs/Web/API/Document/characterSet)DeprecatedRead only

Alias of [Document.characterSet](/en-US/docs/Web/API/Document/characterSet). Use this property instead.

[Document.domain](/en-US/docs/Web/API/Document/domain)Deprecated

Gets/sets the domain of the current document.

[Document.fgColor](/en-US/docs/Web/API/Document/fgColor)Deprecated

Gets/sets the foreground color, or text color, of the current document.

[Document.fullscreen](/en-US/docs/Web/API/Document/fullscreen)Deprecated

Returns `true` when the document is in [fullscreen mode](/en-US/docs/Web/API/Fullscreen_API).

[Document.inputEncoding](/en-US/docs/Web/API/Document/characterSet)DeprecatedRead only

Alias of [Document.characterSet](/en-US/docs/Web/API/Document/characterSet). Use this property instead.

[Document.lastStyleSheetSet](/en-US/docs/Web/API/Document/lastStyleSheetSet)DeprecatedRead onlyNon-standard

Returns the name of the style sheet set that was last enabled. Has the value `null` until the style sheet is changed by setting the value of [selectedStyleSheetSet](/en-US/docs/Web/API/Document/selectedStyleSheetSet).

[Document.linkColor](/en-US/docs/Web/API/Document/linkColor)Deprecated

Gets/sets the color of hyperlinks in the document.

[Document.preferredStyleSheetSet](/en-US/docs/Web/API/Document/preferredStyleSheetSet)DeprecatedRead onlyNon-standard

Returns the preferred style sheet set as specified by the page author.

[Document.rootElement](/en-US/docs/Web/API/Document/rootElement)Deprecated

Like [Document.documentElement](/en-US/docs/Web/API/Document/documentElement), but only for [<svg>](/en-US/docs/Web/SVG/Reference/Element/svg) root elements. Use this property instead.

[Document.selectedStyleSheetSet](/en-US/docs/Web/API/Document/selectedStyleSheetSet)DeprecatedNon-standard

Returns which style sheet set is currently in use.

[Document.styleSheetSets](/en-US/docs/Web/API/Document/styleSheetSets)DeprecatedRead onlyNon-standard

Returns a list of the style sheet sets available on the document.

[Document.vlinkColor](/en-US/docs/Web/API/Document/vlinkColor)Deprecated

Gets/sets the color of visited hyperlinks.

[Document.xmlEncoding](/en-US/docs/Web/API/Document/xmlEncoding)Deprecated

Returns the encoding as determined by the XML declaration.

[Document.xmlStandalone 
Deprecated](#document.xmlstandalone)

Returns `true` if the XML declaration specifies the document to be standalone (e.g., An external part of the DTD affects the document's content), else `false`.

[Document.xmlVersion](/en-US/docs/Web/API/Document/xmlVersion)Deprecated

Returns the version number as specified in the XML declaration or `"1.0"` if the declaration is absent.

## [Instance methods](#instance_methods)

This interface also inherits from the [Node](/en-US/docs/Web/API/Node) and [EventTarget](/en-US/docs/Web/API/EventTarget) interfaces.

[Document.adoptNode()](/en-US/docs/Web/API/Document/adoptNode)

Adopt node from an external document.

[Document.append()](/en-US/docs/Web/API/Document/append)

Inserts a set of [Node](/en-US/docs/Web/API/Node) objects or strings after the last child of the document.

[Document.ariaNotify()](/en-US/docs/Web/API/Document/ariaNotify)ExperimentalNon-standard

Specifies that a given string of text should be announced by a screen reader.

[Document.browsingTopics()](/en-US/docs/Web/API/Document/browsingTopics)Non-standardDeprecated

Returns a promise that fulfills with an array of objects representing the top topics for the user, one from each of the last three epochs. By default, the method also causes the browser to record the current page visit as observed by the caller, so the page's hostname can later be used in topics calculation. See the [Topics API](/en-US/docs/Web/API/Topics_API) for more details.

[Document.captureEvents() 
Deprecated](#document.captureevents)

See [Window.captureEvents](/en-US/docs/Web/API/Window/captureEvents).

[Document.caretPositionFromPoint()](/en-US/docs/Web/API/Document/caretPositionFromPoint)

Returns a [CaretPosition](/en-US/docs/Web/API/CaretPosition) object containing the DOM node containing the caret, and caret's character offset within that node.

[Document.caretRangeFromPoint()](/en-US/docs/Web/API/Document/caretRangeFromPoint)Non-standard

Gets a [Range](/en-US/docs/Web/API/Range) object for the document fragment under the specified coordinates.

[Document.createAttribute()](/en-US/docs/Web/API/Document/createAttribute)

Creates a new [Attr](/en-US/docs/Web/API/Attr) object and returns it.

[Document.createAttributeNS()](/en-US/docs/Web/API/Document/createAttributeNS)

Creates a new attribute node in a given namespace and returns it.

[Document.createCDATASection()](/en-US/docs/Web/API/Document/createCDATASection)

Creates a new CDATA node and returns it.

[Document.createComment()](/en-US/docs/Web/API/Document/createComment)

Creates a new comment node and returns it.

[Document.createDocumentFragment()](/en-US/docs/Web/API/Document/createDocumentFragment)

Creates a new document fragment.

[Document.createElement()](/en-US/docs/Web/API/Document/createElement)

Creates a new element with the given tag name.

[Document.createElementNS()](/en-US/docs/Web/API/Document/createElementNS)

Creates a new element with the given tag name and namespace URI.

[Document.createEvent()](/en-US/docs/Web/API/Document/createEvent)Deprecated

Creates an event object.

[Document.createNodeIterator()](/en-US/docs/Web/API/Document/createNodeIterator)

Creates a [NodeIterator](/en-US/docs/Web/API/NodeIterator) object.

[Document.createProcessingInstruction()](/en-US/docs/Web/API/Document/createProcessingInstruction)

Creates a new [ProcessingInstruction](/en-US/docs/Web/API/ProcessingInstruction) object.

[Document.createRange()](/en-US/docs/Web/API/Document/createRange)

Creates a [Range](/en-US/docs/Web/API/Range) object.

[Document.createTextNode()](/en-US/docs/Web/API/Document/createTextNode)

Creates a text node.

[Document.createTouch()](/en-US/docs/Web/API/Document/createTouch)DeprecatedNon-standard

Creates a [Touch](/en-US/docs/Web/API/Touch) object.

[Document.createTouchList()](/en-US/docs/Web/API/Document/createTouchList)DeprecatedNon-standard

Creates a [TouchList](/en-US/docs/Web/API/TouchList) object.

[Document.createTreeWalker()](/en-US/docs/Web/API/Document/createTreeWalker)

Creates a [TreeWalker](/en-US/docs/Web/API/TreeWalker) object.

[Document.elementFromPoint()](/en-US/docs/Web/API/Document/elementFromPoint)

Returns the topmost element at the specified coordinates.

[Document.elementsFromPoint()](/en-US/docs/Web/API/Document/elementsFromPoint)

Returns an array of all elements at the specified coordinates.

[Document.enableStyleSheetsForSet()](/en-US/docs/Web/API/Document/enableStyleSheetsForSet)DeprecatedNon-standard

Enables the style sheets for the specified style sheet set.

[Document.exitFullscreen()](/en-US/docs/Web/API/Document/exitFullscreen)

Stops document's fullscreen element from being displayed fullscreen.

[Document.exitPictureInPicture()](/en-US/docs/Web/API/Document/exitPictureInPicture)

Remove the video from the floating picture-in-picture window back to its original container.

[Document.exitPointerLock()](/en-US/docs/Web/API/Document/exitPointerLock)

Release the pointer lock.

[Document.getAnimations()](/en-US/docs/Web/API/Document/getAnimations)

Returns an array of all [Animation](/en-US/docs/Web/API/Animation) objects currently in effect, whose target elements are descendants of the `document`.

[Document.getBoxQuads() 
Experimental](#document.getboxquads)

Returns a list of [DOMQuad](/en-US/docs/Web/API/DOMQuad) objects representing the CSS fragments of the node.

[Document.getElementById()](/en-US/docs/Web/API/Document/getElementById)

Returns an object reference to the identified element.

[Document.getElementsByClassName()](/en-US/docs/Web/API/Document/getElementsByClassName)

Returns a list of elements with the given class name.

[Document.getElementsByTagName()](/en-US/docs/Web/API/Document/getElementsByTagName)

Returns a list of elements with the given tag name.

[Document.getElementsByTagNameNS()](/en-US/docs/Web/API/Document/getElementsByTagNameNS)

Returns a list of elements with the given tag name and namespace.

[Document.getSelection()](/en-US/docs/Web/API/Document/getSelection)

Returns a [Selection](/en-US/docs/Web/API/Selection) object representing the range of text selected by the user, or the current position of the caret.

[Document.hasPrivateToken()](/en-US/docs/Web/API/Document/hasPrivateToken)Experimental

Returns a promise that fulfills with a boolean indicating whether the browser has a [private state token](/en-US/docs/Web/API/Private_State_Token_API) stored from a particular issuer.

[Document.hasRedemptionRecord()](/en-US/docs/Web/API/Document/hasRedemptionRecord)Experimental

Returns a promise that fulfills with a boolean indicating whether the browser has a [redemption record](/en-US/docs/Web/API/Private_State_Token_API/Using#redeeming_tokens) originating from a particular issuer.

[Document.hasStorageAccess()](/en-US/docs/Web/API/Document/hasStorageAccess)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with a boolean value indicating whether the document has access to unpartitioned cookies.

[Document.hasUnpartitionedCookieAccess()](/en-US/docs/Web/API/Document/hasUnpartitionedCookieAccess)

New name for [Document.hasStorageAccess()](/en-US/docs/Web/API/Document/hasStorageAccess).

[Document.importNode()](/en-US/docs/Web/API/Document/importNode)

Returns a clone of a node from an external document.

[Document.moveBefore()](/en-US/docs/Web/API/Document/moveBefore)

Moves a given [Node](/en-US/docs/Web/API/Node) inside the `Document` DOM node as a direct child, before a given reference node, without removing and then inserting the node.

[Document.mozSetImageElement()](/en-US/docs/Web/API/Document/mozSetImageElement)Non-standard

Allows you to change the element being used as the background image for a specified element ID.

[Document.prepend()](/en-US/docs/Web/API/Document/prepend)

Inserts a set of [Node](/en-US/docs/Web/API/Node) objects or strings before the first child of the document.

[Document.querySelector()](/en-US/docs/Web/API/Document/querySelector)

Returns the first Element node within the document, in document order, that matches the specified selectors.

[Document.querySelectorAll()](/en-US/docs/Web/API/Document/querySelectorAll)

Returns a list of all the Element nodes within the document that match the specified selectors.

[Document.releaseCapture()](/en-US/docs/Web/API/Document/releaseCapture)Non-standard

Releases the current mouse capture if it's on an element in this document.

[Document.releaseEvents() 
Deprecated](#document.releaseevents)

See [Window.releaseEvents()](/en-US/docs/Web/API/Window/releaseEvents).

[Document.replaceChildren()](/en-US/docs/Web/API/Document/replaceChildren)

Replaces the existing children of a document with a specified new set of children.

[Document.requestStorageAccess()](/en-US/docs/Web/API/Document/requestStorageAccess)

Allows a document loaded in a third-party context (i.e., embedded in an [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe)) to request access to unpartitioned cookies, in cases where user agents by default block access to unpartitioned cookies by sites loaded in a third-party context to improve privacy.

[Document.requestStorageAccessFor()](/en-US/docs/Web/API/Document/requestStorageAccessFor)Experimental

Allows top-level sites to request third-party cookie access on behalf of embedded content originating from another site in the same [related website set](/en-US/docs/Web/API/Storage_Access_API/Related_website_sets).

[Document.startViewTransition()](/en-US/docs/Web/API/Document/startViewTransition)

Starts a new [view transition](/en-US/docs/Web/API/View_Transition_API) and returns a [ViewTransition](/en-US/docs/Web/API/ViewTransition) object to represent it.

The `Document` interface is extended with the [XPathEvaluator](/en-US/docs/Web/API/XPathEvaluator) interface:

[Document.createExpression()](/en-US/docs/Web/API/Document/createExpression)

Compiles an [XPathExpression](/en-US/docs/Web/API/XPathExpression) which can then be used for (repeated) evaluations.

[Document.createNSResolver()](/en-US/docs/Web/API/Document/createNSResolver)Deprecated

Returns the input node as-is.

[Document.evaluate()](/en-US/docs/Web/API/Document/evaluate)

Evaluates an XPath expression.

### [Extension for HTML documents](#extension_for_html_documents)

The `Document` interface for HTML documents inherit from the [HTMLDocument](/en-US/docs/Web/API/HTMLDocument) interface or is extended for such documents:

[Document.clear()](/en-US/docs/Web/API/Document/clear)Deprecated

This method does nothing.

[Document.close()](/en-US/docs/Web/API/Document/close)

Closes a document stream for writing.

[Document.execCommand()](/en-US/docs/Web/API/Document/execCommand)Deprecated

On an editable document, executes a formatting command.

[Document.getElementsByName()](/en-US/docs/Web/API/Document/getElementsByName)

Returns a list of elements with the given name.

[Document.hasFocus()](/en-US/docs/Web/API/Document/hasFocus)

Returns `true` if the focus is currently located anywhere inside the specified document.

[Document.open()](/en-US/docs/Web/API/Document/open)

Opens a document stream for writing.

[Document.queryCommandEnabled()](/en-US/docs/Web/API/Document/queryCommandEnabled)DeprecatedNon-standard

Returns true if the formatting command can be executed on the current range.

[Document.queryCommandIndeterm() 
Deprecated](#document.querycommandindeterm)

Returns true if the formatting command is in an indeterminate state on the current range.

[Document.queryCommandState()](/en-US/docs/Web/API/Document/queryCommandState)DeprecatedNon-standard

Returns true if the formatting command has been executed on the current range.

[Document.queryCommandSupported()](/en-US/docs/Web/API/Document/queryCommandSupported)DeprecatedNon-standard

Returns true if the formatting command is supported on the current range.

[Document.queryCommandValue() 
Deprecated](#document.querycommandvalue)

Returns the current value of the current range for a formatting command.

[Document.write()](/en-US/docs/Web/API/Document/write)Deprecated

Writes text in a document.

[Document.writeln()](/en-US/docs/Web/API/Document/writeln)Deprecated

Writes a line of text in a document.

## [Static methods](#static_methods)

This interface also inherits from the [Node](/en-US/docs/Web/API/Node) and [EventTarget](/en-US/docs/Web/API/EventTarget) interfaces.

[Document.parseHTML()](/en-US/docs/Web/API/Document/parseHTML_static)Experimental

Creates a new `Document` object from a string of HTML in an XSS-safe manner with sanitization.

[Document.parseHTMLUnsafe()](/en-US/docs/Web/API/Document/parseHTMLUnsafe_static)

Creates a new `Document` object from a string of HTML without performing sanitization. The string may contain declarative shadow roots.

## [Events](#events)

Listen to these events using `addEventListener()` or by assigning an event listener to the `oneventname` property of this interface. In addition to the events listed below, many events can bubble from [nodes](/en-US/docs/Web/API/Node) contained in the document tree.

[afterscriptexecute](/en-US/docs/Web/API/Document/afterscriptexecute_event)Non-standardDeprecated

Fired when a static [<script>](/en-US/docs/Web/HTML/Reference/Elements/script) element finishes executing its script

[beforescriptexecute](/en-US/docs/Web/API/Document/beforescriptexecute_event)Non-standardDeprecated

Fired when a static [<script>](/en-US/docs/Web/HTML/Reference/Elements/script) is about to start executing.

[prerenderingchange](/en-US/docs/Web/API/Document/prerenderingchange_event)Experimental

Fired on a prerendered document when it is activated (i.e., the user views the page).

[securitypolicyviolation](/en-US/docs/Web/API/Document/securitypolicyviolation_event)

Fired when a content security policy is violated.

[visibilitychange](/en-US/docs/Web/API/Document/visibilitychange_event)

Fired when the content of a tab has become visible or has been hidden.

### [Fullscreen events](#fullscreen_events)

[fullscreenchange](/en-US/docs/Web/API/Document/fullscreenchange_event)

Fired when the `Document` transitions into or out of [fullscreen](/en-US/docs/Web/API/Fullscreen_API/Guide) mode.

[fullscreenerror](/en-US/docs/Web/API/Document/fullscreenerror_event)

Fired if an error occurs while attempting to switch into or out of [fullscreen](/en-US/docs/Web/API/Fullscreen_API/Guide) mode.

### [Load & unload events](#load_unload_events)

[DOMContentLoaded](/en-US/docs/Web/API/Document/DOMContentLoaded_event)

Fired when the document has been completely loaded and parsed, without waiting for stylesheets, images, and subframes to finish loading.

[readystatechange](/en-US/docs/Web/API/Document/readystatechange_event)

Fired when the [readyState](/en-US/docs/Web/API/Document/readyState) attribute of a document has changed.

### [Pointer lock events](#pointer_lock_events)

[pointerlockchange](/en-US/docs/Web/API/Document/pointerlockchange_event)

Fired when the pointer is locked/unlocked.

[pointerlockerror](/en-US/docs/Web/API/Document/pointerlockerror_event)

Fired when locking the pointer failed.

### [Scroll events](#scroll_events)

[scroll](/en-US/docs/Web/API/Document/scroll_event)

Fired when the document view or an element has been scrolled.

[scrollend](/en-US/docs/Web/API/Document/scrollend_event)

Fired when the document view or an element has completed scrolling.

[scrollsnapchange](/en-US/docs/Web/API/Document/scrollsnapchange_event)Experimental

Fired on the scroll container at the end of a scrolling operation when a new scroll snap target has been selected.

[scrollsnapchanging](/en-US/docs/Web/API/Document/scrollsnapchanging_event)Experimental

Fired on the scroll container when the browser determines a new scroll snap target is pending, i.e., it will be selected when the current scroll gesture ends.

### [Selection events](#selection_events)

[selectionchange](/en-US/docs/Web/API/Document/selectionchange_event)

Fired when the current text selection on a document is changed.

### [Bubbled events](#bubbled_events)

Not all events that bubble can reach the `Document` object. Only the following do and can be listened for on the `Document` object:

- `abort`
- [auxclick](/en-US/docs/Web/API/Element/auxclick_event)
- [beforeinput](/en-US/docs/Web/API/Element/beforeinput_event)
- [beforematch](/en-US/docs/Web/API/Element/beforematch_event)
- [beforetoggle](/en-US/docs/Web/API/HTMLElement/beforetoggle_event)
- [blur](/en-US/docs/Web/API/Element/blur_event)
- `cancel`
- [canplay](/en-US/docs/Web/API/HTMLMediaElement/canplay_event)
- [canplaythrough](/en-US/docs/Web/API/HTMLMediaElement/canplaythrough_event)
- [change](/en-US/docs/Web/API/HTMLElement/change_event)
- [click](/en-US/docs/Web/API/Element/click_event)
- [close](/en-US/docs/Web/API/HTMLDialogElement/close_event)
- [contextlost](/en-US/docs/Web/API/HTMLCanvasElement/contextlost_event)
- [contextmenu](/en-US/docs/Web/API/Element/contextmenu_event)
- [contextrestored](/en-US/docs/Web/API/HTMLCanvasElement/contextrestored_event)
- [copy](/en-US/docs/Web/API/Element/copy_event)
- [cuechange](/en-US/docs/Web/API/HTMLTrackElement/cuechange_event)
- [cut](/en-US/docs/Web/API/Element/cut_event)
- [dblclick](/en-US/docs/Web/API/Element/dblclick_event)
- [drag](/en-US/docs/Web/API/HTMLElement/drag_event)
- [dragend](/en-US/docs/Web/API/HTMLElement/dragend_event)
- [dragenter](/en-US/docs/Web/API/HTMLElement/dragenter_event)
- [dragleave](/en-US/docs/Web/API/HTMLElement/dragleave_event)
- [dragover](/en-US/docs/Web/API/HTMLElement/dragover_event)
- [dragstart](/en-US/docs/Web/API/HTMLElement/dragstart_event)
- [drop](/en-US/docs/Web/API/HTMLElement/drop_event)
- [durationchange](/en-US/docs/Web/API/HTMLMediaElement/durationchange_event)
- [emptied](/en-US/docs/Web/API/HTMLMediaElement/emptied_event)
- [ended](/en-US/docs/Web/API/HTMLMediaElement/ended_event)
- [error](/en-US/docs/Web/API/HTMLElement/error_event)
- [focus](/en-US/docs/Web/API/Element/focus_event)
- [formdata](/en-US/docs/Web/API/HTMLFormElement/formdata_event)
- [input](/en-US/docs/Web/API/Element/input_event)
- [invalid](/en-US/docs/Web/API/HTMLInputElement/invalid_event)
- [keydown](/en-US/docs/Web/API/Element/keydown_event)
- [keypress](/en-US/docs/Web/API/Element/keypress_event)
- [keyup](/en-US/docs/Web/API/Element/keyup_event)
- [load](/en-US/docs/Web/API/HTMLElement/load_event)
- [loadeddata](/en-US/docs/Web/API/HTMLMediaElement/loadeddata_event)
- [loadedmetadata](/en-US/docs/Web/API/HTMLMediaElement/loadedmetadata_event)
- [loadstart](/en-US/docs/Web/API/HTMLMediaElement/loadstart_event)
- [mousedown](/en-US/docs/Web/API/Element/mousedown_event)
- [mouseenter](/en-US/docs/Web/API/Element/mouseenter_event)
- [mouseleave](/en-US/docs/Web/API/Element/mouseleave_event)
- [mousemove](/en-US/docs/Web/API/Element/mousemove_event)
- [mouseout](/en-US/docs/Web/API/Element/mouseout_event)
- [mouseover](/en-US/docs/Web/API/Element/mouseover_event)
- [mouseup](/en-US/docs/Web/API/Element/mouseup_event)
- [paste](/en-US/docs/Web/API/Element/paste_event)
- [pause](/en-US/docs/Web/API/HTMLMediaElement/pause_event)
- [play](/en-US/docs/Web/API/HTMLMediaElement/play_event)
- [playing](/en-US/docs/Web/API/HTMLMediaElement/playing_event)
- [progress](/en-US/docs/Web/API/HTMLMediaElement/progress_event)
- [ratechange](/en-US/docs/Web/API/HTMLMediaElement/ratechange_event)
- [reset](/en-US/docs/Web/API/HTMLFormElement/reset_event)
- [resize](/en-US/docs/Web/API/HTMLVideoElement/resize_event)
- [scroll](/en-US/docs/Web/API/Element/scroll_event)
- [scrollend](/en-US/docs/Web/API/Element/scrollend_event)
- [securitypolicyviolation](/en-US/docs/Web/API/Element/securitypolicyviolation_event)
- [seeked](/en-US/docs/Web/API/HTMLMediaElement/seeked_event)
- [seeking](/en-US/docs/Web/API/HTMLMediaElement/seeking_event)
- [select](/en-US/docs/Web/API/HTMLInputElement/select_event)
- [slotchange](/en-US/docs/Web/API/HTMLSlotElement/slotchange_event)
- [stalled](/en-US/docs/Web/API/HTMLMediaElement/stalled_event)
- [submit](/en-US/docs/Web/API/HTMLFormElement/submit_event)
- [suspend](/en-US/docs/Web/API/HTMLMediaElement/suspend_event)
- [timeupdate](/en-US/docs/Web/API/HTMLMediaElement/timeupdate_event)
- [toggle](/en-US/docs/Web/API/HTMLElement/toggle_event)
- [volumechange](/en-US/docs/Web/API/HTMLMediaElement/volumechange_event)
- [waiting](/en-US/docs/Web/API/HTMLMediaElement/waiting_event)
- [wheel](/en-US/docs/Web/API/Element/wheel_event)

## [Specifications](#specifications)

Specification
[DOM# interface-document](https://dom.spec.whatwg.org/#interface-document)
[HTML# the-document-object](https://html.spec.whatwg.org/multipage/dom.html#the-document-object)
[CSSOM View Module# extensions-to-the-document-interface](https://drafts.csswg.org/cssom-view/#extensions-to-the-document-interface)
[Pointer Lock 2.0# extensions-to-the-document-interface](https://w3c.github.io/pointerlock/#extensions-to-the-document-interface)
[Selection API# extensions-to-document-interface](https://w3c.github.io/selection-api/#extensions-to-document-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 18, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Document/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/document/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDocument&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdocument%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDocument%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdocument%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fee03b8deb5423c80e1cb8f6930a6f52e3f49e678%0A*+Document+last+modified%3A+2025-12-18T09%3A16%3A09.000Z%0A%0A%3C%2Fdetails%3E)
