# SanitizerConfig

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `SanitizerConfig` dictionary of the [HTML Sanitizer API](/en-US/docs/Web/API/HTML_Sanitizer_API) specifies what elements, attributes and comments are allowed or should be removed when inserting strings of HTML into an [Element](/en-US/docs/Web/API/Element) or [ShadowRoot](/en-US/docs/Web/API/ShadowRoot), or when parsing an HTML string into a [Document](/en-US/docs/Web/API/Document).

Note that normally [Sanitizer](/en-US/docs/Web/API/Sanitizer) instances are used instead of `SanitizerConfig` objects, as they are more efficient to share and modify.

## In this article

- [Instance properties](#instance_properties)
- [Description](#description)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[elements](#elements)

An array indicating the elements to allow when sanitizing HTML, optionally also specifying their allowed or removed attributes.

Each element can be specified by name (a string), or as an object with the following properties:

[name](#name)

A string containing the name of the element.

[namespace Optional](#namespace)

A string containing the namespace of the element. The default namespace is `"http://www.w3.org/1999/xhtml"`.

[attributes Optional](#attributes)

An array indicating the attributes to allow on this (allowed) element when sanitizing HTML.

Each attribute can be specified by name (a string), or as an object with the following properties:

[name](#name_2)

A string containing the name of the attribute.

[namespace Optional](#namespace_2)

A string containing the namespace of the attribute, which defaults to `null`.

[removeAttributes Optional](#removeattributes)

An array indicating the attributes to remove on this (allowed) element when sanitizing HTML.

Each attribute can be specified by name (a string), or as an object with the following properties:

[name](#name_3)

A string containing the name of the attribute.

[namespace Optional](#namespace_3)

A string containing the namespace of the attribute, which defaults to `null`.

[removeElements](#removeelements)

An array indicating the elements to remove when sanitizing HTML.

Each element can be specified by name (a string), or as an object with the following properties:

[name](#name_4)

A string containing the name of the element.

[namespace Optional](#namespace_4)

A string containing the namespace of the element. The default namespace is `"http://www.w3.org/1999/xhtml"`.

[replaceWithChildrenElements](#replacewithchildrenelements)

An array indicating the elements to replace with their content when sanitizing HTML. This is primarily used to strip styles from text (for example, you could use this to change `<b>some text</b>` to `some text`).

Each element can be specified by name (a string), or as an object with the following properties:

[name](#name_5)

A string containing the name of the element.

[namespace Optional](#namespace_5)

A string containing the namespace of the element. The default namespace is `"http://www.w3.org/1999/xhtml"`.

[attributes](#attributes_2)

An array indicating the attributes to allow when sanitizing HTML.

Each attribute can be specified by name (a string), or as an object with the following properties:

[name](#name_6)

A string containing the name of the attribute.

[namespace Optional](#namespace_6)

A string containing the namespace of the attribute, which defaults to `null`.

[removeAttributes](#removeattributes_2)

An array indicating the attributes to remove from elements when sanitizing HTML.

Each attribute can be specified by name (a string), or as an object with the following properties:

[name](#name_7)

A string containing the name of the attribute.

[namespace Optional](#namespace_7)

A string containing the namespace of the attribute, which defaults to `null`.

[comments](#comments)

`true` if comments are allowed, and `false` if they are to be removed.

[dataAttributes](#dataattributes)

`true` if all `data-*` attributes will be allowed (in which case `data-*` attributes must not be listed in the `attributes` array). If `false`, any `data-*` attributes to be allowed must be listed in the `attributes` array.

## [Description](#description)

A `SanitizerConfig` specifies what elements, attributes and comments are allowed or should be removed when inserting strings of HTML into an [Element](/en-US/docs/Web/API/Element) or [ShadowRoot](/en-US/docs/Web/API/ShadowRoot), or when parsing an HTML string into a [Document](/en-US/docs/Web/API/Document).

An instance of this type can be passed to the [Sanitizer()](/en-US/docs/Web/API/Sanitizer/Sanitizer) constructor to configure a [Sanitizer](/en-US/docs/Web/API/Sanitizer), and is returned by [Sanitizer.get()](/en-US/docs/Web/API/Sanitizer/get). It can also be passed as the `option.sanitizer` parameter when calling the [sanitization methods](/en-US/docs/Web/API/HTML_Sanitizer_API#sanitization_methods):

- [setHTML()](/en-US/docs/Web/API/Element/setHTML) or [setHTMLUnsafe()](/en-US/docs/Web/API/Element/setHTMLUnsafe) on [Element](/en-US/docs/Web/API/Element).
- [setHTML()](/en-US/docs/Web/API/ShadowRoot/setHTML) or [setHTMLUnsafe()](/en-US/docs/Web/API/ShadowRoot/setHTMLUnsafe) on [ShadowRoot](/en-US/docs/Web/API/ShadowRoot).
- [Document.parseHTML()](/en-US/docs/Web/API/Document/parseHTML_static) or [Document.parseHTMLUnsafe()](/en-US/docs/Web/API/Document/parseHTMLUnsafe_static) static methods.

### [Valid configuration](#valid_configuration)

The configuration object structure allows for the declaration of filter options that are contradictory or redundant, such as specifying an element in both allow and remove lists, or listing an attribute in a list multiple times. In order to avoid any ambiguity, methods that take a `SanitizerConfig` instance require that a valid configuration object be passed, and will throw a [TypeError](/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError) if an invalid configuration is used.

In a valid sanitizer configuration:

- 

Either the `elements` or `removeElements` array may be defined, but not both.

Note: It is impossible to define per-element attributes if the `removeElements` array is defined, because these are added to elements in the `elements` array.

- 

Either the global `attributes` or `removeAttributes` array may be defined, but not both

- 

The `replaceWithChildrenElements` array, if defined, may not have any elements in common with `elements` or `removeElements`

- 

No array may contain duplicate elements or attributes

- 

If the global `attributes` array is defined:

  - An element may define any or none of `attributes` and `removeAttributes`
  - An element's `attributes` must not share any values in common with the global `attributes` array
  - An element's `removeAttributes` array may only contain values that are also present in the global `attributes` array.
  - If `dataAttributes` is `true` the global and element attribute arrays must not contain `data-*` attributes (since these will automatically be allowed).

- 

If the global `removeAttributes` array is defined:

  - An element may specify either `attributes` or `removeAttributes`, but not both
  - An element's `attributes` or `removeAttributes` array, depending on which (if either) is defined, must not share any values in common with the global `removeAttributes` array.
  - The `dataAttributes` boolean must not be defined.

The empty object `{}` is a valid configuration.

Note: The conditions above are from the perspective of a web developer. The [validity check defined in the specification](https://wicg.github.io/sanitizer-api/#sanitizerconfig-valid) is slightly different because it is executed after canonicalization of the configuration, such as adding `removeElements` when both are missing, and adding default namespaces.

### [Allow and remove configurations](#allow_and_remove_configurations)

One of the main implications of the previous section is that a valid configuration can specify either `elements` or `removeElements` arrays (but not both) and either the `attributes` or `removeAttributes` arrays (but not both).

A configuration that has the `elements` and/or `attributes` arrays is referred to as an [allow configuration](/en-US/docs/Web/API/HTML_Sanitizer_API#allow_configurations), as it defines the sanitization behavior in terms of the values that are allowed to be present in the output. A [remove configuration](/en-US/docs/Web/API/HTML_Sanitizer_API#remove_configurations) is one that has either of `removeElements` and/or `removeAttributes`, and defines the behavior in terms of the values that will be removed from the output.

## [Examples](#examples)

### [Creating an "allow" configuration](#creating_an_allow_configuration)

This example shows how you might create an "allow" sanitizer configuration that allows specific elements and attributes, replaces [<b>](/en-US/docs/Web/HTML/Reference/Elements/b) elements with their children, allows comments to be included in the output, and requires that `data-*` attributes are explicitly listed in the `attributes` array to be included. The configuration object is passed to the [Sanitizer()](/en-US/docs/Web/API/Sanitizer/Sanitizer) constructor.

js

```
const sanitizer = new Sanitizer({
  elements: ["div", "p", "script"],
  attributes: ["id"],
  replaceWithChildrenElements: ["b"],
  comments: true,
  dataAttributes: false,
});
```

### [Creating a "remove" configuration](#creating_a_remove_configuration)

This example shows how you might create a "remove" sanitizer configuration that removes both elements and attributes.

js

```
const sanitizer = new Sanitizer({
  removeElements: ["span", "script"],
  removeAttributes: ["lang", "id"],
  comments: false,
});
```

### [Allow element and remove attribute configuration](#allow_element_and_remove_attribute_configuration)

This example shows how you might create a "hybrid" sanitizer configuration that allows some elements and removes certain attributes. You might similarly specify a configuration that removes elements and allows attributes.

js

```
const sanitizer = new Sanitizer({
  elements: ["span", "script"],
  removeAttributes: ["lang", "id"],
});
```

Note that you having both allow and remove arrays for elements, or both allow and remove arrays for attributes is not a [valid configuration](#valid_configuration), and would result in a `TypeError`.

### [Invalid configurations](#invalid_configurations)

This sections shows a number of invalid configurations. These will throw a `TypeError`.

Invalid because both `elements` and `removeElements` are defined:

js

```
const sanitizer1 = new Sanitizer({
  elements: ["span", "script"],
  removeElements: ["div", "b"],
});
```

Invalid because [<span>](/en-US/docs/Web/HTML/Reference/Elements/span) is in both `elements` and `replaceWithChildrenElements`:

js

```
const sanitizer2 = new Sanitizer({
  elements: ["span", "div"],
  replaceWithChildrenElements: ["span"],
});
```

Invalid because the redundant attribute `"data-test"` is defined when `dataAttributes` is true:

js

```
const sanitizer3 = new Sanitizer({
  attributes: ["lang", "id", "data-test"],
  dataAttributes: true,
});
```

Invalid because it has `removeAttributes` and `dataAttributes` defined:

js

```
const sanitizer4 = new Sanitizer({
  removeAttributes: ["lang", "id"],
  dataAttributes: true,
});
```

## [Specifications](#specifications)

Specification
[HTML Sanitizer API# dom-sanitizer-get](https://wicg.github.io/sanitizer-api/#dom-sanitizer-get)
[HTML Sanitizer API# dom-sanitizer-sanitizer](https://wicg.github.io/sanitizer-api/#dom-sanitizer-sanitizer)

## [Browser compatibility](#browser_compatibility)

### [api.Sanitizer.get](#api.Sanitizer.get)

### [api.Sanitizer.Sanitizer](#api.Sanitizer.Sanitizer)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SanitizerConfig/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/sanitizerconfig/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSanitizerConfig&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsanitizerconfig%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSanitizerConfig%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsanitizerconfig%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fae4577f45feb1515c2b887255c45ce0694dbb676%0A*+Document+last+modified%3A+2025-12-08T11%3A05%3A22.000Z%0A%0A%3C%2Fdetails%3E)
