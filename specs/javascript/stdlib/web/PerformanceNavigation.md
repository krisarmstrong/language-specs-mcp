# PerformanceNavigation

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

The legacy `PerformanceNavigation` interface represents information about how the navigation to the current document was done.

Warning: This interface is deprecated in the [Navigation Timing Level 2 specification](https://w3c.github.io/navigation-timing/#obsolete). Please use the [PerformanceNavigationTiming](/en-US/docs/Web/API/PerformanceNavigationTiming) interface instead.

An object of this type can be obtained by calling the [Performance.navigation](/en-US/docs/Web/API/Performance/navigation) read-only attribute.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

The `PerformanceNavigation` interface doesn't inherit any properties.

[PerformanceNavigation.type](/en-US/docs/Web/API/PerformanceNavigation/type)Read onlyDeprecated

An `unsigned short` which indicates how the navigation to this page was done. Possible values are:

[TYPE_NAVIGATE (0)](#type_navigate)

The page was accessed by following a link, a bookmark, a form submission, or a script, or by typing the URL in the address bar.

[TYPE_RELOAD (1)](#type_reload)

The page was accessed by clicking the Reload button or via the [Location.reload()](/en-US/docs/Web/API/Location/reload) method.

[TYPE_BACK_FORWARD (2)](#type_back_forward)

The page was accessed by navigating into the history.

[TYPE_RESERVED (255)](#type_reserved)

Any other way.

[PerformanceNavigation.redirectCount](/en-US/docs/Web/API/PerformanceNavigation/redirectCount)Read onlyDeprecated

An `unsigned short` representing the number of REDIRECTs done before reaching the page.

## [Instance methods](#instance_methods)

The `Performance` interface doesn't inherit any methods.

[PerformanceNavigation.toJSON()](/en-US/docs/Web/API/PerformanceNavigation/toJSON)Deprecated

A [serializer](/en-US/docs/Glossary/Serialization) returning a JSON object representing the `PerformanceNavigation` object.

## [Specifications](#specifications)

Specification
[Navigation Timing Level 2# dom-performancenavigation](https://w3c.github.io/navigation-timing/#dom-performancenavigation)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [Performance](/en-US/docs/Web/API/Performance) that allows access to an object of this type.
- [PerformanceNavigationTiming](/en-US/docs/Web/API/PerformanceNavigationTiming) (part of Navigation Timing Level 2) that has superseded this API.

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/PerformanceNavigation/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/performancenavigation/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceNavigation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fperformancenavigation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceNavigation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fperformancenavigation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
