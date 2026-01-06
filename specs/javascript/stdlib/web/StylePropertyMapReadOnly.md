# StylePropertyMapReadOnly

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStylePropertyMapReadOnly&level=not)

The `StylePropertyMapReadOnly` interface of the [CSS Typed Object Model API](/en-US/docs/Web/API/CSS_Object_Model#css_typed_object_model) provides a read-only representation of a CSS declaration block that is an alternative to [CSSStyleDeclaration](/en-US/docs/Web/API/CSSStyleDeclaration). Retrieve an instance of this interface using [Element.computedStyleMap()](/en-US/docs/Web/API/Element/computedStyleMap).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[StylePropertyMapReadOnly.size](/en-US/docs/Web/API/StylePropertyMapReadOnly/size)

Returns an unsigned long integer containing the size of the `StylePropertyMapReadOnly` object.

## [Instance methods](#instance_methods)

[StylePropertyMapReadOnly.entries()](/en-US/docs/Web/API/StylePropertyMapReadOnly/entries)

Returns an array of a given object's own enumerable property `[key, value]` pairs, in the same order as that provided by a [for...in](/en-US/docs/Web/JavaScript/Reference/Statements/for...in) loop (the difference being that a for-in loop enumerates properties in the prototype chain as well).

[StylePropertyMapReadOnly.forEach()](/en-US/docs/Web/API/StylePropertyMapReadOnly/forEach)

Executes a provided function once for each element of `StylePropertyMapReadOnly`.

[StylePropertyMapReadOnly.get()](/en-US/docs/Web/API/StylePropertyMapReadOnly/get)

Returns the value of the specified property.

[StylePropertyMapReadOnly.getAll()](/en-US/docs/Web/API/StylePropertyMapReadOnly/getAll)

Returns an array of [CSSStyleValue](/en-US/docs/Web/API/CSSStyleValue) objects containing the values for the provided property.

[StylePropertyMapReadOnly.has()](/en-US/docs/Web/API/StylePropertyMapReadOnly/has)

Indicates whether the specified property is in the `StylePropertyMapReadOnly` object.

[StylePropertyMapReadOnly.keys()](/en-US/docs/Web/API/StylePropertyMapReadOnly/keys)

Returns a new array iterator containing the keys for each item in `StylePropertyMapReadOnly`.

[StylePropertyMapReadOnly.values()](/en-US/docs/Web/API/StylePropertyMapReadOnly/values)

Returns a new array iterator containing the values for each index in the `StylePropertyMapReadOnly` object.

## [Examples](#examples)

We have to have an element to observe:

html

```
<p>
  This is a paragraph with some text. We can add some CSS, or not. The style map
  will include all the default and inherited CSS property values.
</p>
<dl id="output"></dl>
```

We add a touch of CSS with a custom property to better demonstrate the output:

css

```
p {
  --some-variable: 1.6em;
  --some-other-variable: translateX(33vw);
  --another-variable: 42;
  line-height: var(--some-variable);
}
```

We add JavaScript to grab our paragraph and return back a definition list of all the default CSS property values using [Element.computedStyleMap()](/en-US/docs/Web/API/Element/computedStyleMap).

js

```
// get the element
const myElement = document.querySelector("p");

// get the <dl> we'll be populating
const stylesList = document.querySelector("#output");

// Retrieve all computed styles with computedStyleMap()
const stylePropertyMap = myElement.computedStyleMap();

// iterate through the map of all the properties and values, adding a <dt> and <dd> for each
for (const [prop, val] of stylePropertyMap) {
  // properties
  const cssProperty = document.createElement("dt");
  cssProperty.innerText = prop;
  stylesList.appendChild(cssProperty);

  // values
  const cssValue = document.createElement("dd");
  cssValue.innerText = val;
  stylesList.appendChild(cssValue);
}
```

## [Specifications](#specifications)

Specification
[CSS Typed OM Level 1# the-stylepropertymap](https://drafts.css-houdini.org/css-typed-om/#the-stylepropertymap)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 5, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/StylePropertyMapReadOnly/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/stylepropertymapreadonly/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStylePropertyMapReadOnly&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fstylepropertymapreadonly%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStylePropertyMapReadOnly%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fstylepropertymapreadonly%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F635820782735cd00f71ce3929ff9377b091f8995%0A*+Document+last+modified%3A+2025-08-05T14%3A01%3A02.000Z%0A%0A%3C%2Fdetails%3E)
