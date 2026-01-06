# MutationEvent

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

Non-standard: This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The `MutationEvent` interface provides event properties that are specific to modifications to the Document Object Model (DOM) hierarchy and nodes.

Note: Using mutation events is problematic:

- Their design is [flawed](https://lists.w3.org/Archives/Public/public-webapps/2011JulSep/0779.html).
- Adding DOM mutation listeners to a document [profoundly degrades the performance](https://groups.google.com/g/mozilla.dev.platform/c/L0Lx11u5Bvs?pli=1) of further DOM modifications to that document (making them 1.5 - 7 times slower!). Moreover, removing the listeners does not reverse the damage.
- They have poor cross-browser compatibility: Safari doesn't support `DOMAttrModified` (see [WebKit bug 8191](https://webkit.org/b/8191)) and Firefox doesn't support mutation name events (like `DOMElementNameChanged` and `DOMAttributeNameChanged`).

They have been deprecated in favor of [mutation observers](/en-US/docs/Web/API/MutationObserver). Consider using these instead.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Mutation events list](#mutation_events_list)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent [UIEvent](/en-US/docs/Web/API/UIEvent), and indirectly from [Event](/en-US/docs/Web/API/Event).

[MutationEvent.attrChange](/en-US/docs/Web/API/MutationEvent/attrChange)Read onlyDeprecatedNon-standard

Indicates what kind of change triggered the `DOMAttrModified` event. It can be `MODIFICATION` (`1`), `ADDITION` (`2`) or `REMOVAL` (`3`). It has no meaning for other events and is then set to `0`.

[MutationEvent.attrName](/en-US/docs/Web/API/MutationEvent/attrName)Read onlyDeprecatedNon-standard

Indicates the name of the node affected by the `DOMAttrModified` event. It has no meaning for other events and is then set to the empty string (`""`).

[MutationEvent.newValue](/en-US/docs/Web/API/MutationEvent/newValue)Read onlyDeprecatedNon-standard

In `DOMAttrModified` events, contains the new value of the modified [Attr](/en-US/docs/Web/API/Attr) node. In `DOMCharacterDataModified` events, contains the new value of the modified [CharacterData](/en-US/docs/Web/API/CharacterData) node. In all other cases, returns the empty string (`""`).

[MutationEvent.prevValue](/en-US/docs/Web/API/MutationEvent/prevValue)Read onlyDeprecatedNon-standard

In `DOMAttrModified` events, contains the previous value of the modified [Attr](/en-US/docs/Web/API/Attr) node. In `DOMCharacterDataModified` events, contains previous new value of the modified [CharacterData](/en-US/docs/Web/API/CharacterData) node. In all other cases, returns the empty string (`""`).

[MutationEvent.relatedNode](/en-US/docs/Web/API/MutationEvent/relatedNode)Read onlyDeprecatedNon-standard

Indicates the node related to the event, like the changed node inside the subtree for `DOMSubtreeModified`.

## [Instance methods](#instance_methods)

[MutationEvent.initMutationEvent()](/en-US/docs/Web/API/MutationEvent/initMutationEvent)DeprecatedNon-standard

Constructor method that returns a new `MutationEvent` configured with the parameters given.

## [Mutation events list](#mutation_events_list)

The following is a list of all mutation events:

- `DOMAttrModified` (Not supported by Safari)
- `DOMAttributeNameChanged` (Not supported by Firefox)
- `DOMCharacterDataModified`
- `DOMElementNameChanged` (Not supported by Firefox)
- `DOMNodeInserted`
- `DOMNodeInsertedIntoDocument`
- `DOMNodeRemoved`
- `DOMNodeRemovedFromDocument`
- `DOMSubtreeModified`

## [Examples](#examples)

You can register a listener for mutation events using [EventTarget.addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) as follows:

js

```
element.addEventListener("DOMNodeInserted", (event) => {
  // …
});
```

## [Specifications](#specifications)

This feature does not appear to be defined in any specification.

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [MutationObserver](/en-US/docs/Web/API/MutationObserver)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 18, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/MutationEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mutationevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMutationEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmutationevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMutationEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmutationevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2ccbd062264d0a2a34f185a3386cb272f42c50f5%0A*+Document+last+modified%3A+2025-09-18T15%3A45%3A07.000Z%0A%0A%3C%2Fdetails%3E)
