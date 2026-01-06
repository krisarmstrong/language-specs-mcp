# CustomElementRegistry

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCustomElementRegistry&level=high)

The `CustomElementRegistry` interface provides methods for registering custom elements and querying registered elements. To get an instance of it, use the [window.customElements](/en-US/docs/Web/API/Window/customElements) property.

## In this article

- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance methods](#instance_methods)

[CustomElementRegistry.define()](/en-US/docs/Web/API/CustomElementRegistry/define)

Defines a new [custom element](/en-US/docs/Web/API/Web_components/Using_custom_elements).

[CustomElementRegistry.get()](/en-US/docs/Web/API/CustomElementRegistry/get)

Returns the constructor for the named custom element, or [undefined](/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined) if the custom element is not defined.

[CustomElementRegistry.getName()](/en-US/docs/Web/API/CustomElementRegistry/getName)

Returns the name for the already-defined custom element, or `null` if the custom element is not defined.

[CustomElementRegistry.upgrade()](/en-US/docs/Web/API/CustomElementRegistry/upgrade)

Upgrades a custom element directly, even before it is connected to its shadow root.

[CustomElementRegistry.whenDefined()](/en-US/docs/Web/API/CustomElementRegistry/whenDefined)

Returns an empty [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when a custom element becomes defined with the given name. If such a custom element is already defined, the returned promise is immediately fulfilled.

## [Examples](#examples)

See the [Examples](/en-US/docs/Web/API/Web_components/Using_custom_elements#examples) section in our [guide to using custom elements](/en-US/docs/Web/API/Web_components/Using_custom_elements).

## [Specifications](#specifications)

Specification
[HTML# custom-elements-api](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements-api)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 27, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/CustomElementRegistry/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/customelementregistry/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCustomElementRegistry&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcustomelementregistry%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCustomElementRegistry%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcustomelementregistry%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F55fe0ef0be11c6d18012d18b355d46f9df60c4db%0A*+Document+last+modified%3A+2023-09-27T02%3A06%3A18.000Z%0A%0A%3C%2Fdetails%3E)
