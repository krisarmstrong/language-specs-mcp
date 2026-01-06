# Element

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FElement&level=high)

`Element` is the most general base class from which all element objects (i.e., objects that represent elements) in a [Document](/en-US/docs/Web/API/Document) inherit. It only has methods and properties common to all kinds of elements. More specific classes inherit from `Element`.

For example, the [HTMLElement](/en-US/docs/Web/API/HTMLElement) interface is the base interface for HTML elements. Similarly, the [SVGElement](/en-US/docs/Web/API/SVGElement) interface is the basis for all SVG elements, and the [MathMLElement](/en-US/docs/Web/API/MathMLElement) interface is the base interface for MathML elements. Most functionality is specified further down the class hierarchy.

Languages outside the realm of the Web platform, like XUL through the `XULElement` interface, also implement `Element`.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

`Element` inherits properties from its parent interface, [Node](/en-US/docs/Web/API/Node), and by extension that interface's parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[Element.assignedSlot](/en-US/docs/Web/API/Element/assignedSlot)Read only

Returns a [HTMLSlotElement](/en-US/docs/Web/API/HTMLSlotElement) representing the [<slot>](/en-US/docs/Web/HTML/Reference/Elements/slot) the node is inserted in.

[Element.attributes](/en-US/docs/Web/API/Element/attributes)Read only

Returns a [NamedNodeMap](/en-US/docs/Web/API/NamedNodeMap) object containing the assigned attributes of the corresponding HTML element.

[Element.childElementCount](/en-US/docs/Web/API/Element/childElementCount)Read only

Returns the number of child elements of this element.

[Element.children](/en-US/docs/Web/API/Element/children)Read only

Returns the child elements of this element.

[Element.classList](/en-US/docs/Web/API/Element/classList)Read only

Returns a [DOMTokenList](/en-US/docs/Web/API/DOMTokenList) containing the list of class attributes.

[Element.className](/en-US/docs/Web/API/Element/className)

A string representing the class of the element.

[Element.clientHeight](/en-US/docs/Web/API/Element/clientHeight)Read only

Returns a number representing the inner height of the element.

[Element.clientLeft](/en-US/docs/Web/API/Element/clientLeft)Read only

Returns a number representing the width of the left border of the element.

[Element.clientTop](/en-US/docs/Web/API/Element/clientTop)Read only

Returns a number representing the width of the top border of the element.

[Element.clientWidth](/en-US/docs/Web/API/Element/clientWidth)Read only

Returns a number representing the inner width of the element.

[Element.currentCSSZoom](/en-US/docs/Web/API/Element/currentCSSZoom)Read only

A number indicating the effective zoom size of the element, or 1.0 if the element is not rendered.

[Element.elementTiming](/en-US/docs/Web/API/Element/elementTiming)Experimental

A string reflecting the [elementtiming](/en-US/docs/Web/HTML/Reference/Attributes/elementtiming) attribute which marks an element for observation in the [PerformanceElementTiming](/en-US/docs/Web/API/PerformanceElementTiming) API.

[Element.firstElementChild](/en-US/docs/Web/API/Element/firstElementChild)Read only

Returns the first child element of this element.

[Element.id](/en-US/docs/Web/API/Element/id)

A string representing the id of the element.

[Element.innerHTML](/en-US/docs/Web/API/Element/innerHTML)

A string representing the markup of the element's content.

[Element.lastElementChild](/en-US/docs/Web/API/Element/lastElementChild)Read only

Returns the last child element of this element.

[Element.localName](/en-US/docs/Web/API/Element/localName)Read only

A string representing the local part of the qualified name of the element.

[Element.namespaceURI](/en-US/docs/Web/API/Element/namespaceURI)Read only

The namespace URI of the element, or `null` if it is no namespace.

[Element.nextElementSibling](/en-US/docs/Web/API/Element/nextElementSibling)Read only

An `Element`, the element immediately following the given one in the tree, or `null` if there's no sibling node.

[Element.outerHTML](/en-US/docs/Web/API/Element/outerHTML)

A string representing the markup of the element including its content. When used as a setter, replaces the element with nodes parsed from the given string.

[Element.part](/en-US/docs/Web/API/Element/part)

Represents the part identifier(s) of the element (i.e., set using the `part` attribute), returned as a [DOMTokenList](/en-US/docs/Web/API/DOMTokenList).

[Element.prefix](/en-US/docs/Web/API/Element/prefix)Read only

A string representing the namespace prefix of the element, or `null` if no prefix is specified.

[Element.previousElementSibling](/en-US/docs/Web/API/Element/previousElementSibling)Read only

An `Element`, the element immediately preceding the given one in the tree, or `null` if there is no sibling element.

[Element.scrollHeight](/en-US/docs/Web/API/Element/scrollHeight)Read only

Returns a number representing the scroll view height of an element.

[Element.scrollLeft](/en-US/docs/Web/API/Element/scrollLeft)

A number representing the left scroll offset of the element.

[Element.scrollLeftMax](/en-US/docs/Web/API/Element/scrollLeftMax)Non-standardRead only

Returns a number representing the maximum left scroll offset possible for the element.

[Element.scrollTop](/en-US/docs/Web/API/Element/scrollTop)

A number representing number of pixels the top of the element is scrolled vertically.

[Element.scrollTopMax](/en-US/docs/Web/API/Element/scrollTopMax)Non-standardRead only

Returns a number representing the maximum top scroll offset possible for the element.

[Element.scrollWidth](/en-US/docs/Web/API/Element/scrollWidth)Read only

Returns a number representing the scroll view width of the element.

[Element.shadowRoot](/en-US/docs/Web/API/Element/shadowRoot)Read only

Returns the open shadow root that is hosted by the element, or null if no open shadow root is present.

[Element.slot](/en-US/docs/Web/API/Element/slot)

Returns the name of the shadow DOM slot the element is inserted in.

[Element.tagName](/en-US/docs/Web/API/Element/tagName)Read only

Returns a string with the name of the tag for the given element.

### [Instance properties included from ARIA](#instance_properties_included_from_aria)

The `Element` interface also includes the following properties.

[Element.ariaAtomic](/en-US/docs/Web/API/Element/ariaAtomic)

A string reflecting the [aria-atomic](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-atomic) attribute, which indicates whether assistive technologies will present all, or only parts of, the changed region based on the change notifications defined by the [aria-relevant](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-relevant) attribute.

[Element.ariaAutoComplete](/en-US/docs/Web/API/Element/ariaAutoComplete)

A string reflecting the [aria-autocomplete](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-autocomplete) attribute, which indicates whether inputting text could trigger display of one or more predictions of the user's intended value for a combobox, searchbox, or textbox and specifies how predictions would be presented if they were made.

[Element.ariaBrailleLabel](/en-US/docs/Web/API/Element/ariaBrailleLabel)

A string reflecting the [aria-braillelabel](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-braillelabel) attribute, which defines the braille label of the element.

[Element.ariaBrailleRoleDescription](/en-US/docs/Web/API/Element/ariaBrailleRoleDescription)

A string reflecting the [aria-brailleroledescription](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-brailleroledescription) attribute, which defines the ARIA braille role description of the element.

[Element.ariaBusy](/en-US/docs/Web/API/Element/ariaBusy)

A string reflecting the [aria-busy](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-busy) attribute, which indicates whether an element is being modified, as assistive technologies may want to wait until the modifications are complete before exposing them to the user.

[Element.ariaChecked](/en-US/docs/Web/API/Element/ariaChecked)

A string reflecting the [aria-checked](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-checked) attribute, which indicates the current "checked" state of checkboxes, radio buttons, and other widgets that have a checked state.

[Element.ariaColCount](/en-US/docs/Web/API/Element/ariaColCount)

A string reflecting the [aria-colcount](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-colcount) attribute, which defines the number of columns in a table, grid, or treegrid.

[Element.ariaColIndex](/en-US/docs/Web/API/Element/ariaColIndex)

A string reflecting the [aria-colindex](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-colindex) attribute, which defines an element's column index or position with respect to the total number of columns within a table, grid, or treegrid.

[Element.ariaColIndexText](/en-US/docs/Web/API/Element/ariaColIndexText)

A string reflecting the [aria-colindextext](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-colindextext) attribute, which defines a human readable text alternative of aria-colindex.

[Element.ariaColSpan](/en-US/docs/Web/API/Element/ariaColSpan)

A string reflecting the [aria-colspan](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-colspan) attribute, which defines the number of columns spanned by a cell or gridcell within a table, grid, or treegrid.

[Element.ariaCurrent](/en-US/docs/Web/API/Element/ariaCurrent)

A string reflecting the [aria-current](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-current) attribute, which indicates the element that represents the current item within a container or set of related elements.

[Element.ariaDescription](/en-US/docs/Web/API/Element/ariaDescription)

A string reflecting the [aria-description](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-description) attribute, which defines a string value that describes or annotates the current element.

[Element.ariaDisabled](/en-US/docs/Web/API/Element/ariaDisabled)

A string reflecting the [aria-disabled](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-disabled) attribute, which indicates that the element is perceivable but disabled, so it is not editable or otherwise operable.

[Element.ariaExpanded](/en-US/docs/Web/API/Element/ariaExpanded)

A string reflecting the [aria-expanded](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-expanded) attribute, which indicates whether a grouping element owned or controlled by this element is expanded or collapsed.

[Element.ariaHasPopup](/en-US/docs/Web/API/Element/ariaHasPopup)

A string reflecting the [aria-haspopup](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-haspopup) attribute, which indicates the availability and type of interactive popup element, such as menu or dialog, that can be triggered by an element.

[Element.ariaHidden](/en-US/docs/Web/API/Element/ariaHidden)

A string reflecting the [aria-hidden](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-hidden) attribute, which indicates whether the element is exposed to an accessibility API.

[Element.ariaInvalid](/en-US/docs/Web/API/Element/ariaInvalid)

A string reflecting the [aria-invalid](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-invalid) attribute, which indicates the entered value does not conform to the format expected by the application.

[Element.ariaKeyShortcuts](/en-US/docs/Web/API/Element/ariaKeyShortcuts)

A string reflecting the [aria-keyshortcuts](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-keyshortcuts) attribute, which indicates keyboard shortcuts that an author has implemented to activate or give focus to an element.

[Element.ariaLabel](/en-US/docs/Web/API/Element/ariaLabel)

A string reflecting the [aria-label](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-label) attribute, which defines a string value that labels the current element.

[Element.ariaLevel](/en-US/docs/Web/API/Element/ariaLevel)

A string reflecting the [aria-level](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-level) attribute, which defines the hierarchical level of an element within a structure.

[Element.ariaLive](/en-US/docs/Web/API/Element/ariaLive)

A string reflecting the [aria-live](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-live) attribute, which indicates that an element will be updated, and describes the types of updates the user agents, assistive technologies, and user can expect from the live region.

[Element.ariaModal](/en-US/docs/Web/API/Element/ariaModal)

A string reflecting the [aria-modal](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-modal) attribute, which indicates whether an element is modal when displayed.

[Element.ariaMultiline](/en-US/docs/Web/API/Element/ariaMultiLine)

A string reflecting the [aria-multiline](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-multiline) attribute, which indicates whether a text box accepts multiple lines of input or only a single line.

[Element.ariaMultiSelectable](/en-US/docs/Web/API/Element/ariaMultiSelectable)

A string reflecting the [aria-multiselectable](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-multiselectable) attribute, which indicates that the user may select more than one item from the current selectable descendants.

[Element.ariaOrientation](/en-US/docs/Web/API/Element/ariaOrientation)

A string reflecting the [aria-orientation](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-orientation) attribute, which indicates whether the element's orientation is horizontal, vertical, or unknown/ambiguous.

[Element.ariaPlaceholder](/en-US/docs/Web/API/Element/ariaPlaceholder)

A string reflecting the [aria-placeholder](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-placeholder) attribute, which defines a short hint intended to aid the user with data entry when the control has no value.

[Element.ariaPosInSet](/en-US/docs/Web/API/Element/ariaPosInSet)

A string reflecting the [aria-posinset](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-posinset) attribute, which defines an element's number or position in the current set of listitems or treeitems.

[Element.ariaPressed](/en-US/docs/Web/API/Element/ariaPressed)

A string reflecting the [aria-pressed](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-pressed) attribute, which indicates the current "pressed" state of toggle buttons.

[Element.ariaReadOnly](/en-US/docs/Web/API/Element/ariaReadOnly)

A string reflecting the [aria-readonly](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-readonly) attribute, which indicates that the element is not editable, but is otherwise operable.

[Element.ariaRelevant](/en-US/docs/Web/API/Element/ariaRelevant)Non-standard

A string reflecting the [aria-relevant](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-relevant) attribute, which indicates what notifications the user agent will trigger when the accessibility tree within a live region is modified. This is used to describe what changes in an `aria-live` region are relevant and should be announced.

[Element.ariaRequired](/en-US/docs/Web/API/Element/ariaRequired)

A string reflecting the [aria-required](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-required) attribute, which indicates that user input is required on the element before a form may be submitted.

[Element.ariaRoleDescription](/en-US/docs/Web/API/Element/ariaRoleDescription)

A string reflecting the [aria-roledescription](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-roledescription) attribute, which defines a human-readable, author-localized description for the role of an element.

[Element.ariaRowCount](/en-US/docs/Web/API/Element/ariaRowCount)

A string reflecting the [aria-rowcount](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-rowcount) attribute, which defines the total number of rows in a table, grid, or treegrid.

[Element.ariaRowIndex](/en-US/docs/Web/API/Element/ariaRowIndex)

A string reflecting the [aria-rowindex](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-rowindex) attribute, which defines an element's row index or position with respect to the total number of rows within a table, grid, or treegrid.

[Element.ariaRowIndexText](/en-US/docs/Web/API/Element/ariaRowIndexText)

A string reflecting the [aria-rowindextext](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-rowindextext) attribute, which defines a human readable text alternative of aria-rowindex.

[Element.ariaRowSpan](/en-US/docs/Web/API/Element/ariaRowSpan)

A string reflecting the [aria-rowspan](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-rowspan) attribute, which defines the number of rows spanned by a cell or gridcell within a table, grid, or treegrid.

[Element.ariaSelected](/en-US/docs/Web/API/Element/ariaSelected)

A string reflecting the [aria-selected](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-selected) attribute, which indicates the current "selected" state of elements that have a selected state.

[Element.ariaSetSize](/en-US/docs/Web/API/Element/ariaSetSize)

A string reflecting the [aria-setsize](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-setsize) attribute, which defines the number of items in the current set of listitems or treeitems.

[Element.ariaSort](/en-US/docs/Web/API/Element/ariaSort)

A string reflecting the [aria-sort](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-sort) attribute, which indicates if items in a table or grid are sorted in ascending or descending order.

[Element.ariaValueMax](/en-US/docs/Web/API/Element/ariaValueMax)

A string reflecting the [aria-valueMax](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-valuemax) attribute, which defines the maximum allowed value for a range widget.

[Element.ariaValueMin](/en-US/docs/Web/API/Element/ariaValueMin)

A string reflecting the [aria-valueMin](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-valuemin) attribute, which defines the minimum allowed value for a range widget.

[Element.ariaValueNow](/en-US/docs/Web/API/Element/ariaValueNow)

A string reflecting the [aria-valueNow](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-valuenow) attribute, which defines the current value for a range widget.

[Element.ariaValueText](/en-US/docs/Web/API/Element/ariaValueText)

A string reflecting the [aria-valuetext](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-valuetext) attribute, which defines the human-readable text alternative of `aria-valuenow` for a range widget.

[Element.role](/en-US/docs/Web/API/Element/role)

A string reflecting the explicitly set [role](/en-US/docs/Web/Accessibility/ARIA/Reference/Roles) attribute, which provides the semantic role of the element.

#### Instance properties reflected from ARIA element references

The properties reflect the elements specified by `id` reference in the corresponding attributes, but with some caveats. See [Reflected element references](/en-US/docs/Web/API/Document_Object_Model/Reflected_attributes#reflected_element_references) in the Reflected attributes guide for more information.

[Element.ariaActiveDescendantElement](/en-US/docs/Web/API/Element/ariaActiveDescendantElement)

An element that represents the current active element when focus is on a [composite](/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/composite_role) widget, [combobox](/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/combobox_role), [textbox](/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/textbox_role), [group](/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/group_role), or [application](/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/application_role). Reflects the [aria-activedescendant](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-activedescendant) attribute.

[Element.ariaControlsElements](/en-US/docs/Web/API/Element/ariaControlsElements)

An array of elements whose contents or presence are controlled by the element it is applied to. Reflects the [aria-controls](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-controls) attribute.

[Element.ariaDescribedByElements](/en-US/docs/Web/API/Element/ariaDescribedByElements)

An array of elements that contain the accessible description for the element it is applied to. Reflects the [aria-describedby](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-describedby) attribute.

[Element.ariaDetailsElements](/en-US/docs/Web/API/Element/ariaDetailsElements)

An array of elements that provide accessible details for the element it is applied to. Reflects the [aria-details](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-details) attribute.

[Element.ariaErrorMessageElements](/en-US/docs/Web/API/Element/ariaErrorMessageElements)

An array of elements that provide an error message for the element it is applied to. Reflects the [aria-errormessage](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-errormessage) attribute.

[Element.ariaFlowToElements](/en-US/docs/Web/API/Element/ariaFlowToElements)

An array of elements that identify the next element (or elements) in an alternate reading order of content, overriding the general default reading order at the user's discretion. Reflects the [aria-flowto](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-flowto) attribute.

[Element.ariaLabelledByElements](/en-US/docs/Web/API/Element/ariaLabelledByElements)

An array of elements that provide the accessible name for the element it is applied to. Reflects the [aria-labelledby](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-labelledby) attribute.

[Element.ariaOwnsElements](/en-US/docs/Web/API/Element/ariaOwnsElements)

An array of elements owned by the element this is applied to. This is used to define a visual, functional, or contextual relationship between a parent and its child elements when the DOM hierarchy cannot be used to represent the relationship. Reflects the [aria-owns](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-owns) attribute.

## [Instance methods](#instance_methods)

`Element` inherits methods from its parents [Node](/en-US/docs/Web/API/Node), and its own parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[Element.after()](/en-US/docs/Web/API/Element/after)

Inserts a set of [Node](/en-US/docs/Web/API/Node) objects or strings in the children list of the `Element`'s parent, just after the `Element`.

[Element.animate()](/en-US/docs/Web/API/Element/animate)

A shortcut method to create and run an animation on an element. Returns the created Animation object instance.

[Element.ariaNotify()](/en-US/docs/Web/API/Element/ariaNotify)ExperimentalNon-standard

Specifies that a given string of text should be announced by a screen reader.

[Element.append()](/en-US/docs/Web/API/Element/append)

Inserts a set of [Node](/en-US/docs/Web/API/Node) objects or strings after the last child of the element.

[Element.attachShadow()](/en-US/docs/Web/API/Element/attachShadow)

Attaches a shadow DOM tree to the specified element and returns a reference to its [ShadowRoot](/en-US/docs/Web/API/ShadowRoot).

[Element.before()](/en-US/docs/Web/API/Element/before)

Inserts a set of [Node](/en-US/docs/Web/API/Node) objects or strings in the children list of the `Element`'s parent, just before the `Element`.

[Element.checkVisibility()](/en-US/docs/Web/API/Element/checkVisibility)

Returns whether an element is expected to be visible or not based on configurable checks.

[Element.closest()](/en-US/docs/Web/API/Element/closest)

Returns the `Element` which is the closest ancestor of the current element (or the current element itself) which matches the selectors given in parameter.

[Element.computedStyleMap()](/en-US/docs/Web/API/Element/computedStyleMap)

Returns a [StylePropertyMapReadOnly](/en-US/docs/Web/API/StylePropertyMapReadOnly) interface which provides a read-only representation of a CSS declaration block that is an alternative to [CSSStyleDeclaration](/en-US/docs/Web/API/CSSStyleDeclaration).

[Element.getAnimations()](/en-US/docs/Web/API/Element/getAnimations)

Returns an array of Animation objects currently active on the element.

[Element.getAttribute()](/en-US/docs/Web/API/Element/getAttribute)

Retrieves the value of the named attribute from the current node and returns it as a string.

[Element.getAttributeNames()](/en-US/docs/Web/API/Element/getAttributeNames)

Returns an array of attribute names from the current element.

[Element.getAttributeNode()](/en-US/docs/Web/API/Element/getAttributeNode)

Retrieves the node representation of the named attribute from the current node and returns it as an [Attr](/en-US/docs/Web/API/Attr).

[Element.getAttributeNodeNS()](/en-US/docs/Web/API/Element/getAttributeNodeNS)

Retrieves the node representation of the attribute with the specified name and namespace, from the current node and returns it as an [Attr](/en-US/docs/Web/API/Attr).

[Element.getAttributeNS()](/en-US/docs/Web/API/Element/getAttributeNS)

Retrieves the value of the attribute with the specified namespace and name from the current node and returns it as a string.

[Element.getBoundingClientRect()](/en-US/docs/Web/API/Element/getBoundingClientRect)

Returns the size of an element and its position relative to the viewport.

`Element.getBoxQuads()`Experimental

Returns a list of [DOMQuad](/en-US/docs/Web/API/DOMQuad) objects representing the CSS fragments of the node.

[Element.getClientRects()](/en-US/docs/Web/API/Element/getClientRects)

Returns a collection of rectangles that indicate the bounding rectangles for each line of text in a client.

[Element.getElementsByClassName()](/en-US/docs/Web/API/Element/getElementsByClassName)

Returns a live [HTMLCollection](/en-US/docs/Web/API/HTMLCollection) that contains all descendants of the current element that possess the list of classes given in the parameter.

[Element.getElementsByTagName()](/en-US/docs/Web/API/Element/getElementsByTagName)

Returns a live [HTMLCollection](/en-US/docs/Web/API/HTMLCollection) containing all descendant elements, of a particular tag name, from the current element.

[Element.getElementsByTagNameNS()](/en-US/docs/Web/API/Element/getElementsByTagNameNS)

Returns a live [HTMLCollection](/en-US/docs/Web/API/HTMLCollection) containing all descendant elements, of a particular tag name and namespace, from the current element.

[Element.getHTML()](/en-US/docs/Web/API/Element/getHTML)

Returns the DOM content of the element as an HTML string, optionally including any shadow DOM.

[Element.hasAttribute()](/en-US/docs/Web/API/Element/hasAttribute)

Returns a boolean value indicating if the element has the specified attribute or not.

[Element.hasAttributeNS()](/en-US/docs/Web/API/Element/hasAttributeNS)

Returns a boolean value indicating if the element has the specified attribute, in the specified namespace, or not.

[Element.hasAttributes()](/en-US/docs/Web/API/Element/hasAttributes)

Returns a boolean value indicating if the element has one or more HTML attributes present.

[Element.hasPointerCapture()](/en-US/docs/Web/API/Element/hasPointerCapture)

Indicates whether the element on which it is invoked has pointer capture for the pointer identified by the given pointer ID.

[Element.insertAdjacentElement()](/en-US/docs/Web/API/Element/insertAdjacentElement)

Inserts a given element node at a given position relative to the element it is invoked upon.

[Element.insertAdjacentHTML()](/en-US/docs/Web/API/Element/insertAdjacentHTML)

Parses the text as HTML or XML and inserts the resulting nodes into the tree in the position given.

[Element.insertAdjacentText()](/en-US/docs/Web/API/Element/insertAdjacentText)

Inserts a given text node at a given position relative to the element it is invoked upon.

[Element.matches()](/en-US/docs/Web/API/Element/matches)

Returns a boolean value indicating whether or not the element would be selected by the specified selector string.

[Element.moveBefore()](/en-US/docs/Web/API/Element/moveBefore)

Moves a given [Node](/en-US/docs/Web/API/Node) inside the invoking node as a direct child, before a given reference node, without removing and then inserting the node.

[Element.prepend()](/en-US/docs/Web/API/Element/prepend)

Inserts a set of [Node](/en-US/docs/Web/API/Node) objects or strings before the first child of the element.

[Element.querySelector()](/en-US/docs/Web/API/Element/querySelector)

Returns the first [Node](/en-US/docs/Web/API/Node) which matches the specified selector string relative to the element.

[Element.querySelectorAll()](/en-US/docs/Web/API/Element/querySelectorAll)

Returns a [NodeList](/en-US/docs/Web/API/NodeList) of nodes which match the specified selector string relative to the element.

[Element.releasePointerCapture()](/en-US/docs/Web/API/Element/releasePointerCapture)

Releases (stops) pointer capture that was previously set for a specific [PointerEvent](/en-US/docs/Web/API/PointerEvent).

[Element.remove()](/en-US/docs/Web/API/Element/remove)

Removes the element from the children list of its parent.

[Element.removeAttribute()](/en-US/docs/Web/API/Element/removeAttribute)

Removes the named attribute from the current node.

[Element.removeAttributeNode()](/en-US/docs/Web/API/Element/removeAttributeNode)

Removes the node representation of the named attribute from the current node.

[Element.removeAttributeNS()](/en-US/docs/Web/API/Element/removeAttributeNS)

Removes the attribute with the specified name and namespace, from the current node.

[Element.replaceChildren()](/en-US/docs/Web/API/Element/replaceChildren)

Replaces the existing children of a [Node](/en-US/docs/Web/API/Node) with a specified new set of children.

[Element.replaceWith()](/en-US/docs/Web/API/Element/replaceWith)

Replaces the element in the children list of its parent with a set of [Node](/en-US/docs/Web/API/Node) objects or strings.

[Element.requestFullscreen()](/en-US/docs/Web/API/Element/requestFullscreen)

Asynchronously asks the browser to make the element fullscreen.

[Element.requestPointerLock()](/en-US/docs/Web/API/Element/requestPointerLock)

Allows to asynchronously ask for the pointer to be locked on the given element.

[Element.scroll()](/en-US/docs/Web/API/Element/scroll)

Scrolls to a particular set of coordinates inside a given element.

[Element.scrollBy()](/en-US/docs/Web/API/Element/scrollBy)

Scrolls an element by the given amount.

[Element.scrollIntoView()](/en-US/docs/Web/API/Element/scrollIntoView)

Scrolls the page until the element gets into the view.

[Element.scrollIntoViewIfNeeded()](/en-US/docs/Web/API/Element/scrollIntoViewIfNeeded)Non-standard

Scrolls the current element into the visible area of the browser window if it's not already within the visible area of the browser window. Use the standard [Element.scrollIntoView()](/en-US/docs/Web/API/Element/scrollIntoView) instead.

[Element.scrollTo()](/en-US/docs/Web/API/Element/scrollTo)

Scrolls to a particular set of coordinates inside a given element.

[Element.setAttribute()](/en-US/docs/Web/API/Element/setAttribute)

Sets the value of a named attribute of the current node.

[Element.setAttributeNode()](/en-US/docs/Web/API/Element/setAttributeNode)

Sets the node representation of the named attribute from the current node.

[Element.setAttributeNodeNS()](/en-US/docs/Web/API/Element/setAttributeNodeNS)

Sets the node representation of the attribute with the specified name and namespace, from the current node.

[Element.setAttributeNS()](/en-US/docs/Web/API/Element/setAttributeNS)

Sets the value of the attribute with the specified name and namespace, from the current node.

[Element.setCapture()](/en-US/docs/Web/API/Element/setCapture)Non-standardDeprecated

Sets up mouse event capture, redirecting all mouse events to this element.

[Element.setHTML()](/en-US/docs/Web/API/Element/setHTML)Secure contextExperimental

Parses and [sanitizes](/en-US/docs/Web/API/HTML_Sanitizer_API) a string of HTML into a document fragment, which then replaces the element's original subtree in the DOM.

[Element.setHTMLUnsafe()](/en-US/docs/Web/API/Element/setHTMLUnsafe)

Parses a string of HTML into a document fragment, without sanitization, which then replaces the element's original subtree in the DOM. The HTML string may include declarative shadow roots, which would be parsed as template elements if the HTML was set using [Element.innerHTML](/en-US/docs/Web/API/Element/innerHTML).

[Element.setPointerCapture()](/en-US/docs/Web/API/Element/setPointerCapture)

Designates a specific element as the capture target of future [pointer events](/en-US/docs/Web/API/Pointer_events).

[Element.toggleAttribute()](/en-US/docs/Web/API/Element/toggleAttribute)

Toggles a boolean attribute, removing it if it is present and adding it if it is not present, on the specified element.

## [Events](#events)

Listen to these events using `addEventListener()` or by assigning an event listener to the `oneventname` property of this interface.

[afterscriptexecute](/en-US/docs/Web/API/Element/afterscriptexecute_event)Non-standardDeprecated

Fired when a script has been executed.

[beforeinput](/en-US/docs/Web/API/Element/beforeinput_event)

Fired when the value of an input element is about to be modified.

[beforematch](/en-US/docs/Web/API/Element/beforematch_event)

Fires on an element that is in the [hidden until found](/en-US/docs/Web/HTML/Reference/Global_attributes/hidden) state, when the browser is about to reveal its content because the user has found the content through the "find in page" feature or through fragment navigation.

[beforescriptexecute](/en-US/docs/Web/API/Element/beforescriptexecute_event)Non-standardDeprecated

Fired when a script is about to be executed.

[beforexrselect](/en-US/docs/Web/API/Element/beforexrselect_event)Experimental

Fired before WebXR select events ([select](/en-US/docs/Web/API/XRSession/select_event), [selectstart](/en-US/docs/Web/API/XRSession/selectstart_event), [selectend](/en-US/docs/Web/API/XRSession/selectend_event)) are dispatched.

[contentvisibilityautostatechange](/en-US/docs/Web/API/Element/contentvisibilityautostatechange_event)

Fires on any element with [content-visibility: auto](/en-US/docs/Web/CSS/Reference/Properties/content-visibility) set on it when it starts or stops being [relevant to the user](/en-US/docs/Web/CSS/Guides/Containment/Using#relevant_to_the_user) and [skipping its contents](/en-US/docs/Web/CSS/Guides/Containment/Using#skips_its_contents).

[input](/en-US/docs/Web/API/Element/input_event)

Fires when an element's value is changed as a direct result of a user action.

[securitypolicyviolation](/en-US/docs/Web/API/Element/securitypolicyviolation_event)

Fired when a [Content Security Policy](/en-US/docs/Web/HTTP/Guides/CSP) is violated.

[wheel](/en-US/docs/Web/API/Element/wheel_event)

Fired when the user rotates a wheel button on a pointing device (typically a mouse).

### [Animation events](#animation_events)

[animationcancel](/en-US/docs/Web/API/Element/animationcancel_event)

Fired when an animation unexpectedly aborts.

[animationend](/en-US/docs/Web/API/Element/animationend_event)

Fired when an animation has completed normally.

[animationiteration](/en-US/docs/Web/API/Element/animationiteration_event)

Fired when an animation iteration has completed.

[animationstart](/en-US/docs/Web/API/Element/animationstart_event)

Fired when an animation starts.

### [Clipboard events](#clipboard_events)

[copy](/en-US/docs/Web/API/Element/copy_event)

Fired when the user initiates a copy action through the browser's user interface.

[cut](/en-US/docs/Web/API/Element/cut_event)

Fired when the user initiates a cut action through the browser's user interface.

[paste](/en-US/docs/Web/API/Element/paste_event)

Fired when the user initiates a paste action through the browser's user interface.

### [Composition events](#composition_events)

[compositionend](/en-US/docs/Web/API/Element/compositionend_event)

Fired when a text composition system such as an [input method editor](/en-US/docs/Glossary/Input_method_editor) completes or cancels the current composition session.

[compositionstart](/en-US/docs/Web/API/Element/compositionstart_event)

Fired when a text composition system such as an [input method editor](/en-US/docs/Glossary/Input_method_editor) starts a new composition session.

[compositionupdate](/en-US/docs/Web/API/Element/compositionupdate_event)

Fired when a new character is received in the context of a text composition session controlled by a text composition system such as an [input method editor](/en-US/docs/Glossary/Input_method_editor).

### [Focus events](#focus_events)

[blur](/en-US/docs/Web/API/Element/blur_event)

Fired when an element has lost focus.

[focus](/en-US/docs/Web/API/Element/focus_event)

Fired when an element has gained focus.

[focusin](/en-US/docs/Web/API/Element/focusin_event)

Fired when an element has gained focus, after [focus](/en-US/docs/Web/API/Element/focus_event).

[focusout](/en-US/docs/Web/API/Element/focusout_event)

Fired when an element has lost focus, after [blur](/en-US/docs/Web/API/Element/blur_event).

### [Fullscreen events](#fullscreen_events)

[fullscreenchange](/en-US/docs/Web/API/Element/fullscreenchange_event)

Sent to an `Element` when it transitions into or out of [fullscreen](/en-US/docs/Web/API/Fullscreen_API/Guide) mode.

[fullscreenerror](/en-US/docs/Web/API/Element/fullscreenerror_event)

Sent to an `Element` if an error occurs while attempting to switch it into or out of [fullscreen](/en-US/docs/Web/API/Fullscreen_API/Guide) mode.

### [Keyboard events](#keyboard_events)

[keydown](/en-US/docs/Web/API/Element/keydown_event)

Fired when a key is pressed.

[keypress](/en-US/docs/Web/API/Element/keypress_event)Deprecated

Fired when a key that produces a character value is pressed down.

[keyup](/en-US/docs/Web/API/Element/keyup_event)

Fired when a key is released.

### [Mouse events](#mouse_events)

[auxclick](/en-US/docs/Web/API/Element/auxclick_event)

Fired when a non-primary pointing device button (e.g., any mouse button other than the left button) has been pressed and released on an element.

[click](/en-US/docs/Web/API/Element/click_event)

Fired when a pointing device button (e.g., a mouse's primary button) is pressed and released on a single element.

[contextmenu](/en-US/docs/Web/API/Element/contextmenu_event)

Fired when the user attempts to open a context menu.

[dblclick](/en-US/docs/Web/API/Element/dblclick_event)

Fired when a pointing device button (e.g., a mouse's primary button) is clicked twice on a single element.

[DOMActivate](/en-US/docs/Web/API/Element/DOMActivate_event)Deprecated

Occurs when an element is activated, for instance, through a mouse click or a keypress.

[DOMMouseScroll](/en-US/docs/Web/API/Element/DOMMouseScroll_event)DeprecatedNon-standard

Occurs when mouse wheel or similar device is operated and the accumulated scroll amount is over 1 line or 1 page since last event.

[mousedown](/en-US/docs/Web/API/Element/mousedown_event)

Fired when a pointing device button is pressed on an element.

[mouseenter](/en-US/docs/Web/API/Element/mouseenter_event)

Fired when a pointing device (usually a mouse) is moved over the element that has the listener attached.

[mouseleave](/en-US/docs/Web/API/Element/mouseleave_event)

Fired when the pointer of a pointing device (usually a mouse) is moved out of an element that has the listener attached to it.

[mousemove](/en-US/docs/Web/API/Element/mousemove_event)

Fired when a pointing device (usually a mouse) is moved while over an element.

[mouseout](/en-US/docs/Web/API/Element/mouseout_event)

Fired when a pointing device (usually a mouse) is moved off the element to which the listener is attached or off one of its children.

[mouseover](/en-US/docs/Web/API/Element/mouseover_event)

Fired when a pointing device is moved onto the element to which the listener is attached or onto one of its children.

[mouseup](/en-US/docs/Web/API/Element/mouseup_event)

Fired when a pointing device button is released on an element.

[mousewheel](/en-US/docs/Web/API/Element/mousewheel_event)DeprecatedNon-standard

Fired when a mouse wheel or similar device is operated.

[MozMousePixelScroll](/en-US/docs/Web/API/Element/MozMousePixelScroll_event)DeprecatedNon-standard

Fired when a mouse wheel or similar device is operated.

[webkitmouseforcechanged](/en-US/docs/Web/API/Element/webkitmouseforcechanged_event)Non-standard

Fired each time the amount of pressure changes on the trackpad touch screen.

[webkitmouseforcedown](/en-US/docs/Web/API/Element/webkitmouseforcedown_event)Non-standard

Fired after the mousedown event as soon as sufficient pressure has been applied to qualify as a "force click".

[webkitmouseforcewillbegin](/en-US/docs/Web/API/Element/webkitmouseforcewillbegin_event)Non-standard

Fired before the [mousedown](/en-US/docs/Web/API/Element/mousedown_event) event.

[webkitmouseforceup](/en-US/docs/Web/API/Element/webkitmouseforceup_event)Non-standard

Fired after the [webkitmouseforcedown](/en-US/docs/Web/API/Element/webkitmouseforcedown_event) event as soon as the pressure has been reduced sufficiently to end the "force click".

### [Pointer events](#pointer_events)

[gotpointercapture](/en-US/docs/Web/API/Element/gotpointercapture_event)

Fired when an element captures a pointer using [setPointerCapture()](/en-US/docs/Web/API/Element/setPointerCapture).

[lostpointercapture](/en-US/docs/Web/API/Element/lostpointercapture_event)

Fired when a [captured pointer](/en-US/docs/Web/API/Pointer_events#pointer_capture) is released.

[pointercancel](/en-US/docs/Web/API/Element/pointercancel_event)

Fired when a pointer event is canceled.

[pointerdown](/en-US/docs/Web/API/Element/pointerdown_event)

Fired when a pointer becomes active.

[pointerenter](/en-US/docs/Web/API/Element/pointerenter_event)

Fired when a pointer is moved into the hit test boundaries of an element or one of its descendants.

[pointerleave](/en-US/docs/Web/API/Element/pointerleave_event)

Fired when a pointer is moved out of the hit test boundaries of an element.

[pointermove](/en-US/docs/Web/API/Element/pointermove_event)

Fired when a pointer changes coordinates.

[pointerout](/en-US/docs/Web/API/Element/pointerout_event)

Fired when a pointer is moved out of the hit test boundaries of an element (among other reasons).

[pointerover](/en-US/docs/Web/API/Element/pointerover_event)

Fired when a pointer is moved into an element's hit test boundaries.

[pointerrawupdate](/en-US/docs/Web/API/Element/pointerrawupdate_event)

Fired when a pointer changes any properties that don't fire [pointerdown](/en-US/docs/Web/API/Element/pointerdown_event) or [pointerup](/en-US/docs/Web/API/Element/pointerup_event) events.

[pointerup](/en-US/docs/Web/API/Element/pointerup_event)

Fired when a pointer is no longer active.

### [Scroll events](#scroll_events)

[scroll](/en-US/docs/Web/API/Element/scroll_event)

Fired when the document view or an element has been scrolled.

[scrollend](/en-US/docs/Web/API/Element/scrollend_event)

Fires when the document view has completed scrolling.

[scrollsnapchange](/en-US/docs/Web/API/Element/scrollsnapchange_event)Experimental

Fired on the scroll container at the end of a scrolling operation when a new scroll snap target has been selected.

[scrollsnapchanging](/en-US/docs/Web/API/Element/scrollsnapchanging_event)Experimental

Fired on the scroll container when the browser determines a new scroll snap target is pending, i.e., it will be selected when the current scroll gesture ends.

### [Touch events](#touch_events)

[gesturechange](/en-US/docs/Web/API/Element/gesturechange_event)Non-standard

Fired when digits move during a touch gesture.

[gestureend](/en-US/docs/Web/API/Element/gestureend_event)Non-standard

Fired when there are no longer multiple fingers contacting the touch surface, thus ending the gesture.

[gesturestart](/en-US/docs/Web/API/Element/gesturestart_event)Non-standard

Fired when multiple fingers contact the touch surface, thus starting a new gesture.

[touchcancel](/en-US/docs/Web/API/Element/touchcancel_event)

Fired when one or more touch points have been disrupted in an implementation-specific manner (for example, too many touch points are created).

[touchend](/en-US/docs/Web/API/Element/touchend_event)

Fired when one or more touch points are removed from the touch surface.

[touchmove](/en-US/docs/Web/API/Element/touchmove_event)

Fired when one or more touch points are moved along the touch surface.

[touchstart](/en-US/docs/Web/API/Element/touchstart_event)

Fired when one or more touch points are placed on the touch surface.

### [Transition events](#transition_events)

[transitioncancel](/en-US/docs/Web/API/Element/transitioncancel_event)

An [Event](/en-US/docs/Web/API/Event) fired when a [CSS transition](/en-US/docs/Web/CSS/Guides/Transitions) has been cancelled.

[transitionend](/en-US/docs/Web/API/Element/transitionend_event)

An [Event](/en-US/docs/Web/API/Event) fired when a [CSS transition](/en-US/docs/Web/CSS/Guides/Transitions) has finished playing.

[transitionrun](/en-US/docs/Web/API/Element/transitionrun_event)

An [Event](/en-US/docs/Web/API/Event) fired when a [CSS transition](/en-US/docs/Web/CSS/Guides/Transitions) is created (i.e., when it is added to a set of running transitions), though not necessarily started.

[transitionstart](/en-US/docs/Web/API/Element/transitionstart_event)

An [Event](/en-US/docs/Web/API/Event) fired when a [CSS transition](/en-US/docs/Web/CSS/Guides/Transitions) has started transitioning.

## [Specifications](#specifications)

Specification
[DOM# interface-element](https://dom.spec.whatwg.org/#interface-element)
[Pointer Events# extensions-to-the-element-interface](https://w3c.github.io/pointerevents/#extensions-to-the-element-interface)
[Fullscreen API# api](https://fullscreen.spec.whatwg.org/#api)
[DOM Parsing and Serialization# extensions-to-the-element-interface](https://w3c.github.io/DOM-Parsing/#extensions-to-the-element-interface)
[CSSOM View Module# extension-to-the-element-interface](https://drafts.csswg.org/cssom-view/#extension-to-the-element-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Element/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/element/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Felement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Felement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
