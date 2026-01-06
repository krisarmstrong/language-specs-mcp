# CSS Object Model (CSSOM)

The CSS Object Model is a set of APIs allowing the manipulation of CSS from JavaScript. It is much like the DOM, but for the CSS rather than the HTML. It allows users to read and modify CSS style dynamically.

The values of CSS are represented untyped, that is using [String](/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) objects.

## In this article

- [Reference](#reference)
- [Tutorials](#tutorials)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Reference](#reference)

- [AnimationEvent](/en-US/docs/Web/API/AnimationEvent)
- [CaretPosition](/en-US/docs/Web/API/CaretPosition)
- [CSS](/en-US/docs/Web/API/CSS)
- [CSSConditionRule](/en-US/docs/Web/API/CSSConditionRule)
- [CSSCounterStyleRule](/en-US/docs/Web/API/CSSCounterStyleRule)
- [CSSFontFaceRule](/en-US/docs/Web/API/CSSFontFaceRule)
- `CSSFontFeatureValuesMap`
- [CSSFontFeatureValuesRule](/en-US/docs/Web/API/CSSFontFeatureValuesRule)
- [CSSFunctionDeclarations](/en-US/docs/Web/API/CSSFunctionDeclarations)
- [CSSFunctionDescriptors](/en-US/docs/Web/API/CSSFunctionDescriptors)
- [CSSFunctionRule](/en-US/docs/Web/API/CSSFunctionRule)
- [CSSGroupingRule](/en-US/docs/Web/API/CSSGroupingRule)
- [CSSImportRule](/en-US/docs/Web/API/CSSImportRule)
- [CSSKeyframeRule](/en-US/docs/Web/API/CSSKeyframeRule)
- [CSSKeyframesRule](/en-US/docs/Web/API/CSSKeyframesRule)
- `CSSMarginRule`
- [CSSMediaRule](/en-US/docs/Web/API/CSSMediaRule)
- [CSSNamespaceRule](/en-US/docs/Web/API/CSSNamespaceRule)
- [CSSPageRule](/en-US/docs/Web/API/CSSPageRule)
- [CSSPositionTryRule](/en-US/docs/Web/API/CSSPositionTryRule)
- [CSSPositionTryDescriptors](/en-US/docs/Web/API/CSSPositionTryDescriptors)
- [CSSRule](/en-US/docs/Web/API/CSSRule)
- [CSSRuleList](/en-US/docs/Web/API/CSSRuleList)
- [CSSStartingStyleRule](/en-US/docs/Web/API/CSSStartingStyleRule)
- [CSSStyleDeclaration](/en-US/docs/Web/API/CSSStyleDeclaration)
- [CSSStyleSheet](/en-US/docs/Web/API/CSSStyleSheet)
- [CSSStyleRule](/en-US/docs/Web/API/CSSStyleRule)
- [CSSSupportsRule](/en-US/docs/Web/API/CSSSupportsRule)
- [CSSNestedDeclarations](/en-US/docs/Web/API/CSSNestedDeclarations)
- [FontFace](/en-US/docs/Web/API/FontFace)
- [FontFaceSet](/en-US/docs/Web/API/FontFaceSet)
- [FontFaceSetLoadEvent](/en-US/docs/Web/API/FontFaceSetLoadEvent)
- [MediaList](/en-US/docs/Web/API/MediaList)
- [MediaQueryList](/en-US/docs/Web/API/MediaQueryList)
- [MediaQueryListEvent](/en-US/docs/Web/API/MediaQueryListEvent)
- [Screen](/en-US/docs/Web/API/Screen)
- [StyleSheet](/en-US/docs/Web/API/StyleSheet)
- [StyleSheetList](/en-US/docs/Web/API/StyleSheetList)
- [TransitionEvent](/en-US/docs/Web/API/TransitionEvent)
- [VisualViewport](/en-US/docs/Web/API/VisualViewport)

Several other interfaces are also extended by the CSSOM-related specifications: [Document](/en-US/docs/Web/API/Document), [Window](/en-US/docs/Web/API/Window), [Element](/en-US/docs/Web/API/Element), [HTMLElement](/en-US/docs/Web/API/HTMLElement), [HTMLImageElement](/en-US/docs/Web/API/HTMLImageElement), [Range](/en-US/docs/Web/API/Range), [MouseEvent](/en-US/docs/Web/API/MouseEvent), and [SVGElement](/en-US/docs/Web/API/SVGElement).

### [CSS Typed Object Model](#css_typed_object_model)

- [CSSImageValue](/en-US/docs/Web/API/CSSImageValue)
- [CSSKeywordValue](/en-US/docs/Web/API/CSSKeywordValue)
- [CSSMathInvert](/en-US/docs/Web/API/CSSMathInvert)
- [CSSMathMax](/en-US/docs/Web/API/CSSMathMax)
- [CSSMathMin](/en-US/docs/Web/API/CSSMathMin)
- [CSSMathNegate](/en-US/docs/Web/API/CSSMathNegate)
- [CSSMathProduct](/en-US/docs/Web/API/CSSMathProduct)
- [CSSMathSum](/en-US/docs/Web/API/CSSMathSum)
- [CSSMathValue](/en-US/docs/Web/API/CSSMathValue)
- [CSSMatrixComponent](/en-US/docs/Web/API/CSSMatrixComponent)
- [CSSNumericArray](/en-US/docs/Web/API/CSSNumericArray)
- [CSSNumericValue](/en-US/docs/Web/API/CSSNumericValue)
- [CSSPerspective](/en-US/docs/Web/API/CSSPerspective)
- [CSSPositionValue](/en-US/docs/Web/API/CSSPositionValue)
- [CSSRotate](/en-US/docs/Web/API/CSSRotate)
- [CSSScale](/en-US/docs/Web/API/CSSScale)
- [CSSSkew](/en-US/docs/Web/API/CSSSkew)
- [CSSSkewX](/en-US/docs/Web/API/CSSSkewX)
- [CSSSkewY](/en-US/docs/Web/API/CSSSkewY)
- [CSSStyleValue](/en-US/docs/Web/API/CSSStyleValue)
- [CSSTransformComponent](/en-US/docs/Web/API/CSSTransformComponent)
- [CSSTransformValue](/en-US/docs/Web/API/CSSTransformValue)
- [CSSTranslate](/en-US/docs/Web/API/CSSTranslate)
- [CSSUnitValue](/en-US/docs/Web/API/CSSUnitValue)
- [CSSUnparsedValue](/en-US/docs/Web/API/CSSUnparsedValue)
- [CSSVariableReferenceValue](/en-US/docs/Web/API/CSSVariableReferenceValue)
- [StylePropertyMap](/en-US/docs/Web/API/StylePropertyMap)
- [StylePropertyMapReadOnly](/en-US/docs/Web/API/StylePropertyMapReadOnly)

### [Obsolete CSSOM interfaces 
Deprecated](#obsolete_cssom_interfaces_deprecated)

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

- [CSSPrimitiveValue](/en-US/docs/Web/API/CSSPrimitiveValue)Deprecated
- [CSSValue](/en-US/docs/Web/API/CSSValue)Deprecated
- [CSSValueList](/en-US/docs/Web/API/CSSValueList)Deprecated

## [Tutorials](#tutorials)

- [Determining the dimensions of elements](/en-US/docs/Web/API/CSS_Object_Model/Determining_the_dimensions_of_elements)
- [Managing screen orientation](/en-US/docs/Web/API/CSS_Object_Model/Managing_screen_orientation)

## [Specifications](#specifications)

Specification[CSS Object Model (CSSOM)](https://drafts.csswg.org/cssom/)[CSSOM View Module](https://drafts.csswg.org/cssom-view/)[CSS Typed OM Level 1](https://drafts.css-houdini.org/css-typed-om/)

## [Browser compatibility](#browser_compatibility)

All these features have been added little by little over the years to the different browsers: it was a quite complex process that can't be summarized in a simple table. Please refer to the specific interfaces for its availability.

## [See also](#see_also)

- [Document Object Model (DOM)](/en-US/docs/Web/API/Document_Object_Model)
- [Houdini APIs](/en-US/docs/Web/API/Houdini_APIs)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 15, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSS_Object_Model/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/css_object_model/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSS_Object_Model&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcss_object_model%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSS_Object_Model%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcss_object_model%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F792888cd76b95a986a38d6a48bece464731dda51%0A*+Document+last+modified%3A+2025-10-15T14%3A04%3A43.000Z%0A%0A%3C%2Fdetails%3E)
