# CSSPositionValue

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

Non-standard: This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The `CSSPositionValue` interface of the [CSS Typed Object Model API](/en-US/docs/Web/API/CSS_Object_Model#css_typed_object_model) represents values for properties that take a position, for example [object-position](/en-US/docs/Web/CSS/Reference/Properties/object-position).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[CSSPositionValue()](/en-US/docs/Web/API/CSSPositionValue/CSSPositionValue)Non-standardDeprecated

Creates a new `CSSPositionValue` object.

## [Instance properties](#instance_properties)

[CSSPositionValue.x](/en-US/docs/Web/API/CSSPositionValue/x)Non-standardDeprecated

Returns the item's position along the web page's horizontal axis.

[CSSPositionValue.y](/en-US/docs/Web/API/CSSPositionValue/y)Non-standardDeprecated

Returns the item's position along the vertical axis.

## [Instance methods](#instance_methods)

None.

## [Examples](#examples)

The following example positions a container `<div>` 5 pixels from the top and 10 pixels from the left of the page.

js

```
const replacedEl = document.getElementById("image");
const position = new CSSPositionValue(CSS.px(35), CSS.px(40));

replacedEl.attributeStyleMap.set("object-position", position);
console.log(position.x.value, position.y.value);
console.log(replacedEl.computedStyleMap().get("object-position"));
```

We set the [object-position](/en-US/docs/Web/CSS/Reference/Properties/object-position) property, then check the values returned.

```
#image {
  width: 300px;
  height: 300px;
  border: 1px solid black;
  background-color: #dededf;
  object-fit: none;
}
```

```
<p>
  Check the developer tools to see the log in the console and to inspect the
  style attribute on the image.
</p>
<img id="image" src="mdn.svg" alt="MDN Logo" />
```

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [CSSImageValue](/en-US/docs/Web/API/CSSImageValue)
- [CSSKeywordValue](/en-US/docs/Web/API/CSSKeywordValue)
- [CSSNumericValue](/en-US/docs/Web/API/CSSNumericValue)
- [CSSTransformValue](/en-US/docs/Web/API/CSSTransformValue)
- [CSSUnparsedValue](/en-US/docs/Web/API/CSSUnparsedValue)
- [Using the CSS Typed OM](/en-US/docs/Web/API/CSS_Typed_OM_API/Guide)
- [CSS Typed Object Model API](/en-US/docs/Web/API/CSS_Typed_OM_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 19, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/CSSPositionValue/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/csspositionvalue/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSPositionValue&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcsspositionvalue%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSPositionValue%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcsspositionvalue%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb280ea1234452ff553caa466bf532a66ba51db01%0A*+Document+last+modified%3A+2023-02-19T06%3A34%3A57.000Z%0A%0A%3C%2Fdetails%3E)
