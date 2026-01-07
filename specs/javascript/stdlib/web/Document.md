DOM Standardhttps://whatwg.org/

# DOM

Living Standard — Last Updated 15 December 2025

Participate: [GitHub whatwg/dom](https://github.com/whatwg/dom) ([new issue](https://github.com/whatwg/dom/issues/new/choose), [open issues](https://github.com/whatwg/dom/issues)) [Chat on Matrix](https://whatwg.org/chat)Commits: [GitHub whatwg/dom/commits](https://github.com/whatwg/dom/commits)[Snapshot as of this commit](/commit-snapshots/8c4de13362ec502b668cc74d3281c233fcdbc399/)[@thedomstandard](https://twitter.com/thedomstandard)Tests: [web-platform-tests dom/](https://github.com/web-platform-tests/wpt/tree/master/dom) ([ongoing work](https://github.com/web-platform-tests/wpt/labels/dom)) Translations (non-normative): [日本語](https://triple-underscore.github.io/DOM4-ja.html)[简体中文](https://htmlspecs.com/dom/)[한국어](https://ko.htmlspecs.com/dom/)

## Abstract

DOM defines a platform-neutral model for events, aborting activities, and node trees.

## Table of Contents

1. [1 Infrastructure](#infrastructure)

  1. [1.1 Trees](#trees)
  2. [1.2 Ordered sets](#ordered-sets)
  3. [1.3 Selectors](#selectors)
  4. [1.4 Name validation](#namespaces)

2. [2 Events](#events)

  1. [2.1 Introduction to "DOM Events"](#introduction-to-dom-events)
  2. [2.2 Interface Event](#interface-event)
  3. [2.3 Legacy extensions to the Window interface](#interface-window-extensions)
  4. [2.4 Interface CustomEvent](#interface-customevent)
  5. [2.5 Constructing events](#constructing-events)
  6. [2.6 Defining event interfaces](#defining-event-interfaces)
  7. [2.7 Interface EventTarget](#interface-eventtarget)
  8. [2.8 Observing event listeners](#observing-event-listeners)
  9. [2.9 Dispatching events](#dispatching-events)
  10. [2.10 Firing events](#firing-events)
  11. [2.11 Action versus occurrence](#action-versus-occurrence)

3. [3 Aborting ongoing activities](#aborting-ongoing-activities)

  1. [3.1 Interface AbortController](#interface-abortcontroller)
  2. [3.2 Interface AbortSignal](#interface-AbortSignal)

    1. [3.2.1 Garbage collection](#abort-signal-garbage-collection)

  3. [3.3 Using AbortController and AbortSignal objects in
APIs](#abortcontroller-api-integration)

4. [4 Nodes](#nodes)

  1. [4.1 Introduction to "The DOM"](#introduction-to-the-dom)
  2. [4.2 Node tree](#node-trees)

    1. [4.2.1 Document tree](#document-trees)
    2. [4.2.2 Shadow tree](#shadow-trees)

      1. [4.2.2.1 Slots](#shadow-tree-slots)
      2. [4.2.2.2 Slottables](#light-tree-slotables)
      3. [4.2.2.3 Finding slots and slottables](#finding-slots-and-slotables)
      4. [4.2.2.4 Assigning slottables and slots](#assigning-slotables-and-slots)
      5. [4.2.2.5 Signaling slot change](#signaling-slot-change)

    3. [4.2.3 Mutation algorithms](#mutation-algorithms)
    4. [4.2.4 Mixin NonElementParentNode](#interface-nonelementparentnode)
    5. [4.2.5 Mixin DocumentOrShadowRoot](#mixin-documentorshadowroot)
    6. [4.2.6 Mixin ParentNode](#interface-parentnode)
    7. [4.2.7 Mixin NonDocumentTypeChildNode](#interface-nondocumenttypechildnode)
    8. [4.2.8 Mixin ChildNode](#interface-childnode)
    9. [4.2.9 Mixin Slottable](#mixin-slotable)
    10. [4.2.10 Old-style collections: NodeList and HTMLCollection](#old-style-collections)

      1. [4.2.10.1 Interface NodeList](#interface-nodelist)
      2. [4.2.10.2 Interface HTMLCollection](#interface-htmlcollection)

  3. [4.3 Mutation observers](#mutation-observers)

    1. [4.3.1 Interface MutationObserver](#interface-mutationobserver)
    2. [4.3.2 Queuing a mutation record](#queueing-a-mutation-record)
    3. [4.3.3 Interface MutationRecord](#interface-mutationrecord)

  4. [4.4 Interface Node](#interface-node)
  5. [4.5 Interface Document](#interface-document)

    1. [4.5.1 Interface DOMImplementation](#interface-domimplementation)

  6. [4.6 Interface DocumentType](#interface-documenttype)
  7. [4.7 Interface DocumentFragment](#interface-documentfragment)
  8. [4.8 Interface ShadowRoot](#interface-shadowroot)
  9. [4.9 Interface Element](#interface-element)

    1. [4.9.1 Interface NamedNodeMap](#interface-namednodemap)
    2. [4.9.2 Interface Attr](#interface-attr)

  10. [4.10 Interface CharacterData](#interface-characterdata)
  11. [4.11 Interface Text](#interface-text)
  12. [4.12 Interface CDATASection](#interface-cdatasection)
  13. [4.13 Interface ProcessingInstruction](#interface-processinginstruction)
  14. [4.14 Interface Comment](#interface-comment)

5. [5 Ranges](#ranges)

  1. [5.1 Introduction to "DOM Ranges"](#introduction-to-dom-ranges)
  2. [5.2 Boundary points](#boundary-points)
  3. [5.3 Interface AbstractRange](#interface-abstractrange)
  4. [5.4 Interface StaticRange](#interface-staticrange)
  5. [5.5 Interface Range](#interface-range)

6. [6 Traversal](#traversal)

  1. [6.1 Interface NodeIterator](#interface-nodeiterator)
  2. [6.2 Interface TreeWalker](#interface-treewalker)
  3. [6.3 Interface NodeFilter](#interface-nodefilter)

7. [7 Sets](#sets)

  1. [7.1 Interface DOMTokenList](#interface-domtokenlist)

8. [8 XPath](#xpath)

  1. [8.1 Interface XPathResult](#interface-xpathresult)
  2. [8.2 Interface XPathExpression](#interface-xpathexpression)
  3. [8.3 Mixin XPathEvaluatorBase](#mixin-xpathevaluatorbase)
  4. [8.4 Interface XPathEvaluator](#interface-xpathevaluator)

9. [9 XSLT](#xslt)

  1. [9.1 Interface XSLTProcessor](#interface-xsltprocessor)

10. [10 Security and privacy considerations](#security-and-privacy)
11. [11 Historical](#historical)
12. [Acknowledgments](#acks)
13. [Intellectual property rights](#ipr)
14. [Index](#index)

  1. [Terms defined by this specification](#index-defined-here)
  2. [Terms defined by reference](#index-defined-elsewhere)

15. [References](#references)

  1. [Normative References](#normative)
  2. [Informative References](#informative)

16. [IDL Index](#idl-index)

## 1. Infrastructure#infrastructure

This specification depends on the Infra Standard. [[INFRA]](#biblio-infra)

Some of the terms used in this specification are defined in Encoding, Selectors, Trusted Types, Web IDL, XML, and Namespaces in XML. [[ENCODING]](#biblio-encoding)[[SELECTORS4]](#biblio-selectors4)[[TRUSTED-TYPES]](#biblio-trusted-types)[[WEBIDL]](#biblio-webidl)[[XML]](#biblio-xml)[[XML-NAMES]](#biblio-xml-names)

When extensions are needed, the DOM Standard can be updated accordingly, or a new standard can be written that hooks into the provided extensibility hooks for applicable specifications. 

### 1.1. Trees#trees

A tree is a finite hierarchical tree structure. In tree order is preorder, depth-first traversal of a [tree](#concept-tree). 

An object that participates in a [tree](#concept-tree) has a parent, which is either null or an object, and has children, which is an [ordered set](https://infra.spec.whatwg.org/#ordered-set) of objects. An object A whose [parent](#concept-tree-parent) is object B is a [child](#concept-tree-child) of B. 

The root of an object is itself, if its [parent](#concept-tree-parent) is null, or else it is the [root](#concept-tree-root) of its [parent](#concept-tree-parent). The [root](#concept-tree-root) of a [tree](#concept-tree) is any object [participating](#concept-tree-participate) in that [tree](#concept-tree) whose [parent](#concept-tree-parent) is null. 

An object A is called a descendant of an object B, if either A is a [child](#concept-tree-child) of B or A is a [child](#concept-tree-child) of an object C that is a [descendant](#concept-tree-descendant) of B. 

An inclusive descendant is an object or one of its [descendants](#concept-tree-descendant). 

An object A is called an ancestor of an object B if and only if B is a [descendant](#concept-tree-descendant) of A. 

An inclusive ancestor is an object or one of its [ancestors](#concept-tree-ancestor). 

An object A is called a sibling of an object B, if and only if B and A share the same non-null [parent](#concept-tree-parent). 

An inclusive sibling is an object or one of its [siblings](#concept-tree-sibling). 

An object A is preceding an object B if A and B are in the same [tree](#concept-tree) and A comes before B in [tree order](#concept-tree-order). 

An object A is following an object B if A and B are in the same [tree](#concept-tree) and A comes after B in [tree order](#concept-tree-order). 

The first child of an object is its first [child](#concept-tree-child) or null if it has no [children](#concept-tree-child). 

The last child of an object is its last [child](#concept-tree-child) or null if it has no [children](#concept-tree-child). 

The previous sibling of an object is its first [preceding](#concept-tree-preceding)[sibling](#concept-tree-sibling) or null if it has no [preceding](#concept-tree-preceding)[sibling](#concept-tree-sibling). 

The next sibling of an object is its first [following](#concept-tree-following)[sibling](#concept-tree-sibling) or null if it has no [following](#concept-tree-following)[sibling](#concept-tree-sibling). 

The index of an object is its number of [preceding](#concept-tree-preceding)[siblings](#concept-tree-sibling), or 0 if it has none. 

### 1.2. Ordered sets#ordered-sets

The ordered set parser takes a string input and then runs these steps: 

1. 

Let inputTokens be the result of [splitting input on ASCII whitespace](https://infra.spec.whatwg.org/#split-on-ascii-whitespace). 

2. 

Let tokens be a new [ordered set](https://infra.spec.whatwg.org/#ordered-set). 

3. 

[For each](https://infra.spec.whatwg.org/#list-iterate)token of inputTokens: [append](https://infra.spec.whatwg.org/#set-append)token to tokens. 

4. Return tokens. 

The ordered set serializer takes a set and returns the [concatenation](https://infra.spec.whatwg.org/#string-concatenate) of set using U+0020 SPACE. 

### 1.3. Selectors#selectors

To scope-match a selectors string given a string selectors against a [node](#concept-node)node: 

1. 

Let selector be the result of [parse a selector](https://drafts.csswg.org/selectors-4/#parse-a-selector)selectors. [[SELECTORS4]](#biblio-selectors4)

2. 

If selector is failure, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[SyntaxError](https://webidl.spec.whatwg.org/#syntaxerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

Return the result of [match a selector against a tree](https://drafts.csswg.org/selectors-4/#match-a-selector-against-a-tree) with selector and node’s [root](#concept-tree-root) using [scoping root](https://drafts.csswg.org/selectors-4/#scoping-root)node. [[SELECTORS4]](#biblio-selectors4). 

Support for namespaces within selectors is not planned and will not be added. 

### 1.4. Name validation#namespaces

A [string](https://infra.spec.whatwg.org/#string) is a valid namespace prefix if its [length](https://infra.spec.whatwg.org/#string-length) is at least 1 and it does not contain [ASCII whitespace](https://infra.spec.whatwg.org/#ascii-whitespace), U+0000 NULL, U+002F (/), or U+003E (>). 

A [string](https://infra.spec.whatwg.org/#string) is a valid attribute local name if its [length](https://infra.spec.whatwg.org/#string-length) is at least 1 and it does not contain [ASCII whitespace](https://infra.spec.whatwg.org/#ascii-whitespace), U+0000 NULL, U+002F (/), U+003D (=), or U+003E (>). 

A [string](https://infra.spec.whatwg.org/#string)name is a valid element local name if the following steps return true: 

1. 

If name’s [length](https://infra.spec.whatwg.org/#string-length) is 0, then return false. 

2. 

If name’s 0th [code point](https://infra.spec.whatwg.org/#code-point) is an [ASCII alpha](https://infra.spec.whatwg.org/#ascii-alpha): 

  1. 

If name contains [ASCII whitespace](https://infra.spec.whatwg.org/#ascii-whitespace), U+0000 NULL, U+002F (/), or U+003E (>), then return false. 

  2. 

Return true. 

3. 

If name’s 0th [code point](https://infra.spec.whatwg.org/#code-point) is not U+003A (:), U+005F (_), or in the range U+0080 to U+10FFFF, inclusive, then return false. 

4. 

If name’s subsequent [code points](https://infra.spec.whatwg.org/#code-point), if any, are not [ASCII alphas](https://infra.spec.whatwg.org/#ascii-alpha), [ASCII digits](https://infra.spec.whatwg.org/#ascii-digit), U+002D (-), U+002E (.), U+003A (:), U+005F (_), or in the range U+0080 to U+10FFFF, inclusive, then return false. 

5. 

Return true. 

This concept is used to validate [element](#concept-element)[local names](#concept-element-local-name), when constructed by DOM APIs. The intention is to allow any name that is possible to construct using the HTML parser (the branch where the first [code point](https://infra.spec.whatwg.org/#code-point) is an [ASCII alpha](https://infra.spec.whatwg.org/#ascii-alpha)), plus some additional possibilities. For those additional possibilities, the ASCII range is restricted for historical reasons, but beyond ASCII anything is allowed. 

The following JavaScript-compatible regular expression is an implementation of [valid element local name](#valid-element-local-name): 

```
/^(?:[A-Za-z][^\0\t\n\f\r\u0020/>]*|[:_\u0080-\u{10FFFF}][A-Za-z0-9-.:_\u0080-\u{10FFFF}]*)$/u
```

A [string](https://infra.spec.whatwg.org/#string) is a valid doctype name if it does not contain [ASCII whitespace](https://infra.spec.whatwg.org/#ascii-whitespace), U+0000 NULL, or U+003E (>). 

The empty string is a [valid doctype name](#valid-doctype-name). 

To validate and extract a namespace and qualifiedName, given a context: 

1. 

If namespace is the empty string, then set it to null. 

2. 

Let prefix be null. 

3. 

Let localName be qualifiedName. 

4. 

If qualifiedName contains a U+003A (:): 

  1. 

Let splitResult be the result of running [strictly split](https://infra.spec.whatwg.org/#strictly-split) given qualifiedName and U+003A (:). 

  2. 

Set prefix to splitResult[0]. 

  3. 

Set localName to splitResult[1]. 

  4. 

If prefix is not a [valid namespace prefix](#valid-namespace-prefix), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidCharacterError](https://webidl.spec.whatwg.org/#invalidcharactererror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

5. 

[Assert](https://infra.spec.whatwg.org/#assert): prefix is either null or a [valid namespace prefix](#valid-namespace-prefix). 

6. 

If context is "`attribute`" and localName is not a [valid attribute local name](#valid-attribute-local-name), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidCharacterError](https://webidl.spec.whatwg.org/#invalidcharactererror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

7. 

If context is "`element`" and localName is not a [valid element local name](#valid-element-local-name), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidCharacterError](https://webidl.spec.whatwg.org/#invalidcharactererror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

8. 

If prefix is non-null and namespace is null, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NamespaceError](https://webidl.spec.whatwg.org/#namespaceerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

9. 

If prefix is "`xml`" and namespace is not the [XML namespace](https://infra.spec.whatwg.org/#xml-namespace), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NamespaceError](https://webidl.spec.whatwg.org/#namespaceerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

10. 

If either qualifiedName or prefix is "`xmlns`" and namespace is not the [XMLNS namespace](https://infra.spec.whatwg.org/#xmlns-namespace), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NamespaceError](https://webidl.spec.whatwg.org/#namespaceerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

11. 

If namespace is the [XMLNS namespace](https://infra.spec.whatwg.org/#xmlns-namespace) and neither qualifiedName nor prefix is "`xmlns`", then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NamespaceError](https://webidl.spec.whatwg.org/#namespaceerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

12. 

Return (namespace, prefix, localName). 

Various APIs in this specification used to validate namespace prefixes, attribute local names, element local names, and doctype names more strictly. This was done in a way that aligned with various XML-related specifications. (Although not all rules from the those specifications were enforced.) 

This was found to be annoying for web developers, especially since it meant there were some names that could be created by the HTML parser, but not by DOM APIs. So, the validations have been loosened to just those described above. 

## 2. Events#events

### 2.1. Introduction to "DOM Events"#introduction-to-dom-events

Throughout the web platform [events](#concept-event) are [dispatched](#concept-event-dispatch) to objects to signal an occurrence, such as network activity or user interaction. These objects implement the [EventTarget](#eventtarget) interface and can therefore add [event listeners](#concept-event-listener) to observe [events](#concept-event) by calling [addEventListener()](#dom-eventtarget-addeventlistener):

```
obj.addEventListener("load", imgFetched)

function imgFetched(ev) {
  // great success
  …
}
```

[Event listeners](#concept-event-listener) can be removed by utilizing the [removeEventListener()](#dom-eventtarget-removeeventlistener) method, passing the same arguments.

Alternatively, [event listeners](#concept-event-listener) can be removed by passing an [AbortSignal](#abortsignal) to [addEventListener()](#dom-eventtarget-addeventlistener) and calling [abort()](#dom-abortcontroller-abort) on the controller owning the signal.

[Events](#concept-event) are objects too and implement the [Event](#event) interface (or a derived interface). In the example above ev is the [event](#concept-event). ev is passed as an argument to the [event listener](#concept-event-listener)’s [callback](#event-listener-callback) (typically a JavaScript Function as shown above). [Event listeners](#concept-event-listener) key off the [event](#concept-event)’s [type](#dom-event-type) attribute value ("`load`" in the above example). The [event](#concept-event)’s [target](#dom-event-target) attribute value returns the object to which the [event](#concept-event) was [dispatched](#concept-event-dispatch) (obj above).

Although [events](#concept-event) are typically [dispatched](#concept-event-dispatch) by the user agent as the result of user interaction or the completion of some task, applications can [dispatch](#concept-event-dispatch)[events](#concept-event) themselves by using what are commonly known as synthetic events: 

```
// add an appropriate event listener
obj.addEventListener("cat", function(e) { process(e.detail) })

// create and dispatch the event
var event = new CustomEvent("cat", {"detail":{"hazcheeseburger":true}})
obj.dispatchEvent(event)
```

Apart from signaling, [events](#concept-event) are sometimes also used to let an application control what happens next in an operation. For instance as part of form submission an [event](#concept-event) whose [type](#dom-event-type) attribute value is "`submit`" is [dispatched](#concept-event-dispatch). If this [event](#concept-event)’s [preventDefault()](#dom-event-preventdefault) method is invoked, form submission will be terminated. Applications who wish to make use of this functionality through [events](#concept-event)[dispatched](#concept-event-dispatch) by the application (synthetic events) can make use of the return value of the [dispatchEvent()](#dom-eventtarget-dispatchevent) method:

```
if(obj.dispatchEvent(event)) {
  // event was not canceled, time for some magic
  …
}
```

When an [event](#concept-event) is [dispatched](#concept-event-dispatch) to an object that [participates](#concept-tree-participate) in a [tree](#concept-tree) (e.g., an [element](#concept-element)), it can reach [event listeners](#concept-event-listener) on that object’s [ancestors](#concept-tree-ancestor) too. Effectively, all the object’s [inclusive ancestor](#concept-tree-inclusive-ancestor)[event listeners](#concept-event-listener) whose [capture](#event-listener-capture) is true are invoked, in [tree order](#concept-tree-order). And then, if [event](#concept-event)’s [bubbles](#dom-event-bubbles) is true, all the object’s [inclusive ancestor](#concept-tree-inclusive-ancestor)[event listeners](#concept-event-listener) whose [capture](#event-listener-capture) is false are invoked, now in reverse [tree order](#concept-tree-order). 

Let’s look at an example of how [events](#concept-event) work in a [tree](#concept-tree): 

```
<!doctype html>
<html>
 <head>
  <title>Boring example</title>
 </head>
 <body>
  <p>Hello <span id=x>world</span>!</p>
  <script>
   function test(e) {
     debug(e.target, e.currentTarget, e.eventPhase)
   }
   document.addEventListener("hey", test, {capture: true})
   document.body.addEventListener("hey", test)
   var ev = new Event("hey", {bubbles:true})
   document.getElementById("x").dispatchEvent(ev)
  </script>
 </body>
</html>
```

The `debug` function will be invoked twice. Each time the [event](#concept-event)’s [target](#dom-event-target) attribute value will be the `span`[element](#concept-element). The first time [currentTarget](#dom-event-currenttarget) attribute’s value will be the [document](#concept-document), the second time the `body`[element](#concept-element). [eventPhase](#dom-event-eventphase) attribute’s value switches from [CAPTURING_PHASE](#dom-event-capturing_phase) to [BUBBLING_PHASE](#dom-event-bubbling_phase). If an [event listener](#concept-event-listener) was registered for the `span`[element](#concept-element), [eventPhase](#dom-event-eventphase) attribute’s value would have been [AT_TARGET](#dom-event-at_target). 

### 2.2. Interface [Event](#event)#interface-event

```
[Exposed=*]
interface Event {
  constructor(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString type, optional EventInit#dictdef-eventinit eventInitDict = {});

  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString type#dom-event-type;
  readonly attribute EventTarget#eventtarget? target#dom-event-target;
  readonly attribute EventTarget#eventtarget? srcElement#dom-event-srcelement; // legacy
  readonly attribute EventTarget#eventtarget? currentTarget#dom-event-currenttarget;
  sequencehttps://webidl.spec.whatwg.org/#idl-sequence<EventTarget#eventtarget> composedPath#dom-event-composedpath();

  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short NONE#dom-event-none = 0;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short CAPTURING_PHASE#dom-event-capturing_phase = 1;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short AT_TARGET#dom-event-at_target = 2;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short BUBBLING_PHASE#dom-event-bubbling_phase = 3;
  readonly attribute unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short eventPhase#dom-event-eventphase;

  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined stopPropagation#dom-event-stoppropagation();
           attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean cancelBubble#dom-event-cancelbubble; // legacy alias of .stopPropagation()
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined stopImmediatePropagation#dom-event-stopimmediatepropagation();

  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean bubbles#dom-event-bubbles;
  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean cancelable#dom-event-cancelable;
           attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean returnValue#dom-event-returnvalue;  // legacy
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined preventDefault#dom-event-preventdefault();
  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean defaultPrevented#dom-event-defaultprevented;
  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean composed#dom-event-composed;

  [LegacyUnforgeablehttps://webidl.spec.whatwg.org/#LegacyUnforgeable] readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean isTrusted#dom-event-istrusted;
  readonly attribute DOMHighResTimeStamphttps://w3c.github.io/hr-time/#dom-domhighrestimestamp timeStamp#dom-event-timestamp;

  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined initEvent#dom-event-initevent(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString type, optional booleanhttps://webidl.spec.whatwg.org/#idl-boolean bubbles = false, optional booleanhttps://webidl.spec.whatwg.org/#idl-boolean cancelable = false); // legacy
};

dictionary EventInit {
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean bubbles = false;
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean cancelable = false;
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean composed = false;
};
```

An [Event](#event) object is simply named an event. It allows for signaling that something has occurred, e.g., that an image has completed downloading.

A potential event target is null or an [EventTarget](#eventtarget) object. 

An [event](#concept-event) has an associated target (a [potential event target](#potential-event-target)). Unless stated otherwise it is null. 

An [event](#concept-event) has an associated relatedTarget (a [potential event target](#potential-event-target)). Unless stated otherwise it is null. 

Other specifications use [relatedTarget](#event-relatedtarget) to define a `relatedTarget` attribute. [[UIEVENTS]](#biblio-uievents)

An [event](#concept-event) has an associated touch target list (a [list](https://infra.spec.whatwg.org/#list) of zero or more [potential event targets](#potential-event-target)). Unless stated otherwise it is the empty list. 

The [touch target list](#event-touch-target-list) is for the exclusive use of defining the [TouchEvent](https://w3c.github.io/touch-events/#idl-def-touchevent) interface and related interfaces. [[TOUCH-EVENTS]](#biblio-touch-events)

An [event](#concept-event) has an associated path. A [path](#event-path) is a [list](https://infra.spec.whatwg.org/#list) of [structs](https://infra.spec.whatwg.org/#struct). Each [struct](https://infra.spec.whatwg.org/#struct) consists of an invocation target (an [EventTarget](#eventtarget) object), an invocation-target-in-shadow-tree (a boolean), a shadow-adjusted target (a [potential event target](#potential-event-target)), a relatedTarget (a [potential event target](#potential-event-target)), a touch target list (a [list](https://infra.spec.whatwg.org/#list) of [potential event targets](#potential-event-target)), a root-of-closed-tree (a boolean), and a slot-in-closed-tree (a boolean). A [path](#event-path) is initially the empty list.

[Event](#dom-event-event)`event = new (type [, eventInitDict])`Returns a new event whose [type](#dom-event-type) attribute value is set to type. The eventInitDict argument allows for setting the [bubbles](#dom-event-bubbles) and [cancelable](#dom-event-cancelable) attributes via object members of the same name. [type](#dom-event-type)Returns the type of event, e.g. "`click`", "`hashchange`", or "`submit`". [target](#dom-event-target)Returns the object to which event is [dispatched](#concept-event-dispatch) (its [target](#event-target)). [currentTarget](#dom-event-currenttarget)Returns the object whose [event listener](#concept-event-listener)’s [callback](#event-listener-callback) is currently being invoked. [composedPath()](#dom-event-composedpath)Returns the [invocation target](#event-path-invocation-target) objects of event’s [path](#event-path) (objects on which listeners will be invoked), except for any [nodes](#concept-node) in [shadow trees](#concept-shadow-tree) of which the [shadow root](#concept-shadow-root)’s [mode](#shadowroot-mode) is "`closed`" that are not reachable from event’s [currentTarget](#dom-event-currenttarget). [eventPhase](#dom-event-eventphase)Returns the [event](#concept-event)’s phase, which is one of [NONE](#dom-event-none), [CAPTURING_PHASE](#dom-event-capturing_phase), [AT_TARGET](#dom-event-at_target), and [BUBBLING_PHASE](#dom-event-bubbling_phase). [stopPropagation](#dom-event-stoppropagation)`event . ()`When [dispatched](#concept-event-dispatch) in a [tree](#concept-tree), invoking this method prevents event from reaching any objects other than the current object. [stopImmediatePropagation](#dom-event-stopimmediatepropagation)`event . ()`Invoking this method prevents event from reaching any registered [event listeners](#concept-event-listener) after the current one finishes running and, when [dispatched](#concept-event-dispatch) in a [tree](#concept-tree), also prevents event from reaching any other objects. [bubbles](#dom-event-bubbles)Returns true or false depending on how event was initialized. True if event goes through its [target](#event-target)’s [ancestors](#concept-tree-ancestor) in reverse [tree order](#concept-tree-order); otherwise false. [cancelable](#dom-event-cancelable)Returns true or false depending on how event was initialized. Its return value does not always carry meaning, but true can indicate that part of the operation during which event was [dispatched](#concept-event-dispatch), can be canceled by invoking the [preventDefault()](#dom-event-preventdefault) method. [preventDefault](#dom-event-preventdefault)`event . ()`If invoked when the [cancelable](#dom-event-cancelable) attribute value is true, and while executing a listener for the event with [passive](#dom-addeventlisteneroptions-passive) set to false, signals to the operation that caused event to be [dispatched](#concept-event-dispatch) that it needs to be canceled. [defaultPrevented](#dom-event-defaultprevented)Returns true if [preventDefault()](#dom-event-preventdefault) was invoked successfully to indicate cancelation; otherwise false. [composed](#dom-event-composed)Returns true or false depending on how event was initialized. True if event invokes listeners past a [ShadowRoot](#shadowroot)[node](#concept-node) that is the [root](#concept-tree-root) of its [target](#event-target); otherwise false. [isTrusted](#dom-event-istrusted)Returns true if event was [dispatched](#concept-event-dispatch) by the user agent, and false otherwise. [timeStamp](#dom-event-timestamp)Returns the event’s timestamp as the number of milliseconds measured relative to the occurrence. 

The `type` attribute must return the value it was initialized to. When an [event](#concept-event) is created the attribute must be initialized to the empty string. 

The `target` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [target](#event-target). 

The `srcElement` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [target](#event-target). 

The `currentTarget` attribute must return the value it was initialized to. When an [event](#concept-event) is created the attribute must be initialized to null. 

The `composedPath()` method steps are: 

1. 

Let composedPath be an empty [list](https://infra.spec.whatwg.org/#list). 

2. 

Let path be [this](https://webidl.spec.whatwg.org/#this)’s [path](#event-path). 

3. 

If path[is empty](https://infra.spec.whatwg.org/#list-is-empty), then return composedPath. 

4. 

Let currentTarget be [this](https://webidl.spec.whatwg.org/#this)’s [currentTarget](#dom-event-currenttarget) attribute value. 

5. 

[Assert](https://infra.spec.whatwg.org/#assert): currentTarget is an [EventTarget](#eventtarget) object. 

6. 

[Append](https://infra.spec.whatwg.org/#list-append)currentTarget to composedPath. 

7. 

Let currentTargetIndex be 0. 

8. 

Let currentTargetHiddenSubtreeLevel be 0. 

9. 

Let index be path’s [size](https://infra.spec.whatwg.org/#list-size) − 1. 

10. 

While index is greater than or equal to 0: 

  1. 

If path[index]'s [root-of-closed-tree](#event-path-root-of-closed-tree) is true, then increase currentTargetHiddenSubtreeLevel by 1. 

  2. 

If path[index]'s [invocation target](#event-path-invocation-target) is currentTarget, then set currentTargetIndex to index and [break](https://infra.spec.whatwg.org/#iteration-break). 

  3. 

If path[index]'s [slot-in-closed-tree](#event-path-slot-in-closed-tree) is true, then decrease currentTargetHiddenSubtreeLevel by 1. 

  4. 

Decrease index by 1. 

11. 

Let currentHiddenLevel and maxHiddenLevel be currentTargetHiddenSubtreeLevel. 

12. 

Set index to currentTargetIndex − 1. 

13. 

While index is greater than or equal to 0: 

  1. 

If path[index]'s [root-of-closed-tree](#event-path-root-of-closed-tree) is true, then increase currentHiddenLevel by 1. 

  2. 

If currentHiddenLevel is less than or equal to maxHiddenLevel, then [prepend](https://infra.spec.whatwg.org/#list-prepend)path[index]'s [invocation target](#event-path-invocation-target) to composedPath. 

  3. 

If path[index]'s [slot-in-closed-tree](#event-path-slot-in-closed-tree) is true: 

    1. 

Decrease currentHiddenLevel by 1. 

    2. 

If currentHiddenLevel is less than maxHiddenLevel, then set maxHiddenLevel to currentHiddenLevel. 

  4. 

Decrease index by 1. 

14. 

Set currentHiddenLevel and maxHiddenLevel to currentTargetHiddenSubtreeLevel. 

15. 

Set index to currentTargetIndex + 1. 

16. 

While index is less than path’s [size](https://infra.spec.whatwg.org/#list-size): 

  1. 

If path[index]'s [slot-in-closed-tree](#event-path-slot-in-closed-tree) is true, then increase currentHiddenLevel by 1. 

  2. 

If currentHiddenLevel is less than or equal to maxHiddenLevel, then [append](https://infra.spec.whatwg.org/#list-append)path[index]'s [invocation target](#event-path-invocation-target) to composedPath. 

  3. 

If path[index]'s [root-of-closed-tree](#event-path-root-of-closed-tree) is true: 

    1. 

Decrease currentHiddenLevel by 1. 

    2. 

If currentHiddenLevel is less than maxHiddenLevel, then set maxHiddenLevel to currentHiddenLevel. 

  4. 

Increase index by 1. 

17. 

Return composedPath. 

The `eventPhase` attribute must return the value it was initialized to, which must be one of the following: 

`NONE` (numeric value 0) [Events](#concept-event) not currently [dispatched](#concept-event-dispatch) are in this phase. `CAPTURING_PHASE` (numeric value 1) When an [event](#concept-event) is [dispatched](#concept-event-dispatch) to an object that [participates](#concept-tree-participate) in a [tree](#concept-tree) it will be in this phase before it reaches its [target](#event-target). `AT_TARGET` (numeric value 2) When an [event](#concept-event) is [dispatched](#concept-event-dispatch) it will be in this phase on its [target](#event-target). `BUBBLING_PHASE` (numeric value 3) When an [event](#concept-event) is [dispatched](#concept-event-dispatch) to an object that [participates](#concept-tree-participate) in a [tree](#concept-tree) it will be in this phase after it reaches its [target](#event-target). 

Initially the attribute must be initialized to [NONE](#dom-event-none). 

Each [event](#concept-event) has the following associated flags that are all initially unset: 

- stop propagation flag
- stop immediate propagation flag
- canceled flag
- in passive listener flag
- composed flag
- initialized flag
- dispatch flag

The `stopPropagation()` method steps are to set [this](https://webidl.spec.whatwg.org/#this)’s [stop propagation flag](#stop-propagation-flag).

The `cancelBubble` getter steps are to return true if [this](https://webidl.spec.whatwg.org/#this)’s [stop propagation flag](#stop-propagation-flag) is set; otherwise false. 

The [cancelBubble](#dom-event-cancelbubble) setter steps are to set [this](https://webidl.spec.whatwg.org/#this)’s [stop propagation flag](#stop-propagation-flag) if the given value is true; otherwise do nothing. 

The `stopImmediatePropagation()` method steps are to set [this](https://webidl.spec.whatwg.org/#this)’s [stop propagation flag](#stop-propagation-flag) and [this](https://webidl.spec.whatwg.org/#this)’s [stop immediate propagation flag](#stop-immediate-propagation-flag). 

The `bubbles` and `cancelable` attributes must return the values they were initialized to. 

To set the canceled flag, given an [event](#concept-event)event, if event’s [cancelable](#dom-event-cancelable) attribute value is true and event’s [in passive listener flag](#in-passive-listener-flag) is unset, then set event’s [canceled flag](#canceled-flag), and do nothing otherwise. 

The `returnValue` getter steps are to return false if [this](https://webidl.spec.whatwg.org/#this)’s [canceled flag](#canceled-flag) is set; otherwise true. 

The [returnValue](#dom-event-returnvalue) setter steps are to [set the canceled flag](#set-the-canceled-flag) with [this](https://webidl.spec.whatwg.org/#this) if the given value is false; otherwise do nothing. 

The `preventDefault()` method steps are to [set the canceled flag](#set-the-canceled-flag) with [this](https://webidl.spec.whatwg.org/#this). 

There are scenarios where invoking [preventDefault()](#dom-event-preventdefault) has no effect. User agents are encouraged to log the precise cause in a developer console, to aid debugging. 

The `defaultPrevented` getter steps are to return true if [this](https://webidl.spec.whatwg.org/#this)’s [canceled flag](#canceled-flag) is set; otherwise false. 

The `composed` getter steps are to return true if [this](https://webidl.spec.whatwg.org/#this)’s [composed flag](#composed-flag) is set; otherwise false. 

The `isTrusted` attribute must return the value it was initialized to. When an [event](#concept-event) is created the attribute must be initialized to false. 

[isTrusted](#dom-event-istrusted) is a convenience that indicates whether an [event](#concept-event) is [dispatched](#concept-event-dispatch) by the user agent (as opposed to using [dispatchEvent()](#dom-eventtarget-dispatchevent)). The sole legacy exception is [click()](https://html.spec.whatwg.org/multipage/interaction.html#dom-click), which causes the user agent to dispatch an [event](#concept-event) whose [isTrusted](#dom-event-istrusted) attribute is initialized to false. 

The `timeStamp` attribute must return the value it was initialized to. 

To initialize an event, with type, bubbles, and cancelable, run these steps: 

1. 

Set event’s [initialized flag](#initialized-flag). 

2. 

Unset event’s [stop propagation flag](#stop-propagation-flag), [stop immediate propagation flag](#stop-immediate-propagation-flag), and [canceled flag](#canceled-flag). 

3. 

Set event’s [isTrusted](#dom-event-istrusted) attribute to false. 

4. 

Set event’s [target](#event-target) to null. 

5. 

Set event’s [type](#dom-event-type) attribute to type. 

6. 

Set event’s [bubbles](#dom-event-bubbles) attribute to bubbles. 

7. 

Set event’s [cancelable](#dom-event-cancelable) attribute to cancelable. 

The `initEvent(type, bubbles, cancelable)` method steps are: 

1. 

If [this](https://webidl.spec.whatwg.org/#this)’s [dispatch flag](#dispatch-flag) is set, then return. 

2. 

[Initialize](#concept-event-initialize)[this](https://webidl.spec.whatwg.org/#this) with type, bubbles, and cancelable. 

[initEvent()](#dom-event-initevent) is redundant with [event](#concept-event) constructors and incapable of setting [composed](#dom-event-composed). It has to be supported for legacy content. 

### 2.3. Legacy extensions to the [Window](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window) interface#interface-window-extensions

```
partial interface Windowhttps://html.spec.whatwg.org/multipage/nav-history-apis.html#window {
  [Replaceablehttps://webidl.spec.whatwg.org/#Replaceable] readonly attribute (Event#event or undefinedhttps://webidl.spec.whatwg.org/#idl-undefined) event#dom-window-event; // legacy
};
```

Each [Window](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window) object has an associated current event (undefined or an [Event](#event) object). Unless stated otherwise it is undefined. 

The `event` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [current event](#window-current-event). 

Web developers are strongly encouraged to instead rely on the [Event](#event) object passed to event listeners, as that will result in more portable code. This attribute is not available in workers or worklets, and is inaccurate for events dispatched in [shadow trees](#concept-shadow-tree). 

### 2.4. Interface [CustomEvent](#customevent)#interface-customevent

```
[Exposed=*]
interface CustomEvent : Event#event {
  constructor(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString type, optional CustomEventInit#dictdef-customeventinit eventInitDict = {});

  readonly attribute anyhttps://webidl.spec.whatwg.org/#idl-any detail#dom-customevent-detail;

  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined initCustomEvent#dom-customevent-initcustomevent(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString type, optional booleanhttps://webidl.spec.whatwg.org/#idl-boolean bubbles = false, optional booleanhttps://webidl.spec.whatwg.org/#idl-boolean cancelable = false, optional anyhttps://webidl.spec.whatwg.org/#idl-any detail = null); // legacy
};

dictionary CustomEventInit : EventInit#dictdef-eventinit {
  anyhttps://webidl.spec.whatwg.org/#idl-any detail = null;
};
```

[Events](#concept-event) using the [CustomEvent](#customevent) interface can be used to carry custom data.

[CustomEvent](#dom-customevent-customevent)`event = new (type [, eventInitDict])`Works analogously to the constructor for [Event](#event) except that the eventInitDict argument now allows for setting the [detail](#dom-customevent-detail) attribute too. [detail](#dom-customevent-detail)Returns any custom data event was created with. Typically used for synthetic events. 

The `detail` attribute must return the value it was initialized to. 

The `initCustomEvent(type, bubbles, cancelable, detail)` method steps are: 

1. 

If [this](https://webidl.spec.whatwg.org/#this)’s [dispatch flag](#dispatch-flag) is set, then return. 

2. 

[Initialize](#concept-event-initialize)[this](https://webidl.spec.whatwg.org/#this) with type, bubbles, and cancelable. 

3. 

Set [this](https://webidl.spec.whatwg.org/#this)’s [detail](#dom-customevent-detail) attribute to detail. 

### 2.5. Constructing events#constructing-events

[Specifications](#other-applicable-specifications) may define event constructing steps for all or some [events](#concept-event). The algorithm is passed an [event](#concept-event)event and an [EventInit](#dictdef-eventinit)eventInitDict as indicated in the [inner event creation steps](#inner-event-creation-steps).

This construct can be used by [Event](#event) subclasses that have a more complex structure than a simple 1:1 mapping between their initializing dictionary members and IDL attributes. 

When a constructor of the [Event](#event) interface, or of an interface that inherits from the [Event](#event) interface, is invoked, these steps must be run, given the arguments type and eventInitDict: 

1. 

Let event be the result of running the [inner event creation steps](#inner-event-creation-steps) with this interface, null, now, and eventInitDict. 

2. 

Initialize event’s [type](#dom-event-type) attribute to type. 

3. 

Return event. 

To create an event using eventInterface, which must be either [Event](#event) or an interface that inherits from it, and optionally given a [realm](https://tc39.es/ecma262/#realm)realm, run these steps:

1. 

If realm is not given, then set it to null. 

2. 

Let dictionary be the result of [converting](https://webidl.spec.whatwg.org/#dfn-convert-ecmascript-to-idl-value) the JavaScript value undefined to the dictionary type accepted by eventInterface’s constructor. (This dictionary type will either be [EventInit](#dictdef-eventinit) or a dictionary that inherits from it.) 

This does not work if members are required; see [whatwg/dom#600](https://github.com/whatwg/dom/issues/600). 

3. 

Let event be the result of running the [inner event creation steps](#inner-event-creation-steps) with eventInterface, realm, the time of the occurrence that the event is signaling, and dictionary. 

#example-timestamp-initializationIn macOS the time of the occurrence for input actions is available via the `timestamp` property of `NSEvent` objects. 

4. 

Initialize event’s [isTrusted](#dom-event-istrusted) attribute to true. 

5. 

Return event. 

[Create an event](#concept-event-create) is meant to be used by other specifications which need to separately [create](#concept-event-create) and [dispatch](#concept-event-dispatch) events, instead of simply [firing](#concept-event-fire) them. It ensures the event’s attributes are initialized to the correct defaults.

The inner event creation steps, given an eventInterface, realm, time, and dictionary, are as follows:

1. 

Let event be the result of creating a new object using eventInterface. If realm is non-null, then use that realm; otherwise, use the default behavior defined in Web IDL. 

As of the time of this writing Web IDL does not yet define any default behavior; see [whatwg/webidl#135](https://github.com/whatwg/webidl/issues/135). 

2. 

Set event’s [initialized flag](#initialized-flag). 

3. 

Initialize event’s [timeStamp](#dom-event-timestamp) attribute to the [relative high resolution coarse time](https://w3c.github.io/hr-time/#dfn-relative-high-resolution-coarse-time) given time and event’s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global). 

4. 

[For each](https://infra.spec.whatwg.org/#map-iterate)member → value of dictionary: if event has an attribute whose [identifier](https://webidl.spec.whatwg.org/#dfn-identifier) is member, then initialize that attribute to value. 

5. 

Run the [event constructing steps](#concept-event-constructor-ext) with event and dictionary. 

6. 

Return event. 

### 2.6. Defining event interfaces#defining-event-interfaces

In general, when defining a new interface that inherits from [Event](#event) please always ask feedback from the [WHATWG](https://whatwg.org/) or the [W3C WebApps WG](https://www.w3.org/2008/webapps/) community.

The [CustomEvent](#customevent) interface can be used as starting point. However, do not introduce any `init*Event()` methods as they are redundant with constructors. Interfaces that inherit from the [Event](#event) interface that have such a method only have it for historical reasons.

### 2.7. Interface [EventTarget](#eventtarget)#interface-eventtarget

```
[Exposed=*]
interface EventTarget {
  constructor#dom-eventtarget-eventtarget();

  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined addEventListener#dom-eventtarget-addeventlistener(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString type, EventListener#callbackdef-eventlistener? callback, optional (AddEventListenerOptions#dictdef-addeventlisteneroptions or booleanhttps://webidl.spec.whatwg.org/#idl-boolean) options = {});
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined removeEventListener#dom-eventtarget-removeeventlistener(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString type, EventListener#callbackdef-eventlistener? callback, optional (EventListenerOptions#dictdef-eventlisteneroptions or booleanhttps://webidl.spec.whatwg.org/#idl-boolean) options = {});
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean dispatchEvent#dom-eventtarget-dispatchevent(Event#event event);
};

callback interface EventListener {
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined handleEvent(Event#event event);
};

dictionary EventListenerOptions {
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean capture = false;
};

dictionary AddEventListenerOptions : EventListenerOptions#dictdef-eventlisteneroptions {
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean passive;
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean once = false;
  AbortSignal#abortsignal signal;
};
```

An [EventTarget](#eventtarget) object represents a target to which an [event](#concept-event) can be [dispatched](#concept-event-dispatch) when something has occurred. 

Each [EventTarget](#eventtarget) object has an associated event listener list (a [list](https://infra.spec.whatwg.org/#list) of zero or more [event listeners](#concept-event-listener)). It is initially the empty list. 

An event listener can be used to observe a specific [event](#concept-event) and consists of: 

- type (a string) 
- callback (null or an [EventListener](#callbackdef-eventlistener) object) 
- capture (a boolean, initially false) 
- passive (null or a boolean, initially null) 
- once (a boolean, initially false) 
- signal (null or an [AbortSignal](#abortsignal) object) 
- removed (a boolean for bookkeeping purposes, initially false) 

Although [callback](#event-listener-callback) is an [EventListener](#callbackdef-eventlistener) object, an [event listener](#concept-event-listener) is a broader concept as can be seen above. 

Each [EventTarget](#eventtarget) object also has an associated get the parent algorithm, which takes an [event](#concept-event)event, and returns an [EventTarget](#eventtarget) object. Unless specified otherwise it returns null. 

[Nodes](#concept-node), [shadow roots](#concept-shadow-root), and [documents](#concept-document) override the [get the parent](#get-the-parent) algorithm. 

Each [EventTarget](#eventtarget) object can have an associated activation behavior algorithm. The [activation behavior](#eventtarget-activation-behavior) algorithm is passed an [event](#concept-event), as indicated in the [dispatch](#concept-event-dispatch) algorithm.

This exists because user agents perform certain actions for certain [EventTarget](#eventtarget) objects, e.g., the [area](https://html.spec.whatwg.org/multipage/image-maps.html#the-area-element) element, in response to synthetic [MouseEvent](https://w3c.github.io/uievents/#mouseevent)[events](#concept-event) whose [type](#dom-event-type) attribute is `click`. Web compatibility prevented it from being removed and it is now the enshrined way of defining an activation of something. [[HTML]](#biblio-html)

Each [EventTarget](#eventtarget) object that has [activation behavior](#eventtarget-activation-behavior), can additionally have both (not either) a legacy-pre-activation behavior algorithm and a legacy-canceled-activation behavior algorithm. 

These algorithms only exist for checkbox and radio [input](https://html.spec.whatwg.org/multipage/input.html#the-input-element) elements and are not to be used for anything else. [[HTML]](#biblio-html)

[EventTarget](#dom-eventtarget-eventtarget)`target = new ();`

Creates a new [EventTarget](#eventtarget) object, which can be used by developers to [dispatch](#concept-event-dispatch) and listen for [events](#concept-event). 

[addEventListener](#dom-eventtarget-addeventlistener)`target . (type, callback [, options])`

Appends an [event listener](#concept-event-listener) for [events](#concept-event) whose [type](#dom-event-type) attribute value is type. The callback argument sets the [callback](#event-listener-callback) that will be invoked when the [event](#concept-event) is [dispatched](#concept-event-dispatch). 

The options argument sets listener-specific options. For compatibility this can be a boolean, in which case the method behaves exactly as if the value was specified as options’s [capture](#dom-eventlisteneroptions-capture). 

When set to true, options’s [capture](#dom-eventlisteneroptions-capture) prevents [callback](#event-listener-callback) from being invoked when the [event](#concept-event)’s [eventPhase](#dom-event-eventphase) attribute value is [BUBBLING_PHASE](#dom-event-bubbling_phase). When false (or not present), [callback](#event-listener-callback) will not be invoked when [event](#concept-event)’s [eventPhase](#dom-event-eventphase) attribute value is [CAPTURING_PHASE](#dom-event-capturing_phase). Either way, [callback](#event-listener-callback) will be invoked if [event](#concept-event)’s [eventPhase](#dom-event-eventphase) attribute value is [AT_TARGET](#dom-event-at_target). 

When set to true, options’s [passive](#dom-addeventlisteneroptions-passive) indicates that the [callback](#event-listener-callback) will not cancel the event by invoking [preventDefault()](#dom-event-preventdefault). This is used to enable performance optimizations described in [§ 2.8 Observing event listeners](#observing-event-listeners). 

When set to true, options’s [once](#dom-addeventlisteneroptions-once) indicates that the [callback](#event-listener-callback) will only be invoked once after which the event listener will be removed. 

If an [AbortSignal](#abortsignal) is passed for options’s [signal](#dom-addeventlisteneroptions-signal), then the event listener will be removed when signal is aborted. 

The [event listener](#concept-event-listener) is appended to target’s [event listener list](#eventtarget-event-listener-list) and is not appended if it has the same [type](#event-listener-type), [callback](#event-listener-callback), and [capture](#event-listener-capture). 

[removeEventListener](#dom-eventtarget-removeeventlistener)`target . (type, callback [, options])`

Removes the [event listener](#concept-event-listener) in target’s [event listener list](#eventtarget-event-listener-list) with the same type, callback, and options. 

[dispatchEvent](#dom-eventtarget-dispatchevent)`target . (event)`

[Dispatches](#concept-event-dispatch) a synthetic event event to target and returns true if either event’s [cancelable](#dom-event-cancelable) attribute value is false or its [preventDefault()](#dom-event-preventdefault) method was not invoked; otherwise false. 

To flattenoptions, run these steps: 

1. 

If options is a boolean, then return options. 

2. 

Return options["[capture](#dom-eventlisteneroptions-capture)"]. 

To flatten moreoptions, run these steps: 

1. 

Let capture be the result of [flattening](#concept-flatten-options)options. 

2. 

Let once be false. 

3. 

Let passive and signal be null. 

4. 

If options is a [dictionary](https://webidl.spec.whatwg.org/#dfn-dictionary): 

  1. 

Set once to options["[once](#dom-addeventlisteneroptions-once)"]. 

  2. 

If options["[passive](#dom-addeventlisteneroptions-passive)"] [exists](https://infra.spec.whatwg.org/#map-exists), then set passive to options["[passive](#dom-addeventlisteneroptions-passive)"]. 

  3. 

If options["[signal](#dom-addeventlisteneroptions-signal)"] [exists](https://infra.spec.whatwg.org/#map-exists), then set signal to options["[signal](#dom-addeventlisteneroptions-signal)"]. 

5. 

Return capture, passive, once, and signal. 

The `new EventTarget()` constructor steps are to do nothing. 

Because of the defaults stated elsewhere, the returned [EventTarget](#eventtarget)’s [get the parent](#get-the-parent) algorithm will return null, and it will have no [activation behavior](#eventtarget-activation-behavior), [legacy-pre-activation behavior](#eventtarget-legacy-pre-activation-behavior), or [legacy-canceled-activation behavior](#eventtarget-legacy-canceled-activation-behavior). 

In the future we could allow custom [get the parent](#get-the-parent) algorithms. Let us know if this would be useful for your programs. For now, all author-created [EventTarget](#eventtarget)s do not participate in a tree structure.

The default passive value, given an event type type and an [EventTarget](#eventtarget)eventTarget, is determined as follows: 

1. 

Return true if all of the following are true: 

  - 

type is one of "`touchstart`", "`touchmove`", "`wheel`", or "`mousewheel`". [[TOUCH-EVENTS]](#biblio-touch-events)[[UIEVENTS]](#biblio-uievents)

  - 

eventTarget is a [Window](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window) object, or is a [node](#concept-node) whose [node document](#concept-node-document) is eventTarget, or is a [node](#concept-node) whose [node document](#concept-node-document)’s [document element](#document-element) is eventTarget, or is a [node](#concept-node) whose [node document](#concept-node-document)’s [body element](https://html.spec.whatwg.org/multipage/dom.html#the-body-element-2) is eventTarget. [[HTML]](#biblio-html)

2. 

Return false. 

To add an event listener, given an [EventTarget](#eventtarget) object eventTarget and an [event listener](#concept-event-listener)listener, run these steps: 

1. 

If eventTarget is a [ServiceWorkerGlobalScope](https://w3c.github.io/ServiceWorker/#serviceworkerglobalscope) object, its [service worker](https://w3c.github.io/ServiceWorker/#serviceworkerglobalscope-service-worker)’s [script resource](https://w3c.github.io/ServiceWorker/#dfn-script-resource)’s [has ever been evaluated flag](https://w3c.github.io/ServiceWorker/#dfn-has-ever-been-evaluated-flag) is set, and listener’s [type](#event-listener-type) matches the [type](#dom-event-type) attribute value of any of the [service worker events](https://w3c.github.io/ServiceWorker/#dfn-service-worker-events), then [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) that this might not give the expected results. [[SERVICE-WORKERS]](#biblio-service-workers)

2. 

If listener’s [signal](#event-listener-signal) is non-null and is [aborted](#abortsignal-aborted), then return. 

3. 

If listener’s [callback](#event-listener-callback) is null, then return. 

4. 

If listener’s [passive](#event-listener-passive) is null, then set it to the [default passive value](#default-passive-value) given listener’s [type](#event-listener-type) and eventTarget. 

5. 

If eventTarget’s [event listener list](#eventtarget-event-listener-list) does not [contain](https://infra.spec.whatwg.org/#list-contain) an [event listener](#concept-event-listener) whose [type](#event-listener-type) is listener’s [type](#event-listener-type), [callback](#event-listener-callback) is listener’s [callback](#event-listener-callback), and [capture](#event-listener-capture) is listener’s [capture](#event-listener-capture), then [append](https://infra.spec.whatwg.org/#list-append)listener to eventTarget’s [event listener list](#eventtarget-event-listener-list). 

6. 

If listener’s [signal](#event-listener-signal) is non-null, then [add the following](#abortsignal-add) abort steps to it: 

  1. [Remove an event listener](#remove-an-event-listener) with eventTarget and listener. 

The [add an event listener](#add-an-event-listener) concept exists to ensure [event handlers](https://html.spec.whatwg.org/multipage/webappapis.html#event-handlers) use the same code path. [[HTML]](#biblio-html)

The `addEventListener(type, callback, options)` method steps are: 

1. 

Let capture, passive, once, and signal be the result of [flattening more](#event-flatten-more)options. 

2. 

[Add an event listener](#add-an-event-listener) with [this](https://webidl.spec.whatwg.org/#this) and an [event listener](#concept-event-listener) whose [type](#event-listener-type) is type, [callback](#event-listener-callback) is callback, [capture](#event-listener-capture) is capture, [passive](#event-listener-passive) is passive, [once](#event-listener-once) is once, and [signal](#event-listener-signal) is signal. 

To remove an event listener, given an [EventTarget](#eventtarget) object eventTarget and an [event listener](#concept-event-listener)listener, run these steps: 

1. 

If eventTarget is a [ServiceWorkerGlobalScope](https://w3c.github.io/ServiceWorker/#serviceworkerglobalscope) object and its [service worker](https://w3c.github.io/ServiceWorker/#serviceworkerglobalscope-service-worker)’s [set of event types to handle](https://w3c.github.io/ServiceWorker/#dfn-set-of-event-types-to-handle)[contains](https://infra.spec.whatwg.org/#list-contain)listener’s [type](#event-listener-type), then [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) that this might not give the expected results. [[SERVICE-WORKERS]](#biblio-service-workers)

2. 

Set listener’s [removed](#event-listener-removed) to true and [remove](https://infra.spec.whatwg.org/#list-remove)listener from eventTarget’s [event listener list](#eventtarget-event-listener-list). 

HTML needs this to define event handlers. [[HTML]](#biblio-html)

To remove all event listeners, given an [EventTarget](#eventtarget) object eventTarget: [for each](https://infra.spec.whatwg.org/#list-iterate)listener of eventTarget’s [event listener list](#eventtarget-event-listener-list): [remove an event listener](#remove-an-event-listener) with eventTarget and listener. 

HTML needs this to define `document.open()`. [[HTML]](#biblio-html)

The `removeEventListener(type, callback, options)` method steps are: 

1. 

Let capture be the result of [flattening](#concept-flatten-options)options. 

2. 

If [this](https://webidl.spec.whatwg.org/#this)’s [event listener list](#eventtarget-event-listener-list)[contains](https://infra.spec.whatwg.org/#list-contain) an [event listener](#concept-event-listener) whose [type](#event-listener-type) is type, [callback](#event-listener-callback) is callback, and [capture](#event-listener-capture) is capture, then [remove an event listener](#remove-an-event-listener) with [this](https://webidl.spec.whatwg.org/#this) and that [event listener](#concept-event-listener). 

The event listener list will not contain multiple event listeners with equal type, callback, and capture, as [add an event listener](#add-an-event-listener) prevents that. 

The `dispatchEvent(event)` method steps are: 

1. 

If event’s [dispatch flag](#dispatch-flag) is set, or if its [initialized flag](#initialized-flag) is not set, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidStateError](https://webidl.spec.whatwg.org/#invalidstateerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

2. 

Initialize event’s [isTrusted](#dom-event-istrusted) attribute to false. 

3. 

Return the result of [dispatching](#concept-event-dispatch)event to [this](https://webidl.spec.whatwg.org/#this). 

### 2.8. Observing event listeners#observing-event-listeners

In general, developers do not expect the presence of an [event listener](#concept-event-listener) to be observable. The impact of an [event listener](#concept-event-listener) is determined by its [callback](#event-listener-callback). That is, a developer adding a no-op [event listener](#concept-event-listener) would not expect it to have any side effects. 

Unfortunately, some event APIs have been designed such that implementing them efficiently requires observing [event listeners](#concept-event-listener). This can make the presence of listeners observable in that even empty listeners can have a dramatic performance impact on the behavior of the application. For example, touch and wheel events which can be used to block asynchronous scrolling. In some cases this problem can be mitigated by specifying the event to be [cancelable](#dom-event-cancelable) only when there is at least one non-[passive](#dom-addeventlisteneroptions-passive) listener. For example, non-[passive](#dom-addeventlisteneroptions-passive)[TouchEvent](https://w3c.github.io/touch-events/#idl-def-touchevent) listeners must block scrolling, but if all listeners are [passive](#dom-addeventlisteneroptions-passive) then scrolling can be allowed to start [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel) by making the [TouchEvent](https://w3c.github.io/touch-events/#idl-def-touchevent) uncancelable (so that calls to [preventDefault()](#dom-event-preventdefault) are ignored). So code dispatching an event is able to observe the absence of non-[passive](#dom-addeventlisteneroptions-passive) listeners, and use that to clear the [cancelable](#dom-event-cancelable) property of the event being dispatched. 

Ideally, any new event APIs are defined such that they do not need this property. (Use [whatwg/dom](https://github.com/whatwg/dom/issues) for discussion.) 

To legacy-obtain service worker fetch event listener callbacks given a [ServiceWorkerGlobalScope](https://w3c.github.io/ServiceWorker/#serviceworkerglobalscope)global, run these steps. They return a [list](https://infra.spec.whatwg.org/#list) of [EventListener](#callbackdef-eventlistener) objects. 

1. 

Let callbacks be « ». 

2. 

[For each](https://infra.spec.whatwg.org/#list-iterate)listener of global’s [event listener list](#eventtarget-event-listener-list): if listener’s [type](#event-listener-type) is "`fetch`" and listener’s [callback](#event-listener-callback) is non-null, then [append](https://infra.spec.whatwg.org/#list-append)listener’s [callback](#event-listener-callback) to callbacks. 

3. 

Return callbacks. 

### 2.9. Dispatching events#dispatching-events

To dispatch an event to a target, with an optional legacy target override flag and an optional legacyOutputDidListenersThrowFlag, run these steps: 

1. 

Set event’s [dispatch flag](#dispatch-flag). 

2. 

Let targetOverride be target, if legacy target override flag is not given, and target’s [associated Document](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window) otherwise. [[HTML]](#biblio-html)

legacy target override flag is only used by HTML and only when target is a [Window](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window) object. 

3. 

Let activationTarget be null. 

4. 

Let relatedTarget be the result of [retargeting](#retarget)event’s [relatedTarget](#event-relatedtarget) against target. 

5. 

Let clearTargets be false. 

6. 

If target is not relatedTarget or target is event’s [relatedTarget](#event-relatedtarget): 

  1. 

Let touchTargets be a new [list](https://infra.spec.whatwg.org/#list). 

  2. 

[For each](https://infra.spec.whatwg.org/#list-iterate)touchTarget of event’s [touch target list](#event-touch-target-list): [append](https://infra.spec.whatwg.org/#list-append) the result of [retargeting](#retarget)touchTarget against target to touchTargets. 

  3. 

[Append to an event path](#concept-event-path-append) with event, target, targetOverride, relatedTarget, touchTargets, and false. 

  4. 

Let isActivationEvent be true, if event is a [MouseEvent](https://w3c.github.io/uievents/#mouseevent) object and event’s [type](#dom-event-type) attribute is "`click`"; otherwise false. 

  5. 

If isActivationEvent is true and target has [activation behavior](#eventtarget-activation-behavior), then set activationTarget to target. 

  6. 

Let slottable be target, if target is a [slottable](#concept-slotable) and is [assigned](#slotable-assigned), and null otherwise. 

  7. 

Let slot-in-closed-tree be false. 

  8. 

Let parent be the result of invoking target’s [get the parent](#get-the-parent) with event. 

  9. 

While parent is non-null:

    1. 

If slottable is non-null: 

      1. 

Assert: parent is a [slot](#concept-slot). 

      2. 

Set slottable to null. 

      3. 

If parent’s [root](#concept-tree-root) is a [shadow root](#concept-shadow-root) whose [mode](#shadowroot-mode) is "`closed`", then set slot-in-closed-tree to true. 

    2. 

If parent is a [slottable](#concept-slotable) and is [assigned](#slotable-assigned), then set slottable to parent. 

    3. 

Let relatedTarget be the result of [retargeting](#retarget)event’s [relatedTarget](#event-relatedtarget) against parent. 

    4. 

Let touchTargets be a new [list](https://infra.spec.whatwg.org/#list). 

    5. 

[For each](https://infra.spec.whatwg.org/#list-iterate)touchTarget of event’s [touch target list](#event-touch-target-list): [append](https://infra.spec.whatwg.org/#list-append) the result of [retargeting](#retarget)touchTarget against parent to touchTargets. 

    6. 

If parent is a [Window](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window) object, or parent is a [node](#concept-node) and target’s [root](#concept-tree-root) is a [shadow-including inclusive ancestor](#concept-shadow-including-inclusive-ancestor) of parent: 

      1. 

If isActivationEvent is true, event’s [bubbles](#dom-event-bubbles) attribute is true, activationTarget is null, and parent has [activation behavior](#eventtarget-activation-behavior), then set activationTarget to parent. 

      2. 

[Append to an event path](#concept-event-path-append) with event, parent, null, relatedTarget, touchTargets, and slot-in-closed-tree. 

    7. 

Otherwise, if parent is relatedTarget, then set parent to null. 

    8. 

Otherwise: 

      1. 

Set target to parent. 

      2. 

If isActivationEvent is true, activationTarget is null, and target has [activation behavior](#eventtarget-activation-behavior), then set activationTarget to target. 

      3. 

[Append to an event path](#concept-event-path-append) with event, parent, target, relatedTarget, touchTargets, and slot-in-closed-tree. 

    9. 

If parent is non-null, then set parent to the result of invoking parent’s [get the parent](#get-the-parent) with event. 

    10. 

Set slot-in-closed-tree to false. 

  10. 

Let clearTargetsStruct be the last struct in event’s [path](#event-path) whose [shadow-adjusted target](#event-path-shadow-adjusted-target) is non-null. 

  11. 

If clearTargetsStruct’s [shadow-adjusted target](#event-path-shadow-adjusted-target), clearTargetsStruct’s [relatedTarget](#event-path-relatedtarget), or an [EventTarget](#eventtarget) object in clearTargetsStruct’s [touch target list](#event-path-touch-target-list) is a [node](#concept-node) whose [root](#concept-tree-root) is a [shadow root](#concept-shadow-root): set clearTargets to true. 

  12. 

If activationTarget is non-null and activationTarget has [legacy-pre-activation behavior](#eventtarget-legacy-pre-activation-behavior), then run activationTarget’s [legacy-pre-activation behavior](#eventtarget-legacy-pre-activation-behavior). 

  13. 

[For each](https://infra.spec.whatwg.org/#list-iterate)struct of event’s [path](#event-path), in reverse order: 

    1. 

If struct’s [shadow-adjusted target](#event-path-shadow-adjusted-target) is non-null, then set event’s [eventPhase](#dom-event-eventphase) attribute to [AT_TARGET](#dom-event-at_target). 

    2. 

Otherwise, set event’s [eventPhase](#dom-event-eventphase) attribute to [CAPTURING_PHASE](#dom-event-capturing_phase). 

    3. 

[Invoke](#concept-event-listener-invoke) with struct, event, "`capturing`", and legacyOutputDidListenersThrowFlag if given. 

  14. 

[For each](https://infra.spec.whatwg.org/#list-iterate)struct of event’s [path](#event-path): 

    1. 

If struct’s [shadow-adjusted target](#event-path-shadow-adjusted-target) is non-null, then set event’s [eventPhase](#dom-event-eventphase) attribute to [AT_TARGET](#dom-event-at_target). 

    2. 

Otherwise: 

      1. 

If event’s [bubbles](#dom-event-bubbles) attribute is false, then [continue](https://infra.spec.whatwg.org/#iteration-continue). 

      2. 

Set event’s [eventPhase](#dom-event-eventphase) attribute to [BUBBLING_PHASE](#dom-event-bubbling_phase). 

    3. 

[Invoke](#concept-event-listener-invoke) with struct, event, "`bubbling`", and legacyOutputDidListenersThrowFlag if given. 

7. 

Set event’s [eventPhase](#dom-event-eventphase) attribute to [NONE](#dom-event-none). 

8. 

Set event’s [currentTarget](#dom-event-currenttarget) attribute to null. 

9. 

Set event’s [path](#event-path) to the empty list. 

10. 

Unset event’s [dispatch flag](#dispatch-flag), [stop propagation flag](#stop-propagation-flag), and [stop immediate propagation flag](#stop-immediate-propagation-flag). 

11. 

If clearTargets is true: 

  1. 

Set event’s [target](#event-target) to null. 

  2. 

Set event’s [relatedTarget](#event-relatedtarget) to null. 

  3. 

Set event’s [touch target list](#event-touch-target-list) to the empty list. 

12. 

If activationTarget is non-null: 

  1. 

If event’s [canceled flag](#canceled-flag) is unset, then run activationTarget’s [activation behavior](#eventtarget-activation-behavior) with event. 

  2. 

Otherwise, if activationTarget has [legacy-canceled-activation behavior](#eventtarget-legacy-canceled-activation-behavior), then run activationTarget’s [legacy-canceled-activation behavior](#eventtarget-legacy-canceled-activation-behavior). 

13. 

Return false if event’s [canceled flag](#canceled-flag) is set; otherwise true. 

To append to an event path, given an event, invocationTarget, shadowAdjustedTarget, relatedTarget, touchTargets, and a slot-in-closed-tree, run these steps:

1. 

Let invocationTargetInShadowTree be false. 

2. 

If invocationTarget is a [node](#concept-node) and its [root](#concept-tree-root) is a [shadow root](#concept-shadow-root), then set invocationTargetInShadowTree to true. 

3. 

Let root-of-closed-tree be false. 

4. 

If invocationTarget is a [shadow root](#concept-shadow-root) whose [mode](#shadowroot-mode) is "`closed`", then set root-of-closed-tree to true. 

5. 

[Append](https://infra.spec.whatwg.org/#list-append) a new [struct](https://infra.spec.whatwg.org/#struct) to event’s [path](#event-path) whose [invocation target](#event-path-invocation-target) is invocationTarget, [invocation-target-in-shadow-tree](#event-path-invocation-target-in-shadow-tree) is invocationTargetInShadowTree, [shadow-adjusted target](#event-path-shadow-adjusted-target) is shadowAdjustedTarget, [relatedTarget](#event-path-relatedtarget) is relatedTarget, [touch target list](#event-path-touch-target-list) is touchTargets, [root-of-closed-tree](#event-path-root-of-closed-tree) is root-of-closed-tree, and [slot-in-closed-tree](#event-path-slot-in-closed-tree) is slot-in-closed-tree. 

To invoke, given a struct, event, phase, and an optional legacyOutputDidListenersThrowFlag, run these steps: 

1. 

Set event’s [target](#event-target) to the [shadow-adjusted target](#event-path-shadow-adjusted-target) of the last struct in event’s [path](#event-path), that is either struct or preceding struct, whose [shadow-adjusted target](#event-path-shadow-adjusted-target) is non-null. 

2. 

Set event’s [relatedTarget](#event-relatedtarget) to struct’s [relatedTarget](#event-path-relatedtarget). 

3. 

Set event’s [touch target list](#event-touch-target-list) to struct’s [touch target list](#event-path-touch-target-list). 

4. 

If event’s [stop propagation flag](#stop-propagation-flag) is set, then return. 

5. 

Initialize event’s [currentTarget](#dom-event-currenttarget) attribute to struct’s [invocation target](#event-path-invocation-target). 

6. 

Let listeners be a [clone](https://infra.spec.whatwg.org/#list-clone) of event’s [currentTarget](#dom-event-currenttarget) attribute value’s [event listener list](#eventtarget-event-listener-list). 

This avoids [event listeners](#concept-event-listener) added after this point from being run. Note that removal still has an effect due to the [removed](#event-listener-removed) field. 

7. 

Let invocationTargetInShadowTree be struct’s [invocation-target-in-shadow-tree](#event-path-invocation-target-in-shadow-tree). 

8. 

Let found be the result of running [inner invoke](#concept-event-listener-inner-invoke) with event, listeners, phase, invocationTargetInShadowTree, and legacyOutputDidListenersThrowFlag if given. 

9. 

If found is false and event’s [isTrusted](#dom-event-istrusted) attribute is true: 

  1. 

Let originalEventType be event’s [type](#dom-event-type) attribute value. 

  2. 

If event’s [type](#dom-event-type) attribute value is a match for any of the strings in the first column in the following table, set event’s [type](#dom-event-type) attribute value to the string in the second column on the same row as the matching string, and return otherwise. 

Event type Legacy event type "`animationend`" "`webkitAnimationEnd`" "`animationiteration`" "`webkitAnimationIteration`" "`animationstart`" "`webkitAnimationStart`" "`transitionend`" "`webkitTransitionEnd`" 
  3. 

[Inner invoke](#concept-event-listener-inner-invoke) with event, listeners, phase, invocationTargetInShadowTree, and legacyOutputDidListenersThrowFlag if given. 

  4. 

Set event’s [type](#dom-event-type) attribute value to originalEventType. 

To inner invoke, given an event, listeners, phase, invocationTargetInShadowTree, and an optional legacyOutputDidListenersThrowFlag, run these steps: 

1. 

Let found be false. 

2. 

[For each](https://infra.spec.whatwg.org/#list-iterate)listener of listeners, whose [removed](#event-listener-removed) is false: 

  1. 

If event’s [type](#dom-event-type) attribute value is not listener’s [type](#event-listener-type), then [continue](https://infra.spec.whatwg.org/#iteration-continue). 

  2. 

Set found to true. 

  3. 

If phase is "`capturing`" and listener’s [capture](#event-listener-capture) is false, then [continue](https://infra.spec.whatwg.org/#iteration-continue). 

  4. 

If phase is "`bubbling`" and listener’s [capture](#event-listener-capture) is true, then [continue](https://infra.spec.whatwg.org/#iteration-continue). 

  5. 

If listener’s [once](#event-listener-once) is true, then [remove an event listener](#remove-an-event-listener) given event’s [currentTarget](#dom-event-currenttarget) attribute value and listener. 

  6. 

Let global be listener[callback](#event-listener-callback)’s [associated realm](https://webidl.spec.whatwg.org/#dfn-associated-realm)’s [global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-realm-global). 

  7. 

Let currentEvent be undefined. 

  8. 

If global is a [Window](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window) object: 

    1. 

Set currentEvent to global’s [current event](#window-current-event). 

    2. 

If invocationTargetInShadowTree is false, then set global’s [current event](#window-current-event) to event. 

  9. 

If listener’s [passive](#event-listener-passive) is true, then set event’s [in passive listener flag](#in-passive-listener-flag). 

  10. 

If global is a [Window](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window) object, then [record timing info for event listener](https://w3c.github.io/long-animation-frames/#record-timing-info-for-event-listener) given event and listener. 

  11. 

[Call a user object’s operation](https://webidl.spec.whatwg.org/#call-a-user-objects-operation) with listener’s [callback](#event-listener-callback), "`handleEvent`", « event », and event’s [currentTarget](#dom-event-currenttarget) attribute value. If this throws an exception exception: 

    1. 

[Report](https://html.spec.whatwg.org/multipage/webappapis.html#report-an-exception)exception for listener’s [callback](#event-listener-callback)’s corresponding JavaScript object’s [associated realm](https://webidl.spec.whatwg.org/#dfn-associated-realm)’s [global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-realm-global). 

    2. 

Set legacyOutputDidListenersThrowFlag if given. 

The legacyOutputDidListenersThrowFlag is only used by Indexed Database API. [[INDEXEDDB]](#biblio-indexeddb)

  12. 

Unset event’s [in passive listener flag](#in-passive-listener-flag). 

  13. 

If global is a [Window](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window) object, then set global’s [current event](#window-current-event) to currentEvent. 

  14. 

If event’s [stop immediate propagation flag](#stop-immediate-propagation-flag) is set, then [break](https://infra.spec.whatwg.org/#iteration-break). 

3. 

Return found. 

### 2.10. Firing events#firing-events

To fire an event named e at target, optionally using an eventConstructor, with a description of how IDL attributes are to be initialized, and a legacy target override flag, run these steps: 

1. 

If eventConstructor is not given, then let eventConstructor be [Event](#event). 

2. 

Let event be the result of [creating an event](#concept-event-create) given eventConstructor, in the [relevant realm](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-realm) of target. 

3. 

Initialize event’s [type](#dom-event-type) attribute to e. 

4. 

Initialize any other IDL attributes of event as described in the invocation of this algorithm. 

This also allows for the [isTrusted](#dom-event-istrusted) attribute to be set to false. 

5. 

Return the result of [dispatching](#concept-event-dispatch)event at target, with legacy target override flag set if set. 

Fire in the context of DOM is short for [creating](#concept-event-create), initializing, and [dispatching](#concept-event-dispatch) an [event](#concept-event). [Fire an event](#concept-event-fire) makes that process easier to write down. 

#firing-events-example

If the [event](#concept-event) needs its [bubbles](#dom-event-bubbles) or [cancelable](#dom-event-cancelable) attribute initialized, one could write "[fire an event](#concept-event-fire) named `submit` at target with its [cancelable](#dom-event-cancelable) attribute initialized to true". 

Or, when a custom constructor is needed, "[fire an event](#concept-event-fire) named `click` at target using [MouseEvent](https://w3c.github.io/uievents/#mouseevent) with its [detail](https://w3c.github.io/uievents/#dom-uievent-detail) attribute initialized to 1". 

Occasionally the return value is important: 

1. 

Let doAction be the result of [firing an event](#concept-event-fire) named `like` at target. 

2. 

If doAction is true, then … 

### 2.11. Action versus occurrence#action-versus-occurrence

An [event](#concept-event) signifies an occurrence, not an action. Phrased differently, it represents a notification from an algorithm and can be used to influence the future course of that algorithm (e.g., through invoking [preventDefault()](#dom-event-preventdefault)). [Events](#concept-event) must not be used as actions or initiators that cause some algorithm to start running. That is not what they are for. 

This is called out here specifically because previous iterations of the DOM had a concept of "default actions" associated with [events](#concept-event) that gave folks all the wrong ideas. [Events](#concept-event) do not represent or cause actions, they can only be used to influence an ongoing one. 

## 3. Aborting ongoing activities#aborting-ongoing-activities

Though promises do not have a built-in aborting mechanism, many APIs using them require abort semantics. [AbortController](#abortcontroller) is meant to support these requirements by providing an [abort()](#dom-abortcontroller-abort) method that toggles the state of a corresponding [AbortSignal](#abortsignal) object. The API which wishes to support aborting can accept an [AbortSignal](#abortsignal) object, and use its state to determine how to proceed. 

APIs that rely upon [AbortController](#abortcontroller) are encouraged to respond to [abort()](#dom-abortcontroller-abort) by rejecting any unsettled promise with the [AbortSignal](#abortsignal)’s [abort reason](#abortsignal-abort-reason). 

#aborting-ongoing-activities-example

A hypothetical `doAmazingness({ ... })` method could accept an [AbortSignal](#abortsignal) object to support aborting as follows: 

```
const controller = new AbortController();
const signal = controller.signal;

startSpinner();

doAmazingness({ ..., signal })
  .then(result => ...)
  .catch(err => {
    if (err.name == 'AbortError') return;
    showUserErrorMessage();
  })
  .then(() => stopSpinner());

// …

controller.abort();
```

`doAmazingness` could be implemented as follows: 

```
function doAmazingness({signal}) {
  return new Promise((resolve, reject) => {
    signal.throwIfAborted();

    // Begin doing amazingness, and call resolve(result) when done.
    // But also, watch for signals:
    signal.addEventListener('abort', () => {
      // Stop doing amazingness, and:
      reject(signal.reason);
    });
  });
}
```

APIs that do not return promises can either react in an equivalent manner or opt to not surface the [AbortSignal](#abortsignal)’s [abort reason](#abortsignal-abort-reason) at all. [addEventListener()](#dom-eventtarget-addeventlistener) is an example of an API where the latter made sense. 

APIs that require more granular control could extend both [AbortController](#abortcontroller) and [AbortSignal](#abortsignal) objects according to their needs. 

### 3.1. Interface [AbortController](#abortcontroller)#interface-abortcontroller

```
[Exposed=*]
interface AbortController {
  constructor#dom-abortcontroller-abortcontroller();

  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute AbortSignal#abortsignal signal#dom-abortcontroller-signal;

  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined abort#dom-abortcontroller-abort(optional anyhttps://webidl.spec.whatwg.org/#idl-any reason);
};
```

[AbortController](#dom-abortcontroller-abortcontroller)`controller = new ()`Returns a new controller whose [signal](#dom-abortcontroller-signal) is set to a newly created [AbortSignal](#abortsignal) object. [signal](#dom-abortcontroller-signal)`controller .`Returns the [AbortSignal](#abortsignal) object associated with this object. [abort](#dom-abortcontroller-abort)`controller . (reason)`Invoking this method will store reason in this object’s [AbortSignal](#abortsignal)’s [abort reason](#abortsignal-abort-reason), and signal to any observers that the associated activity is to be aborted. If reason is undefined, then an "[AbortError](https://webidl.spec.whatwg.org/#aborterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException) will be stored. 

An [AbortController](#abortcontroller) object has an associated signal (an [AbortSignal](#abortsignal) object). 

The `new AbortController()` constructor steps are: 

1. 

Let signal be a new [AbortSignal](#abortsignal) object. 

2. 

Set [this](https://webidl.spec.whatwg.org/#this)’s [signal](#abortcontroller-signal) to signal. 

The `signal` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [signal](#abortcontroller-signal). 

The `abort(reason)` method steps are to [signal abort](#abortcontroller-signal-abort) on [this](https://webidl.spec.whatwg.org/#this) with reason if it is given. 

To signal abort on an [AbortController](#abortcontroller)controller with an optional reason, [signal abort](#abortsignal-signal-abort) on controller’s [signal](#abortcontroller-signal) with reason if it is given. 

### 3.2. Interface [AbortSignal](#abortsignal)#interface-AbortSignal

```
[Exposed=*]
interface AbortSignal : EventTarget#eventtarget {
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] static AbortSignal#abortsignal abort#dom-abortsignal-abort(optional anyhttps://webidl.spec.whatwg.org/#idl-any reason);
  [Exposedhttps://webidl.spec.whatwg.org/#Exposed=(Window,Worker), NewObjecthttps://webidl.spec.whatwg.org/#NewObject] static AbortSignal#abortsignal timeout#dom-abortsignal-timeout([EnforceRangehttps://webidl.spec.whatwg.org/#EnforceRange] unsigned long longhttps://webidl.spec.whatwg.org/#idl-unsigned-long-long milliseconds);
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] static AbortSignal#abortsignal _any#dom-abortsignal-any(sequencehttps://webidl.spec.whatwg.org/#idl-sequence<AbortSignal#abortsignal> signals);

  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean aborted#dom-abortsignal-aborted;
  readonly attribute anyhttps://webidl.spec.whatwg.org/#idl-any reason#dom-abortsignal-reason;
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined throwIfAborted#dom-abortsignal-throwifaborted();

  attribute EventHandlerhttps://html.spec.whatwg.org/multipage/webappapis.html#eventhandler onabort#dom-abortsignal-onabort;
};
```

[abort](#dom-abortsignal-abort)`AbortSignal . (reason)`Returns an [AbortSignal](#abortsignal) instance whose [abort reason](#abortsignal-abort-reason) is set to reason if not undefined; otherwise to an "[AbortError](https://webidl.spec.whatwg.org/#aborterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). [any](#dom-abortsignal-any)`AbortSignal . (signals)`Returns an [AbortSignal](#abortsignal) instance which will be aborted once any of signals is aborted. Its [abort reason](#abortsignal-abort-reason) will be set to whichever one of signals caused it to be aborted. [timeout](#dom-abortsignal-timeout)`AbortSignal . (milliseconds)`Returns an [AbortSignal](#abortsignal) instance which will be aborted in milliseconds milliseconds. Its [abort reason](#abortsignal-abort-reason) will be set to a "[TimeoutError](https://webidl.spec.whatwg.org/#timeouterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). [aborted](#dom-abortsignal-aborted)`signal .`Returns true if signal’s [AbortController](#abortcontroller) has signaled to abort; otherwise false. [reason](#dom-abortsignal-reason)`signal .`Returns signal’s [abort reason](#abortsignal-abort-reason). [throwIfAborted](#dom-abortsignal-throwifaborted)`signal . ()`Throws signal’s [abort reason](#abortsignal-abort-reason), if signal’s [AbortController](#abortcontroller) has signaled to abort; otherwise, does nothing. 

An [AbortSignal](#abortsignal) object has an associated abort reason (a JavaScript value), which is initially undefined. 

An [AbortSignal](#abortsignal) object has associated abort algorithms, (a [set](https://infra.spec.whatwg.org/#ordered-set) of algorithms which are to be executed when it is [aborted](#abortsignal-aborted)), which is initially empty. 

The [abort algorithms](#abortsignal-abort-algorithms) enable APIs with complex requirements to react in a reasonable way to [abort()](#dom-abortcontroller-abort). For example, a given API’s [abort reason](#abortsignal-abort-reason) might need to be propagated to a cross-thread environment, such as a service worker. 

An [AbortSignal](#abortsignal) object has a dependent (a boolean), which is initially false. 

An [AbortSignal](#abortsignal) object has associated source signals (a weak [set](https://infra.spec.whatwg.org/#ordered-set) of [AbortSignal](#abortsignal) objects that the object is dependent on for its [aborted](#abortsignal-aborted) state), which is initially empty. 

An [AbortSignal](#abortsignal) object has associated dependent signals (a weak [set](https://infra.spec.whatwg.org/#ordered-set) of [AbortSignal](#abortsignal) objects that are dependent on the object for their [aborted](#abortsignal-aborted) state), which is initially empty. 

The static `abort(reason)` method steps are: 

1. 

Let signal be a new [AbortSignal](#abortsignal) object. 

2. 

Set signal’s [abort reason](#abortsignal-abort-reason) to reason if it is given; otherwise to a new "[AbortError](https://webidl.spec.whatwg.org/#aborterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. Return signal. 

The static `timeout(milliseconds)` method steps are: 

1. 

Let signal be a new [AbortSignal](#abortsignal) object. 

2. 

Let global be signal’s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global). 

3. 

[Run steps after a timeout](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#run-steps-after-a-timeout) given global, "`AbortSignal-timeout`", milliseconds, and the following step:

  1. 

[Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [timer task source](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#timer-task-source) given global to [signal abort](#abortsignal-signal-abort) given signal and a new "[TimeoutError](https://webidl.spec.whatwg.org/#timeouterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

For the duration of this timeout, if signal has any event listeners registered for its [abort](#eventdef-abortsignal-abort) event, there must be a strong reference from global to signal. 

4. 

Return signal. 

The static `any(signals)` method steps are to return the result of [creating a dependent abort signal](#create-a-dependent-abort-signal) from signals using [AbortSignal](#abortsignal) and the [current realm](https://tc39.es/ecma262/#current-realm). 

The `aborted` getter steps are to return true if [this](https://webidl.spec.whatwg.org/#this) is [aborted](#abortsignal-aborted); otherwise false. 

The `reason` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [abort reason](#abortsignal-abort-reason). 

The `throwIfAborted()` method steps are to throw [this](https://webidl.spec.whatwg.org/#this)’s [abort reason](#abortsignal-abort-reason), if [this](https://webidl.spec.whatwg.org/#this) is [aborted](#abortsignal-aborted). 

#example-throwifaborted

This method is primarily useful for when functions accepting [AbortSignal](#abortsignal)s want to throw (or return a rejected promise) at specific checkpoints, instead of passing along the [AbortSignal](#abortsignal) to other methods. For example, the following function allows aborting in between each attempt to poll for a condition. This gives opportunities to abort the polling process, even though the actual asynchronous operation (i.e., `await func()`) does not accept an [AbortSignal](#abortsignal). 

```
async function waitForCondition(func, targetValue, { signal } = {}) {
  while (true) {
    signal?.throwIfAborted();

    const result = await func();
    if (result === targetValue) {
      return;
    }
  }
}
```

The `onabort` attribute is an [event handler IDL attribute](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-idl-attributes) for the `onabort`[event handler](https://html.spec.whatwg.org/multipage/webappapis.html#event-handlers), whose [event handler event type](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-event-type) is `abort`. 

Changes to an [AbortSignal](#abortsignal) object represent the wishes of the corresponding [AbortController](#abortcontroller) object, but an API observing the [AbortSignal](#abortsignal) object can choose to ignore them. For instance, if the operation has already completed. 

An [AbortSignal](#abortsignal) object is aborted when its [abort reason](#abortsignal-abort-reason) is not undefined. 

To add an algorithm algorithm to an [AbortSignal](#abortsignal) object signal: 

1. 

If signal is [aborted](#abortsignal-aborted), then return. 

2. 

[Append](https://infra.spec.whatwg.org/#set-append)algorithm to signal’s [abort algorithms](#abortsignal-abort-algorithms). 

To remove an algorithm algorithm from an [AbortSignal](#abortsignal)signal, [remove](https://infra.spec.whatwg.org/#list-remove)algorithm from signal’s [abort algorithms](#abortsignal-abort-algorithms). 

To signal abort, given an [AbortSignal](#abortsignal) object signal and an optional reason: 

1. 

If signal is [aborted](#abortsignal-aborted), then return. 

2. 

Set signal’s [abort reason](#abortsignal-abort-reason) to reason if it is given; otherwise to a new "[AbortError](https://webidl.spec.whatwg.org/#aborterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

Let dependentSignalsToAbort be a new [list](https://infra.spec.whatwg.org/#list). 

4. 

[For each](https://infra.spec.whatwg.org/#list-iterate)dependentSignal of signal’s [dependent signals](#abortsignal-dependent-signals): 

  1. 

If dependentSignal is not [aborted](#abortsignal-aborted): 

    1. 

Set dependentSignal’s [abort reason](#abortsignal-abort-reason) to signal’s [abort reason](#abortsignal-abort-reason). 

    2. 

[Append](https://infra.spec.whatwg.org/#list-append)dependentSignal to dependentSignalsToAbort. 

5. 

[Run the abort steps](#run-the-abort-steps) for signal. 

6. 

[For each](https://infra.spec.whatwg.org/#list-iterate)dependentSignal of dependentSignalsToAbort, [run the abort steps](#run-the-abort-steps) for dependentSignal. 

To run the abort steps for an [AbortSignal](#abortsignal)signal: 

1. 

[For each](https://infra.spec.whatwg.org/#list-iterate)algorithm of signal’s [abort algorithms](#abortsignal-abort-algorithms): run algorithm. 

2. 

[Empty](https://infra.spec.whatwg.org/#list-empty)signal’s [abort algorithms](#abortsignal-abort-algorithms). 

3. 

[Fire an event](#concept-event-fire) named [abort](#eventdef-abortsignal-abort) at signal. 

To create a dependent abort signal from a list of [AbortSignal](#abortsignal) objects signals, using signalInterface, which must be either [AbortSignal](#abortsignal) or an interface that inherits from it, and a realm: 

1. 

Let resultSignal be a [new](https://webidl.spec.whatwg.org/#new) object implementing signalInterface using realm. 

2. 

[For each](https://infra.spec.whatwg.org/#list-iterate)signal of signals: if signal is [aborted](#abortsignal-aborted), then set resultSignal’s [abort reason](#abortsignal-abort-reason) to signal’s [abort reason](#abortsignal-abort-reason) and return resultSignal. 

3. 

Set resultSignal’s [dependent](#abortsignal-dependent) to true. 

4. 

[For each](https://infra.spec.whatwg.org/#list-iterate)signal of signals: 

  1. 

If signal’s [dependent](#abortsignal-dependent) is false: 

    1. 

[Append](https://infra.spec.whatwg.org/#set-append)signal to resultSignal’s [source signals](#abortsignal-source-signals). 

    2. 

[Append](https://infra.spec.whatwg.org/#set-append)resultSignal to signal’s [dependent signals](#abortsignal-dependent-signals). 

  2. 

Otherwise, [for each](https://infra.spec.whatwg.org/#list-iterate)sourceSignal of signal’s [source signals](#abortsignal-source-signals): 

    1. 

Assert: sourceSignal is not [aborted](#abortsignal-aborted) and not [dependent](#abortsignal-dependent). 

    2. 

[Append](https://infra.spec.whatwg.org/#set-append)sourceSignal to resultSignal’s [source signals](#abortsignal-source-signals). 

    3. 

[Append](https://infra.spec.whatwg.org/#set-append)resultSignal to sourceSignal’s [dependent signals](#abortsignal-dependent-signals). 

5. 

Return resultSignal. 

#### 3.2.1. Garbage collection#abort-signal-garbage-collection

A non-[aborted](#abortsignal-aborted)[dependent](#abortsignal-dependent)[AbortSignal](#abortsignal) object must not be garbage collected while its [source signals](#abortsignal-source-signals) is non-empty and it has registered event listeners for its [abort](#eventdef-abortsignal-abort) event or its [abort algorithms](#abortsignal-abort-algorithms) is non-empty. 

### 3.3. Using [AbortController](#abortcontroller) and [AbortSignal](#abortsignal) objects in APIs#abortcontroller-api-integration

Any web platform API using promises to represent operations that can be aborted must adhere to the following: 

- Accept [AbortSignal](#abortsignal) objects through a `signal` dictionary member. 
- Convey that the operation got aborted by rejecting the promise with [AbortSignal](#abortsignal) object’s [abort reason](#abortsignal-abort-reason). 
- Reject immediately if the [AbortSignal](#abortsignal) is already [aborted](#abortsignal-aborted), otherwise: 
- Use the [abort algorithms](#abortsignal-abort-algorithms) mechanism to observe changes to the [AbortSignal](#abortsignal) object and do so in a manner that does not lead to clashes with other observers. 

#aborting-ongoing-activities-spec-example

The method steps for a promise-returning method `doAmazingness(options)` could be as follows: 

1. 

Let global be [this](https://webidl.spec.whatwg.org/#this)’s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global). 

2. 

Let p be [a new promise](https://webidl.spec.whatwg.org/#a-new-promise). 

3. 

If options["`signal`"] [exists](https://infra.spec.whatwg.org/#map-exists): 

  1. 

Let signal be options["`signal`"]. 

  2. 

If signal is [aborted](#abortsignal-aborted), then [reject](https://webidl.spec.whatwg.org/#reject)p with signal’s [abort reason](#abortsignal-abort-reason) and return p. 

  3. 

[Add the following abort steps](#abortsignal-add) to signal: 

    1. 

Stop doing amazing things. 

    2. 

[Reject](https://webidl.spec.whatwg.org/#reject)p with signal’s [abort reason](#abortsignal-abort-reason). 

4. 

Run these steps [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel): 

  1. 

Let amazingResult be the result of doing some amazing things. 

  2. 

[Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the amazing task source given global to [resolve](https://webidl.spec.whatwg.org/#resolve)p with amazingResult. 

5. 

Return p. 

APIs not using promises should still adhere to the above as much as possible. 

## 4. Nodes#nodes

### 4.1. Introduction to "The DOM"#introduction-to-the-dom

In its original sense, "The DOM" is an API for accessing and manipulating documents (in particular, HTML and XML documents). In this specification, the term "document" is used for any markup-based resource, ranging from short static documents to long essays or reports with rich multimedia, as well as to fully-fledged interactive applications.

Each such document is represented as a [node tree](#concept-node-tree). Some of the [nodes](#concept-node) in a [tree](#concept-tree) can have [children](#concept-tree-child), while others are always leaves. 

To illustrate, consider this HTML document:

```
<!DOCTYPE html>
<html class=e>
 <head><title>Aliens?</title></head>
 <body>Why yes.</body>
</html>
```

It is represented as follows:

- [Document](#concept-document)

  - [Doctype](#concept-doctype): `html`
  - [Element](#element): `html``class`="`e`"

    - [Element](#element): `head`

      - [Element](#element): `title`

        - [Text](#text): Aliens?

    - [Text](#text): ⏎␣
    - [Element](#element): `body`

      - [Text](#text): Why yes.⏎

Note that, due to the magic that is [HTML parsing](https://html.spec.whatwg.org/multipage/parsing.html#html-parser), not all [ASCII whitespace](https://infra.spec.whatwg.org/#ascii-whitespace) were turned into [Text](#text)[nodes](#concept-node), but the general concept is clear. Markup goes in, a [tree](#concept-tree) of [nodes](#concept-node) comes out. 

The most excellent [Live DOM Viewer](https://software.hixie.ch/utilities/js/live-dom-viewer/) can be used to explore this matter in more detail. 

### 4.2. Node tree#node-trees

Nodes are objects that [implement](https://webidl.spec.whatwg.org/#implements)[Node](#node). [Nodes](#concept-node)[participate](#concept-tree-participate) in a [tree](#concept-tree), which is known as the node tree. 

In practice you deal with more specific objects. 

Objects that [implement](https://webidl.spec.whatwg.org/#implements)[Node](#node) also implement an inherited interface: [Document](#document), [DocumentType](#documenttype), [DocumentFragment](#documentfragment), [Element](#element), [CharacterData](#characterdata), or [Attr](#attr). 

Objects that implement [DocumentFragment](#documentfragment) sometimes implement [ShadowRoot](#shadowroot). 

Objects that implement [Element](#element) also typically implement an inherited interface, such as [HTMLAnchorElement](https://html.spec.whatwg.org/multipage/text-level-semantics.html#htmlanchorelement). 

Objects that implement [CharacterData](#characterdata) also implement an inherited interface: [Text](#text), [ProcessingInstruction](#processinginstruction), or [Comment](#comment). 

Objects that implement [Text](#text) sometimes implement [CDATASection](#cdatasection). 

Thus, every [node](#boundary-point-node)’s [primary interface](https://webidl.spec.whatwg.org/#dfn-primary-interface) is one of: [Document](#document), [DocumentType](#documenttype), [DocumentFragment](#documentfragment), [ShadowRoot](#shadowroot), [Element](#element) or an inherited interface of [Element](#element), [Attr](#attr), [Text](#text), [CDATASection](#cdatasection), [ProcessingInstruction](#processinginstruction), or [Comment](#comment). 

For brevity, this specification refers to an object that [implements](https://webidl.spec.whatwg.org/#implements)[Node](#node) and an inherited interface `NodeInterface`, as a `NodeInterface`[node](#concept-node). 

A [node tree](#concept-node-tree) is constrained as follows, expressed as a relationship between a [node](#concept-node) and its potential [children](#concept-tree-child): 

[Document](#document)

In [tree order](#concept-tree-order): 

1. 

Zero or more [ProcessingInstruction](#processinginstruction) or [Comment](#comment)[nodes](#concept-node). 

2. 

Optionally one [DocumentType](#documenttype)[node](#concept-node). 

3. 

Zero or more [ProcessingInstruction](#processinginstruction) or [Comment](#comment)[nodes](#concept-node). 

4. 

Optionally one [Element](#element)[node](#concept-node). 

5. 

Zero or more [ProcessingInstruction](#processinginstruction) or [Comment](#comment)[nodes](#concept-node). 

[DocumentFragment](#documentfragment)[Element](#element)

Zero or more [Element](#element) or [CharacterData](#characterdata)[nodes](#concept-node). 

[DocumentType](#documenttype)[CharacterData](#characterdata)[Attr](#attr)

No [children](#concept-tree-child). 

[Attr](#attr)[nodes](#concept-node)[participate](#concept-tree-participate) in a [tree](#concept-tree) for historical reasons; they never have a (non-null) [parent](#concept-tree-parent) or any [children](#concept-tree-child) and are therefore alone in a [tree](#concept-tree). 

To determine the length of a [node](#concept-node)node, run these steps: 

1. 

If node is a [DocumentType](#documenttype) or [Attr](#attr)[node](#concept-node), then return 0. 

2. 

If node is a [CharacterData](#characterdata)[node](#concept-node), then return node’s [data](#concept-cd-data)’s [length](https://infra.spec.whatwg.org/#string-length). 

3. 

Return the number of node’s [children](#concept-tree-child). 

A [node](#concept-node) is considered empty if its [length](#concept-node-length) is 0. 

#### 4.2.1. Document tree#document-trees

A document tree is a [node tree](#concept-node-tree) whose [root](#concept-tree-root) is a [document](#concept-document). 

The document element of a [document](#concept-document) is the [element](#concept-element) whose [parent](#concept-tree-parent) is that [document](#concept-document), if it exists; otherwise null. 

Per the [node tree](#concept-node-tree) constraints, there can be only one such [element](#concept-element). 

A [node](#concept-node) is in a document tree if its [root](#concept-tree-root) is a [document](#concept-document). 

A [node](#concept-node) is in a document if it is [in a document tree](#in-a-document-tree). The term [in a document](#in-a-document) is no longer supposed to be used. It indicates that the standard using it has not been updated to account for [shadow trees](#concept-shadow-tree).

#### 4.2.2. Shadow tree#shadow-trees

A shadow tree is a [node tree](#concept-node-tree) whose [root](#concept-tree-root) is a [shadow root](#concept-shadow-root). 

A [shadow root](#concept-shadow-root) is always attached to another [node tree](#concept-node-tree) through its [host](#concept-documentfragment-host). A [shadow tree](#concept-shadow-tree) is therefore never alone. The [node tree](#concept-node-tree) of a [shadow root](#concept-shadow-root)’s [host](#concept-documentfragment-host) is sometimes referred to as the light tree.

A [shadow tree](#concept-shadow-tree)’s corresponding [light tree](#concept-light-tree) can be a [shadow tree](#concept-shadow-tree) itself.

A [node](#concept-node) is connected if its [shadow-including root](#concept-shadow-including-root) is a [document](#concept-document). 

##### 4.2.2.1. Slots#shadow-tree-slots

A [shadow tree](#concept-shadow-tree) contains zero or more [elements](#concept-element) that are slots.

A [slot](#concept-slot) can only be created through HTML’s [slot](https://html.spec.whatwg.org/multipage/scripting.html#the-slot-element) element.

A [slot](#concept-slot) has an associated name (a string). Unless stated otherwise it is the empty string.

Use these [attribute change steps](#concept-element-attributes-change-ext) to update a [slot](#concept-slot)’s [name](#slot-name): 

1. 

If element is a [slot](#concept-slot), localName is `name`, and namespace is null: 

  1. 

If value is oldValue, then return. 

  2. 

If value is null and oldValue is the empty string, then return. 

  3. 

If value is the empty string and oldValue is null, then return. 

  4. 

If value is null or the empty string, then set element’s [name](#slot-name) to the empty string. 

  5. 

Otherwise, set element’s [name](#slot-name) to value. 

  6. 

Run [assign slottables for a tree](#assign-slotables-for-a-tree) with element’s [root](#concept-tree-root). 

The first [slot](#concept-slot) in a [shadow tree](#concept-shadow-tree), in [tree order](#concept-tree-order), whose [name](#slot-name) is the empty string, is sometimes known as the "default slot".

A [slot](#concept-slot) has an associated assigned nodes (a list of [slottables](#concept-slotable)). Unless stated otherwise it is empty.

##### 4.2.2.2. Slottables#light-tree-slotables

[Element](#element) and [Text](#text)[nodes](#concept-node) are slottables.

A [slot](#concept-slot) can be a [slottable](#concept-slotable). 

A [slottable](#concept-slotable) has an associated name (a string). Unless stated otherwise it is the empty string.

Use these [attribute change steps](#concept-element-attributes-change-ext) to update a [slottable](#concept-slotable)’s [name](#slotable-name): 

1. 

If localName is `slot` and namespace is null: 

  1. 

If value is oldValue, then return. 

  2. 

If value is null and oldValue is the empty string, then return. 

  3. 

If value is the empty string and oldValue is null, then return. 

  4. 

If value is null or the empty string, then set element’s [name](#slotable-name) to the empty string. 

  5. 

Otherwise, set element’s [name](#slotable-name) to value. 

  6. 

If element is [assigned](#slotable-assigned), then run [assign slottables](#assign-slotables) for element’s [assigned slot](#slotable-assigned-slot). 

  7. 

Run [assign a slot](#assign-a-slot) for element. 

A [slottable](#concept-slotable) has an associated assigned slot (null or a [slot](#concept-slot)). Unless stated otherwise it is null. A [slottable](#concept-slotable) is assigned if its [assigned slot](#slotable-assigned-slot) is non-null.

A [slottable](#concept-slotable) has an associated manual slot assignment (null or a [slot](#concept-slot)). Unless stated otherwise, it is null. 

A [slottable](#concept-slotable)’s [manual slot assignment](#slottable-manual-slot-assignment) can be implemented using a weak reference to the [slot](#concept-slot), because this variable is not directly accessible from script. 

##### 4.2.2.3. Finding slots and slottables#finding-slots-and-slotables

To find a slot for a given [slottable](#concept-slotable)slottable and an optional boolean open (default false): 

1. 

If slottable’s [parent](#concept-tree-parent) is null, then return null. 

2. 

Let shadow be slottable’s [parent](#concept-tree-parent)’s [shadow root](#concept-element-shadow-root). 

3. 

If shadow is null, then return null. 

4. 

If open is true and shadow’s [mode](#shadowroot-mode) is not "`open`", then return null. 

5. 

If shadow’s [slot assignment](#shadowroot-slot-assignment) is "`manual`", then return the [slot](#concept-slot) in shadow’s [descendants](#concept-tree-descendant) whose [manually assigned nodes](https://html.spec.whatwg.org/multipage/scripting.html#manually-assigned-nodes)[contains](https://infra.spec.whatwg.org/#list-contain)slottable, if any; otherwise null. 

6. 

Return the first [slot](#concept-slot) in [tree order](#concept-tree-order) in shadow’s [descendants](#concept-tree-descendant) whose [name](#slot-name) is slottable’s [name](#slotable-name), if any; otherwise null. 

To find slottables for a given [slot](#concept-slot)slot: 

1. 

Let result be « ». 

2. 

Let root be slot’s [root](#concept-tree-root). 

3. 

If root is not a [shadow root](#concept-shadow-root), then return result. 

4. 

Let host be root’s [host](#concept-documentfragment-host). 

5. 

If root’s [slot assignment](#shadowroot-slot-assignment) is "`manual`": 

  1. 

[For each](https://infra.spec.whatwg.org/#list-iterate)[slottable](#concept-slotable)slottable of slot’s [manually assigned nodes](https://html.spec.whatwg.org/multipage/scripting.html#manually-assigned-nodes), if slottable’s [parent](#concept-tree-parent) is host, [append](https://infra.spec.whatwg.org/#list-append)slottable to result. 

6. 

Otherwise, for each [slottable](#concept-slotable)[child](#concept-tree-child)slottable of host, in [tree order](#concept-tree-order): 

  1. 

Let foundSlot be the result of [finding a slot](#find-a-slot) given slottable. 

  2. 

If foundSlot is slot, then [append](https://infra.spec.whatwg.org/#list-append)slottable to result. 

7. 

Return result. 

To find flattened slottables for a given [slot](#concept-slot)slot: 

1. 

Let result be « ». 

2. 

If slot’s [root](#concept-tree-root) is not a [shadow root](#concept-shadow-root), then return result. 

3. 

Let slottables be the result of [finding slottables](#find-slotables) given slot. 

4. 

If slottables is the empty list, then append each [slottable](#concept-slotable)[child](#concept-tree-child) of slot, in [tree order](#concept-tree-order), to slottables. 

5. 

For each node of slottables: 

  1. 

If node is a [slot](#concept-slot) whose [root](#concept-tree-root) is a [shadow root](#concept-shadow-root): 

    1. 

Let temporaryResult be the result of [finding flattened slottables](#find-flattened-slotables) given node. 

    2. 

Append each [slottable](#concept-slotable) in temporaryResult, in order, to result. 

  2. 

Otherwise, append node to result. 

6. 

Return result. 

##### 4.2.2.4. Assigning slottables and slots#assigning-slotables-and-slots

To assign slottables for a [slot](#concept-slot)slot: 

1. 

Let slottables be the result of [finding slottables](#find-slotables) for slot. 

2. 

If slottables and slot’s [assigned nodes](#slot-assigned-nodes) are not identical, then run [signal a slot change](#signal-a-slot-change) for slot. 

3. 

Set slot’s [assigned nodes](#slot-assigned-nodes) to slottables. 

4. 

For each slottable of slottables: set slottable’s [assigned slot](#slotable-assigned-slot) to slot. 

To assign slottables for a tree, given a [node](#concept-node)root, run [assign slottables](#assign-slotables) for each [slot](#concept-slot) of root’s [inclusive descendants](#concept-tree-inclusive-descendant), in [tree order](#concept-tree-order). 

To assign a slot, given a [slottable](#concept-slotable)slottable: 

1. 

Let slot be the result of [finding a slot](#find-a-slot) with slottable. 

2. 

If slot is non-null, then run [assign slottables](#assign-slotables) for slot. 

##### 4.2.2.5. Signaling slot change#signaling-slot-change

Each [similar-origin window agent](https://html.spec.whatwg.org/multipage/webappapis.html#similar-origin-window-agent) has signal slots (a [set](https://infra.spec.whatwg.org/#ordered-set) of [slots](#concept-slot)), which is initially empty. [[HTML]](#biblio-html)

To signal a slot change, for a [slot](#concept-slot)slot: 

1. 

[Append](https://infra.spec.whatwg.org/#set-append)slot to slot’s [relevant agent](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-agent)’s [signal slots](#signal-slot-list). 

2. 

[Queue a mutation observer microtask](#queue-a-mutation-observer-compound-microtask). 

#### 4.2.3. Mutation algorithms#mutation-algorithms

To ensure pre-insert validity of a [node](#concept-node)node into a [node](#concept-node)parent before null or a [node](#concept-node)child: 

1. 

If parent is not a [Document](#document), [DocumentFragment](#documentfragment), or [Element](#element)[node](#concept-node), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

2. 

If node is a [host-including inclusive ancestor](#concept-tree-host-including-inclusive-ancestor) of parent, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

If child is non-null and its [parent](#concept-tree-parent) is not parent, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotFoundError](https://webidl.spec.whatwg.org/#notfounderror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

4. 

If node is not a [DocumentFragment](#documentfragment), [DocumentType](#documenttype), [Element](#element), or [CharacterData](#characterdata)[node](#concept-node), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

5. 

If either node is a [Text](#text)[node](#concept-node) and parent is a [document](#concept-document), or node is a [doctype](#concept-doctype) and parent is not a [document](#concept-document), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

6. 

If parent is a [document](#concept-document), and any of the statements below, switched on the interface node[implements](https://webidl.spec.whatwg.org/#implements), are true, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

[DocumentFragment](#documentfragment)

If node has more than one [element](#concept-element)[child](#concept-tree-child) or has a [Text](#text)[node](#concept-node)[child](#concept-tree-child). 

Otherwise, if node has one [element](#concept-element)[child](#concept-tree-child) and either parent has an [element](#concept-element)[child](#concept-tree-child), child is a [doctype](#concept-doctype), or child is non-null and a [doctype](#concept-doctype) is [following](#concept-tree-following)child. 

[Element](#element)

parent has an [element](#concept-element)[child](#concept-tree-child), child is a [doctype](#concept-doctype), or child is non-null and a [doctype](#concept-doctype) is [following](#concept-tree-following)child. 

[DocumentType](#documenttype)

parent has a [doctype](#concept-doctype)[child](#concept-tree-child), child is non-null and an [element](#concept-element) is [preceding](#concept-tree-preceding)child, or child is null and parent has an [element](#concept-element)[child](#concept-tree-child). 

To pre-insert a [node](#concept-node)node into a [node](#concept-node)parent before null or [node](#concept-node)child: 

1. 

[Ensure pre-insert validity](#concept-node-ensure-pre-insertion-validity) of node into parent before child. 

2. 

Let referenceChild be child. 

3. 

If referenceChild is node, then set referenceChild to node’s [next sibling](#concept-tree-next-sibling). 

4. 

[Insert](#concept-node-insert)node into parent before referenceChild. 

5. 

Return node. 

[Specifications](#other-applicable-specifications) may define insertion steps for all or some [nodes](#concept-node). The algorithm is passed insertedNode, as indicated in the [insert](#concept-node-insert) algorithm below. These steps must not modify the [node tree](#concept-node-tree) that insertedNode[participates](#concept-tree-participate) in, create [browsing contexts](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context), [fire events](#concept-event-fire), or otherwise execute JavaScript. These steps may [queue tasks](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) to do these things asynchronously, however. 

#example-foo-what-do-i-put-here

While the [insertion steps](#concept-node-insert-ext) cannot execute JavaScript (among other things), they will indeed have script-observable consequences. Consider the below example: 

```
const h1 = document.querySelector('h1');

const fragment = new DocumentFragment();
const script = fragment.appendChild(document.createElement('script'));
const style = fragment.appendChild(document.createElement('style'));

script.innerText= 'console.log(getComputedStyle(h1).color)'; // Logs 'rgb(255, 0, 0)'
style.innerText = 'h1 {color: rgb(255, 0, 0);}';

document.body.append(fragment);
```

The script in the above example logs `'rgb(255, 0, 0)'` because the following happen in order: 

1. 

The [insert](#concept-node-insert) algorithm runs, which will insert the [script](https://html.spec.whatwg.org/multipage/scripting.html#script) and [style](https://html.spec.whatwg.org/multipage/semantics.html#the-style-element) elements in order. 

  1. 

The HTML Standard’s [insertion steps](#concept-node-insert-ext) run for the [script](https://html.spec.whatwg.org/multipage/scripting.html#script) element; they do nothing. [[HTML]](#biblio-html)

  2. 

The HTML Standard’s [insertion steps](#concept-node-insert-ext) run for the [style](https://html.spec.whatwg.org/multipage/semantics.html#the-style-element) element; they immediately apply its style rules to the document. [[HTML]](#biblio-html)

  3. 

The HTML Standard’s [post-connection steps](#concept-node-post-connection-ext) run for the [script](https://html.spec.whatwg.org/multipage/scripting.html#script) element; they run the script, which immediately observes the style rules that were applied in the above step. [[HTML]](#biblio-html)

[Specifications](#other-applicable-specifications) may also define post-connection steps for all or some [nodes](#concept-node). The algorithm is passed connectedNode, as indicated in the [insert](#concept-node-insert) algorithm below. 

The purpose of the [post-connection steps](#concept-node-post-connection-ext) is to provide an opportunity for [nodes](#concept-node) to perform any connection-related operations that modify the [node tree](#concept-node-tree) that connectedNode[participates](#concept-tree-participate) in, create [browsing contexts](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context), or otherwise execute JavaScript. These steps allow a batch of [nodes](#concept-node) to be [inserted](#concept-node-insert)atomically with respect to script, with all major side effects occurring after the batch insertions into the [node tree](#concept-node-tree) is complete. This ensures that all pending [node tree](#concept-node-tree) insertions completely finish before more insertions can occur. 

[Specifications](#other-applicable-specifications) may define children changed steps for all or some [nodes](#concept-node). The algorithm is passed no argument and is called from [insert](#concept-node-insert), [remove](#concept-node-remove), and [replace data](#concept-cd-replace). 

To insert a [node](#concept-node)node into a [node](#concept-node)parent before null or a [node](#concept-node)child, with an optional boolean suppressObservers (default false): 

1. 

Let nodes be node’s [children](#concept-tree-child), if node is a [DocumentFragment](#documentfragment)[node](#concept-node); otherwise « node ». 

2. 

Let count be nodes’s [size](https://infra.spec.whatwg.org/#list-size). 

3. 

If count is 0, then return. 

4. 

If node is a [DocumentFragment](#documentfragment)[node](#concept-node): 

  1. 

[Remove](#concept-node-remove) its [children](#concept-tree-child) with [suppressObservers](#remove-suppressobservers) set to true. 

  2. 

[Queue a tree mutation record](#queue-a-tree-mutation-record) for node with « », nodes, null, and null. 

This step intentionally does not pay attention to suppressObservers. 

5. 

If child is non-null: 

  1. 

For each [live range](#concept-live-range) whose [start node](#concept-range-start-node) is parent and [start offset](#concept-range-start-offset) is greater than child’s [index](#concept-tree-index): increase its [start offset](#concept-range-start-offset) by count. 

  2. 

For each [live range](#concept-live-range) whose [end node](#concept-range-end-node) is parent and [end offset](#concept-range-end-offset) is greater than child’s [index](#concept-tree-index): increase its [end offset](#concept-range-end-offset) by count. 

6. 

Let previousSibling be child’s [previous sibling](#concept-tree-previous-sibling) or parent’s [last child](#concept-tree-last-child) if child is null. 

7. 

For each node in nodes, in [tree order](#concept-tree-order): 

  1. 

[Adopt](#concept-node-adopt)node into parent’s [node document](#concept-node-document). 

  2. 

If child is null, then [append](https://infra.spec.whatwg.org/#set-append)node to parent’s [children](#concept-tree-child). 

  3. 

Otherwise, [insert](https://infra.spec.whatwg.org/#list-insert)node into parent’s [children](#concept-tree-child) before child’s [index](#concept-tree-index). 

  4. 

If parent is a [shadow host](#element-shadow-host) whose [shadow root](#concept-shadow-root)’s [slot assignment](#shadowroot-slot-assignment) is "`named`" and node is a [slottable](#concept-slotable), then [assign a slot](#assign-a-slot) for node. 

  5. 

If parent’s [root](#concept-tree-root) is a [shadow root](#concept-shadow-root), and parent is a [slot](#concept-slot) whose [assigned nodes](#slot-assigned-nodes) is the empty list, then run [signal a slot change](#signal-a-slot-change) for parent. 

  6. 

Run [assign slottables for a tree](#assign-slotables-for-a-tree) with node’s [root](#concept-tree-root). 

  7. 

For each [shadow-including inclusive descendant](#concept-shadow-including-inclusive-descendant)inclusiveDescendant of node, in [shadow-including tree order](#concept-shadow-including-tree-order): 

    1. 

Run the [insertion steps](#concept-node-insert-ext) with inclusiveDescendant. 

    2. 

If inclusiveDescendant is not [connected](#connected), then [continue](https://infra.spec.whatwg.org/#iteration-continue). 

    3. 

If inclusiveDescendant is an [element](#concept-element) and inclusiveDescendant’s [custom element registry](#element-custom-element-registry) is non-null: 

      1. 

If inclusiveDescendant’s [custom element registry](#element-custom-element-registry)’s [is scoped](https://html.spec.whatwg.org/multipage/custom-elements.html#is-scoped) is true, then [append](https://infra.spec.whatwg.org/#set-append)inclusiveDescendant’s [node document](#concept-node-document) to inclusiveDescendant’s [custom element registry](#element-custom-element-registry)’s [scoped document set](https://html.spec.whatwg.org/multipage/custom-elements.html#scoped-document-set). 

      2. 

If inclusiveDescendant is [custom](#concept-element-custom), then [enqueue a custom element callback reaction](https://html.spec.whatwg.org/multipage/custom-elements.html#enqueue-a-custom-element-callback-reaction) with inclusiveDescendant, callback name "`connectedCallback`", and « ». 

      3. 

Otherwise, [try to upgrade](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-try-upgrade)inclusiveDescendant. 

If this successfully upgrades inclusiveDescendant, its `connectedCallback` will be enqueued automatically during the [upgrade an element](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-upgrade-an-element) algorithm. 

    4. 

Otherwise, if inclusiveDescendant is a [shadow root](#concept-shadow-root), inclusiveDescendant’s [custom element registry](#shadowroot-custom-element-registry) is non-null, and inclusiveDescendant’s [custom element registry](#shadowroot-custom-element-registry)’s [is scoped](https://html.spec.whatwg.org/multipage/custom-elements.html#is-scoped) is true, then [append](https://infra.spec.whatwg.org/#set-append)inclusiveDescendant’s [node document](#concept-node-document) to inclusiveDescendant’s [custom element registry](#shadowroot-custom-element-registry)’s [scoped document set](https://html.spec.whatwg.org/multipage/custom-elements.html#scoped-document-set). 

8. 

If suppressObservers is false, then [queue a tree mutation record](#queue-a-tree-mutation-record) for parent with nodes, « », previousSibling, and child. 

9. 

Run the [children changed steps](#concept-node-children-changed-ext) for parent. 

10. 

Let staticNodeList be a [list](https://infra.spec.whatwg.org/#list) of [nodes](#concept-node), initially « ».

We collect all [nodes](#concept-node)before calling the [post-connection steps](#concept-node-post-connection-ext) on any one of them, instead of calling the [post-connection steps](#concept-node-post-connection-ext)while we’re traversing the [node tree](#concept-node-tree). This is because the [post-connection steps](#concept-node-post-connection-ext) can modify the tree’s structure, making live traversal unsafe, possibly leading to the [post-connection steps](#concept-node-post-connection-ext) being called multiple times on the same [node](#boundary-point-node).

11. 

For each node of nodes, in [tree order](#concept-tree-order): 

  1. 

For each [shadow-including inclusive descendant](#concept-shadow-including-inclusive-descendant)inclusiveDescendant of node, in [shadow-including tree order](#concept-shadow-including-tree-order): [append](https://infra.spec.whatwg.org/#list-append)inclusiveDescendant to staticNodeList. 

12. 

[For each](https://infra.spec.whatwg.org/#list-iterate)node of staticNodeList: if node is [connected](#connected), then run the [post-connection steps](#concept-node-post-connection-ext) with node. 

To append a [node](#concept-node)node to a [node](#concept-node)parent: [pre-insert](#concept-node-pre-insert)node into parent before null. 

[Specifications](#other-applicable-specifications) may define moving steps for all or some [nodes](#concept-node). The algorithm is passed a [node](#concept-node)movedNode, and a [node](#concept-node)-or-null oldParent as indicated in the [move](#move) algorithm below. Like the [insertion steps](#concept-node-insert-ext), these steps must not modify the [node tree](#concept-node-tree) that movedNode[participates](#concept-tree-participate) in, create [browsing contexts](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context), [fire events](#concept-event-fire), or otherwise execute JavaScript. These steps may queue tasks to do these things asynchronously, however. 

To move a [node](#concept-node)node into a [node](#concept-node)newParent before null or a [node](#concept-node)child: 

1. 

If newParent’s [shadow-including root](#concept-shadow-including-root) is not the same as node’s [shadow-including root](#concept-shadow-including-root), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException).

This has the side effect of ensuring that a move is only performed if newParent’s [connected](#connected) is node’s [connected](#connected).

2. 

If node is a [host-including inclusive ancestor](#concept-tree-host-including-inclusive-ancestor) of newParent, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

If child is non-null and its [parent](#concept-tree-parent) is not newParent, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotFoundError](https://webidl.spec.whatwg.org/#notfounderror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

4. 

If node is not an [Element](#element) or a [CharacterData](#characterdata)[node](#concept-node), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException).

5. 

If node is a [Text](#text)[node](#concept-node) and newParent is a [document](#concept-document), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

6. 

If newParent is a [document](#concept-document), node is an [Element](#element)[node](#concept-node), and either newParent has an [element](#concept-element)[child](#concept-tree-child), child is a [doctype](#concept-doctype), or child is non-null and a [doctype](#concept-doctype) is [following](#concept-tree-following)child then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

7. 

Let oldParent be node’s [parent](#concept-tree-parent). 

8. 

[Assert](https://infra.spec.whatwg.org/#assert): oldParent is non-null. 

9. 

Run the [live range pre-remove steps](#live-range-pre-remove-steps), given node. 

10. 

For each [NodeIterator](#nodeiterator) object iterator whose [root](#concept-traversal-root)’s [node document](#concept-node-document) is node’s [node document](#concept-node-document): run the [NodeIterator pre-remove steps](#nodeiterator-pre-removing-steps) given node and iterator. 

11. 

Let oldPreviousSibling be node’s [previous sibling](#concept-tree-previous-sibling). 

12. 

Let oldNextSibling be node’s [next sibling](#concept-tree-next-sibling). 

13. 

[Remove](https://infra.spec.whatwg.org/#list-remove)node from oldParent’s [children](#concept-tree-child). 

14. 

If node is [assigned](#slotable-assigned), then run [assign slottables](#assign-slotables) for node’s [assigned slot](#slotable-assigned-slot). 

15. 

If oldParent’s [root](#concept-tree-root) is a [shadow root](#concept-shadow-root), and oldParent is a [slot](#concept-slot) whose [assigned nodes](#slot-assigned-nodes)[is empty](https://infra.spec.whatwg.org/#list-is-empty), then run [signal a slot change](#signal-a-slot-change) for oldParent. 

16. 

If node has an [inclusive descendant](#concept-tree-inclusive-descendant) that is a [slot](#concept-slot): 

  1. 

Run [assign slottables for a tree](#assign-slotables-for-a-tree) with oldParent’s [root](#concept-tree-root). 

  2. 

Run [assign slottables for a tree](#assign-slotables-for-a-tree) with node. 

17. 

If child is non-null: 

  1. 

For each [live range](#concept-live-range) whose [start node](#concept-range-start-node) is newParent and [start offset](#concept-range-start-offset) is greater than child’s [index](#concept-tree-index): increase its [start offset](#concept-range-start-offset) by 1. 

  2. 

For each [live range](#concept-live-range) whose [end node](#concept-range-end-node) is newParent and [end offset](#concept-range-end-offset) is greater than child’s [index](#concept-tree-index): increase its [end offset](#concept-range-end-offset) by 1. 

18. 

Let newPreviousSibling be child’s [previous sibling](#concept-tree-previous-sibling) if child is non-null, and newParent’s [last child](#concept-tree-last-child) otherwise. 

19. 

If child is null, then [append](https://infra.spec.whatwg.org/#set-append)node to newParent’s [children](#concept-tree-child). 

20. 

Otherwise, [insert](https://infra.spec.whatwg.org/#list-insert)node into newParent’s [children](#concept-tree-child) before child’s [index](#concept-tree-index). 

21. 

If newParent is a [shadow host](#element-shadow-host) whose [shadow root](#concept-shadow-root)’s [slot assignment](#shadowroot-slot-assignment) is "`named`" and node is a [slottable](#concept-slotable), then [assign a slot](#assign-a-slot) for node. 

22. 

If newParent’s [root](#concept-tree-root) is a [shadow root](#concept-shadow-root), and newParent is a [slot](#concept-slot) whose [assigned nodes](#slot-assigned-nodes)[is empty](https://infra.spec.whatwg.org/#list-is-empty), then run [signal a slot change](#signal-a-slot-change) for newParent. 

23. 

Run [assign slottables for a tree](#assign-slotables-for-a-tree) with node’s [root](#concept-tree-root). 

24. 

For each [shadow-including inclusive descendant](#concept-shadow-including-inclusive-descendant)inclusiveDescendant of node, in [shadow-including tree order](#concept-shadow-including-tree-order): 

  1. 

If inclusiveDescendant is node, then run the [moving steps](#concept-node-move-ext) with inclusiveDescendant and oldParent. Otherwise, run the [moving steps](#concept-node-move-ext) with inclusiveDescendant and null. 

Because the [move](#move) algorithm is a separate primitive from [insert](#concept-node-insert) and [remove](#concept-node-remove), it does not invoke the traditional [insertion steps](#concept-node-insert-ext) or [removing steps](#concept-node-remove-ext) for inclusiveDescendant. 

  2. 

If inclusiveDescendant is [custom](#concept-element-custom) and newParent is [connected](#connected), then [enqueue a custom element callback reaction](https://html.spec.whatwg.org/multipage/custom-elements.html#enqueue-a-custom-element-callback-reaction) with inclusiveDescendant, callback name "`connectedMoveCallback`", and « ». 

25. 

[Queue a tree mutation record](#queue-a-tree-mutation-record) for oldParent with « », « node », oldPreviousSibling, and oldNextSibling.

26. 

[Queue a tree mutation record](#queue-a-tree-mutation-record) for newParent with « node », « », newPreviousSibling, and child.

To replace a [node](#concept-node)child with a [node](#concept-node)node within a [node](#concept-node)parent: 

1. 

If parent is not a [Document](#document), [DocumentFragment](#documentfragment), or [Element](#element)[node](#concept-node), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

2. 

If node is a [host-including inclusive ancestor](#concept-tree-host-including-inclusive-ancestor) of parent, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

If child’s [parent](#concept-tree-parent) is not parent, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotFoundError](https://webidl.spec.whatwg.org/#notfounderror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

4. 

If node is not a [DocumentFragment](#documentfragment), [DocumentType](#documenttype), [Element](#element), or [CharacterData](#characterdata)[node](#concept-node), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

5. 

If either node is a [Text](#text)[node](#concept-node) and parent is a [document](#concept-document), or node is a [doctype](#concept-doctype) and parent is not a [document](#concept-document), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

6. 

If parent is a [document](#concept-document), and any of the statements below, switched on the interface node[implements](https://webidl.spec.whatwg.org/#implements), are true, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

[DocumentFragment](#documentfragment)

If node has more than one [element](#concept-element)[child](#concept-tree-child) or has a [Text](#text)[node](#concept-node)[child](#concept-tree-child). 

Otherwise, if node has one [element](#concept-element)[child](#concept-tree-child) and either parent has an [element](#concept-element)[child](#concept-tree-child) that is not child or a [doctype](#concept-doctype) is [following](#concept-tree-following)child. 

[Element](#element)

parent has an [element](#concept-element)[child](#concept-tree-child) that is not child or a [doctype](#concept-doctype) is [following](#concept-tree-following)child. 

[DocumentType](#documenttype)

parent has a [doctype](#concept-doctype)[child](#concept-tree-child) that is not child, or an [element](#concept-element) is [preceding](#concept-tree-preceding)child. 

The above statements differ from the [pre-insert](#concept-node-pre-insert) algorithm. 

7. 

Let referenceChild be child’s [next sibling](#concept-tree-next-sibling). 

8. 

If referenceChild is node, then set referenceChild to node’s [next sibling](#concept-tree-next-sibling). 

9. 

Let previousSibling be child’s [previous sibling](#concept-tree-previous-sibling). 

10. 

Let removedNodes be the empty set. 

11. 

If child’s [parent](#concept-tree-parent) is non-null: 

  1. 

Set removedNodes to « child ». 

  2. 

[Remove](#concept-node-remove)child with [suppressObservers](#remove-suppressobservers) set to true. 

The above can only be false if child is node. 

12. 

Let nodes be node’s [children](#concept-tree-child) if node is a [DocumentFragment](#documentfragment)[node](#concept-node); otherwise « node ». 

13. 

[Insert](#concept-node-insert)node into parent before referenceChild with [suppressObservers](#insert-suppressobservers) set to true. 

14. 

[Queue a tree mutation record](#queue-a-tree-mutation-record) for parent with nodes, removedNodes, previousSibling, and referenceChild. 

15. 

Return child. 

To replace all with a [node](#concept-node) or null node within a [node](#concept-node)parent: 

1. 

Let removedNodes be parent’s [children](#concept-tree-child). 

2. 

Let addedNodes be the empty set. 

3. 

If node is a [DocumentFragment](#documentfragment)[node](#concept-node), then set addedNodes to node’s [children](#concept-tree-child). 

4. 

Otherwise, if node is non-null, set addedNodes to « node ». 

5. 

[Remove](#concept-node-remove) all parent’s [children](#concept-tree-child), in [tree order](#concept-tree-order), with [suppressObservers](#remove-suppressobservers) set to true. 

6. 

If node is non-null, then [insert](#concept-node-insert)node into parent before null with [suppressObservers](#insert-suppressobservers) set to true. 

7. 

If either addedNodes or removedNodes[is not empty](https://infra.spec.whatwg.org/#list-is-empty), then [queue a tree mutation record](#queue-a-tree-mutation-record) for parent with addedNodes, removedNodes, null, and null. 

This algorithm does not make any checks with regards to the [node tree](#concept-node-tree) constraints. Specification authors need to use it wisely. 

To pre-remove a [node](#concept-node)child from a [node](#concept-node)parent: 

1. 

If child’s [parent](#concept-tree-parent) is not parent, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotFoundError](https://webidl.spec.whatwg.org/#notfounderror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

2. 

[Remove](#concept-node-remove)child. 

3. 

Return child. 

[Specifications](#other-applicable-specifications) may define removing steps for all or some [nodes](#concept-node). The algorithm is passed a [node](#concept-node)removedNode and a [node](#concept-node)-or-null oldParent, as indicated in the [remove](#concept-node-remove) algorithm below. 

To remove a [node](#concept-node)node, with an optional boolean suppressObservers (default false): 

1. 

Let parent be node’s [parent](#concept-tree-parent). 

2. 

Assert: parent is non-null. 

3. 

Run the [live range pre-remove steps](#live-range-pre-remove-steps), given node. 

4. 

For each [NodeIterator](#nodeiterator) object iterator whose [root](#concept-traversal-root)’s [node document](#concept-node-document) is node’s [node document](#concept-node-document): run the [NodeIterator pre-remove steps](#nodeiterator-pre-removing-steps) given node and iterator. 

5. 

Let oldPreviousSibling be node’s [previous sibling](#concept-tree-previous-sibling). 

6. 

Let oldNextSibling be node’s [next sibling](#concept-tree-next-sibling). 

7. 

[Remove](https://infra.spec.whatwg.org/#list-remove)node from its parent’s [children](#concept-tree-child). 

8. 

If node is [assigned](#slotable-assigned), then run [assign slottables](#assign-slotables) for node’s [assigned slot](#slotable-assigned-slot). 

9. 

If parent’s [root](#concept-tree-root) is a [shadow root](#concept-shadow-root), and parent is a [slot](#concept-slot) whose [assigned nodes](#slot-assigned-nodes) is the empty list, then run [signal a slot change](#signal-a-slot-change) for parent. 

10. 

If node has an [inclusive descendant](#concept-tree-inclusive-descendant) that is a [slot](#concept-slot): 

  1. 

Run [assign slottables for a tree](#assign-slotables-for-a-tree) with parent’s [root](#concept-tree-root). 

  2. 

Run [assign slottables for a tree](#assign-slotables-for-a-tree) with node. 

11. 

Run the [removing steps](#concept-node-remove-ext) with node and parent. 

12. 

Let isParentConnected be parent’s [connected](#connected). 

13. 

If node is [custom](#concept-element-custom) and isParentConnected is true, then [enqueue a custom element callback reaction](https://html.spec.whatwg.org/multipage/custom-elements.html#enqueue-a-custom-element-callback-reaction) with node, callback name "`disconnectedCallback`", and « ». 

It is intentional for now that [custom](#concept-element-custom)[elements](#concept-element) do not get parent passed. This might change in the future if there is a need. 

14. 

For each [shadow-including descendant](#concept-shadow-including-descendant)descendant of node, in [shadow-including tree order](#concept-shadow-including-tree-order): 

  1. 

Run the [removing steps](#concept-node-remove-ext) with descendant and null. 

  2. 

If descendant is [custom](#concept-element-custom) and isParentConnected is true, then [enqueue a custom element callback reaction](https://html.spec.whatwg.org/multipage/custom-elements.html#enqueue-a-custom-element-callback-reaction) with descendant, callback name "`disconnectedCallback`", and « ». 

15. 

For each [inclusive ancestor](#concept-tree-inclusive-ancestor)inclusiveAncestor of parent, and then [for each](https://infra.spec.whatwg.org/#list-iterate)registered of inclusiveAncestor’s [registered observer list](#registered-observer-list), if registered’s [options](#registered-observer-options)["[subtree](#dom-mutationobserverinit-subtree)"] is true, then [append](https://infra.spec.whatwg.org/#list-append) a new [transient registered observer](#transient-registered-observer) whose [observer](#registered-observer-observer) is registered’s [observer](#registered-observer-observer), [options](#registered-observer-options) is registered’s [options](#registered-observer-options), and [source](#transient-registered-observer-source) is registered to node’s [registered observer list](#registered-observer-list). 

16. 

If suppressObservers is false, then [queue a tree mutation record](#queue-a-tree-mutation-record) for parent with « », « node », oldPreviousSibling, and oldNextSibling. 

17. 

Run the [children changed steps](#concept-node-children-changed-ext) for parent. 

#### 4.2.4. Mixin [NonElementParentNode](#nonelementparentnode)#interface-nonelementparentnode

Web compatibility prevents the [getElementById()](#dom-nonelementparentnode-getelementbyid) method from being exposed on [elements](#concept-element) (and therefore on [ParentNode](#parentnode)). 

```
interface mixin NonElementParentNode {
  Element#element? getElementById#dom-nonelementparentnode-getelementbyid(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString elementId);
};
Document#document includes NonElementParentNode#nonelementparentnode;
DocumentFragment#documentfragment includes NonElementParentNode#nonelementparentnode;
```

[getElementById](#dom-nonelementparentnode-getelementbyid)`node . (elementId)`

Returns the first [element](#concept-element) within node’s [descendants](#concept-tree-descendant) whose [ID](#concept-id) is elementId. 

The `getElementById(elementId)` method steps are to return the first [element](#concept-element), in [tree order](#concept-tree-order), within [this](https://webidl.spec.whatwg.org/#this)’s [descendants](#concept-tree-descendant), whose [ID](#concept-id) is elementId; otherwise, if there is no such [element](#concept-element), null. 

#### 4.2.5. Mixin [DocumentOrShadowRoot](#documentorshadowroot)#mixin-documentorshadowroot

```
interface mixin DocumentOrShadowRoot {
  readonly attribute CustomElementRegistryhttps://html.spec.whatwg.org/multipage/custom-elements.html#customelementregistry? customElementRegistry#dom-documentorshadowroot-customelementregistry;
};
Document#document includes DocumentOrShadowRoot#documentorshadowroot;
ShadowRoot#shadowroot includes DocumentOrShadowRoot#documentorshadowroot;
```

[customElementRegistry](#dom-documentorshadowroot-customelementregistry)

Returns documentOrShadowRoot’s [CustomElementRegistry](https://html.spec.whatwg.org/multipage/custom-elements.html#customelementregistry) object, if any; otherwise null. 

The `customElementRegistry` getter steps are: 

1. 

If [this](https://webidl.spec.whatwg.org/#this) is a [document](#concept-document), then return [this](https://webidl.spec.whatwg.org/#this)’s [custom element registry](#document-custom-element-registry). 

2. 

[Assert](https://infra.spec.whatwg.org/#assert): [this](https://webidl.spec.whatwg.org/#this) is a [ShadowRoot](#shadowroot)[node](#concept-node). 

3. 

Return [this](https://webidl.spec.whatwg.org/#this)’s [custom element registry](#shadowroot-custom-element-registry). 

The [DocumentOrShadowRoot](#documentorshadowroot) mixin is also expected to be used by other standards that want to define APIs shared between [documents](#concept-document) and [shadow roots](#concept-shadow-root). 

#### 4.2.6. Mixin [ParentNode](#parentnode)#interface-parentnode

To convert nodes into a node, given a [list](https://infra.spec.whatwg.org/#list) of [nodes](#concept-node) and strings nodes, and [document](#concept-document)document: 

1. 

Replace each string of nodes with a new [Text](#text)[node](#concept-node) whose [data](#concept-cd-data) is the string and [node document](#concept-node-document) is document. 

2. 

If nodes’s [size](https://infra.spec.whatwg.org/#list-size) is 1, then return nodes[0]. 

3. 

Let fragment be a new [DocumentFragment](#documentfragment)[node](#concept-node) whose [node document](#concept-node-document) is document. 

4. 

For each node of nodes: [append](#concept-node-append)node to fragment. 

5. 

Return fragment. 

```
interface mixin ParentNode {
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute HTMLCollection#htmlcollection children#dom-parentnode-children;
  readonly attribute Element#element? firstElementChild#dom-parentnode-firstelementchild;
  readonly attribute Element#element? lastElementChild#dom-parentnode-lastelementchild;
  readonly attribute unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long childElementCount#dom-parentnode-childelementcount;

  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, Unscopablehttps://webidl.spec.whatwg.org/#Unscopable] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined prepend#dom-parentnode-prepend((Node#node or DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString)... nodes);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, Unscopablehttps://webidl.spec.whatwg.org/#Unscopable] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined append#dom-parentnode-append((Node#node or DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString)... nodes);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, Unscopablehttps://webidl.spec.whatwg.org/#Unscopable] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined replaceChildren#dom-parentnode-replacechildren((Node#node or DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString)... nodes);

  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined moveBefore#dom-parentnode-movebefore(Node#node node, Node#node? child);

  Element#element? querySelector#dom-parentnode-queryselector(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString selectors);
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] NodeList#nodelist querySelectorAll#dom-parentnode-queryselectorall(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString selectors);
};
Document#document includes ParentNode#parentnode;
DocumentFragment#documentfragment includes ParentNode#parentnode;
Element#element includes ParentNode#parentnode;
```

[children](#dom-parentnode-children)Returns the [child](#concept-tree-child)[elements](#concept-element). [firstElementChild](#dom-parentnode-firstelementchild)Returns the first [child](#concept-tree-child) that is an [element](#concept-element); otherwise null. [lastElementChild](#dom-parentnode-lastelementchild)Returns the last [child](#concept-tree-child) that is an [element](#concept-element); otherwise null. [prepend](#dom-parentnode-prepend)`node . (nodes)`

Inserts nodes before the [first child](#concept-tree-first-child) of node, while replacing strings in nodes with equivalent [Text](#text)[nodes](#concept-node). 

[Throws](https://webidl.spec.whatwg.org/#dfn-throw) a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException) if the constraints of the [node tree](#concept-node-tree) are violated. 

[append](#dom-parentnode-append)`node . (nodes)`

Inserts nodes after the [last child](#concept-tree-last-child) of node, while replacing strings in nodes with equivalent [Text](#text)[nodes](#concept-node). 

[Throws](https://webidl.spec.whatwg.org/#dfn-throw) a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException) if the constraints of the [node tree](#concept-node-tree) are violated. 

[replaceChildren](#dom-parentnode-replacechildren)`node . (nodes)`

Replace all [children](#concept-tree-child) of node with nodes, while replacing strings in nodes with equivalent [Text](#text)[nodes](#concept-node). 

[Throws](https://webidl.spec.whatwg.org/#dfn-throw) a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException) if the constraints of the [node tree](#concept-node-tree) are violated. 

[moveBefore](#dom-parentnode-movebefore)`node . (movedNode, child)`

Moves, without first removing, movedNode into node after child if child is non-null; otherwise after the [last child](#concept-tree-last-child) of node. This method preserves state associated with movedNode. 

[Throws](https://webidl.spec.whatwg.org/#dfn-throw) a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException) if the constraints of the [node tree](#concept-node-tree) are violated, or the state associated with the moved node cannot be preserved. 

[querySelector](#dom-parentnode-queryselector)`node . (selectors)`

Returns the first [element](#concept-element) that is a [descendant](#concept-tree-descendant) of node that matches selectors. 

[querySelectorAll](#dom-parentnode-queryselectorall)`node . (selectors)`

Returns all [element](#concept-element)[descendants](#concept-tree-descendant) of node that match selectors. 

The `children` getter steps are to return an [HTMLCollection](#htmlcollection)[collection](#concept-collection) rooted at [this](https://webidl.spec.whatwg.org/#this) matching only [element](#concept-element)[children](#concept-tree-child). 

The `firstElementChild` getter steps are to return the first [child](#concept-tree-child) that is an [element](#concept-element); otherwise null. 

The `lastElementChild` getter steps are to return the last [child](#concept-tree-child) that is an [element](#concept-element); otherwise null. 

The `childElementCount` getter steps are to return the number of [children](#concept-tree-child) of [this](https://webidl.spec.whatwg.org/#this) that are [elements](#concept-element). 

The `prepend(nodes)` method steps are: 

1. 

Let node be the result of [converting nodes into a node](#convert-nodes-into-a-node) given nodes and [this](https://webidl.spec.whatwg.org/#this)’s [node document](#concept-node-document). 

2. 

[Pre-insert](#concept-node-pre-insert)node into [this](https://webidl.spec.whatwg.org/#this) before [this](https://webidl.spec.whatwg.org/#this)’s [first child](#concept-tree-first-child). 

The `append(nodes)` method steps are: 

1. 

Let node be the result of [converting nodes into a node](#convert-nodes-into-a-node) given nodes and [this](https://webidl.spec.whatwg.org/#this)’s [node document](#concept-node-document). 

2. 

[Append](#concept-node-append)node to [this](https://webidl.spec.whatwg.org/#this). 

The `replaceChildren(nodes)` method steps are: 

1. 

Let node be the result of [converting nodes into a node](#convert-nodes-into-a-node) given nodes and [this](https://webidl.spec.whatwg.org/#this)’s [node document](#concept-node-document). 

2. 

[Ensure pre-insert validity](#concept-node-ensure-pre-insertion-validity) of node into [this](https://webidl.spec.whatwg.org/#this) before null. 

3. 

[Replace all](#concept-node-replace-all) with node within [this](https://webidl.spec.whatwg.org/#this). 

The `moveBefore(node, child)` method steps are: 

1. 

Let referenceChild be child. 

2. 

If referenceChild is node, then set referenceChild to node’s [next sibling](#concept-tree-next-sibling). 

3. 

[Move](#move)node into [this](https://webidl.spec.whatwg.org/#this) before referenceChild. 

The `querySelector(selectors)` method steps are to return the first result of running [scope-match a selectors string](#scope-match-a-selectors-string)selectors against [this](https://webidl.spec.whatwg.org/#this), if the result is not an empty list; otherwise null. 

The `querySelectorAll(selectors)` method steps are to return the [static](#concept-collection-static) result of running [scope-match a selectors string](#scope-match-a-selectors-string)selectors against [this](https://webidl.spec.whatwg.org/#this). 

#### 4.2.7. Mixin [NonDocumentTypeChildNode](#nondocumenttypechildnode)#interface-nondocumenttypechildnode

Web compatibility prevents the [previousElementSibling](#dom-nondocumenttypechildnode-previouselementsibling) and [nextElementSibling](#dom-nondocumenttypechildnode-nextelementsibling) attributes from being exposed on [doctypes](#concept-doctype) (and therefore on [ChildNode](#childnode)). 

```
interface mixin NonDocumentTypeChildNode {
  readonly attribute Element#element? previousElementSibling#dom-nondocumenttypechildnode-previouselementsibling;
  readonly attribute Element#element? nextElementSibling#dom-nondocumenttypechildnode-nextelementsibling;
};
Element#element includes NonDocumentTypeChildNode#nondocumenttypechildnode;
CharacterData#characterdata includes NonDocumentTypeChildNode#nondocumenttypechildnode;
```

[previousElementSibling](#dom-nondocumenttypechildnode-previouselementsibling)Returns the first [preceding](#concept-tree-preceding)[sibling](#concept-tree-sibling) that is an [element](#concept-element); otherwise null. [nextElementSibling](#dom-nondocumenttypechildnode-nextelementsibling)Returns the first [following](#concept-tree-following)[sibling](#concept-tree-sibling) that is an [element](#concept-element); otherwise null. 

The `previousElementSibling` getter steps are to return the first [preceding](#concept-tree-preceding)[sibling](#concept-tree-sibling) that is an [element](#concept-element); otherwise null. 

The `nextElementSibling` getter steps are to return the first [following](#concept-tree-following)[sibling](#concept-tree-sibling) that is an [element](#concept-element); otherwise null. 

#### 4.2.8. Mixin [ChildNode](#childnode)#interface-childnode

```
interface mixin ChildNode {
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, Unscopablehttps://webidl.spec.whatwg.org/#Unscopable] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined before#dom-childnode-before((Node#node or DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString)... nodes);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, Unscopablehttps://webidl.spec.whatwg.org/#Unscopable] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined after#dom-childnode-after((Node#node or DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString)... nodes);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, Unscopablehttps://webidl.spec.whatwg.org/#Unscopable] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined replaceWith#dom-childnode-replacewith((Node#node or DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString)... nodes);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, Unscopablehttps://webidl.spec.whatwg.org/#Unscopable] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined remove#dom-childnode-remove();
};
DocumentType#documenttype includes ChildNode#childnode;
Element#element includes ChildNode#childnode;
CharacterData#characterdata includes ChildNode#childnode;
```

[before(...nodes)](#dom-childnode-before)

Inserts nodes just before node, while replacing strings in nodes with equivalent [Text](#text)[nodes](#concept-node). 

[Throws](https://webidl.spec.whatwg.org/#dfn-throw) a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException) if the constraints of the [node tree](#concept-node-tree) are violated. 

[after(...nodes)](#dom-childnode-after)

Inserts nodes just after node, while replacing strings in nodes with equivalent [Text](#text)[nodes](#concept-node). 

[Throws](https://webidl.spec.whatwg.org/#dfn-throw) a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException) if the constraints of the [node tree](#concept-node-tree) are violated. 

[replaceWith(...nodes)](#dom-childnode-replacewith)

Replaces node with nodes, while replacing strings in nodes with equivalent [Text](#text)[nodes](#concept-node). 

[Throws](https://webidl.spec.whatwg.org/#dfn-throw) a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException) if the constraints of the [node tree](#concept-node-tree) are violated. 

[remove()](#dom-childnode-remove)Removes node. 

The `before(nodes)` method steps are: 

1. 

Let parent be [this](https://webidl.spec.whatwg.org/#this)’s [parent](#concept-tree-parent). 

2. 

If parent is null, then return. 

3. 

Let viablePreviousSibling be [this](https://webidl.spec.whatwg.org/#this)’s first [preceding](#concept-tree-preceding)[sibling](#concept-tree-sibling) not in nodes; otherwise null. 

4. 

Let node be the result of [converting nodes into a node](#convert-nodes-into-a-node), given nodes and [this](https://webidl.spec.whatwg.org/#this)’s [node document](#concept-node-document). 

5. 

If viablePreviousSibling is null, then set it to parent’s [first child](#concept-tree-first-child); otherwise to viablePreviousSibling’s [next sibling](#concept-tree-next-sibling). 

6. 

[Pre-insert](#concept-node-pre-insert)node into parent before viablePreviousSibling. 

The `after(nodes)` method steps are: 

1. 

Let parent be [this](https://webidl.spec.whatwg.org/#this)’s [parent](#concept-tree-parent). 

2. 

If parent is null, then return. 

3. 

Let viableNextSibling be [this](https://webidl.spec.whatwg.org/#this)’s first [following](#concept-tree-following)[sibling](#concept-tree-sibling) not in nodes; otherwise null. 

4. 

Let node be the result of [converting nodes into a node](#convert-nodes-into-a-node), given nodes and [this](https://webidl.spec.whatwg.org/#this)’s [node document](#concept-node-document). 

5. 

[Pre-insert](#concept-node-pre-insert)node into parent before viableNextSibling. 

The `replaceWith(nodes)` method steps are: 

1. 

Let parent be [this](https://webidl.spec.whatwg.org/#this)’s [parent](#concept-tree-parent). 

2. 

If parent is null, then return. 

3. 

Let viableNextSibling be [this](https://webidl.spec.whatwg.org/#this)’s first [following](#concept-tree-following)[sibling](#concept-tree-sibling) not in nodes; otherwise null. 

4. 

Let node be the result of [converting nodes into a node](#convert-nodes-into-a-node), given nodes and [this](https://webidl.spec.whatwg.org/#this)’s [node document](#concept-node-document). 

5. 

If [this](https://webidl.spec.whatwg.org/#this)’s [parent](#concept-tree-parent) is parent, [replace](#concept-node-replace)[this](https://webidl.spec.whatwg.org/#this) with node within parent. 

[This](https://webidl.spec.whatwg.org/#this) could have been inserted into node. 

6. 

Otherwise, [pre-insert](#concept-node-pre-insert)node into parent before viableNextSibling. 

The `remove()` method steps are: 

1. 

If [this](https://webidl.spec.whatwg.org/#this)’s [parent](#concept-tree-parent) is null, then return. 

2. 

[Remove](#concept-node-remove)[this](https://webidl.spec.whatwg.org/#this). 

#### 4.2.9. Mixin [Slottable](#slotable)#mixin-slotable

```
interface mixin Slottable {
  readonly attribute HTMLSlotElementhttps://html.spec.whatwg.org/multipage/scripting.html#htmlslotelement? assignedSlot#dom-slotable-assignedslot;
};
Element#element includes Slottable#slotable;
Text#text includes Slottable#slotable;
```

The `assignedSlot` getter steps are to return the result of [find a slot](#find-a-slot) given [this](https://webidl.spec.whatwg.org/#this) and true. 

#### 4.2.10. Old-style collections: [NodeList](#nodelist) and [HTMLCollection](#htmlcollection)#old-style-collections

A collection is an object that represents a list of [nodes](#concept-node). A [collection](#concept-collection) can be either live or static. Unless otherwise stated, a [collection](#concept-collection) must be [live](#concept-collection-live).

If a [collection](#concept-collection) is [live](#concept-collection-live), then the attributes and methods on that object must operate on the actual underlying data, not a snapshot of the data.

When a [collection](#concept-collection) is created, a filter and a root are associated with it.

The [collection](#concept-collection) then represents a view of the subtree rooted at the [collection’s](#concept-collection) root, containing only nodes that match the given filter. The view is linear. In the absence of specific requirements to the contrary, the nodes within the [collection](#concept-collection) must be sorted in [tree order](#concept-tree-order).

##### 4.2.10.1. Interface [NodeList](#nodelist)#interface-nodelist

A [NodeList](#nodelist) object is a [collection](#concept-collection) of [nodes](#concept-node). 

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface NodeList {
  getter Node#node? item#dom-nodelist-item(unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long index);
  readonly attribute unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long length#dom-nodelist-length;
  iterable<Node#node>;
};
```

collection . [length](#dom-nodelist-length)Returns the number of [nodes](#concept-node) in the [collection](#concept-collection). element = collection . [item(index)](#dom-nodelist-item)element = collection[index] Returns the [node](#concept-node) with index index from the [collection](#concept-collection). The [nodes](#concept-node) are sorted in [tree order](#concept-tree-order). 

The object’s [supported property indices](https://webidl.spec.whatwg.org/#dfn-supported-property-indices) are the numbers in the range zero to one less than the number of nodes [represented by the collection](#represented-by-the-collection). If there are no such elements, then there are no [supported property indices](https://webidl.spec.whatwg.org/#dfn-supported-property-indices). 

The `length` attribute must return the number of nodes [represented by the collection](#represented-by-the-collection). 

The `item(index)` method must return the indexth[node](#concept-node) in the [collection](#concept-collection). If there is no indexth[node](#concept-node) in the [collection](#concept-collection), then the method must return null. 

##### 4.2.10.2. Interface [HTMLCollection](#htmlcollection)#interface-htmlcollection

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window, LegacyUnenumerableNamedPropertieshttps://webidl.spec.whatwg.org/#LegacyUnenumerableNamedProperties]
interface HTMLCollection {
  readonly attribute unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long length#dom-htmlcollection-length;
  getter Element#element? item#dom-htmlcollection-item(unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long index);
  getter Element#element? namedItem(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString name);
};
```

An [HTMLCollection](#htmlcollection) object is a [collection](#concept-collection) of [elements](#concept-element). 

[HTMLCollection](#htmlcollection) is a historical artifact we cannot rid the web of. While developers are of course welcome to keep using it, new API standard designers ought not to use it (use `sequence<T>` in IDL instead). 

collection . [length](#dom-htmlcollection-length) Returns the number of [elements](#concept-element) in the [collection](#concept-collection). element = collection . [item(index)](#dom-htmlcollection-item)element = collection[index]  Returns the [element](#concept-element) with index index from the [collection](#concept-collection). The [elements](#concept-element) are sorted in [tree order](#concept-tree-order). element = collection . [namedItem(name)](#dom-htmlcollection-nameditem)element = collection[name]  Returns the first [element](#concept-element) with [ID](#concept-id) or name name from the collection. 

The object’s [supported property indices](https://webidl.spec.whatwg.org/#dfn-supported-property-indices) are the numbers in the range zero to one less than the number of elements [represented by the collection](#represented-by-the-collection). If there are no such elements, then there are no [supported property indices](https://webidl.spec.whatwg.org/#dfn-supported-property-indices). 

The `length` getter steps are to return the number of nodes [represented by the collection](#represented-by-the-collection). 

The `item(index)` method steps are to return the indexth[element](#concept-element) in the [collection](#concept-collection). If there is no indexth[element](#concept-element) in the [collection](#concept-collection), then the method must return null. 

The [supported property names](https://webidl.spec.whatwg.org/#dfn-supported-property-names) are the values from the list returned by these steps: 

1. 

Let result be an empty list. 

2. 

For each element[represented by the collection](#represented-by-the-collection), in [tree order](#concept-tree-order): 

  1. 

If element has an [ID](#concept-id) which is not in result, append element’s [ID](#concept-id) to result. 

  2. 

If element is in the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace) and [has](#concept-element-attribute-has) a [name attribute](#concept-named-attribute) whose [value](#concept-attribute-value) is neither the empty string nor is in result, append element’s [name attribute](#concept-named-attribute)[value](#concept-attribute-value) to result. 

3. 

Return result. 

The `namedItem(key)` method steps are: 

1. 

If key is the empty string, return null. 

2. 

Return the first [element](#concept-element) in the [collection](#concept-collection) for which at least one of the following is true: 

  - it has an [ID](#concept-id) which is key; 
  - it is in the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace) and [has](#concept-element-attribute-has) a [name attribute](#concept-named-attribute) whose [value](#concept-attribute-value) is key; 

or null if there is no such [element](#concept-element). 

### 4.3. Mutation observers#mutation-observers

Each [similar-origin window agent](https://html.spec.whatwg.org/multipage/webappapis.html#similar-origin-window-agent) has a mutation observer microtask queued (a boolean), which is initially false. [[HTML]](#biblio-html)

Each [similar-origin window agent](https://html.spec.whatwg.org/multipage/webappapis.html#similar-origin-window-agent) also has pending mutation observers (a [set](https://infra.spec.whatwg.org/#ordered-set) of zero or more [MutationObserver](#mutationobserver) objects), which is initially empty. 

To queue a mutation observer microtask: 

1. 

If the [surrounding agent](https://tc39.es/ecma262/#surrounding-agent)’s [mutation observer microtask queued](#mutation-observer-compound-microtask-queued-flag) is true, then return. 

2. 

Set the [surrounding agent](https://tc39.es/ecma262/#surrounding-agent)’s [mutation observer microtask queued](#mutation-observer-compound-microtask-queued-flag) to true. 

3. 

[Queue](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-microtask) a [microtask](https://html.spec.whatwg.org/multipage/webappapis.html#microtask) to [notify mutation observers](#notify-mutation-observers). 

To notify mutation observers: 

1. 

Set the [surrounding agent](https://tc39.es/ecma262/#surrounding-agent)’s [mutation observer microtask queued](#mutation-observer-compound-microtask-queued-flag) to false. 

2. 

Let notifySet be a [clone](https://infra.spec.whatwg.org/#list-clone) of the [surrounding agent](https://tc39.es/ecma262/#surrounding-agent)’s [pending mutation observers](#mutation-observer-list). 

3. 

[Empty](https://infra.spec.whatwg.org/#list-empty) the [surrounding agent](https://tc39.es/ecma262/#surrounding-agent)’s [pending mutation observers](#mutation-observer-list). 

4. 

Let signalSet be a [clone](https://infra.spec.whatwg.org/#list-clone) of the [surrounding agent](https://tc39.es/ecma262/#surrounding-agent)’s [signal slots](#signal-slot-list). 

5. 

[Empty](https://infra.spec.whatwg.org/#list-empty) the [surrounding agent](https://tc39.es/ecma262/#surrounding-agent)’s [signal slots](#signal-slot-list). 

6. 

[For each](https://infra.spec.whatwg.org/#list-iterate)mo of notifySet: 

  1. 

Let records be a [clone](https://infra.spec.whatwg.org/#list-clone) of mo’s [record queue](#concept-mo-queue). 

  2. 

[Empty](https://infra.spec.whatwg.org/#list-empty)mo’s [record queue](#concept-mo-queue). 

  3. 

[For each](https://infra.spec.whatwg.org/#list-iterate)node of mo’s [node list](#mutationobserver-node-list): [remove](https://infra.spec.whatwg.org/#list-remove) all [transient registered observers](#transient-registered-observer) whose [observer](#registered-observer-observer) is mo from node’s [registered observer list](#registered-observer-list). 

  4. 

If records[is not empty](https://infra.spec.whatwg.org/#list-is-empty), then [invoke](https://webidl.spec.whatwg.org/#invoke-a-callback-function)mo’s [callback](#concept-mo-callback) with « records, mo » and "`report`", and with [callback this value](https://webidl.spec.whatwg.org/#dfn-callback-this-value)mo. 

7. 

[For each](https://infra.spec.whatwg.org/#list-iterate)slot of signalSet: [fire an event](#concept-event-fire) named `slotchange`, with its [bubbles](#dom-event-bubbles) attribute set to true, at slot. 

Each [node](#concept-node) has a registered observer list (a [list](https://infra.spec.whatwg.org/#list) of zero or more [registered observers](#registered-observer)), which is initially empty. 

A registered observer consists of an observer (a [MutationObserver](#mutationobserver) object) and options (a [MutationObserverInit](#dictdef-mutationobserverinit) dictionary). 

A transient registered observer is a [registered observer](#registered-observer) that also consists of a source (a [registered observer](#registered-observer)). 

[Transient registered observers](#transient-registered-observer) are used to track mutations within a given [node](#concept-node)’s [descendants](#concept-tree-descendant) after [node](#concept-node) has been removed so they do not get lost when [subtree](#dom-mutationobserverinit-subtree) is set to true on [node](#concept-node)’s [parent](#concept-tree-parent). 

#### 4.3.1. Interface [MutationObserver](#mutationobserver)#interface-mutationobserver

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface MutationObserver {
  constructor#dom-mutationobserver-mutationobserver(MutationCallback#callbackdef-mutationcallback callback);

  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined observe#dom-mutationobserver-observe(Node#node target, optional MutationObserverInit#dictdef-mutationobserverinit options = {});
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined disconnect#dom-mutationobserver-disconnect();
  sequencehttps://webidl.spec.whatwg.org/#idl-sequence<MutationRecord#mutationrecord> takeRecords#dom-mutationobserver-takerecords();
};

callback MutationCallback = undefinedhttps://webidl.spec.whatwg.org/#idl-undefined (sequencehttps://webidl.spec.whatwg.org/#idl-sequence<MutationRecord#mutationrecord> mutations, MutationObserver#mutationobserver observer);

dictionary MutationObserverInit {
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean childList = false;
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean attributes;
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean characterData;
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean subtree = false;
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean attributeOldValue;
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean characterDataOldValue;
  sequencehttps://webidl.spec.whatwg.org/#idl-sequence<DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString> attributeFilter;
};
```

A [MutationObserver](#mutationobserver) object can be used to observe mutations to the [tree](#concept-tree) of [nodes](#concept-node). 

Each [MutationObserver](#mutationobserver) object has these associated concepts: 

- A callback set on creation. 
- A node list (a [list](https://infra.spec.whatwg.org/#list) of weak references to [nodes](#concept-node)), which is initially empty. 
- A record queue (a [queue](https://infra.spec.whatwg.org/#queue) of zero or more [MutationRecord](#mutationrecord) objects), which is initially empty. 

[MutationObserver(callback)](#dom-mutationobserver-mutationobserver)Constructs a [MutationObserver](#mutationobserver) object and sets its [callback](#concept-mo-callback) to callback. The callback is invoked with a list of [MutationRecord](#mutationrecord) objects as first argument and the constructed [MutationObserver](#mutationobserver) object as second argument. It is invoked after [nodes](#concept-node) registered with the [observe()](#dom-mutationobserver-observe) method, are mutated. [observe(target, options)](#dom-mutationobserver-observe) Instructs the user agent to observe a given target (a [node](#concept-node)) and report any mutations based on the criteria given by options (an object). 

The options argument allows for setting mutation observation options via object members. These are the object members that can be used:

[childList](#dom-mutationobserverinit-childlist)Set to true if mutations to target’s [children](#concept-tree-child) are to be observed. [attributes](#dom-mutationobserverinit-attributes)Set to true if mutations to target’s [attributes](#concept-attribute) are to be observed. Can be omitted if [attributeOldValue](#dom-mutationobserverinit-attributeoldvalue) or [attributeFilter](#dom-mutationobserverinit-attributefilter) is specified. [characterData](#dom-mutationobserverinit-characterdata)Set to true if mutations to target’s [data](#concept-cd-data) are to be observed. Can be omitted if [characterDataOldValue](#dom-mutationobserverinit-characterdataoldvalue) is specified. [subtree](#dom-mutationobserverinit-subtree)Set to true if mutations to not just target, but also target’s [descendants](#concept-tree-descendant) are to be observed. [attributeOldValue](#dom-mutationobserverinit-attributeoldvalue)Set to true if [attributes](#dom-mutationobserverinit-attributes) is true or omitted and target’s [attribute](#concept-attribute)[value](#concept-attribute-value) before the mutation needs to be recorded. [characterDataOldValue](#dom-mutationobserverinit-characterdataoldvalue)Set to true if [characterData](#dom-mutationobserverinit-characterdata) is set to true or omitted and target’s [data](#concept-cd-data) before the mutation needs to be recorded. [attributeFilter](#dom-mutationobserverinit-attributefilter)Set to a list of [attribute](#concept-attribute)[local names](#concept-attribute-local-name) (without [namespace](#concept-attribute-namespace)) if not all [attribute](#concept-attribute) mutations need to be observed and [attributes](#dom-mutationobserverinit-attributes) is true or omitted. [disconnect()](#dom-mutationobserver-disconnect)Stops observer from observing any mutations. Until the [observe()](#dom-mutationobserver-observe) method is used again, observer’s [callback](#concept-mo-callback) will not be invoked. [takeRecords()](#dom-mutationobserver-takerecords)Empties the [record queue](#concept-mo-queue) and returns what was in there. 

The `new MutationObserver(callback)` constructor steps are to set [this](https://webidl.spec.whatwg.org/#this)’s [callback](#concept-mo-callback) to callback. 

The `observe(target, options)` method steps are: 

1. 

If either options["[attributeOldValue](#dom-mutationobserverinit-attributeoldvalue)"] or options["[attributeFilter](#dom-mutationobserverinit-attributefilter)"] [exists](https://infra.spec.whatwg.org/#map-exists), and options["[attributes](#dom-mutationobserverinit-attributes)"] does not [exist](https://infra.spec.whatwg.org/#map-exists), then set options["[attributes](#dom-mutationobserverinit-attributes)"] to true. 

2. 

If options["[characterDataOldValue](#dom-mutationobserverinit-characterdataoldvalue)"] [exists](https://infra.spec.whatwg.org/#map-exists) and options["[characterData](#dom-mutationobserverinit-characterdata)"] does not [exist](https://infra.spec.whatwg.org/#map-exists), then set options["[characterData](#dom-mutationobserverinit-characterdata)"] to true. 

3. 

If none of options["[childList](#dom-mutationobserverinit-childlist)"], options["[attributes](#dom-mutationobserverinit-attributes)"], and options["[characterData](#dom-mutationobserverinit-characterdata)"] is true, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a `TypeError`. 

4. 

If options["[attributeOldValue](#dom-mutationobserverinit-attributeoldvalue)"] is true and options["[attributes](#dom-mutationobserverinit-attributes)"] is false, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a `TypeError`. 

5. 

If options["[attributeFilter](#dom-mutationobserverinit-attributefilter)"] is present and options["[attributes](#dom-mutationobserverinit-attributes)"] is false, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a `TypeError`. 

6. 

If options["[characterDataOldValue](#dom-mutationobserverinit-characterdataoldvalue)"] is true and options["[characterData](#dom-mutationobserverinit-characterdata)"] is false, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a `TypeError`. 

7. 

[For each](https://infra.spec.whatwg.org/#list-iterate)registered of target’s [registered observer list](#registered-observer-list): if registered’s [observer](#registered-observer-observer) is [this](https://webidl.spec.whatwg.org/#this): 

  1. 

[For each](https://infra.spec.whatwg.org/#list-iterate)node of [this](https://webidl.spec.whatwg.org/#this)’s [node list](#mutationobserver-node-list): [remove](https://infra.spec.whatwg.org/#list-remove) all [transient registered observers](#transient-registered-observer) whose [source](#transient-registered-observer-source) is registered from node’s [registered observer list](#registered-observer-list). 

  2. 

Set registered’s [options](#registered-observer-options) to options. 

8. 

Otherwise: 

  1. 

[Append](https://infra.spec.whatwg.org/#list-append) a new [registered observer](#registered-observer) whose [observer](#registered-observer-observer) is [this](https://webidl.spec.whatwg.org/#this) and [options](#registered-observer-options) is options to target’s [registered observer list](#registered-observer-list). 

  2. 

[Append](https://infra.spec.whatwg.org/#list-append) a weak reference to target to [this](https://webidl.spec.whatwg.org/#this)’s [node list](#mutationobserver-node-list). 

The `disconnect()` method steps are: 

1. 

[For each](https://infra.spec.whatwg.org/#list-iterate)node of [this](https://webidl.spec.whatwg.org/#this)’s [node list](#mutationobserver-node-list): [remove](https://infra.spec.whatwg.org/#list-remove) any [registered observer](#registered-observer) from node’s [registered observer list](#registered-observer-list) for which [this](https://webidl.spec.whatwg.org/#this) is the [observer](#registered-observer-observer). 

2. 

[Empty](https://infra.spec.whatwg.org/#list-empty)[this](https://webidl.spec.whatwg.org/#this)’s [record queue](#concept-mo-queue). 

The `takeRecords()` method steps are: 

1. 

Let records be a [clone](https://infra.spec.whatwg.org/#list-clone) of [this](https://webidl.spec.whatwg.org/#this)’s [record queue](#concept-mo-queue). 

2. 

[Empty](https://infra.spec.whatwg.org/#list-empty)[this](https://webidl.spec.whatwg.org/#this)’s [record queue](#concept-mo-queue). 

3. 

Return records. 

#### 4.3.2. Queuing a mutation record#queueing-a-mutation-record

To queue a mutation record of type for target with name, namespace, oldValue, addedNodes, removedNodes, previousSibling, and nextSibling: 

1. 

Let interestedObservers be an empty [map](https://infra.spec.whatwg.org/#ordered-map). 

2. 

Let nodes be the [inclusive ancestors](#concept-tree-inclusive-ancestor) of target. 

3. 

For each node of nodes, and then [for each](https://infra.spec.whatwg.org/#list-iterate)registered of node’s [registered observer list](#registered-observer-list): 

  1. 

Let options be registered’s [options](#registered-observer-options). 

  2. 

If none of the following are true 

    - node is not target and options["[subtree](#dom-mutationobserverinit-subtree)"] is false 
    - type is "`attributes`" and options["[attributes](#dom-mutationobserverinit-attributes)"] either does not [exist](https://infra.spec.whatwg.org/#map-exists) or is false 
    - type is "`attributes`", options["[attributeFilter](#dom-mutationobserverinit-attributefilter)"] [exists](https://infra.spec.whatwg.org/#map-exists), and options["[attributeFilter](#dom-mutationobserverinit-attributefilter)"] does not [contain](https://infra.spec.whatwg.org/#list-contain)name or namespace is non-null 
    - type is "`characterData`" and options["[characterData](#dom-mutationobserverinit-characterdata)"] either does not [exist](https://infra.spec.whatwg.org/#map-exists) or is false 
    - type is "`childList`" and options["[childList](#dom-mutationobserverinit-childlist)"] is false 

then: 

    1. 

Let mo be registered’s [observer](#registered-observer-observer). 

    2. 

If interestedObservers[mo] does not [exist](https://infra.spec.whatwg.org/#map-exists), then [set](https://infra.spec.whatwg.org/#map-set)interestedObservers[mo] to null. 

    3. 

If either type is "`attributes`" and options["[attributeOldValue](#dom-mutationobserverinit-attributeoldvalue)"] is true, or type is "`characterData`" and options["[characterDataOldValue](#dom-mutationobserverinit-characterdataoldvalue)"] is true, then [set](https://infra.spec.whatwg.org/#map-set)interestedObservers[mo] to oldValue. 

4. 

[For each](https://infra.spec.whatwg.org/#map-iterate)observer → mappedOldValue of interestedObservers: 

  1. 

Let record be a new [MutationRecord](#mutationrecord) object with its [type](#dom-mutationrecord-type) set to type, [target](#dom-mutationrecord-target) set to target, [attributeName](#dom-mutationrecord-attributename) set to name, [attributeNamespace](#dom-mutationrecord-attributenamespace) set to namespace, [oldValue](#dom-mutationrecord-oldvalue) set to mappedOldValue, [addedNodes](#dom-mutationrecord-addednodes) set to addedNodes, [removedNodes](#dom-mutationrecord-removednodes) set to removedNodes, [previousSibling](#dom-mutationrecord-previoussibling) set to previousSibling, and [nextSibling](#dom-mutationrecord-nextsibling) set to nextSibling. 

  2. 

[Enqueue](https://infra.spec.whatwg.org/#queue-enqueue)record to observer’s [record queue](#concept-mo-queue). 

  3. 

[Append](https://infra.spec.whatwg.org/#set-append)observer to the [surrounding agent](https://tc39.es/ecma262/#surrounding-agent)’s [pending mutation observers](#mutation-observer-list). 

5. 

[Queue a mutation observer microtask](#queue-a-mutation-observer-compound-microtask). 

To queue a tree mutation record for target with addedNodes, removedNodes, previousSibling, and nextSibling: 

1. 

[Assert](https://infra.spec.whatwg.org/#assert): either addedNodes or removedNodes[is not empty](https://infra.spec.whatwg.org/#list-is-empty). 

2. 

[Queue a mutation record](#queue-a-mutation-record) of "`childList`" for target with null, null, null, addedNodes, removedNodes, previousSibling, and nextSibling. 

#### 4.3.3. Interface [MutationRecord](#mutationrecord)#interface-mutationrecord

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface MutationRecord {
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString type#dom-mutationrecord-type;
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute Node#node target#dom-mutationrecord-target;
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute NodeList#nodelist addedNodes#dom-mutationrecord-addednodes;
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute NodeList#nodelist removedNodes#dom-mutationrecord-removednodes;
  readonly attribute Node#node? previousSibling#dom-mutationrecord-previoussibling;
  readonly attribute Node#node? nextSibling#dom-mutationrecord-nextsibling;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? attributeName#dom-mutationrecord-attributename;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? attributeNamespace#dom-mutationrecord-attributenamespace;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? oldValue#dom-mutationrecord-oldvalue;
};
```

[type](#dom-mutationrecord-type)Returns "`attributes`" if it was an [attribute](#concept-attribute) mutation. "`characterData`" if it was a mutation to a [CharacterData](#characterdata)[node](#concept-node). And "`childList`" if it was a mutation to the [tree](#concept-tree) of [nodes](#concept-node). [target](#dom-mutationrecord-target)Returns the [node](#concept-node) the mutation affected, depending on the [type](#dom-mutationrecord-type). For "`attributes`", it is the [element](#concept-element) whose [attribute](#concept-attribute) changed. For "`characterData`", it is the [CharacterData](#characterdata)[node](#concept-node). For "`childList`", it is the [node](#concept-node) whose [children](#concept-tree-child) changed. [addedNodes](#dom-mutationrecord-addednodes)[removedNodes](#dom-mutationrecord-removednodes)Return the [nodes](#concept-node) added and removed respectively. [previousSibling](#dom-mutationrecord-previoussibling)[nextSibling](#dom-mutationrecord-nextsibling)Return the [previous](#concept-tree-previous-sibling) and [next sibling](#concept-tree-next-sibling) respectively of the added or removed [nodes](#concept-node); otherwise null. [attributeName](#dom-mutationrecord-attributename)Returns the [local name](#concept-attribute-local-name) of the changed [attribute](#concept-attribute); otherwise null. [attributeNamespace](#dom-mutationrecord-attributenamespace)Returns the [namespace](#concept-attribute-namespace) of the changed [attribute](#concept-attribute); otherwise null. [oldValue](#dom-mutationrecord-oldvalue)The return value depends on [type](#dom-mutationrecord-type). For "`attributes`", it is the [value](#concept-attribute-value) of the changed [attribute](#concept-attribute) before the change. For "`characterData`", it is the [data](#concept-cd-data) of the changed [node](#concept-node) before the change. For "`childList`", it is null. 

The `type`, `target`, `addedNodes`, `removedNodes`, `previousSibling`, `nextSibling`, `attributeName`, `attributeNamespace`, and `oldValue` attributes must return the values they were initialized to. 

### 4.4. Interface [Node](#node)#interface-node

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface Node : EventTarget#eventtarget {
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short ELEMENT_NODE#dom-node-element_node = 1;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short ATTRIBUTE_NODE#dom-node-attribute_node = 2;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short TEXT_NODE#dom-node-text_node = 3;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short CDATA_SECTION_NODE#dom-node-cdata_section_node = 4;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short ENTITY_REFERENCE_NODE = 5; // legacy
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short ENTITY_NODE = 6; // legacy
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short PROCESSING_INSTRUCTION_NODE#dom-node-processing_instruction_node = 7;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short COMMENT_NODE#dom-node-comment_node = 8;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short DOCUMENT_NODE#dom-node-document_node = 9;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short DOCUMENT_TYPE_NODE#dom-node-document_type_node = 10;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short DOCUMENT_FRAGMENT_NODE#dom-node-document_fragment_node = 11;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short NOTATION_NODE = 12; // legacy
  readonly attribute unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short nodeType#dom-node-nodetype;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString nodeName#dom-node-nodename;

  readonly attribute USVStringhttps://webidl.spec.whatwg.org/#idl-USVString baseURI#dom-node-baseuri;

  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean isConnected#dom-node-isconnected;
  readonly attribute Document#document? ownerDocument#dom-node-ownerdocument;
  Node#node getRootNode#dom-node-getrootnode(optional GetRootNodeOptions#dictdef-getrootnodeoptions options = {});
  readonly attribute Node#node? parentNode#dom-node-parentnode;
  readonly attribute Element#element? parentElement#dom-node-parentelement;
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean hasChildNodes#dom-node-haschildnodes();
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute NodeList#nodelist childNodes#dom-node-childnodes;
  readonly attribute Node#node? firstChild#dom-node-firstchild;
  readonly attribute Node#node? lastChild#dom-node-lastchild;
  readonly attribute Node#node? previousSibling#dom-node-previoussibling;
  readonly attribute Node#node? nextSibling#dom-node-nextsibling;

  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? nodeValue#dom-node-nodevalue;
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? textContent#dom-node-textcontent;
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined normalize#dom-node-normalize();

  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, NewObjecthttps://webidl.spec.whatwg.org/#NewObject] Node#node cloneNode#dom-node-clonenode(optional booleanhttps://webidl.spec.whatwg.org/#idl-boolean subtree = false);
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean isEqualNode#dom-node-isequalnode(Node#node? otherNode);
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean isSameNode#dom-node-issamenode(Node#node? otherNode); // legacy alias of ===

  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short DOCUMENT_POSITION_DISCONNECTED#dom-node-document_position_disconnected = 0x01;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short DOCUMENT_POSITION_PRECEDING#dom-node-document_position_preceding = 0x02;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short DOCUMENT_POSITION_FOLLOWING#dom-node-document_position_following = 0x04;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short DOCUMENT_POSITION_CONTAINS#dom-node-document_position_contains = 0x08;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short DOCUMENT_POSITION_CONTAINED_BY#dom-node-document_position_contained_by = 0x10;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC#dom-node-document_position_implementation_specific = 0x20;
  unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short compareDocumentPosition#dom-node-comparedocumentposition(Node#node other);
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean contains#dom-node-contains(Node#node? other);

  DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? lookupPrefix#dom-node-lookupprefix(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace);
  DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? lookupNamespaceURI#dom-node-lookupnamespaceuri(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? prefix);
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean isDefaultNamespace#dom-node-isdefaultnamespace(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace);

  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Node#node insertBefore#dom-node-insertbefore(Node#node node, Node#node? child);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Node#node appendChild#dom-node-appendchild(Node#node node);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Node#node replaceChild#dom-node-replacechild(Node#node node, Node#node child);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Node#node removeChild#dom-node-removechild(Node#node child);
};

dictionary GetRootNodeOptions {
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean composed = false;
};
```

[Node](#node) is an abstract interface that is used by all [nodes](#concept-node). You cannot get a direct instance of it. 

Each [node](#concept-node) has an associated node document, set upon creation, that is a [document](#concept-document). 

A [node](#concept-node)’s [node document](#concept-node-document) can be changed by the [adopt](#concept-node-adopt) algorithm. 

A [node](#concept-node)’s [get the parent](#get-the-parent) algorithm, given an event, returns the [node](#concept-node)’s [assigned slot](#slotable-assigned-slot), if [node](#concept-node) is [assigned](#slotable-assigned); otherwise [node](#concept-node)’s [parent](#concept-tree-parent). 

Each [node](#concept-node) also has a [registered observer list](#registered-observer-list). 

[nodeType](#dom-node-nodetype)

Returns a number appropriate for the type of node, as follows: 

[Element](#element)[Node](#node)[ELEMENT_NODE](#dom-node-element_node) (1). [Attr](#attr)[Node](#node)[ATTRIBUTE_NODE](#dom-node-attribute_node) (2). An [exclusive Text node](#exclusive-text-node)[Node](#node)[TEXT_NODE](#dom-node-text_node) (3). [CDATASection](#cdatasection)[Node](#node)[CDATA_SECTION_NODE](#dom-node-cdata_section_node) (4). [ProcessingInstruction](#processinginstruction)[Node](#node)[PROCESSING_INSTRUCTION_NODE](#dom-node-processing_instruction_node) (7). [Comment](#comment)[Node](#node)[COMMENT_NODE](#dom-node-comment_node) (8). [Document](#document)[Node](#node)[DOCUMENT_NODE](#dom-node-document_node) (9). [DocumentType](#documenttype)[Node](#node)[DOCUMENT_TYPE_NODE](#dom-node-document_type_node) (10). [DocumentFragment](#documentfragment)[Node](#node)[DOCUMENT_FRAGMENT_NODE](#dom-node-document_fragment_node) (11). [nodeName](#dom-node-nodename)

Returns a string appropriate for the type of node, as follows: 

[Element](#element)Its [HTML-uppercased qualified name](#element-html-uppercased-qualified-name). [Attr](#attr)Its [qualified name](#concept-attribute-qualified-name). An [exclusive Text node](#exclusive-text-node)"`#text`". [CDATASection](#cdatasection)"`#cdata-section`". [ProcessingInstruction](#processinginstruction)Its [target](#concept-pi-target). [Comment](#comment)"`#comment`". [Document](#document)"`#document`". [DocumentType](#documenttype)Its [name](#concept-doctype-name). [DocumentFragment](#documentfragment)"`#document-fragment`". 

The `nodeType` getter steps are to return the first matching statement, switching on the interface [this](https://webidl.spec.whatwg.org/#this)[implements](https://webidl.spec.whatwg.org/#implements): 

[Element](#element)`ELEMENT_NODE` (1) [Attr](#attr)`ATTRIBUTE_NODE` (2); An [exclusive Text node](#exclusive-text-node)`TEXT_NODE` (3); [CDATASection](#cdatasection)`CDATA_SECTION_NODE` (4); [ProcessingInstruction](#processinginstruction)`PROCESSING_INSTRUCTION_NODE` (7); [Comment](#comment)`COMMENT_NODE` (8); [Document](#document)`DOCUMENT_NODE` (9); [DocumentType](#documenttype)`DOCUMENT_TYPE_NODE` (10); [DocumentFragment](#documentfragment)`DOCUMENT_FRAGMENT_NODE` (11). 

The `nodeName` getter steps are to return the first matching statement, switching on the interface [this](https://webidl.spec.whatwg.org/#this)[implements](https://webidl.spec.whatwg.org/#implements): 

[Element](#element)Its [HTML-uppercased qualified name](#element-html-uppercased-qualified-name). [Attr](#attr)Its [qualified name](#concept-attribute-qualified-name). An [exclusive Text node](#exclusive-text-node)"`#text`". [CDATASection](#cdatasection)"`#cdata-section`". [ProcessingInstruction](#processinginstruction)Its [target](#concept-pi-target). [Comment](#comment)"`#comment`". [Document](#document)"`#document`". [DocumentType](#documenttype)Its [name](#concept-doctype-name). [DocumentFragment](#documentfragment)"`#document-fragment`". [baseURI](#dom-node-baseuri)Returns node’s [node document](#concept-node-document)’s [document base URL](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#document-base-url). 

The `baseURI` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [node document](#concept-node-document)’s [document base URL](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#document-base-url), [serialized](https://url.spec.whatwg.org/#concept-url-serializer). 

[isConnected](#dom-node-isconnected)

Returns true if node is [connected](#connected); otherwise false. 

[ownerDocument](#dom-node-ownerdocument) Returns the [node document](#concept-node-document). Returns null for [documents](#concept-document). [getRootNode()](#dom-node-getrootnode)Returns node’s [root](#concept-tree-root). [getRootNode](#dom-node-getrootnode)`node . ({ composed:true })`Returns node’s [shadow-including root](#concept-shadow-including-root). [parentNode](#dom-node-parentnode)Returns the [parent](#concept-tree-parent). [parentElement](#dom-node-parentelement)Returns the [parent element](#parent-element). [hasChildNodes()](#dom-node-haschildnodes)Returns whether node has [children](#concept-tree-child). [childNodes](#dom-node-childnodes)Returns the [children](#concept-tree-child). [firstChild](#dom-node-firstchild)Returns the [first child](#concept-tree-first-child). [lastChild](#dom-node-lastchild)Returns the [last child](#concept-tree-last-child). [previousSibling](#dom-node-previoussibling)Returns the [previous sibling](#concept-tree-previous-sibling). [nextSibling](#dom-node-nextsibling)Returns the [next sibling](#concept-tree-next-sibling). 

The `isConnected` getter steps are to return true, if [this](https://webidl.spec.whatwg.org/#this) is [connected](#connected); otherwise false.

The `ownerDocument` getter steps are to return null, if [this](https://webidl.spec.whatwg.org/#this) is a [document](#concept-document); otherwise [this](https://webidl.spec.whatwg.org/#this)’s [node document](#concept-node-document). 

The [node document](#concept-node-document) of a [document](#concept-document) is that [document](#concept-document) itself. All [nodes](#concept-node) have a [node document](#concept-node-document) at all times. 

The `getRootNode(options)` method steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [shadow-including root](#concept-shadow-including-root) if options["[composed](#dom-getrootnodeoptions-composed)"] is true; otherwise [this](https://webidl.spec.whatwg.org/#this)’s [root](#concept-tree-root). 

The `parentNode` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [parent](#concept-tree-parent). 

The `parentElement` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [parent element](#parent-element). 

The `hasChildNodes()` method steps are to return true if [this](https://webidl.spec.whatwg.org/#this) has [children](#concept-tree-child); otherwise false. 

The `childNodes` getter steps are to return a [NodeList](#nodelist) rooted at [this](https://webidl.spec.whatwg.org/#this) matching only [children](#concept-tree-child). 

The `firstChild` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [first child](#concept-tree-first-child). 

The `lastChild` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [last child](#concept-tree-last-child). 

The `previousSibling` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [previous sibling](#concept-tree-previous-sibling). 

The `nextSibling` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [next sibling](#concept-tree-next-sibling). 

The `nodeValue` getter steps are to return the following, switching on the interface [this](https://webidl.spec.whatwg.org/#this)[implements](https://webidl.spec.whatwg.org/#implements): 

[Attr](#attr)[this](https://webidl.spec.whatwg.org/#this)’s [value](#concept-attribute-value). [CharacterData](#characterdata)[this](https://webidl.spec.whatwg.org/#this)’s [data](#concept-cd-data). Otherwise Null. 

The [nodeValue](#dom-node-nodevalue) setter steps are to, if the given value is null, act as if it was the empty string instead, and then do as described below, switching on the interface [this](https://webidl.spec.whatwg.org/#this)[implements](https://webidl.spec.whatwg.org/#implements): 

[Attr](#attr)

[Set an existing attribute value](#set-an-existing-attribute-value) with [this](https://webidl.spec.whatwg.org/#this) and the given value. 

[CharacterData](#characterdata)

[Replace data](#concept-cd-replace) of [this](https://webidl.spec.whatwg.org/#this) with 0, [this](https://webidl.spec.whatwg.org/#this)’s [length](#concept-node-length), and the given value. 

Otherwise 

Do nothing. 

To get text content with a [node](#concept-node)node, return the following, switching on the interface node[implements](https://webidl.spec.whatwg.org/#implements): 

[DocumentFragment](#documentfragment)[Element](#element)The [descendant text content](#concept-descendant-text-content) of node. [Attr](#attr)node’s [value](#concept-attribute-value). [CharacterData](#characterdata)node’s [data](#concept-cd-data). Otherwise Null. 

The `textContent` getter steps are to return the result of running [get text content](#get-text-content) with [this](https://webidl.spec.whatwg.org/#this). 

To string replace all with a string string within a [node](#concept-node)parent, run these steps: 

1. 

Let node be null. 

2. 

If string is not the empty string, then set node to a new [Text](#text)[node](#concept-node) whose [data](#concept-cd-data) is string and [node document](#concept-node-document) is parent’s [node document](#concept-node-document). 

3. 

[Replace all](#concept-node-replace-all) with node within parent. 

To set text content with a [node](#concept-node)node and a string value, do as defined below, switching on the interface node[implements](https://webidl.spec.whatwg.org/#implements): 

[DocumentFragment](#documentfragment)[Element](#element)

[String replace all](#string-replace-all) with value within node. 

[Attr](#attr)

[Set an existing attribute value](#set-an-existing-attribute-value) with node and value. 

[CharacterData](#characterdata)

[Replace data](#concept-cd-replace) of node with 0, node’s [length](#concept-node-length), and value. 

Otherwise 

Do nothing. 

The [textContent](#dom-node-textcontent) setter steps are to, if the given value is null, act as if it was the empty string instead, and then run [set text content](#set-text-content) with [this](https://webidl.spec.whatwg.org/#this) and the given value. 

[normalize()](#dom-node-normalize)Removes [empty](#concept-node-empty)[exclusive Text nodes](#exclusive-text-node) and concatenates the [data](#concept-cd-data) of remaining [contiguous exclusive Text nodes](#contiguous-exclusive-text-nodes) into the first of their [nodes](#concept-node). 

The `normalize()` method steps are to run these steps for each [descendant](#concept-tree-descendant)[exclusive Text node](#exclusive-text-node)node of [this](https://webidl.spec.whatwg.org/#this): 

1. 

Let length be node’s [length](#concept-node-length). 

2. 

If length is zero, then [remove](#concept-node-remove)node and continue with the next [exclusive Text node](#exclusive-text-node), if any. 

3. 

Let data be the [concatenation](https://infra.spec.whatwg.org/#string-concatenate) of the [data](#concept-cd-data) of node’s [contiguous exclusive Text nodes](#contiguous-exclusive-text-nodes) (excluding itself), in [tree order](#concept-tree-order). 

4. 

[Replace data](#concept-cd-replace) of node with length, 0, and data. 

5. 

Let currentNode be node’s [next sibling](#concept-tree-next-sibling). 

6. 

While currentNode is an [exclusive Text node](#exclusive-text-node): 

  1. 

For each [live range](#concept-live-range) whose [start node](#concept-range-start-node) is currentNode: add length to its [start offset](#concept-range-start-offset) and set its [start node](#concept-range-start-node) to node. 

  2. 

For each [live range](#concept-live-range) whose [end node](#concept-range-end-node) is currentNode: add length to its [end offset](#concept-range-end-offset) and set its [end node](#concept-range-end-node) to node. 

  3. 

For each [live range](#concept-live-range) whose [start node](#concept-range-start-node) is currentNode’s [parent](#concept-tree-parent) and [start offset](#concept-range-start-offset) is currentNode’s [index](#concept-tree-index): set its [start node](#concept-range-start-node) to node and its [start offset](#concept-range-start-offset) to length. 

  4. 

For each [live range](#concept-live-range) whose [end node](#concept-range-end-node) is currentNode’s [parent](#concept-tree-parent) and [end offset](#concept-range-end-offset) is currentNode’s [index](#concept-tree-index): set its [end node](#concept-range-end-node) to node and its [end offset](#concept-range-end-offset) to length. 

  5. 

Add currentNode’s [length](#concept-node-length) to length. 

  6. 

Set currentNode to its [next sibling](#concept-tree-next-sibling). 

7. 

[Remove](#concept-node-remove)node’s [contiguous exclusive Text nodes](#contiguous-exclusive-text-nodes) (excluding itself), in [tree order](#concept-tree-order). 

[cloneNode](#dom-node-clonenode)`node . ([subtree = false])`Returns a copy of node. If subtree is true, the copy also includes the node’s [descendants](#concept-tree-descendant). [isEqualNode](#dom-node-isequalnode)`node . (otherNode)`Returns whether node and otherNode have the same properties. [Specifications](#other-applicable-specifications) may define cloning steps for all or some [nodes](#concept-node). The algorithm is passed node, copy, and subtree as indicated in the [clone a node](#concept-node-clone) algorithm. 

HTML defines [cloning steps](#concept-node-clone-ext) for several elements, such as [input](https://html.spec.whatwg.org/multipage/input.html#the-input-element), [script](https://html.spec.whatwg.org/multipage/scripting.html#script), and [template](https://html.spec.whatwg.org/multipage/scripting.html#the-template-element). SVG ought to do the same for its [script](https://html.spec.whatwg.org/multipage/scripting.html#script) elements, but does not. 

To clone a node given a [node](#concept-node)node and an optional [document](#concept-document)document (default node’s [node document](#concept-node-document)), boolean subtree (default false), [node](#concept-node)-or-null parent (default null), and null or a [CustomElementRegistry](https://html.spec.whatwg.org/multipage/custom-elements.html#customelementregistry) object fallbackRegistry (default null): 

1. 

[Assert](https://infra.spec.whatwg.org/#assert): node is not a [document](#concept-document) or node is document. 

2. 

Let copy be the result of [cloning a single node](#clone-a-single-node) given node, document, and fallbackRegistry. 

3. 

Run any [cloning steps](#concept-node-clone-ext) defined for node in [other applicable specifications](#other-applicable-specifications) and pass node, copy, and subtree as parameters. 

4. 

If parent is non-null, then [append](#concept-node-append)copy to parent. 

5. 

If subtree is true, then for each child of node’s [children](#concept-tree-child), in [tree order](#concept-tree-order): [clone a node](#concept-node-clone) given child with [document](#clone-a-node-document) set to document, [subtree](#clone-a-node-subtree) set to subtree, [parent](#clone-a-node-parent) set to copy, and [fallbackRegistry](#clone-a-node-fallbackregistry) set to fallbackRegistry. 

6. 

If node is an [element](#concept-element), node is a [shadow host](#element-shadow-host), and node’s [shadow root](#concept-element-shadow-root)’s [clonable](#shadowroot-clonable) is true: 

  1. 

[Assert](https://infra.spec.whatwg.org/#assert): copy is not a [shadow host](#element-shadow-host). 

  2. 

Let shadowRootRegistry be node’s [shadow root](#concept-element-shadow-root)’s [custom element registry](#shadowroot-custom-element-registry). 

  3. 

If shadowRootRegistry[is a global custom element registry](#is-a-global-custom-element-registry), then set shadowRootRegistry to document’s [effective global custom element registry](#effective-global-custom-element-registry). 

  4. 

[Attach a shadow root](#concept-attach-a-shadow-root) with copy, node’s [shadow root](#concept-element-shadow-root)’s [mode](#shadowroot-mode), true, node’s [shadow root](#concept-element-shadow-root)’s [serializable](#shadowroot-serializable), node’s [shadow root](#concept-element-shadow-root)’s [delegates focus](#shadowroot-delegates-focus), node’s [shadow root](#concept-element-shadow-root)’s [slot assignment](#shadowroot-slot-assignment), and shadowRootRegistry. 

  5. 

Set copy’s [shadow root](#concept-element-shadow-root)’s [declarative](#shadowroot-declarative) to node’s [shadow root](#concept-element-shadow-root)’s [declarative](#shadowroot-declarative). 

  6. 

For each child of node’s [shadow root](#concept-element-shadow-root)’s [children](#concept-tree-child), in [tree order](#concept-tree-order): [clone a node](#concept-node-clone) given child with [document](#clone-a-node-document) set to document, [subtree](#clone-a-node-subtree) set to subtree, and [parent](#clone-a-node-parent) set to copy’s [shadow root](#concept-element-shadow-root). 

This intentionally does not pass the [fallbackRegistry](#clone-a-node-fallbackregistry) argument. 

7. 

Return copy. 

To clone a single node given a [node](#concept-node)node, [document](#concept-document)document, and null or a [CustomElementRegistry](https://html.spec.whatwg.org/multipage/custom-elements.html#customelementregistry) object fallbackRegistry: 

1. 

Let copy be null. 

2. 

If node is an [element](#concept-element): 

  1. 

Let registry be node’s [custom element registry](#element-custom-element-registry). 

  2. 

If registry is null, then set registry to fallbackRegistry. 

  3. 

If registry[is a global custom element registry](#is-a-global-custom-element-registry), then set registry to document’s [effective global custom element registry](#effective-global-custom-element-registry). 

  4. 

Set copy to the result of [creating an element](#concept-create-element), given document, node’s [local name](#concept-element-local-name), node’s [namespace](#concept-element-namespace), node’s [namespace prefix](#concept-element-namespace-prefix), node’s [is value](#concept-element-is-value), false, and registry. 

  5. 

[For each](https://infra.spec.whatwg.org/#list-iterate)attribute of node’s [attribute list](#concept-element-attribute): 

    1. 

Let copyAttribute be the result of [cloning a single node](#clone-a-single-node) given attribute, document, and null. 

    2. 

[Append](#concept-element-attributes-append)copyAttribute to copy. 

3. 

Otherwise, set copy to a [node](#concept-node) that [implements](https://webidl.spec.whatwg.org/#implements) the same interfaces as node, and fulfills these additional requirements, switching on the interface node[implements](https://webidl.spec.whatwg.org/#implements): 

[Document](#document)

  1. 

Set copy’s [encoding](#concept-document-encoding), [content type](#concept-document-content-type), [URL](#concept-document-url), [origin](#concept-document-origin), [type](#concept-document-type), [mode](#concept-document-mode), and [allow declarative shadow roots](#document-allow-declarative-shadow-roots), to those of node. 

  2. 

If node’s [custom element registry](#document-custom-element-registry)’s [is scoped](https://html.spec.whatwg.org/multipage/custom-elements.html#is-scoped) is true, then set copy’s [custom element registry](#document-custom-element-registry) to node’s [custom element registry](#document-custom-element-registry). 

[DocumentType](#documenttype)

Set copy’s [name](#concept-doctype-name), [public ID](#concept-doctype-publicid), and [system ID](#concept-doctype-systemid) to those of node. 

[Attr](#attr)

Set copy’s [namespace](#concept-attribute-namespace), [namespace prefix](#concept-attribute-namespace-prefix), [local name](#concept-attribute-local-name), and [value](#concept-attribute-value) to those of node. 

[Text](#text)[Comment](#comment)

Set copy’s [data](#concept-cd-data) to that of node. 

[ProcessingInstruction](#processinginstruction)

Set copy’s [target](#concept-pi-target) and [data](#concept-cd-data) to those of node. 

Otherwise 

Do nothing. 

4. 

[Assert](https://infra.spec.whatwg.org/#assert): copy is a [node](#concept-node). 

5. 

If node is a [document](#concept-document), then set document to copy. 

6. 

Set copy’s [node document](#concept-node-document) to document. 

7. 

Return copy. 

The `cloneNode(subtree)` method steps are: 

1. 

If [this](https://webidl.spec.whatwg.org/#this) is a [shadow root](#concept-shadow-root), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotSupportedError](https://webidl.spec.whatwg.org/#notsupportederror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

2. 

Return the result of [cloning a node](#concept-node-clone) given [this](https://webidl.spec.whatwg.org/#this) with [subtree](#clone-a-node-subtree) set to subtree. 

A [node](#concept-node)Aequals a [node](#concept-node)B if all of the following conditions are true: 

- 

A and B[implement](https://webidl.spec.whatwg.org/#implements) the same interfaces. 

- 

The following are equal, switching on the interface A[implements](https://webidl.spec.whatwg.org/#implements): 

[DocumentType](#documenttype)Its [name](#concept-doctype-name), [public ID](#concept-doctype-publicid), and [system ID](#concept-doctype-systemid). [Element](#element)Its [namespace](#concept-element-namespace), [namespace prefix](#concept-element-namespace-prefix), [local name](#concept-element-local-name), and its [attribute list](#concept-element-attribute)’s [size](https://infra.spec.whatwg.org/#list-size). [Attr](#attr)Its [namespace](#concept-attribute-namespace), [local name](#concept-attribute-local-name), and [value](#concept-attribute-value). [ProcessingInstruction](#processinginstruction)Its [target](#concept-pi-target) and [data](#concept-cd-data). [Text](#text)[Comment](#comment)Its [data](#concept-cd-data). Otherwise — 
- 

If A is an [element](#concept-element), each [attribute](#concept-attribute) in its [attribute list](#concept-element-attribute) has an [attribute](#concept-attribute) that [equals](#concept-node-equals) an [attribute](#concept-attribute) in B’s [attribute list](#concept-element-attribute). 

- 

A and B have the same number of [children](#concept-tree-child). 

- 

Each [child](#concept-tree-child) of A[equals](#concept-node-equals) the [child](#concept-tree-child) of B at the identical [index](#concept-tree-index). 

The `isEqualNode(otherNode)` method steps are to return true if otherNode is non-null and [this](https://webidl.spec.whatwg.org/#this)[equals](#concept-node-equals)otherNode; otherwise false. 

The `isSameNode(otherNode)` method steps are to return true if otherNode is [this](https://webidl.spec.whatwg.org/#this); otherwise false. 

[compareDocumentPosition(other)](#dom-node-comparedocumentposition) Returns a bitmask indicating the position of other relative to node. These are the bits that can be set: [Node](#node)[DOCUMENT_POSITION_DISCONNECTED](#dom-node-document_position_disconnected) (1) Set when node and other are not in the same [tree](#concept-tree). [Node](#node)[DOCUMENT_POSITION_PRECEDING](#dom-node-document_position_preceding) (2) Set when other is [preceding](#concept-tree-preceding)node. [Node](#node)[DOCUMENT_POSITION_FOLLOWING](#dom-node-document_position_following) (4) Set when other is [following](#concept-tree-following)node. [Node](#node)[DOCUMENT_POSITION_CONTAINS](#dom-node-document_position_contains) (8) Set when other is an [ancestor](#concept-tree-ancestor) of node. [Node](#node)[DOCUMENT_POSITION_CONTAINED_BY](#dom-node-document_position_contained_by) (16, 10 in hexadecimal) Set when other is a [descendant](#concept-tree-descendant) of node. [contains(other)](#dom-node-contains)Returns true if other is an [inclusive descendant](#concept-tree-inclusive-descendant) of node; otherwise false. 

These are the constants [compareDocumentPosition()](#dom-node-comparedocumentposition) returns as mask: 

- `DOCUMENT_POSITION_DISCONNECTED` (1); 
- `DOCUMENT_POSITION_PRECEDING` (2); 
- `DOCUMENT_POSITION_FOLLOWING` (4); 
- `DOCUMENT_POSITION_CONTAINS` (8); 
- `DOCUMENT_POSITION_CONTAINED_BY` (16, 10 in hexadecimal); 
- `DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC` (32, 20 in hexadecimal). 

The `compareDocumentPosition(other)` method steps are: 

1. 

If [this](https://webidl.spec.whatwg.org/#this) is other, then return zero. 

2. 

Let node1 be other and node2 be [this](https://webidl.spec.whatwg.org/#this). 

3. 

Let attr1 and attr2 be null. 

4. 

If node1 is an [attribute](#concept-attribute), then set attr1 to node1 and node1 to attr1’s [element](#concept-attribute-element). 

5. 

If node2 is an [attribute](#concept-attribute): 

  1. 

Set attr2 to node2 and node2 to attr2’s [element](#concept-attribute-element). 

  2. 

If attr1 and node1 are non-null, and node2 is node1: 

    1. 

[For each](https://infra.spec.whatwg.org/#list-iterate)attr of node2’s [attribute list](#concept-element-attribute): 

      1. 

If attr[equals](#concept-node-equals)attr1, then return the result of adding [DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC](#dom-node-document_position_implementation_specific) and [DOCUMENT_POSITION_PRECEDING](#dom-node-document_position_preceding). 

      2. 

If attr[equals](#concept-node-equals)attr2, then return the result of adding [DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC](#dom-node-document_position_implementation_specific) and [DOCUMENT_POSITION_FOLLOWING](#dom-node-document_position_following). 

6. 

If node1 or node2 is null, or node1’s [root](#concept-tree-root) is not node2’s [root](#concept-tree-root), then return the result of adding [DOCUMENT_POSITION_DISCONNECTED](#dom-node-document_position_disconnected), [DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC](#dom-node-document_position_implementation_specific), and either [DOCUMENT_POSITION_PRECEDING](#dom-node-document_position_preceding) or [DOCUMENT_POSITION_FOLLOWING](#dom-node-document_position_following), with the constraint that this is to be consistent, together. 

Whether to return [DOCUMENT_POSITION_PRECEDING](#dom-node-document_position_preceding) or [DOCUMENT_POSITION_FOLLOWING](#dom-node-document_position_following) is typically implemented via pointer comparison. In JavaScript implementations a cached `Math.random()` value can be used. 

7. 

If node1 is an [ancestor](#concept-tree-ancestor) of node2 and attr1 is null, or node1 is node2 and attr2 is non-null, then return the result of adding [DOCUMENT_POSITION_CONTAINS](#dom-node-document_position_contains) to [DOCUMENT_POSITION_PRECEDING](#dom-node-document_position_preceding). 

8. 

If node1 is a [descendant](#concept-tree-descendant) of node2 and attr2 is null, or node1 is node2 and attr1 is non-null, then return the result of adding [DOCUMENT_POSITION_CONTAINED_BY](#dom-node-document_position_contained_by) to [DOCUMENT_POSITION_FOLLOWING](#dom-node-document_position_following). 

9. 

If node1 is [preceding](#concept-tree-preceding)node2, then return [DOCUMENT_POSITION_PRECEDING](#dom-node-document_position_preceding). 

Due to the way [attributes](#concept-attribute) are handled in this algorithm this results in a [node](#concept-node)’s [attributes](#concept-attribute) counting as [preceding](#concept-tree-preceding) that [node](#concept-node)’s [children](#concept-tree-child), despite [attributes](#concept-attribute) not [participating](#concept-tree-participate) in the same [tree](#concept-tree). 

10. 

Return [DOCUMENT_POSITION_FOLLOWING](#dom-node-document_position_following). 

The `contains(other)` method steps are to return true if other is an [inclusive descendant](#concept-tree-inclusive-descendant) of [this](https://webidl.spec.whatwg.org/#this); otherwise false (including when other is null). 

To locate a namespace prefix for an element using namespace, run these steps: 

1. 

If element’s [namespace](#concept-element-namespace) is namespace and its [namespace prefix](#concept-element-namespace-prefix) is non-null, then return its [namespace prefix](#concept-element-namespace-prefix). 

2. 

If element[has](#concept-element-attribute-has) an [attribute](#concept-attribute) whose [namespace prefix](#concept-attribute-namespace-prefix) is "`xmlns`" and [value](#concept-attribute-value) is namespace, then return element’s first such [attribute](#concept-attribute)’s [local name](#concept-attribute-local-name). 

3. 

If element’s [parent element](#parent-element) is non-null, then return the result of running [locate a namespace prefix](#locate-a-namespace-prefix) on that [element](#concept-element) using namespace. 

4. 

Return null. 

To locate a namespace for a node using prefix, switch on the interface node[implements](https://webidl.spec.whatwg.org/#implements): 

[Element](#element)

1. 

If prefix is "`xml`", then return the [XML namespace](https://infra.spec.whatwg.org/#xml-namespace). 

2. 

If prefix is "`xmlns`", then return the [XMLNS namespace](https://infra.spec.whatwg.org/#xmlns-namespace). 

3. 

If its [namespace](#concept-element-namespace) is non-null and its [namespace prefix](#concept-element-namespace-prefix) is prefix, then return [namespace](#concept-element-namespace). 

4. 

If it [has](#concept-element-attribute-has) an [attribute](#concept-attribute) whose [namespace](#concept-attribute-namespace) is the [XMLNS namespace](https://infra.spec.whatwg.org/#xmlns-namespace), [namespace prefix](#concept-attribute-namespace-prefix) is "`xmlns`", and [local name](#concept-attribute-local-name) is prefix, or if prefix is null and it [has](#concept-element-attribute-has) an [attribute](#concept-attribute) whose [namespace](#concept-attribute-namespace) is the [XMLNS namespace](https://infra.spec.whatwg.org/#xmlns-namespace), [namespace prefix](#concept-attribute-namespace-prefix) is null, and [local name](#concept-attribute-local-name) is "`xmlns`", then return its [value](#concept-attribute-value) if it is not the empty string, and null otherwise. 

5. 

If its [parent element](#parent-element) is null, then return null. 

6. 

Return the result of running [locate a namespace](#locate-a-namespace) on its [parent element](#parent-element) using prefix. 

[Document](#document)

1. 

If its [document element](#document-element) is null, then return null. 

2. 

Return the result of running [locate a namespace](#locate-a-namespace) on its [document element](#document-element) using prefix. 

[DocumentType](#documenttype)[DocumentFragment](#documentfragment)

Return null. 

[Attr](#attr)

1. 

If its [element](#concept-attribute-element) is null, then return null. 

2. 

Return the result of running [locate a namespace](#locate-a-namespace) on its [element](#concept-attribute-element) using prefix. 

Otherwise 

1. 

If its [parent element](#parent-element) is null, then return null. 

2. 

Return the result of running [locate a namespace](#locate-a-namespace) on its [parent element](#parent-element) using prefix. 

The `lookupPrefix(namespace)` method steps are: 

1. 

If namespace is null or the empty string, then return null. 

2. 

Switch on the interface [this](https://webidl.spec.whatwg.org/#this)[implements](https://webidl.spec.whatwg.org/#implements): 

[Element](#element)

Return the result of [locating a namespace prefix](#locate-a-namespace-prefix) for [this](https://webidl.spec.whatwg.org/#this) using namespace. 

[Document](#document)

  1. 

If [this](https://webidl.spec.whatwg.org/#this)’s [document element](#document-element) is null, then return null. 

  2. 

Return the result of [locating a namespace prefix](#locate-a-namespace-prefix) for [this](https://webidl.spec.whatwg.org/#this)’s [document element](#document-element) using namespace. 

[DocumentType](#documenttype)[DocumentFragment](#documentfragment)

Return null. 

[Attr](#attr)

  1. 

If [this](https://webidl.spec.whatwg.org/#this)’s [element](#concept-attribute-element) is null, then return null. 

  2. 

Return the result of [locating a namespace prefix](#locate-a-namespace-prefix) for [this](https://webidl.spec.whatwg.org/#this)’s [element](#concept-attribute-element) using namespace. 

Otherwise 

  1. 

If [this](https://webidl.spec.whatwg.org/#this)’s [parent element](#parent-element) is null, then return null. 

  2. 

Return the result of [locating a namespace prefix](#locate-a-namespace-prefix) for [this](https://webidl.spec.whatwg.org/#this)’s [parent element](#parent-element) using namespace. 

The `lookupNamespaceURI(prefix)` method steps are: 

1. 

If prefix is the empty string, then set it to null. 

2. 

Return the result of running [locate a namespace](#locate-a-namespace) for [this](https://webidl.spec.whatwg.org/#this) using prefix. 

The `isDefaultNamespace(namespace)` method steps are: 

1. 

If namespace is the empty string, then set it to null. 

2. 

Let defaultNamespace be the result of running [locate a namespace](#locate-a-namespace) for [this](https://webidl.spec.whatwg.org/#this) using null. 

3. 

Return true if defaultNamespace is the same as namespace; otherwise false. 

The `insertBefore(node, child)` method steps are to return the result of [pre-inserting](#concept-node-pre-insert)node into [this](https://webidl.spec.whatwg.org/#this) before child. 

The `appendChild(node)` method steps are to return the result of [appending](#concept-node-append)node to [this](https://webidl.spec.whatwg.org/#this). 

The `replaceChild(node, child)` method steps are to return the result of [replacing](#concept-node-replace)child with node within [this](https://webidl.spec.whatwg.org/#this). 

The `removeChild(child)` method steps are to return the result of [pre-removing](#concept-node-pre-remove)child from [this](https://webidl.spec.whatwg.org/#this). 

The list of elements with qualified name qualifiedName for a [node](#concept-node)root is the [HTMLCollection](#htmlcollection) returned by the following algorithm: 

1. 

If qualifiedName is U+002A (*), then return an [HTMLCollection](#htmlcollection) rooted at root, whose filter matches only [descendant](#concept-tree-descendant)[elements](#concept-element). 

2. 

Otherwise, if root’s [node document](#concept-node-document) is an [HTML document](#html-document), return an [HTMLCollection](#htmlcollection) rooted at root, whose filter matches the following [descendant](#concept-tree-descendant)[elements](#concept-element): 

  - 

Whose [namespace](#concept-element-namespace) is the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace) and whose [qualified name](#concept-element-qualified-name) is qualifiedName, in [ASCII lowercase](https://infra.spec.whatwg.org/#ascii-lowercase). 

  - 

Whose [namespace](#concept-element-namespace) is not the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace) and whose [qualified name](#concept-element-qualified-name) is qualifiedName. 

3. 

Otherwise, return an [HTMLCollection](#htmlcollection) rooted at root, whose filter matches [descendant](#concept-tree-descendant)[elements](#concept-element) whose [qualified name](#concept-element-qualified-name) is qualifiedName. 

When invoked with the same argument, and as long as root’s [node document](#concept-node-document)’s [type](#concept-document-type) has not changed, the same [HTMLCollection](#htmlcollection) object may be returned as returned by an earlier call. 

The list of elements with namespace namespace and local name localName for a [node](#concept-node)root is the [HTMLCollection](#htmlcollection) returned by the following algorithm: 

1. 

If namespace is the empty string, then set it to null. 

2. 

If both namespace and localName are U+002A (*), then return an [HTMLCollection](#htmlcollection) rooted at root, whose filter matches [descendant](#concept-tree-descendant)[elements](#concept-element). 

3. 

If namespace is U+002A (*), then return an [HTMLCollection](#htmlcollection) rooted at root, whose filter matches [descendant](#concept-tree-descendant)[elements](#concept-element) whose [local name](#concept-element-local-name) is localName. 

4. 

If localName is U+002A (*), then return an [HTMLCollection](#htmlcollection) rooted at root, whose filter matches [descendant](#concept-tree-descendant)[elements](#concept-element) whose [namespace](#concept-element-namespace) is namespace. 

5. 

Return an [HTMLCollection](#htmlcollection) rooted at root, whose filter matches [descendant](#concept-tree-descendant)[elements](#concept-element) whose [namespace](#concept-element-namespace) is namespace and [local name](#concept-element-local-name) is localName. 

When invoked with the same arguments, the same [HTMLCollection](#htmlcollection) object may be returned as returned by an earlier call. 

The list of elements with class names classNames for a [node](#concept-node)root is the [HTMLCollection](#htmlcollection) returned by the following algorithm: 

1.  Let classes be the result of running the [ordered set parser](#concept-ordered-set-parser) on classNames. 
2.  If classes is the empty set, return an empty [HTMLCollection](#htmlcollection). 
3. 

Return an [HTMLCollection](#htmlcollection) rooted at root, whose filter matches [descendant](#concept-tree-descendant)[elements](#concept-element) that have all their [classes](#concept-class) in classes. 

The comparisons for the [classes](#concept-class) must be done in an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) manner if root’s [node document](#concept-node-document)’s [mode](#concept-document-mode) is "`quirks`"; otherwise in an [identical to](https://infra.spec.whatwg.org/#string-is) manner. 

When invoked with the same argument, the same [HTMLCollection](#htmlcollection) object may be returned as returned by an earlier call. 

### 4.5. Interface [Document](#document)#interface-document

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface Document : Node#node {
  constructor#dom-document-document();

  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute DOMImplementation#domimplementation implementation#dom-document-implementation;
  readonly attribute USVStringhttps://webidl.spec.whatwg.org/#idl-USVString URL#dom-document-url;
  readonly attribute USVStringhttps://webidl.spec.whatwg.org/#idl-USVString documentURI#dom-document-documenturi;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString compatMode#dom-document-compatmode;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString characterSet#dom-document-characterset;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString charset#dom-document-charset; // legacy alias of .characterSet
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString inputEncoding#dom-document-inputencoding; // legacy alias of .characterSet
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString contentType#dom-document-contenttype;

  readonly attribute DocumentType#documenttype? doctype#dom-document-doctype;
  readonly attribute Element#element? documentElement#dom-document-documentelement;
  HTMLCollection#htmlcollection getElementsByTagName#dom-document-getelementsbytagname(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName);
  HTMLCollection#htmlcollection getElementsByTagNameNS#dom-document-getelementsbytagnamens(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName);
  HTMLCollection#htmlcollection getElementsByClassName#dom-document-getelementsbyclassname(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString classNames);

  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, NewObjecthttps://webidl.spec.whatwg.org/#NewObject] Element#element createElement#dom-document-createelement(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName, optional (DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString or ElementCreationOptions#dictdef-elementcreationoptions) options = {});
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, NewObjecthttps://webidl.spec.whatwg.org/#NewObject] Element#element createElementNS#dom-document-createelementns(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName, optional (DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString or ElementCreationOptions#dictdef-elementcreationoptions) options = {});
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] DocumentFragment#documentfragment createDocumentFragment#dom-document-createdocumentfragment();
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] Text#text createTextNode#dom-document-createtextnode(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString data);
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] CDATASection#cdatasection createCDATASection#dom-document-createcdatasection(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString data);
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] Comment#comment createComment#dom-document-createcomment(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString data);
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] ProcessingInstruction#processinginstruction createProcessingInstruction#dom-document-createprocessinginstruction(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString target, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString data);

  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, NewObjecthttps://webidl.spec.whatwg.org/#NewObject] Node#node importNode#dom-document-importnode(Node#node node, optional (booleanhttps://webidl.spec.whatwg.org/#idl-boolean or ImportNodeOptions#dictdef-importnodeoptions) options = false);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Node#node adoptNode#dom-document-adoptnode(Node#node node);

  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] Attr#attr createAttribute#dom-document-createattribute(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName);
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] Attr#attr createAttributeNS#dom-document-createattributens(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName);

  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] Event#event createEvent#dom-document-createevent(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString interface); // legacy

  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] Range#range createRange#dom-document-createrange();

  // NodeFilter.SHOW_ALL = 0xFFFFFFFF
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] NodeIterator#nodeiterator createNodeIterator#dom-document-createnodeiterator(Node#node root, optional unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long whatToShow = 0xFFFFFFFF, optional NodeFilter#callbackdef-nodefilter? filter = null);
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] TreeWalker#treewalker createTreeWalker#dom-document-createtreewalker(Node#node root, optional unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long whatToShow = 0xFFFFFFFF, optional NodeFilter#callbackdef-nodefilter? filter = null);
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface XMLDocument : Document#document {};

dictionary ElementCreationOptions {
  CustomElementRegistryhttps://html.spec.whatwg.org/multipage/custom-elements.html#customelementregistry? customElementRegistry;
  DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString is;
};

dictionary ImportNodeOptions {
  CustomElementRegistryhttps://html.spec.whatwg.org/multipage/custom-elements.html#customelementregistry customElementRegistry;
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean selfOnly = false;
};
```

[Document](#document)[nodes](#concept-node) are simply known as documents. 

A [document](#concept-document)’s [node document](#concept-node-document) is itself. 

Each [document](#concept-document) has an associated encoding (an [encoding](https://encoding.spec.whatwg.org/#encoding)), content type (a string), URL (a [URL](https://url.spec.whatwg.org/#concept-url)), origin (an [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)), type ("`xml`" or "`html`"), mode ("`no-quirks`", "`quirks`", or "`limited-quirks`"), allow declarative shadow roots (a boolean), and custom element registry (null or a [CustomElementRegistry](https://html.spec.whatwg.org/multipage/custom-elements.html#customelementregistry) object). [[ENCODING]](#biblio-encoding)[[URL]](#biblio-url)[[HTML]](#biblio-html)

Unless stated otherwise, a [document](#concept-document)’s [encoding](#concept-document-encoding) is the [utf-8](https://encoding.spec.whatwg.org/#utf-8)[encoding](https://encoding.spec.whatwg.org/#encoding), [content type](#concept-document-content-type) is "`application/xml`", [URL](#concept-document-url) is "`about:blank`", [origin](#concept-document-origin) is an [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque), [type](#concept-document-type) is "`xml`", [mode](#concept-document-mode) is "`no-quirks`", [allow declarative shadow roots](#document-allow-declarative-shadow-roots) is false, and [custom element registry](#document-custom-element-registry) is null. 

A [document](#concept-document) is said to be an XML document if its [type](#concept-document-type) is "`xml`"; otherwise an HTML document. Whether a [document](#concept-document) is an [HTML document](#html-document) or an [XML document](#xml-document) affects the behavior of certain APIs. 

A [document](#concept-document) is said to be in no-quirks mode if its [mode](#concept-document-mode) is "`no-quirks`", quirks mode if its [mode](#concept-document-mode) is "`quirks`", and limited-quirks mode if its [mode](#concept-document-mode) is "`limited-quirks`". 

The [mode](#concept-document-mode) is only ever changed from the default for [documents](#concept-document) created by the [HTML parser](https://html.spec.whatwg.org/multipage/parsing.html#html-parser) based on the presence, absence, or value of the DOCTYPE string, and by a new [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context) (initial "`about:blank`"). [[HTML]](#biblio-html)

[No-quirks mode](#concept-document-no-quirks) was originally known as "standards mode" and [limited-quirks mode](#concept-document-limited-quirks) was once known as "almost standards mode". They have been renamed because their details are now defined by standards. (And because Ian Hickson vetoed their original names on the basis that they are nonsensical.) 

A [document](#concept-document)’s [get the parent](#get-the-parent) algorithm, given an event, returns null if event’s [type](#dom-event-type) attribute value is "`load`" or [document](#concept-document) does not have a [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#concept-document-bc); otherwise the [document](#concept-document)’s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global). 

[Document()](#dom-document-document)Returns a new [document](#concept-document). [implementation](#dom-document-implementation)Returns document’s [DOMImplementation](#domimplementation) object. [URL](#dom-document-url)[documentURI](#dom-document-documenturi)Returns document’s [URL](#concept-document-url). [compatMode](#dom-document-compatmode) Returns the string "`BackCompat`" if document’s [mode](#concept-document-mode) is "`quirks`"; otherwise "`CSS1Compat`". [characterSet](#dom-document-characterset)Returns document’s [encoding](#concept-document-encoding). [contentType](#dom-document-contenttype)Returns document’s [content type](#concept-document-content-type). 

The `new Document()` constructor steps are to set [this](https://webidl.spec.whatwg.org/#this)’s [origin](#concept-document-origin) to the [origin](#concept-document-origin) of [current global object](https://html.spec.whatwg.org/multipage/webappapis.html#current-global-object)’s [associated Document](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window). [[HTML]](#biblio-html)

Unlike [createDocument()](#dom-domimplementation-createdocument), this constructor does not return an [XMLDocument](#xmldocument) object, but a [document](#concept-document) ([Document](#document) object). 

The `implementation` getter steps are to return the [DOMImplementation](#domimplementation) object that is associated with [this](https://webidl.spec.whatwg.org/#this). 

The `URL` and `documentURI` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [URL](#concept-document-url), [serialized](https://url.spec.whatwg.org/#concept-url-serializer). 

The `compatMode` getter steps are to return "`BackCompat`" if [this](https://webidl.spec.whatwg.org/#this)’s [mode](#concept-document-mode) is "`quirks`"; otherwise "`CSS1Compat`". 

The `characterSet`, `charset`, and `inputEncoding` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [encoding](#concept-document-encoding)’s [name](https://encoding.spec.whatwg.org/#name). 

The `contentType` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [content type](#concept-document-content-type). 

document . [doctype](#dom-document-doctype)Returns the [doctype](#concept-doctype) or null if there is none. document . [documentElement](#dom-document-documentelement)Returns the [document element](#document-element). [getElementsByTagName](#dom-document-getelementsbytagname)`collection = document . (qualifiedName)`

If qualifiedName is "`*`" returns an [HTMLCollection](#htmlcollection) of all [descendant](#concept-tree-descendant)[elements](#concept-element). 

Otherwise, returns an [HTMLCollection](#htmlcollection) of all [descendant](#concept-tree-descendant)[elements](#concept-element) whose [qualified name](#concept-element-qualified-name) is qualifiedName. (Matches case-insensitively against [elements](#concept-element) in the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace) within an [HTML document](#html-document).) 

[getElementsByTagNameNS](#dom-document-getelementsbytagnamens)`collection = document . (namespace, localName)`

If namespace and localName are "`*`", returns an [HTMLCollection](#htmlcollection) of all [descendant](#concept-tree-descendant)[elements](#concept-element). 

If only namespace is "`*`", returns an [HTMLCollection](#htmlcollection) of all [descendant](#concept-tree-descendant)[elements](#concept-element) whose [local name](#concept-element-local-name) is localName. 

If only localName is "`*`", returns an [HTMLCollection](#htmlcollection) of all [descendant](#concept-tree-descendant)[elements](#concept-element) whose [namespace](#concept-element-namespace) is namespace. 

Otherwise, returns an [HTMLCollection](#htmlcollection) of all [descendant](#concept-tree-descendant)[elements](#concept-element) whose [namespace](#concept-element-namespace) is namespace and [local name](#concept-element-local-name) is localName. 

[getElementsByClassName](#dom-document-getelementsbyclassname)`collection = document . (classNames)`[getElementsByClassName](#dom-element-getelementsbyclassname)`collection = element . (classNames)`

Returns an [HTMLCollection](#htmlcollection) of the [elements](#concept-element) in the object on which the method was invoked (a [document](#concept-document) or an [element](#concept-element)) that have all the classes given by classNames. The classNames argument is interpreted as a space-separated list of classes. 

The `doctype` getter steps are to return the [child](#concept-tree-child) of [this](https://webidl.spec.whatwg.org/#this) that is a [doctype](#concept-doctype); otherwise null. 

The `documentElement` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [document element](#document-element). 

The `getElementsByTagName(qualifiedName)` method steps are to return the [list of elements with qualified name qualifiedName](#concept-getelementsbytagname) for [this](https://webidl.spec.whatwg.org/#this). 

Thus, in an [HTML document](#html-document), `document.getElementsByTagName("FOO")` will match `<FOO>` elements that are not in the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace), and `<foo>` elements that are in the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace), but not `<FOO>` elements that are in the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace). 

The `getElementsByTagNameNS(namespace, localName)` method steps are to return the [list of elements with namespace namespace and local
name localName](#concept-getelementsbytagnamens) for [this](https://webidl.spec.whatwg.org/#this). 

The `getElementsByClassName(classNames)` method steps are to return the [list of elements with class names classNames](#concept-getelementsbyclassname) for [this](https://webidl.spec.whatwg.org/#this). 

#example-5ffcda00 Given the following XHTML fragment: 

```
<div id="example">
  <p id="p1" class="aaa bbb"/>
  <p id="p2" class="aaa ccc"/>
  <p id="p3" class="bbb ccc"/>
</div>
```

A call to `document.getElementById("example").getElementsByClassName("aaa")` would return an [HTMLCollection](#htmlcollection) with the two paragraphs `p1` and `p2` in it.

A call to `getElementsByClassName("ccc bbb")` would only return one node, however, namely `p3`. A call to `document.getElementById("example").getElementsByClassName("bbb  ccc ")` would return the same thing.

A call to `getElementsByClassName("aaa,bbb")` would return no nodes; none of the elements above are in the `aaa,bbb` class.

[createElement(localName [, options])](#dom-document-createelement)`element = document .`

Returns an [element](#concept-element) with localName as [local name](#concept-element-local-name) (if document is an [HTML document](#html-document), localName gets lowercased). The [element](#concept-element)’s [namespace](#concept-element-namespace) is the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace) when document is an [HTML document](#html-document) or document’s [content type](#concept-document-content-type) is "`application/xhtml+xml`"; otherwise null. 

When supplied, options’s [customElementRegistry](#dom-elementcreationoptions-customelementregistry) can be used to set the [CustomElementRegistry](https://html.spec.whatwg.org/multipage/custom-elements.html#customelementregistry). 

When supplied, options’s [is](#dom-elementcreationoptions-is) can be used to create a [customized built-in element](https://html.spec.whatwg.org/multipage/custom-elements.html#customized-built-in-element). 

If localName is not a [valid element local name](#valid-element-local-name) an "[InvalidCharacterError](https://webidl.spec.whatwg.org/#invalidcharactererror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException) will be thrown. 

When both options’s [customElementRegistry](#dom-elementcreationoptions-customelementregistry) and options’s [is](#dom-elementcreationoptions-is) are supplied, a "[NotSupportedError](https://webidl.spec.whatwg.org/#notsupportederror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException) will be thrown. 

[createElementNS(namespace, qualifiedName [, options])](#dom-document-createelementns)`element = document .`

Returns an [element](#concept-element) with [namespace](#concept-element-namespace)namespace. Its [namespace prefix](#concept-element-namespace-prefix) will be everything before U+003A (:) in qualifiedName or null. Its [local name](#concept-element-local-name) will be everything after U+003A (:) in qualifiedName or qualifiedName. 

When supplied, options’s [customElementRegistry](#dom-elementcreationoptions-customelementregistry) can be used to set the [CustomElementRegistry](https://html.spec.whatwg.org/multipage/custom-elements.html#customelementregistry). 

When supplied, options’s [is](#dom-elementcreationoptions-is) can be used to create a [customized built-in element](https://html.spec.whatwg.org/multipage/custom-elements.html#customized-built-in-element). 

If qualifiedName is not a (possibly-prefixed) [valid element local name](#valid-element-local-name) an "[InvalidCharacterError](https://webidl.spec.whatwg.org/#invalidcharactererror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException) will be thrown. 

If one of the following conditions is true a "[NamespaceError](https://webidl.spec.whatwg.org/#namespaceerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException) will be thrown: 

- [Namespace prefix](#concept-element-namespace-prefix) is non-null and namespace is the empty string. 
- [Namespace prefix](#concept-element-namespace-prefix) is "`xml`" and namespace is not the [XML namespace](https://infra.spec.whatwg.org/#xml-namespace). 
- qualifiedName or [namespace prefix](#concept-element-namespace-prefix) is "`xmlns`" and namespace is not the [XMLNS namespace](https://infra.spec.whatwg.org/#xmlns-namespace). 
- namespace is the [XMLNS namespace](https://infra.spec.whatwg.org/#xmlns-namespace) and neither qualifiedName nor [namespace prefix](#concept-element-namespace-prefix) is "`xmlns`". 

When both options’s [customElementRegistry](#dom-elementcreationoptions-customelementregistry) and options’s [is](#dom-elementcreationoptions-is) are supplied, a "[NotSupportedError](https://webidl.spec.whatwg.org/#notsupportederror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException) will be thrown. 

[createDocumentFragment()](#dom-document-createdocumentfragment)Returns a [DocumentFragment](#documentfragment)[node](#concept-node). [createTextNode(data)](#dom-document-createtextnode)Returns a [Text](#text)[node](#concept-node) whose [data](#concept-cd-data) is data. [createCDATASection(data)](#dom-document-createcdatasection)Returns a [CDATASection](#cdatasection)[node](#concept-node) whose [data](#concept-cd-data) is data. [createComment(data)](#dom-document-createcomment)Returns a [Comment](#comment)[node](#concept-node) whose [data](#concept-cd-data) is data. [createProcessingInstruction(target, data)](#dom-document-createprocessinginstruction) Returns a [ProcessingInstruction](#processinginstruction)[node](#concept-node) whose [target](#concept-pi-target) is target and [data](#concept-cd-data) is data. If target does not match the [Name](https://www.w3.org/TR/xml/#NT-Name) production an "[InvalidCharacterError](https://webidl.spec.whatwg.org/#invalidcharactererror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException) will be thrown. If data contains "`?>`" an "[InvalidCharacterError](https://webidl.spec.whatwg.org/#invalidcharactererror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException) will be thrown. 

The element interface for any name and namespace is [Element](#element), unless stated otherwise. 

The HTML Standard will, e.g., define that for `html` and the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace), the [HTMLHtmlElement](https://html.spec.whatwg.org/multipage/semantics.html#htmlhtmlelement) interface is used. [[HTML]](#biblio-html)

The `createElement(localName, options)` method steps are: 

1. 

If localName is not a [valid element local name](#valid-element-local-name), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidCharacterError](https://webidl.spec.whatwg.org/#invalidcharactererror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

2. 

If [this](https://webidl.spec.whatwg.org/#this) is an [HTML document](#html-document), then set localName to localName in [ASCII lowercase](https://infra.spec.whatwg.org/#ascii-lowercase). 

3. 

Let registry and is be the result of [flattening element creation options](#flatten-element-creation-options) given options and [this](https://webidl.spec.whatwg.org/#this). 

4. 

Let namespace be the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace), if [this](https://webidl.spec.whatwg.org/#this) is an [HTML document](#html-document) or [this](https://webidl.spec.whatwg.org/#this)’s [content type](#concept-document-content-type) is "`application/xhtml+xml`"; otherwise null. 

5. 

Return the result of [creating an element](#concept-create-element) given [this](https://webidl.spec.whatwg.org/#this), localName, namespace, null, is, true, and registry. 

The internal `createElementNS` steps, given document, namespace, qualifiedName, and options, are as follows: 

1. 

Let (namespace, prefix, localName) be the result of [validating and extracting](#validate-and-extract)namespace and qualifiedName given "`element`". 

2. 

Let registry and is be the result of [flattening element creation options](#flatten-element-creation-options) given options and [this](https://webidl.spec.whatwg.org/#this). 

3. 

Return the result of [creating an element](#concept-create-element) given document, localName, namespace, prefix, is, true, and registry. 

The `createElementNS(namespace, qualifiedName, options)` method steps are to return the result of running the [internal createElementNS steps](#internal-createelementns-steps), given [this](https://webidl.spec.whatwg.org/#this), namespace, qualifiedName, and options. 

To flatten element creation options, given a string or [ElementCreationOptions](#dictdef-elementcreationoptions) dictionary options and a [document](#concept-document)document: 

1. 

Let registry be the result of [looking up a custom element registry](https://html.spec.whatwg.org/multipage/custom-elements.html#look-up-a-custom-element-registry) given document. 

2. 

Let is be null. 

3. 

If options is a dictionary: 

  1. 

If options["[is](#dom-elementcreationoptions-is)"] [exists](https://infra.spec.whatwg.org/#map-exists), then set is to it. 

  2. 

If options["[customElementRegistry](#dom-elementcreationoptions-customelementregistry)"] [exists](https://infra.spec.whatwg.org/#map-exists): 

    1. 

If is is non-null, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotSupportedError](https://webidl.spec.whatwg.org/#notsupportederror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

    2. 

Set registry to options["[customElementRegistry](#dom-elementcreationoptions-customelementregistry)"]. 

  3. 

If registry is non-null, registry’s [is scoped](https://html.spec.whatwg.org/multipage/custom-elements.html#is-scoped) is false, and registry is not document’s [custom element registry](#document-custom-element-registry), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotSupportedError](https://webidl.spec.whatwg.org/#notsupportederror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

4. 

Return registry and is. 

[createElement()](#dom-document-createelement) and [createElementNS()](#dom-document-createelementns)’s options parameter is allowed to be a string for web compatibility. 

The `createDocumentFragment()` method steps are to return a new [DocumentFragment](#documentfragment)[node](#concept-node) whose [node document](#concept-node-document) is [this](https://webidl.spec.whatwg.org/#this). 

The `createTextNode(data)` method steps are to return a new [Text](#text)[node](#concept-node) whose [data](#concept-cd-data) is data and [node document](#concept-node-document) is [this](https://webidl.spec.whatwg.org/#this). 

The `createCDATASection(data)` method steps are: 

1. 

If [this](https://webidl.spec.whatwg.org/#this) is an [HTML document](#html-document), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotSupportedError](https://webidl.spec.whatwg.org/#notsupportederror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

2. 

If data contains the string "`]]>`", then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidCharacterError](https://webidl.spec.whatwg.org/#invalidcharactererror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

Return a new [CDATASection](#cdatasection)[node](#concept-node) with its [data](#concept-cd-data) set to data and [node document](#concept-node-document) set to [this](https://webidl.spec.whatwg.org/#this). 

The `createComment(data)` method steps are to return a new [Comment](#comment)[node](#concept-node) whose [data](#concept-cd-data) is data and [node document](#concept-node-document) is [this](https://webidl.spec.whatwg.org/#this). 

The `createProcessingInstruction(target, data)` method steps are: 

1. If target does not match the [Name](https://www.w3.org/TR/xml/#NT-Name) production, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidCharacterError](https://webidl.spec.whatwg.org/#invalidcharactererror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 
2. If data contains the string "`?>`", then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidCharacterError](https://webidl.spec.whatwg.org/#invalidcharactererror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 
3. Return a new [ProcessingInstruction](#processinginstruction)[node](#concept-node), with [target](#concept-pi-target) set to target, [data](#concept-cd-data) set to data, and [node document](#concept-node-document) set to [this](https://webidl.spec.whatwg.org/#this). 

[importNode](#dom-document-importnode)`clone = document . (node [, options = false])`

Returns a copy of node. If options is true or options is a dictionary whose [selfOnly](#dom-importnodeoptions-selfonly) is false, the copy also includes the node’s [descendants](#concept-tree-descendant). 

options’s [customElementRegistry](#dom-importnodeoptions-customelementregistry) can be used to set the [CustomElementRegistry](https://html.spec.whatwg.org/multipage/custom-elements.html#customelementregistry) of elements that have none. 

If node is a [document](#concept-document) or a [shadow root](#concept-shadow-root), throws a "[NotSupportedError](https://webidl.spec.whatwg.org/#notsupportederror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

[adoptNode](#dom-document-adoptnode)`node = document . (node)`

Moves node from another [document](#concept-document) and returns it. 

If node is a [document](#concept-document), throws a "[NotSupportedError](https://webidl.spec.whatwg.org/#notsupportederror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException) or, if node is a [shadow root](#concept-shadow-root), throws a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

The `importNode(node, options)` method steps are: 

1. 

If node is a [document](#concept-document) or [shadow root](#concept-shadow-root), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotSupportedError](https://webidl.spec.whatwg.org/#notsupportederror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

2. 

Let subtree be false. 

3. 

Let registry be null. 

4. 

If options is a boolean, then set subtree to options. 

5. 

Otherwise: 

  1. 

Set subtree to the negation of options["[selfOnly](#dom-importnodeoptions-selfonly)"]. 

  2. 

If options["[customElementRegistry](#dom-importnodeoptions-customelementregistry)"] [exists](https://infra.spec.whatwg.org/#map-exists), then set registry to it. 

  3. 

If registry’s [is scoped](https://html.spec.whatwg.org/multipage/custom-elements.html#is-scoped) is false and registry is not [this](https://webidl.spec.whatwg.org/#this)’s [custom element registry](#document-custom-element-registry), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotSupportedError](https://webidl.spec.whatwg.org/#notsupportederror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

6. 

If registry is null, then set registry to the result of [looking up a custom element registry](https://html.spec.whatwg.org/multipage/custom-elements.html#look-up-a-custom-element-registry) given [this](https://webidl.spec.whatwg.org/#this). 

7. 

Return the result of [cloning a node](#concept-node-clone) given node with [document](#clone-a-node-document) set to [this](https://webidl.spec.whatwg.org/#this), [subtree](#clone-a-node-subtree) set to subtree, and [fallbackRegistry](#clone-a-node-fallbackregistry) set to registry. 

[Specifications](#other-applicable-specifications) may define adopting steps for all or some [nodes](#concept-node). The algorithm is passed node and oldDocument, as indicated in the [adopt](#concept-node-adopt) algorithm. 

To adopt a [node](#concept-node)node into a [document](#concept-document)document: 

1. 

Let oldDocument be node’s [node document](#concept-node-document). 

2. 

If node’s [parent](#concept-tree-parent) is non-null, then [remove](#concept-node-remove)node. 

3. 

If document is not oldDocument: 

  1. 

For each inclusiveDescendant of node’s [shadow-including inclusive descendants](#concept-shadow-including-inclusive-descendant), in [shadow-including tree order](#concept-shadow-including-tree-order): 

    1. 

Set inclusiveDescendant’s [node document](#concept-node-document) to document. 

    2. 

If inclusiveDescendant is a [shadow root](#concept-shadow-root) and if any of the following are true: 

      - 

inclusiveDescendant’s [custom element registry](#shadowroot-custom-element-registry) is null and inclusiveDescendant’s [keep custom element registry null](#shadowroot-keep-custom-element-registry-null) is false; or 

      - 

inclusiveDescendant’s [custom element registry](#shadowroot-custom-element-registry)[is a global custom element registry](#is-a-global-custom-element-registry), 

then set inclusiveDescendant’s [custom element registry](#shadowroot-custom-element-registry) to document’s [effective global custom element registry](#effective-global-custom-element-registry). 

    3. 

Otherwise, if inclusiveDescendant is an [element](#concept-element): 

      1. 

Set the [node document](#concept-node-document) of each [attribute](#concept-attribute) in inclusiveDescendant’s [attribute list](#concept-element-attribute) to document. 

      2. 

If inclusiveDescendant’s [custom element registry](#element-custom-element-registry) is null or inclusiveDescendant’s [custom element registry](#element-custom-element-registry)’s [is scoped](https://html.spec.whatwg.org/multipage/custom-elements.html#is-scoped) is false, then set inclusiveDescendant’s [custom element registry](#element-custom-element-registry) to document’s [effective global custom element registry](#effective-global-custom-element-registry). 

  2. 

For each inclusiveDescendant of node’s [shadow-including inclusive descendants](#concept-shadow-including-inclusive-descendant) that is [custom](#concept-element-custom), in [shadow-including tree order](#concept-shadow-including-tree-order): [enqueue a custom element callback reaction](https://html.spec.whatwg.org/multipage/custom-elements.html#enqueue-a-custom-element-callback-reaction) with inclusiveDescendant, callback name "`adoptedCallback`", and « oldDocument, document ». 

  3. 

For each inclusiveDescendant of node’s [shadow-including inclusive descendants](#concept-shadow-including-inclusive-descendant), in [shadow-including tree order](#concept-shadow-including-tree-order): run the [adopting steps](#concept-node-adopt-ext) with inclusiveDescendant and oldDocument. 

The `adoptNode(node)` method steps are: 

1. 

If node is a [document](#concept-document), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotSupportedError](https://webidl.spec.whatwg.org/#notsupportederror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

2. 

If node is a [shadow root](#concept-shadow-root), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

If node is a [DocumentFragment](#documentfragment)[node](#concept-node) whose [host](#concept-documentfragment-host) is non-null, then return. 

4. 

[Adopt](#concept-node-adopt)node into [this](https://webidl.spec.whatwg.org/#this). 

5. 

Return node. 

Null or a [CustomElementRegistry](https://html.spec.whatwg.org/multipage/custom-elements.html#customelementregistry) object registryis a global custom element registry if registry is non-null and registry’s [is scoped](https://html.spec.whatwg.org/multipage/custom-elements.html#is-scoped) is false.

A [document](#concept-document)document’s effective global custom element registry is: 

1. 

If document’s [custom element registry](#document-custom-element-registry)[is a global custom element registry](#is-a-global-custom-element-registry), then return document’s [custom element registry](#document-custom-element-registry). 

2. 

Return null. 

The `createAttribute(localName)` method steps are: 

1. 

If localName is not a [valid attribute local name](#valid-attribute-local-name), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidCharacterError](https://webidl.spec.whatwg.org/#invalidcharactererror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

2. If [this](https://webidl.spec.whatwg.org/#this) is an [HTML document](#html-document), then set localName to localName in [ASCII lowercase](https://infra.spec.whatwg.org/#ascii-lowercase). 
3. Return a new [attribute](#concept-attribute) whose [local name](#concept-attribute-local-name) is localName and [node document](#concept-node-document) is [this](https://webidl.spec.whatwg.org/#this). 

The `createAttributeNS(namespace, qualifiedName)` method steps are: 

1. 

Let (namespace, prefix, localName) be the result of [validating and extracting](#validate-and-extract)namespace and qualifiedName given "`attribute`". 

2. 

Return a new [attribute](#concept-attribute) whose [namespace](#concept-attribute-namespace) is namespace, [namespace prefix](#concept-attribute-namespace-prefix) is prefix, [local name](#concept-attribute-local-name) is localName, and [node document](#concept-node-document) is [this](https://webidl.spec.whatwg.org/#this). 

The `createEvent(interface)` method steps are: 

1. 

Let constructor be null. 

2. 

If interface is an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for any of the strings in the first column in the following table, then set constructor to the interface in the second column on the same row as the matching string: 

String Interface Notes "`beforeunloadevent`" [BeforeUnloadEvent](https://html.spec.whatwg.org/multipage/nav-history-apis.html#beforeunloadevent)[[HTML]](#biblio-html)"`compositionevent`" [CompositionEvent](https://w3c.github.io/uievents/#compositionevent)[[UIEVENTS]](#biblio-uievents)"`customevent`" [CustomEvent](#customevent)"`devicemotionevent`" [DeviceMotionEvent](https://w3c.github.io/deviceorientation/spec-source-orientation.html#devicemotion)[[DEVICE-ORIENTATION]](#biblio-device-orientation)"`deviceorientationevent`" [DeviceOrientationEvent](https://w3c.github.io/deviceorientation/spec-source-orientation.html#devicemotion)"`dragevent`" [DragEvent](https://html.spec.whatwg.org/multipage/dnd.html#dragevent)[[HTML]](#biblio-html)"`event`" [Event](#event)"`events`" "`focusevent`" [FocusEvent](https://w3c.github.io/uievents/#focusevent)[[UIEVENTS]](#biblio-uievents)"`hashchangeevent`" [HashChangeEvent](https://html.spec.whatwg.org/multipage/nav-history-apis.html#hashchangeevent)[[HTML]](#biblio-html)"`htmlevents`" [Event](#event)"`keyboardevent`" [KeyboardEvent](https://w3c.github.io/uievents/#keyboardevent)[[UIEVENTS]](#biblio-uievents)"`messageevent`" [MessageEvent](https://html.spec.whatwg.org/multipage/comms.html#messageevent)[[HTML]](#biblio-html)"`mouseevent`" [MouseEvent](https://w3c.github.io/uievents/#mouseevent)[[UIEVENTS]](#biblio-uievents)"`mouseevents`" "`storageevent`" [StorageEvent](https://html.spec.whatwg.org/multipage/webstorage.html#storageevent)[[HTML]](#biblio-html)"`svgevents`" [Event](#event)"`textevent`" [TextEvent](https://w3c.github.io/uievents/#textevent)[[UIEVENTS]](#biblio-uievents)"`touchevent`" [TouchEvent](https://w3c.github.io/touch-events/#idl-def-touchevent)[[TOUCH-EVENTS]](#biblio-touch-events)"`uievent`" [UIEvent](https://w3c.github.io/uievents/#uievent)[[UIEVENTS]](#biblio-uievents)"`uievents`" 
3. 

If constructor is null, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotSupportedError](https://webidl.spec.whatwg.org/#notsupportederror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

4. 

If the interface indicated by constructor is not exposed on the [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) of [this](https://webidl.spec.whatwg.org/#this), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotSupportedError](https://webidl.spec.whatwg.org/#notsupportederror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

Typically user agents disable support for touch events in some configurations, in which case this clause would be triggered for the interface [TouchEvent](https://w3c.github.io/touch-events/#idl-def-touchevent). 

5. 

Let event be the result of [creating an event](#concept-event-create) given constructor. 

6. 

Initialize event’s [type](#dom-event-type) attribute to the empty string. 

7. 

Initialize event’s [timeStamp](#dom-event-timestamp) attribute to the result of calling [current high resolution time](https://w3c.github.io/hr-time/#dfn-current-high-resolution-time) with [this](https://webidl.spec.whatwg.org/#this)’s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global). 

8. 

Initialize event’s [isTrusted](#dom-event-istrusted) attribute to false. 

9. 

Unset event’s [initialized flag](#initialized-flag). 

10. 

Return event. 

[Event](#concept-event) constructors ought to be used instead. 

The `createRange()` method steps are to return a new [live range](#concept-live-range) with ([this](https://webidl.spec.whatwg.org/#this), 0) as its [start](#concept-range-start) an [end](#concept-range-end). 

The [Range()](#dom-range-range) constructor can be used instead. 

The `createNodeIterator(root, whatToShow, filter)` method steps are: 

1. 

Let iterator be a new [NodeIterator](#nodeiterator) object. 

2. 

Set iterator’s [root](#concept-traversal-root) and iterator’s [reference](#nodeiterator-reference) to root. 

3. 

Set iterator’s [pointer before reference](#nodeiterator-pointer-before-reference) to true. 

4. 

Set iterator’s [whatToShow](#concept-traversal-whattoshow) to whatToShow. 

5. 

Set iterator’s [filter](#concept-traversal-filter) to filter. 

6. 

Return iterator. 

The `createTreeWalker(root, whatToShow, filter)` method steps are: 

1. 

Let walker be a new [TreeWalker](#treewalker) object. 

2. 

Set walker’s [root](#concept-traversal-root) and walker’s [current](#treewalker-current) to root. 

3. 

Set walker’s [whatToShow](#concept-traversal-whattoshow) to whatToShow. 

4. 

Set walker’s [filter](#concept-traversal-filter) to filter. 

5. Return walker. 

#### 4.5.1. Interface [DOMImplementation](#domimplementation)#interface-domimplementation

User agents must create a [DOMImplementation](#domimplementation) object whenever a [document](#concept-document) is created and associate it with that [document](#concept-document). 

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface DOMImplementation {
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] DocumentType#documenttype createDocumentType#dom-domimplementation-createdocumenttype(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString name, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString publicId, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString systemId);
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] XMLDocument#xmldocument createDocument#dom-domimplementation-createdocument(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace, [LegacyNullToEmptyStringhttps://webidl.spec.whatwg.org/#LegacyNullToEmptyString] DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName, optional DocumentType#documenttype? doctype = null);
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] Document#document createHTMLDocument#dom-domimplementation-createhtmldocument(optional DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString title);

  booleanhttps://webidl.spec.whatwg.org/#idl-boolean hasFeature#dom-domimplementation-hasfeature(); // useless; always returns true
};
```

[implementation](#dom-document-implementation)[createDocumentType(name, publicId, systemId)](#dom-domimplementation-createdocumenttype) Returns a [doctype](#concept-doctype), with the given name, publicId, and systemId. 

If name is not a [valid doctype name](#valid-doctype-name), an "[InvalidCharacterError](https://webidl.spec.whatwg.org/#invalidcharactererror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException) is thrown.

[implementation](#dom-document-implementation)[createDocument(namespace, qualifiedName [, doctype = null])](#dom-domimplementation-createdocument)`.` Returns an [XMLDocument](#xmldocument), with a [document element](#document-element) whose [local name](#concept-element-local-name) is qualifiedName and whose [namespace](#concept-element-namespace) is namespace (unless qualifiedName is the empty string), and with doctype, if it is given, as its [doctype](#concept-doctype). 

This method throws the same exceptions as the [createElementNS()](#dom-document-createelementns) method, when invoked with namespace and qualifiedName.

[implementation](#dom-document-implementation)[createHTMLDocument([title])](#dom-domimplementation-createhtmldocument)`.` Returns a [document](#concept-document), with a basic [tree](#concept-tree) already constructed including a [title](https://html.spec.whatwg.org/multipage/semantics.html#the-title-element) element, unless the title argument is omitted. 

The `createDocumentType(name, publicId, systemId)` method steps are: 

1. 

If name is not a [valid doctype name](#valid-doctype-name), then throw an "[InvalidCharacterError](https://webidl.spec.whatwg.org/#invalidcharactererror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

2. 

Return a new [doctype](#concept-doctype), with name as its [name](#concept-doctype-name), publicId as its [public ID](#concept-doctype-publicid), and systemId as its [system ID](#concept-doctype-systemid), and with its [node document](#concept-node-document) set to the associated [document](#concept-document) of [this](https://webidl.spec.whatwg.org/#this). 

The `createDocument(namespace, qualifiedName, doctype)` method steps are: 

1. 

Let document be a new [XMLDocument](#xmldocument). 

2. 

Let element be null. 

3. 

If qualifiedName is not the empty string, then set element to the result of running the [internal createElementNS steps](#internal-createelementns-steps), given document, namespace, qualifiedName, and an empty dictionary. 

4. 

If doctype is non-null, [append](#concept-node-append)doctype to document. 

5. 

If element is non-null, [append](#concept-node-append)element to document. 

6. 

document’s [origin](#concept-document-origin) is [this](https://webidl.spec.whatwg.org/#this)’s associated [document](#concept-document)’s [origin](#concept-document-origin). 

7. 

document’s [content type](#concept-document-content-type) is determined by namespace: 

[HTML namespace](https://infra.spec.whatwg.org/#html-namespace)`application/xhtml+xml`[SVG namespace](https://infra.spec.whatwg.org/#svg-namespace)`image/svg+xml`Any other namespace `application/xml`
8. 

Return document. 

The `createHTMLDocument(title)` method steps are: 

1. 

Let doc be a new [document](#concept-document) that is an [HTML document](#html-document). 

2. 

Set doc’s [content type](#concept-document-content-type) to "`text/html`". 

3. 

[Append](#concept-node-append) a new [doctype](#concept-doctype), with "`html`" as its [name](#concept-doctype-name) and with its [node document](#concept-node-document) set to doc, to doc. 

4. 

[Append](#concept-node-append) the result of [creating an element](#concept-create-element) given doc, "`html`", and the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace), to doc. 

5. 

[Append](#concept-node-append) the result of [creating an element](#concept-create-element) given doc, "`head`", and the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace), to the [html](https://html.spec.whatwg.org/multipage/semantics.html#the-html-element) element created earlier. 

6. 

If title is given: 

  1. 

[Append](#concept-node-append) the result of [creating an element](#concept-create-element) given doc, "`title`", and the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace), to the [head](https://html.spec.whatwg.org/multipage/semantics.html#the-head-element) element created earlier. 

  2. 

[Append](#concept-node-append) a new [Text](#text)[node](#concept-node), with its [data](#concept-cd-data) set to title (which could be the empty string) and its [node document](#concept-node-document) set to doc, to the [title](https://html.spec.whatwg.org/multipage/semantics.html#the-title-element) element created earlier. 

7. 

[Append](#concept-node-append) the result of [creating an element](#concept-create-element) given doc, "`body`", and the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace), to the [html](https://html.spec.whatwg.org/multipage/semantics.html#the-html-element) element created earlier.

8. 

doc’s [origin](#concept-document-origin) is [this](https://webidl.spec.whatwg.org/#this)’s associated [document](#concept-document)’s [origin](#concept-document-origin). 

9. 

Return doc. 

The `hasFeature()` method steps are to return true. 

[hasFeature()](#dom-domimplementation-hasfeature) originally would report whether the user agent claimed to support a given DOM feature, but experience proved it was not nearly as reliable or granular as simply checking whether the desired objects, attributes, or methods existed. As such, it is no longer to be used, but continues to exist (and simply returns true) so that old pages don’t stop working. 

### 4.6. Interface [DocumentType](#documenttype)#interface-documenttype

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface DocumentType : Node#node {
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString name#dom-documenttype-name;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString publicId#dom-documenttype-publicid;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString systemId#dom-documenttype-systemid;
};
```

[DocumentType](#documenttype)[nodes](#concept-node) are simply known as doctypes. 

[Doctypes](#concept-doctype) have an associated name, public ID, and system ID. 

When a [doctype](#concept-doctype) is created, its [name](#concept-doctype-name) is always given. Unless explicitly given when a [doctype](#concept-doctype) is created, its [public ID](#concept-doctype-publicid) and [system ID](#concept-doctype-systemid) are the empty string. 

The `name` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [name](#concept-doctype-name). 

The `publicId` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [public ID](#concept-doctype-publicid). 

The `systemId` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [system ID](#concept-doctype-systemid). 

### 4.7. Interface [DocumentFragment](#documentfragment)#interface-documentfragment

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface DocumentFragment : Node#node {
  constructor#dom-documentfragment-documentfragment();
};
```

A [DocumentFragment](#documentfragment)[node](#concept-node) has an associated host (null or an [element](#concept-element) in a different [node tree](#concept-node-tree)). It is null unless otherwise stated. 

An object A is a host-including inclusive ancestor of an object B, if either A is an [inclusive ancestor](#concept-tree-inclusive-ancestor) of B, or if B’s [root](#concept-tree-root) has a non-null [host](#concept-documentfragment-host) and A is a [host-including inclusive ancestor](#concept-tree-host-including-inclusive-ancestor) of B’s [root](#concept-tree-root)’s [host](#concept-documentfragment-host). 

The [DocumentFragment](#documentfragment)[node](#concept-node)’s [host](#concept-documentfragment-host) concept is useful for HTML’s [template](https://html.spec.whatwg.org/multipage/scripting.html#the-template-element) element and for [shadow roots](#concept-shadow-root), and impacts the [pre-insert](#concept-node-pre-insert) and [replace](#concept-node-replace) algorithms. 

[DocumentFragment()](#dom-documentfragment-documentfragment)Returns a new [DocumentFragment](#documentfragment)[node](#concept-node). 

The `new DocumentFragment()` constructor steps are to set [this](https://webidl.spec.whatwg.org/#this)’s [node document](#concept-node-document) to [current global object](https://html.spec.whatwg.org/multipage/webappapis.html#current-global-object)’s [associated Document](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window). 

### 4.8. Interface [ShadowRoot](#shadowroot)#interface-shadowroot

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface ShadowRoot : DocumentFragment#documentfragment {
  readonly attribute ShadowRootMode#enumdef-shadowrootmode mode#dom-shadowroot-mode;
  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean delegatesFocus#dom-shadowroot-delegatesfocus;
  readonly attribute SlotAssignmentMode#enumdef-slotassignmentmode slotAssignment#dom-shadowroot-slotassignment;
  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean clonable#dom-shadowroot-clonable;
  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean serializable#dom-shadowroot-serializable;
  readonly attribute Element#element host#dom-shadowroot-host;

  attribute EventHandlerhttps://html.spec.whatwg.org/multipage/webappapis.html#eventhandler onslotchange#dom-shadowroot-onslotchange;
};

enum ShadowRootMode { "open", "closed" };
enum SlotAssignmentMode { "manual", "named" };
```

[ShadowRoot](#shadowroot)[nodes](#concept-node) are simply known as shadow roots. 

[Shadow roots](#concept-shadow-root)’s associated [host](#concept-documentfragment-host) is never null.

[Shadow roots](#concept-shadow-root) have an associated mode ("`open`" or "`closed`").

[Shadow roots](#concept-shadow-root) have an associated delegates focus (a boolean). It is initially set to false.

[Shadow roots](#concept-shadow-root) have an associated available to element internals (a boolean). It is initially set to false.

[Shadow roots](#concept-shadow-root) have an associated declarative (a boolean). It is initially set to false.

[Shadow roots](#concept-shadow-root) have an associated slot assignment ("`manual`" or "`named`"). 

[Shadow roots](#concept-shadow-root) have an associated clonable (a boolean). It is initially set to false.

[Shadow roots](#concept-shadow-root) have an associated serializable (a boolean). It is initially set to false.

[Shadow roots](#concept-shadow-root) have an associated custom element registry (null or a [CustomElementRegistry](https://html.spec.whatwg.org/multipage/custom-elements.html#customelementregistry) object). It is initially null.

[Shadow roots](#concept-shadow-root) have an associated keep custom element registry null (a boolean). It is initially false. 

This can only ever be true in combination with declarative shadow roots. And it only matters for as long as the [shadow root](#concept-shadow-root)’s [custom element registry](#shadowroot-custom-element-registry) is null. 

A [shadow root](#concept-shadow-root)’s [get the parent](#get-the-parent) algorithm, given an event, returns null if event’s [composed flag](#composed-flag) is unset and [shadow root](#concept-shadow-root) is the [root](#concept-tree-root) of event’s [path](#event-path)’s first struct’s [invocation target](#event-path-invocation-target); otherwise [shadow root](#concept-shadow-root)’s [host](#concept-documentfragment-host). 

The `mode` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [mode](#shadowroot-mode).

The `delegatesFocus` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [delegates focus](#shadowroot-delegates-focus).

The `slotAssignment` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [slot assignment](#shadowroot-slot-assignment). 

The `clonable` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [clonable](#shadowroot-clonable). 

The `serializable` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [serializable](#shadowroot-serializable). 

The `host` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [host](#concept-documentfragment-host). 

The `onslotchange` attribute is an [event handler IDL attribute](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-idl-attributes) for the `onslotchange`[event handler](https://html.spec.whatwg.org/multipage/webappapis.html#event-handlers), whose [event handler event type](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-event-type) is [slotchange](#eventdef-htmlslotelement-slotchange). 

In shadow-including tree order is [shadow-including preorder, depth-first traversal](#shadow-including-preorder-depth-first-traversal) of a [node tree](#concept-node-tree). Shadow-including preorder, depth-first traversal of a [node tree](#concept-node-tree)tree is preorder, depth-first traversal of tree, with for each [shadow host](#element-shadow-host) encountered in tree, [shadow-including preorder, depth-first traversal](#shadow-including-preorder-depth-first-traversal) of that [element](#concept-element)’s [shadow root](#concept-element-shadow-root)’s [node tree](#concept-node-tree) just after it is encountered. 

The shadow-including root of an object is its [root](#concept-tree-root)’s [host](#concept-documentfragment-host)’s [shadow-including root](#concept-shadow-including-root), if the object’s [root](#concept-tree-root) is a [shadow root](#concept-shadow-root); otherwise its [root](#concept-tree-root). 

An object A is a shadow-including descendant of an object B, if A is a [descendant](#concept-tree-descendant) of B, or A’s [root](#concept-tree-root) is a [shadow root](#concept-shadow-root) and A’s [root](#concept-tree-root)’s [host](#concept-documentfragment-host) is a [shadow-including inclusive descendant](#concept-shadow-including-inclusive-descendant) of B. 

A shadow-including inclusive descendant is an object or one of its [shadow-including descendants](#concept-shadow-including-descendant). 

An object A is a shadow-including ancestor of an object B, if and only if B is a [shadow-including descendant](#concept-shadow-including-descendant) of A. 

A shadow-including inclusive ancestor is an object or one of its [shadow-including ancestors](#concept-shadow-including-ancestor). 

A [node](#concept-node)A is closed-shadow-hidden from a [node](#concept-node)B if all of the following conditions are true: 

- 

A’s [root](#concept-tree-root) is a [shadow root](#concept-shadow-root). 

- 

A’s [root](#concept-tree-root) is not a [shadow-including inclusive ancestor](#concept-shadow-including-inclusive-ancestor) of B. 

- 

A’s [root](#concept-tree-root) is a [shadow root](#concept-shadow-root) whose [mode](#shadowroot-mode) is "`closed`" or A’s [root](#concept-tree-root)’s [host](#concept-documentfragment-host) is [closed-shadow-hidden](#concept-closed-shadow-hidden) from B. 

To retarget an object A against an object B, repeat these steps until they return an object:

1. 

If one of the following is true 

  - A is not a [node](#concept-node)
  - A’s [root](#concept-tree-root) is not a [shadow root](#concept-shadow-root)
  - B is a [node](#concept-node) and A’s [root](#concept-tree-root) is a [shadow-including inclusive ancestor](#concept-shadow-including-inclusive-ancestor) of B

then return A. 

2. 

Set A to A’s [root](#concept-tree-root)’s [host](#concept-documentfragment-host). 

The [retargeting](#retarget) algorithm is used by [event dispatch](#concept-event-dispatch) as well as other specifications, such as Fullscreen. [[FULLSCREEN]](#biblio-fullscreen)

### 4.9. Interface [Element](#element)#interface-element

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface Element : Node#node {
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespaceURI#dom-element-namespaceuri;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? prefix#dom-element-prefix;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName#dom-element-localname;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString tagName#dom-element-tagname;

  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString id#dom-element-id;
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString className#dom-element-classname;
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject, PutForwardshttps://webidl.spec.whatwg.org/#PutForwards=value#dom-domtokenlist-value] readonly attribute DOMTokenList#domtokenlist classList#dom-element-classlist;
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, Unscopablehttps://webidl.spec.whatwg.org/#Unscopable] attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString slot#dom-element-slot;

  booleanhttps://webidl.spec.whatwg.org/#idl-boolean hasAttributes#dom-element-hasattributes();
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute NamedNodeMap#namednodemap attributes#dom-element-attributes;
  sequencehttps://webidl.spec.whatwg.org/#idl-sequence<DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString> getAttributeNames#dom-element-getattributenames();
  DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? getAttribute#dom-element-getattribute(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName);
  DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? getAttributeNS#dom-element-getattributens(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined setAttribute#dom-element-setattribute(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName, (TrustedTypehttps://w3c.github.io/trusted-types/dist/spec/#typedefdef-trustedtype or DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString) value);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined setAttributeNS#dom-element-setattributens(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName, (TrustedTypehttps://w3c.github.io/trusted-types/dist/spec/#typedefdef-trustedtype or DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString) value);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined removeAttribute#dom-element-removeattribute(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined removeAttributeNS#dom-element-removeattributens(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] booleanhttps://webidl.spec.whatwg.org/#idl-boolean toggleAttribute#dom-element-toggleattribute(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName, optional booleanhttps://webidl.spec.whatwg.org/#idl-boolean force);
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean hasAttribute#dom-element-hasattribute(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName);
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean hasAttributeNS#dom-element-hasattributens(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName);

  Attr#attr? getAttributeNode#dom-element-getattributenode(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName);
  Attr#attr? getAttributeNodeNS#dom-element-getattributenodens(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Attr#attr? setAttributeNode#dom-element-setattributenode(Attr#attr attr);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Attr#attr? setAttributeNodeNS#dom-element-setattributenodens(Attr#attr attr);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Attr#attr removeAttributeNode#dom-element-removeattributenode(Attr#attr attr);

  ShadowRoot#shadowroot attachShadow#dom-element-attachshadow(ShadowRootInit#dictdef-shadowrootinit init);
  readonly attribute ShadowRoot#shadowroot? shadowRoot#dom-element-shadowroot;

  readonly attribute CustomElementRegistryhttps://html.spec.whatwg.org/multipage/custom-elements.html#customelementregistry? customElementRegistry#dom-element-customelementregistry;

  Element#element? closest#dom-element-closest(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString selectors);
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean matches#dom-element-matches(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString selectors);
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean webkitMatchesSelector#dom-element-webkitmatchesselector(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString selectors); // legacy alias of .matches

  HTMLCollection#htmlcollection getElementsByTagName#dom-element-getelementsbytagname(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName);
  HTMLCollection#htmlcollection getElementsByTagNameNS#dom-element-getelementsbytagnamens(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName);
  HTMLCollection#htmlcollection getElementsByClassName#dom-element-getelementsbyclassname(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString classNames);

  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Element#element? insertAdjacentElement#dom-element-insertadjacentelement(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString where, Element#element element); // legacy
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined insertAdjacentText#dom-element-insertadjacenttext(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString where, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString data); // legacy
};

dictionary ShadowRootInit {
  required ShadowRootMode#enumdef-shadowrootmode mode;
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean delegatesFocus = false;
  SlotAssignmentMode#enumdef-slotassignmentmode slotAssignment = "named";
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean clonable = false;
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean serializable = false;
  CustomElementRegistryhttps://html.spec.whatwg.org/multipage/custom-elements.html#customelementregistry? customElementRegistry;
};
```

[ShadowRootInit](#dictdef-shadowrootinit) somewhat unusually allows both `undefined` and `null` to be passed to its [customElementRegistry](#dom-shadowrootinit-customelementregistry) member to allow web developers to pass a [ShadowRoot](#shadowroot) node instead of a dictionary to [attachShadow()](#dom-element-attachshadow). 

[Element](#element)[nodes](#concept-node) are simply known as elements. 

[Elements](#concept-element) have an associated: 

namespaceNull or a non-empty string. namespace prefixNull or a non-empty string. local nameA non-empty string. custom element registryNull or a [CustomElementRegistry](https://html.spec.whatwg.org/multipage/custom-elements.html#customelementregistry) object. custom element state"`undefined`", "`failed`", "`uncustomized`", "`precustomized`", or "`custom`". custom element definitionNull or a [custom element definition](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-definition). `is` valueNull or a [valid custom element name](https://html.spec.whatwg.org/multipage/custom-elements.html#valid-custom-element-name). 

When an [element](#concept-element) is [created](#concept-create-element), all of these values are initialized. 

An [element](#concept-element) whose [custom element state](#concept-element-custom-element-state) is "`uncustomized`" or "`custom`" is said to be defined. An [element](#concept-element) whose [custom element state](#concept-element-custom-element-state) is "`custom`" is said to be custom. 

Whether or not an element is [defined](#concept-element-defined) is used to determine the behavior of the [:defined](https://drafts.csswg.org/selectors-4/#defined-pseudo) pseudo-class. Whether or not an element is [custom](#concept-element-custom) is used to determine the behavior of the [mutation algorithms](#mutation-algorithms). The "`failed`" and "`precustomized`" states are used to ensure that if a [custom element constructor](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-constructor) fails to execute correctly the first time, it is not executed again by an [upgrade](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-upgrade-an-element).

#example-c5b21302

The following code illustrates elements in each of these four states:

```
<!DOCTYPE html>
<script>
  window.customElements.define("sw-rey", class extends HTMLElement {})
  window.customElements.define("sw-finn", class extends HTMLElement {}, { extends: "p" })
  window.customElements.define("sw-kylo", class extends HTMLElement {
    constructor() {
      // super() intentionally omitted for this example
    }
  })
</script>

<!-- "undefined" (not defined, not custom) -->
<sw-han></sw-han>
<p is="sw-luke"></p>
<p is="asdf"></p>

<!-- "failed" (not defined, not custom) -->
<sw-kylo></sw-kylo>

<!-- "uncustomized" (defined, not custom) -->
<p></p>
<asdf></asdf>

<!-- "custom" (defined, custom) -->
<sw-rey></sw-rey>
<p is="sw-finn"></p>
```

[Elements](#concept-element) also have an associated shadow root (null or a [shadow root](#concept-shadow-root)). It is null unless otherwise stated. An [element](#concept-element) is a shadow host if its [shadow root](#concept-element-shadow-root) is non-null. 

An [element](#concept-element)’s qualified name is its [local name](#concept-element-local-name) if its [namespace prefix](#concept-element-namespace-prefix) is null; otherwise its [namespace prefix](#concept-element-namespace-prefix), followed by "`:`", followed by its [local name](#concept-element-local-name). 

An [element](#concept-element)’s HTML-uppercased qualified name is the return value of these steps: 

1. 

Let qualifiedName be [this](https://webidl.spec.whatwg.org/#this)’s [qualified name](#concept-element-qualified-name). 

2. 

If [this](https://webidl.spec.whatwg.org/#this) is in the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace) and its [node document](#concept-node-document) is an [HTML document](#html-document), then set qualifiedName to qualifiedName in [ASCII uppercase](https://infra.spec.whatwg.org/#ascii-uppercase). 

3. Return qualifiedName. 

User agents could optimize [qualified name](#concept-element-qualified-name) and [HTML-uppercased qualified name](#element-html-uppercased-qualified-name) by storing them in internal slots. 

To create an element, given a [document](#concept-document)document, string localName, string-or-null namespace, and optionally a string-or-null prefix (default null), string-or-null is (default null), boolean synchronousCustomElements (default false), and "`default`", null, or a [CustomElementRegistry](https://html.spec.whatwg.org/multipage/custom-elements.html#customelementregistry) object registry (default "`default`"): 

1. 

Let result be null. 

2. 

If registry is "`default`", then set registry to the result of [looking up a custom element registry](https://html.spec.whatwg.org/multipage/custom-elements.html#look-up-a-custom-element-registry) given document. 

3. 

Let definition be the result of [looking up a custom element definition](https://html.spec.whatwg.org/multipage/custom-elements.html#look-up-a-custom-element-definition) given registry, namespace, localName, and is. 

4. 

If definition is non-null, and definition’s [name](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-name) is not equal to its [local name](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-local-name) (i.e., definition represents a [customized built-in element](https://html.spec.whatwg.org/multipage/custom-elements.html#customized-built-in-element)): 

  1. 

Let interface be the [element interface](#concept-element-interface) for localName and the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace). 

  2. 

Set result to the result of [creating an element internal](#create-an-element-internal) given document, interface, localName, the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace), prefix, "`undefined`", is, and registry. 

  3. 

If synchronousCustomElements is true, then run this step while catching any exceptions: 

    1. 

[Upgrade](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-upgrade-an-element)result using definition. 

If this step threw an exception exception: 

    1. 

[Report](https://html.spec.whatwg.org/multipage/webappapis.html#report-an-exception)exception for definition’s [constructor](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-constructor)’s corresponding JavaScript object’s [associated realm](https://webidl.spec.whatwg.org/#dfn-associated-realm)’s [global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-realm-global). 

    2. 

Set result’s [custom element state](#concept-element-custom-element-state) to "`failed`". 

  4. 

Otherwise, [enqueue a custom element upgrade reaction](https://html.spec.whatwg.org/multipage/custom-elements.html#enqueue-a-custom-element-upgrade-reaction) given result and definition. 

5. 

Otherwise, if definition is non-null: 

  1. 

If synchronousCustomElements is true: 

    1. 

Let C be definition’s [constructor](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-constructor). 

    2. 

[Set](https://infra.spec.whatwg.org/#map-set) the [surrounding agent](https://tc39.es/ecma262/#surrounding-agent)’s [active custom element constructor map](https://html.spec.whatwg.org/multipage/custom-elements.html#active-custom-element-constructor-map)[C] to registry. 

    3. 

Run these steps while catching any exceptions: 

      1. 

Set result to the result of [constructing](https://webidl.spec.whatwg.org/#construct-a-callback-function)C, with no arguments. 

      2. 

Assert: result’s [custom element state](#concept-element-custom-element-state) and [custom element definition](#concept-element-custom-element-definition) are initialized. 

      3. 

Assert: result’s [namespace](#concept-element-namespace) is the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace). 

IDL enforces that result is an [HTMLElement](https://html.spec.whatwg.org/multipage/dom.html#htmlelement) object, which all use the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace). 

      4. 

If result’s [attribute list](#concept-element-attribute)[is not empty](https://infra.spec.whatwg.org/#list-is-empty), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotSupportedError](https://webidl.spec.whatwg.org/#notsupportederror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

      5. 

If result has [children](#concept-tree-child), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotSupportedError](https://webidl.spec.whatwg.org/#notsupportederror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

      6. 

If result’s [parent](#concept-tree-parent) is non-null, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotSupportedError](https://webidl.spec.whatwg.org/#notsupportederror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

      7. 

If result’s [node document](#concept-node-document) is not document, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotSupportedError](https://webidl.spec.whatwg.org/#notsupportederror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

      8. 

If result’s [local name](#concept-element-local-name) is not equal to localName, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotSupportedError](https://webidl.spec.whatwg.org/#notsupportederror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

      9. 

Set result’s [namespace prefix](#concept-element-namespace-prefix) to prefix. 

      10. 

Set result’s [is value](#concept-element-is-value) to null. 

      11. 

Set result’s [custom element registry](#element-custom-element-registry) to registry. 

If any of these steps threw an exception exception: 

      1. 

[Report](https://html.spec.whatwg.org/multipage/webappapis.html#report-an-exception)exception for definition’s [constructor](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-constructor)’s corresponding JavaScript object’s [associated realm](https://webidl.spec.whatwg.org/#dfn-associated-realm)’s [global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-realm-global). 

      2. 

Set result to the result of [creating an element internal](#create-an-element-internal) given document, [HTMLUnknownElement](https://html.spec.whatwg.org/multipage/dom.html#htmlunknownelement), localName, the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace), prefix, "`failed`", null, and registry. 

    4. 

[Remove](https://infra.spec.whatwg.org/#map-remove) the [surrounding agent](https://tc39.es/ecma262/#surrounding-agent)’s [active custom element constructor map](https://html.spec.whatwg.org/multipage/custom-elements.html#active-custom-element-constructor-map)[C]. 

Under normal circumstances it will already have been removed at this point. 

  2. 

Otherwise: 

    1. 

Set result to the result of [creating an element internal](#create-an-element-internal) given document, [HTMLElement](https://html.spec.whatwg.org/multipage/dom.html#htmlelement), localName, the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace), prefix, "`undefined`", null, and registry. 

    2. 

[Enqueue a custom element upgrade reaction](https://html.spec.whatwg.org/multipage/custom-elements.html#enqueue-a-custom-element-upgrade-reaction) given result and definition. 

6. 

Otherwise: 

  1. 

Let interface be the [element interface](#concept-element-interface) for localName and namespace. 

  2. 

Set result to the result of [creating an element internal](#create-an-element-internal) given document, interface, localName, namespace, prefix, "`uncustomized`", is, and registry. 

  3. 

If namespace is the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace), and either localName is a [valid custom element name](https://html.spec.whatwg.org/multipage/custom-elements.html#valid-custom-element-name) or is is non-null, then set result’s [custom element state](#concept-element-custom-element-state) to "`undefined`". 

7. 

Return result. 

To create an element internal given a [document](#concept-document)document, an interface interface a string localName, a string-or-null namespace, a string-or-null prefix, a string state, a string-or-null is, and null or a [CustomElementRegistry](https://html.spec.whatwg.org/multipage/custom-elements.html#customelementregistry) object registry: 

1. 

Let element be a new [element](#concept-element) that implements interface, with [namespace](#concept-element-namespace) set to namespace, [namespace prefix](#concept-element-namespace-prefix) set to prefix, [local name](#concept-element-local-name) set to localName, [custom element registry](#element-custom-element-registry) set to registry, [custom element state](#concept-element-custom-element-state) set to state, [custom element definition](#concept-element-custom-element-definition) set to null, [is value](#concept-element-is-value) set to is, and [node document](#concept-node-document) set to document. 

2. 

[Assert](https://infra.spec.whatwg.org/#assert): element’s [attribute list](#concept-element-attribute)[is empty](https://infra.spec.whatwg.org/#list-is-empty). 

3. 

Return element. 

[Elements](#concept-element) also have an attribute list, which is a [list](https://infra.spec.whatwg.org/#list) exposed through a [NamedNodeMap](#namednodemap). Unless explicitly given when an [element](#concept-element) is created, its [attribute list](#concept-element-attribute)[is empty](https://infra.spec.whatwg.org/#list-is-empty). 

An [element](#concept-element)has an [attribute](#concept-attribute)A if its [attribute list](#concept-element-attribute)[contains](https://infra.spec.whatwg.org/#list-contain)A. 

This and [other specifications](#other-applicable-specifications) may define attribute change steps for [elements](#concept-element). The algorithm is passed element, localName, oldValue, value, and namespace. 

To handle attribute changes for an [attribute](#concept-attribute)attribute with element, oldValue, and newValue, run these steps: 

1. 

[Queue a mutation record](#queue-a-mutation-record) of "`attributes`" for element with attribute’s [local name](#concept-attribute-local-name), attribute’s [namespace](#concept-attribute-namespace), oldValue, « », « », null, and null. 

2. 

If element is [custom](#concept-element-custom), then [enqueue a custom element callback reaction](https://html.spec.whatwg.org/multipage/custom-elements.html#enqueue-a-custom-element-callback-reaction) with element, callback name "`attributeChangedCallback`", and « attribute’s [local name](#concept-attribute-local-name), oldValue, newValue, attribute’s [namespace](#concept-attribute-namespace) ». 

3. 

Run the [attribute change steps](#concept-element-attributes-change-ext) with element, attribute’s [local name](#concept-attribute-local-name), oldValue, newValue, and attribute’s [namespace](#concept-attribute-namespace). 

To change an [attribute](#concept-attribute)attribute to value, run these steps: 

1. 

Let oldValue be attribute’s [value](#concept-attribute-value).

2. 

Set attribute’s [value](#concept-attribute-value) to value. 

3. 

[Handle attribute changes](#handle-attribute-changes) for attribute with attribute’s [element](#concept-attribute-element), oldValue, and value. 

To append an [attribute](#concept-attribute)attribute to an [element](#concept-element)element, run these steps: 

1. 

[Append](https://infra.spec.whatwg.org/#list-append)attribute to element’s [attribute list](#concept-element-attribute). 

2. 

Set attribute’s [element](#concept-attribute-element) to element. 

3. 

Set attribute’s [node document](#concept-node-document) to element’s [node document](#concept-node-document). 

4. 

[Handle attribute changes](#handle-attribute-changes) for attribute with element, null, and attribute’s [value](#concept-attribute-value). 

To remove an [attribute](#concept-attribute)attribute, run these steps: 

1. 

Let element be attribute’s [element](#concept-attribute-element).

2. [Remove](https://infra.spec.whatwg.org/#list-remove)attribute from element’s [attribute
 list](#concept-element-attribute). 
3. 

Set attribute’s [element](#concept-attribute-element) to null. 

4. 

[Handle attribute changes](#handle-attribute-changes) for attribute with element, attribute’s [value](#concept-attribute-value), and null. 

To replace an [attribute](#concept-attribute)oldAttribute with an [attribute](#concept-attribute)newAttribute: 

1. 

Let element be oldAttribute’s [element](#concept-attribute-element).

2. 

[Replace](https://infra.spec.whatwg.org/#list-replace)oldAttribute by newAttribute in element’s [attribute list](#concept-element-attribute). 

3. 

Set newAttribute’s [element](#concept-attribute-element) to element. 

4. 

Set newAttribute’s [node document](#concept-node-document) to element’s [node document](#concept-node-document). 

5. 

Set oldAttribute’s [element](#concept-attribute-element) to null. 

6. 

[Handle attribute changes](#handle-attribute-changes) for oldAttribute with element, oldAttribute’s [value](#concept-attribute-value), and newAttribute’s [value](#concept-attribute-value). 

To get an attribute by name given a string qualifiedName and an [element](#concept-element)element: 

1. 

If element is in the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace) and its [node document](#concept-node-document) is an [HTML document](#html-document), then set qualifiedName to qualifiedName in [ASCII lowercase](https://infra.spec.whatwg.org/#ascii-lowercase). 

2. 

Return the first [attribute](#concept-attribute) in element’s [attribute list](#concept-element-attribute) whose [qualified name](#concept-attribute-qualified-name) is qualifiedName; otherwise null. 

To get an attribute by namespace and local name given null or a string namespace, a string localName, and an [element](#concept-element)element: 

1. 

If namespace is the empty string, then set it to null. 

2. 

Return the [attribute](#concept-attribute) in element’s [attribute list](#concept-element-attribute) whose [namespace](#concept-attribute-namespace) is namespace and [local name](#concept-attribute-local-name) is localName, if any; otherwise null. 

To get an attribute value given an [element](#concept-element)element, a string localName, and an optional null or string namespace (default null):

1. 

Let attr be the result of [getting an attribute](#concept-element-attributes-get-by-namespace) given namespace, localName, and element.

2. 

If attr is null, then return the empty string.

3. 

Return attr’s [value](#concept-attribute-value).

To set an attribute given an [attribute](#concept-attribute)attr and an [element](#concept-element)element: 

1. 

Let verifiedValue be the result of calling [get trusted type compliant attribute value](https://w3c.github.io/trusted-types/dist/spec/#get-trusted-type-compliant-attribute-value) with attr’s [local name](#concept-attribute-local-name), attr’s [namespace](#concept-attribute-namespace), element, and attr’s [value](#concept-attribute-value). [[TRUSTED-TYPES]](#biblio-trusted-types)

2. 

If attr’s [element](#concept-attribute-element) is neither null nor element, [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InUseAttributeError](https://webidl.spec.whatwg.org/#inuseattributeerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

Let oldAttr be the result of [getting an attribute](#concept-element-attributes-get-by-namespace) given attr’s [namespace](#concept-attribute-namespace), attr’s [local name](#concept-attribute-local-name), and element. 

4. 

If oldAttr is attr, return attr. 

5. 

Set attr’s [value](#concept-attribute-value) to verifiedValue. 

6. 

If oldAttr is non-null, then [replace](#concept-element-attributes-replace)oldAttr with attr. 

7. 

Otherwise, [append](#concept-element-attributes-append)attr to element. 

8. 

Return oldAttr. 

To set an attribute value given an [element](#concept-element)element, a string localName, a string value, an optional null or string prefix (default null), and an optional null or string namespace (default null): 

1. Let attribute be the result of [getting an attribute](#concept-element-attributes-get-by-namespace) given namespace, localName, and element. 
2. If attribute is null, create an [attribute](#concept-attribute) whose [namespace](#concept-attribute-namespace) is namespace, [namespace prefix](#concept-attribute-namespace-prefix) is prefix, [local name](#concept-attribute-local-name) is localName, [value](#concept-attribute-value) is value, and [node document](#concept-node-document) is element’s [node document](#concept-node-document), then [append](#concept-element-attributes-append) this [attribute](#concept-attribute) to element, and then return. 
3. 

[Change](#concept-element-attributes-change)attribute to value. 

To remove an attribute by name given a string qualifiedName and an [element](#concept-element)element: 

1. 

Let attr be the result of [getting an attribute](#concept-element-attributes-get-by-name) given qualifiedName and element. 

2. 

If attr is non-null, then [remove](#concept-element-attributes-remove)attr. 

3. 

Return attr. 

To remove an attribute by namespace and local name given null or a string namespace, a string localName, and an [element](#concept-element)element: 

1. 

Let attr be the result of [getting an attribute](#concept-element-attributes-get-by-namespace) given namespace, localName, and element. 

2. 

If attr is non-null, then [remove](#concept-element-attributes-remove)attr. 

3. 

Return attr. 

An [element](#concept-element) can have an associated unique identifier (ID)

Historically [elements](#concept-element) could have multiple identifiers e.g., by using the HTML `id`[attribute](#concept-attribute) and a DTD. This specification makes [ID](#concept-id) a concept of the DOM and allows for only one per [element](#concept-element), given by an [id attribute](#concept-named-attribute). 

Use these [attribute change steps](#concept-element-attributes-change-ext) to update an [element](#concept-element)’s [ID](#concept-id): 

1. 

If localName is `id`, namespace is null, and value is null or the empty string, then unset element’s [ID](#concept-id). 

2. 

Otherwise, if localName is `id`, namespace is null, then set element’s [ID](#concept-id) to value. 

While this specification defines requirements for `class`, `id`, and `slot`[attributes](#concept-attribute) on any [element](#concept-element), it makes no claims as to whether using them is conforming or not. 

A [node](#concept-node)’s [parent](#concept-tree-parent) of type [Element](#element) is known as its parent element. If the [node](#concept-node) has a [parent](#concept-tree-parent) of a different type, its [parent element](#parent-element) is null. 

namespace = element . [namespaceURI](#dom-element-namespaceuri)Returns the [namespace](#concept-element-namespace). prefix = element . [prefix](#dom-element-prefix)Returns the [namespace prefix](#concept-element-namespace-prefix). localName = element . [localName](#dom-element-localname)Returns the [local name](#concept-element-local-name). qualifiedName = element . [tagName](#dom-element-tagname)Returns the [HTML-uppercased qualified name](#element-html-uppercased-qualified-name). 

The `namespaceURI` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [namespace](#concept-element-namespace). 

The `prefix` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [namespace prefix](#concept-element-namespace-prefix). 

The `localName` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [local name](#concept-element-local-name). 

The `tagName` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [HTML-uppercased qualified name](#element-html-uppercased-qualified-name). 

[id](#dom-element-id)`element .  [ = value ]`

Returns the value of element’s `id` content attribute. Can be set to change it. 

[className](#dom-element-classname)`element .  [ = value ]`

Returns the value of element’s `class` content attribute. Can be set to change it. 

[classList](#dom-element-classlist)`element .`

Allows for manipulation of element’s `class` content attribute as a set of whitespace-separated tokens through a [DOMTokenList](#domtokenlist) object. 

[slot](#dom-element-slot)`element .  [ = value ]`

Returns the value of element’s `slot` content attribute. Can be set to change it. 

IDL attributes that are defined to reflect a string name, must have these getter and setter steps:

getter steps 

Return the result of running [get an attribute value](#concept-element-attributes-get-value) given [this](https://webidl.spec.whatwg.org/#this) and name.

setter steps 

[Set an attribute value](#concept-element-attributes-set-value) for [this](https://webidl.spec.whatwg.org/#this) using name and the given value. 

The `id` attribute must [reflect](#concept-reflect) "`id`". 

The `className` attribute must [reflect](#concept-reflect) "`class`". 

The `classList` getter steps are to return a [DOMTokenList](#domtokenlist) object whose associated [element](#concept-element) is [this](https://webidl.spec.whatwg.org/#this) and whose associated [attribute](#concept-attribute)’s [local name](#concept-attribute-local-name) is `class`. The [token set](#concept-dtl-tokens) of this particular [DOMTokenList](#domtokenlist) object are also known as the [element](#concept-element)’s classes. 

The `slot` attribute must [reflect](#concept-reflect) "`slot`". 

`id`, `class`, and `slot` are effectively superglobal attributes as they can appear on any element, regardless of that element’s namespace.

[hasAttributes](#dom-element-hasattributes)`element . ()`

Returns true if element has attributes; otherwise false. 

[getAttributeNames](#dom-element-getattributenames)`element . ()`

Returns the [qualified names](#concept-attribute-qualified-name) of all element’s [attributes](#concept-attribute). Can contain duplicates. 

[getAttribute](#dom-element-getattribute)`element . (qualifiedName)`

Returns element’s first [attribute](#concept-attribute) whose [qualified name](#concept-attribute-qualified-name) is qualifiedName, and null if there is no such [attribute](#concept-attribute) otherwise. 

[getAttributeNS](#dom-element-getattributens)`element . (namespace, localName)`

Returns element’s [attribute](#concept-attribute) whose [namespace](#concept-attribute-namespace) is namespace and [local name](#concept-attribute-local-name) is localName, and null if there is no such [attribute](#concept-attribute) otherwise. 

[setAttribute](#dom-element-setattribute)`element . (qualifiedName, value)`

Sets the [value](#concept-attribute-value) of element’s first [attribute](#concept-attribute) whose [qualified name](#concept-attribute-qualified-name) is qualifiedName to value. 

[setAttributeNS](#dom-element-setattributens)`element . (namespace, localName, value)`

Sets the [value](#concept-attribute-value) of element’s [attribute](#concept-attribute) whose [namespace](#concept-attribute-namespace) is namespace and [local name](#concept-attribute-local-name) is localName to value. 

[removeAttribute](#dom-element-removeattribute)`element . (qualifiedName)`

Removes element’s first [attribute](#concept-attribute) whose [qualified name](#concept-attribute-qualified-name) is qualifiedName. 

[removeAttributeNS](#dom-element-removeattributens)`element . (namespace, localName)`

Removes element’s [attribute](#concept-attribute) whose [namespace](#concept-attribute-namespace) is namespace and [local name](#concept-attribute-local-name) is localName. 

[toggleAttribute](#dom-element-toggleattribute)`element . (qualifiedName [, force])`

If force is not given, "toggles" qualifiedName, removing it if it is present and adding it if it is not present. If force is true, adds qualifiedName. If force is false, removes qualifiedName. 

Returns true if qualifiedName is now present; otherwise false. 

[hasAttribute](#dom-element-hasattribute)`element . (qualifiedName)`

Returns true if element has an [attribute](#concept-attribute) whose [qualified name](#concept-attribute-qualified-name) is qualifiedName; otherwise false. 

[hasAttributeNS](#dom-element-hasattributens)`element . (namespace, localName)`

Returns true if element has an [attribute](#concept-attribute) whose [namespace](#concept-attribute-namespace) is namespace and [local name](#concept-attribute-local-name) is localName. 

The `hasAttributes()` method steps are to return false if [this](https://webidl.spec.whatwg.org/#this)’s [attribute list](#concept-element-attribute)[is empty](https://infra.spec.whatwg.org/#list-is-empty); otherwise true. 

The `attributes` getter steps are to return the associated [NamedNodeMap](#namednodemap). 

The `getAttributeNames()` method steps are to return the [qualified names](#concept-attribute-qualified-name) of the [attributes](#concept-attribute) in [this](https://webidl.spec.whatwg.org/#this)’s [attribute list](#concept-element-attribute), in order; otherwise a new [list](https://infra.spec.whatwg.org/#list). 

These are not guaranteed to be unique. 

The `getAttribute(qualifiedName)` method steps are: 

1. 

Let attr be the result of [getting an attribute](#concept-element-attributes-get-by-name) given qualifiedName and [this](https://webidl.spec.whatwg.org/#this). 

2. 

If attr is null, return null. 

3. 

Return attr’s [value](#concept-attribute-value). 

The `getAttributeNS(namespace, localName)` method steps are: 

1. 

Let attr be the result of [getting an attribute](#concept-element-attributes-get-by-namespace) given namespace, localName, and [this](https://webidl.spec.whatwg.org/#this). 

2. 

If attr is null, return null. 

3. 

Return attr’s [value](#concept-attribute-value). 

The `setAttribute(qualifiedName, value)` method steps are: 

1. 

If qualifiedName is not a [valid attribute local name](#valid-attribute-local-name), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidCharacterError](https://webidl.spec.whatwg.org/#invalidcharactererror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

#node-setAttribute-qualifiedNameDespite the parameter naming, qualifiedName is only used as a [qualified name](#concept-attribute-qualified-name) if an [attribute](#concept-attribute) already exists with that qualified name. Otherwise, it is used as the [local name](#concept-attribute-local-name) of the new attribute. We only need to validate it for the latter case. 

2. 

If [this](https://webidl.spec.whatwg.org/#this) is in the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace) and its [node document](#concept-node-document) is an [HTML document](#html-document), then set qualifiedName to qualifiedName in [ASCII lowercase](https://infra.spec.whatwg.org/#ascii-lowercase). 

3. 

Let verifiedValue be the result of calling [get trusted type compliant attribute value](https://w3c.github.io/trusted-types/dist/spec/#get-trusted-type-compliant-attribute-value) with qualifiedName, null, [this](https://webidl.spec.whatwg.org/#this), and value. [[TRUSTED-TYPES]](#biblio-trusted-types)

4. 

Let attribute be the first [attribute](#concept-attribute) in [this](https://webidl.spec.whatwg.org/#this)’s [attribute list](#concept-element-attribute) whose [qualified name](#concept-attribute-qualified-name) is qualifiedName, and null otherwise. 

5. 

If attribute is non-null, then [change](#concept-element-attributes-change)attribute to verifiedValue and return. 

6. 

Set attribute to a new [attribute](#concept-attribute) whose [local name](#concept-attribute-local-name) is qualifiedName, [value](#concept-attribute-value) is verifiedValue, and [node document](#concept-node-document) is [this](https://webidl.spec.whatwg.org/#this)’s [node document](#concept-node-document). 

7. 

[Append](#concept-element-attributes-append)attribute to [this](https://webidl.spec.whatwg.org/#this). 

The `setAttributeNS(namespace, qualifiedName, value)` method steps are: 

1. 

Let (namespace, prefix, localName) be the result of [validating and extracting](#validate-and-extract)namespace and qualifiedName given "`attribute`". 

2. 

Let verifiedValue be the result of calling [get trusted type compliant attribute value](https://w3c.github.io/trusted-types/dist/spec/#get-trusted-type-compliant-attribute-value) with localName, namespace, [this](https://webidl.spec.whatwg.org/#this), and value. [[TRUSTED-TYPES]](#biblio-trusted-types)

3. 

[Set an attribute value](#concept-element-attributes-set-value) for [this](https://webidl.spec.whatwg.org/#this) using localName, verifiedValue, prefix, and namespace. 

The `removeAttribute(qualifiedName)` method steps are to [remove an attribute](#concept-element-attributes-remove-by-name) given qualifiedName and [this](https://webidl.spec.whatwg.org/#this), and then return undefined. 

The `removeAttributeNS(namespace, localName)` method steps are to [remove an attribute](#concept-element-attributes-remove-by-namespace) given namespace, localName, and [this](https://webidl.spec.whatwg.org/#this), and then return undefined. 

The `hasAttribute(qualifiedName)` method steps are: 

1. 

If [this](https://webidl.spec.whatwg.org/#this) is in the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace) and its [node document](#concept-node-document) is an [HTML document](#html-document), then set qualifiedName to qualifiedName in [ASCII lowercase](https://infra.spec.whatwg.org/#ascii-lowercase). 

2. 

Return true if [this](https://webidl.spec.whatwg.org/#this)[has](#concept-element-attribute-has) an [attribute](#concept-attribute) whose [qualified name](#concept-attribute-qualified-name) is qualifiedName; otherwise false. 

The `toggleAttribute(qualifiedName, force)` method steps are: 

1. 

If qualifiedName is not a [valid attribute local name](#valid-attribute-local-name), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidCharacterError](https://webidl.spec.whatwg.org/#invalidcharactererror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

See [the discussion above](#node-setAttribute-qualifiedName) about why we validate it as a local name, instead of a qualified name. 

2. 

If [this](https://webidl.spec.whatwg.org/#this) is in the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace) and its [node document](#concept-node-document) is an [HTML document](#html-document), then set qualifiedName to qualifiedName in [ASCII lowercase](https://infra.spec.whatwg.org/#ascii-lowercase). 

3. 

Let attribute be the first [attribute](#concept-attribute) in [this](https://webidl.spec.whatwg.org/#this)’s [attribute list](#concept-element-attribute) whose [qualified name](#concept-attribute-qualified-name) is qualifiedName, and null otherwise. 

4. 

If attribute is null: 

  1. 

If force is not given or is true, create an [attribute](#concept-attribute) whose [local name](#concept-attribute-local-name) is qualifiedName, [value](#concept-attribute-value) is the empty string, and [node document](#concept-node-document) is [this](https://webidl.spec.whatwg.org/#this)’s [node document](#concept-node-document), then [append](#concept-element-attributes-append) this [attribute](#concept-attribute) to [this](https://webidl.spec.whatwg.org/#this), and then return true. 

  2. 

Return false. 

5. 

Otherwise, if force is not given or is false, [remove an attribute](#concept-element-attributes-remove-by-name) given qualifiedName and [this](https://webidl.spec.whatwg.org/#this), and then return false. 

6. 

Return true. 

The `hasAttributeNS(namespace, localName)` method steps are: 

1. 

If namespace is the empty string, then set it to null. 

2. Return true if [this](https://webidl.spec.whatwg.org/#this)[has](#concept-element-attribute-has) an [attribute](#concept-attribute) whose [namespace](#concept-attribute-namespace) is namespace and [local name](#concept-attribute-local-name) is localName; otherwise false. 

The `getAttributeNode(qualifiedName)` method steps are to return the result of [getting an attribute](#concept-element-attributes-get-by-name) given qualifiedName and [this](https://webidl.spec.whatwg.org/#this). 

The `getAttributeNodeNS(namespace, localName)` method steps are to return the result of [getting an attribute](#concept-element-attributes-get-by-namespace) given namespace, localName, and [this](https://webidl.spec.whatwg.org/#this). 

The `setAttributeNode(attr)` and `setAttributeNodeNS(attr)` methods steps are to return the result of [setting an attribute](#concept-element-attributes-set) given attr and [this](https://webidl.spec.whatwg.org/#this). 

The `removeAttributeNode(attr)` method steps are: 

1. 

If [this](https://webidl.spec.whatwg.org/#this)’s [attribute list](#concept-element-attribute) does not [contain](https://infra.spec.whatwg.org/#list-contain)attr, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotFoundError](https://webidl.spec.whatwg.org/#notfounderror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

2. 

[Remove](#concept-element-attributes-remove)attr. 

3. 

Return attr. 

[attachShadow(init)](#dom-element-attachshadow)

Creates a [shadow root](#concept-shadow-root) for element and returns it. 

[shadowRoot](#dom-element-shadowroot)

Returns element’s [shadow root](#concept-element-shadow-root), if any, and if [shadow root](#concept-shadow-root)’s [mode](#shadowroot-mode) is "`open`"; otherwise null. 

A valid shadow host name is: 

- a [valid custom element name](https://html.spec.whatwg.org/multipage/custom-elements.html#valid-custom-element-name)
- "`article`", "`aside`", "`blockquote`", "`body`", "`div`", "`footer`", "`h1`", "`h2`", "`h3`", "`h4`", "`h5`", "`h6`", "`header`", "`main`", "`nav`", "`p`", "`section`", or "`span`" 

The `attachShadow(init)` method steps are: 

1. 

Let registry be [this](https://webidl.spec.whatwg.org/#this)’s [node document](#concept-node-document)’s [custom element registry](#document-custom-element-registry). 

2. 

If init["[customElementRegistry](#dom-shadowrootinit-customelementregistry)"] [exists](https://infra.spec.whatwg.org/#map-exists), then set registry to it. 

3. 

If registry is non-null, registry’s [is scoped](https://html.spec.whatwg.org/multipage/custom-elements.html#is-scoped) is false, and registry is not [this](https://webidl.spec.whatwg.org/#this)’s [node document](#concept-node-document)’s [custom element registry](#document-custom-element-registry), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotSupportedError](https://webidl.spec.whatwg.org/#notsupportederror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

4. 

Run [attach a shadow root](#concept-attach-a-shadow-root) with [this](https://webidl.spec.whatwg.org/#this), init["[mode](#dom-shadowrootinit-mode)"], init["[clonable](#dom-shadowrootinit-clonable)"], init["[serializable](#dom-shadowrootinit-serializable)"], init["[delegatesFocus](#dom-shadowrootinit-delegatesfocus)"], init["[slotAssignment](#dom-shadowrootinit-slotassignment)"], and registry. 

5. 

Return [this](https://webidl.spec.whatwg.org/#this)’s [shadow root](#concept-element-shadow-root). 

To attach a shadow root, given an [element](#concept-element)element, a string mode, a boolean clonable, a boolean serializable, a boolean delegatesFocus, a string slotAssignment, and null or a [CustomElementRegistry](https://html.spec.whatwg.org/multipage/custom-elements.html#customelementregistry) object registry: 

1. 

If element’s [namespace](#concept-element-namespace) is not the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotSupportedError](https://webidl.spec.whatwg.org/#notsupportederror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

2. 

If element’s [local name](#concept-element-local-name) is not a [valid shadow host name](#valid-shadow-host-name), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotSupportedError](https://webidl.spec.whatwg.org/#notsupportederror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

If element’s [local name](#concept-element-local-name) is a [valid custom element name](https://html.spec.whatwg.org/multipage/custom-elements.html#valid-custom-element-name), or element’s [is value](#concept-element-is-value) is non-null: 

  1. 

Let definition be the result of [looking up a custom element definition](https://html.spec.whatwg.org/multipage/custom-elements.html#look-up-a-custom-element-definition) given element’s [custom element registry](#element-custom-element-registry), its [namespace](#concept-element-namespace), its [local name](#concept-element-local-name), and its [is value](#concept-element-is-value). 

  2. 

If definition is non-null and definition’s [disable shadow](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-disable-shadow) is true, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotSupportedError](https://webidl.spec.whatwg.org/#notsupportederror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

4. 

If element is a [shadow host](#element-shadow-host): 

  1. 

Let currentShadowRoot be element’s [shadow root](#concept-element-shadow-root). 

  2. 

If any of the following are true: 

    - 

currentShadowRoot’s [declarative](#shadowroot-declarative) is false; or 

    - 

currentShadowRoot’s [mode](#shadowroot-mode) is not mode, 

then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotSupportedError](https://webidl.spec.whatwg.org/#notsupportederror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

  3. 

Otherwise: 

    1. 

[Remove](#concept-node-remove) all of currentShadowRoot’s [children](#concept-tree-child), in [tree order](#concept-tree-order). 

    2. 

Set currentShadowRoot’s [declarative](#shadowroot-declarative) to false. 

    3. 

Return. 

5. 

Let shadow be a new [shadow root](#concept-shadow-root) whose [node document](#concept-node-document) is element’s [node document](#concept-node-document), [host](#concept-documentfragment-host) is element, and [mode](#shadowroot-mode) is mode. 

6. 

Set shadow’s [delegates focus](#shadowroot-delegates-focus) to delegatesFocus. 

7. 

If element’s [custom element state](#concept-element-custom-element-state) is "`precustomized`" or "`custom`", then set shadow’s [available to element internals](#shadowroot-available-to-element-internals) to true. 

8. 

Set shadow’s [slot assignment](#shadowroot-slot-assignment) to slotAssignment. 

9. 

Set shadow’s [declarative](#shadowroot-declarative) to false. 

10. 

Set shadow’s [clonable](#shadowroot-clonable) to clonable. 

11. 

Set shadow’s [serializable](#shadowroot-serializable) to serializable. 

12. 

Set shadow’s [custom element registry](#shadowroot-custom-element-registry) to registry. 

13. 

Set element’s [shadow root](#concept-element-shadow-root) to shadow. 

The `shadowRoot` getter steps are: 

1. 

Let shadow be [this](https://webidl.spec.whatwg.org/#this)’s [shadow root](#concept-element-shadow-root). 

2. 

If shadow is null or its [mode](#shadowroot-mode) is "`closed`", then return null. 

3. 

Return shadow. 

[customElementRegistry](#dom-element-customelementregistry)

Returns element’s [CustomElementRegistry](https://html.spec.whatwg.org/multipage/custom-elements.html#customelementregistry) object, if any; otherwise null. 

The `customElementRegistry` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [custom element registry](#element-custom-element-registry). 

[closest(selectors)](#dom-element-closest)Returns the first (starting at element) [inclusive ancestor](#concept-tree-inclusive-ancestor) that matches selectors, and null otherwise. [matches(selectors)](#dom-element-matches)Returns true if matching selectors against element’s [root](#concept-tree-root) yields element; otherwise false. 

The `closest(selectors)` method steps are: 

1. 

Let selector be the result of [parse a selector](https://drafts.csswg.org/selectors-4/#parse-a-selector) from selectors. [[SELECTORS4]](#biblio-selectors4)

2. 

If selector is failure, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[SyntaxError](https://webidl.spec.whatwg.org/#syntaxerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

Let elements be [this](https://webidl.spec.whatwg.org/#this)’s [inclusive ancestors](#concept-tree-inclusive-ancestor) that are [elements](#concept-element), in reverse [tree order](#concept-tree-order). 

4. 

For each element of elements: if [match a selector against an element](https://drafts.csswg.org/selectors-4/#match-a-selector-against-an-element), using selector, element, and [scoping root](https://drafts.csswg.org/selectors-4/#scoping-root)[this](https://webidl.spec.whatwg.org/#this), returns success, return element. [[SELECTORS4]](#biblio-selectors4)

5. 

Return null. 

The `matches(selectors)` and `webkitMatchesSelector(selectors)` method steps are: 

1. 

Let selector be the result of [parse a selector](https://drafts.csswg.org/selectors-4/#parse-a-selector) from selectors. [[SELECTORS4]](#biblio-selectors4)

2. 

If selector is failure, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[SyntaxError](https://webidl.spec.whatwg.org/#syntaxerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

If the result of [match a selector against an element](https://drafts.csswg.org/selectors-4/#match-a-selector-against-an-element), using selector, [this](https://webidl.spec.whatwg.org/#this), and [scoping root](https://drafts.csswg.org/selectors-4/#scoping-root)[this](https://webidl.spec.whatwg.org/#this), returns success, then return true; otherwise, return false. [[SELECTORS4]](#biblio-selectors4)

The `getElementsByTagName(qualifiedName)` method steps are to return the [list of elements with qualified name qualifiedName](#concept-getelementsbytagname) for [this](https://webidl.spec.whatwg.org/#this). 

The `getElementsByTagNameNS(namespace, localName)` method steps are to return the [list of elements with namespace namespace and local
name localName](#concept-getelementsbytagnamens) for [this](https://webidl.spec.whatwg.org/#this). 

The `getElementsByClassName(classNames)` method steps are to return the [list of elements with class names classNames](#concept-getelementsbyclassname) for [this](https://webidl.spec.whatwg.org/#this). 

To insert adjacent, given an [element](#concept-element)element, string where, and a [node](#concept-node)node, run the steps associated with the first [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for where: 

"`beforebegin`" 

If element’s [parent](#concept-tree-parent) is null, return null. 

Return the result of [pre-inserting](#concept-node-pre-insert)node into element’s [parent](#concept-tree-parent) before element. 

"`afterbegin`" 

Return the result of [pre-inserting](#concept-node-pre-insert)node into element before element’s [first child](#concept-tree-first-child). 

"`beforeend`" 

Return the result of [pre-inserting](#concept-node-pre-insert)node into element before null. 

"`afterend`" 

If element’s [parent](#concept-tree-parent) is null, return null. 

Return the result of [pre-inserting](#concept-node-pre-insert)node into element’s [parent](#concept-tree-parent) before element’s [next sibling](#concept-tree-next-sibling). 

Otherwise 

[Throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[SyntaxError](https://webidl.spec.whatwg.org/#syntaxerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

The `insertAdjacentElement(where, element)` method steps are to return the result of running [insert adjacent](#insert-adjacent), give [this](https://webidl.spec.whatwg.org/#this), where, and element. 

The `insertAdjacentText(where, data)` method steps are: 

1. 

Let text be a new [Text](#text)[node](#concept-node) whose [data](#concept-cd-data) is data and [node document](#concept-node-document) is [this](https://webidl.spec.whatwg.org/#this)’s [node document](#concept-node-document). 

2. 

Run [insert adjacent](#insert-adjacent), given [this](https://webidl.spec.whatwg.org/#this), where, and text. 

This method returns nothing because it existed before we had a chance to design it. 

#### 4.9.1. Interface [NamedNodeMap](#namednodemap)#interface-namednodemap

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window,
 LegacyUnenumerableNamedPropertieshttps://webidl.spec.whatwg.org/#LegacyUnenumerableNamedProperties]
interface NamedNodeMap {
  readonly attribute unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long length#dom-namednodemap-length;
  getter Attr#attr? item#dom-namednodemap-item(unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long index);
  getter Attr#attr? getNamedItem#dom-namednodemap-getnameditem(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName);
  Attr#attr? getNamedItemNS#dom-namednodemap-getnameditemns(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Attr#attr? setNamedItem#dom-namednodemap-setnameditem(Attr#attr attr);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Attr#attr? setNamedItemNS#dom-namednodemap-setnameditemns(Attr#attr attr);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Attr#attr removeNamedItem#dom-namednodemap-removenameditem(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Attr#attr removeNamedItemNS#dom-namednodemap-removenameditemns(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName);
};
```

A [NamedNodeMap](#namednodemap) has an associated element (an [element](#concept-element)). 

A [NamedNodeMap](#namednodemap) object’s attribute list is its [element](#concept-namednodemap-element)’s [attribute list](#concept-element-attribute). 

A [NamedNodeMap](#namednodemap) object’s [supported property indices](https://webidl.spec.whatwg.org/#dfn-supported-property-indices) are the numbers in the range zero to its [attribute list](#concept-namednodemap-attribute)’s [size](https://infra.spec.whatwg.org/#list-size) − 1, unless the [attribute list](#concept-namednodemap-attribute)[is empty](https://infra.spec.whatwg.org/#list-is-empty), in which case there are no [supported property indices](https://webidl.spec.whatwg.org/#dfn-supported-property-indices). 

The `length` getter steps are to return the [attribute list](#concept-namednodemap-attribute)’s [size](https://infra.spec.whatwg.org/#list-size). 

The `item(index)` method steps are: 

1. 

If index is equal to or greater than [this](https://webidl.spec.whatwg.org/#this)’s [attribute list](#concept-namednodemap-attribute)’s [size](https://infra.spec.whatwg.org/#list-size), then return null. 

2. 

Otherwise, return [this](https://webidl.spec.whatwg.org/#this)’s [attribute list](#concept-namednodemap-attribute)[index]. 

A [NamedNodeMap](#namednodemap) object’s [supported property names](https://webidl.spec.whatwg.org/#dfn-supported-property-names) are the return value of running these steps: 

1. 

Let names be the [qualified names](#concept-attribute-qualified-name) of the [attributes](#concept-attribute) in this [NamedNodeMap](#namednodemap) object’s [attribute list](#concept-namednodemap-attribute), with duplicates omitted, in order. 

2. 

If this [NamedNodeMap](#namednodemap) object’s [element](#concept-namednodemap-element) is in the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace) and its [node document](#concept-node-document) is an [HTML document](#html-document), then [for each](https://infra.spec.whatwg.org/#list-iterate)name of names: 

  1. 

Let lowercaseName be name, in [ASCII lowercase](https://infra.spec.whatwg.org/#ascii-lowercase). 

  2. 

If lowercaseName is not equal to name, remove name from names. 

3. 

Return names. 

The `getNamedItem(qualifiedName)` method steps are to return the result of [getting an attribute](#concept-element-attributes-get-by-name) given qualifiedName and [element](#concept-namednodemap-element). 

The `getNamedItemNS(namespace, localName)` method steps are to return the result of [getting an attribute](#concept-element-attributes-get-by-namespace) given namespace, localName, and [element](#concept-namednodemap-element). 

The `setNamedItem(attr)` and `setNamedItemNS(attr)` method steps are to return the result of [setting an attribute](#concept-element-attributes-set) given attr and [element](#concept-namednodemap-element). 

The `removeNamedItem(qualifiedName)` method steps are: 

1. 

Let attr be the result of [removing an attribute](#concept-element-attributes-remove-by-name) given qualifiedName and [element](#concept-namednodemap-element). 

2. 

If attr is null, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotFoundError](https://webidl.spec.whatwg.org/#notfounderror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

Return attr. 

The `removeNamedItemNS(namespace, localName)` method steps are: 

1. 

Let attr be the result of [removing an attribute](#concept-element-attributes-remove-by-namespace) given namespace, localName, and [element](#concept-namednodemap-element). 

2. 

If attr is null, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotFoundError](https://webidl.spec.whatwg.org/#notfounderror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

Return attr. 

#### 4.9.2. Interface [Attr](#attr)#interface-attr

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface Attr : Node#node {
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespaceURI#dom-attr-namespaceuri;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? prefix#dom-attr-prefix;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName#dom-attr-localname;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString name#dom-attr-name;
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString value#dom-attr-value;

  readonly attribute Element#element? ownerElement#dom-attr-ownerelement;

  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean specified#dom-attr-specified; // useless; always returns true
};
```

[Attr](#attr)[nodes](#concept-node) are simply known as attributes. They are sometimes referred to as content attributes to avoid confusion with IDL attributes. 

[Attributes](#concept-attribute) have a namespace (null or a non-empty string), namespace prefix (null or a non-empty string), local name (a non-empty string), value (a string), and element (null or an [element](#concept-element)).

If designed today they would just have a name and value. ☹ 

An [attribute](#concept-attribute)’s qualified name is its [local name](#concept-attribute-local-name) if its [namespace prefix](#concept-attribute-namespace-prefix) is null, and its [namespace prefix](#concept-attribute-namespace-prefix), followed by "`:`", followed by its [local name](#concept-attribute-local-name), otherwise. 

User agents could have this as an internal slot as an optimization. 

When an [attribute](#concept-attribute) is created, its [local name](#concept-attribute-local-name) is given. Unless explicitly given when an [attribute](#concept-attribute) is created, its [namespace](#concept-attribute-namespace), [namespace prefix](#concept-attribute-namespace-prefix), and [element](#concept-attribute-element) are set to null, and its [value](#concept-attribute-value) is set to the empty string. 

An `A` attribute is an [attribute](#concept-attribute) whose [local name](#concept-attribute-local-name) is `A` and whose [namespace](#concept-attribute-namespace) and [namespace prefix](#concept-attribute-namespace-prefix) are null. 

The `namespaceURI` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [namespace](#concept-attribute-namespace). 

The `prefix` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [namespace prefix](#concept-attribute-namespace-prefix). 

The `localName` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [local name](#concept-attribute-local-name). 

The `name` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [qualified name](#concept-attribute-qualified-name). 

The `value` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [value](#concept-attribute-value). 

To set an existing attribute value, given an [attribute](#concept-attribute)attribute and string value, run these steps: 

1. 

If attribute’s [element](#concept-attribute-element) is null, then set attribute’s [value](#concept-attribute-value) to value and return. 

2. 

Let element be attribute’s [element](#concept-attribute-element). 

3. 

Let verifiedValue be the result of calling [get trusted type compliant attribute value](https://w3c.github.io/trusted-types/dist/spec/#get-trusted-type-compliant-attribute-value) with attribute’s [local name](#concept-attribute-local-name), attribute’s [namespace](#concept-attribute-namespace), element, and value. [[TRUSTED-TYPES]](#biblio-trusted-types)

4. 

If attribute’s [element](#concept-attribute-element) is null, then set attribute’s [value](#concept-attribute-value) to verifiedValue and return. 

5. 

[Change](#concept-element-attributes-change)attribute to verifiedValue. 

The [value](#dom-attr-value) setter steps are to [set an existing attribute value](#set-an-existing-attribute-value) with [this](https://webidl.spec.whatwg.org/#this) and the given value. 

The `ownerElement` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [element](#concept-attribute-element). 

The `specified` getter steps are to return true. 

### 4.10. Interface [CharacterData](#characterdata)#interface-characterdata

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface CharacterData : Node#node {
  attribute [LegacyNullToEmptyStringhttps://webidl.spec.whatwg.org/#LegacyNullToEmptyString] DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString data#dom-characterdata-data;
  readonly attribute unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long length#dom-characterdata-length;
  DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString substringData#dom-characterdata-substringdata(unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long offset, unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long count);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined appendData#dom-characterdata-appenddata(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString data);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined insertData#dom-characterdata-insertdata(unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long offset, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString data);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined deleteData#dom-characterdata-deletedata(unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long offset, unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long count);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined replaceData#dom-characterdata-replacedata(unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long offset, unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long count, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString data);
};
```

[CharacterData](#characterdata) is an abstract interface. You cannot get a direct instance of it. It is used by [Text](#text), [ProcessingInstruction](#processinginstruction), and [Comment](#comment)[nodes](#concept-node). 

Each [node](#concept-node) inheriting from the [CharacterData](#characterdata) interface has an associated mutable string called data. 

To replace data of a [node](#concept-node)node with an integer offset, integer count, and string data: 

1. 

Let length be node’s [length](#concept-node-length). 

2. 

If offset is greater than length, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[IndexSizeError](https://webidl.spec.whatwg.org/#indexsizeerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

If offset + count is greater than length, then set count to length − offset. 

4. 

[Queue a mutation record](#queue-a-mutation-record) of "`characterData`" for node with null, null, node’s [data](#concept-cd-data), « », « », null, and null. 

5. 

Insert data into node’s [data](#concept-cd-data) after offset[code units](https://infra.spec.whatwg.org/#code-unit). 

6. 

Let deleteOffset be offset + data’s [length](https://infra.spec.whatwg.org/#string-length). 

7. 

Starting from deleteOffset[code units](https://infra.spec.whatwg.org/#code-unit), remove count[code units](https://infra.spec.whatwg.org/#code-unit) from node’s [data](#concept-cd-data). 

8. 

For each [live range](#concept-live-range) whose [start node](#concept-range-start-node) is node and [start offset](#concept-range-start-offset) is greater than offset but less than or equal to offset + count: set its [start offset](#concept-range-start-offset) to offset. 

9. 

For each [live range](#concept-live-range) whose [end node](#concept-range-end-node) is node and [end offset](#concept-range-end-offset) is greater than offset but less than or equal to offset + count: set its [end offset](#concept-range-end-offset) to offset. 

10. 

For each [live range](#concept-live-range) whose [start node](#concept-range-start-node) is node and [start offset](#concept-range-start-offset) is greater than offset + count: increase its [start offset](#concept-range-start-offset) by data’s [length](https://infra.spec.whatwg.org/#string-length) and decrease it by count. 

11. 

For each [live range](#concept-live-range) whose [end node](#concept-range-end-node) is node and [end offset](#concept-range-end-offset) is greater than offset + count: increase its [end offset](#concept-range-end-offset) by data’s [length](https://infra.spec.whatwg.org/#string-length) and decrease it by count. 

12. 

If node’s [parent](#concept-tree-parent) is non-null, then run the [children changed steps](#concept-node-children-changed-ext) for node’s [parent](#concept-tree-parent). 

To substring data of a [node](#concept-node)node with an integer offset and integer count: 

1. 

Let length be node’s [length](#concept-node-length). 

2. 

If offset is greater than length, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[IndexSizeError](https://webidl.spec.whatwg.org/#indexsizeerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

If offset + count is greater than length, then return a string whose value is the [code units](https://infra.spec.whatwg.org/#code-unit) from the offsetth[code unit](https://infra.spec.whatwg.org/#code-unit) to the end of node’s [data](#concept-cd-data). 

4. 

Return a string whose value is the [code units](https://infra.spec.whatwg.org/#code-unit) from the offsetth[code unit](https://infra.spec.whatwg.org/#code-unit) to the offset+countth[code unit](https://infra.spec.whatwg.org/#code-unit) in node’s [data](#concept-cd-data). 

The `data` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [data](#concept-cd-data). Its setter steps are to [replace data](#concept-cd-replace) of [this](https://webidl.spec.whatwg.org/#this) with 0, [this](https://webidl.spec.whatwg.org/#this)’s [length](#concept-node-length), and the given value. 

The `length` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [length](#concept-node-length). 

The `substringData(offset, count)` method steps are to return the result of [substringing data](#concept-cd-substring) of [this](https://webidl.spec.whatwg.org/#this) with offset and count. 

The `appendData(data)` method steps are to [replace data](#concept-cd-replace) of [this](https://webidl.spec.whatwg.org/#this) with [this](https://webidl.spec.whatwg.org/#this)’s [length](#concept-node-length), 0, and data. 

The `insertData(offset, data)` method steps are to [replace data](#concept-cd-replace) of [this](https://webidl.spec.whatwg.org/#this) with offset, 0, and data. 

The `deleteData(offset, count)` method steps are to [replace data](#concept-cd-replace) of [this](https://webidl.spec.whatwg.org/#this) with offset, count, and the empty string. 

The `replaceData(offset, count, data)` method steps are to [replace data](#concept-cd-replace) of [this](https://webidl.spec.whatwg.org/#this) with offset, count, and data. 

### 4.11. Interface [Text](#text)#interface-text

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface Text : CharacterData#characterdata {
  constructor#dom-text-text(optional DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString data = "");

  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] Text#text splitText#dom-text-splittext(unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long offset);
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString wholeText#dom-text-wholetext;
};
```

[Text([data = ""])](#dom-text-text)`text = new`Returns a new [Text](#text)[node](#concept-node) whose [data](#concept-cd-data) is data. [splitText(offset)](#dom-text-splittext)Splits [data](#concept-cd-data) at the given offset and returns the remainder as [Text](#text)[node](#concept-node). [wholeText](#dom-text-wholetext)Returns the combined [data](#concept-cd-data) of all direct [Text](#text)[node](#concept-node)[siblings](#concept-tree-sibling). 

An exclusive [Text](#text) node is a [Text](#text)[node](#concept-node) that is not a [CDATASection](#cdatasection)[node](#concept-node). 

The contiguous [Text](#text) nodes of a [node](#concept-node)node are node, node’s [previous sibling](#concept-tree-previous-sibling)[Text](#text)[node](#concept-node), if any, and its [contiguous Text nodes](#contiguous-text-nodes), and node’s [next sibling](#concept-tree-next-sibling)[Text](#text)[node](#concept-node), if any, and its [contiguous Text nodes](#contiguous-text-nodes), avoiding any duplicates. 

The contiguous exclusive [Text](#text) nodes of a [node](#concept-node)node are node, node’s [previous sibling](#concept-tree-previous-sibling)[exclusive Text node](#exclusive-text-node), if any, and its [contiguous exclusive Text nodes](#contiguous-exclusive-text-nodes), and node’s [next sibling](#concept-tree-next-sibling)[exclusive Text node](#exclusive-text-node), if any, and its [contiguous exclusive Text nodes](#contiguous-exclusive-text-nodes), avoiding any duplicates. 

The child text content of a [node](#concept-node)node is the [concatenation](https://infra.spec.whatwg.org/#string-concatenate) of the [data](#concept-cd-data) of all the [Text](#text)[node](#concept-node)[children](#concept-tree-child) of node, in [tree order](#concept-tree-order). 

The descendant text content of a [node](#concept-node)node is the [concatenation](https://infra.spec.whatwg.org/#string-concatenate) of the [data](#concept-cd-data) of all the [Text](#text)[node](#concept-node)[descendants](#concept-tree-descendant) of node, in [tree order](#concept-tree-order). 

The `new Text(data)` constructor steps are to set [this](https://webidl.spec.whatwg.org/#this)’s [data](#concept-cd-data) to data and [this](https://webidl.spec.whatwg.org/#this)’s [node document](#concept-node-document) to [current global object](https://html.spec.whatwg.org/multipage/webappapis.html#current-global-object)’s [associated Document](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window). 

To split a [Text](#text)[node](#concept-node)node with integer offset: 

1. 

Let length be node’s [length](#concept-node-length). 

2. 

If offset is greater than length, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[IndexSizeError](https://webidl.spec.whatwg.org/#indexsizeerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

Let count be length − offset. 

4. 

Let newData be the result of [substringing data](#concept-cd-substring) of node with offset and count. 

5. 

Let newNode be a new [Text](#text)[node](#concept-node) whose [node document](#concept-node-document) is node’s [node document](#concept-node-document) and [data](#concept-cd-data) is newData. 

6. 

Let parent be node’s [parent](#concept-tree-parent). 

7. 

If parent is non-null: 

  1. 

[Insert](#concept-node-insert)newNode into parent before node’s [next sibling](#concept-tree-next-sibling). 

  2. 

For each [live range](#concept-live-range) whose [start node](#concept-range-start-node) is node and [start offset](#concept-range-start-offset) is greater than offset, set its [start node](#concept-range-start-node) to newNode and decrease its [start offset](#concept-range-start-offset) by offset. 

  3. 

For each [live range](#concept-live-range) whose [end node](#concept-range-end-node) is node and [end offset](#concept-range-end-offset) is greater than offset, set its [end node](#concept-range-end-node) to newNode and decrease its [end offset](#concept-range-end-offset) by offset. 

  4. 

For each [live range](#concept-live-range) whose [start node](#concept-range-start-node) is parent and [start offset](#concept-range-start-offset) is equal to the [index](#concept-tree-index) of node plus 1, increase its [start offset](#concept-range-start-offset) by 1. 

  5. 

For each [live range](#concept-live-range) whose [end node](#concept-range-end-node) is parent and [end offset](#concept-range-end-offset) is equal to the [index](#concept-tree-index) of node plus 1, increase its [end offset](#concept-range-end-offset) by 1. 

8. 

[Replace data](#concept-cd-replace) of node with offset, count, and the empty string. 

9. 

Return newNode. 

The `splitText(offset)` method steps are to [split](#concept-text-split)[this](https://webidl.spec.whatwg.org/#this) with offset offset. 

The `wholeText` getter steps are to return the [concatenation](https://infra.spec.whatwg.org/#string-concatenate) of the [data](#concept-cd-data) of the [contiguous Text nodes](#contiguous-text-nodes) of [this](https://webidl.spec.whatwg.org/#this), in [tree order](#concept-tree-order). 

### 4.12. Interface [CDATASection](#cdatasection)#interface-cdatasection

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface CDATASection : Text#text {
};
```

### 4.13. Interface [ProcessingInstruction](#processinginstruction)#interface-processinginstruction

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface ProcessingInstruction : CharacterData#characterdata {
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString target#dom-processinginstruction-target;
};
```

[ProcessingInstruction](#processinginstruction)[nodes](#concept-node) have an associated target. 

The `target` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [target](#concept-pi-target). 

### 4.14. Interface [Comment](#comment)#interface-comment

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface Comment : CharacterData#characterdata {
  constructor#dom-comment-comment(optional DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString data = "");
};
```

[Comment([data = ""])](#dom-comment-comment)`comment = new`Returns a new [Comment](#comment)[node](#concept-node) whose [data](#concept-cd-data) is data. 

The `new Comment(data)` constructor steps are to set [this](https://webidl.spec.whatwg.org/#this)’s [data](#concept-cd-data) to data and [this](https://webidl.spec.whatwg.org/#this)’s [node document](#concept-node-document) to [current global object](https://html.spec.whatwg.org/multipage/webappapis.html#current-global-object)’s [associated Document](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window). 

## 5. Ranges#ranges

### 5.1. Introduction to "DOM Ranges"#introduction-to-dom-ranges

[StaticRange](#staticrange) and [Range](#range) objects ([ranges](#concept-range)) represent a sequence of content within a [node tree](#concept-node-tree). Each [range](#concept-range) has a [start](#concept-range-start) and an [end](#concept-range-end) which are [boundary points](#concept-range-bp). A [boundary point](#concept-range-bp) is a [tuple](https://infra.spec.whatwg.org/#tuple) consisting of a [node](#boundary-point-node) and an [offset](#concept-range-bp-offset). So in other words, a [range](#concept-range) represents a piece of content within a [node tree](#concept-node-tree) between two [boundary points](#concept-range-bp). 

[Ranges](#concept-range) are frequently used in editing for selecting and copying content. 

- [Element](#element): `p`

  - [Element](#element): `<img src="insanity-wolf" alt="Little-endian BOM; decode as big-endian!">`
  - [Text](#text):  CSS 2.1 syndata is 
  - [Element](#element): `<em>`

    - [Text](#text): awesome

  - [Text](#text): !

In the [node tree](#concept-node-tree) above, a [range](#concept-range) can be used to represent the sequence “syndata is awes”. Assuming p is assigned to the `p`[element](#concept-element), and em to the `em`[element](#concept-element), this would be done as follows: 

```
var range = new Range(),
    firstText = p.childNodes[1],
    secondText = em.firstChild
range.setStart(firstText, 9) // do not forget the leading space
range.setEnd(secondText, 4)
// range now stringifies to the aforementioned quote
```

[Attributes](#concept-attribute) such as `src` and `alt` in the [node tree](#concept-node-tree) above cannot be represented by a [range](#concept-range). [Ranges](#concept-range) are only useful for [nodes](#concept-node). 

[Range](#range) objects, unlike [StaticRange](#staticrange) objects, are affected by mutations to the [node tree](#concept-node-tree). Therefore they are also known as [live ranges](#concept-live-range). Such mutations will not invalidate them and will try to ensure that it still represents the same piece of content. Necessarily, a [live range](#concept-live-range) might itself be modified as part of the mutation to the [node tree](#concept-node-tree) when, e.g., part of the content it represents is mutated. 

See the [insert](#concept-node-insert) and [remove](#concept-node-remove) algorithms, the [normalize()](#dom-node-normalize) method, and the [replace data](#concept-cd-replace) and [split](#concept-text-split) algorithms for details. 

Updating [live ranges](#concept-live-range) in response to [node tree](#concept-node-tree) mutations can be expensive. For every [node tree](#concept-node-tree) change, all affected [Range](#range) objects need to be updated. Even if the application is uninterested in some [live ranges](#concept-live-range), it still has to pay the cost of keeping them up-to-date when a mutation occurs. 

A [StaticRange](#staticrange) object is a lightweight [range](#concept-range) that does not update when the [node tree](#concept-node-tree) mutates. It is therefore not subject to the same maintenance cost as [live ranges](#concept-live-range). 

### 5.2. Boundary points#boundary-points

A boundary point is a [tuple](https://infra.spec.whatwg.org/#tuple) consisting of a node (a [node](#concept-node)) and an offset (a non-negative integer). 

A correct [boundary point](#concept-range-bp)’s [offset](#concept-range-bp-offset) will be between 0 and the [boundary point](#concept-range-bp)’s [node](#boundary-point-node)’s [length](#concept-node-length), inclusive. 

The position of a [boundary point](#concept-range-bp) (nodeA, offsetA) relative to a [boundary point](#concept-range-bp) (nodeB, offsetB) is before, equal, or after, as returned by these steps: 

1. 

Assert: nodeA and nodeB have the same [root](#concept-tree-root). 

2. If nodeA is nodeB, then return [equal](#concept-range-bp-equal) if offsetA is offsetB, [before](#concept-range-bp-before) if offsetA is less than offsetB, and [after](#concept-range-bp-after) if offsetA is greater than offsetB. 
3. 

If nodeA is [following](#concept-tree-following)nodeB, then if the [position](#concept-range-bp-position) of (nodeB, offsetB) relative to (nodeA, offsetA) is [before](#concept-range-bp-before), return [after](#concept-range-bp-after), and if it is [after](#concept-range-bp-after), return [before](#concept-range-bp-before). 

4. 

If nodeA is an [ancestor](#concept-tree-ancestor) of nodeB: 

  1. 

Let child be nodeB. 

  2. 

While child is not a [child](#concept-tree-child) of nodeA, set child to its [parent](#concept-tree-parent). 

  3. 

If child’s [index](#concept-tree-index) is less than offsetA, then return [after](#concept-range-bp-after). 

5. 

Return [before](#concept-range-bp-before). 

### 5.3. Interface [AbstractRange](#abstractrange)#interface-abstractrange

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface AbstractRange {
  readonly attribute Node#node startContainer#dom-range-startcontainer;
  readonly attribute unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long startOffset#dom-range-startoffset;
  readonly attribute Node#node endContainer#dom-range-endcontainer;
  readonly attribute unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long endOffset#dom-range-endoffset;
  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean collapsed#dom-range-collapsed;
};
```

Objects implementing the [AbstractRange](#abstractrange) interface are known as ranges. 

A [range](#concept-range) has two associated [boundary points](#concept-range-bp) — a start and end. 

For convenience, a [range](#concept-range)’s start node is its [start](#concept-range-start)’s [node](#boundary-point-node), its start offset is its [start](#concept-range-start)’s [offset](#concept-range-bp-offset), its end node is its [end](#concept-range-end)’s [node](#boundary-point-node), and its end offset is its [end](#concept-range-end)’s [offset](#concept-range-bp-offset). 

A [range](#concept-range) is collapsed if its [start node](#concept-range-start-node) is its [end node](#concept-range-end-node) and its [start offset](#concept-range-start-offset) is its [end offset](#concept-range-end-offset). 

[startContainer](#dom-range-startcontainer)`node = range .`Returns range’s [start node](#concept-range-start-node). [startOffset](#dom-range-startoffset)`offset = range .`Returns range’s [start offset](#concept-range-start-offset). [endContainer](#dom-range-endcontainer)`node = range .`Returns range’s [end node](#concept-range-end-node). [endOffset](#dom-range-endoffset)`offset = range .`Returns range’s [end offset](#concept-range-end-offset). [collapsed](#dom-range-collapsed)`collapsed = range .`Returns true if range is [collapsed](#range-collapsed); otherwise false. 

The `startContainer` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [start node](#concept-range-start-node). 

The `startOffset` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [start offset](#concept-range-start-offset). 

The `endContainer` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [end node](#concept-range-end-node). 

The `endOffset` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [end offset](#concept-range-end-offset). 

The `collapsed` getter steps are to return true if [this](https://webidl.spec.whatwg.org/#this) is [collapsed](#range-collapsed); otherwise false. 

### 5.4. Interface [StaticRange](#staticrange)#interface-staticrange

```
dictionary StaticRangeInit {
  required Node#node startContainer;
  required unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long startOffset;
  required Node#node endContainer;
  required unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long endOffset;
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface StaticRange : AbstractRange#abstractrange {
  constructor#dom-staticrange-staticrange(StaticRangeInit#dictdef-staticrangeinit init);
};
```

[StaticRange](#dom-staticrange-staticrange)`staticRange = new (init)`

Returns a new [range](#concept-range) object that does not update when the [node tree](#concept-node-tree) mutates. 

The `new StaticRange(init)` constructor steps are: 

1. 

If init["[startContainer](#dom-staticrangeinit-startcontainer)"] or init["[endContainer](#dom-staticrangeinit-endcontainer)"] is a [DocumentType](#documenttype) or [Attr](#attr)[node](#concept-node), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidNodeTypeError](https://webidl.spec.whatwg.org/#invalidnodetypeerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

2. 

Set [this](https://webidl.spec.whatwg.org/#this)’s [start](#concept-range-start) to (init["[startContainer](#dom-staticrangeinit-startcontainer)"], init["[startOffset](#dom-staticrangeinit-startoffset)"]) and [end](#concept-range-end) to (init["[endContainer](#dom-staticrangeinit-endcontainer)"], init["[endOffset](#dom-staticrangeinit-endoffset)"]). 

A [StaticRange](#staticrange) is valid if all of the following are true: 

- 

Its [start](#concept-range-start) and [end](#concept-range-end) are in the same [node tree](#concept-node-tree). 

- 

Its [start offset](#concept-range-start-offset) is between 0 and its [start node](#concept-range-start-node)’s [length](#concept-node-length), inclusive. 

- 

Its [end offset](#concept-range-end-offset) is between 0 and its [end node](#concept-range-end-node)’s [length](#concept-node-length), inclusive. 

- 

Its [start](#concept-range-start) is [before](#concept-range-bp-before) or [equal](#concept-range-bp-equal) to its [end](#concept-range-end). 

### 5.5. Interface [Range](#range)#interface-range

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface Range : AbstractRange#abstractrange {
  constructor#dom-range-range();

  readonly attribute Node#node commonAncestorContainer#dom-range-commonancestorcontainer;

  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined setStart#dom-range-setstart(Node#node node, unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long offset);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined setEnd#dom-range-setend(Node#node node, unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long offset);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined setStartBefore#dom-range-setstartbefore(Node#node node);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined setStartAfter#dom-range-setstartafter(Node#node node);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined setEndBefore#dom-range-setendbefore(Node#node node);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined setEndAfter#dom-range-setendafter(Node#node node);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined collapse#dom-range-collapse(optional booleanhttps://webidl.spec.whatwg.org/#idl-boolean toStart = false);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined selectNode#dom-range-selectnode(Node#node node);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined selectNodeContents#dom-range-selectnodecontents(Node#node node);

  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short START_TO_START = 0;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short START_TO_END = 1;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short END_TO_END = 2;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short END_TO_START = 3;
  shorthttps://webidl.spec.whatwg.org/#idl-short compareBoundaryPoints#dom-range-compareboundarypoints(unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short how, Range#range sourceRange);

  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined deleteContents#dom-range-deletecontents();
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, NewObjecthttps://webidl.spec.whatwg.org/#NewObject] DocumentFragment#documentfragment extractContents#dom-range-extractcontents();
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, NewObjecthttps://webidl.spec.whatwg.org/#NewObject] DocumentFragment#documentfragment cloneContents#dom-range-clonecontents();
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined insertNode#dom-range-insertnode(Node#node node);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined surroundContents#dom-range-surroundcontents(Node#node newParent);

  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] Range#range cloneRange#dom-range-clonerange();
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined detach#dom-range-detach();

  booleanhttps://webidl.spec.whatwg.org/#idl-boolean isPointInRange#dom-range-ispointinrange(Node#node node, unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long offset);
  shorthttps://webidl.spec.whatwg.org/#idl-short comparePoint#dom-range-comparepoint(Node#node node, unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long offset);

  booleanhttps://webidl.spec.whatwg.org/#idl-boolean intersectsNode#dom-range-intersectsnode(Node#node node);

  stringifier#dom-range-stringifier;
};
```

Objects implementing the [Range](#range) interface are known as live ranges. 

Algorithms that modify a [tree](#concept-tree) (in particular the [insert](#concept-node-insert), [remove](#concept-node-remove), [move](#move), [replace data](#concept-cd-replace), and [split](#concept-text-split) algorithms) modify [live ranges](#concept-live-range) associated with that [tree](#concept-tree). 

The root of a [live range](#concept-live-range) is the [root](#concept-tree-root) of its [start node](#concept-range-start-node). 

A [node](#concept-node)node is contained in a [live range](#concept-live-range)range if node’s [root](#concept-tree-root) is range’s [root](#concept-range-root), and (node, 0) is [after](#concept-range-bp-after)range’s [start](#concept-range-start), and (node, node’s [length](#concept-node-length)) is [before](#concept-range-bp-before)range’s [end](#concept-range-end). 

A [node](#concept-node) is partially contained in a [live range](#concept-live-range) if it’s an [inclusive ancestor](#concept-tree-inclusive-ancestor) of the [live range](#concept-live-range)’s [start node](#concept-range-start-node) but not its [end node](#concept-range-end-node), or vice versa. 

Some facts to better understand these definitions: 

- 

The content that one would think of as being within the [live range](#concept-live-range) consists of all [contained](#contained)[nodes](#concept-node), plus possibly some of the contents of the [start node](#concept-range-start-node) and [end node](#concept-range-end-node) if those are [CharacterData](#characterdata)[nodes](#concept-node). 

- 

The [nodes](#concept-node) that are contained in a [live range](#concept-live-range) will generally not be contiguous, because the [parent](#concept-tree-parent) of a [contained](#contained)[node](#concept-node) will not always be [contained](#contained). 

- 

However, the [descendants](#concept-tree-descendant) of a [contained](#contained)[node](#concept-node) are [contained](#contained), and if two [siblings](#concept-tree-sibling) are [contained](#contained), so are any [siblings](#concept-tree-sibling) that lie between them. 

- 

The [start node](#concept-range-start-node) and [end node](#concept-range-end-node) of a [live range](#concept-live-range) are never [contained](#contained) within it. 

- 

The first [contained](#contained)[node](#concept-node) (if there are any) will always be after the [start node](#concept-range-start-node), and the last [contained](#contained)[node](#concept-node) will always be equal to or before the [end node](#concept-range-end-node)’s last [descendant](#concept-tree-descendant). 

- 

There exists a [partially contained](#partially-contained)[node](#concept-node) if and only if the [start node](#concept-range-start-node) and [end node](#concept-range-end-node) are different. 

- 

The [commonAncestorContainer](#dom-range-commonancestorcontainer) attribute value is neither [contained](#contained) nor [partially contained](#partially-contained). 

- 

If the [start node](#concept-range-start-node) is an [ancestor](#concept-tree-ancestor) of the [end node](#concept-range-end-node), the common [inclusive ancestor](#concept-tree-inclusive-ancestor) will be the [start node](#concept-range-start-node). Exactly one of its [children](#concept-tree-child) will be [partially contained](#partially-contained), and a [child](#concept-tree-child) will be [contained](#contained) if and only if it [precedes](#concept-tree-preceding) the [partially contained](#partially-contained)[child](#concept-tree-child). If the [end node](#concept-range-end-node) is an [ancestor](#concept-tree-ancestor) of the [start node](#concept-range-start-node), the opposite holds. 

- 

If the [start node](#concept-range-start-node) is not an [inclusive ancestor](#concept-tree-inclusive-ancestor) of the [end node](#concept-range-end-node), nor vice versa, the common [inclusive ancestor](#concept-tree-inclusive-ancestor) will be distinct from both of them. Exactly two of its [children](#concept-tree-child) will be [partially contained](#partially-contained), and a [child](#concept-tree-child) will be contained if and only if it lies between those two. 

The live range pre-remove steps given a [node](#concept-node)node, are: 

1. 

Let parent be node’s [parent](#concept-tree-parent). 

2. 

[Assert](https://infra.spec.whatwg.org/#assert): parent is non-null. 

3. 

Let index be node’s [index](#concept-tree-index). 

4. 

For each [live range](#concept-live-range) whose [start node](#concept-range-start-node) is an [inclusive descendant](#concept-tree-inclusive-descendant) of node, set its [start](#concept-range-start) to (parent, index). 

5. 

For each [live range](#concept-live-range) whose [end node](#concept-range-end-node) is an [inclusive descendant](#concept-tree-inclusive-descendant) of node, set its [end](#concept-range-end) to (parent, index). 

6. 

For each [live range](#concept-live-range) whose [start node](#concept-range-start-node) is parent and [start offset](#concept-range-start-offset) is greater than index, decrease its [start offset](#concept-range-start-offset) by 1. 

7. 

For each [live range](#concept-live-range) whose [end node](#concept-range-end-node) is parent and [end offset](#concept-range-end-offset) is greater than index, decrease its [end offset](#concept-range-end-offset) by 1. 

[Range()](#dom-range-range)`range = new`Returns a new [live range](#concept-live-range). 

The `new Range()` constructor steps are to set [this](https://webidl.spec.whatwg.org/#this)’s [start](#concept-range-start) and [end](#concept-range-end) to ([current global object](https://html.spec.whatwg.org/multipage/webappapis.html#current-global-object)’s [associated Document](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window), 0). 

container = range . [commonAncestorContainer](#dom-range-commonancestorcontainer)Returns the [node](#concept-node), furthest away from the [document](#concept-document), that is an [ancestor](#concept-tree-ancestor) of both range’s [start node](#concept-range-start-node) and [end node](#concept-range-end-node). 

The `commonAncestorContainer` getter steps are: 

1. 

Let container be [start node](#concept-range-start-node). 

2. 

While container is not an [inclusive ancestor](#concept-tree-inclusive-ancestor) of [end node](#concept-range-end-node): set container to container’s [parent](#concept-tree-parent). 

3. 

Return container. 

To set the start or end of a range to a [boundary point](#concept-range-bp) (node, offset): 

1. 

If node is a [doctype](#concept-doctype), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidNodeTypeError](https://webidl.spec.whatwg.org/#invalidnodetypeerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

2. 

If offset is greater than node’s [length](#concept-node-length), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[IndexSizeError](https://webidl.spec.whatwg.org/#indexsizeerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

Let boundaryPoint be the [boundary point](#concept-range-bp) (node, offset). 

4. If these steps were invoked as "set the start" 

  1. 

If range’s [root](#concept-range-root) is not node’s [root](#concept-tree-root) or boundaryPoint is [after](#concept-range-bp-after)range’s [end](#concept-range-end), then set range’s [end](#concept-range-end) to boundaryPoint. 

  2. 

Set range’s [start](#concept-range-start) to boundaryPoint. 

If these steps were invoked as "set the end" 

  1. 

If range’s [root](#concept-range-root) is not node’s [root](#concept-tree-root) or boundaryPoint is [before](#concept-range-bp-before)range’s [start](#concept-range-start), then set range’s [start](#concept-range-start) to boundaryPoint. 

  2. 

Set range’s [end](#concept-range-end) to boundaryPoint. 

The `setStart(node, offset)` method steps are to [set the start](#concept-range-bp-set) of [this](https://webidl.spec.whatwg.org/#this) to [boundary point](#concept-range-bp) (node, offset). 

The `setEnd(node, offset)` method steps are to [set the end](#concept-range-bp-set) of [this](https://webidl.spec.whatwg.org/#this) to [boundary point](#concept-range-bp) (node, offset). 

The `setStartBefore(node)` method steps are: 

1. 

Let parent be node’s [parent](#concept-tree-parent). 

2. 

If parent is null, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidNodeTypeError](https://webidl.spec.whatwg.org/#invalidnodetypeerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

[Set the start](#concept-range-bp-set) of [this](https://webidl.spec.whatwg.org/#this) to [boundary point](#concept-range-bp) (parent, node’s [index](#concept-tree-index)). 

The `setStartAfter(node)` method steps are: 

1. 

Let parent be node’s [parent](#concept-tree-parent). 

2. 

If parent is null, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidNodeTypeError](https://webidl.spec.whatwg.org/#invalidnodetypeerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

[Set the start](#concept-range-bp-set) of [this](https://webidl.spec.whatwg.org/#this) to [boundary point](#concept-range-bp) (parent, node’s [index](#concept-tree-index) plus 1). 

The `setEndBefore(node)` method steps are: 

1. 

Let parent be node’s [parent](#concept-tree-parent). 

2. 

If parent is null, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidNodeTypeError](https://webidl.spec.whatwg.org/#invalidnodetypeerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

[Set the end](#concept-range-bp-set) of [this](https://webidl.spec.whatwg.org/#this) to [boundary point](#concept-range-bp) (parent, node’s [index](#concept-tree-index)). 

The `setEndAfter(node)` method steps are: 

1. 

Let parent be node’s [parent](#concept-tree-parent). 

2. 

If parent is null, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidNodeTypeError](https://webidl.spec.whatwg.org/#invalidnodetypeerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

[Set the end](#concept-range-bp-set) of [this](https://webidl.spec.whatwg.org/#this) to [boundary point](#concept-range-bp) (parent, node’s [index](#concept-tree-index) plus 1). 

The `collapse(toStart)` method steps are to, if toStart is true, set [end](#concept-range-end) to [start](#concept-range-start); otherwise set [start](#concept-range-start) to [end](#concept-range-end). 

To select a [node](#concept-node)node within a [range](#concept-range)range: 

1. 

Let parent be node’s [parent](#concept-tree-parent). 

2. 

If parent is null, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidNodeTypeError](https://webidl.spec.whatwg.org/#invalidnodetypeerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

Let index be node’s [index](#concept-tree-index). 

4. 

Set range’s [start](#concept-range-start) to [boundary point](#concept-range-bp) (parent, index). 

5. 

Set range’s [end](#concept-range-end) to [boundary point](#concept-range-bp) (parent, index plus 1). 

The `selectNode(node)` method steps are to [select](#concept-range-select)node within [this](https://webidl.spec.whatwg.org/#this). 

The `selectNodeContents(node)` method steps are: 

1. 

If node is a [doctype](#concept-doctype), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidNodeTypeError](https://webidl.spec.whatwg.org/#invalidnodetypeerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

2. 

Let length be the [length](#concept-node-length) of node. 

3. 

Set [start](#concept-range-start) to the [boundary point](#concept-range-bp) (node, 0). 

4. 

Set [end](#concept-range-end) to the [boundary point](#concept-range-bp) (node, length). 

The `compareBoundaryPoints(how, sourceRange)` method steps are: 

1. 

If how is not one of 

  - [START_TO_START](#dom-range-start_to_start), 
  - [START_TO_END](#dom-range-start_to_end), 
  - [END_TO_END](#dom-range-end_to_end), and 
  - [END_TO_START](#dom-range-end_to_start), 

then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[NotSupportedError](https://webidl.spec.whatwg.org/#notsupportederror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

2. 

If [this](https://webidl.spec.whatwg.org/#this)’s [root](#concept-range-root) is not sourceRange’s [root](#concept-range-root), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[WrongDocumentError](https://webidl.spec.whatwg.org/#wrongdocumenterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

Let thisPoint and sourcePoint be null. 

4. 

Switch on how: 

[START_TO_START](#dom-range-start_to_start): 

Set thisPoint to [this](https://webidl.spec.whatwg.org/#this)’s [start](#concept-range-start) and sourcePoint to sourceRange’s [start](#concept-range-start). 

[START_TO_END](#dom-range-start_to_end): 

Set thisPoint to [this](https://webidl.spec.whatwg.org/#this)’s [end](#concept-range-end) and sourcePoint to sourceRange’s [start](#concept-range-start). 

[END_TO_END](#dom-range-end_to_end): 

Set thisPoint to [this](https://webidl.spec.whatwg.org/#this)’s [end](#concept-range-end) and sourcePoint to sourceRange’s [end](#concept-range-end). 

[END_TO_START](#dom-range-end_to_start): 

Set thisPoint to [this](https://webidl.spec.whatwg.org/#this)’s [start](#concept-range-start) and sourcePoint to sourceRange’s [end](#concept-range-end). 

5. 

Switch on the [position](#concept-range-bp-position) of thisPoint relative to sourcePoint: 

[before](#concept-range-bp-before)Return −1. [equal](#concept-range-bp-equal)Return 0. [after](#concept-range-bp-after)Return 1. 

The `deleteContents()` method steps are: 

1. 

If [this](https://webidl.spec.whatwg.org/#this) is [collapsed](#range-collapsed), then return. 

2. 

Let originalStartNode, originalStartOffset, originalEndNode, and originalEndOffset be [this](https://webidl.spec.whatwg.org/#this)’s [start node](#concept-range-start-node), [start offset](#concept-range-start-offset), [end node](#concept-range-end-node), and [end offset](#concept-range-end-offset), respectively. 

3. 

If originalStartNode is originalEndNode and it is a [CharacterData](#characterdata)[node](#concept-node): 

  1. 

[Replace data](#concept-cd-replace) of originalStartNode with originalStartOffset, originalEndOffset − originalStartOffset, and the empty string. 

  2. 

Return. 

4. 

Let nodesToRemove be a list of all the [nodes](#concept-node) that are [contained](#contained) in [this](https://webidl.spec.whatwg.org/#this), in [tree order](#concept-tree-order), omitting any [node](#concept-node) whose [parent](#concept-tree-parent) is also [contained](#contained) in [this](https://webidl.spec.whatwg.org/#this). 

5. 

Let newNode and newOffset be null. 

6. 

If originalStartNode is an [inclusive ancestor](#concept-tree-inclusive-ancestor) of originalEndNode, then set newNode to originalStartNode and newOffset to originalStartOffset. 

7. 

Otherwise: 

  1. 

Let referenceNode be originalStartNode. 

  2. 

While referenceNode’s [parent](#concept-tree-parent) is non-null and is not an [inclusive ancestor](#concept-tree-inclusive-ancestor) of originalEndNode: set referenceNode to its [parent](#concept-tree-parent). 

  3. 

Set newNode to referenceNode’s [parent](#concept-tree-parent) and newOffset to referenceNode’s [index](#concept-tree-index) + 1. 

If referenceNode’s [parent](#concept-tree-parent) were null, it would be the [root](#concept-range-root) of [this](https://webidl.spec.whatwg.org/#this). And then it would be an [inclusive ancestor](#concept-tree-inclusive-ancestor) of originalEndNode and we could not reach this point. 

8. 

If originalStartNode is a [CharacterData](#characterdata)[node](#concept-node), then [replace data](#concept-cd-replace) of originalStartNode with originalStartOffset, originalStartNode’s [length](#concept-node-length) − originalStartOffset, and the empty string. 

9. 

For each node of nodesToRemove, in [tree order](#concept-tree-order): [remove](#concept-node-remove)node. 

10. 

If originalEndNode is a [CharacterData](#characterdata)[node](#concept-node), then [replace data](#concept-cd-replace) of originalEndNode with 0, originalEndOffset, and the empty string. 

11. 

Set [start](#concept-range-start) and [end](#concept-range-end) to (newNode, newOffset). 

To extract a [live range](#concept-live-range)range: 

1. 

Let fragment be a new [DocumentFragment](#documentfragment)[node](#concept-node) whose [node document](#concept-node-document) is range’s [start node](#concept-range-start-node)’s [node document](#concept-node-document). 

2. 

If range is [collapsed](#range-collapsed), then return fragment. 

3. 

Let originalStartNode, originalStartOffset, originalEndNode, and originalEndOffset be range’s [start node](#concept-range-start-node), [start offset](#concept-range-start-offset), [end node](#concept-range-end-node), and [end offset](#concept-range-end-offset), respectively. 

4. 

If originalStartNode is originalEndNode and it is a [CharacterData](#characterdata)[node](#concept-node): 

  1. 

Let clone be a [clone](#concept-node-clone) of originalStartNode. 

  2. 

Set clone’s [data](#concept-cd-data) to the result of [substringing data](#concept-cd-substring) of originalStartNode with originalStartOffset and originalEndOffset − originalStartOffset. 

  3. 

[Append](#concept-node-append)clone to fragment. 

  4. 

[Replace data](#concept-cd-replace) of originalStartNode with originalStartOffset, originalEndOffset − originalStartOffset, and the empty string. 

  5. Return fragment. 

5. 

Let commonAncestor be originalStartNode. 

6. 

While commonAncestor is not an [inclusive ancestor](#concept-tree-inclusive-ancestor) of originalEndNode: set commonAncestor to its own [parent](#concept-tree-parent). 

7. 

Let firstPartiallyContainedChild be null. 

8. If originalStartNode is not an [inclusive ancestor](#concept-tree-inclusive-ancestor) of originalEndNode, then set firstPartiallyContainedChild to the first [child](#concept-tree-child) of commonAncestor that is [partially contained](#partially-contained) in range. 
9. 

Let lastPartiallyContainedChild be null. 

10. 

If originalEndNode is not an [inclusive ancestor](#concept-tree-inclusive-ancestor) of originalStartNode, then set lastPartiallyContainedChild to the last [child](#concept-tree-child) of commonAncestor that is [partially contained](#partially-contained) in range. 

These variable assignments do actually always make sense. For instance, if originalStartNode is not an [inclusive ancestor](#concept-tree-inclusive-ancestor) of originalEndNode, originalStartNode is itself [partially contained](#partially-contained) in range, and so are all its [ancestors](#concept-tree-ancestor) up until a [child](#concept-tree-child) of commonAncestor. commonAncestor cannot be originalStartNode, because it has to be an [inclusive ancestor](#concept-tree-inclusive-ancestor) of originalEndNode. The other case is similar. Also, notice that the two [children](#concept-tree-child) will never be equal if both are defined. 

11. 

Let containedChildren be a list of all [children](#concept-tree-child) of commonAncestor that are [contained](#contained) in range, in [tree order](#concept-tree-order). 

12. 

If any member of containedChildren is a [doctype](#concept-doctype), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

We do not have to worry about the first or last partially contained node, because a [doctype](#concept-doctype) can never be partially contained. It cannot be a boundary point of a range, and it cannot be the ancestor of anything. 

13. 

Let newNode and newOffset be null. 

14. 

If originalStartNode is an [inclusive ancestor](#concept-tree-inclusive-ancestor) of originalEndNode, then set newNode to originalStartNode and newOffset to originalStartOffset. 

15. 

Otherwise: 

  1. 

Let referenceNode be originalStartNode. 

  2. 

While referenceNode’s [parent](#concept-tree-parent) is non-null and is not an [inclusive ancestor](#concept-tree-inclusive-ancestor) of originalEndNode: set referenceNode to its [parent](#concept-tree-parent). 

  3. 

Set newNode to the [parent](#concept-tree-parent) of referenceNode, and newOffset to referenceNode’s [index](#concept-tree-index) + 1. 

If referenceNode’s [parent](#concept-tree-parent) is null, it would be the [root](#concept-range-root) of range. And then it would be an [inclusive ancestor](#concept-tree-inclusive-ancestor) of originalEndNode and we could not reach this point. 

16. 

If firstPartiallyContainedChild is a [CharacterData](#characterdata)[node](#concept-node): 

In this case, firstPartiallyContainedChild is originalStartNode. 

  1. 

Let clone be a [clone](#concept-node-clone) of originalStartNode. 

  2. 

Set the [data](#concept-cd-data) of clone to the result of [substringing data](#concept-cd-substring) of originalStartNode with originalStartOffset and originalStartNode’s [length](#concept-node-length) − originalStartOffset. 

  3. 

[Append](#concept-node-append)clone to fragment. 

  4. 

[Replace data](#concept-cd-replace) of originalStartNode with originalStartOffset, originalStartNode’s [length](#concept-node-length) − originalStartOffset, and the empty string. 

17. 

Otherwise, if firstPartiallyContainedChild is non-null: 

  1. 

Let clone be a [clone](#concept-node-clone) of firstPartiallyContainedChild. 

  2. 

[Append](#concept-node-append)clone to fragment. 

  3. 

Let subrange be a new [live range](#concept-live-range) whose [start](#concept-range-start) is (originalStartNode, originalStartOffset) and whose [end](#concept-range-end) is (firstPartiallyContainedChild, firstPartiallyContainedChild’s [length](#concept-node-length)). 

  4. 

Let subfragment be the result of [extracting](#concept-range-extract)subrange. 

  5. [Append](#concept-node-append)subfragment to clone. 

18. 

For each contained child of containedChildren: [append](#concept-node-append)contained child to fragment. 

19. 

If lastPartiallyContainedChild is a [CharacterData](#characterdata)[node](#concept-node): 

In this case, lastPartiallyContainedChild is originalEndNode. 

  1. 

Let clone be a [clone](#concept-node-clone) of originalEndNode. 

  2. 

Set clone’s [data](#concept-cd-data) to the result of [substringing data](#concept-cd-substring) of originalEndNode with 0 and originalEndOffset. 

  3. 

[Append](#concept-node-append)clone to fragment. 

  4. 

[Replace data](#concept-cd-replace) of originalEndNode with 0, originalEndOffset, and the empty string. 

20. 

Otherwise, if lastPartiallyContainedChild is non-null: 

  1. 

Let clone be a [clone](#concept-node-clone) of lastPartiallyContainedChild. 

  2. 

[Append](#concept-node-append)clone to fragment. 

  3. 

Let subrange be a new [live range](#concept-live-range) whose [start](#concept-range-start) is (lastPartiallyContainedChild, 0) and whose [end](#concept-range-end) is (originalEndNode, originalEndOffset). 

  4. 

Let subfragment be the result of [extracting](#concept-range-extract)subrange. 

  5. 

[Append](#concept-node-append)subfragment to clone. 

21. 

Set range’s [start](#concept-range-start) and [end](#concept-range-end) to (newNode, newOffset). 

22. 

Return fragment. 

The `extractContents()` method steps are to return the result of [extracting](#concept-range-extract)[this](https://webidl.spec.whatwg.org/#this). 

To clone the contents of a [live range](#concept-live-range)range: 

1. 

Let fragment be a new [DocumentFragment](#documentfragment)[node](#concept-node) whose [node document](#concept-node-document) is range’s [start node](#concept-range-start-node)’s [node document](#concept-node-document). 

2. 

If range is [collapsed](#range-collapsed), then return fragment. 

3. 

Let originalStartNode, originalStartOffset, originalEndNode, and originalEndOffset be range’s [start node](#concept-range-start-node), [start offset](#concept-range-start-offset), [end node](#concept-range-end-node), and [end offset](#concept-range-end-offset), respectively. 

4. 

If originalStartNode is originalEndNode and it is a [CharacterData](#characterdata)[node](#concept-node): 

  1. 

Let clone be a [clone](#concept-node-clone) of originalStartNode. 

  2. 

Set clone’s [data](#concept-cd-data) to the result of [substringing data](#concept-cd-substring) of originalStartNode with originalStartOffset and originalEndOffset − originalStartOffset. 

  3. 

[Append](#concept-node-append)clone to fragment. 

  4. 

Return fragment. 

5. 

Let commonAncestor be originalStartNode. 

6. 

While commonAncestor is not an [inclusive ancestor](#concept-tree-inclusive-ancestor) of originalEndNode: set commonAncestor to its own [parent](#concept-tree-parent). 

7. 

Let firstPartiallyContainedChild be null. 

8. 

If originalStartNode is not an [inclusive ancestor](#concept-tree-inclusive-ancestor) of originalEndNode, then set firstPartiallyContainedChild to the first [child](#concept-tree-child) of commonAncestor that is [partially contained](#partially-contained) in range. 

9. 

Let lastPartiallyContainedChild be null. 

10. 

If originalEndNode is not an [inclusive ancestor](#concept-tree-inclusive-ancestor) of originalStartNode, then set lastPartiallyContainedChild to the last [child](#concept-tree-child) of commonAncestor that is [partially contained](#partially-contained) in range. 

These variable assignments do actually always make sense. For instance, if originalStartNode is not an [inclusive ancestor](#concept-tree-inclusive-ancestor) of originalEndNode, originalStartNode is itself [partially contained](#partially-contained) in range, and so are all its [ancestors](#concept-tree-ancestor) up until a [child](#concept-tree-child) of commonAncestor. commonAncestor cannot be originalStartNode, because it has to be an [inclusive ancestor](#concept-tree-inclusive-ancestor) of originalEndNode. The other case is similar. Also, notice that the two [children](#concept-tree-child) will never be equal if both are defined. 

11. 

Let containedChildren be a list of all [children](#concept-tree-child) of commonAncestor that are [contained](#contained) in range, in [tree order](#concept-tree-order). 

12. 

If any member of containedChildren is a [doctype](#concept-doctype), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

We do not have to worry about the first or last partially contained node, because a [doctype](#concept-doctype) can never be partially contained. It cannot be a boundary point of a range, and it cannot be the ancestor of anything. 

13. 

If firstPartiallyContainedChild is a [CharacterData](#characterdata)[node](#concept-node): 

In this case, firstPartiallyContainedChild is originalStartNode. 

  1. 

Let clone be a [clone](#concept-node-clone) of originalStartNode. 

  2. 

Set the [data](#concept-cd-data) of clone to the result of [substringing data](#concept-cd-substring) of originalStartNode with originalStartOffset and originalStartNode’s [length](#concept-node-length) − originalStartOffset. 

  3. 

[Append](#concept-node-append)clone to fragment. 

14. 

Otherwise, if firstPartiallyContainedChild is non-null: 

  1. 

Let clone be a [clone](#concept-node-clone) of firstPartiallyContainedChild. 

  2. 

[Append](#concept-node-append)clone to fragment. 

  3. 

Let subrange be a new [live range](#concept-live-range) whose [start](#concept-range-start) is (originalStartNode, originalStartOffset) and whose [end](#concept-range-end) is (firstPartiallyContainedChild, firstPartiallyContainedChild’s [length](#concept-node-length)). 

  4. 

Let subfragment be the result of [cloning the contents](#concept-range-clone) of subrange. 

  5. 

[Append](#concept-node-append)subfragment to clone. 

15. 

For each contained child of containedChildren: 

  1. 

Let clone be a [clone](#concept-node-clone) of contained child with [subtree](#clone-a-node-subtree) set to true. 

  2. 

[Append](#concept-node-append)clone to fragment. 

16. 

If lastPartiallyContainedChild is a [CharacterData](#characterdata)[node](#concept-node): 

In this case, lastPartiallyContainedChild is originalEndNode. 

  1. 

Let clone be a [clone](#concept-node-clone) of originalEndNode. 

  2. 

Set clone’s [data](#concept-cd-data) to the result of [substringing data](#concept-cd-substring) of originalEndNode with 0 and originalEndOffset. 

  3. 

[Append](#concept-node-append)clone to fragment. 

17. 

Otherwise, if lastPartiallyContainedChild is non-null: 

  1. 

Let clone be a [clone](#concept-node-clone) of lastPartiallyContainedChild. 

  2. 

[Append](#concept-node-append)clone to fragment. 

  3. 

Let subrange be a new [live range](#concept-live-range) whose [start](#concept-range-start) is (lastPartiallyContainedChild, 0) and whose [end](#concept-range-end) is (originalEndNode, originalEndOffset). 

  4. 

Let subfragment be the result of [cloning the contents](#concept-range-clone) of subrange. 

  5. 

[Append](#concept-node-append)subfragment to clone. 

18. 

Return fragment. 

The `cloneContents()` method steps are to return the result of [cloning the contents](#concept-range-clone) of [this](https://webidl.spec.whatwg.org/#this). 

To insert a [node](#concept-node)node into a [live range](#concept-live-range)range: 

1. 

If range’s [start node](#concept-range-start-node) is a [ProcessingInstruction](#processinginstruction) or [Comment](#comment)[node](#concept-node), is a [Text](#text)[node](#concept-node) whose [parent](#concept-tree-parent) is null, or is node, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[HierarchyRequestError](https://webidl.spec.whatwg.org/#hierarchyrequesterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

2. 

Let referenceNode be null. 

3. 

If range’s [start node](#concept-range-start-node) is a [Text](#text)[node](#concept-node), then set referenceNode to that [Text](#text)[node](#concept-node). 

4. 

Otherwise, set referenceNode to the [child](#concept-tree-child) of range’s [start node](#concept-range-start-node) whose [index](#concept-tree-index) is range’s [start offset](#concept-range-start-offset) if there is such a [child](#concept-tree-child); otherwise null. 

5. 

Let parent be range’s [start node](#concept-range-start-node) if referenceNode is null; otherwise referenceNode’s [parent](#concept-tree-parent). 

6. 

[Ensure pre-insert validity](#concept-node-ensure-pre-insertion-validity) of node into parent before referenceNode. 

7. 

If range’s [start node](#concept-range-start-node) is a [Text](#text)[node](#concept-node), then set referenceNode to the result of [splitting](#concept-text-split) it with offset range’s [start offset](#concept-range-start-offset). 

8. 

If node is referenceNode, then set referenceNode to its [next sibling](#concept-tree-next-sibling). 

9. 

If node’s [parent](#concept-tree-parent) is non-null, then [remove](#concept-node-remove)node. 

10. 

Let newOffset be parent’s [length](#concept-node-length) if referenceNode is null; otherwise referenceNode’s [index](#concept-tree-index). 

11. 

Increase newOffset by node’s [length](#concept-node-length) if node is a [DocumentFragment](#documentfragment)[node](#concept-node); otherwise 1. 

12. 

[Pre-insert](#concept-node-pre-insert)node into parent before referenceNode. 

13. 

If range is [collapsed](#range-collapsed), then set range’s [end](#concept-range-end) to (parent, newOffset). 

The `insertNode(node)` method steps are to [insert](#concept-range-insert)node into [this](https://webidl.spec.whatwg.org/#this). 

The `surroundContents(newParent)` method steps are: 

1. 

If a non-[Text](#text)[node](#concept-node) is [partially contained](#partially-contained) in [this](https://webidl.spec.whatwg.org/#this), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidStateError](https://webidl.spec.whatwg.org/#invalidstateerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

2. 

If newParent is a [Document](#document), [DocumentType](#documenttype), or [DocumentFragment](#documentfragment)[node](#concept-node), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidNodeTypeError](https://webidl.spec.whatwg.org/#invalidnodetypeerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

For historical reasons [CharacterData](#characterdata)[nodes](#concept-node) are not checked here and end up throwing later on as a side effect. 

3. 

Let fragment be the result of [extracting](#concept-range-extract)[this](https://webidl.spec.whatwg.org/#this). 

4. 

If newParent has [children](#concept-tree-child), then [replace all](#concept-node-replace-all) with null within newParent. 

5. 

[Insert](#concept-range-insert)newParent into [this](https://webidl.spec.whatwg.org/#this). 

6. 

[Append](#concept-node-append)fragment to newParent. 

7. 

[Select](#concept-range-select)newParent within [this](https://webidl.spec.whatwg.org/#this). 

The `cloneRange()` method steps are to return a new [live range](#concept-live-range) with the same [start](#concept-range-start) and [end](#concept-range-end) as [this](https://webidl.spec.whatwg.org/#this). 

The `detach()` method steps are to do nothing. Its functionality (disabling a [Range](#range) object) was removed, but the method itself is preserved for compatibility.

position = range . [comparePoint(node, offset)](#dom-range-comparepoint)Returns −1 if the point is before the range, 0 if the point is in the range, and 1 if the point is after the range. intersects = range . [intersectsNode(node)](#dom-range-intersectsnode)Returns whether range intersects node. 

The `isPointInRange(node, offset)` method steps are: 

1. 

If node’s [root](#concept-tree-root) is not [this](https://webidl.spec.whatwg.org/#this)’s [root](#concept-range-root), then return false. 

2. 

If node is a [doctype](#concept-doctype), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidNodeTypeError](https://webidl.spec.whatwg.org/#invalidnodetypeerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

If offset is greater than node’s [length](#concept-node-length), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[IndexSizeError](https://webidl.spec.whatwg.org/#indexsizeerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

4. 

If (node, offset) is [before](#concept-range-bp-before)[start](#concept-range-start) or [after](#concept-range-bp-after)[end](#concept-range-end), then return false. 

5. 

Return true. 

The `comparePoint(node, offset)` method steps are: 

1. 

If node’s [root](#concept-tree-root) is not [this](https://webidl.spec.whatwg.org/#this)’s [root](#concept-range-root), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[WrongDocumentError](https://webidl.spec.whatwg.org/#wrongdocumenterror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

2. 

If node is a [doctype](#concept-doctype), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidNodeTypeError](https://webidl.spec.whatwg.org/#invalidnodetypeerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

If offset is greater than node’s [length](#concept-node-length), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[IndexSizeError](https://webidl.spec.whatwg.org/#indexsizeerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

4. 

If (node, offset) is [before](#concept-range-bp-before)[start](#concept-range-start), then return −1. 

5. 

If (node, offset) is [after](#concept-range-bp-after)[end](#concept-range-end), then return 1. 

6. 

Return 0. 

The `intersectsNode(node)` method steps are: 

1. 

If node’s [root](#concept-tree-root) is not [this](https://webidl.spec.whatwg.org/#this)’s [root](#concept-range-root), then return false. 

2. 

Let parent be node’s [parent](#concept-tree-parent). 

3. 

If parent is null, then return true. 

4. 

Let offset be node’s [index](#concept-tree-index). 

5. 

If (parent, offset) is [before](#concept-range-bp-before)[end](#concept-range-end) and (parent, offset + 1) is [after](#concept-range-bp-after)[start](#concept-range-start), then return true. 

6. 

Return false. 

The stringification behavior must run these steps: 

1. 

Let string be the empty string. 

2. 

If [this](https://webidl.spec.whatwg.org/#this)’s [start node](#concept-range-start-node) is [this](https://webidl.spec.whatwg.org/#this)’s [end node](#concept-range-end-node) and it is a [Text](#text)[node](#concept-node), then return the substring of that [Text](#text)[node](#concept-node)’s [data](#concept-cd-data) beginning at [this](https://webidl.spec.whatwg.org/#this)’s [start offset](#concept-range-start-offset) and ending at [this](https://webidl.spec.whatwg.org/#this)’s [end offset](#concept-range-end-offset). 

3. 

If [this](https://webidl.spec.whatwg.org/#this)’s [start node](#concept-range-start-node) is a [Text](#text)[node](#concept-node), then append the substring of that [node](#concept-node)’s [data](#concept-cd-data) from [this](https://webidl.spec.whatwg.org/#this)’s [start offset](#concept-range-start-offset) until the end to string. 

4. 

Append the [concatenation](https://infra.spec.whatwg.org/#string-concatenate) of the [data](#concept-cd-data) of all [Text](#text)[nodes](#concept-node) that are [contained](#contained) in [this](https://webidl.spec.whatwg.org/#this), in [tree order](#concept-tree-order), to string. 

5. 

If [this](https://webidl.spec.whatwg.org/#this)’s [end node](#concept-range-end-node) is a [Text](#text)[node](#concept-node), then append the substring of that [node](#concept-node)’s [data](#concept-cd-data) from its start until [this](https://webidl.spec.whatwg.org/#this)’s [end offset](#concept-range-end-offset) to string. 

6. 

Return string. 

The [createContextualFragment()](https://w3c.github.io/DOM-Parsing/#dom-range-createcontextualfragment), [getClientRects()](https://drafts.csswg.org/cssom-view-1/#dom-range-getclientrects), and [getBoundingClientRect()](https://drafts.csswg.org/cssom-view-1/#dom-range-getboundingclientrect) methods are defined in other specifications. [[DOM-Parsing]](#biblio-dom-parsing)[[CSSOM-VIEW]](#biblio-cssom-view)

## 6. Traversal#traversal

[NodeIterator](#nodeiterator) and [TreeWalker](#treewalker) objects can be used to filter and traverse [node](#concept-node)[trees](#concept-tree). 

Each [NodeIterator](#nodeiterator) and [TreeWalker](#treewalker) object has an associated boolean is active to avoid recursive invocations. It is initially false. 

Each [NodeIterator](#nodeiterator) and [TreeWalker](#treewalker) object also has an associated root (a [node](#concept-node)), a whatToShow (a bitmask), and a filter (a callback). 

To filter a [node](#concept-node)node within a [NodeIterator](#nodeiterator) or [TreeWalker](#treewalker) object traverser: 

1. 

If traverser’s [is active](#concept-traversal-active) is true, then throw an "[InvalidStateError](https://webidl.spec.whatwg.org/#invalidstateerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

2. 

Let n be node’s [nodeType](#dom-node-nodetype) attribute value − 1. 

3. 

If the nth bit (where 0 is the least significant bit) of traverser’s [whatToShow](#concept-traversal-whattoshow) is not set, then return [FILTER_SKIP](#dom-nodefilter-filter_skip). 

4. 

If traverser’s [filter](#concept-traversal-filter) is null, then return [FILTER_ACCEPT](#dom-nodefilter-filter_accept). 

5. 

Set traverser’s [is active](#concept-traversal-active) to true. 

6. 

Let result be the return value of [call a user object’s operation](https://webidl.spec.whatwg.org/#call-a-user-objects-operation) with traverser’s [filter](#concept-traversal-filter), "`acceptNode`", and « node ». If this throws an exception, then set traverser’s [is active](#concept-traversal-active) to false and rethrow the exception. 

7. 

Set traverser’s [is active](#concept-traversal-active) to false. 

8. 

Return result. 

### 6.1. Interface [NodeIterator](#nodeiterator)#interface-nodeiterator

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface NodeIterator {
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute Node#node root#dom-nodeiterator-root;
  readonly attribute Node#node referenceNode#dom-nodeiterator-referencenode;
  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean pointerBeforeReferenceNode#dom-nodeiterator-pointerbeforereferencenode;
  readonly attribute unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long whatToShow#dom-nodeiterator-whattoshow;
  readonly attribute NodeFilter#callbackdef-nodefilter? filter#dom-nodeiterator-filter;

  Node#node? nextNode#dom-nodeiterator-nextnode();
  Node#node? previousNode#dom-nodeiterator-previousnode();

  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined detach#dom-nodeiterator-detach();
};
```

[NodeIterator](#nodeiterator) objects can be created using the [createNodeIterator()](#dom-document-createnodeiterator) method on [Document](#document) objects. 

Each [NodeIterator](#nodeiterator) object has an associated iterator collection, which is a [collection](#concept-collection) rooted at the [NodeIterator](#nodeiterator) object’s [root](#concept-traversal-root), whose filter matches any [node](#concept-node). 

Each [NodeIterator](#nodeiterator) object also has an associated reference (a [node](#concept-node)) and pointer before reference (a boolean). 

As mentioned earlier, [NodeIterator](#nodeiterator) objects have an associated [is active](#concept-traversal-active), [root](#concept-traversal-root), [whatToShow](#concept-traversal-whattoshow), and [filter](#concept-traversal-filter) as well. 

The `NodeIterator` pre-remove steps given a [NodeIterator](#nodeiterator) object nodeIterator and [node](#concept-node)toBeRemovedNode, are: 

1. 

If toBeRemovedNode is not an [inclusive ancestor](#concept-tree-inclusive-ancestor) of nodeIterator’s [reference](#nodeiterator-reference), or toBeRemovedNode is nodeIterator’s [root](#concept-traversal-root), then return. 

2. 

If nodeIterator’s [pointer before reference](#nodeiterator-pointer-before-reference) is true: 

  1. 

Let next be toBeRemovedNode’s first [following](#concept-tree-following)[node](#concept-node) that is an [inclusive descendant](#concept-tree-inclusive-descendant) of nodeIterator’s [root](#concept-traversal-root) and is not an [inclusive descendant](#concept-tree-inclusive-descendant) of toBeRemovedNode, if there is such a [node](#concept-node); otherwise null. 

  2. 

If next is non-null, then set nodeIterator’s [reference](#nodeiterator-reference) to next and return. 

  3. 

Set nodeIterator’s [pointer before reference](#nodeiterator-pointer-before-reference) to false. 

3. 

Set nodeIterator’s [reference](#nodeiterator-reference) to toBeRemovedNode’s [parent](#concept-tree-parent), if toBeRemovedNode’s [previous sibling](#concept-tree-previous-sibling) is null; otherwise to the [inclusive descendant](#concept-tree-inclusive-descendant) of toBeRemovedNode’s [previous sibling](#concept-tree-previous-sibling) that appears last in [tree order](#concept-tree-order). 

The `root` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [root](#concept-traversal-root). 

The `referenceNode` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [reference](#nodeiterator-reference). 

The `pointerBeforeReferenceNode` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [pointer before reference](#nodeiterator-pointer-before-reference). 

The `whatToShow` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [whatToShow](#concept-traversal-whattoshow). 

The `filter` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [filter](#concept-traversal-filter). 

To traverse, given a [NodeIterator](#nodeiterator) object iterator and "`next`" or "`previous`" type: 

1. 

Let node be iterator’s [reference](#nodeiterator-reference). 

2. 

Let beforeNode be iterator’s [pointer before reference](#nodeiterator-pointer-before-reference). 

3. 

While true: 

  1. 

If type is `next`": 

    1. 

If beforeNode is false, then set node to the first [node](#concept-node)[following](#concept-tree-following)node in iterator’s [iterator collection](#iterator-collection). If there is no such [node](#concept-node), then return null. 

    2. 

If beforeNode is true, then set it to false. 

  2. 

Otherwise: 

    1. 

If beforeNode is true, then set node to the first [node](#concept-node)[preceding](#concept-tree-preceding)node in iterator’s [iterator collection](#iterator-collection). If there is no such [node](#concept-node), then return null. 

    2. 

If beforeNode is false, then set it to true. 

  3. 

Let result be the result of [filtering](#concept-node-filter)node within iterator. 

  4. 

If result is [FILTER_ACCEPT](#dom-nodefilter-filter_accept), then [break](https://infra.spec.whatwg.org/#iteration-break). 

4. 

Set iterator’s [reference](#nodeiterator-reference) to node. 

5. 

Set iterator’s [pointer before reference](#nodeiterator-pointer-before-reference) to beforeNode. 

6. 

Return node. 

The `nextNode()` method steps are to return the result of [traversing](#concept-nodeiterator-traverse) with [this](https://webidl.spec.whatwg.org/#this) and "`next`". 

The `previousNode()` method steps are to return the result of [traversing](#concept-nodeiterator-traverse) with [this](https://webidl.spec.whatwg.org/#this) and "`previous`". 

The `detach()` method steps are to do nothing. Its functionality (disabling a [NodeIterator](#nodeiterator) object) was removed, but the method itself is preserved for compatibility.

### 6.2. Interface [TreeWalker](#treewalker)#interface-treewalker

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface TreeWalker {
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute Node#node root#dom-treewalker-root;
  readonly attribute unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long whatToShow#dom-treewalker-whattoshow;
  readonly attribute NodeFilter#callbackdef-nodefilter? filter#dom-treewalker-filter;
           attribute Node#node currentNode#dom-treewalker-currentnode;

  Node#node? parentNode#dom-treewalker-parentnode();
  Node#node? firstChild#dom-treewalker-firstchild();
  Node#node? lastChild#dom-treewalker-lastchild();
  Node#node? previousSibling#dom-treewalker-previoussibling();
  Node#node? nextSibling#dom-treewalker-nextsibling();
  Node#node? previousNode#dom-treewalker-previousnode();
  Node#node? nextNode#dom-treewalker-nextnode();
};
```

[TreeWalker](#treewalker) objects can be created using the [createTreeWalker()](#dom-document-createtreewalker) method on [Document](#document) objects. 

Each [TreeWalker](#treewalker) object has an associated current (a [node](#concept-node)). 

As mentioned earlier [TreeWalker](#treewalker) objects have an associated [root](#concept-traversal-root), [whatToShow](#concept-traversal-whattoshow), and [filter](#concept-traversal-filter) as well. 

The `root` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [root](#concept-traversal-root). 

The `whatToShow` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [whatToShow](#concept-traversal-whattoshow). 

The `filter` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [filter](#concept-traversal-filter). 

The `currentNode` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [current](#treewalker-current). 

The [currentNode](#dom-treewalker-currentnode) setter steps are to set [this](https://webidl.spec.whatwg.org/#this)’s [current](#treewalker-current) to the given value. 

The `parentNode()` method steps are: 

1. 

Let node be [this](https://webidl.spec.whatwg.org/#this)’s [current](#treewalker-current). 

2. 

While node is non-null and is not [this](https://webidl.spec.whatwg.org/#this)’s [root](#concept-traversal-root): 

  1. 

Set node to node’s [parent](#concept-tree-parent). 

  2. 

If node is non-null and [filtering](#concept-node-filter)node within [this](https://webidl.spec.whatwg.org/#this) returns [FILTER_ACCEPT](#dom-nodefilter-filter_accept), then set [this](https://webidl.spec.whatwg.org/#this)’s [current](#treewalker-current) to node and return node. 

3. 

Return null. 

To traverse children, given a [TreeWalker](#treewalker) object walker and "`first`" or "`last`" type: 

1. 

Let node be walker’s [current](#treewalker-current). 

2. 

Set node to node’s [first child](#concept-tree-first-child) if type is "`first`"; otherwise to node’s [last child](#concept-tree-last-child). 

3. 

While node is non-null: 

  1. 

Let result be the result of [filtering](#concept-node-filter)node within walker. 

  2. 

If result is [FILTER_ACCEPT](#dom-nodefilter-filter_accept), then set walker’s [current](#treewalker-current) to node and return node. 

  3. 

If result is [FILTER_SKIP](#dom-nodefilter-filter_skip): 

    1. 

Let child be node’s [first child](#concept-tree-first-child) if type is "`first`"; otherwise node’s [last child](#concept-tree-last-child). 

    2. 

If child is non-null, then set node to child and [continue](https://infra.spec.whatwg.org/#iteration-continue). 

  4. 

While node is non-null: 

    1. 

Let sibling be node’s [next sibling](#concept-tree-next-sibling) if type is "`first`"; otherwise node’s [previous sibling](#concept-tree-previous-sibling). 

    2. 

If sibling is non-null, then set node to sibling and [break](https://infra.spec.whatwg.org/#iteration-break). 

    3. 

Let parent be node’s [parent](#concept-tree-parent). 

    4. 

If parent is null, walker’s [root](#concept-traversal-root), or walker’s [current](#treewalker-current), then return null. 

    5. 

Set node to parent. 

4. 

Return null. 

The `firstChild()` method steps are to [traverse children](#concept-traverse-children) with [this](https://webidl.spec.whatwg.org/#this) and "`first`". 

The `lastChild()` method steps are to [traverse children](#concept-traverse-children) with [this](https://webidl.spec.whatwg.org/#this) and "`last`". 

To traverse siblings, given a [TreeWalker](#treewalker) object walker and "`next`" or "`previous`" type: 

1. 

Let node be walker’s [current](#treewalker-current). 

2. 

If node is [root](#concept-traversal-root), then return null. 

3. 

While true: 

  1. 

Let sibling be node’s [next sibling](#concept-tree-next-sibling) if type is "`next`"; otherwise node’s [previous sibling](#concept-tree-previous-sibling). 

  2. 

While sibling is non-null: 

    1. 

Set node to sibling. 

    2. 

Let result be the result of [filtering](#concept-node-filter)node within walker. 

    3. 

If result is [FILTER_ACCEPT](#dom-nodefilter-filter_accept), then set walker’s [current](#treewalker-current) to node and return node. 

    4. 

Set sibling to node’s [first child](#concept-tree-first-child) if type is "`next`"; otherwise to node’s [last child](#concept-tree-last-child). 

    5. 

If result is [FILTER_REJECT](#dom-nodefilter-filter_reject) or sibling is null, then set sibling to node’s [next sibling](#concept-tree-next-sibling) if type is "`next`"; otherwise to node’s [previous sibling](#concept-tree-previous-sibling). 

  3. 

Set node to node’s [parent](#concept-tree-parent). 

  4. 

If node is null or walker’s [root](#concept-traversal-root), then return null. 

  5. 

If the return value of [filtering](#concept-node-filter)node within walker is [FILTER_ACCEPT](#dom-nodefilter-filter_accept), then return null. 

The `nextSibling()` method steps are to [traverse siblings](#concept-traverse-siblings) with [this](https://webidl.spec.whatwg.org/#this) and "`next`". 

The `previousSibling()` method steps are to [traverse siblings](#concept-traverse-siblings) with [this](https://webidl.spec.whatwg.org/#this) and "`previous`". 

The `previousNode()` method steps are: 

1. 

Let node be [this](https://webidl.spec.whatwg.org/#this)’s [current](#treewalker-current). 

2. 

While node is not [this](https://webidl.spec.whatwg.org/#this)’s [root](#concept-traversal-root): 

  1. 

Let sibling be node’s [previous sibling](#concept-tree-previous-sibling). 

  2. 

While sibling is non-null: 

    1. 

Set node to sibling. 

    2. 

Let result be the result of [filtering](#concept-node-filter)node within [this](https://webidl.spec.whatwg.org/#this). 

    3. 

While result is not [FILTER_REJECT](#dom-nodefilter-filter_reject) and node has a [child](#concept-tree-child): 

      1. 

Set node to node’s [last child](#concept-tree-last-child). 

      2. 

Set result to the result of [filtering](#concept-node-filter)node within [this](https://webidl.spec.whatwg.org/#this). 

    4. 

If result is [FILTER_ACCEPT](#dom-nodefilter-filter_accept), then set [this](https://webidl.spec.whatwg.org/#this)’s [current](#treewalker-current) to node and return node. 

    5. 

Set sibling to node’s [previous sibling](#concept-tree-previous-sibling). 

  3. 

If node is [this](https://webidl.spec.whatwg.org/#this)’s [root](#concept-traversal-root) or node’s [parent](#concept-tree-parent) is null, then return null. 

  4. 

Set node to node’s [parent](#concept-tree-parent). 

  5. 

If the return value of [filtering](#concept-node-filter)node within [this](https://webidl.spec.whatwg.org/#this) is [FILTER_ACCEPT](#dom-nodefilter-filter_accept), then set [this](https://webidl.spec.whatwg.org/#this)’s [current](#treewalker-current) to node and return node. 

3. 

Return null. 

The `nextNode()` method steps are: 

1. 

Let node be [this](https://webidl.spec.whatwg.org/#this)’s [current](#treewalker-current). 

2. 

Let result be [FILTER_ACCEPT](#dom-nodefilter-filter_accept). 

3. 

While true: 

  1. 

While result is not [FILTER_REJECT](#dom-nodefilter-filter_reject) and node has a [child](#concept-tree-child): 

    1. 

Set node to its [first child](#concept-tree-first-child). 

    2. 

Set result to the result of [filtering](#concept-node-filter)node within [this](https://webidl.spec.whatwg.org/#this). 

    3. 

If result is [FILTER_ACCEPT](#dom-nodefilter-filter_accept), then set [this](https://webidl.spec.whatwg.org/#this)’s [current](#treewalker-current) to node and return node. 

  2. 

Let sibling be null. 

  3. 

Let temporary be node. 

  4. 

While temporary is non-null: 

    1. 

If temporary is [this](https://webidl.spec.whatwg.org/#this)’s [root](#concept-traversal-root), then return null. 

    2. 

Set sibling to temporary’s [next sibling](#concept-tree-next-sibling). 

    3. 

If sibling is non-null, then set node to sibling and [break](https://infra.spec.whatwg.org/#iteration-break). 

    4. 

Set temporary to temporary’s [parent](#concept-tree-parent). 

  5. 

Set result to the result of [filtering](#concept-node-filter)node within [this](https://webidl.spec.whatwg.org/#this). 

  6. 

If result is [FILTER_ACCEPT](#dom-nodefilter-filter_accept), then set [this](https://webidl.spec.whatwg.org/#this)’s [current](#treewalker-current) to node and return node. 

### 6.3. Interface [NodeFilter](#callbackdef-nodefilter)#interface-nodefilter

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
callback interface NodeFilter {
  // Constants for acceptNode()
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short FILTER_ACCEPT#dom-nodefilter-filter_accept = 1;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short FILTER_REJECT#dom-nodefilter-filter_reject = 2;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short FILTER_SKIP#dom-nodefilter-filter_skip = 3;

  // Constants for whatToShow
  const unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long SHOW_ALL#dom-nodefilter-show_all = 0xFFFFFFFF;
  const unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long SHOW_ELEMENT#dom-nodefilter-show_element = 0x1;
  const unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long SHOW_ATTRIBUTE#dom-nodefilter-show_attribute = 0x2;
  const unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long SHOW_TEXT#dom-nodefilter-show_text = 0x4;
  const unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long SHOW_CDATA_SECTION#dom-nodefilter-show_cdata_section = 0x8;
  const unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long SHOW_ENTITY_REFERENCE = 0x10; // legacy
  const unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long SHOW_ENTITY = 0x20; // legacy
  const unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long SHOW_PROCESSING_INSTRUCTION#dom-nodefilter-show_processing_instruction = 0x40;
  const unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long SHOW_COMMENT#dom-nodefilter-show_comment = 0x80;
  const unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long SHOW_DOCUMENT#dom-nodefilter-show_document = 0x100;
  const unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long SHOW_DOCUMENT_TYPE#dom-nodefilter-show_document_type = 0x200;
  const unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long SHOW_DOCUMENT_FRAGMENT#dom-nodefilter-show_document_fragment = 0x400;
  const unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long SHOW_NOTATION = 0x800; // legacy

  unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short acceptNode(Node#node node);
};
```

[NodeFilter](#callbackdef-nodefilter) objects can be used as [filter](#concept-traversal-filter) for [NodeIterator](#nodeiterator) and [TreeWalker](#treewalker) objects and also provide constants for their [whatToShow](#concept-traversal-whattoshow) bitmask. A [NodeFilter](#callbackdef-nodefilter) object is typically implemented as a JavaScript function. 

These constants can be used as [filter](#concept-traversal-filter) return value: 

- `FILTER_ACCEPT` (1); 
- `FILTER_REJECT` (2); 
- `FILTER_SKIP` (3). 

These constants can be used for [whatToShow](#concept-traversal-whattoshow): 

- `SHOW_ALL` (4294967295, FFFFFFFF in hexadecimal); 
- `SHOW_ELEMENT` (1); 
- `SHOW_ATTRIBUTE` (2); 
- `SHOW_TEXT` (4); 
- `SHOW_CDATA_SECTION` (8); 
- `SHOW_PROCESSING_INSTRUCTION` (64, 40 in hexadecimal); 
- `SHOW_COMMENT` (128, 80 in hexadecimal); 
- `SHOW_DOCUMENT` (256, 100 in hexadecimal); 
- `SHOW_DOCUMENT_TYPE` (512, 200 in hexadecimal); 
- `SHOW_DOCUMENT_FRAGMENT` (1024, 400 in hexadecimal). 

## 7. Sets#sets

Yes, the name [DOMTokenList](#domtokenlist) is an unfortunate legacy mishap. 

### 7.1. Interface [DOMTokenList](#domtokenlist)#interface-domtokenlist

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface DOMTokenList {
  readonly attribute unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long length#dom-domtokenlist-length;
  getter DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? item#dom-domtokenlist-item(unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long index);
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean contains#dom-domtokenlist-contains(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString token);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined add#dom-domtokenlist-add(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString... tokens);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined remove#dom-domtokenlist-remove(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString... tokens);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] booleanhttps://webidl.spec.whatwg.org/#idl-boolean toggle#dom-domtokenlist-toggle(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString token, optional booleanhttps://webidl.spec.whatwg.org/#idl-boolean force);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] booleanhttps://webidl.spec.whatwg.org/#idl-boolean replace#dom-domtokenlist-replace(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString token, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString newToken);
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean supports#dom-domtokenlist-supports(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString token);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] stringifier attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString value#dom-domtokenlist-value;
  iterable<DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString>;
};
```

A [DOMTokenList](#domtokenlist) object has an associated token set (a [set](https://infra.spec.whatwg.org/#ordered-set)), which is initially empty. 

A [DOMTokenList](#domtokenlist) object also has an associated element (an [element](#concept-element)) and an attribute name (an [attribute](#concept-attribute)’s [local name](#concept-attribute-local-name)). 

[Specifications](#other-applicable-specifications) may define supported tokens for a [DOMTokenList](#domtokenlist)’s [element](#domtokenlist-element) and [attribute name](#domtokenlist-attribute-name).

A [DOMTokenList](#domtokenlist) object set’s validation steps for a given token are: 

1. 

If set’s [element](#domtokenlist-element) and [attribute name](#domtokenlist-attribute-name) does not define [supported tokens](#concept-supported-tokens), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a `TypeError`. 

2. 

Let lowercaseToken be token, in [ASCII lowercase](https://infra.spec.whatwg.org/#ascii-lowercase). 

3. 

If lowercaseToken is present in the [supported tokens](#concept-supported-tokens) of set’s [element](#domtokenlist-element) and [attribute name](#domtokenlist-attribute-name), then return true. 

4. 

Return false. 

A [DOMTokenList](#domtokenlist) object set’s update steps are: 

1. 

If [get an attribute by namespace and local name](#concept-element-attributes-get-by-namespace) given null, set’s [attribute name](#domtokenlist-attribute-name), and set’s [element](#domtokenlist-element) returns null and set’s [token set](#concept-dtl-tokens) is empty, then return. 

2. 

[Set an attribute value](#concept-element-attributes-set-value) given set’s [element](#domtokenlist-element), set’s [attribute name](#domtokenlist-attribute-name), and the result of running the [ordered set serializer](#concept-ordered-set-serializer) for set’s [token set](#concept-dtl-tokens). 

A [DOMTokenList](#domtokenlist) object set’s serialize steps are to return the result of running [get an attribute value](#concept-element-attributes-get-value) given set’s [element](#domtokenlist-element) and set’s [attribute name](#domtokenlist-attribute-name). 

A [DOMTokenList](#domtokenlist) object set has these [attribute change steps](#concept-element-attributes-change-ext) for set’s [element](#domtokenlist-element): 

1. 

If localName is set’s [attribute name](#domtokenlist-attribute-name), namespace is null, and value is null, then [empty](https://infra.spec.whatwg.org/#list-empty)[token set](#concept-dtl-tokens). 

2. 

Otherwise, if localName is set’s [attribute name](#domtokenlist-attribute-name) and namespace is null, then set set’s [token set](#concept-dtl-tokens) to value, [parsed](#concept-ordered-set-parser). 

When a [DOMTokenList](#domtokenlist) object set is created: 

1. 

Let element be set’s [element](#domtokenlist-element). 

2. 

Let attributeName be set’s [attribute name](#domtokenlist-attribute-name). 

3. 

Let value be the result of [getting an attribute value](#concept-element-attributes-get-value) given element and attributeName. 

4. 

Run the [attribute change steps](#concept-element-attributes-change-ext) for element, attributeName, value, value, and null. 

[length](#dom-domtokenlist-length)

Returns the number of tokens. 

[item(index)](#dom-domtokenlist-item)`tokenlist[index]`

Returns the token with index index. 

[contains(token)](#dom-domtokenlist-contains)

Returns true if token is present; otherwise false. 

[add(tokens…)](#dom-domtokenlist-add)`tokenlist .`

Adds all arguments passed, except those already present. 

Throws a "[SyntaxError](https://webidl.spec.whatwg.org/#syntaxerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException) if one of the arguments is the empty string. 

Throws an "[InvalidCharacterError](https://webidl.spec.whatwg.org/#invalidcharactererror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException) if one of the arguments contains any [ASCII whitespace](https://infra.spec.whatwg.org/#ascii-whitespace). 

[remove(tokens…)](#dom-domtokenlist-remove)`tokenlist .`

Removes arguments passed, if they are present. 

Throws a "[SyntaxError](https://webidl.spec.whatwg.org/#syntaxerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException) if one of the arguments is the empty string. 

Throws an "[InvalidCharacterError](https://webidl.spec.whatwg.org/#invalidcharactererror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException) if one of the arguments contains any [ASCII whitespace](https://infra.spec.whatwg.org/#ascii-whitespace). 

[toggle(token [, force])](#dom-domtokenlist-toggle)`tokenlist .`

If force is not given, "toggles" token, removing it if it’s present and adding it if it’s not present. If force is true, adds token (same as [add()](#dom-domtokenlist-add)). If force is false, removes token (same as [remove()](#dom-domtokenlist-remove)). 

Returns true if token is now present; otherwise false. 

Throws a "[SyntaxError](https://webidl.spec.whatwg.org/#syntaxerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException) if token is empty. 

Throws an "[InvalidCharacterError](https://webidl.spec.whatwg.org/#invalidcharactererror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException) if token contains any spaces. 

[replace(token, newToken)](#dom-domtokenlist-replace)`tokenlist .`

Replaces token with newToken. 

Returns true if token was replaced with newToken; otherwise false. 

Throws a "[SyntaxError](https://webidl.spec.whatwg.org/#syntaxerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException) if one of the arguments is the empty string. 

Throws an "[InvalidCharacterError](https://webidl.spec.whatwg.org/#invalidcharactererror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException) if one of the arguments contains any [ASCII whitespace](https://infra.spec.whatwg.org/#ascii-whitespace). 

[supports(token)](#dom-domtokenlist-supports)`tokenlist .`

Returns true if token is in the associated attribute’s supported tokens. Returns false otherwise. 

Throws a `TypeError` if the associated attribute has no supported tokens defined. 

[value](#dom-domtokenlist-value)

Returns the associated set as string. 

Can be set, to change the associated attribute. 

The `length` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [token set](#concept-dtl-tokens)’s [size](https://infra.spec.whatwg.org/#list-size). 

The object’s [supported property indices](https://webidl.spec.whatwg.org/#dfn-supported-property-indices) are the numbers in the range zero to object’s [token set](#concept-dtl-tokens)’s [size](https://infra.spec.whatwg.org/#list-size) − 1, unless [token set](#concept-dtl-tokens)[is empty](https://infra.spec.whatwg.org/#list-is-empty), in which case there are no [supported property indices](https://webidl.spec.whatwg.org/#dfn-supported-property-indices). 

The `item(index)` method steps are: 

1. 

If index is equal to or greater than [this](https://webidl.spec.whatwg.org/#this)’s [token set](#concept-dtl-tokens)’s [size](https://infra.spec.whatwg.org/#list-size), then return null. 

2. 

Return [this](https://webidl.spec.whatwg.org/#this)’s [token set](#concept-dtl-tokens)[index]. 

The `contains(token)` method steps are to return true if [this](https://webidl.spec.whatwg.org/#this)’s [token set](#concept-dtl-tokens)[token] [exists](https://infra.spec.whatwg.org/#list-contain); otherwise false. 

The `add(tokens…)` method steps are: 

1. 

[For each](https://infra.spec.whatwg.org/#list-iterate)token of tokens: 

  1. 

If token is the empty string, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[SyntaxError](https://webidl.spec.whatwg.org/#syntaxerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

  2. 

If token contains any [ASCII whitespace](https://infra.spec.whatwg.org/#ascii-whitespace), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidCharacterError](https://webidl.spec.whatwg.org/#invalidcharactererror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

2. 

[For each](https://infra.spec.whatwg.org/#list-iterate)token of tokens: [append](https://infra.spec.whatwg.org/#set-append)token to [this](https://webidl.spec.whatwg.org/#this)’s [token set](#concept-dtl-tokens). 

3. 

Run the [update steps](#concept-dtl-update). 

The `remove(tokens…)` method steps are: 

1. 

[For each](https://infra.spec.whatwg.org/#list-iterate)token of tokens: 

  1. 

If token is the empty string, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[SyntaxError](https://webidl.spec.whatwg.org/#syntaxerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

  2. 

If token contains any [ASCII whitespace](https://infra.spec.whatwg.org/#ascii-whitespace), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidCharacterError](https://webidl.spec.whatwg.org/#invalidcharactererror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

2. 

For each token of tokens: [remove](https://infra.spec.whatwg.org/#list-remove)token from [this](https://webidl.spec.whatwg.org/#this)’s [token set](#concept-dtl-tokens). 

3. 

Run the [update steps](#concept-dtl-update). 

The `toggle(token, force)` method steps are: 

1. 

If token is the empty string, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[SyntaxError](https://webidl.spec.whatwg.org/#syntaxerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

2. 

If token contains any [ASCII whitespace](https://infra.spec.whatwg.org/#ascii-whitespace), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidCharacterError](https://webidl.spec.whatwg.org/#invalidcharactererror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

If [this](https://webidl.spec.whatwg.org/#this)’s [token set](#concept-dtl-tokens)[token] [exists](https://infra.spec.whatwg.org/#list-contain): 

  1. 

If force is either not given or is false, then [remove](https://infra.spec.whatwg.org/#list-remove)token from [this](https://webidl.spec.whatwg.org/#this)’s [token set](#concept-dtl-tokens), run the [update steps](#concept-dtl-update) and return false. 

  2. 

Return true. 

4. 

Otherwise, if force not given or is true, [append](https://infra.spec.whatwg.org/#set-append)token to [this](https://webidl.spec.whatwg.org/#this)’s [token set](#concept-dtl-tokens), run the [update steps](#concept-dtl-update), and return true. 

5. 

Return false. 

The [update steps](#concept-dtl-update) are not always run for [toggle()](#dom-domtokenlist-toggle) for web compatibility. 

The `replace(token, newToken)` method steps are: 

1. 

If either token or newToken is the empty string, then [throw](https://webidl.spec.whatwg.org/#dfn-throw) a "[SyntaxError](https://webidl.spec.whatwg.org/#syntaxerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

2. 

If either token or newToken contains any [ASCII whitespace](https://infra.spec.whatwg.org/#ascii-whitespace), then [throw](https://webidl.spec.whatwg.org/#dfn-throw) an "[InvalidCharacterError](https://webidl.spec.whatwg.org/#invalidcharactererror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException). 

3. 

If [this](https://webidl.spec.whatwg.org/#this)’s [token set](#concept-dtl-tokens) does not [contain](https://infra.spec.whatwg.org/#list-contain)token, then return false.

4. 

[Replace](https://infra.spec.whatwg.org/#set-replace)token in [this](https://webidl.spec.whatwg.org/#this)’s [token set](#concept-dtl-tokens) with newToken. 

5. 

Run the [update steps](#concept-dtl-update). 

6. 

Return true. 

The [update steps](#concept-dtl-update) are not always run for [replace()](#dom-domtokenlist-replace) for web compatibility. 

The `supports(token)` method steps are: 

1. 

Let result be the return value of [validation steps](#concept-domtokenlist-validation) called with token. 

2. 

Return result. 

The `value` getter steps are to return the result of running [this](https://webidl.spec.whatwg.org/#this)’s [serialize steps](#concept-dtl-serialize). 

The [value](#dom-domtokenlist-value) setter steps are to [set an attribute value](#concept-element-attributes-set-value) for [this](https://webidl.spec.whatwg.org/#this)’s [element](#domtokenlist-element) using [this](https://webidl.spec.whatwg.org/#this)’s [attribute name](#domtokenlist-attribute-name) and the given value. 

## 8. XPath#xpath

DOM Level 3 XPath defined an API for evaluating XPath 1.0 expressions. These APIs are widely implemented, but have not been maintained. The interface definitions are maintained here so that they can be updated when Web IDL changes. Complete definitions of these APIs remain necessary and such work is tracked and can be contributed to in [whatwg/dom#67](https://github.com/whatwg/dom/issues/67). [[DOM-Level-3-XPath]](#biblio-dom-level-3-xpath)[[XPath]](#biblio-xpath)[[WEBIDL]](#biblio-webidl)

### 8.1. Interface [XPathResult](#xpathresult)#interface-xpathresult

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface XPathResult {
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short ANY_TYPE = 0;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short NUMBER_TYPE = 1;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short STRING_TYPE = 2;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short BOOLEAN_TYPE = 3;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short UNORDERED_NODE_ITERATOR_TYPE = 4;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short ORDERED_NODE_ITERATOR_TYPE = 5;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short UNORDERED_NODE_SNAPSHOT_TYPE = 6;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short ORDERED_NODE_SNAPSHOT_TYPE = 7;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short ANY_UNORDERED_NODE_TYPE = 8;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short FIRST_ORDERED_NODE_TYPE = 9;

  readonly attribute unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short resultType;
  readonly attribute unrestricted doublehttps://webidl.spec.whatwg.org/#idl-unrestricted-double numberValue;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString stringValue;
  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean booleanValue;
  readonly attribute Node#node? singleNodeValue;
  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean invalidIteratorState;
  readonly attribute unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long snapshotLength;

  Node#node? iterateNext();
  Node#node? snapshotItem(unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long index);
};
```

### 8.2. Interface [XPathExpression](#xpathexpression)#interface-xpathexpression

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface XPathExpression {
  // XPathResult.ANY_TYPE = 0
  XPathResult#xpathresult evaluate(Node#node contextNode, optional unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short type = 0, optional XPathResult#xpathresult? result = null);
};
```

### 8.3. Mixin [XPathEvaluatorBase](#xpathevaluatorbase)#mixin-xpathevaluatorbase

```
callback interface XPathNSResolver {
  DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? lookupNamespaceURI(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? prefix);
};

interface mixin XPathEvaluatorBase {
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] XPathExpression#xpathexpression createExpression(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString expression, optional XPathNSResolver#callbackdef-xpathnsresolver? resolver = null);
  Node#node createNSResolver#dom-xpathevaluatorbase-creatensresolver(Node#node nodeResolver); // legacy
  // XPathResult.ANY_TYPE = 0
  XPathResult#xpathresult evaluate(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString expression, Node#node contextNode, optional XPathNSResolver#callbackdef-xpathnsresolver? resolver = null, optional unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short type = 0, optional XPathResult#xpathresult? result = null);
};
Document#document includes XPathEvaluatorBase#xpathevaluatorbase;
```

The `createNSResolver(nodeResolver)` method steps are to return nodeResolver. 

This method exists only for historical reasons. 

### 8.4. Interface [XPathEvaluator](#xpathevaluator)#interface-xpathevaluator

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface XPathEvaluator {
  constructor();
};

XPathEvaluator#xpathevaluator includes XPathEvaluatorBase#xpathevaluatorbase;
```

For historical reasons you can both construct [XPathEvaluator](#xpathevaluator) and access the same methods on [Document](#document). 

## 9. XSLT#xslt

XSL Transformations (XSLT) is a language for transforming XML documents into other XML documents. The APIs defined in this section have been widely implemented, and are maintained here so that they can be updated when Web IDL changes. Complete definitions of these APIs remain necessary and such work is tracked and can be contributed to in [whatwg/dom#181](https://github.com/whatwg/dom/issues/181). [[XSLT]](#biblio-xslt)

### 9.1. Interface [XSLTProcessor](#xsltprocessor)#interface-xsltprocessor

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface XSLTProcessor {
  constructor();
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined importStylesheet(Node#node style);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] DocumentFragment#documentfragment transformToFragment(Node#node source, Document#document output);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Document#document transformToDocument(Node#node source);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined setParameter([LegacyNullToEmptyStringhttps://webidl.spec.whatwg.org/#LegacyNullToEmptyString] DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString namespaceURI, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName, anyhttps://webidl.spec.whatwg.org/#idl-any value);
  anyhttps://webidl.spec.whatwg.org/#idl-any getParameter([LegacyNullToEmptyStringhttps://webidl.spec.whatwg.org/#LegacyNullToEmptyString] DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString namespaceURI, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined removeParameter([LegacyNullToEmptyStringhttps://webidl.spec.whatwg.org/#LegacyNullToEmptyString] DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString namespaceURI, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined clearParameters();
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined reset();
};
```

## 10. Security and privacy considerations#security-and-privacy

There are no known security or privacy considerations for this standard. 

## 11. Historical#historical

This standard used to contain several interfaces and interface members that have been removed. 

These interfaces have been removed: 

- `DOMConfiguration`
- `DOMError`
- `DOMErrorHandler`
- `DOMImplementationList`
- `DOMImplementationSource`
- `DOMLocator`
- `DOMObject`
- `DOMUserData`
- `Entity`
- `EntityReference`
- `MutationEvent`
- `MutationNameEvent`
- `NameList`
- `Notation`
- `RangeException`
- `TypeInfo`
- `UserDataHandler`

And these interface members have been removed: 

[Attr](#attr)

- `schemaTypeInfo`
- `isId`

[Document](#document)

- `createEntityReference()`
- `xmlEncoding`
- `xmlStandalone`
- `xmlVersion`
- `strictErrorChecking`
- `domConfig`
- `normalizeDocument()`
- `renameNode()`

[DocumentType](#documenttype)

- `entities`
- `notations`
- `internalSubset`

[DOMImplementation](#domimplementation)

- `getFeature()`

[Element](#element)

- `schemaTypeInfo`
- `setIdAttribute()`
- `setIdAttributeNS()`
- `setIdAttributeNode()`

[Node](#node)

- `isSupported`
- `getFeature()`
- `getUserData()`
- `setUserData()`

[NodeIterator](#nodeiterator)

- `expandEntityReferences`

[Text](#text)

- `isElementContentWhitespace`
- `replaceWholeText()`

[TreeWalker](#treewalker)

- `expandEntityReferences`

## Acknowledgments#acks

There have been a lot of people that have helped make DOM more interoperable over the years and thereby furthered the goals of this standard. Likewise many people have helped making this standard what it is today. 

With that, many thanks to Adam Klein, Adrian Bateman, Ahmid snuggs, Alex Komoroske, Alex Russell, Alexey Shvayka, Andreas Kling, Andreu Botella, Anthony Ramine, Arkadiusz Michalski, Arnaud Le Hors, Arun Ranganathan, Benjamin Gruenbaum, Björn Höhrmann, Boris Zbarsky, Brandon Payton, Brandon Slade, Brandon Wallace, Brian Kardell, C. Scott Ananian, Cameron McCormack, Chris Dumez, Chris Paris, Chris Rebert, Cyrille Tuzi, Dan Burzo, Daniel Clark, Daniel Glazman, Darien Maillet Valentine, Darin Fisher, David Baron, David Bruant, David Flanagan, David Håsäther, David Hyatt, Deepak Sherveghar, Dethe Elza, Dimitri Glazkov, Domenic Denicola, Dominic Cooney, Dominique Hazaël-Massieux, Don Jordan, Doug Schepers, Edgar Chen, Elisée Maurer, Elliott Sprehn, Emilio Cobos Álvarez, Eric Bidelman, Erik Arvidsson, François Daoust, François Remy, Gary Kacmarcik, Gavin Nicol, Giorgio Liscio, Glen Huang, Glenn Adams, Glenn Maynard, Hajime Morrita, Harald Alvestrand, Hayato Ito, Henri Sivonen, Hongchan Choi, Hunan Rostomyan, Ian Hickson, Igor Bukanov, Jacob Rossi, Jake Archibald, Jake Verbaten, James Graham, James Greene, James M Snell, James Robinson, Jayson Chen, Jeffrey Yasskin, Jens Lindström, Jeremy Davis, Jesse McCarthy, Jinho Bang, João Eiras, Joe Kesselman, John Atkins, John Dai, Jonas Sicking, Jonathan Kingston, Jonathan Robie, Joris van der Wel, Joshua Bell, J. S. Choi, Jungkee Song, Justin Summerlin, Kagami Sascha Rosylight, 呂康豪 (Kang-Hao Lu), 田村健人 (Kent TAMURA), Kevin J. Sung, Kevin Sweeney, Kirill Topolyan, Koji Ishii, Lachlan Hunt, Lauren Wood, Luca Casonato, Luke Zielinski, Magne Andersson, Majid Valipour, Malte Ubl, Manish Goregaokar, Manish Tripathi, Marcos Caceres, Mark Miller, Martijn van der Ven, Mason Freed, Mats Palmgren, Mounir Lamouri, Michael Stramel, Michael™ Smith, Mike Champion, Mike Taylor, Mike West, Nicolás Peña Moreno, Nidhi Jaju, Ojan Vafai, Oliver Nightingale, Olli Pettay, Ondřej Žára, Peter Sharpe, Philip Jägenstedt, Philippe Le Hégaret, Piers Wombwell, Pierre-Marie Dartus, prosody—Gab Vereable Context(, Rafael Weinstein, Rakina Zata Amni, Richard Bradshaw, Rick Byers, Rick Waldron, Robbert Broersma, Robin Berjon, Roland Steiner, Rune F. Halvorsen, Russell Bicknell, Ruud Steltenpool, Ryosuke Niwa, Sam Dutton, Sam Sneddon, Samuel Giles, Sanket Joshi, Scott Haseley, Sebastian Mayr, Seo Sanghyeon, Sergey G. Grekhov, Shiki Okasaka, Shinya Kawanaka, Simon Pieters, Simon Wülker, Stef Busking, Steve Byrne, Stig Halvorsen, Tab Atkins, Takashi Sakamoto, Takayoshi Kochi, Theresa O’Connor, Theodore Dubois, timeless, Timo Tijhof, Tobie Langel, Tom Pixley, Travis Leithead, Trevor Rowbotham, triple-underscore, Tristan Fraipont, Veli Şenol, Vidur Apparao, Warren He, Xidorn Quan, Yash Handa, Yehuda Katz, Yoav Weiss, Yoichi Osato, Yoshinori Sano, Yu Han, Yusuke Abe, and Zack Weinberg for being awesome! 

This standard is written by [Anne van Kesteren](https://annevankesteren.nl/) ([Apple](https://www.apple.com/), [annevk@annevk.nl](mailto:annevk@annevk.nl)) with substantial contributions from Aryeh Gregor ([ayg@aryeh.name](mailto:ayg@aryeh.name)) and Ms2ger ([ms2ger@gmail.com](mailto:ms2ger@gmail.com)). 

## Intellectual property rights#ipr

Part of the revision history of the integration points related to [custom](#concept-element-custom) elements can be found in [the w3c/webcomponents repository](https://github.com/w3c/webcomponents), which is available under the [W3C Software and Document License](https://www.w3.org/Consortium/Legal/2015/copyright-software-and-document). 

Copyright © WHATWG (Apple, Google, Mozilla, Microsoft). This work is licensed under a [Creative Commons Attribution 4.0
International License](https://creativecommons.org/licenses/by/4.0/). To the extent portions of it are incorporated into source code, such portions in the source code are licensed under the [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause) instead.

This is the Living Standard. Those interested in the patent-review version should view the [Living Standard Review Draft](/review-drafts/2025-12/).

## Index#index

### Terms defined by this specification#index-defined-here

- [abort](#eventdef-abortsignal-abort), in § 3.2
-  abort() 

  - [method for AbortController](#dom-abortcontroller-abort), in § 3.1
  - [method for AbortSignal](#dom-abortsignal-abort), in § 3.2

- [abort algorithms](#abortsignal-abort-algorithms), in § 3.2
- [AbortController](#abortcontroller), in § 3.1
- [AbortController()](#dom-abortcontroller-abortcontroller), in § 3.1
-  aborted 

  - [attribute for AbortSignal](#dom-abortsignal-aborted), in § 3.2
  - [dfn for AbortSignal](#abortsignal-aborted), in § 3.2

- [abort reason](#abortsignal-abort-reason), in § 3.2
-  abort(reason) 

  - [method for AbortController](#dom-abortcontroller-abort), in § 3.1
  - [method for AbortSignal](#dom-abortsignal-abort), in § 3.2

- [AbortSignal](#abortsignal), in § 3.2
- [AbstractRange](#abstractrange), in § 5.3
- [acceptNode(node)](#dom-nodefilter-acceptnode), in § 6.3
- [activation behavior](#eventtarget-activation-behavior), in § 2.7
- [add](#abortsignal-add), in § 3.2
- [add()](#dom-domtokenlist-add), in § 7.1
- [add an event listener](#add-an-event-listener), in § 2.7
- [addedNodes](#dom-mutationrecord-addednodes), in § 4.3.3
- [AddEventListenerOptions](#dictdef-addeventlisteneroptions), in § 2.7
- [addEventListener(type, callback)](#dom-eventtarget-addeventlistener), in § 2.7
- [addEventListener(type, callback, options)](#dom-eventtarget-addeventlistener), in § 2.7
- [add(...tokens)](#dom-domtokenlist-add), in § 7.1
- [add(tokens)](#dom-domtokenlist-add), in § 7.1
- [adopt](#concept-node-adopt), in § 4.5
- [adopting steps](#concept-node-adopt-ext), in § 4.5
- [adoptNode(node)](#dom-document-adoptnode), in § 4.5
- [after](#concept-range-bp-after), in § 5.2
- [after()](#dom-childnode-after), in § 4.2.8
- [after(...nodes)](#dom-childnode-after), in § 4.2.8
- [allow declarative shadow roots](#document-allow-declarative-shadow-roots), in § 4.5
- [ancestor](#concept-tree-ancestor), in § 1.1
- [any(signals)](#dom-abortsignal-any), in § 3.2
- [ANY_TYPE](#dom-xpathresult-any_type), in § 8.1
- [ANY_UNORDERED_NODE_TYPE](#dom-xpathresult-any_unordered_node_type), in § 8.1
- [append](#concept-node-append), in § 4.2.3
- [append()](#dom-parentnode-append), in § 4.2.6
- [append an attribute](#concept-element-attributes-append), in § 4.9
- [appendChild(node)](#dom-node-appendchild), in § 4.4
- [appendData(data)](#dom-characterdata-appenddata), in § 4.10
- [append(...nodes)](#dom-parentnode-append), in § 4.2.6
- [append to an event path](#concept-event-path-append), in § 2.9
- [assign a slot](#assign-a-slot), in § 4.2.2.4
- [assigned](#slotable-assigned), in § 4.2.2.2
- [assigned nodes](#slot-assigned-nodes), in § 4.2.2.1
- [assigned slot](#slotable-assigned-slot), in § 4.2.2.2
- [assignedSlot](#dom-slotable-assignedslot), in § 4.2.9
- [assign slottables](#assign-slotables), in § 4.2.2.4
- [assign slottables for a tree](#assign-slotables-for-a-tree), in § 4.2.2.4
- [attach a shadow root](#concept-attach-a-shadow-root), in § 4.9
- [attachShadow(init)](#dom-element-attachshadow), in § 4.9
- [AT_TARGET](#dom-event-at_target), in § 2.2
- [Attr](#attr), in § 4.9.2
- [attribute](#concept-attribute), in § 4.9.2
- [attribute change steps](#concept-element-attributes-change-ext), in § 4.9
- [attributeFilter](#dom-mutationobserverinit-attributefilter), in § 4.3.1
-  attribute list 

  - [dfn for Element](#concept-element-attribute), in § 4.9
  - [dfn for NamedNodeMap](#concept-namednodemap-attribute), in § 4.9.1

- [attribute name](#domtokenlist-attribute-name), in § 7.1
- [attributeName](#dom-mutationrecord-attributename), in § 4.3.3
- [attributeNamespace](#dom-mutationrecord-attributenamespace), in § 4.3.3
- [ATTRIBUTE_NODE](#dom-node-attribute_node), in § 4.4
- [attributeOldValue](#dom-mutationobserverinit-attributeoldvalue), in § 4.3.1
-  attributes 

  - [attribute for Element](#dom-element-attributes), in § 4.9
  - [dict-member for MutationObserverInit](#dom-mutationobserverinit-attributes), in § 4.3.1

- [available to element internals](#shadowroot-available-to-element-internals), in § 4.8
- [baseURI](#dom-node-baseuri), in § 4.4
- [before](#concept-range-bp-before), in § 5.2
- [before()](#dom-childnode-before), in § 4.2.8
- [before(...nodes)](#dom-childnode-before), in § 4.2.8
- [BOOLEAN_TYPE](#dom-xpathresult-boolean_type), in § 8.1
- [booleanValue](#dom-xpathresult-booleanvalue), in § 8.1
- [boundary point](#concept-range-bp), in § 5.2
-  bubbles 

  - [attribute for Event](#dom-event-bubbles), in § 2.2
  - [dict-member for EventInit](#dom-eventinit-bubbles), in § 2.2

- [BUBBLING_PHASE](#dom-event-bubbling_phase), in § 2.2
-  callback 

  - [dfn for MutationObserver](#concept-mo-callback), in § 4.3.1
  - [dfn for event listener](#event-listener-callback), in § 2.7

-  cancelable 

  - [attribute for Event](#dom-event-cancelable), in § 2.2
  - [dict-member for EventInit](#dom-eventinit-cancelable), in § 2.2

- [cancelBubble](#dom-event-cancelbubble), in § 2.2
- [canceled flag](#canceled-flag), in § 2.2
-  capture 

  - [dfn for event listener](#event-listener-capture), in § 2.7
  - [dict-member for EventListenerOptions](#dom-eventlisteneroptions-capture), in § 2.7

- [CAPTURING_PHASE](#dom-event-capturing_phase), in § 2.2
- [CDATASection](#cdatasection), in § 4.12
- [CDATA_SECTION_NODE](#dom-node-cdata_section_node), in § 4.4
- [change an attribute](#concept-element-attributes-change), in § 4.9
- [CharacterData](#characterdata), in § 4.10
- [characterData](#dom-mutationobserverinit-characterdata), in § 4.3.1
- [characterDataOldValue](#dom-mutationobserverinit-characterdataoldvalue), in § 4.3.1
- [characterSet](#dom-document-characterset), in § 4.5
- [charset](#dom-document-charset), in § 4.5
- [child](#concept-tree-child), in § 1.1
- [childElementCount](#dom-parentnode-childelementcount), in § 4.2.6
- [childList](#dom-mutationobserverinit-childlist), in § 4.3.1
- [ChildNode](#childnode), in § 4.2.8
- [childNodes](#dom-node-childnodes), in § 4.4
-  children 

  - [attribute for ParentNode](#dom-parentnode-children), in § 4.2.6
  - [dfn for tree](#concept-tree-child), in § 1.1

- [children changed steps](#concept-node-children-changed-ext), in § 4.2.3
- [child text content](#concept-child-text-content), in § 4.11
- [class](#concept-class), in § 4.9
- [classList](#dom-element-classlist), in § 4.9
- [className](#dom-element-classname), in § 4.9
- [clearParameters()](#dom-xsltprocessor-clearparameters), in § 9.1
-  clonable 

  - [attribute for ShadowRoot](#dom-shadowroot-clonable), in § 4.8
  - [dfn for ShadowRoot](#shadowroot-clonable), in § 4.8
  - [dict-member for ShadowRootInit](#dom-shadowrootinit-clonable), in § 4.9

- [clone a node](#concept-node-clone), in § 4.4
- [clone a single node](#clone-a-single-node), in § 4.4
- [cloneContents()](#dom-range-clonecontents), in § 5.5
- [cloneNode()](#dom-node-clonenode), in § 4.4
- [cloneNode(subtree)](#dom-node-clonenode), in § 4.4
- [cloneRange()](#dom-range-clonerange), in § 5.5
- [clone the contents](#concept-range-clone), in § 5.5
- [cloning steps](#concept-node-clone-ext), in § 4.4
- [cloning the contents](#concept-range-clone), in § 5.5
- ["closed"](#dom-shadowrootmode-closed), in § 4.8
- [closed-shadow-hidden](#concept-closed-shadow-hidden), in § 4.8
- [closest(selectors)](#dom-element-closest), in § 4.9
- [collapse()](#dom-range-collapse), in § 5.5
-  collapsed 

  - [attribute for AbstractRange](#dom-range-collapsed), in § 5.3
  - [dfn for range](#range-collapsed), in § 5.3

- [collapse(toStart)](#dom-range-collapse), in § 5.5
- [collection](#concept-collection), in § 4.2.10
- [Comment](#comment), in § 4.14
- [Comment()](#dom-comment-comment), in § 4.14
- [Comment(data)](#dom-comment-comment), in § 4.14
- [COMMENT_NODE](#dom-node-comment_node), in § 4.4
- [commonAncestorContainer](#dom-range-commonancestorcontainer), in § 5.5
- [compareBoundaryPoints(how, sourceRange)](#dom-range-compareboundarypoints), in § 5.5
- [compareDocumentPosition(other)](#dom-node-comparedocumentposition), in § 4.4
- [comparePoint(node, offset)](#dom-range-comparepoint), in § 5.5
- [compatMode](#dom-document-compatmode), in § 4.5
-  composed 

  - [attribute for Event](#dom-event-composed), in § 2.2
  - [dict-member for EventInit](#dom-eventinit-composed), in § 2.2
  - [dict-member for GetRootNodeOptions](#dom-getrootnodeoptions-composed), in § 4.4

- [composed flag](#composed-flag), in § 2.2
- [composedPath()](#dom-event-composedpath), in § 2.2
- [connected](#connected), in § 4.2.2
- [constructor](#concept-event-constructor), in § 2.5
-  constructor() 

  - [constructor for AbortController](#dom-abortcontroller-abortcontroller), in § 3.1
  - [constructor for Comment](#dom-comment-comment), in § 4.14
  - [constructor for Document](#dom-document-document), in § 4.5
  - [constructor for DocumentFragment](#dom-documentfragment-documentfragment), in § 4.7
  - [constructor for EventTarget](#dom-eventtarget-eventtarget), in § 2.7
  - [constructor for Range](#dom-range-range), in § 5.5
  - [constructor for Text](#dom-text-text), in § 4.11
  - [constructor for XPathEvaluator](#dom-xpathevaluator-xpathevaluator), in § 8.4
  - [constructor for XSLTProcessor](#dom-xsltprocessor-xsltprocessor), in § 9.1

- [constructor(callback)](#dom-mutationobserver-mutationobserver), in § 4.3.1
-  constructor(data) 

  - [constructor for Comment](#dom-comment-comment), in § 4.14
  - [constructor for Text](#dom-text-text), in § 4.11

- [constructor(init)](#dom-staticrange-staticrange), in § 5.4
-  constructor(type) 

  - [constructor for CustomEvent](#dom-customevent-customevent), in § 2.4
  - [constructor for Event](#dom-event-event), in § 2.2

-  constructor(type, eventInitDict) 

  - [constructor for CustomEvent](#dom-customevent-customevent), in § 2.4
  - [constructor for Event](#dom-event-event), in § 2.2

- [contained](#contained), in § 5.5
- [contains(other)](#dom-node-contains), in § 4.4
- [contains(token)](#dom-domtokenlist-contains), in § 7.1
- [content type](#concept-document-content-type), in § 4.5
- [contentType](#dom-document-contenttype), in § 4.5
- [contiguous exclusive Text nodes](#contiguous-exclusive-text-nodes), in § 4.11
- [contiguous Text nodes](#contiguous-text-nodes), in § 4.11
- [convert nodes into a node](#convert-nodes-into-a-node), in § 4.2.6
- [create a dependent abort signal](#create-a-dependent-abort-signal), in § 3.2
- [create an element](#concept-create-element), in § 4.9
- [create an element internal](#create-an-element-internal), in § 4.9
- [create an event](#concept-event-create), in § 2.5
- [createAttribute(localName)](#dom-document-createattribute), in § 4.5
- [createAttributeNS(namespace, qualifiedName)](#dom-document-createattributens), in § 4.5
- [createCDATASection(data)](#dom-document-createcdatasection), in § 4.5
- [createComment(data)](#dom-document-createcomment), in § 4.5
- [createDocumentFragment()](#dom-document-createdocumentfragment), in § 4.5
- [createDocument(namespace, qualifiedName)](#dom-domimplementation-createdocument), in § 4.5.1
- [createDocument(namespace, qualifiedName, doctype)](#dom-domimplementation-createdocument), in § 4.5.1
- [createDocumentType(name, publicId, systemId)](#dom-domimplementation-createdocumenttype), in § 4.5.1
- [createElement(localName)](#dom-document-createelement), in § 4.5
- [createElement(localName, options)](#dom-document-createelement), in § 4.5
- [createElementNS(namespace, qualifiedName)](#dom-document-createelementns), in § 4.5
- [createElementNS(namespace, qualifiedName, options)](#dom-document-createelementns), in § 4.5
- [createEntityReference()](#dom-document-createentityreference), in § 11
- [createEvent(interface)](#dom-document-createevent), in § 4.5
- [createExpression(expression)](#dom-xpathevaluatorbase-createexpression), in § 8.3
- [createExpression(expression, resolver)](#dom-xpathevaluatorbase-createexpression), in § 8.3
- [createHTMLDocument()](#dom-domimplementation-createhtmldocument), in § 4.5.1
- [createHTMLDocument(title)](#dom-domimplementation-createhtmldocument), in § 4.5.1
- [createNodeIterator(root)](#dom-document-createnodeiterator), in § 4.5
- [createNodeIterator(root, whatToShow)](#dom-document-createnodeiterator), in § 4.5
- [createNodeIterator(root, whatToShow, filter)](#dom-document-createnodeiterator), in § 4.5
- [createNSResolver(nodeResolver)](#dom-xpathevaluatorbase-creatensresolver), in § 8.3
- [createProcessingInstruction(target, data)](#dom-document-createprocessinginstruction), in § 4.5
- [createRange()](#dom-document-createrange), in § 4.5
- [createTextNode(data)](#dom-document-createtextnode), in § 4.5
- [createTreeWalker(root)](#dom-document-createtreewalker), in § 4.5
- [createTreeWalker(root, whatToShow)](#dom-document-createtreewalker), in § 4.5
- [createTreeWalker(root, whatToShow, filter)](#dom-document-createtreewalker), in § 4.5
- [creating an event](#concept-event-create), in § 2.5
- [current](#treewalker-current), in § 6.2
- [current event](#window-current-event), in § 2.3
- [currentNode](#dom-treewalker-currentnode), in § 6.2
- [currentTarget](#dom-event-currenttarget), in § 2.2
- [custom](#concept-element-custom), in § 4.9
- [custom element definition](#concept-element-custom-element-definition), in § 4.9
-  custom element registry 

  - [dfn for Document](#document-custom-element-registry), in § 4.5
  - [dfn for Element](#element-custom-element-registry), in § 4.9
  - [dfn for ShadowRoot](#shadowroot-custom-element-registry), in § 4.8

-  customElementRegistry 

  - [attribute for DocumentOrShadowRoot](#dom-documentorshadowroot-customelementregistry), in § 4.2.5
  - [attribute for Element](#dom-element-customelementregistry), in § 4.9
  - [dict-member for ElementCreationOptions](#dom-elementcreationoptions-customelementregistry), in § 4.5
  - [dict-member for ImportNodeOptions](#dom-importnodeoptions-customelementregistry), in § 4.5
  - [dict-member for ShadowRootInit](#dom-shadowrootinit-customelementregistry), in § 4.9

- [custom element state](#concept-element-custom-element-state), in § 4.9
- [CustomEvent](#customevent), in § 2.4
- [CustomEventInit](#dictdef-customeventinit), in § 2.4
- [CustomEvent(type)](#dom-customevent-customevent), in § 2.4
- [CustomEvent(type, eventInitDict)](#dom-customevent-customevent), in § 2.4
-  data 

  - [attribute for CharacterData](#dom-characterdata-data), in § 4.10
  - [dfn for CharacterData](#concept-cd-data), in § 4.10

- [declarative](#shadowroot-declarative), in § 4.8
- [default passive value](#default-passive-value), in § 2.7
- [defaultPrevented](#dom-event-defaultprevented), in § 2.2
- [defined](#concept-element-defined), in § 4.9
- [delegates focus](#shadowroot-delegates-focus), in § 4.8
-  delegatesFocus 

  - [attribute for ShadowRoot](#dom-shadowroot-delegatesfocus), in § 4.8
  - [dict-member for ShadowRootInit](#dom-shadowrootinit-delegatesfocus), in § 4.9

- [deleteContents()](#dom-range-deletecontents), in § 5.5
- [deleteData(offset, count)](#dom-characterdata-deletedata), in § 4.10
- [dependent](#abortsignal-dependent), in § 3.2
- [dependent signals](#abortsignal-dependent-signals), in § 3.2
- [descendant](#concept-tree-descendant), in § 1.1
- [descendant text content](#concept-descendant-text-content), in § 4.11
-  detach() 

  - [method for NodeIterator](#dom-nodeiterator-detach), in § 6.1
  - [method for Range](#dom-range-detach), in § 5.5

-  detail 

  - [attribute for CustomEvent](#dom-customevent-detail), in § 2.4
  - [dict-member for CustomEventInit](#dom-customeventinit-detail), in § 2.4

- [disconnect()](#dom-mutationobserver-disconnect), in § 4.3.1
- [dispatch](#concept-event-dispatch), in § 2.9
- [dispatchEvent(event)](#dom-eventtarget-dispatchevent), in § 2.7
- [dispatch flag](#dispatch-flag), in § 2.2
-  doctype 

  - [attribute for Document](#dom-document-doctype), in § 4.5
  - [definition of](#concept-doctype), in § 4.6

- [Document](#document), in § 4.5
-  document 

  - [definition of](#concept-document), in § 4.5
  - [dfn for clone a node](#clone-a-node-document), in § 4.4

- [Document()](#dom-document-document), in § 4.5
- [document element](#document-element), in § 4.2.1
- [documentElement](#dom-document-documentelement), in § 4.5
- [DocumentFragment](#documentfragment), in § 4.7
- [DocumentFragment()](#dom-documentfragment-documentfragment), in § 4.7
- [DOCUMENT_FRAGMENT_NODE](#dom-node-document_fragment_node), in § 4.4
- [DOCUMENT_NODE](#dom-node-document_node), in § 4.4
- [DocumentOrShadowRoot](#documentorshadowroot), in § 4.2.5
- [DOCUMENT_POSITION_CONTAINED_BY](#dom-node-document_position_contained_by), in § 4.4
- [DOCUMENT_POSITION_CONTAINS](#dom-node-document_position_contains), in § 4.4
- [DOCUMENT_POSITION_DISCONNECTED](#dom-node-document_position_disconnected), in § 4.4
- [DOCUMENT_POSITION_FOLLOWING](#dom-node-document_position_following), in § 4.4
- [DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC](#dom-node-document_position_implementation_specific), in § 4.4
- [DOCUMENT_POSITION_PRECEDING](#dom-node-document_position_preceding), in § 4.4
- [document tree](#concept-document-tree), in § 4.2.1
- [DocumentType](#documenttype), in § 4.6
- [DOCUMENT_TYPE_NODE](#dom-node-document_type_node), in § 4.4
- [documentURI](#dom-document-documenturi), in § 4.5
- [domConfig](#dom-document-domconfig), in § 11
- [DOMConfiguration](#domconfiguration), in § 11
- [DOMError](#domerror), in § 11
- [DOMErrorHandler](#domerrorhandler), in § 11
- [DOMImplementation](#domimplementation), in § 4.5.1
- [DOMImplementationList](#domimplementationlist), in § 11
- [DOMImplementationSource](#domimplementationsource), in § 11
- [DOMLocator](#domlocator), in § 11
- [DOMObject](#domobject), in § 11
- [DOMTokenList](#domtokenlist), in § 7.1
- [DOMUserData](#domuserdata), in § 11
- [effective global custom element registry](#effective-global-custom-element-registry), in § 4.5
- [Element](#element), in § 4.9
-  element 

  - [definition of](#concept-element), in § 4.9
  - [dfn for Attr](#concept-attribute-element), in § 4.9.2
  - [dfn for DOMTokenList](#domtokenlist-element), in § 7.1
  - [dfn for NamedNodeMap](#concept-namednodemap-element), in § 4.9.1

- [ElementCreationOptions](#dictdef-elementcreationoptions), in § 4.5
- [element interface](#concept-element-interface), in § 4.5
- [ELEMENT_NODE](#dom-node-element_node), in § 4.4
- [empty](#concept-node-empty), in § 4.2
- [encoding](#concept-document-encoding), in § 4.5
- [end](#concept-range-end), in § 5.3
-  endContainer 

  - [attribute for AbstractRange](#dom-range-endcontainer), in § 5.3
  - [dict-member for StaticRangeInit](#dom-staticrangeinit-endcontainer), in § 5.4

- [end node](#concept-range-end-node), in § 5.3
- [end offset](#concept-range-end-offset), in § 5.3
-  endOffset 

  - [attribute for AbstractRange](#dom-range-endoffset), in § 5.3
  - [dict-member for StaticRangeInit](#dom-staticrangeinit-endoffset), in § 5.4

- [END_TO_END](#dom-range-end_to_end), in § 5.5
- [END_TO_START](#dom-range-end_to_start), in § 5.5
- [ensure pre-insert validity](#concept-node-ensure-pre-insertion-validity), in § 4.2.3
- [entities](#dom-documenttype-entities), in § 11
- [Entity](#entity), in § 11
- [ENTITY_NODE](#dom-node-entity_node), in § 4.4
- [EntityReference](#entityreference), in § 11
- [ENTITY_REFERENCE_NODE](#dom-node-entity_reference_node), in § 4.4
- [equal](#concept-range-bp-equal), in § 5.2
- [equals](#concept-node-equals), in § 4.4
- [evaluate(contextNode)](#dom-xpathexpression-evaluate), in § 8.2
- [evaluate(contextNode, type)](#dom-xpathexpression-evaluate), in § 8.2
- [evaluate(contextNode, type, result)](#dom-xpathexpression-evaluate), in § 8.2
- [evaluate(expression, contextNode)](#dom-xpathevaluatorbase-evaluate), in § 8.3
- [evaluate(expression, contextNode, resolver)](#dom-xpathevaluatorbase-evaluate), in § 8.3
- [evaluate(expression, contextNode, resolver, type)](#dom-xpathevaluatorbase-evaluate), in § 8.3
- [evaluate(expression, contextNode, resolver, type, result)](#dom-xpathevaluatorbase-evaluate), in § 8.3
- [Event](#event), in § 2.2
-  event 

  - [attribute for Window](#dom-window-event), in § 2.3
  - [definition of](#concept-event), in § 2.2

- [event constructing steps](#concept-event-constructor-ext), in § 2.5
- [EventInit](#dictdef-eventinit), in § 2.2
- [event listener](#concept-event-listener), in § 2.7
- [EventListener](#callbackdef-eventlistener), in § 2.7
- [event listener list](#eventtarget-event-listener-list), in § 2.7
- [EventListenerOptions](#dictdef-eventlisteneroptions), in § 2.7
- [eventPhase](#dom-event-eventphase), in § 2.2
- [EventTarget](#eventtarget), in § 2.7
- [EventTarget()](#dom-eventtarget-eventtarget), in § 2.7
- [Event(type)](#dom-event-event), in § 2.2
- [Event(type, eventInitDict)](#dom-event-event), in § 2.2
- [exclusive Text node](#exclusive-text-node), in § 4.11
-  expandEntityReferences 

  - [attribute for NodeIterator](#dom-nodeiterator-expandentityreferences), in § 11
  - [attribute for TreeWalker](#dom-treewalker-expandentityreferences), in § 11

- [extract](#concept-range-extract), in § 5.5
- [extractContents()](#dom-range-extractcontents), in § 5.5
- [fallbackRegistry](#clone-a-node-fallbackregistry), in § 4.4
-  filter 

  - [attribute for NodeIterator](#dom-nodeiterator-filter), in § 6.1
  - [attribute for TreeWalker](#dom-treewalker-filter), in § 6.2
  - [definition of](#concept-node-filter), in § 6
  - [dfn for traversal](#concept-traversal-filter), in § 6

- [FILTER_ACCEPT](#dom-nodefilter-filter_accept), in § 6.3
- [FILTER_REJECT](#dom-nodefilter-filter_reject), in § 6.3
- [FILTER_SKIP](#dom-nodefilter-filter_skip), in § 6.3
- [find a slot](#find-a-slot), in § 4.2.2.3
- [find flattened slottables](#find-flattened-slotables), in § 4.2.2.3
- [find slottables](#find-slotables), in § 4.2.2.3
- [fire an event](#concept-event-fire), in § 2.10
- [first child](#concept-tree-first-child), in § 1.1
- [firstChild](#dom-node-firstchild), in § 4.4
- [firstChild()](#dom-treewalker-firstchild), in § 6.2
- [firstElementChild](#dom-parentnode-firstelementchild), in § 4.2.6
- [FIRST_ORDERED_NODE_TYPE](#dom-xpathresult-first_ordered_node_type), in § 8.1
- [flatten](#concept-flatten-options), in § 2.7
- [flatten element creation options](#flatten-element-creation-options), in § 4.5
- [flatten more](#event-flatten-more), in § 2.7
- [following](#concept-tree-following), in § 1.1
- [get an attribute by name](#concept-element-attributes-get-by-name), in § 4.9
- [get an attribute by namespace and local name](#concept-element-attributes-get-by-namespace), in § 4.9
- [get an attribute value](#concept-element-attributes-get-value), in § 4.9
- [getAttributeNames()](#dom-element-getattributenames), in § 4.9
- [getAttributeNodeNS(namespace, localName)](#dom-element-getattributenodens), in § 4.9
- [getAttributeNode(qualifiedName)](#dom-element-getattributenode), in § 4.9
- [getAttributeNS(namespace, localName)](#dom-element-getattributens), in § 4.9
- [getAttribute(qualifiedName)](#dom-element-getattribute), in § 4.9
- [getElementById(elementId)](#dom-nonelementparentnode-getelementbyid), in § 4.2.4
-  getElementsByClassName(classNames) 

  - [method for Document](#dom-document-getelementsbyclassname), in § 4.5
  - [method for Element](#dom-element-getelementsbyclassname), in § 4.9

-  getElementsByTagNameNS(namespace, localName) 

  - [method for Document](#dom-document-getelementsbytagnamens), in § 4.5
  - [method for Element](#dom-element-getelementsbytagnamens), in § 4.9

-  getElementsByTagName(qualifiedName) 

  - [method for Document](#dom-document-getelementsbytagname), in § 4.5
  - [method for Element](#dom-element-getelementsbytagname), in § 4.9

-  getFeature() 

  - [method for DOMImplementation](#dom-domimplementation-getfeature), in § 11
  - [method for Node](#dom-node-getfeature), in § 11

- [getNamedItemNS(namespace, localName)](#dom-namednodemap-getnameditemns), in § 4.9.1
- [getNamedItem(qualifiedName)](#dom-namednodemap-getnameditem), in § 4.9.1
- [getParameter(namespaceURI, localName)](#dom-xsltprocessor-getparameter), in § 9.1
- [getRootNode()](#dom-node-getrootnode), in § 4.4
- [getRootNode(options)](#dom-node-getrootnode), in § 4.4
- [GetRootNodeOptions](#dictdef-getrootnodeoptions), in § 4.4
- [get text content](#get-text-content), in § 4.4
- [get the parent](#get-the-parent), in § 2.7
- [getUserData()](#dom-node-getuserdata), in § 11
- [handle attribute changes](#handle-attribute-changes), in § 4.9
- [handleEvent(event)](#dom-eventlistener-handleevent), in § 2.7
- [has an attribute](#concept-element-attribute-has), in § 4.9
- [hasAttributeNS(namespace, localName)](#dom-element-hasattributens), in § 4.9
- [hasAttribute(qualifiedName)](#dom-element-hasattribute), in § 4.9
- [hasAttributes()](#dom-element-hasattributes), in § 4.9
- [hasChildNodes()](#dom-node-haschildnodes), in § 4.4
- [hasFeature()](#dom-domimplementation-hasfeature), in § 4.5.1
-  host 

  - [attribute for ShadowRoot](#dom-shadowroot-host), in § 4.8
  - [dfn for DocumentFragment](#concept-documentfragment-host), in § 4.7

- [host-including inclusive ancestor](#concept-tree-host-including-inclusive-ancestor), in § 4.7
- [HTMLCollection](#htmlcollection), in § 4.2.10.2
- [HTML document](#html-document), in § 4.5
- [HTML-uppercased qualified name](#element-html-uppercased-qualified-name), in § 4.9
- [ID](#concept-id), in § 4.9
- [id](#dom-element-id), in § 4.9
- [implementation](#dom-document-implementation), in § 4.5
- [importNode(node)](#dom-document-importnode), in § 4.5
- [importNode(node, options)](#dom-document-importnode), in § 4.5
- [ImportNodeOptions](#dictdef-importnodeoptions), in § 4.5
- [importStylesheet(style)](#dom-xsltprocessor-importstylesheet), in § 9.1
- [in a document](#in-a-document), in § 4.2.1
- [in a document tree](#in-a-document-tree), in § 4.2.1
- [inclusive ancestor](#concept-tree-inclusive-ancestor), in § 1.1
- [inclusive descendant](#concept-tree-inclusive-descendant), in § 1.1
- [inclusive sibling](#concept-tree-inclusive-sibling), in § 1.1
- [index](#concept-tree-index), in § 1.1
- [initCustomEvent(type)](#dom-customevent-initcustomevent), in § 2.4
- [initCustomEvent(type, bubbles)](#dom-customevent-initcustomevent), in § 2.4
- [initCustomEvent(type, bubbles, cancelable)](#dom-customevent-initcustomevent), in § 2.4
- [initCustomEvent(type, bubbles, cancelable, detail)](#dom-customevent-initcustomevent), in § 2.4
- [initEvent(type)](#dom-event-initevent), in § 2.2
- [initEvent(type, bubbles)](#dom-event-initevent), in § 2.2
- [initEvent(type, bubbles, cancelable)](#dom-event-initevent), in § 2.2
- [initialize](#concept-event-initialize), in § 2.2
- [initialized flag](#initialized-flag), in § 2.2
- [inner event creation steps](#inner-event-creation-steps), in § 2.5
- [inner invoke](#concept-event-listener-inner-invoke), in § 2.9
- [in passive listener flag](#in-passive-listener-flag), in § 2.2
- [inputEncoding](#dom-document-inputencoding), in § 4.5
-  insert 

  - [definition of](#concept-node-insert), in § 4.2.3
  - [dfn for live range](#concept-range-insert), in § 5.5

- [insert adjacent](#insert-adjacent), in § 4.9
- [insertAdjacentElement(where, element)](#dom-element-insertadjacentelement), in § 4.9
- [insertAdjacentText(where, data)](#dom-element-insertadjacenttext), in § 4.9
- [insertBefore(node, child)](#dom-node-insertbefore), in § 4.4
- [insertData(offset, data)](#dom-characterdata-insertdata), in § 4.10
- [insertion steps](#concept-node-insert-ext), in § 4.2.3
- [insertNode(node)](#dom-range-insertnode), in § 5.5
- [internal createElementNS steps](#internal-createelementns-steps), in § 4.5
- [internalSubset](#dom-documenttype-internalsubset), in § 11
- [intersectsNode(node)](#dom-range-intersectsnode), in § 5.5
- [invalidIteratorState](#dom-xpathresult-invaliditeratorstate), in § 8.1
- [invocation target](#event-path-invocation-target), in § 2.2
- [invocation-target-in-shadow-tree](#event-path-invocation-target-in-shadow-tree), in § 2.2
- [invoke](#concept-event-listener-invoke), in § 2.9
- [is](#dom-elementcreationoptions-is), in § 4.5
- [is active](#concept-traversal-active), in § 6
- [is a global custom element registry](#is-a-global-custom-element-registry), in § 4.5
- [isConnected](#dom-node-isconnected), in § 4.4
- [isDefaultNamespace(namespace)](#dom-node-isdefaultnamespace), in § 4.4
- [isElementContentWhitespace](#dom-text-iselementcontentwhitespace), in § 11
- [isEqualNode(otherNode)](#dom-node-isequalnode), in § 4.4
- [isId](#dom-attr-isid), in § 11
- [isPointInRange(node, offset)](#dom-range-ispointinrange), in § 5.5
- [isSameNode(otherNode)](#dom-node-issamenode), in § 4.4
- [isSupported](#dom-node-issupported), in § 11
- [isTrusted](#dom-event-istrusted), in § 2.2
- [is value](#concept-element-is-value), in § 4.9
-  item(index) 

  - [method for DOMTokenList](#dom-domtokenlist-item), in § 7.1
  - [method for HTMLCollection](#dom-htmlcollection-item), in § 4.2.10.2
  - [method for NamedNodeMap](#dom-namednodemap-item), in § 4.9.1
  - [method for NodeList](#dom-nodelist-item), in § 4.2.10.1

- [iterateNext()](#dom-xpathresult-iteratenext), in § 8.1
- [iterator collection](#iterator-collection), in § 6.1
- [keep custom element registry null](#shadowroot-keep-custom-element-registry-null), in § 4.8
- [last child](#concept-tree-last-child), in § 1.1
- [lastChild](#dom-node-lastchild), in § 4.4
- [lastChild()](#dom-treewalker-lastchild), in § 6.2
- [lastElementChild](#dom-parentnode-lastelementchild), in § 4.2.6
- [legacy-canceled-activation behavior](#eventtarget-legacy-canceled-activation-behavior), in § 2.7
- [legacy-obtain service worker fetch event listener callbacks](#legacy-obtain-service-worker-fetch-event-listener-callbacks), in § 2.8
- [legacy-pre-activation behavior](#eventtarget-legacy-pre-activation-behavior), in § 2.7
-  length 

  - [attribute for CharacterData](#dom-characterdata-length), in § 4.10
  - [attribute for DOMTokenList](#dom-domtokenlist-length), in § 7.1
  - [attribute for HTMLCollection](#dom-htmlcollection-length), in § 4.2.10.2
  - [attribute for NamedNodeMap](#dom-namednodemap-length), in § 4.9.1
  - [attribute for NodeList](#dom-nodelist-length), in § 4.2.10.1
  - [dfn for Node](#concept-node-length), in § 4.2

- [light tree](#concept-light-tree), in § 4.2.2
- [limited-quirks mode](#concept-document-limited-quirks), in § 4.5
- [list of elements with class names classNames](#concept-getelementsbyclassname), in § 4.4
- [list of elements with namespace namespace and local name localName](#concept-getelementsbytagnamens), in § 4.4
- [list of elements with qualified name qualifiedName](#concept-getelementsbytagname), in § 4.4
- [live](#concept-collection-live), in § 4.2.10
- [live collection](#concept-collection-live), in § 4.2.10
- [live range pre-remove steps](#live-range-pre-remove-steps), in § 5.5
- [live ranges](#concept-live-range), in § 5.5
-  local name 

  - [dfn for Attr](#concept-attribute-local-name), in § 4.9.2
  - [dfn for Element](#concept-element-local-name), in § 4.9

-  localName 

  - [attribute for Attr](#dom-attr-localname), in § 4.9.2
  - [attribute for Element](#dom-element-localname), in § 4.9

- [locate a namespace](#locate-a-namespace), in § 4.4
- [locate a namespace prefix](#locate-a-namespace-prefix), in § 4.4
- [locating a namespace prefix](#locate-a-namespace-prefix), in § 4.4
-  lookupNamespaceURI(prefix) 

  - [method for Node](#dom-node-lookupnamespaceuri), in § 4.4
  - [method for XPathNSResolver](#dom-xpathnsresolver-lookupnamespaceuri), in § 8.3

- [lookupPrefix(namespace)](#dom-node-lookupprefix), in § 4.4
- ["manual"](#dom-slotassignmentmode-manual), in § 4.8
- [manual slot assignment](#slottable-manual-slot-assignment), in § 4.2.2.2
- [matches(selectors)](#dom-element-matches), in § 4.9
-  mode 

  - [attribute for ShadowRoot](#dom-shadowroot-mode), in § 4.8
  - [dfn for Document](#concept-document-mode), in § 4.5
  - [dfn for ShadowRoot](#shadowroot-mode), in § 4.8
  - [dict-member for ShadowRootInit](#dom-shadowrootinit-mode), in § 4.9

- [move](#move), in § 4.2.3
- [moveBefore(node, child)](#dom-parentnode-movebefore), in § 4.2.6
- [moving steps](#concept-node-move-ext), in § 4.2.3
- [MutationCallback](#callbackdef-mutationcallback), in § 4.3.1
- [MutationEvent](#mutationevent), in § 11
- [MutationNameEvent](#mutationnameevent), in § 11
- [MutationObserver](#mutationobserver), in § 4.3.1
- [MutationObserver(callback)](#dom-mutationobserver-mutationobserver), in § 4.3.1
- [MutationObserverInit](#dictdef-mutationobserverinit), in § 4.3.1
- [mutation observer microtask queued](#mutation-observer-compound-microtask-queued-flag), in § 4.3
- [MutationRecord](#mutationrecord), in § 4.3.3
-  name 

  - [attribute for Attr](#dom-attr-name), in § 4.9.2
  - [attribute for DocumentType](#dom-documenttype-name), in § 4.6
  - [dfn for DocumentType](#concept-doctype-name), in § 4.6
  - [dfn for slot](#slot-name), in § 4.2.2.1
  - [dfn for slottable](#slotable-name), in § 4.2.2.2

- ["named"](#dom-slotassignmentmode-named), in § 4.8
- [named attribute](#concept-named-attribute), in § 4.9.2
- [namedItem(key)](#dom-htmlcollection-nameditem-key), in § 4.2.10.2
- [namedItem(name)](#dom-htmlcollection-nameditem), in § 4.2.10.2
- [NamedNodeMap](#namednodemap), in § 4.9.1
- [NameList](#namelist), in § 11
-  namespace 

  - [dfn for Attr](#concept-attribute-namespace), in § 4.9.2
  - [dfn for Element](#concept-element-namespace), in § 4.9

-  namespace prefix 

  - [dfn for Attr](#concept-attribute-namespace-prefix), in § 4.9.2
  - [dfn for Element](#concept-element-namespace-prefix), in § 4.9

-  namespaceURI 

  - [attribute for Attr](#dom-attr-namespaceuri), in § 4.9.2
  - [attribute for Element](#dom-element-namespaceuri), in § 4.9

- [nextElementSibling](#dom-nondocumenttypechildnode-nextelementsibling), in § 4.2.7
-  nextNode() 

  - [method for NodeIterator](#dom-nodeiterator-nextnode), in § 6.1
  - [method for TreeWalker](#dom-treewalker-nextnode), in § 6.2

- [next sibling](#concept-tree-next-sibling), in § 1.1
-  nextSibling 

  - [attribute for MutationRecord](#dom-mutationrecord-nextsibling), in § 4.3.3
  - [attribute for Node](#dom-node-nextsibling), in § 4.4

- [nextSibling()](#dom-treewalker-nextsibling), in § 6.2
- [Node](#node), in § 4.4
- [node](#boundary-point-node), in § 5.2
- [node document](#concept-node-document), in § 4.4
- [NodeFilter](#callbackdef-nodefilter), in § 6.3
- [NodeIterator](#nodeiterator), in § 6.1
- [NodeIterator pre-remove steps](#nodeiterator-pre-removing-steps), in § 6.1
- [node list](#mutationobserver-node-list), in § 4.3.1
- [NodeList](#nodelist), in § 4.2.10.1
- [nodeName](#dom-node-nodename), in § 4.4
- [Nodes](#concept-node), in § 4.2
- [node tree](#concept-node-tree), in § 4.2
- [nodeType](#dom-node-nodetype), in § 4.4
- [nodeValue](#dom-node-nodevalue), in § 4.4
- [NonDocumentTypeChildNode](#nondocumenttypechildnode), in § 4.2.7
- [NONE](#dom-event-none), in § 2.2
- [NonElementParentNode](#nonelementparentnode), in § 4.2.4
- [no-quirks mode](#concept-document-no-quirks), in § 4.5
- [normalize()](#dom-node-normalize), in § 4.4
- [normalizeDocument()](#dom-document-normalizedocument), in § 11
- [Notation](#notation), in § 11
- [NOTATION_NODE](#dom-node-notation_node), in § 4.4
- [notations](#dom-documenttype-notations), in § 11
- [notify mutation observers](#notify-mutation-observers), in § 4.3
- [NUMBER_TYPE](#dom-xpathresult-number_type), in § 8.1
- [numberValue](#dom-xpathresult-numbervalue), in § 8.1
- [observer](#registered-observer-observer), in § 4.3
- [observe(target)](#dom-mutationobserver-observe), in § 4.3.1
- [observe(target, options)](#dom-mutationobserver-observe), in § 4.3.1
- [offset](#concept-range-bp-offset), in § 5.2
- [oldValue](#dom-mutationrecord-oldvalue), in § 4.3.3
-  onabort 

  - [attribute for AbortSignal](#dom-abortsignal-onabort), in § 3.2
  - [dfn for AbortSignal](#abortsignal-onabort), in § 3.2

-  once 

  - [dfn for event listener](#event-listener-once), in § 2.7
  - [dict-member for AddEventListenerOptions](#dom-addeventlisteneroptions-once), in § 2.7

-  onslotchange 

  - [attribute for ShadowRoot](#dom-shadowroot-onslotchange), in § 4.8
  - [dfn for ShadowRoot](#shadowroot-onslotchange), in § 4.8

- ["open"](#dom-shadowrootmode-open), in § 4.8
- [options](#registered-observer-options), in § 4.3
- [ORDERED_NODE_ITERATOR_TYPE](#dom-xpathresult-ordered_node_iterator_type), in § 8.1
- [ORDERED_NODE_SNAPSHOT_TYPE](#dom-xpathresult-ordered_node_snapshot_type), in § 8.1
- [ordered set parser](#concept-ordered-set-parser), in § 1.2
- [ordered set serializer](#concept-ordered-set-serializer), in § 1.2
- [origin](#concept-document-origin), in § 4.5
- [other applicable specifications](#other-applicable-specifications), in § 1
- [ownerDocument](#dom-node-ownerdocument), in § 4.4
- [ownerElement](#dom-attr-ownerelement), in § 4.9.2
-  parent 

  - [dfn for clone a node](#clone-a-node-parent), in § 4.4
  - [dfn for tree](#concept-tree-parent), in § 1.1

- [parent element](#parent-element), in § 4.9
- [parentElement](#dom-node-parentelement), in § 4.4
- [ParentNode](#parentnode), in § 4.2.6
- [parentNode](#dom-node-parentnode), in § 4.4
- [parentNode()](#dom-treewalker-parentnode), in § 6.2
- [partially contained](#partially-contained), in § 5.5
- [participate](#concept-tree-participate), in § 1.1
- [participate in a tree](#concept-tree-participate), in § 1.1
- [participates in a tree](#concept-tree-participate), in § 1.1
-  passive 

  - [dfn for event listener](#event-listener-passive), in § 2.7
  - [dict-member for AddEventListenerOptions](#dom-addeventlisteneroptions-passive), in § 2.7

- [path](#event-path), in § 2.2
- [pending mutation observers](#mutation-observer-list), in § 4.3
- [pointer before reference](#nodeiterator-pointer-before-reference), in § 6.1
- [pointerBeforeReferenceNode](#dom-nodeiterator-pointerbeforereferencenode), in § 6.1
- [position](#concept-range-bp-position), in § 5.2
- [post-connection steps](#concept-node-post-connection-ext), in § 4.2.3
- [potential event target](#potential-event-target), in § 2.2
- [preceding](#concept-tree-preceding), in § 1.1
-  prefix 

  - [attribute for Attr](#dom-attr-prefix), in § 4.9.2
  - [attribute for Element](#dom-element-prefix), in § 4.9

- [pre-insert](#concept-node-pre-insert), in § 4.2.3
- [prepend()](#dom-parentnode-prepend), in § 4.2.6
- [prepend(...nodes)](#dom-parentnode-prepend), in § 4.2.6
- [pre-remove](#concept-node-pre-remove), in § 4.2.3
- [preventDefault()](#dom-event-preventdefault), in § 2.2
- [previousElementSibling](#dom-nondocumenttypechildnode-previouselementsibling), in § 4.2.7
-  previousNode() 

  - [method for NodeIterator](#dom-nodeiterator-previousnode), in § 6.1
  - [method for TreeWalker](#dom-treewalker-previousnode), in § 6.2

- [previous sibling](#concept-tree-previous-sibling), in § 1.1
-  previousSibling 

  - [attribute for MutationRecord](#dom-mutationrecord-previoussibling), in § 4.3.3
  - [attribute for Node](#dom-node-previoussibling), in § 4.4

- [previousSibling()](#dom-treewalker-previoussibling), in § 6.2
- [ProcessingInstruction](#processinginstruction), in § 4.13
- [PROCESSING_INSTRUCTION_NODE](#dom-node-processing_instruction_node), in § 4.4
- [public ID](#concept-doctype-publicid), in § 4.6
- [publicId](#dom-documenttype-publicid), in § 4.6
-  qualified name 

  - [dfn for Attr](#concept-attribute-qualified-name), in § 4.9.2
  - [dfn for Element](#concept-element-qualified-name), in § 4.9

- [querySelectorAll(selectors)](#dom-parentnode-queryselectorall), in § 4.2.6
- [querySelector(selectors)](#dom-parentnode-queryselector), in § 4.2.6
- [queue a mutation observer microtask](#queue-a-mutation-observer-compound-microtask), in § 4.3
- [queue a mutation record](#queue-a-mutation-record), in § 4.3.2
- [queue a tree mutation record](#queue-a-tree-mutation-record), in § 4.3.2
- [quirks mode](#concept-document-quirks), in § 4.5
- [Range](#range), in § 5.5
- [range](#concept-range), in § 5.3
- [Range()](#dom-range-range), in § 5.5
- [RangeException](#rangeexception), in § 11
- [reason](#dom-abortsignal-reason), in § 3.2
- [record queue](#concept-mo-queue), in § 4.3.1
- [reference](#nodeiterator-reference), in § 6.1
- [referenceNode](#dom-nodeiterator-referencenode), in § 6.1
- [reflect](#concept-reflect), in § 4.9
- [registered observer](#registered-observer), in § 4.3
- [registered observer list](#registered-observer-list), in § 4.3
-  relatedTarget 

  - [dfn for Event](#event-relatedtarget), in § 2.2
  - [dfn for Event/path](#event-path-relatedtarget), in § 2.2

-  remove 

  - [definition of](#concept-node-remove), in § 4.2.3
  - [dfn for AbortSignal](#abortsignal-remove), in § 3.2

-  remove() 

  - [method for ChildNode](#dom-childnode-remove), in § 4.2.8
  - [method for DOMTokenList](#dom-domtokenlist-remove), in § 7.1

- [remove all event listeners](#remove-all-event-listeners), in § 2.7
- [remove an attribute](#concept-element-attributes-remove), in § 4.9
- [remove an attribute by name](#concept-element-attributes-remove-by-name), in § 4.9
- [remove an attribute by namespace and local name](#concept-element-attributes-remove-by-namespace), in § 4.9
- [remove an event listener](#remove-an-event-listener), in § 2.7
- [removeAttributeNode(attr)](#dom-element-removeattributenode), in § 4.9
- [removeAttributeNS(namespace, localName)](#dom-element-removeattributens), in § 4.9
- [removeAttribute(qualifiedName)](#dom-element-removeattribute), in § 4.9
- [removeChild(child)](#dom-node-removechild), in § 4.4
- [removed](#event-listener-removed), in § 2.7
- [removedNodes](#dom-mutationrecord-removednodes), in § 4.3.3
- [removeEventListener(type, callback)](#dom-eventtarget-removeeventlistener), in § 2.7
- [removeEventListener(type, callback, options)](#dom-eventtarget-removeeventlistener), in § 2.7
- [removeNamedItemNS(namespace, localName)](#dom-namednodemap-removenameditemns), in § 4.9.1
- [removeNamedItem(qualifiedName)](#dom-namednodemap-removenameditem), in § 4.9.1
- [removeParameter(namespaceURI, localName)](#dom-xsltprocessor-removeparameter), in § 9.1
- [remove(...tokens)](#dom-domtokenlist-remove), in § 7.1
- [remove(tokens)](#dom-domtokenlist-remove), in § 7.1
- [removing steps](#concept-node-remove-ext), in § 4.2.3
- [renameNode()](#dom-document-renamenode), in § 11
- [replace](#concept-node-replace), in § 4.2.3
- [replace all](#concept-node-replace-all), in § 4.2.3
- [replace an attribute](#concept-element-attributes-replace), in § 4.9
- [replaceChild(node, child)](#dom-node-replacechild), in § 4.4
- [replaceChildren()](#dom-parentnode-replacechildren), in § 4.2.6
- [replaceChildren(...nodes)](#dom-parentnode-replacechildren), in § 4.2.6
- [replace data](#concept-cd-replace), in § 4.10
- [replaceData(offset, count, data)](#dom-characterdata-replacedata), in § 4.10
- [replace(token, newToken)](#dom-domtokenlist-replace), in § 7.1
- [replaceWholeText()](#dom-text-replacewholetext), in § 11
- [replaceWith()](#dom-childnode-replacewith), in § 4.2.8
- [replaceWith(...nodes)](#dom-childnode-replacewith), in § 4.2.8
- [represented by the collection](#represented-by-the-collection), in § 4.2.10
- [reset()](#dom-xsltprocessor-reset), in § 9.1
- [resultType](#dom-xpathresult-resulttype), in § 8.1
- [retarget](#retarget), in § 4.8
- [retargeting](#retarget), in § 4.8
- [returnValue](#dom-event-returnvalue), in § 2.2
-  root 

  - [attribute for NodeIterator](#dom-nodeiterator-root), in § 6.1
  - [attribute for TreeWalker](#dom-treewalker-root), in § 6.2
  - [dfn for live range](#concept-range-root), in § 5.5
  - [dfn for traversal](#concept-traversal-root), in § 6
  - [dfn for tree](#concept-tree-root), in § 1.1

- [root-of-closed-tree](#event-path-root-of-closed-tree), in § 2.2
- [run the abort steps](#run-the-abort-steps), in § 3.2
-  schemaTypeInfo 

  - [attribute for Attr](#dom-attr-schematypeinfo), in § 11
  - [attribute for Element](#dom-element-schematypeinfo), in § 11

- [scope-match a selectors string](#scope-match-a-selectors-string), in § 1.3
- [select](#concept-range-select), in § 5.5
- [selectNodeContents(node)](#dom-range-selectnodecontents), in § 5.5
- [selectNode(node)](#dom-range-selectnode), in § 5.5
- [selfOnly](#dom-importnodeoptions-selfonly), in § 4.5
-  serializable 

  - [attribute for ShadowRoot](#dom-shadowroot-serializable), in § 4.8
  - [dfn for ShadowRoot](#shadowroot-serializable), in § 4.8
  - [dict-member for ShadowRootInit](#dom-shadowrootinit-serializable), in § 4.9

- [serialize steps](#concept-dtl-serialize), in § 7.1
- [set an attribute](#concept-element-attributes-set), in § 4.9
- [set an attribute value](#concept-element-attributes-set-value), in § 4.9
- [set an existing attribute value](#set-an-existing-attribute-value), in § 4.9.2
- [setAttributeNode(attr)](#dom-element-setattributenode), in § 4.9
- [setAttributeNodeNS(attr)](#dom-element-setattributenodens), in § 4.9
- [setAttributeNS(namespace, qualifiedName, value)](#dom-element-setattributens), in § 4.9
- [setAttribute(qualifiedName, value)](#dom-element-setattribute), in § 4.9
- [setEndAfter(node)](#dom-range-setendafter), in § 5.5
- [setEndBefore(node)](#dom-range-setendbefore), in § 5.5
- [setEnd(node, offset)](#dom-range-setend), in § 5.5
- [setIdAttribute()](#dom-element-setidattribute), in § 11
- [setIdAttributeNode()](#dom-element-setidattributenode), in § 11
- [setIdAttributeNS()](#dom-element-setidattributens), in § 11
- [setNamedItem(attr)](#dom-namednodemap-setnameditem), in § 4.9.1
- [setNamedItemNS(attr)](#dom-namednodemap-setnameditemns), in § 4.9.1
- [setParameter(namespaceURI, localName, value)](#dom-xsltprocessor-setparameter), in § 9.1
- [setStartAfter(node)](#dom-range-setstartafter), in § 5.5
- [setStartBefore(node)](#dom-range-setstartbefore), in § 5.5
- [setStart(node, offset)](#dom-range-setstart), in § 5.5
- [set text content](#set-text-content), in § 4.4
- [set the canceled flag](#set-the-canceled-flag), in § 2.2
- [set the end](#concept-range-bp-set), in § 5.5
- [set the start](#concept-range-bp-set), in § 5.5
- [setUserData()](#dom-node-setuserdata), in § 11
- [shadow-adjusted target](#event-path-shadow-adjusted-target), in § 2.2
- [shadow host](#element-shadow-host), in § 4.9
- [shadow-including ancestor](#concept-shadow-including-ancestor), in § 4.8
- [shadow-including descendant](#concept-shadow-including-descendant), in § 4.8
- [shadow-including inclusive ancestor](#concept-shadow-including-inclusive-ancestor), in § 4.8
- [shadow-including inclusive descendant](#concept-shadow-including-inclusive-descendant), in § 4.8
- [Shadow-including preorder, depth-first traversal](#shadow-including-preorder-depth-first-traversal), in § 4.8
- [shadow-including root](#concept-shadow-including-root), in § 4.8
- [shadow-including tree order](#concept-shadow-including-tree-order), in § 4.8
-  shadow root 

  - [definition of](#concept-shadow-root), in § 4.8
  - [dfn for Element](#concept-element-shadow-root), in § 4.9

- [ShadowRoot](#shadowroot), in § 4.8
- [shadowRoot](#dom-element-shadowroot), in § 4.9
- [ShadowRootInit](#dictdef-shadowrootinit), in § 4.9
- [ShadowRootMode](#enumdef-shadowrootmode), in § 4.8
- [shadow tree](#concept-shadow-tree), in § 4.2.2
- [SHOW_ALL](#dom-nodefilter-show_all), in § 6.3
- [SHOW_ATTRIBUTE](#dom-nodefilter-show_attribute), in § 6.3
- [SHOW_CDATA_SECTION](#dom-nodefilter-show_cdata_section), in § 6.3
- [SHOW_COMMENT](#dom-nodefilter-show_comment), in § 6.3
- [SHOW_DOCUMENT](#dom-nodefilter-show_document), in § 6.3
- [SHOW_DOCUMENT_FRAGMENT](#dom-nodefilter-show_document_fragment), in § 6.3
- [SHOW_DOCUMENT_TYPE](#dom-nodefilter-show_document_type), in § 6.3
- [SHOW_ELEMENT](#dom-nodefilter-show_element), in § 6.3
- [SHOW_ENTITY](#dom-nodefilter-show_entity), in § 6.3
- [SHOW_ENTITY_REFERENCE](#dom-nodefilter-show_entity_reference), in § 6.3
- [SHOW_NOTATION](#dom-nodefilter-show_notation), in § 6.3
- [SHOW_PROCESSING_INSTRUCTION](#dom-nodefilter-show_processing_instruction), in § 6.3
- [SHOW_TEXT](#dom-nodefilter-show_text), in § 6.3
- [sibling](#concept-tree-sibling), in § 1.1
-  signal 

  - [attribute for AbortController](#dom-abortcontroller-signal), in § 3.1
  - [dfn for AbortController](#abortcontroller-signal), in § 3.1
  - [dfn for event listener](#event-listener-signal), in § 2.7
  - [dict-member for AddEventListenerOptions](#dom-addeventlisteneroptions-signal), in § 2.7

-  signal abort 

  - [dfn for AbortController](#abortcontroller-signal-abort), in § 3.1
  - [dfn for AbortSignal](#abortsignal-signal-abort), in § 3.2

- [signal a slot change](#signal-a-slot-change), in § 4.2.2.5
- [signal slots](#signal-slot-list), in § 4.2.2.5
- [singleNodeValue](#dom-xpathresult-singlenodevalue), in § 8.1
-  slot 

  - [attribute for Element](#dom-element-slot), in § 4.9
  - [definition of](#concept-slot), in § 4.2.2.1

- [slot assignment](#shadowroot-slot-assignment), in § 4.8
-  slotAssignment 

  - [attribute for ShadowRoot](#dom-shadowroot-slotassignment), in § 4.8
  - [dict-member for ShadowRootInit](#dom-shadowrootinit-slotassignment), in § 4.9

- [SlotAssignmentMode](#enumdef-slotassignmentmode), in § 4.8
- [slotchange](#eventdef-htmlslotelement-slotchange), in § 4.3
- [slot-in-closed-tree](#event-path-slot-in-closed-tree), in § 2.2
- [Slottable](#slotable), in § 4.2.9
- [slottable](#concept-slotable), in § 4.2.2.2
- [snapshotItem(index)](#dom-xpathresult-snapshotitem), in § 8.1
- [snapshotLength](#dom-xpathresult-snapshotlength), in § 8.1
- [source](#transient-registered-observer-source), in § 4.3
- [source signals](#abortsignal-source-signals), in § 3.2
- [specified](#dom-attr-specified), in § 4.9.2
- [split a Text node](#concept-text-split), in § 4.11
- [splitText(offset)](#dom-text-splittext), in § 4.11
- [srcElement](#dom-event-srcelement), in § 2.2
- [start](#concept-range-start), in § 5.3
-  startContainer 

  - [attribute for AbstractRange](#dom-range-startcontainer), in § 5.3
  - [dict-member for StaticRangeInit](#dom-staticrangeinit-startcontainer), in § 5.4

- [start node](#concept-range-start-node), in § 5.3
- [start offset](#concept-range-start-offset), in § 5.3
-  startOffset 

  - [attribute for AbstractRange](#dom-range-startoffset), in § 5.3
  - [dict-member for StaticRangeInit](#dom-staticrangeinit-startoffset), in § 5.4

- [START_TO_END](#dom-range-start_to_end), in § 5.5
- [START_TO_START](#dom-range-start_to_start), in § 5.5
- [static collection](#concept-collection-static), in § 4.2.10
- [StaticRange](#staticrange), in § 5.4
- [StaticRange(init)](#dom-staticrange-staticrange), in § 5.4
- [StaticRangeInit](#dictdef-staticrangeinit), in § 5.4
- [stopImmediatePropagation()](#dom-event-stopimmediatepropagation), in § 2.2
- [stop immediate propagation flag](#stop-immediate-propagation-flag), in § 2.2
- [stopPropagation()](#dom-event-stoppropagation), in § 2.2
- [stop propagation flag](#stop-propagation-flag), in § 2.2
- [strictErrorChecking](#dom-document-stricterrorchecking), in § 11
- [stringification behavior](#DOMTokenList-stringification-behavior), in § 7.1
- [stringificationbehavior](#dom-range-stringifier), in § 5.5
- [string replace all](#string-replace-all), in § 4.4
- [STRING_TYPE](#dom-xpathresult-string_type), in § 8.1
- [stringValue](#dom-xpathresult-stringvalue), in § 8.1
- [substring data](#concept-cd-substring), in § 4.10
- [substringData(offset, count)](#dom-characterdata-substringdata), in § 4.10
-  subtree 

  - [dfn for clone a node](#clone-a-node-subtree), in § 4.4
  - [dict-member for MutationObserverInit](#dom-mutationobserverinit-subtree), in § 4.3.1

- [supported tokens](#concept-supported-tokens), in § 7.1
- [supports(token)](#dom-domtokenlist-supports), in § 7.1
-  suppressObservers 

  - [dfn for insert](#insert-suppressobservers), in § 4.2.3
  - [dfn for remove](#remove-suppressobservers), in § 4.2.3

- [surroundContents(newParent)](#dom-range-surroundcontents), in § 5.5
- [system ID](#concept-doctype-systemid), in § 4.6
- [systemId](#dom-documenttype-systemid), in § 4.6
- [tagName](#dom-element-tagname), in § 4.9
- [takeRecords()](#dom-mutationobserver-takerecords), in § 4.3.1
-  target 

  - [attribute for Event](#dom-event-target), in § 2.2
  - [attribute for MutationRecord](#dom-mutationrecord-target), in § 4.3.3
  - [attribute for ProcessingInstruction](#dom-processinginstruction-target), in § 4.13
  - [dfn for Event](#event-target), in § 2.2
  - [dfn for ProcessingInstruction](#concept-pi-target), in § 4.13

- [Text](#text), in § 4.11
- [Text()](#dom-text-text), in § 4.11
- [textContent](#dom-node-textcontent), in § 4.4
- [Text(data)](#dom-text-text), in § 4.11
- [TEXT_NODE](#dom-node-text_node), in § 4.4
- [throwIfAborted()](#dom-abortsignal-throwifaborted), in § 3.2
- [timeout(milliseconds)](#dom-abortsignal-timeout), in § 3.2
- [timeStamp](#dom-event-timestamp), in § 2.2
- [toggleAttribute(qualifiedName)](#dom-element-toggleattribute), in § 4.9
- [toggleAttribute(qualifiedName, force)](#dom-element-toggleattribute), in § 4.9
- [toggle(token)](#dom-domtokenlist-toggle), in § 7.1
- [toggle(token, force)](#dom-domtokenlist-toggle), in § 7.1
- [token set](#concept-dtl-tokens), in § 7.1
-  touch target list 

  - [dfn for Event](#event-touch-target-list), in § 2.2
  - [dfn for Event/path](#event-path-touch-target-list), in § 2.2

- [transformToDocument(source)](#dom-xsltprocessor-transformtodocument), in § 9.1
- [transformToFragment(source, output)](#dom-xsltprocessor-transformtofragment), in § 9.1
- [transient registered observer](#transient-registered-observer), in § 4.3
- [traverse](#concept-nodeiterator-traverse), in § 6.1
- [traverse children](#concept-traverse-children), in § 6.2
- [traverse siblings](#concept-traverse-siblings), in § 6.2
- [tree](#concept-tree), in § 1.1
- [tree order](#concept-tree-order), in § 1.1
- [TreeWalker](#treewalker), in § 6.2
-  type 

  - [attribute for Event](#dom-event-type), in § 2.2
  - [attribute for MutationRecord](#dom-mutationrecord-type), in § 4.3.3
  - [dfn for Document](#concept-document-type), in § 4.5
  - [dfn for event listener](#event-listener-type), in § 2.7

- [TypeInfo](#typeinfo), in § 11
- [UNORDERED_NODE_ITERATOR_TYPE](#dom-xpathresult-unordered_node_iterator_type), in § 8.1
- [UNORDERED_NODE_SNAPSHOT_TYPE](#dom-xpathresult-unordered_node_snapshot_type), in § 8.1
- [update steps](#concept-dtl-update), in § 7.1
-  URL 

  - [attribute for Document](#dom-document-url), in § 4.5
  - [dfn for Document](#concept-document-url), in § 4.5

- [UserDataHandler](#userdatahandler), in § 11
- [valid](#staticrange-valid), in § 5.4
- [validate and extract](#validate-and-extract), in § 1.4
- [validation steps](#concept-domtokenlist-validation), in § 7.1
- [valid attribute local name](#valid-attribute-local-name), in § 1.4
- [valid doctype name](#valid-doctype-name), in § 1.4
- [valid element local name](#valid-element-local-name), in § 1.4
- [valid namespace prefix](#valid-namespace-prefix), in § 1.4
- [valid shadow host name](#valid-shadow-host-name), in § 4.9
-  value 

  - [attribute for Attr](#dom-attr-value), in § 4.9.2
  - [attribute for DOMTokenList](#dom-domtokenlist-value), in § 7.1
  - [dfn for Attr](#concept-attribute-value), in § 4.9.2

- [webkitMatchesSelector(selectors)](#dom-element-webkitmatchesselector), in § 4.9
-  whatToShow 

  - [attribute for NodeIterator](#dom-nodeiterator-whattoshow), in § 6.1
  - [attribute for TreeWalker](#dom-treewalker-whattoshow), in § 6.2
  - [dfn for traversal](#concept-traversal-whattoshow), in § 6

- [wholeText](#dom-text-wholetext), in § 4.11
- [XML document](#xml-document), in § 4.5
- [XMLDocument](#xmldocument), in § 4.5
- [xmlEncoding](#dom-document-xmlencoding), in § 11
- [xmlStandalone](#dom-document-xmlstandalone), in § 11
- [xmlVersion](#dom-document-xmlversion), in § 11
- [XPathEvaluator](#xpathevaluator), in § 8.4
- [XPathEvaluator()](#dom-xpathevaluator-xpathevaluator), in § 8.4
- [XPathEvaluatorBase](#xpathevaluatorbase), in § 8.3
- [XPathExpression](#xpathexpression), in § 8.2
- [XPathNSResolver](#callbackdef-xpathnsresolver), in § 8.3
- [XPathResult](#xpathresult), in § 8.1
- [XSLTProcessor](#xsltprocessor), in § 9.1
- [XSLTProcessor()](#dom-xsltprocessor-xsltprocessor), in § 9.1

### Terms defined by reference#index-defined-elsewhere

- [] defines the following terms: 

  - DeviceMotionEvent
  - DeviceOrientationEvent
  - TouchEvent
  - createContextualFragment()

- [CONSOLE] defines the following terms: 

  - report a warning to the console

- [CSSOM-VIEW] defines the following terms: 

  - getBoundingClientRect()
  - getClientRects()

- [ECMASCRIPT] defines the following terms: 

  - current realm
  - realm
  - surrounding agent

- [ENCODING] defines the following terms: 

  - encoding
  - name
  - UTF-8

- [HR-TIME-3] defines the following terms: 

  - DOMHighResTimeStamp
  - current high resolution time
  - relative high resolution coarse time

- [HTML] defines the following terms: 

  - BeforeUnloadEvent
  - CEReactions
  - CustomElementRegistry
  - DragEvent
  - EventHandler
  - HTMLAnchorElement
  - HTMLElement
  - HTMLHtmlElement
  - HTMLSlotElement
  - HTMLUnknownElement
  - HashChangeEvent
  - MessageEvent
  - StorageEvent
  - Window
  - active custom element constructor map
  - area
  - associated Document
  - browsing context
  - browsing context (for Document)
  - click()
  - constructor
  - current global object
  - custom element constructor
  - custom element definition
  - customized built-in element
  - disable shadow
  - document base URL
  - enqueue a custom element callback reaction
  - enqueue a custom element upgrade reaction
  - event handler
  - event handler event type
  - event handler IDL attribute
  - global object
  - head
  - html
  - HTML parser
  - in parallel
  - input
  - is scoped
  - local name
  - look up a custom element definition
  - look up a custom element registry
  - manually assigned nodes
  - microtask
  - name
  - opaque origin
  - origin
  - queue a global task
  - queue a microtask
  - relevant agent
  - relevant global object
  - relevant realm
  - report an exception
  - run steps after a timeout
  - scoped document set
  - script
  - similar-origin window agent
  - slot
  - style
  - template
  - the body element
  - timer task source
  - title
  - try to upgrade an element
  - upgrade an element
  - valid custom element name

- [INFRA] defines the following terms: 

  - append (for list)
  - append (for set)
  - ASCII alpha
  - ASCII case-insensitive
  - ASCII digit
  - ASCII lowercase
  - ASCII uppercase
  - ASCII whitespace
  - assert
  - break
  - clone
  - code point
  - code unit
  - concatenation
  - contain
  - continue
  - empty
  - enqueue
  - exist (for list)
  - exist (for map)
  - for each (for list)
  - for each (for map)
  - HTML namespace
  - identical to
  - insert
  - is empty
  - is not empty
  - length
  - list
  - map
  - ordered set
  - prepend
  - queue
  - remove (for list)
  - remove (for map)
  - replace (for list)
  - replace (for set)
  - set
  - set (for map)
  - size
  - split on ASCII whitespace
  - strictly split
  - string
  - struct
  - SVG namespace
  - tuple
  - XML namespace
  - XMLNS namespace

- [LONG-ANIMATION-FRAMES] defines the following terms: 

  - record timing info for event listener

- [SELECTORS4] defines the following terms: 

  - :defined
  - match a selector against a tree
  - match a selector against an element
  - parse a selector
  - scoping root

- [SERVICE-WORKERS] defines the following terms: 

  - ServiceWorkerGlobalScope
  - has ever been evaluated flag
  - script resource
  - service worker
  - service worker events
  - set of event types to handle

- [TRUSTED-TYPES] defines the following terms: 

  - TrustedType
  - get trusted type compliant attribute value

- [UIEVENTS] defines the following terms: 

  - CompositionEvent
  - FocusEvent
  - KeyboardEvent
  - MouseEvent
  - TextEvent
  - UIEvent
  - detail

- [URL] defines the following terms: 

  - URL
  - URL serializer

- [WEBIDL] defines the following terms: 

  - AbortError
  - DOMException
  - DOMString
  - EnforceRange
  - Exposed
  - HierarchyRequestError
  - InUseAttributeError
  - IndexSizeError
  - InvalidCharacterError
  - InvalidNodeTypeError
  - InvalidStateError
  - LegacyNullToEmptyString
  - LegacyUnenumerableNamedProperties
  - LegacyUnforgeable
  - NamespaceError
  - NewObject
  - NotFoundError
  - NotSupportedError
  - PutForwards
  - Replaceable
  - SameObject
  - SyntaxError
  - TimeoutError
  - USVString
  - Unscopable
  - WrongDocumentError
  - a new promise
  - any
  - associated realm
  - boolean
  - call a user object's operation
  - callback this value
  - construct
  - converted to an IDL value
  - dictionary
  - identifier
  - implements
  - invoke
  - new
  - primary interface
  - reject
  - resolve
  - sequence
  - short
  - supported property indices
  - supported property names
  - this
  - throw
  - undefined
  - unrestricted double
  - unsigned long
  - unsigned long long
  - unsigned short

- [XML] defines the following terms: 

  - Name

## References#references

### Normative References#normative

[CONSOLE] Dominic Farolino; Robert Kowalski; Terin Stock. [Console Standard](https://console.spec.whatwg.org/). Living Standard. URL: [https://console.spec.whatwg.org/](https://console.spec.whatwg.org/)[DEVICE-ORIENTATION] Reilly Grant; Marcos Caceres. [Device Orientation and Motion](https://w3c.github.io/deviceorientation/). URL: [https://w3c.github.io/deviceorientation/](https://w3c.github.io/deviceorientation/)[ECMASCRIPT] [ECMAScript Language Specification](https://tc39.es/ecma262/multipage/). URL: [https://tc39.es/ecma262/multipage/](https://tc39.es/ecma262/multipage/)[ENCODING] Anne van Kesteren. [Encoding Standard](https://encoding.spec.whatwg.org/). Living Standard. URL: [https://encoding.spec.whatwg.org/](https://encoding.spec.whatwg.org/)[HR-TIME-3] Yoav Weiss. [High Resolution Time](https://w3c.github.io/hr-time/). URL: [https://w3c.github.io/hr-time/](https://w3c.github.io/hr-time/)[HTML] Anne van Kesteren; et al. [HTML Standard](https://html.spec.whatwg.org/multipage/). Living Standard. URL: [https://html.spec.whatwg.org/multipage/](https://html.spec.whatwg.org/multipage/)[INFRA] Anne van Kesteren; Domenic Denicola. [Infra Standard](https://infra.spec.whatwg.org/). Living Standard. URL: [https://infra.spec.whatwg.org/](https://infra.spec.whatwg.org/)[LONG-ANIMATION-FRAMES] [Long Animation Frames API](https://w3c.github.io/long-animation-frames/). Editor's Draft. URL: [https://w3c.github.io/long-animation-frames/](https://w3c.github.io/long-animation-frames/)[SELECTORS4] Elika Etemad; Tab Atkins Jr.. [Selectors Level 4](https://drafts.csswg.org/selectors/). URL: [https://drafts.csswg.org/selectors/](https://drafts.csswg.org/selectors/)[SERVICE-WORKERS] Monica CHINTALA; Yoshisato Yanagisawa. [Service Workers Nightly](https://w3c.github.io/ServiceWorker/). URL: [https://w3c.github.io/ServiceWorker/](https://w3c.github.io/ServiceWorker/)[TOUCH-EVENTS] Doug Schepers; et al. [Touch Events](https://w3c.github.io/touch-events/). URL: [https://w3c.github.io/touch-events/](https://w3c.github.io/touch-events/)[TRUSTED-TYPES] Krzysztof Kotowicz. [Trusted Types](https://w3c.github.io/trusted-types/dist/spec/). URL: [https://w3c.github.io/trusted-types/dist/spec/](https://w3c.github.io/trusted-types/dist/spec/)[UIEVENTS] Gary Kacmarcik; Travis Leithead. [UI Events](https://w3c.github.io/uievents/). URL: [https://w3c.github.io/uievents/](https://w3c.github.io/uievents/)[URL] Anne van Kesteren. [URL Standard](https://url.spec.whatwg.org/). Living Standard. URL: [https://url.spec.whatwg.org/](https://url.spec.whatwg.org/)[WEBIDL] Edgar Chen; Timothy Gu. [Web IDL Standard](https://webidl.spec.whatwg.org/). Living Standard. URL: [https://webidl.spec.whatwg.org/](https://webidl.spec.whatwg.org/)[XML] Tim Bray; et al. [Extensible Markup Language (XML) 1.0 (Fifth Edition)](https://www.w3.org/TR/xml/). 26 November 2008. REC. URL: [https://www.w3.org/TR/xml/](https://www.w3.org/TR/xml/)[XML-NAMES] Tim Bray; et al. [Namespaces in XML 1.0 (Third Edition)](https://www.w3.org/TR/xml-names/). 8 December 2009. REC. URL: [https://www.w3.org/TR/xml-names/](https://www.w3.org/TR/xml-names/)

### Informative References#informative

[CSSOM-VIEW] Simon Fraser; Emilio Cobos Álvarez. [CSSOM View Module](https://drafts.csswg.org/cssom-view/). URL: [https://drafts.csswg.org/cssom-view/](https://drafts.csswg.org/cssom-view/)[DOM-Level-3-XPath] Ray Whitmer. [Document Object Model (DOM) Level 3 XPath Specification](https://www.w3.org/TR/DOM-Level-3-XPath/). 3 November 2020. NOTE. URL: [https://www.w3.org/TR/DOM-Level-3-XPath/](https://www.w3.org/TR/DOM-Level-3-XPath/)[DOM-Parsing] Travis Leithead. [DOM Parsing and Serialization](https://w3c.github.io/DOM-Parsing/). URL: [https://w3c.github.io/DOM-Parsing/](https://w3c.github.io/DOM-Parsing/)[FULLSCREEN] Philip Jägenstedt. [Fullscreen API Standard](https://fullscreen.spec.whatwg.org/). Living Standard. URL: [https://fullscreen.spec.whatwg.org/](https://fullscreen.spec.whatwg.org/)[INDEXEDDB] Nikunj Mehta; et al. [Indexed Database API](https://w3c.github.io/IndexedDB/). URL: [https://w3c.github.io/IndexedDB/](https://w3c.github.io/IndexedDB/)[XPath] James Clark; Steven DeRose. [XML Path Language (XPath) Version 1.0](https://www.w3.org/TR/xpath-10/). 16 November 1999. REC. URL: [https://www.w3.org/TR/xpath-10/](https://www.w3.org/TR/xpath-10/)[XSLT] James Clark. [XSL Transformations (XSLT) Version 1.0](https://www.w3.org/TR/xslt-10/). 16 November 1999. REC. URL: [https://www.w3.org/TR/xslt-10/](https://www.w3.org/TR/xslt-10/)

## IDL Index#idl-index

```
[Exposed=*]
interface Event#event {
  constructor#dom-event-event(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString type#dom-event-event-type-eventinitdict-type, optional EventInit#dictdef-eventinit eventInitDict#dom-event-event-type-eventinitdict-eventinitdict = {});

  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString type#dom-event-type;
  readonly attribute EventTarget#eventtarget? target#dom-event-target;
  readonly attribute EventTarget#eventtarget? srcElement#dom-event-srcelement; // legacy
  readonly attribute EventTarget#eventtarget? currentTarget#dom-event-currenttarget;
  sequencehttps://webidl.spec.whatwg.org/#idl-sequence<EventTarget#eventtarget> composedPath#dom-event-composedpath();

  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short NONE#dom-event-none = 0;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short CAPTURING_PHASE#dom-event-capturing_phase = 1;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short AT_TARGET#dom-event-at_target = 2;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short BUBBLING_PHASE#dom-event-bubbling_phase = 3;
  readonly attribute unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short eventPhase#dom-event-eventphase;

  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined stopPropagation#dom-event-stoppropagation();
           attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean cancelBubble#dom-event-cancelbubble; // legacy alias of .stopPropagation()
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined stopImmediatePropagation#dom-event-stopimmediatepropagation();

  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean bubbles#dom-event-bubbles;
  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean cancelable#dom-event-cancelable;
           attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean returnValue#dom-event-returnvalue;  // legacy
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined preventDefault#dom-event-preventdefault();
  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean defaultPrevented#dom-event-defaultprevented;
  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean composed#dom-event-composed;

  [LegacyUnforgeablehttps://webidl.spec.whatwg.org/#LegacyUnforgeable] readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean isTrusted#dom-event-istrusted;
  readonly attribute DOMHighResTimeStamphttps://w3c.github.io/hr-time/#dom-domhighrestimestamp timeStamp#dom-event-timestamp;

  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined initEvent#dom-event-initevent(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString type#dom-event-initevent-type-bubbles-cancelable-type, optional booleanhttps://webidl.spec.whatwg.org/#idl-boolean bubbles#dom-event-initevent-type-bubbles-cancelable-bubbles = false, optional booleanhttps://webidl.spec.whatwg.org/#idl-boolean cancelable#dom-event-initevent-type-bubbles-cancelable-cancelable = false); // legacy
};

dictionary EventInit#dictdef-eventinit {
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean bubbles#dom-eventinit-bubbles = false;
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean cancelable#dom-eventinit-cancelable = false;
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean composed#dom-eventinit-composed = false;
};

partial interface Windowhttps://html.spec.whatwg.org/multipage/nav-history-apis.html#window {
  [Replaceablehttps://webidl.spec.whatwg.org/#Replaceable] readonly attribute (Event#event or undefinedhttps://webidl.spec.whatwg.org/#idl-undefined) event#dom-window-event; // legacy
};

[Exposed=*]
interface CustomEvent#customevent : Event#event {
  constructor#dom-customevent-customevent(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString type#dom-customevent-customevent-type-eventinitdict-type, optional CustomEventInit#dictdef-customeventinit eventInitDict#dom-customevent-customevent-type-eventinitdict-eventinitdict = {});

  readonly attribute anyhttps://webidl.spec.whatwg.org/#idl-any detail#dom-customevent-detail;

  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined initCustomEvent#dom-customevent-initcustomevent(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString type#dom-customevent-initcustomevent-type-bubbles-cancelable-detail-type, optional booleanhttps://webidl.spec.whatwg.org/#idl-boolean bubbles#dom-customevent-initcustomevent-type-bubbles-cancelable-detail-bubbles = false, optional booleanhttps://webidl.spec.whatwg.org/#idl-boolean cancelable#dom-customevent-initcustomevent-type-bubbles-cancelable-detail-cancelable = false, optional anyhttps://webidl.spec.whatwg.org/#idl-any detail#dom-customevent-initcustomevent-type-bubbles-cancelable-detail-detail = null); // legacy
};

dictionary CustomEventInit#dictdef-customeventinit : EventInit#dictdef-eventinit {
  anyhttps://webidl.spec.whatwg.org/#idl-any detail#dom-customeventinit-detail = null;
};

[Exposed=*]
interface EventTarget#eventtarget {
  constructor#dom-eventtarget-eventtarget();

  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined addEventListener#dom-eventtarget-addeventlistener(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString type#dom-eventtarget-addeventlistener-type-callback-options-type, EventListener#callbackdef-eventlistener? callback#dom-eventtarget-addeventlistener-type-callback-options-callback, optional (AddEventListenerOptions#dictdef-addeventlisteneroptions or booleanhttps://webidl.spec.whatwg.org/#idl-boolean) options#dom-eventtarget-addeventlistener-type-callback-options-options = {});
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined removeEventListener#dom-eventtarget-removeeventlistener(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString type#dom-eventtarget-removeeventlistener-type-callback-options-type, EventListener#callbackdef-eventlistener? callback#dom-eventtarget-removeeventlistener-type-callback-options-callback, optional (EventListenerOptions#dictdef-eventlisteneroptions or booleanhttps://webidl.spec.whatwg.org/#idl-boolean) options#dom-eventtarget-removeeventlistener-type-callback-options-options = {});
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean dispatchEvent#dom-eventtarget-dispatchevent(Event#event event#dom-eventtarget-dispatchevent-event-event);
};

callback interface EventListener#callbackdef-eventlistener {
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined handleEvent#dom-eventlistener-handleevent(Event#event event#dom-eventlistener-handleevent-event-event);
};

dictionary EventListenerOptions#dictdef-eventlisteneroptions {
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean capture#dom-eventlisteneroptions-capture = false;
};

dictionary AddEventListenerOptions#dictdef-addeventlisteneroptions : EventListenerOptions#dictdef-eventlisteneroptions {
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean passive#dom-addeventlisteneroptions-passive;
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean once#dom-addeventlisteneroptions-once = false;
  AbortSignal#abortsignal signal#dom-addeventlisteneroptions-signal;
};

[Exposed=*]
interface AbortController#abortcontroller {
  constructor#dom-abortcontroller-abortcontroller();

  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute AbortSignal#abortsignal signal#dom-abortcontroller-signal;

  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined abort#dom-abortcontroller-abort(optional anyhttps://webidl.spec.whatwg.org/#idl-any reason#dom-abortcontroller-abort-reason-reason);
};

[Exposed=*]
interface AbortSignal#abortsignal : EventTarget#eventtarget {
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] static AbortSignal#abortsignal abort#dom-abortsignal-abort(optional anyhttps://webidl.spec.whatwg.org/#idl-any reason#dom-abortsignal-abort-reason-reason);
  [Exposedhttps://webidl.spec.whatwg.org/#Exposed=(Window,Worker), NewObjecthttps://webidl.spec.whatwg.org/#NewObject] static AbortSignal#abortsignal timeout#dom-abortsignal-timeout([EnforceRangehttps://webidl.spec.whatwg.org/#EnforceRange] unsigned long longhttps://webidl.spec.whatwg.org/#idl-unsigned-long-long milliseconds#dom-abortsignal-timeout-milliseconds-milliseconds);
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] static AbortSignal#abortsignal _any#dom-abortsignal-any(sequencehttps://webidl.spec.whatwg.org/#idl-sequence<AbortSignal#abortsignal> signals#dom-abortsignal-any-signals-signals);

  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean aborted#dom-abortsignal-aborted;
  readonly attribute anyhttps://webidl.spec.whatwg.org/#idl-any reason#dom-abortsignal-reason;
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined throwIfAborted#dom-abortsignal-throwifaborted();

  attribute EventHandlerhttps://html.spec.whatwg.org/multipage/webappapis.html#eventhandler onabort#dom-abortsignal-onabort;
};
interface mixin NonElementParentNode#nonelementparentnode {
  Element#element? getElementById#dom-nonelementparentnode-getelementbyid(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString elementId#dom-nonelementparentnode-getelementbyid-elementid-elementid);
};
Document#document includes NonElementParentNode#nonelementparentnode;
DocumentFragment#documentfragment includes NonElementParentNode#nonelementparentnode;

interface mixin DocumentOrShadowRoot#documentorshadowroot {
  readonly attribute CustomElementRegistryhttps://html.spec.whatwg.org/multipage/custom-elements.html#customelementregistry? customElementRegistry#dom-documentorshadowroot-customelementregistry;
};
Document#document includes DocumentOrShadowRoot#documentorshadowroot;
ShadowRoot#shadowroot includes DocumentOrShadowRoot#documentorshadowroot;

interface mixin ParentNode#parentnode {
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute HTMLCollection#htmlcollection children#dom-parentnode-children;
  readonly attribute Element#element? firstElementChild#dom-parentnode-firstelementchild;
  readonly attribute Element#element? lastElementChild#dom-parentnode-lastelementchild;
  readonly attribute unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long childElementCount#dom-parentnode-childelementcount;

  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, Unscopablehttps://webidl.spec.whatwg.org/#Unscopable] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined prepend#dom-parentnode-prepend((Node#node or DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString)... nodes#dom-parentnode-prepend-nodes-nodes);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, Unscopablehttps://webidl.spec.whatwg.org/#Unscopable] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined append#dom-parentnode-append((Node#node or DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString)... nodes#dom-parentnode-append-nodes-nodes);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, Unscopablehttps://webidl.spec.whatwg.org/#Unscopable] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined replaceChildren#dom-parentnode-replacechildren((Node#node or DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString)... nodes#dom-parentnode-replacechildren-nodes-nodes);

  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined moveBefore#dom-parentnode-movebefore(Node#node node#dom-parentnode-movebefore-node-child-node, Node#node? child#dom-parentnode-movebefore-node-child-child);

  Element#element? querySelector#dom-parentnode-queryselector(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString selectors#dom-parentnode-queryselector-selectors-selectors);
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] NodeList#nodelist querySelectorAll#dom-parentnode-queryselectorall(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString selectors#dom-parentnode-queryselectorall-selectors-selectors);
};
Document#document includes ParentNode#parentnode;
DocumentFragment#documentfragment includes ParentNode#parentnode;
Element#element includes ParentNode#parentnode;

interface mixin NonDocumentTypeChildNode#nondocumenttypechildnode {
  readonly attribute Element#element? previousElementSibling#dom-nondocumenttypechildnode-previouselementsibling;
  readonly attribute Element#element? nextElementSibling#dom-nondocumenttypechildnode-nextelementsibling;
};
Element#element includes NonDocumentTypeChildNode#nondocumenttypechildnode;
CharacterData#characterdata includes NonDocumentTypeChildNode#nondocumenttypechildnode;

interface mixin ChildNode#childnode {
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, Unscopablehttps://webidl.spec.whatwg.org/#Unscopable] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined before#dom-childnode-before((Node#node or DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString)... nodes#dom-childnode-before-nodes-nodes);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, Unscopablehttps://webidl.spec.whatwg.org/#Unscopable] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined after#dom-childnode-after((Node#node or DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString)... nodes#dom-childnode-after-nodes-nodes);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, Unscopablehttps://webidl.spec.whatwg.org/#Unscopable] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined replaceWith#dom-childnode-replacewith((Node#node or DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString)... nodes#dom-childnode-replacewith-nodes-nodes);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, Unscopablehttps://webidl.spec.whatwg.org/#Unscopable] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined remove#dom-childnode-remove();
};
DocumentType#documenttype includes ChildNode#childnode;
Element#element includes ChildNode#childnode;
CharacterData#characterdata includes ChildNode#childnode;

interface mixin Slottable#slotable {
  readonly attribute HTMLSlotElementhttps://html.spec.whatwg.org/multipage/scripting.html#htmlslotelement? assignedSlot#dom-slotable-assignedslot;
};
Element#element includes Slottable#slotable;
Text#text includes Slottable#slotable;

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface NodeList#nodelist {
  getter Node#node? item#dom-nodelist-item(unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long index#dom-nodelist-item-index-index);
  readonly attribute unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long length#dom-nodelist-length;
  iterable<Node#node>;
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window, LegacyUnenumerableNamedPropertieshttps://webidl.spec.whatwg.org/#LegacyUnenumerableNamedProperties]
interface HTMLCollection#htmlcollection {
  readonly attribute unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long length#dom-htmlcollection-length;
  getter Element#element? item#dom-htmlcollection-item(unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long index#dom-htmlcollection-item-index-index);
  getter Element#element? namedItem#dom-htmlcollection-nameditem(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString name#dom-htmlcollection-nameditem-name-name);
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface MutationObserver#mutationobserver {
  constructor#dom-mutationobserver-mutationobserver(MutationCallback#callbackdef-mutationcallback callback#dom-mutationobserver-mutationobserver-callback-callback);

  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined observe#dom-mutationobserver-observe(Node#node target#dom-mutationobserver-observe-target-options-target, optional MutationObserverInit#dictdef-mutationobserverinit options#dom-mutationobserver-observe-target-options-options = {});
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined disconnect#dom-mutationobserver-disconnect();
  sequencehttps://webidl.spec.whatwg.org/#idl-sequence<MutationRecord#mutationrecord> takeRecords#dom-mutationobserver-takerecords();
};

callback MutationCallback#callbackdef-mutationcallback = undefinedhttps://webidl.spec.whatwg.org/#idl-undefined (sequencehttps://webidl.spec.whatwg.org/#idl-sequence<MutationRecord#mutationrecord> mutations#dom-mutationcallback-mutations, MutationObserver#mutationobserver observer#dom-mutationcallback-observer);

dictionary MutationObserverInit#dictdef-mutationobserverinit {
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean childList#dom-mutationobserverinit-childlist = false;
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean attributes#dom-mutationobserverinit-attributes;
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean characterData#dom-mutationobserverinit-characterdata;
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean subtree#dom-mutationobserverinit-subtree = false;
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean attributeOldValue#dom-mutationobserverinit-attributeoldvalue;
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean characterDataOldValue#dom-mutationobserverinit-characterdataoldvalue;
  sequencehttps://webidl.spec.whatwg.org/#idl-sequence<DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString> attributeFilter#dom-mutationobserverinit-attributefilter;
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface MutationRecord#mutationrecord {
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString type#dom-mutationrecord-type;
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute Node#node target#dom-mutationrecord-target;
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute NodeList#nodelist addedNodes#dom-mutationrecord-addednodes;
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute NodeList#nodelist removedNodes#dom-mutationrecord-removednodes;
  readonly attribute Node#node? previousSibling#dom-mutationrecord-previoussibling;
  readonly attribute Node#node? nextSibling#dom-mutationrecord-nextsibling;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? attributeName#dom-mutationrecord-attributename;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? attributeNamespace#dom-mutationrecord-attributenamespace;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? oldValue#dom-mutationrecord-oldvalue;
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface Node#node : EventTarget#eventtarget {
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short ELEMENT_NODE#dom-node-element_node = 1;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short ATTRIBUTE_NODE#dom-node-attribute_node = 2;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short TEXT_NODE#dom-node-text_node = 3;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short CDATA_SECTION_NODE#dom-node-cdata_section_node = 4;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short ENTITY_REFERENCE_NODE#dom-node-entity_reference_node = 5; // legacy
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short ENTITY_NODE#dom-node-entity_node = 6; // legacy
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short PROCESSING_INSTRUCTION_NODE#dom-node-processing_instruction_node = 7;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short COMMENT_NODE#dom-node-comment_node = 8;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short DOCUMENT_NODE#dom-node-document_node = 9;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short DOCUMENT_TYPE_NODE#dom-node-document_type_node = 10;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short DOCUMENT_FRAGMENT_NODE#dom-node-document_fragment_node = 11;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short NOTATION_NODE#dom-node-notation_node = 12; // legacy
  readonly attribute unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short nodeType#dom-node-nodetype;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString nodeName#dom-node-nodename;

  readonly attribute USVStringhttps://webidl.spec.whatwg.org/#idl-USVString baseURI#dom-node-baseuri;

  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean isConnected#dom-node-isconnected;
  readonly attribute Document#document? ownerDocument#dom-node-ownerdocument;
  Node#node getRootNode#dom-node-getrootnode(optional GetRootNodeOptions#dictdef-getrootnodeoptions options#dom-node-getrootnode-options-options = {});
  readonly attribute Node#node? parentNode#dom-node-parentnode;
  readonly attribute Element#element? parentElement#dom-node-parentelement;
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean hasChildNodes#dom-node-haschildnodes();
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute NodeList#nodelist childNodes#dom-node-childnodes;
  readonly attribute Node#node? firstChild#dom-node-firstchild;
  readonly attribute Node#node? lastChild#dom-node-lastchild;
  readonly attribute Node#node? previousSibling#dom-node-previoussibling;
  readonly attribute Node#node? nextSibling#dom-node-nextsibling;

  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? nodeValue#dom-node-nodevalue;
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? textContent#dom-node-textcontent;
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined normalize#dom-node-normalize();

  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, NewObjecthttps://webidl.spec.whatwg.org/#NewObject] Node#node cloneNode#dom-node-clonenode(optional booleanhttps://webidl.spec.whatwg.org/#idl-boolean subtree#dom-node-clonenode-subtree-subtree = false);
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean isEqualNode#dom-node-isequalnode(Node#node? otherNode#dom-node-isequalnode-othernode-othernode);
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean isSameNode#dom-node-issamenode(Node#node? otherNode#dom-node-issamenode-othernode-othernode); // legacy alias of ===

  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short DOCUMENT_POSITION_DISCONNECTED#dom-node-document_position_disconnected = 0x01;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short DOCUMENT_POSITION_PRECEDING#dom-node-document_position_preceding = 0x02;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short DOCUMENT_POSITION_FOLLOWING#dom-node-document_position_following = 0x04;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short DOCUMENT_POSITION_CONTAINS#dom-node-document_position_contains = 0x08;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short DOCUMENT_POSITION_CONTAINED_BY#dom-node-document_position_contained_by = 0x10;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC#dom-node-document_position_implementation_specific = 0x20;
  unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short compareDocumentPosition#dom-node-comparedocumentposition(Node#node other#dom-node-comparedocumentposition-other-other);
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean contains#dom-node-contains(Node#node? other#dom-node-contains-other-other);

  DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? lookupPrefix#dom-node-lookupprefix(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace#dom-node-lookupprefix-namespace-namespace);
  DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? lookupNamespaceURI#dom-node-lookupnamespaceuri(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? prefix#dom-node-lookupnamespaceuri-prefix-prefix);
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean isDefaultNamespace#dom-node-isdefaultnamespace(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace#dom-node-isdefaultnamespace-namespace-namespace);

  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Node#node insertBefore#dom-node-insertbefore(Node#node node#dom-node-insertbefore-node-child-node, Node#node? child#dom-node-insertbefore-node-child-child);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Node#node appendChild#dom-node-appendchild(Node#node node#dom-node-appendchild-node-node);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Node#node replaceChild#dom-node-replacechild(Node#node node#dom-node-replacechild-node-child-node, Node#node child#dom-node-replacechild-node-child-child);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Node#node removeChild#dom-node-removechild(Node#node child#dom-node-removechild-child-child);
};

dictionary GetRootNodeOptions#dictdef-getrootnodeoptions {
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean composed#dom-getrootnodeoptions-composed = false;
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface Document#document : Node#node {
  constructor#dom-document-document();

  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute DOMImplementation#domimplementation implementation#dom-document-implementation;
  readonly attribute USVStringhttps://webidl.spec.whatwg.org/#idl-USVString URL#dom-document-url;
  readonly attribute USVStringhttps://webidl.spec.whatwg.org/#idl-USVString documentURI#dom-document-documenturi;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString compatMode#dom-document-compatmode;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString characterSet#dom-document-characterset;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString charset#dom-document-charset; // legacy alias of .characterSet
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString inputEncoding#dom-document-inputencoding; // legacy alias of .characterSet
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString contentType#dom-document-contenttype;

  readonly attribute DocumentType#documenttype? doctype#dom-document-doctype;
  readonly attribute Element#element? documentElement#dom-document-documentelement;
  HTMLCollection#htmlcollection getElementsByTagName#dom-document-getelementsbytagname(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName#dom-document-getelementsbytagname-qualifiedname-qualifiedname);
  HTMLCollection#htmlcollection getElementsByTagNameNS#dom-document-getelementsbytagnamens(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace#dom-document-getelementsbytagnamens-namespace-localname-namespace, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName#dom-document-getelementsbytagnamens-namespace-localname-localname);
  HTMLCollection#htmlcollection getElementsByClassName#dom-document-getelementsbyclassname(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString classNames#dom-document-getelementsbyclassname-classnames-classnames);

  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, NewObjecthttps://webidl.spec.whatwg.org/#NewObject] Element#element createElement#dom-document-createelement(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName#dom-document-createelement-localname-options-localname, optional (DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString or ElementCreationOptions#dictdef-elementcreationoptions) options#dom-document-createelement-localname-options-options = {});
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, NewObjecthttps://webidl.spec.whatwg.org/#NewObject] Element#element createElementNS#dom-document-createelementns(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace#dom-document-createelementns-namespace-qualifiedname-options-namespace, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName#dom-document-createelementns-namespace-qualifiedname-options-qualifiedname, optional (DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString or ElementCreationOptions#dictdef-elementcreationoptions) options#dom-document-createelementns-namespace-qualifiedname-options-options = {});
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] DocumentFragment#documentfragment createDocumentFragment#dom-document-createdocumentfragment();
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] Text#text createTextNode#dom-document-createtextnode(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString data#dom-document-createtextnode-data-data);
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] CDATASection#cdatasection createCDATASection#dom-document-createcdatasection(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString data#dom-document-createcdatasection-data-data);
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] Comment#comment createComment#dom-document-createcomment(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString data#dom-document-createcomment-data-data);
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] ProcessingInstruction#processinginstruction createProcessingInstruction#dom-document-createprocessinginstruction(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString target#dom-document-createprocessinginstruction-target-data-target, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString data#dom-document-createprocessinginstruction-target-data-data);

  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, NewObjecthttps://webidl.spec.whatwg.org/#NewObject] Node#node importNode#dom-document-importnode(Node#node node#dom-document-importnode-node-options-node, optional (booleanhttps://webidl.spec.whatwg.org/#idl-boolean or ImportNodeOptions#dictdef-importnodeoptions) options#dom-document-importnode-node-options-options = false);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Node#node adoptNode#dom-document-adoptnode(Node#node node#dom-document-adoptnode-node-node);

  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] Attr#attr createAttribute#dom-document-createattribute(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName#dom-document-createattribute-localname-localname);
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] Attr#attr createAttributeNS#dom-document-createattributens(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace#dom-document-createattributens-namespace-qualifiedname-namespace, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName#dom-document-createattributens-namespace-qualifiedname-qualifiedname);

  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] Event#event createEvent#dom-document-createevent(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString interface#dom-document-createevent-interface-interface); // legacy

  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] Range#range createRange#dom-document-createrange();

  // NodeFilter.SHOW_ALL = 0xFFFFFFFF
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] NodeIterator#nodeiterator createNodeIterator#dom-document-createnodeiterator(Node#node root#dom-document-createnodeiterator-root-whattoshow-filter-root, optional unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long whatToShow#dom-document-createnodeiterator-root-whattoshow-filter-whattoshow = 0xFFFFFFFF, optional NodeFilter#callbackdef-nodefilter? filter#dom-document-createnodeiterator-root-whattoshow-filter-filter = null);
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] TreeWalker#treewalker createTreeWalker#dom-document-createtreewalker(Node#node root#dom-document-createtreewalker-root-whattoshow-filter-root, optional unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long whatToShow#dom-document-createtreewalker-root-whattoshow-filter-whattoshow = 0xFFFFFFFF, optional NodeFilter#callbackdef-nodefilter? filter#dom-document-createtreewalker-root-whattoshow-filter-filter = null);
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface XMLDocument#xmldocument : Document#document {};

dictionary ElementCreationOptions#dictdef-elementcreationoptions {
  CustomElementRegistryhttps://html.spec.whatwg.org/multipage/custom-elements.html#customelementregistry? customElementRegistry#dom-elementcreationoptions-customelementregistry;
  DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString is#dom-elementcreationoptions-is;
};

dictionary ImportNodeOptions#dictdef-importnodeoptions {
  CustomElementRegistryhttps://html.spec.whatwg.org/multipage/custom-elements.html#customelementregistry customElementRegistry#dom-importnodeoptions-customelementregistry;
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean selfOnly#dom-importnodeoptions-selfonly = false;
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface DOMImplementation#domimplementation {
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] DocumentType#documenttype createDocumentType#dom-domimplementation-createdocumenttype(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString name#dom-domimplementation-createdocumenttype-name-publicid-systemid-name, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString publicId#dom-domimplementation-createdocumenttype-name-publicid-systemid-publicid, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString systemId#dom-domimplementation-createdocumenttype-name-publicid-systemid-systemid);
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] XMLDocument#xmldocument createDocument#dom-domimplementation-createdocument(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace#dom-domimplementation-createdocument-namespace-qualifiedname-doctype-namespace, [LegacyNullToEmptyStringhttps://webidl.spec.whatwg.org/#LegacyNullToEmptyString] DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName#dom-domimplementation-createdocument-namespace-qualifiedname-doctype-qualifiedname, optional DocumentType#documenttype? doctype#dom-domimplementation-createdocument-namespace-qualifiedname-doctype-doctype = null);
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] Document#document createHTMLDocument#dom-domimplementation-createhtmldocument(optional DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString title#dom-domimplementation-createhtmldocument-title-title);

  booleanhttps://webidl.spec.whatwg.org/#idl-boolean hasFeature#dom-domimplementation-hasfeature(); // useless; always returns true
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface DocumentType#documenttype : Node#node {
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString name#dom-documenttype-name;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString publicId#dom-documenttype-publicid;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString systemId#dom-documenttype-systemid;
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface DocumentFragment#documentfragment : Node#node {
  constructor#dom-documentfragment-documentfragment();
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface ShadowRoot#shadowroot : DocumentFragment#documentfragment {
  readonly attribute ShadowRootMode#enumdef-shadowrootmode mode#dom-shadowroot-mode;
  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean delegatesFocus#dom-shadowroot-delegatesfocus;
  readonly attribute SlotAssignmentMode#enumdef-slotassignmentmode slotAssignment#dom-shadowroot-slotassignment;
  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean clonable#dom-shadowroot-clonable;
  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean serializable#dom-shadowroot-serializable;
  readonly attribute Element#element host#dom-shadowroot-host;

  attribute EventHandlerhttps://html.spec.whatwg.org/multipage/webappapis.html#eventhandler onslotchange#dom-shadowroot-onslotchange;
};

enum ShadowRootMode#enumdef-shadowrootmode { "open"#dom-shadowrootmode-open, "closed"#dom-shadowrootmode-closed };
enum SlotAssignmentMode#enumdef-slotassignmentmode { "manual"#dom-slotassignmentmode-manual, "named"#dom-slotassignmentmode-named };

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface Element#element : Node#node {
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespaceURI#dom-element-namespaceuri;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? prefix#dom-element-prefix;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName#dom-element-localname;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString tagName#dom-element-tagname;

  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString id#dom-element-id;
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString className#dom-element-classname;
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject, PutForwardshttps://webidl.spec.whatwg.org/#PutForwards=value#dom-domtokenlist-value] readonly attribute DOMTokenList#domtokenlist classList#dom-element-classlist;
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, Unscopablehttps://webidl.spec.whatwg.org/#Unscopable] attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString slot#dom-element-slot;

  booleanhttps://webidl.spec.whatwg.org/#idl-boolean hasAttributes#dom-element-hasattributes();
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute NamedNodeMap#namednodemap attributes#dom-element-attributes;
  sequencehttps://webidl.spec.whatwg.org/#idl-sequence<DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString> getAttributeNames#dom-element-getattributenames();
  DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? getAttribute#dom-element-getattribute(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName#dom-element-getattribute-qualifiedname-qualifiedname);
  DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? getAttributeNS#dom-element-getattributens(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace#dom-element-getattributens-namespace-localname-namespace, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName#dom-element-getattributens-namespace-localname-localname);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined setAttribute#dom-element-setattribute(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName#dom-element-setattribute-qualifiedname-value-qualifiedname, (TrustedTypehttps://w3c.github.io/trusted-types/dist/spec/#typedefdef-trustedtype or DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString) value#dom-element-setattribute-qualifiedname-value-value);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined setAttributeNS#dom-element-setattributens(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace#dom-element-setattributens-namespace-qualifiedname-value-namespace, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName#dom-element-setattributens-namespace-qualifiedname-value-qualifiedname, (TrustedTypehttps://w3c.github.io/trusted-types/dist/spec/#typedefdef-trustedtype or DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString) value#dom-element-setattributens-namespace-qualifiedname-value-value);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined removeAttribute#dom-element-removeattribute(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName#dom-element-removeattribute-qualifiedname-qualifiedname);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined removeAttributeNS#dom-element-removeattributens(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace#dom-element-removeattributens-namespace-localname-namespace, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName#dom-element-removeattributens-namespace-localname-localname);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] booleanhttps://webidl.spec.whatwg.org/#idl-boolean toggleAttribute#dom-element-toggleattribute(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName#dom-element-toggleattribute-qualifiedname-force-qualifiedname, optional booleanhttps://webidl.spec.whatwg.org/#idl-boolean force#dom-element-toggleattribute-qualifiedname-force-force);
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean hasAttribute#dom-element-hasattribute(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName#dom-element-hasattribute-qualifiedname-qualifiedname);
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean hasAttributeNS#dom-element-hasattributens(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace#dom-element-hasattributens-namespace-localname-namespace, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName#dom-element-hasattributens-namespace-localname-localname);

  Attr#attr? getAttributeNode#dom-element-getattributenode(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName#dom-element-getattributenode-qualifiedname-qualifiedname);
  Attr#attr? getAttributeNodeNS#dom-element-getattributenodens(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace#dom-element-getattributenodens-namespace-localname-namespace, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName#dom-element-getattributenodens-namespace-localname-localname);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Attr#attr? setAttributeNode#dom-element-setattributenode(Attr#attr attr#dom-element-setattributenode-attr-attr);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Attr#attr? setAttributeNodeNS#dom-element-setattributenodens(Attr#attr attr#dom-element-setattributenodens-attr-attr);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Attr#attr removeAttributeNode#dom-element-removeattributenode(Attr#attr attr#dom-element-removeattributenode-attr-attr);

  ShadowRoot#shadowroot attachShadow#dom-element-attachshadow(ShadowRootInit#dictdef-shadowrootinit init#dom-element-attachshadow-init-init);
  readonly attribute ShadowRoot#shadowroot? shadowRoot#dom-element-shadowroot;

  readonly attribute CustomElementRegistryhttps://html.spec.whatwg.org/multipage/custom-elements.html#customelementregistry? customElementRegistry#dom-element-customelementregistry;

  Element#element? closest#dom-element-closest(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString selectors#dom-element-closest-selectors-selectors);
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean matches#dom-element-matches(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString selectors#dom-element-matches-selectors-selectors);
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean webkitMatchesSelector#dom-element-webkitmatchesselector(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString selectors#dom-element-webkitmatchesselector-selectors-selectors); // legacy alias of .matches

  HTMLCollection#htmlcollection getElementsByTagName#dom-element-getelementsbytagname(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName#dom-element-getelementsbytagname-qualifiedname-qualifiedname);
  HTMLCollection#htmlcollection getElementsByTagNameNS#dom-element-getelementsbytagnamens(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace#dom-element-getelementsbytagnamens-namespace-localname-namespace, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName#dom-element-getelementsbytagnamens-namespace-localname-localname);
  HTMLCollection#htmlcollection getElementsByClassName#dom-element-getelementsbyclassname(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString classNames#dom-element-getelementsbyclassname-classnames-classnames);

  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Element#element? insertAdjacentElement#dom-element-insertadjacentelement(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString where#dom-element-insertadjacentelement-where-element-where, Element#element element#dom-element-insertadjacentelement-where-element-element); // legacy
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined insertAdjacentText#dom-element-insertadjacenttext(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString where#dom-element-insertadjacenttext-where-data-where, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString data#dom-element-insertadjacenttext-where-data-data); // legacy
};

dictionary ShadowRootInit#dictdef-shadowrootinit {
  required ShadowRootMode#enumdef-shadowrootmode mode#dom-shadowrootinit-mode;
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean delegatesFocus#dom-shadowrootinit-delegatesfocus = false;
  SlotAssignmentMode#enumdef-slotassignmentmode slotAssignment#dom-shadowrootinit-slotassignment = "named";
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean clonable#dom-shadowrootinit-clonable = false;
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean serializable#dom-shadowrootinit-serializable = false;
  CustomElementRegistryhttps://html.spec.whatwg.org/multipage/custom-elements.html#customelementregistry? customElementRegistry#dom-shadowrootinit-customelementregistry;
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window,
 LegacyUnenumerableNamedPropertieshttps://webidl.spec.whatwg.org/#LegacyUnenumerableNamedProperties]
interface NamedNodeMap#namednodemap {
  readonly attribute unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long length#dom-namednodemap-length;
  getter Attr#attr? item#dom-namednodemap-item(unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long index#dom-namednodemap-item-index-index);
  getter Attr#attr? getNamedItem#dom-namednodemap-getnameditem(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName#dom-namednodemap-getnameditem-qualifiedname-qualifiedname);
  Attr#attr? getNamedItemNS#dom-namednodemap-getnameditemns(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace#dom-namednodemap-getnameditemns-namespace-localname-namespace, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName#dom-namednodemap-getnameditemns-namespace-localname-localname);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Attr#attr? setNamedItem#dom-namednodemap-setnameditem(Attr#attr attr#dom-namednodemap-setnameditem-attr-attr);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Attr#attr? setNamedItemNS#dom-namednodemap-setnameditemns(Attr#attr attr#dom-namednodemap-setnameditemns-attr-attr);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Attr#attr removeNamedItem#dom-namednodemap-removenameditem(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString qualifiedName#dom-namednodemap-removenameditem-qualifiedname-qualifiedname);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Attr#attr removeNamedItemNS#dom-namednodemap-removenameditemns(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespace#dom-namednodemap-removenameditemns-namespace-localname-namespace, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName#dom-namednodemap-removenameditemns-namespace-localname-localname);
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface Attr#attr : Node#node {
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? namespaceURI#dom-attr-namespaceuri;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? prefix#dom-attr-prefix;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName#dom-attr-localname;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString name#dom-attr-name;
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString value#dom-attr-value;

  readonly attribute Element#element? ownerElement#dom-attr-ownerelement;

  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean specified#dom-attr-specified; // useless; always returns true
};
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface CharacterData#characterdata : Node#node {
  attribute [LegacyNullToEmptyStringhttps://webidl.spec.whatwg.org/#LegacyNullToEmptyString] DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString data#dom-characterdata-data;
  readonly attribute unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long length#dom-characterdata-length;
  DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString substringData#dom-characterdata-substringdata(unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long offset#dom-characterdata-substringdata-offset-count-offset, unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long count#dom-characterdata-substringdata-offset-count-count);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined appendData#dom-characterdata-appenddata(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString data#dom-characterdata-appenddata-data-data);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined insertData#dom-characterdata-insertdata(unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long offset#dom-characterdata-insertdata-offset-data-offset, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString data#dom-characterdata-insertdata-offset-data-data);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined deleteData#dom-characterdata-deletedata(unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long offset#dom-characterdata-deletedata-offset-count-offset, unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long count#dom-characterdata-deletedata-offset-count-count);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined replaceData#dom-characterdata-replacedata(unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long offset#dom-characterdata-replacedata-offset-count-data-offset, unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long count#dom-characterdata-replacedata-offset-count-data-count, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString data#dom-characterdata-replacedata-offset-count-data-data);
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface Text#text : CharacterData#characterdata {
  constructor#dom-text-text(optional DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString data#dom-text-text-data-data = "");

  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] Text#text splitText#dom-text-splittext(unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long offset#dom-text-splittext-offset-offset);
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString wholeText#dom-text-wholetext;
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface CDATASection#cdatasection : Text#text {
};
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface ProcessingInstruction#processinginstruction : CharacterData#characterdata {
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString target#dom-processinginstruction-target;
};
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface Comment#comment : CharacterData#characterdata {
  constructor#dom-comment-comment(optional DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString data#dom-comment-comment-data-data = "");
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface AbstractRange#abstractrange {
  readonly attribute Node#node startContainer#dom-range-startcontainer;
  readonly attribute unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long startOffset#dom-range-startoffset;
  readonly attribute Node#node endContainer#dom-range-endcontainer;
  readonly attribute unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long endOffset#dom-range-endoffset;
  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean collapsed#dom-range-collapsed;
};

dictionary StaticRangeInit#dictdef-staticrangeinit {
  required Node#node startContainer#dom-staticrangeinit-startcontainer;
  required unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long startOffset#dom-staticrangeinit-startoffset;
  required Node#node endContainer#dom-staticrangeinit-endcontainer;
  required unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long endOffset#dom-staticrangeinit-endoffset;
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface StaticRange#staticrange : AbstractRange#abstractrange {
  constructor#dom-staticrange-staticrange(StaticRangeInit#dictdef-staticrangeinit init#dom-staticrange-staticrange-init-init);
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface Range#range : AbstractRange#abstractrange {
  constructor#dom-range-range();

  readonly attribute Node#node commonAncestorContainer#dom-range-commonancestorcontainer;

  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined setStart#dom-range-setstart(Node#node node#dom-range-setstart-node-offset-node, unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long offset#dom-range-setstart-node-offset-offset);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined setEnd#dom-range-setend(Node#node node#dom-range-setend-node-offset-node, unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long offset#dom-range-setend-node-offset-offset);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined setStartBefore#dom-range-setstartbefore(Node#node node#dom-range-setstartbefore-node-node);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined setStartAfter#dom-range-setstartafter(Node#node node#dom-range-setstartafter-node-node);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined setEndBefore#dom-range-setendbefore(Node#node node#dom-range-setendbefore-node-node);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined setEndAfter#dom-range-setendafter(Node#node node#dom-range-setendafter-node-node);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined collapse#dom-range-collapse(optional booleanhttps://webidl.spec.whatwg.org/#idl-boolean toStart#dom-range-collapse-tostart-tostart = false);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined selectNode#dom-range-selectnode(Node#node node#dom-range-selectnode-node-node);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined selectNodeContents#dom-range-selectnodecontents(Node#node node#dom-range-selectnodecontents-node-node);

  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short START_TO_START#dom-range-start_to_start = 0;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short START_TO_END#dom-range-start_to_end = 1;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short END_TO_END#dom-range-end_to_end = 2;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short END_TO_START#dom-range-end_to_start = 3;
  shorthttps://webidl.spec.whatwg.org/#idl-short compareBoundaryPoints#dom-range-compareboundarypoints(unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short how#dom-range-compareboundarypoints-how-sourcerange-how, Range#range sourceRange#dom-range-compareboundarypoints-how-sourcerange-sourcerange);

  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined deleteContents#dom-range-deletecontents();
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, NewObjecthttps://webidl.spec.whatwg.org/#NewObject] DocumentFragment#documentfragment extractContents#dom-range-extractcontents();
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions, NewObjecthttps://webidl.spec.whatwg.org/#NewObject] DocumentFragment#documentfragment cloneContents#dom-range-clonecontents();
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined insertNode#dom-range-insertnode(Node#node node#dom-range-insertnode-node-node);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined surroundContents#dom-range-surroundcontents(Node#node newParent#dom-range-surroundcontents-newparent-newparent);

  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] Range#range cloneRange#dom-range-clonerange();
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined detach#dom-range-detach();

  booleanhttps://webidl.spec.whatwg.org/#idl-boolean isPointInRange#dom-range-ispointinrange(Node#node node#dom-range-ispointinrange-node-offset-node, unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long offset#dom-range-ispointinrange-node-offset-offset);
  shorthttps://webidl.spec.whatwg.org/#idl-short comparePoint#dom-range-comparepoint(Node#node node#dom-range-comparepoint-node-offset-node, unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long offset#dom-range-comparepoint-node-offset-offset);

  booleanhttps://webidl.spec.whatwg.org/#idl-boolean intersectsNode#dom-range-intersectsnode(Node#node node#dom-range-intersectsnode-node-node);

  stringifier#dom-range-stringifier;
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface NodeIterator#nodeiterator {
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute Node#node root#dom-nodeiterator-root;
  readonly attribute Node#node referenceNode#dom-nodeiterator-referencenode;
  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean pointerBeforeReferenceNode#dom-nodeiterator-pointerbeforereferencenode;
  readonly attribute unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long whatToShow#dom-nodeiterator-whattoshow;
  readonly attribute NodeFilter#callbackdef-nodefilter? filter#dom-nodeiterator-filter;

  Node#node? nextNode#dom-nodeiterator-nextnode();
  Node#node? previousNode#dom-nodeiterator-previousnode();

  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined detach#dom-nodeiterator-detach();
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface TreeWalker#treewalker {
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute Node#node root#dom-treewalker-root;
  readonly attribute unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long whatToShow#dom-treewalker-whattoshow;
  readonly attribute NodeFilter#callbackdef-nodefilter? filter#dom-treewalker-filter;
           attribute Node#node currentNode#dom-treewalker-currentnode;

  Node#node? parentNode#dom-treewalker-parentnode();
  Node#node? firstChild#dom-treewalker-firstchild();
  Node#node? lastChild#dom-treewalker-lastchild();
  Node#node? previousSibling#dom-treewalker-previoussibling();
  Node#node? nextSibling#dom-treewalker-nextsibling();
  Node#node? previousNode#dom-treewalker-previousnode();
  Node#node? nextNode#dom-treewalker-nextnode();
};
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
callback interface NodeFilter#callbackdef-nodefilter {
  // Constants for acceptNode()
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short FILTER_ACCEPT#dom-nodefilter-filter_accept = 1;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short FILTER_REJECT#dom-nodefilter-filter_reject = 2;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short FILTER_SKIP#dom-nodefilter-filter_skip = 3;

  // Constants for whatToShow
  const unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long SHOW_ALL#dom-nodefilter-show_all = 0xFFFFFFFF;
  const unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long SHOW_ELEMENT#dom-nodefilter-show_element = 0x1;
  const unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long SHOW_ATTRIBUTE#dom-nodefilter-show_attribute = 0x2;
  const unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long SHOW_TEXT#dom-nodefilter-show_text = 0x4;
  const unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long SHOW_CDATA_SECTION#dom-nodefilter-show_cdata_section = 0x8;
  const unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long SHOW_ENTITY_REFERENCE#dom-nodefilter-show_entity_reference = 0x10; // legacy
  const unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long SHOW_ENTITY#dom-nodefilter-show_entity = 0x20; // legacy
  const unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long SHOW_PROCESSING_INSTRUCTION#dom-nodefilter-show_processing_instruction = 0x40;
  const unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long SHOW_COMMENT#dom-nodefilter-show_comment = 0x80;
  const unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long SHOW_DOCUMENT#dom-nodefilter-show_document = 0x100;
  const unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long SHOW_DOCUMENT_TYPE#dom-nodefilter-show_document_type = 0x200;
  const unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long SHOW_DOCUMENT_FRAGMENT#dom-nodefilter-show_document_fragment = 0x400;
  const unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long SHOW_NOTATION#dom-nodefilter-show_notation = 0x800; // legacy

  unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short acceptNode#dom-nodefilter-acceptnode(Node#node node#dom-nodefilter-acceptnode-node-node);
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface DOMTokenList#domtokenlist {
  readonly attribute unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long length#dom-domtokenlist-length;
  getter DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? item#dom-domtokenlist-item(unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long index#dom-domtokenlist-item-index-index);
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean contains#dom-domtokenlist-contains(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString token#dom-domtokenlist-contains-token-token);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined add#dom-domtokenlist-add(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString... tokens#dom-domtokenlist-add-tokens-tokens);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] undefinedhttps://webidl.spec.whatwg.org/#idl-undefined remove#dom-domtokenlist-remove(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString... tokens#dom-domtokenlist-remove-tokens-tokens);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] booleanhttps://webidl.spec.whatwg.org/#idl-boolean toggle#dom-domtokenlist-toggle(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString token#dom-domtokenlist-toggle-token-force-token, optional booleanhttps://webidl.spec.whatwg.org/#idl-boolean force#dom-domtokenlist-toggle-token-force-force);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] booleanhttps://webidl.spec.whatwg.org/#idl-boolean replace#dom-domtokenlist-replace(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString token#dom-domtokenlist-replace-token-newtoken-token, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString newToken#dom-domtokenlist-replace-token-newtoken-newtoken);
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean supports#dom-domtokenlist-supports(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString token#dom-domtokenlist-supports-token-token);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] stringifier#DOMTokenList-stringification-behavior attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString value#dom-domtokenlist-value;
  iterable<DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString>;
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface XPathResult#xpathresult {
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short ANY_TYPE#dom-xpathresult-any_type = 0;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short NUMBER_TYPE#dom-xpathresult-number_type = 1;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short STRING_TYPE#dom-xpathresult-string_type = 2;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short BOOLEAN_TYPE#dom-xpathresult-boolean_type = 3;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short UNORDERED_NODE_ITERATOR_TYPE#dom-xpathresult-unordered_node_iterator_type = 4;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short ORDERED_NODE_ITERATOR_TYPE#dom-xpathresult-ordered_node_iterator_type = 5;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short UNORDERED_NODE_SNAPSHOT_TYPE#dom-xpathresult-unordered_node_snapshot_type = 6;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short ORDERED_NODE_SNAPSHOT_TYPE#dom-xpathresult-ordered_node_snapshot_type = 7;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short ANY_UNORDERED_NODE_TYPE#dom-xpathresult-any_unordered_node_type = 8;
  const unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short FIRST_ORDERED_NODE_TYPE#dom-xpathresult-first_ordered_node_type = 9;

  readonly attribute unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short resultType#dom-xpathresult-resulttype;
  readonly attribute unrestricted doublehttps://webidl.spec.whatwg.org/#idl-unrestricted-double numberValue#dom-xpathresult-numbervalue;
  readonly attribute DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString stringValue#dom-xpathresult-stringvalue;
  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean booleanValue#dom-xpathresult-booleanvalue;
  readonly attribute Node#node? singleNodeValue#dom-xpathresult-singlenodevalue;
  readonly attribute booleanhttps://webidl.spec.whatwg.org/#idl-boolean invalidIteratorState#dom-xpathresult-invaliditeratorstate;
  readonly attribute unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long snapshotLength#dom-xpathresult-snapshotlength;

  Node#node? iterateNext#dom-xpathresult-iteratenext();
  Node#node? snapshotItem#dom-xpathresult-snapshotitem(unsigned longhttps://webidl.spec.whatwg.org/#idl-unsigned-long index#dom-xpathresult-snapshotitem-index-index);
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface XPathExpression#xpathexpression {
  // XPathResult.ANY_TYPE = 0
  XPathResult#xpathresult evaluate#dom-xpathexpression-evaluate(Node#node contextNode#dom-xpathexpression-evaluate-contextnode-type-result-contextnode, optional unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short type#dom-xpathexpression-evaluate-contextnode-type-result-type = 0, optional XPathResult#xpathresult? result#dom-xpathexpression-evaluate-contextnode-type-result-result = null);
};

callback interface XPathNSResolver#callbackdef-xpathnsresolver {
  DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? lookupNamespaceURI#dom-xpathnsresolver-lookupnamespaceuri(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString? prefix#dom-xpathnsresolver-lookupnamespaceuri-prefix-prefix);
};

interface mixin XPathEvaluatorBase#xpathevaluatorbase {
  [NewObjecthttps://webidl.spec.whatwg.org/#NewObject] XPathExpression#xpathexpression createExpression#dom-xpathevaluatorbase-createexpression(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString expression#dom-xpathevaluatorbase-createexpression-expression-resolver-expression, optional XPathNSResolver#callbackdef-xpathnsresolver? resolver#dom-xpathevaluatorbase-createexpression-expression-resolver-resolver = null);
  Node#node createNSResolver#dom-xpathevaluatorbase-creatensresolver(Node#node nodeResolver#dom-xpathevaluatorbase-creatensresolver-noderesolver-noderesolver); // legacy
  // XPathResult.ANY_TYPE = 0
  XPathResult#xpathresult evaluate#dom-xpathevaluatorbase-evaluate(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString expression#dom-xpathevaluatorbase-evaluate-expression-contextnode-resolver-type-result-expression, Node#node contextNode#dom-xpathevaluatorbase-evaluate-expression-contextnode-resolver-type-result-contextnode, optional XPathNSResolver#callbackdef-xpathnsresolver? resolver#dom-xpathevaluatorbase-evaluate-expression-contextnode-resolver-type-result-resolver = null, optional unsigned shorthttps://webidl.spec.whatwg.org/#idl-unsigned-short type#dom-xpathevaluatorbase-evaluate-expression-contextnode-resolver-type-result-type = 0, optional XPathResult#xpathresult? result#dom-xpathevaluatorbase-evaluate-expression-contextnode-resolver-type-result-result = null);
};
Document#document includes XPathEvaluatorBase#xpathevaluatorbase;

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface XPathEvaluator#xpathevaluator {
  constructor#dom-xpathevaluator-xpathevaluator();
};

XPathEvaluator#xpathevaluator includes XPathEvaluatorBase#xpathevaluatorbase;

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
interface XSLTProcessor#xsltprocessor {
  constructor#dom-xsltprocessor-xsltprocessor();
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined importStylesheet#dom-xsltprocessor-importstylesheet(Node#node style#dom-xsltprocessor-importstylesheet-style-style);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] DocumentFragment#documentfragment transformToFragment#dom-xsltprocessor-transformtofragment(Node#node source#dom-xsltprocessor-transformtofragment-source-output-source, Document#document output#dom-xsltprocessor-transformtofragment-source-output-output);
  [CEReactionshttps://html.spec.whatwg.org/multipage/custom-elements.html#cereactions] Document#document transformToDocument#dom-xsltprocessor-transformtodocument(Node#node source#dom-xsltprocessor-transformtodocument-source-source);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined setParameter#dom-xsltprocessor-setparameter([LegacyNullToEmptyStringhttps://webidl.spec.whatwg.org/#LegacyNullToEmptyString] DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString namespaceURI#dom-xsltprocessor-setparameter-namespaceuri-localname-value-namespaceuri, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName#dom-xsltprocessor-setparameter-namespaceuri-localname-value-localname, anyhttps://webidl.spec.whatwg.org/#idl-any value#dom-xsltprocessor-setparameter-namespaceuri-localname-value-value);
  anyhttps://webidl.spec.whatwg.org/#idl-any getParameter#dom-xsltprocessor-getparameter([LegacyNullToEmptyStringhttps://webidl.spec.whatwg.org/#LegacyNullToEmptyString] DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString namespaceURI#dom-xsltprocessor-getparameter-namespaceuri-localname-namespaceuri, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName#dom-xsltprocessor-getparameter-namespaceuri-localname-localname);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined removeParameter#dom-xsltprocessor-removeparameter([LegacyNullToEmptyStringhttps://webidl.spec.whatwg.org/#LegacyNullToEmptyString] DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString namespaceURI#dom-xsltprocessor-removeparameter-namespaceuri-localname-namespaceuri, DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString localName#dom-xsltprocessor-removeparameter-namespaceuri-localname-localname);
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined clearParameters#dom-xsltprocessor-clearparameters();
  undefinedhttps://webidl.spec.whatwg.org/#idl-undefined reset#dom-xsltprocessor-reset();
};

```

✔MDN

[AbortController/AbortController](https://developer.mozilla.org/en-US/docs/Web/API/AbortController/AbortController)

In all current engines.

Firefox57+Safari12.1+Chrome66+Opera?Edge79+Edge (Legacy)16+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?Node.js15.0.0+

[AbortController/abort](https://developer.mozilla.org/en-US/docs/Web/API/AbortController/abort)

In all current engines.

Firefox57+Safari12.1+Chrome66+Opera?Edge79+Edge (Legacy)16+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?Node.js15.0.0+✔MDN

[AbortController/signal](https://developer.mozilla.org/en-US/docs/Web/API/AbortController/signal)

In all current engines.

Firefox57+Safari12.1+Chrome66+Opera?Edge79+Edge (Legacy)16+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?Node.js15.0.0+✔MDN

[AbortController](https://developer.mozilla.org/en-US/docs/Web/API/AbortController)

In all current engines.

Firefox57+Safari12.1+Chrome66+Opera?Edge79+Edge (Legacy)16+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?Node.js15.0.0+✔MDN

[AbortSignal/abort_event](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal/abort_event)

In all current engines.

Firefox57+Safari11.1+Chrome66+Opera?Edge79+Edge (Legacy)16+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?Node.js15.0.0+✔MDN

[AbortSignal/abort_event](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal/abort_event)

In all current engines.

Firefox57+Safari11.1+Chrome66+Opera?Edge79+Edge (Legacy)16+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?Node.js15.0.0+✔MDN

[AbortSignal/abort_static](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal/abort_static)

In all current engines.

Firefox88+Safari15+Chrome93+Opera?Edge93+Edge (Legacy)?IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?Node.js15.12.0+✔MDN

[AbortSignal/aborted](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal/aborted)

In all current engines.

Firefox57+Safari11.1+Chrome66+Opera?Edge79+Edge (Legacy)16+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?Node.js15.0.0+✔MDN

[AbortSignal/reason](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal/reason)

In all current engines.

Firefox97+Safari15.4+Chrome98+Opera?Edge98+Edge (Legacy)?IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?Node.js17.2.0+✔MDN

[AbortSignal/throwIfAborted](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal/throwIfAborted)

In all current engines.

Firefox97+Safari15.4+Chrome100+Opera?Edge100+Edge (Legacy)?IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?Node.js17.3.0+✔MDN

[AbortSignal/timeout_static](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal/timeout_static)

In all current engines.

Firefox100+Safari16+Chrome103+Opera?Edge103+Edge (Legacy)?IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?Node.js17.3.0+✔MDN

[AbortSignal](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal)

In all current engines.

Firefox57+Safari11.1+Chrome66+Opera?Edge79+Edge (Legacy)16+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?Node.js15.0.0+✔MDN

[AbstractRange/collapsed](https://developer.mozilla.org/en-US/docs/Web/API/AbstractRange/collapsed)

In all current engines.

Firefox69+Safari14.1+Chrome90+Opera?Edge90+Edge (Legacy)NoneIENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[Range/collapsed](https://developer.mozilla.org/en-US/docs/Web/API/Range/collapsed)

In all current engines.

Firefox1+Safari1+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+

[StaticRange/collapsed](https://developer.mozilla.org/en-US/docs/Web/API/StaticRange/collapsed)

In all current engines.

Firefox69+Safari10.1+Chrome60+Opera?Edge79+Edge (Legacy)18IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[AbstractRange/endContainer](https://developer.mozilla.org/en-US/docs/Web/API/AbstractRange/endContainer)

In all current engines.

Firefox69+Safari14.1+Chrome90+Opera?Edge90+Edge (Legacy)NoneIENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[Range/endContainer](https://developer.mozilla.org/en-US/docs/Web/API/Range/endContainer)

In all current engines.

Firefox1+Safari1+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+

[StaticRange/endContainer](https://developer.mozilla.org/en-US/docs/Web/API/StaticRange/endContainer)

In all current engines.

Firefox69+Safari10.1+Chrome60+Opera?Edge79+Edge (Legacy)18IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[AbstractRange/endOffset](https://developer.mozilla.org/en-US/docs/Web/API/AbstractRange/endOffset)

In all current engines.

Firefox69+Safari14.1+Chrome90+Opera?Edge90+Edge (Legacy)NoneIENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[Range/endOffset](https://developer.mozilla.org/en-US/docs/Web/API/Range/endOffset)

In all current engines.

Firefox1+Safari1+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+

[StaticRange/endOffset](https://developer.mozilla.org/en-US/docs/Web/API/StaticRange/endOffset)

In all current engines.

Firefox69+Safari10.1+Chrome60+Opera?Edge79+Edge (Legacy)18IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[AbstractRange/startContainer](https://developer.mozilla.org/en-US/docs/Web/API/AbstractRange/startContainer)

In all current engines.

Firefox69+Safari14.1+Chrome90+Opera?Edge90+Edge (Legacy)NoneIENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[Range/startContainer](https://developer.mozilla.org/en-US/docs/Web/API/Range/startContainer)

In all current engines.

Firefox1+Safari1+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+

[StaticRange/startContainer](https://developer.mozilla.org/en-US/docs/Web/API/StaticRange/startContainer)

In all current engines.

Firefox69+Safari10.1+Chrome60+Opera?Edge79+Edge (Legacy)18IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[AbstractRange/startOffset](https://developer.mozilla.org/en-US/docs/Web/API/AbstractRange/startOffset)

In all current engines.

Firefox69+Safari14.1+Chrome90+Opera?Edge90+Edge (Legacy)NoneIENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[Range/startOffset](https://developer.mozilla.org/en-US/docs/Web/API/Range/startOffset)

In all current engines.

Firefox1+Safari1+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+

[StaticRange/startOffset](https://developer.mozilla.org/en-US/docs/Web/API/StaticRange/startOffset)

In all current engines.

Firefox69+Safari10.1+Chrome60+Opera?Edge79+Edge (Legacy)18IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[AbstractRange](https://developer.mozilla.org/en-US/docs/Web/API/AbstractRange)

In all current engines.

Firefox69+Safari14.1+Chrome90+Opera?Edge90+Edge (Legacy)NoneIENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[Attr/localName](https://developer.mozilla.org/en-US/docs/Web/API/Attr/localName)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Attr/name](https://developer.mozilla.org/en-US/docs/Web/API/Attr/name)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Attr/namespaceURI](https://developer.mozilla.org/en-US/docs/Web/API/Attr/namespaceURI)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Attr/ownerElement](https://developer.mozilla.org/en-US/docs/Web/API/Attr/ownerElement)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE8+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Attr/prefix](https://developer.mozilla.org/en-US/docs/Web/API/Attr/prefix)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Attr/value](https://developer.mozilla.org/en-US/docs/Web/API/Attr/value)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Attr](https://developer.mozilla.org/en-US/docs/Web/API/Attr)

In all current engines.

Firefox1+Safari1+Chrome1+Opera8+Edge79+Edge (Legacy)12+IE5.5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[CDATASection](https://developer.mozilla.org/en-US/docs/Web/API/CDATASection)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari1+Chrome for Android?Android WebView37+Samsung Internet?Opera Mobile12.1+✔MDN

[CharacterData/after](https://developer.mozilla.org/en-US/docs/Web/API/CharacterData/after)

In all current engines.

Firefox49+Safari10+Chrome54+Opera39+Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[DocumentType/after](https://developer.mozilla.org/en-US/docs/Web/API/DocumentType/after)

In all current engines.

Firefox49+Safari10+Chrome54+Opera39+Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[Element/after](https://developer.mozilla.org/en-US/docs/Web/API/Element/after)

In all current engines.

Firefox49+Safari10+Chrome54+Opera39+Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[CharacterData/appendData](https://developer.mozilla.org/en-US/docs/Web/API/CharacterData/appendData)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[CharacterData/before](https://developer.mozilla.org/en-US/docs/Web/API/CharacterData/before)

In all current engines.

Firefox49+Safari10+Chrome54+Opera39+Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[DocumentType/before](https://developer.mozilla.org/en-US/docs/Web/API/DocumentType/before)

In all current engines.

Firefox49+Safari10+Chrome54+Opera39+Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[Element/before](https://developer.mozilla.org/en-US/docs/Web/API/Element/before)

In all current engines.

Firefox49+Safari10+Chrome54+Opera39+Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[CharacterData/data](https://developer.mozilla.org/en-US/docs/Web/API/CharacterData/data)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[CharacterData/deleteData](https://developer.mozilla.org/en-US/docs/Web/API/CharacterData/deleteData)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[CharacterData/insertData](https://developer.mozilla.org/en-US/docs/Web/API/CharacterData/insertData)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[CharacterData/length](https://developer.mozilla.org/en-US/docs/Web/API/CharacterData/length)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[CharacterData/nextElementSibling](https://developer.mozilla.org/en-US/docs/Web/API/CharacterData/nextElementSibling)

In all current engines.

Firefox25+Safari9+Chrome29+Opera?Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[Element/nextElementSibling](https://developer.mozilla.org/en-US/docs/Web/API/Element/nextElementSibling)

In all current engines.

Firefox3.5+Safari4+Chrome2+Opera10+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView37+Samsung Internet?Opera Mobile10.1+✔MDN

[CharacterData/previousElementSibling](https://developer.mozilla.org/en-US/docs/Web/API/CharacterData/previousElementSibling)

In all current engines.

Firefox25+Safari9+Chrome29+Opera?Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[Element/previousElementSibling](https://developer.mozilla.org/en-US/docs/Web/API/Element/previousElementSibling)

In all current engines.

Firefox3.5+Safari4+Chrome2+Opera10+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView37+Samsung Internet?Opera Mobile10.1+✔MDN

[CharacterData/remove](https://developer.mozilla.org/en-US/docs/Web/API/CharacterData/remove)

In all current engines.

Firefox23+Safari7+Chrome24+Opera?Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[DocumentType/remove](https://developer.mozilla.org/en-US/docs/Web/API/DocumentType/remove)

In all current engines.

Firefox23+Safari7+Chrome24+Opera?Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[Element/remove](https://developer.mozilla.org/en-US/docs/Web/API/Element/remove)

In all current engines.

Firefox23+Safari7+Chrome24+Opera?Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[CharacterData/replaceData](https://developer.mozilla.org/en-US/docs/Web/API/CharacterData/replaceData)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[CharacterData/replaceWith](https://developer.mozilla.org/en-US/docs/Web/API/CharacterData/replaceWith)

In all current engines.

Firefox49+Safari10+Chrome54+Opera39+Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[DocumentType/replaceWith](https://developer.mozilla.org/en-US/docs/Web/API/DocumentType/replaceWith)

In all current engines.

Firefox49+Safari10+Chrome54+Opera39+Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[Element/replaceWith](https://developer.mozilla.org/en-US/docs/Web/API/Element/replaceWith)

In all current engines.

Firefox49+Safari10+Chrome54+Opera39+Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[CharacterData/substringData](https://developer.mozilla.org/en-US/docs/Web/API/CharacterData/substringData)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[CharacterData](https://developer.mozilla.org/en-US/docs/Web/API/CharacterData)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Comment/Comment](https://developer.mozilla.org/en-US/docs/Web/API/Comment/Comment)

In all current engines.

Firefox24+Safari8+Chrome29+Opera?Edge79+Edge (Legacy)16+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[Comment](https://developer.mozilla.org/en-US/docs/Web/API/Comment)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[CustomEvent/CustomEvent](https://developer.mozilla.org/en-US/docs/Web/API/CustomEvent/CustomEvent)

In all current engines.

Firefox11+Safari6+Chrome15+Opera11.6+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12+✔MDN

[CustomEvent/detail](https://developer.mozilla.org/en-US/docs/Web/API/CustomEvent/detail)

In all current engines.

Firefox6+Safari5+Chrome5+Opera11.6+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari5+Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile12+✔MDN

[CustomEvent](https://developer.mozilla.org/en-US/docs/Web/API/CustomEvent)

In all current engines.

Firefox6+Safari5+Chrome5+Opera11+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari5+Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile11+Node.js19.0.0+✔MDN

[DOMImplementation/createDocument](https://developer.mozilla.org/en-US/docs/Web/API/DOMImplementation/createDocument)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[DOMImplementation/createDocumentType](https://developer.mozilla.org/en-US/docs/Web/API/DOMImplementation/createDocumentType)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[DOMImplementation/createHTMLDocument](https://developer.mozilla.org/en-US/docs/Web/API/DOMImplementation/createHTMLDocument)

In all current engines.

Firefox4+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[DOMImplementation](https://developer.mozilla.org/en-US/docs/Web/API/DOMImplementation)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[DOMTokenList/add](https://developer.mozilla.org/en-US/docs/Web/API/DOMTokenList/add)

In all current engines.

Firefox3.6+Safari5.1+Chrome8+Opera12.1+Edge79+Edge (Legacy)12+IE10+Firefox for Android?iOS Safari?Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile12.1+✔MDN

[DOMTokenList/contains](https://developer.mozilla.org/en-US/docs/Web/API/DOMTokenList/contains)

In all current engines.

Firefox3.6+Safari5.1+Chrome8+Opera12.1+Edge79+Edge (Legacy)12+IE10+Firefox for Android?iOS Safari?Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile12.1+✔MDN

[DOMTokenList/item](https://developer.mozilla.org/en-US/docs/Web/API/DOMTokenList/item)

In all current engines.

Firefox3.6+Safari5.1+Chrome8+Opera12.1+Edge79+Edge (Legacy)12+IE10+Firefox for Android?iOS Safari?Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile12.1+✔MDN

[DOMTokenList/length](https://developer.mozilla.org/en-US/docs/Web/API/DOMTokenList/length)

In all current engines.

Firefox3.6+Safari5.1+Chrome8+Opera12.1+Edge79+Edge (Legacy)12+IE10+Firefox for Android?iOS Safari?Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile12.1+✔MDN

[DOMTokenList/remove](https://developer.mozilla.org/en-US/docs/Web/API/DOMTokenList/remove)

In all current engines.

Firefox3.6+Safari5.1+Chrome8+Opera12.1+Edge79+Edge (Legacy)12+IE10+Firefox for Android?iOS Safari?Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile12.1+✔MDN

[DOMTokenList/replace](https://developer.mozilla.org/en-US/docs/Web/API/DOMTokenList/replace)

In all current engines.

Firefox49+Safari10.1+Chrome61+Opera?Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[DOMTokenList/supports](https://developer.mozilla.org/en-US/docs/Web/API/DOMTokenList/supports)

In all current engines.

Firefox49+Safari10.1+Chrome49+Opera?Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[DOMTokenList/toggle](https://developer.mozilla.org/en-US/docs/Web/API/DOMTokenList/toggle)

In all current engines.

Firefox3.6+Safari5.1+Chrome8+Opera12.1+Edge79+Edge (Legacy)12+IE10+Firefox for Android?iOS Safari?Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile12.1+✔MDN

[DOMTokenList/value](https://developer.mozilla.org/en-US/docs/Web/API/DOMTokenList/value)

In all current engines.

Firefox47+Safari10+Chrome50+Opera?Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[DOMTokenList](https://developer.mozilla.org/en-US/docs/Web/API/DOMTokenList)

In all current engines.

Firefox3.6+Safari5.1+Chrome8+Opera11.5+Edge79+Edge (Legacy)12+IE10+Firefox for Android?iOS Safari?Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile11.5+✔MDN

[Document/Document](https://developer.mozilla.org/en-US/docs/Web/API/Document/Document)

In all current engines.

Firefox20+Safari8+Chrome60+Opera?Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[Document/URL](https://developer.mozilla.org/en-US/docs/Web/API/Document/URL)

In all current engines.

Firefox1+Safari1+Chrome1+Opera3+Edge79+Edge (Legacy)12+IE4+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Document/adoptNode](https://developer.mozilla.org/en-US/docs/Web/API/Document/adoptNode)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Document/append](https://developer.mozilla.org/en-US/docs/Web/API/Document/append)

In all current engines.

Firefox49+Safari10+Chrome54+Opera?Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[DocumentFragment/append](https://developer.mozilla.org/en-US/docs/Web/API/DocumentFragment/append)

In all current engines.

Firefox49+Safari10+Chrome54+Opera?Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[Element/append](https://developer.mozilla.org/en-US/docs/Web/API/Element/append)

In all current engines.

Firefox49+Safari10+Chrome54+Opera?Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[Document/characterSet](https://developer.mozilla.org/en-US/docs/Web/API/Document/characterSet)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari1+Chrome for Android?Android WebView1+Samsung Internet?Opera Mobile12.1+✔MDN

[Document/childElementCount](https://developer.mozilla.org/en-US/docs/Web/API/Document/childElementCount)

In all current engines.

Firefox25+Safari9+Chrome29+Opera?Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[DocumentFragment/childElementCount](https://developer.mozilla.org/en-US/docs/Web/API/DocumentFragment/childElementCount)

In all current engines.

Firefox25+Safari9+Chrome29+Opera?Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[Element/childElementCount](https://developer.mozilla.org/en-US/docs/Web/API/Element/childElementCount)

In all current engines.

Firefox3.5+Safari4+Chrome2+Opera10+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView37+Samsung Internet?Opera Mobile10.1+✔MDN

[Document/children](https://developer.mozilla.org/en-US/docs/Web/API/Document/children)

In all current engines.

Firefox25+Safari9+Chrome29+Opera?Edge79+Edge (Legacy)16+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[DocumentFragment/children](https://developer.mozilla.org/en-US/docs/Web/API/DocumentFragment/children)

In all current engines.

Firefox25+Safari9+Chrome29+Opera?Edge79+Edge (Legacy)16+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[Element/children](https://developer.mozilla.org/en-US/docs/Web/API/Element/children)

In all current engines.

Firefox3.5+Safari4+Chrome1+Opera10+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Document/compatMode](https://developer.mozilla.org/en-US/docs/Web/API/Document/compatMode)

In all current engines.

Firefox1+Safari3.1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Document/contentType](https://developer.mozilla.org/en-US/docs/Web/API/Document/contentType)

In all current engines.

Firefox1+Safari9+Chrome36+Opera23+Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile24+✔MDN

[Document/createAttribute](https://developer.mozilla.org/en-US/docs/Web/API/Document/createAttribute)

In all current engines.

Firefox44+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Document/createAttributeNS](https://developer.mozilla.org/en-US/docs/Web/API/Document/createAttributeNS)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Document/createCDATASection](https://developer.mozilla.org/en-US/docs/Web/API/Document/createCDATASection)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+

[Document/createComment](https://developer.mozilla.org/en-US/docs/Web/API/Document/createComment)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Document/createDocumentFragment](https://developer.mozilla.org/en-US/docs/Web/API/Document/createDocumentFragment)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Document/createElement](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement)

In all current engines.

Firefox1+Safari1+Chrome1+Opera6+Edge79+Edge (Legacy)12+IE5+Firefox for Android4+iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Document/createElementNS](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElementNS)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android4+iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Document/createEvent](https://developer.mozilla.org/en-US/docs/Web/API/Document/createEvent)

In all current engines.

Firefox1+Safari1+Chrome1+Opera7+Edge79+Edge (Legacy)12+IE9+Firefox for Android4+iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Document/createExpression](https://developer.mozilla.org/en-US/docs/Web/API/Document/createExpression)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari1+Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile12.1+

[XPathEvaluator/createExpression](https://developer.mozilla.org/en-US/docs/Web/API/XPathEvaluator/createExpression)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Document/createNodeIterator](https://developer.mozilla.org/en-US/docs/Web/API/Document/createNodeIterator)

In all current engines.

Firefox1+Safari3+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Document/createNSResolver](https://developer.mozilla.org/en-US/docs/Web/API/Document/createNSResolver)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari1+Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile12.1+

[XPathEvaluator/createNSResolver](https://developer.mozilla.org/en-US/docs/Web/API/XPathEvaluator/createNSResolver)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Document/createProcessingInstruction](https://developer.mozilla.org/en-US/docs/Web/API/Document/createProcessingInstruction)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Document/createRange](https://developer.mozilla.org/en-US/docs/Web/API/Document/createRange)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Document/createTextNode](https://developer.mozilla.org/en-US/docs/Web/API/Document/createTextNode)

In all current engines.

Firefox1+Safari1+Chrome1+Opera7+Edge79+Edge (Legacy)12+IE5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Document/createTreeWalker](https://developer.mozilla.org/en-US/docs/Web/API/Document/createTreeWalker)

In all current engines.

Firefox1+Safari3+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Document/doctype](https://developer.mozilla.org/en-US/docs/Web/API/Document/doctype)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Document/documentElement](https://developer.mozilla.org/en-US/docs/Web/API/Document/documentElement)

In all current engines.

Firefox1+Safari1+Chrome1+Opera7+Edge79+Edge (Legacy)12+IE5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Document/documentURI](https://developer.mozilla.org/en-US/docs/Web/API/Document/documentURI)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Document/evaluate](https://developer.mozilla.org/en-US/docs/Web/API/Document/evaluate)

In all current engines.

Firefox1+Safari3+Chrome1+Opera9+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari1+Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile10.1+

[XPathEvaluator/evaluate](https://developer.mozilla.org/en-US/docs/Web/API/XPathEvaluator/evaluate)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Document/firstElementChild](https://developer.mozilla.org/en-US/docs/Web/API/Document/firstElementChild)

In all current engines.

Firefox25+Safari9+Chrome29+Opera?Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[DocumentFragment/firstElementChild](https://developer.mozilla.org/en-US/docs/Web/API/DocumentFragment/firstElementChild)

In all current engines.

Firefox25+Safari9+Chrome29+Opera?Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[Element/firstElementChild](https://developer.mozilla.org/en-US/docs/Web/API/Element/firstElementChild)

In all current engines.

Firefox3.5+Safari4+Chrome2+Opera10+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView37+Samsung Internet?Opera Mobile10.1+✔MDN

[Document/getElementById](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById)

In all current engines.

Firefox1+Safari1+Chrome1+Opera7+Edge79+Edge (Legacy)12+IE5.5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Document/getElementsByClassName](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementsByClassName)

In all current engines.

Firefox3+Safari3.1+Chrome1+Opera9.5+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Document/getElementsByTagName](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementsByTagName)

In all current engines.

Firefox1+Safari1+Chrome1+Opera5.1+Edge79+Edge (Legacy)12+IE5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Document/getElementsByTagNameNS](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementsByTagNameNS)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Document/implementation](https://developer.mozilla.org/en-US/docs/Web/API/Document/implementation)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Document/importNode](https://developer.mozilla.org/en-US/docs/Web/API/Document/importNode)

In all current engines.

Firefox1+Safari1+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Document/lastElementChild](https://developer.mozilla.org/en-US/docs/Web/API/Document/lastElementChild)

In all current engines.

Firefox25+Safari9+Chrome29+Opera?Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[DocumentFragment/lastElementChild](https://developer.mozilla.org/en-US/docs/Web/API/DocumentFragment/lastElementChild)

In all current engines.

Firefox25+Safari9+Chrome29+Opera?Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[Element/lastElementChild](https://developer.mozilla.org/en-US/docs/Web/API/Element/lastElementChild)

In all current engines.

Firefox3.5+Safari4+Chrome2+Opera10+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView37+Samsung Internet?Opera Mobile10.1+✔MDN

[Document/prepend](https://developer.mozilla.org/en-US/docs/Web/API/Document/prepend)

In all current engines.

Firefox49+Safari10+Chrome54+Opera?Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[DocumentFragment/prepend](https://developer.mozilla.org/en-US/docs/Web/API/DocumentFragment/prepend)

In all current engines.

Firefox49+Safari10+Chrome54+Opera?Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[Element/prepend](https://developer.mozilla.org/en-US/docs/Web/API/Element/prepend)

In all current engines.

Firefox49+Safari10+Chrome54+Opera?Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[Document/querySelector](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)

In all current engines.

Firefox3.5+Safari3.1+Chrome1+Opera10+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+

[DocumentFragment/querySelector](https://developer.mozilla.org/en-US/docs/Web/API/DocumentFragment/querySelector)

In all current engines.

Firefox3.5+Safari4+Chrome2+Opera10+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView37+Samsung Internet?Opera Mobile10.1+✔MDN

[Document/querySelectorAll](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll)

In all current engines.

Firefox3.5+Safari3.1+Chrome1+Opera10+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+

[DocumentFragment/querySelectorAll](https://developer.mozilla.org/en-US/docs/Web/API/DocumentFragment/querySelectorAll)

In all current engines.

Firefox3.5+Safari4+Chrome2+Opera10+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView37+Samsung Internet?Opera Mobile10.1+

[Element/querySelector](https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelector)

In all current engines.

Firefox3.5+Safari3.1+Chrome1+Opera10+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+

[Element/querySelectorAll](https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelectorAll)

In all current engines.

Firefox3.5+Safari3.1+Chrome1+Opera10+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Document/replaceChildren](https://developer.mozilla.org/en-US/docs/Web/API/Document/replaceChildren)

In all current engines.

Firefox78+Safari14+Chrome86+Opera?Edge86+Edge (Legacy)?IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[DocumentFragment/replaceChildren](https://developer.mozilla.org/en-US/docs/Web/API/DocumentFragment/replaceChildren)

In all current engines.

Firefox78+Safari14+Chrome86+Opera?Edge86+Edge (Legacy)?IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[Element/replaceChildren](https://developer.mozilla.org/en-US/docs/Web/API/Element/replaceChildren)

In all current engines.

Firefox78+Safari14+Chrome86+Opera?Edge86+Edge (Legacy)?IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[Document](https://developer.mozilla.org/en-US/docs/Web/API/Document)

In all current engines.

Firefox1+Safari1+Chrome1+Opera3+Edge79+Edge (Legacy)12+IE4+Firefox for Android?iOS Safari?Chrome for Android?Android WebView37+Samsung Internet?Opera Mobile10.1+✔MDN

[DocumentFragment/DocumentFragment](https://developer.mozilla.org/en-US/docs/Web/API/DocumentFragment/DocumentFragment)

In all current engines.

Firefox24+Safari8+Chrome29+Opera?Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[DocumentFragment/getElementById](https://developer.mozilla.org/en-US/docs/Web/API/DocumentFragment/getElementById)

In all current engines.

Firefox28+Safari9+Chrome36+Opera?Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[DocumentFragment](https://developer.mozilla.org/en-US/docs/Web/API/DocumentFragment)

In all current engines.

Firefox1+Safari3+Chrome1+Opera8+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[DocumentType/name](https://developer.mozilla.org/en-US/docs/Web/API/DocumentType/name)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[DocumentType/publicId](https://developer.mozilla.org/en-US/docs/Web/API/DocumentType/publicId)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[DocumentType/systemId](https://developer.mozilla.org/en-US/docs/Web/API/DocumentType/systemId)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[DocumentType](https://developer.mozilla.org/en-US/docs/Web/API/DocumentType)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari1+Chrome for Android?Android WebView37+Samsung Internet?Opera Mobile12.1+✔MDN

[Element/assignedSlot](https://developer.mozilla.org/en-US/docs/Web/API/Element/assignedSlot)

In all current engines.

Firefox63+Safari10+Chrome53+Opera?Edge79+Edge (Legacy)?IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[Text/assignedSlot](https://developer.mozilla.org/en-US/docs/Web/API/Text/assignedSlot)

In all current engines.

Firefox63+Safari10+Chrome53+Opera?Edge79+Edge (Legacy)?IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[Element/attachShadow](https://developer.mozilla.org/en-US/docs/Web/API/Element/attachShadow)

In all current engines.

Firefox63+Safari10+Chrome53+Opera?Edge79+Edge (Legacy)?IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[Element/attributes](https://developer.mozilla.org/en-US/docs/Web/API/Element/attributes)

In all current engines.

Firefox1+Safari1+Chrome1+Opera8+Edge79+Edge (Legacy)12+IE5.5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Element/classList](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList)

In all current engines.

Firefox3.6+Safari7+Chrome22+Opera11.5+Edge79+Edge (Legacy)16+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView4.4+Samsung Internet?Opera Mobile11.5+✔MDN

[Element/className](https://developer.mozilla.org/en-US/docs/Web/API/Element/className)

In all current engines.

Firefox1+Safari1+Chrome22+Opera8+Edge79+Edge (Legacy)12+IE5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Element/closest](https://developer.mozilla.org/en-US/docs/Web/API/Element/closest)

In all current engines.

Firefox35+Safari6+Chrome41+Opera?Edge79+Edge (Legacy)15+IENoneFirefox for Android?iOS Safari9+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[Element/getAttribute](https://developer.mozilla.org/en-US/docs/Web/API/Element/getAttribute)

In all current engines.

Firefox1+Safari1+Chrome1+Opera8+Edge79+Edge (Legacy)12+IE5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Element/getAttributeNames](https://developer.mozilla.org/en-US/docs/Web/API/Element/getAttributeNames)

In all current engines.

Firefox45+Safari10.1+Chrome61+Opera?Edge79+Edge (Legacy)18IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[Element/getAttributeNode](https://developer.mozilla.org/en-US/docs/Web/API/Element/getAttributeNode)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Element/getAttributeNodeNS](https://developer.mozilla.org/en-US/docs/Web/API/Element/getAttributeNodeNS)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Element/getAttributeNS](https://developer.mozilla.org/en-US/docs/Web/API/Element/getAttributeNS)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Element/getElementsByClassName](https://developer.mozilla.org/en-US/docs/Web/API/Element/getElementsByClassName)

In all current engines.

Firefox3+Safari3.1+Chrome1+Opera9.5+Edge79+Edge (Legacy)16+IENoneFirefox for Android4+iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Element/getElementsByTagName](https://developer.mozilla.org/en-US/docs/Web/API/Element/getElementsByTagName)

In all current engines.

Firefox1+Safari1+Chrome1+Opera8+Edge79+Edge (Legacy)12+IE5.5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Element/getElementsByTagNameNS](https://developer.mozilla.org/en-US/docs/Web/API/Element/getElementsByTagNameNS)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android4+iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Element/hasAttribute](https://developer.mozilla.org/en-US/docs/Web/API/Element/hasAttribute)

In all current engines.

Firefox1+Safari1+Chrome1+Opera8+Edge79+Edge (Legacy)12+IE8+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Element/hasAttributeNS](https://developer.mozilla.org/en-US/docs/Web/API/Element/hasAttributeNS)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Element/hasAttributes](https://developer.mozilla.org/en-US/docs/Web/API/Element/hasAttributes)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE8+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Element/id](https://developer.mozilla.org/en-US/docs/Web/API/Element/id)

In all current engines.

Firefox1+Safari1+Chrome23+Opera12.1+Edge79+Edge (Legacy)12+IE5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Element/insertAdjacentElement](https://developer.mozilla.org/en-US/docs/Web/API/Element/insertAdjacentElement)

In all current engines.

Firefox48+Safari3+Chrome1+Opera8+Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Element/insertAdjacentText](https://developer.mozilla.org/en-US/docs/Web/API/Element/insertAdjacentText)

In all current engines.

Firefox48+Safari4+Chrome1+Opera12.1+Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari4+Chrome for Android?Android WebView2.2+Samsung Internet?Opera Mobile12.1+✔MDN

[Element/localName](https://developer.mozilla.org/en-US/docs/Web/API/Element/localName)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Element/matches](https://developer.mozilla.org/en-US/docs/Web/API/Element/matches)

In all current engines.

Firefox34+Safari8+Chrome33+Opera21+Edge79+Edge (Legacy)15+IENoneFirefox for Android34+iOS Safari?Chrome for Android?Android WebView4.4+Samsung Internet?Opera Mobile21+✔MDN

[Element/namespaceURI](https://developer.mozilla.org/en-US/docs/Web/API/Element/namespaceURI)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Element/prefix](https://developer.mozilla.org/en-US/docs/Web/API/Element/prefix)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Element/removeAttribute](https://developer.mozilla.org/en-US/docs/Web/API/Element/removeAttribute)

In all current engines.

Firefox1+Safari1+Chrome1+Opera8+Edge79+Edge (Legacy)12+IE5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Element/removeAttributeNode](https://developer.mozilla.org/en-US/docs/Web/API/Element/removeAttributeNode)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Element/removeAttributeNS](https://developer.mozilla.org/en-US/docs/Web/API/Element/removeAttributeNS)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Element/setAttribute](https://developer.mozilla.org/en-US/docs/Web/API/Element/setAttribute)

In all current engines.

Firefox1+Safari1+Chrome1+Opera8+Edge79+Edge (Legacy)12+IE5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Element/setAttributeNode](https://developer.mozilla.org/en-US/docs/Web/API/Element/setAttributeNode)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Element/setAttributeNodeNS](https://developer.mozilla.org/en-US/docs/Web/API/Element/setAttributeNodeNS)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Element/setAttributeNS](https://developer.mozilla.org/en-US/docs/Web/API/Element/setAttributeNS)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Element/shadowRoot](https://developer.mozilla.org/en-US/docs/Web/API/Element/shadowRoot)

In all current engines.

Firefox63+Safari10+Chrome35+Opera?Edge79+Edge (Legacy)?IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[Element/slot](https://developer.mozilla.org/en-US/docs/Web/API/Element/slot)

In all current engines.

Firefox63+Safari10+Chrome53+Opera?Edge79+Edge (Legacy)?IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[Global_attributes/slot](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/slot)

In all current engines.

Firefox63+Safari10+Chrome53+Opera?Edge79+Edge (Legacy)NoneIE?Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[Element/tagName](https://developer.mozilla.org/en-US/docs/Web/API/Element/tagName)

In all current engines.

Firefox1+Safari1+Chrome1+Opera8+Edge79+Edge (Legacy)12+IE5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Element/toggleAttribute](https://developer.mozilla.org/en-US/docs/Web/API/Element/toggleAttribute)

In all current engines.

Firefox63+Safari12+Chrome69+Opera?Edge79+Edge (Legacy)18IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[Element](https://developer.mozilla.org/en-US/docs/Web/API/Element)

In all current engines.

Firefox1+Safari1+Chrome1+Opera8+Edge79+Edge (Legacy)12+IE4+Firefox for Android?iOS Safari?Chrome for Android?Android WebView37+Samsung Internet?Opera Mobile10.1+✔MDN

[Event/Event](https://developer.mozilla.org/en-US/docs/Web/API/Event/Event)

In all current engines.

Firefox11+Safari6+Chrome15+Opera11.6+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12+Node.js15.0.0+✔MDN

[Event/bubbles](https://developer.mozilla.org/en-US/docs/Web/API/Event/bubbles)

In all current engines.

Firefox1.5+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView37+Samsung Internet?Opera Mobile12.1+Node.js14.5.0+✔MDN

[Event/cancelable](https://developer.mozilla.org/en-US/docs/Web/API/Event/cancelable)

In all current engines.

Firefox1.5+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView37+Samsung Internet?Opera Mobile12.1+Node.js14.5.0+✔MDN

[Event/composed](https://developer.mozilla.org/en-US/docs/Web/API/Event/composed)

In all current engines.

Firefox52+Safari10+Chrome53+Opera?Edge79+Edge (Legacy)?IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?Node.js14.5.0+✔MDN

[Event/composedPath](https://developer.mozilla.org/en-US/docs/Web/API/Event/composedPath)

In all current engines.

Firefox59+Safari10+Chrome53+Opera?Edge79+Edge (Legacy)?IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?Node.js14.5.0+✔MDN

[Event/currentTarget](https://developer.mozilla.org/en-US/docs/Web/API/Event/currentTarget)

In all current engines.

Firefox1+Safari1+Chrome1+Opera7+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+Node.js14.5.0+✔MDN

[Event/defaultPrevented](https://developer.mozilla.org/en-US/docs/Web/API/Event/defaultPrevented)

In all current engines.

Firefox6+Safari5+Chrome5+Opera11+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari5+Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile11+Node.js14.5.0+✔MDN

[Event/eventPhase](https://developer.mozilla.org/en-US/docs/Web/API/Event/eventPhase)

In all current engines.

Firefox1.5+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+Node.js14.5.0+✔MDN

[Event/isTrusted](https://developer.mozilla.org/en-US/docs/Web/API/Event/isTrusted)

In all current engines.

Firefox1.5+Safari10+Chrome46+Opera33+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView46+Samsung Internet?Opera Mobile33+Node.js14.5.0+✔MDN

[Event/preventDefault](https://developer.mozilla.org/en-US/docs/Web/API/Event/preventDefault)

In all current engines.

Firefox1+Safari1+Chrome1+Opera7+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+Node.js14.5.0+✔MDN

[Event/stopImmediatePropagation](https://developer.mozilla.org/en-US/docs/Web/API/Event/stopImmediatePropagation)

In all current engines.

Firefox10+Safari5+Chrome5+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari5+Chrome for Android?Android WebView37+Samsung Internet?Opera Mobile12.1+Node.js14.5.0+✔MDN

[Event/stopPropagation](https://developer.mozilla.org/en-US/docs/Web/API/Event/stopPropagation)

In all current engines.

Firefox1+Safari1+Chrome1+Opera7+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+Node.js14.5.0+✔MDN

[Event/target](https://developer.mozilla.org/en-US/docs/Web/API/Event/target)

In all current engines.

Firefox1+Safari1+Chrome1+Opera7+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+Node.js14.5.0+✔MDN

[Event/timeStamp](https://developer.mozilla.org/en-US/docs/Web/API/Event/timeStamp)

In all current engines.

Firefox1.5+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView1+Samsung Internet?Opera Mobile12.1+Node.js14.5.0+✔MDN

[Event/type](https://developer.mozilla.org/en-US/docs/Web/API/Event/type)

In all current engines.

Firefox1.5+Safari1+Chrome1+Opera7+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+Node.js14.5.0+✔MDN

[Event](https://developer.mozilla.org/en-US/docs/Web/API/Event)

In all current engines.

Firefox1+Safari1+Chrome1+Opera4+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView37+Samsung Internet?Opera Mobile10.1+Node.js14.5.0+✔MDN

[EventTarget/EventTarget](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/EventTarget)

In all current engines.

Firefox59+Safari14+Chrome64+Opera?Edge79+Edge (Legacy)?IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?Node.js15.0.0+✔MDN

[EventTarget/addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)

In all current engines.

Firefox1+Safari1+Chrome1+Opera7+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView1+Samsung Internet?Opera Mobile10.1+Node.js14.5.0+✔MDN

[EventTarget/dispatchEvent](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/dispatchEvent)

In all current engines.

Firefox2+Safari3.1+Chrome4+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView4+Samsung Internet?Opera Mobile10.1+Node.js14.5.0+✔MDN

[EventTarget/removeEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/removeEventListener)

In all current engines.

Firefox1+Safari1+Chrome1+Opera7+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+Node.js14.5.0+✔MDN

[EventTarget](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget)

In all current engines.

Firefox1+Safari1+Chrome1+Opera7+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari1+Chrome for Android?Android WebView37+Samsung Internet?Opera Mobile10.1+Node.js14.5.0+✔MDN

[HTMLCollection/item](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCollection/item)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE8+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[HTMLCollection/length](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCollection/length)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE8+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[HTMLCollection/namedItem](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCollection/namedItem)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE8+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[HTMLCollection](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCollection)

In all current engines.

Firefox1+Safari1+Chrome1+Opera8+Edge79+Edge (Legacy)12+IE8+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[HTMLSlotElement/slotchange_event](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSlotElement/slotchange_event)

In all current engines.

Firefox63+Safari10.1+Chrome53+Opera?Edge79+Edge (Legacy)?IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[MutationObserver/MutationObserver](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver/MutationObserver)

In all current engines.

Firefox14+Safari7+Chrome26+Opera15+Edge79+Edge (Legacy)12+IE11Firefox for Android?iOS Safari?Chrome for Android?Android WebView4.4+Samsung Internet?Opera Mobile14+✔MDN

[MutationObserver/disconnect](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver/disconnect)

In all current engines.

Firefox14+Safari6+Chrome18+Opera?Edge79+Edge (Legacy)12+IE11Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[MutationObserver/observe](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver/observe)

In all current engines.

Firefox14+Safari6+Chrome18+Opera?Edge79+Edge (Legacy)12+IE11Firefox for Android?iOS Safari6+Chrome for Android?Android WebView4.4+Samsung Internet?Opera Mobile?✔MDN

[MutationObserver/takeRecords](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver/takeRecords)

In all current engines.

Firefox14+Safari6+Chrome20+Opera?Edge79+Edge (Legacy)12+IE11Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[MutationObserver](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver)

In all current engines.

Firefox14+Safari7+Chrome26+Opera15+Edge79+Edge (Legacy)12+IE11Firefox for Android?iOS Safari?Chrome for Android?Android WebView4.4+Samsung Internet?Opera Mobile14+✔MDN

[MutationRecord/addedNodes](https://developer.mozilla.org/en-US/docs/Web/API/MutationRecord/addedNodes)

In all current engines.

Firefox14+Safari7+Chrome16+Opera?Edge79+Edge (Legacy)12+IE11Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[MutationRecord/attributeName](https://developer.mozilla.org/en-US/docs/Web/API/MutationRecord/attributeName)

In all current engines.

Firefox14+Safari7+Chrome16+Opera?Edge79+Edge (Legacy)12+IE11Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[MutationRecord/attributeNamespace](https://developer.mozilla.org/en-US/docs/Web/API/MutationRecord/attributeNamespace)

In all current engines.

Firefox14+Safari7+Chrome16+Opera?Edge79+Edge (Legacy)12+IE11Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[MutationRecord/nextSibling](https://developer.mozilla.org/en-US/docs/Web/API/MutationRecord/nextSibling)

In all current engines.

Firefox14+Safari7+Chrome16+Opera?Edge79+Edge (Legacy)12+IE11Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[MutationRecord/oldValue](https://developer.mozilla.org/en-US/docs/Web/API/MutationRecord/oldValue)

In all current engines.

Firefox14+Safari7+Chrome16+Opera?Edge79+Edge (Legacy)12+IE11Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[MutationRecord/previousSibling](https://developer.mozilla.org/en-US/docs/Web/API/MutationRecord/previousSibling)

In all current engines.

Firefox14+Safari7+Chrome16+Opera?Edge79+Edge (Legacy)12+IE11Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[MutationRecord/removedNodes](https://developer.mozilla.org/en-US/docs/Web/API/MutationRecord/removedNodes)

In all current engines.

Firefox14+Safari7+Chrome16+Opera?Edge79+Edge (Legacy)12+IE11Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[MutationRecord/target](https://developer.mozilla.org/en-US/docs/Web/API/MutationRecord/target)

In all current engines.

Firefox14+Safari7+Chrome16+Opera?Edge79+Edge (Legacy)12+IE11Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[MutationRecord/type](https://developer.mozilla.org/en-US/docs/Web/API/MutationRecord/type)

In all current engines.

Firefox14+Safari7+Chrome16+Opera?Edge79+Edge (Legacy)12+IE11Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[MutationRecord](https://developer.mozilla.org/en-US/docs/Web/API/MutationRecord)

In all current engines.

Firefox14+Safari7+Chrome16+Opera?Edge79+Edge (Legacy)12+IE11Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[NamedNodeMap/getNamedItem](https://developer.mozilla.org/en-US/docs/Web/API/NamedNodeMap/getNamedItem)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[NamedNodeMap/getNamedItemNS](https://developer.mozilla.org/en-US/docs/Web/API/NamedNodeMap/getNamedItemNS)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[NamedNodeMap/item](https://developer.mozilla.org/en-US/docs/Web/API/NamedNodeMap/item)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[NamedNodeMap/length](https://developer.mozilla.org/en-US/docs/Web/API/NamedNodeMap/length)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[NamedNodeMap/removeNamedItem](https://developer.mozilla.org/en-US/docs/Web/API/NamedNodeMap/removeNamedItem)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[NamedNodeMap/removeNamedItemNS](https://developer.mozilla.org/en-US/docs/Web/API/NamedNodeMap/removeNamedItemNS)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[NamedNodeMap/setNamedItem](https://developer.mozilla.org/en-US/docs/Web/API/NamedNodeMap/setNamedItem)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[NamedNodeMap/setNamedItemNS](https://developer.mozilla.org/en-US/docs/Web/API/NamedNodeMap/setNamedItemNS)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[NamedNodeMap](https://developer.mozilla.org/en-US/docs/Web/API/NamedNodeMap)

In all current engines.

Firefox34+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Node/appendChild](https://developer.mozilla.org/en-US/docs/Web/API/Node/appendChild)

In all current engines.

Firefox1+Safari1.1+Chrome1+Opera7+Edge79+Edge (Legacy)12+IE5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Node/baseURI](https://developer.mozilla.org/en-US/docs/Web/API/Node/baseURI)

In all current engines.

Firefox1+Safari4+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Node/childNodes](https://developer.mozilla.org/en-US/docs/Web/API/Node/childNodes)

In all current engines.

Firefox1+Safari1.2+Chrome1+Opera7+Edge79+Edge (Legacy)12+IE5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Node/cloneNode](https://developer.mozilla.org/en-US/docs/Web/API/Node/cloneNode)

In all current engines.

Firefox1+Safari1.1+Chrome1+Opera7+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Node/compareDocumentPosition](https://developer.mozilla.org/en-US/docs/Web/API/Node/compareDocumentPosition)

In all current engines.

Firefox1+Safari4+Chrome2+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView37+Samsung Internet?Opera Mobile12.1+✔MDN

[Node/contains](https://developer.mozilla.org/en-US/docs/Web/API/Node/contains)

In all current engines.

Firefox9+Safari1.1+Chrome16+Opera7+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Node/firstChild](https://developer.mozilla.org/en-US/docs/Web/API/Node/firstChild)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Node/getRootNode](https://developer.mozilla.org/en-US/docs/Web/API/Node/getRootNode)

In all current engines.

Firefox53+Safari10.1+Chrome54+Opera?Edge79+Edge (Legacy)?IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[Node/hasChildNodes](https://developer.mozilla.org/en-US/docs/Web/API/Node/hasChildNodes)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Node/insertBefore](https://developer.mozilla.org/en-US/docs/Web/API/Node/insertBefore)

In all current engines.

Firefox1+Safari1.1+Chrome1+Opera7+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Node/isConnected](https://developer.mozilla.org/en-US/docs/Web/API/Node/isConnected)

In all current engines.

Firefox49+Safari10+Chrome51+Opera?Edge79+Edge (Legacy)?IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet6.0+Opera Mobile?✔MDN

[Node/isDefaultNamespace](https://developer.mozilla.org/en-US/docs/Web/API/Node/isDefaultNamespace)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Node/isEqualNode](https://developer.mozilla.org/en-US/docs/Web/API/Node/isEqualNode)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Node/isSameNode](https://developer.mozilla.org/en-US/docs/Web/API/Node/isSameNode)

In all current engines.

Firefox48+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Node/lastChild](https://developer.mozilla.org/en-US/docs/Web/API/Node/lastChild)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE6+Firefox for Android45+iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Node/lookupNamespaceURI](https://developer.mozilla.org/en-US/docs/Web/API/Node/lookupNamespaceURI)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Node/lookupPrefix](https://developer.mozilla.org/en-US/docs/Web/API/Node/lookupPrefix)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Node/nextSibling](https://developer.mozilla.org/en-US/docs/Web/API/Node/nextSibling)

In all current engines.

Firefox1+Safari1.1+Chrome1+Opera7+Edge79+Edge (Legacy)12+IE5.5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Node/nodeName](https://developer.mozilla.org/en-US/docs/Web/API/Node/nodeName)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Node/nodeType](https://developer.mozilla.org/en-US/docs/Web/API/Node/nodeType)

In all current engines.

Firefox1+Safari1.1+Chrome1+Opera7+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Node/nodeValue](https://developer.mozilla.org/en-US/docs/Web/API/Node/nodeValue)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Node/normalize](https://developer.mozilla.org/en-US/docs/Web/API/Node/normalize)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Node/ownerDocument](https://developer.mozilla.org/en-US/docs/Web/API/Node/ownerDocument)

In all current engines.

Firefox9+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Node/parentElement](https://developer.mozilla.org/en-US/docs/Web/API/Node/parentElement)

In all current engines.

Firefox9+Safari1.1+Chrome1+Opera7+Edge79+Edge (Legacy)12+IE8+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Node/parentNode](https://developer.mozilla.org/en-US/docs/Web/API/Node/parentNode)

In all current engines.

Firefox1+Safari1.1+Chrome1+Opera7+Edge79+Edge (Legacy)12+IE5.5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Node/previousSibling](https://developer.mozilla.org/en-US/docs/Web/API/Node/previousSibling)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE5.5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Node/removeChild](https://developer.mozilla.org/en-US/docs/Web/API/Node/removeChild)

In all current engines.

Firefox1+Safari1.1+Chrome1+Opera7+Edge79+Edge (Legacy)12+IE5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Node/replaceChild](https://developer.mozilla.org/en-US/docs/Web/API/Node/replaceChild)

In all current engines.

Firefox1+Safari1.1+Chrome1+Opera7+Edge79+Edge (Legacy)12+IE6+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Node/textContent](https://developer.mozilla.org/en-US/docs/Web/API/Node/textContent)

In all current engines.

Firefox1+Safari3+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Node](https://developer.mozilla.org/en-US/docs/Web/API/Node)

In all current engines.

Firefox1+Safari1+Chrome1+Opera7+Edge79+Edge (Legacy)12+IE5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView37+Samsung Internet?Opera Mobile10.1+✔MDN

[NodeIterator/filter](https://developer.mozilla.org/en-US/docs/Web/API/NodeIterator/filter)

In all current engines.

Firefox3.5+Safari3+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[NodeIterator/nextNode](https://developer.mozilla.org/en-US/docs/Web/API/NodeIterator/nextNode)

In all current engines.

Firefox3.5+Safari3+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[NodeIterator/pointerBeforeReferenceNode](https://developer.mozilla.org/en-US/docs/Web/API/NodeIterator/pointerBeforeReferenceNode)

In all current engines.

Firefox3.5+Safari3+Chrome1+Opera15+Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari3+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile14+✔MDN

[NodeIterator/previousNode](https://developer.mozilla.org/en-US/docs/Web/API/NodeIterator/previousNode)

In all current engines.

Firefox3.5+Safari3+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[NodeIterator/referenceNode](https://developer.mozilla.org/en-US/docs/Web/API/NodeIterator/referenceNode)

In all current engines.

Firefox3.5+Safari3+Chrome1+Opera15+Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari3+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile14+✔MDN

[NodeIterator/root](https://developer.mozilla.org/en-US/docs/Web/API/NodeIterator/root)

In all current engines.

Firefox3.5+Safari3+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[NodeIterator/whatToShow](https://developer.mozilla.org/en-US/docs/Web/API/NodeIterator/whatToShow)

In all current engines.

Firefox3.5+Safari3+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[NodeIterator](https://developer.mozilla.org/en-US/docs/Web/API/NodeIterator)

In all current engines.

Firefox3.5+Safari3+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[NodeList/forEach](https://developer.mozilla.org/en-US/docs/Web/API/NodeList/forEach)

In all current engines.

Firefox50+Safari10+Chrome51+Opera?Edge79+Edge (Legacy)16+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[Reference/Global_Objects/Array/@@iterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/@@iterator)

In all current engines.

Firefox36+Safari10+Chrome51+Opera?Edge79+Edge (Legacy)?IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?

[NodeList](https://developer.mozilla.org/en-US/docs/Web/API/NodeList)

In all current engines.

Firefox1+Safari1+Chrome1+Opera8+Edge79+Edge (Legacy)12+IE5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[NodeList/item](https://developer.mozilla.org/en-US/docs/Web/API/NodeList/item)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[NodeList/length](https://developer.mozilla.org/en-US/docs/Web/API/NodeList/length)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[ProcessingInstruction/target](https://developer.mozilla.org/en-US/docs/Web/API/ProcessingInstruction/target)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[ProcessingInstruction](https://developer.mozilla.org/en-US/docs/Web/API/ProcessingInstruction)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Range/Range](https://developer.mozilla.org/en-US/docs/Web/API/Range/Range)

In all current engines.

Firefox24+Safari8+Chrome29+Opera?Edge79+Edge (Legacy)15+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[Range/cloneContents](https://developer.mozilla.org/en-US/docs/Web/API/Range/cloneContents)

In all current engines.

Firefox1+Safari1+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Range/cloneRange](https://developer.mozilla.org/en-US/docs/Web/API/Range/cloneRange)

In all current engines.

Firefox1+Safari1+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Range/collapse](https://developer.mozilla.org/en-US/docs/Web/API/Range/collapse)

In all current engines.

Firefox1+Safari1+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Range/commonAncestorContainer](https://developer.mozilla.org/en-US/docs/Web/API/Range/commonAncestorContainer)

In all current engines.

Firefox1+Safari1+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Range/compareBoundaryPoints](https://developer.mozilla.org/en-US/docs/Web/API/Range/compareBoundaryPoints)

In all current engines.

Firefox1+Safari1+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Range/comparePoint](https://developer.mozilla.org/en-US/docs/Web/API/Range/comparePoint)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)17+IENoneFirefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Range/deleteContents](https://developer.mozilla.org/en-US/docs/Web/API/Range/deleteContents)

In all current engines.

Firefox1+Safari1+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+MDN

[Range/detach](https://developer.mozilla.org/en-US/docs/Web/API/Range/detach)

Firefox1–15Safari1+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Range/extractContents](https://developer.mozilla.org/en-US/docs/Web/API/Range/extractContents)

In all current engines.

Firefox1+Safari1+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Range/insertNode](https://developer.mozilla.org/en-US/docs/Web/API/Range/insertNode)

In all current engines.

Firefox1+Safari1+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Range/intersectsNode](https://developer.mozilla.org/en-US/docs/Web/API/Range/intersectsNode)

In all current engines.

Firefox17+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)17+IENoneFirefox for Android19+iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Range/isPointInRange](https://developer.mozilla.org/en-US/docs/Web/API/Range/isPointInRange)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)15+IENoneFirefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Range/selectNode](https://developer.mozilla.org/en-US/docs/Web/API/Range/selectNode)

In all current engines.

Firefox1+Safari1+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Range/selectNodeContents](https://developer.mozilla.org/en-US/docs/Web/API/Range/selectNodeContents)

In all current engines.

Firefox1+Safari1+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Range/setEnd](https://developer.mozilla.org/en-US/docs/Web/API/Range/setEnd)

In all current engines.

Firefox1+Safari1+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Range/setEndAfter](https://developer.mozilla.org/en-US/docs/Web/API/Range/setEndAfter)

In all current engines.

Firefox1+Safari1+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Range/setEndBefore](https://developer.mozilla.org/en-US/docs/Web/API/Range/setEndBefore)

In all current engines.

Firefox1+Safari1+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Range/setStart](https://developer.mozilla.org/en-US/docs/Web/API/Range/setStart)

In all current engines.

Firefox1+Safari1+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Range/setStartAfter](https://developer.mozilla.org/en-US/docs/Web/API/Range/setStartAfter)

In all current engines.

Firefox1+Safari1+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Range/setStartBefore](https://developer.mozilla.org/en-US/docs/Web/API/Range/setStartBefore)

In all current engines.

Firefox1+Safari1+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Range/surroundContents](https://developer.mozilla.org/en-US/docs/Web/API/Range/surroundContents)

In all current engines.

Firefox1+Safari1+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Range/toString](https://developer.mozilla.org/en-US/docs/Web/API/Range/toString)

In all current engines.

Firefox1+Safari1+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[Range](https://developer.mozilla.org/en-US/docs/Web/API/Range)

In all current engines.

Firefox1+Safari1+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile10.1+✔MDN

[ShadowRoot/delegatesFocus](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot/delegatesFocus)

In all current engines.

Firefox94+Safari15+Chrome53+Opera?Edge79+Edge (Legacy)?IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[ShadowRoot/host](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot/host)

In all current engines.

Firefox63+Safari10+Chrome53+Opera?Edge79+Edge (Legacy)?IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[ShadowRoot/mode](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot/mode)

In all current engines.

Firefox63+Safari10.1+Chrome53+Opera?Edge79+Edge (Legacy)?IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[ShadowRoot/slotAssignment](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot/slotAssignment)

In all current engines.

Firefox92+Safari16.4+Chrome86+Opera?Edge86+Edge (Legacy)?IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[ShadowRoot](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot)

In all current engines.

Firefox63+Safari10+Chrome53+Opera?Edge79+Edge (Legacy)?IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[StaticRange/StaticRange](https://developer.mozilla.org/en-US/docs/Web/API/StaticRange/StaticRange)

In all current engines.

Firefox71+Safari13.1+Chrome90+Opera?Edge90+Edge (Legacy)?IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[StaticRange](https://developer.mozilla.org/en-US/docs/Web/API/StaticRange)

In all current engines.

Firefox69+Safari10.1+Chrome60+Opera?Edge79+Edge (Legacy)18IENoneFirefox for Android79+iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[Text/Text](https://developer.mozilla.org/en-US/docs/Web/API/Text/Text)

In all current engines.

Firefox24+Safari8+Chrome29+Opera?Edge79+Edge (Legacy)16+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?✔MDN

[Text/splitText](https://developer.mozilla.org/en-US/docs/Web/API/Text/splitText)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView1+Samsung Internet?Opera Mobile12.1+✔MDN

[Text/wholeText](https://developer.mozilla.org/en-US/docs/Web/API/Text/wholeText)

In all current engines.

Firefox3.5+Safari4+Chrome2+Opera12.1+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[Text](https://developer.mozilla.org/en-US/docs/Web/API/Text)

In all current engines.

Firefox1+Safari1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IE5+Firefox for Android?iOS Safari?Chrome for Android?Android WebView37+Samsung Internet?Opera Mobile12.1+✔MDN

[TreeWalker/currentNode](https://developer.mozilla.org/en-US/docs/Web/API/TreeWalker/currentNode)

In all current engines.

Firefox4+Safari3+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile10.1+✔MDN

[TreeWalker/filter](https://developer.mozilla.org/en-US/docs/Web/API/TreeWalker/filter)

In all current engines.

Firefox4+Safari3+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile10.1+✔MDN

[TreeWalker/firstChild](https://developer.mozilla.org/en-US/docs/Web/API/TreeWalker/firstChild)

In all current engines.

Firefox4+Safari3+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile10.1+✔MDN

[TreeWalker/lastChild](https://developer.mozilla.org/en-US/docs/Web/API/TreeWalker/lastChild)

In all current engines.

Firefox4+Safari3+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile10.1+✔MDN

[TreeWalker/nextNode](https://developer.mozilla.org/en-US/docs/Web/API/TreeWalker/nextNode)

In all current engines.

Firefox4+Safari3+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile10.1+✔MDN

[TreeWalker/nextSibling](https://developer.mozilla.org/en-US/docs/Web/API/TreeWalker/nextSibling)

In all current engines.

Firefox4+Safari3+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile10.1+✔MDN

[TreeWalker/parentNode](https://developer.mozilla.org/en-US/docs/Web/API/TreeWalker/parentNode)

In all current engines.

Firefox4+Safari3+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile10.1+✔MDN

[TreeWalker/previousNode](https://developer.mozilla.org/en-US/docs/Web/API/TreeWalker/previousNode)

In all current engines.

Firefox4+Safari3+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile10.1+✔MDN

[TreeWalker/previousSibling](https://developer.mozilla.org/en-US/docs/Web/API/TreeWalker/previousSibling)

In all current engines.

Firefox4+Safari3+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile10.1+✔MDN

[TreeWalker/root](https://developer.mozilla.org/en-US/docs/Web/API/TreeWalker/root)

In all current engines.

Firefox4+Safari3+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile10.1+✔MDN

[TreeWalker/whatToShow](https://developer.mozilla.org/en-US/docs/Web/API/TreeWalker/whatToShow)

In all current engines.

Firefox4+Safari3+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile10.1+✔MDN

[TreeWalker](https://developer.mozilla.org/en-US/docs/Web/API/TreeWalker)

In all current engines.

Firefox4+Safari3+Chrome1+Opera9+Edge79+Edge (Legacy)12+IE9+Firefox for Android?iOS Safari3+Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile10.1+✔MDN

[XMLDocument](https://developer.mozilla.org/en-US/docs/Web/API/XMLDocument)

In all current engines.

Firefox1+Safari10+Chrome34+Opera21+Edge79+Edge (Legacy)12+IE11Firefox for Android?iOS Safari10+Chrome for Android?Android WebView37+Samsung Internet?Opera Mobile21+✔MDN

[XPathEvaluator/XPathEvaluator](https://developer.mozilla.org/en-US/docs/Web/API/XPathEvaluator/XPathEvaluator)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[XPathEvaluator](https://developer.mozilla.org/en-US/docs/Web/API/XPathEvaluator)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[XPathExpression/evaluate](https://developer.mozilla.org/en-US/docs/Web/API/XPathExpression/evaluate)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[XPathExpression](https://developer.mozilla.org/en-US/docs/Web/API/XPathExpression)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[XPathResult/booleanValue](https://developer.mozilla.org/en-US/docs/Web/API/XPathResult/booleanValue)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[XPathResult/invalidIteratorState](https://developer.mozilla.org/en-US/docs/Web/API/XPathResult/invalidIteratorState)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari1+Chrome for Android?Android WebView37+Samsung Internet?Opera Mobile12.1+✔MDN

[XPathResult/iterateNext](https://developer.mozilla.org/en-US/docs/Web/API/XPathResult/iterateNext)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[XPathResult/numberValue](https://developer.mozilla.org/en-US/docs/Web/API/XPathResult/numberValue)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[XPathResult/resultType](https://developer.mozilla.org/en-US/docs/Web/API/XPathResult/resultType)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari1+Chrome for Android?Android WebView37+Samsung Internet?Opera Mobile12.1+✔MDN

[XPathResult/singleNodeValue](https://developer.mozilla.org/en-US/docs/Web/API/XPathResult/singleNodeValue)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[XPathResult/snapshotItem](https://developer.mozilla.org/en-US/docs/Web/API/XPathResult/snapshotItem)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[XPathResult/snapshotLength](https://developer.mozilla.org/en-US/docs/Web/API/XPathResult/snapshotLength)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[XPathResult/stringValue](https://developer.mozilla.org/en-US/docs/Web/API/XPathResult/stringValue)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[XPathResult](https://developer.mozilla.org/en-US/docs/Web/API/XPathResult)

In all current engines.

Firefox1+Safari3+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari1+Chrome for Android?Android WebView?Samsung Internet?Opera Mobile12.1+✔MDN

[XSLTProcessor/XSLTProcessor](https://developer.mozilla.org/en-US/docs/Web/API/XSLTProcessor/XSLTProcessor)

In all current engines.

Firefox1+Safari3.1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile12.1+✔MDN

[XSLTProcessor/clearParameters](https://developer.mozilla.org/en-US/docs/Web/API/XSLTProcessor/clearParameters)

In all current engines.

Firefox1+Safari3.1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile12.1+✔MDN

[XSLTProcessor/getParameter](https://developer.mozilla.org/en-US/docs/Web/API/XSLTProcessor/getParameter)

In all current engines.

Firefox1+Safari3.1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile12.1+✔MDN

[XSLTProcessor/importStylesheet](https://developer.mozilla.org/en-US/docs/Web/API/XSLTProcessor/importStylesheet)

In all current engines.

Firefox1+Safari3.1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile12.1+✔MDN

[XSLTProcessor/removeParameter](https://developer.mozilla.org/en-US/docs/Web/API/XSLTProcessor/removeParameter)

In all current engines.

Firefox1+Safari3.1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile12.1+✔MDN

[XSLTProcessor/reset](https://developer.mozilla.org/en-US/docs/Web/API/XSLTProcessor/reset)

In all current engines.

Firefox1+Safari3.1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile12.1+✔MDN

[XSLTProcessor/setParameter](https://developer.mozilla.org/en-US/docs/Web/API/XSLTProcessor/setParameter)

In all current engines.

Firefox1+Safari3.1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile12.1+✔MDN

[XSLTProcessor/transformToDocument](https://developer.mozilla.org/en-US/docs/Web/API/XSLTProcessor/transformToDocument)

In all current engines.

Firefox1+Safari3.1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile12.1+✔MDN

[XSLTProcessor/transformToFragment](https://developer.mozilla.org/en-US/docs/Web/API/XSLTProcessor/transformToFragment)

In all current engines.

Firefox1+Safari3.1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile12.1+✔MDN

[XSLTProcessor](https://developer.mozilla.org/en-US/docs/Web/API/XSLTProcessor)

In all current engines.

Firefox1+Safari3.1+Chrome1+Opera12.1+Edge79+Edge (Legacy)12+IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView3+Samsung Internet?Opera Mobile12.1+✔MDN

[Element/slot](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/slot)

In all current engines.

Firefox63+Safari10+Chrome53+Opera?Edge79+Edge (Legacy)?IENoneFirefox for Android?iOS Safari?Chrome for Android?Android WebView?Samsung Internet?Opera Mobile?
