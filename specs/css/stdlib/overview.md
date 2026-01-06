# CSS reference

Use this CSS reference to browse an [alphabetical index](#index) of all of the standard [CSS](/en-US/docs/Web/CSS)[properties](/en-US/docs/Web/CSS/Reference/Properties), [pseudo-classes](/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes), [pseudo-elements](/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements), [data types](/en-US/docs/Web/CSS/Reference/Values/Data_types), [functional notations](/en-US/docs/Web/CSS/Reference/Values/Functions) and [at-rules](/en-US/docs/Web/CSS/Reference/At-rules). You can also browse [key CSS concepts](#concepts) and a list of [selectors organized by type](#selectors). Also included is a brief [DOM-CSS / CSSOM reference](#dom-css_cssom).

## In this article

- [Basic rule syntax](#basic_rule_syntax)
- [Index](#index)
- [Selectors](#selectors)
- [Concepts](#concepts)
- [DOM-CSS / CSSOM](#dom-css_cssom)
- [See also](#see_also)
- [External Links](#external_links)

## [Basic rule syntax](#basic_rule_syntax)

### [Style rule syntax](#style_rule_syntax)

```
style-rule ::=
    selectors-list {
      properties-list
    }
```

Where:

```
selectors-list ::=
    selector[:pseudo-class] [::pseudo-element]
    [, selectors-list]

properties-list ::=
    [property : value] [; properties-list]
```

See the index of [selectors](#selectors), [pseudo-classes](#pseudo), and [pseudo-elements](#pseudo) below. The syntax for each specified value depends on the data type defined for each specified property.

#### Style rule examples

css

```
strong {
  color: red;
}

div.menu-bar li:hover > ul {
  display: block;
}
```

For a beginner-level introduction to the syntax of selectors, see our [guide on CSS Selectors](/en-US/docs/Learn_web_development/Core/Styling_basics/Basic_selectors). Be aware that any [syntax](/en-US/docs/Web/CSS/Guides/Syntax/Introduction) error in a rule definition invalidates the entire rule. Invalid rules are ignored by the browser. Note that CSS rule definitions are entirely (Unicode) [text-based](https://drafts.csswg.org/css-syntax/#intro), whereas DOM-CSS / CSSOM (the rule management system) is [object-based](https://drafts.csswg.org/cssom/#introduction).

### [At-rule syntax](#at-rule_syntax)

As the structure of at-rules varies widely, please see [At-rule](/en-US/docs/Web/CSS/Reference/At-rules) to find the syntax of the specific one you want.

## [Index](#index)

Note: This index does not include SVG-exclusive presentation attributes, which can be used as CSS properties on [SVG](/en-US/docs/Web/SVG) elements.

Note: The property names in this index do not include the JavaScript names which do differ from the CSS standard names.

### -

- [--*](/en-US/docs/Web/CSS/Reference/Properties/--*)
- [-webkit-line-clamp](/en-US/docs/Web/CSS/Reference/Properties/line-clamp)
- [-webkit-text-fill-color](/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-fill-color)
- [-webkit-text-stroke](/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke)
- [-webkit-text-stroke-color](/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke-color)
- [-webkit-text-stroke-width](/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke-width)

### A

- [abs()](/en-US/docs/Web/CSS/Reference/Values/abs)
- [accent-color](/en-US/docs/Web/CSS/Reference/Properties/accent-color)
- [acos()](/en-US/docs/Web/CSS/Reference/Values/acos)
- [:active](/en-US/docs/Web/CSS/Reference/Selectors/:active)
- [:active-view-transition](/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition)
- `:active-view-transition-type()`
- [additive-symbols (@counter-style)](/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/additive-symbols)
- [::after (:after)](/en-US/docs/Web/CSS/Reference/Selectors/::after)
- [align-content](/en-US/docs/Web/CSS/Reference/Properties/align-content)
- [align-items](/en-US/docs/Web/CSS/Reference/Properties/align-items)
- [align-self](/en-US/docs/Web/CSS/Reference/Properties/align-self)
- [alignment-baseline](/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline)
- [all](/en-US/docs/Web/CSS/Reference/Properties/all)
- [anchor()](/en-US/docs/Web/CSS/Reference/Values/anchor)
- [anchor-name](/en-US/docs/Web/CSS/Reference/Properties/anchor-name)
- `anchor-scope`
- [anchor-size()](/en-US/docs/Web/CSS/Reference/Values/anchor-size)
- [<angle>](/en-US/docs/Web/CSS/Reference/Values/angle)
- [<angle-percentage>](/en-US/docs/Web/CSS/Reference/Values/angle-percentage)
- [animation](/en-US/docs/Web/CSS/Reference/Properties/animation)
- [animation-composition](/en-US/docs/Web/CSS/Reference/Properties/animation-composition)
- [animation-delay](/en-US/docs/Web/CSS/Reference/Properties/animation-delay)
- [animation-direction](/en-US/docs/Web/CSS/Reference/Properties/animation-direction)
- [animation-duration](/en-US/docs/Web/CSS/Reference/Properties/animation-duration)
- [animation-fill-mode](/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
- [animation-iteration-count](/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count)
- [animation-name](/en-US/docs/Web/CSS/Reference/Properties/animation-name)
- [animation-play-state](/en-US/docs/Web/CSS/Reference/Properties/animation-play-state)
- [animation-range](/en-US/docs/Web/CSS/Reference/Properties/animation-range)
- [animation-range-end](/en-US/docs/Web/CSS/Reference/Properties/animation-range-end)
- [animation-range-start](/en-US/docs/Web/CSS/Reference/Properties/animation-range-start)
- [animation-timeline](/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
- [animation-timing-function](/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function)
- [@annotation](/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values#annotation)
- [:any-link](/en-US/docs/Web/CSS/Reference/Selectors/:any-link)
- [appearance](/en-US/docs/Web/CSS/Reference/Properties/appearance)
- [ascent-override (@font-face)](/en-US/docs/Web/CSS/Reference/At-rules/@font-face/ascent-override)
- [asin()](/en-US/docs/Web/CSS/Reference/Values/asin)
- [aspect-ratio](/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio)
- [atan()](/en-US/docs/Web/CSS/Reference/Values/atan)
- [atan2()](/en-US/docs/Web/CSS/Reference/Values/atan2)
- [attr()](/en-US/docs/Web/CSS/Reference/Values/attr)
- [:autofill](/en-US/docs/Web/CSS/Reference/Selectors/:autofill)

### B

- [::backdrop](/en-US/docs/Web/CSS/Reference/Selectors/::backdrop)
- [backdrop-filter](/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter)
- [backface-visibility](/en-US/docs/Web/CSS/Reference/Properties/backface-visibility)
- [background](/en-US/docs/Web/CSS/Reference/Properties/background)
- [background-attachment](/en-US/docs/Web/CSS/Reference/Properties/background-attachment)
- [background-blend-mode](/en-US/docs/Web/CSS/Reference/Properties/background-blend-mode)
- [background-clip](/en-US/docs/Web/CSS/Reference/Properties/background-clip)
- [background-color](/en-US/docs/Web/CSS/Reference/Properties/background-color)
- [background-image](/en-US/docs/Web/CSS/Reference/Properties/background-image)
- [background-origin](/en-US/docs/Web/CSS/Reference/Properties/background-origin)
- [background-position](/en-US/docs/Web/CSS/Reference/Properties/background-position)
- [background-position-x](/en-US/docs/Web/CSS/Reference/Properties/background-position-x)
- [background-position-y](/en-US/docs/Web/CSS/Reference/Properties/background-position-y)
- [background-repeat](/en-US/docs/Web/CSS/Reference/Properties/background-repeat)
- [background-size](/en-US/docs/Web/CSS/Reference/Properties/background-size)
- [base-palette (@font-palette-values)](/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/base-palette)
- `baseline-shift`
- [<basic-shape>](/en-US/docs/Web/CSS/Reference/Values/basic-shape)
- [::before (:before)](/en-US/docs/Web/CSS/Reference/Selectors/::before)
- [:blank](/en-US/docs/Web/CSS/Reference/Selectors/:blank)
- `bleed (@page)`
- [<blend-mode>](/en-US/docs/Web/CSS/Reference/Values/blend-mode)
- [block-size](/en-US/docs/Web/CSS/Reference/Properties/block-size)
- [blur()](/en-US/docs/Web/CSS/Reference/Values/filter-function/blur)
- [border](/en-US/docs/Web/CSS/Reference/Properties/border)
- [border-block](/en-US/docs/Web/CSS/Reference/Properties/border-block)
- [border-block-color](/en-US/docs/Web/CSS/Reference/Properties/border-block-color)
- [border-block-end](/en-US/docs/Web/CSS/Reference/Properties/border-block-end)
- [border-block-end-color](/en-US/docs/Web/CSS/Reference/Properties/border-block-end-color)
- [border-block-end-style](/en-US/docs/Web/CSS/Reference/Properties/border-block-end-style)
- [border-block-end-width](/en-US/docs/Web/CSS/Reference/Properties/border-block-end-width)
- [border-block-start](/en-US/docs/Web/CSS/Reference/Properties/border-block-start)
- [border-block-start-color](/en-US/docs/Web/CSS/Reference/Properties/border-block-start-color)
- [border-block-start-style](/en-US/docs/Web/CSS/Reference/Properties/border-block-start-style)
- [border-block-start-width](/en-US/docs/Web/CSS/Reference/Properties/border-block-start-width)
- [border-block-style](/en-US/docs/Web/CSS/Reference/Properties/border-block-style)
- [border-block-width](/en-US/docs/Web/CSS/Reference/Properties/border-block-width)
- [border-bottom](/en-US/docs/Web/CSS/Reference/Properties/border-bottom)
- [border-bottom-color](/en-US/docs/Web/CSS/Reference/Properties/border-bottom-color)
- [border-bottom-left-radius](/en-US/docs/Web/CSS/Reference/Properties/border-bottom-left-radius)
- [border-bottom-right-radius](/en-US/docs/Web/CSS/Reference/Properties/border-bottom-right-radius)
- [border-bottom-style](/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style)
- [border-bottom-width](/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width)
- [border-collapse](/en-US/docs/Web/CSS/Reference/Properties/border-collapse)
- [border-color](/en-US/docs/Web/CSS/Reference/Properties/border-color)
- [border-end-end-radius](/en-US/docs/Web/CSS/Reference/Properties/border-end-end-radius)
- [border-end-start-radius](/en-US/docs/Web/CSS/Reference/Properties/border-end-start-radius)
- [border-image](/en-US/docs/Web/CSS/Reference/Properties/border-image)
- [border-image-outset](/en-US/docs/Web/CSS/Reference/Properties/border-image-outset)
- [border-image-repeat](/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat)
- [border-image-slice](/en-US/docs/Web/CSS/Reference/Properties/border-image-slice)
- [border-image-source](/en-US/docs/Web/CSS/Reference/Properties/border-image-source)
- [border-image-width](/en-US/docs/Web/CSS/Reference/Properties/border-image-width)
- [border-inline](/en-US/docs/Web/CSS/Reference/Properties/border-inline)
- [border-inline-color](/en-US/docs/Web/CSS/Reference/Properties/border-inline-color)
- [border-inline-end](/en-US/docs/Web/CSS/Reference/Properties/border-inline-end)
- [border-inline-end-color](/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-color)
- [border-inline-end-style](/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-style)
- [border-inline-end-width](/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-width)
- [border-inline-start](/en-US/docs/Web/CSS/Reference/Properties/border-inline-start)
- [border-inline-start-color](/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-color)
- [border-inline-start-style](/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-style)
- [border-inline-start-width](/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-width)
- [border-inline-style](/en-US/docs/Web/CSS/Reference/Properties/border-inline-style)
- [border-inline-width](/en-US/docs/Web/CSS/Reference/Properties/border-inline-width)
- [border-left](/en-US/docs/Web/CSS/Reference/Properties/border-left)
- [border-left-color](/en-US/docs/Web/CSS/Reference/Properties/border-left-color)
- [border-left-style](/en-US/docs/Web/CSS/Reference/Properties/border-left-style)
- [border-left-width](/en-US/docs/Web/CSS/Reference/Properties/border-left-width)
- [border-radius](/en-US/docs/Web/CSS/Reference/Properties/border-radius)
- [border-right](/en-US/docs/Web/CSS/Reference/Properties/border-right)
- [border-right-color](/en-US/docs/Web/CSS/Reference/Properties/border-right-color)
- [border-right-style](/en-US/docs/Web/CSS/Reference/Properties/border-right-style)
- [border-right-width](/en-US/docs/Web/CSS/Reference/Properties/border-right-width)
- [border-spacing](/en-US/docs/Web/CSS/Reference/Properties/border-spacing)
- [border-start-end-radius](/en-US/docs/Web/CSS/Reference/Properties/border-start-end-radius)
- [border-start-start-radius](/en-US/docs/Web/CSS/Reference/Properties/border-start-start-radius)
- [border-style](/en-US/docs/Web/CSS/Reference/Properties/border-style)
- [border-top](/en-US/docs/Web/CSS/Reference/Properties/border-top)
- [border-top-color](/en-US/docs/Web/CSS/Reference/Properties/border-top-color)
- [border-top-left-radius](/en-US/docs/Web/CSS/Reference/Properties/border-top-left-radius)
- [border-top-right-radius](/en-US/docs/Web/CSS/Reference/Properties/border-top-right-radius)
- [border-top-style](/en-US/docs/Web/CSS/Reference/Properties/border-top-style)
- [border-top-width](/en-US/docs/Web/CSS/Reference/Properties/border-top-width)
- [border-width](/en-US/docs/Web/CSS/Reference/Properties/border-width)
- [bottom](/en-US/docs/Web/CSS/Reference/Properties/bottom)
- [@bottom-left-corner](/en-US/docs/Web/CSS/Reference/At-rules/@page#page-margin-box-type)
- [box-decoration-break](/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break)
- [box-shadow](/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
- [box-sizing](/en-US/docs/Web/CSS/Reference/Properties/box-sizing)
- [break-after](/en-US/docs/Web/CSS/Reference/Properties/break-after)
- [break-before](/en-US/docs/Web/CSS/Reference/Properties/break-before)
- [break-inside](/en-US/docs/Web/CSS/Reference/Properties/break-inside)
- [brightness()](/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness)
- [:buffering](/en-US/docs/Web/CSS/Reference/Selectors/:buffering)

### C

- [calc()](/en-US/docs/Web/CSS/Reference/Values/calc)
- [calc-size()](/en-US/docs/Web/CSS/Reference/Values/calc-size)
- `cap`
- [caption-side](/en-US/docs/Web/CSS/Reference/Properties/caption-side)
- [caret](/en-US/docs/Web/CSS/Reference/Properties/caret)
- [caret-color](/en-US/docs/Web/CSS/Reference/Properties/caret-color)
- [caret-shape](/en-US/docs/Web/CSS/Reference/Properties/caret-shape)
- `ch`
- [@character-variant](/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values#character-variant)
- [@charset](/en-US/docs/Web/CSS/Reference/At-rules/@charset)
- [:checked](/en-US/docs/Web/CSS/Reference/Selectors/:checked)
- [::checkmark](/en-US/docs/Web/CSS/Reference/Selectors/::checkmark)
- [circle()](/en-US/docs/Web/CSS/Reference/Values/basic-shape#circle)
- [clamp()](/en-US/docs/Web/CSS/Reference/Values/clamp)
- [clear](/en-US/docs/Web/CSS/Reference/Properties/clear)
- [clip-path](/en-US/docs/Web/CSS/Reference/Properties/clip-path)
- [clip-rule](/en-US/docs/Web/CSS/Reference/Properties/clip-rule)
- `cm`
- [<color>](/en-US/docs/Web/CSS/Reference/Values/color_value)
- [color](/en-US/docs/Web/CSS/Reference/Properties/color)
- [color-interpolation-filters](/en-US/docs/Web/CSS/Reference/Properties/color-interpolation-filters)
- `color-mix()`
- [color-scheme](/en-US/docs/Web/CSS/Reference/Properties/color-scheme)
- [column-count](/en-US/docs/Web/CSS/Reference/Properties/column-count)
- [column-fill](/en-US/docs/Web/CSS/Reference/Properties/column-fill)
- [column-gap](/en-US/docs/Web/CSS/Reference/Properties/column-gap)
- [column-rule](/en-US/docs/Web/CSS/Reference/Properties/column-rule)
- [column-rule-color](/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
- [column-rule-style](/en-US/docs/Web/CSS/Reference/Properties/column-rule-style)
- [column-rule-width](/en-US/docs/Web/CSS/Reference/Properties/column-rule-width)
- [column-span](/en-US/docs/Web/CSS/Reference/Properties/column-span)
- [column-width](/en-US/docs/Web/CSS/Reference/Properties/column-width)
- [columns](/en-US/docs/Web/CSS/Reference/Properties/columns)
- [conic-gradient()](/en-US/docs/Web/CSS/Reference/Values/gradient/conic-gradient)
- [contain](/en-US/docs/Web/CSS/Reference/Properties/contain)
- [contain-intrinsic-block-size](/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-block-size)
- [contain-intrinsic-height](/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height)
- [contain-intrinsic-inline-size](/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-inline-size)
- [contain-intrinsic-size](/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size)
- [contain-intrinsic-width](/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-width)
- [@container](/en-US/docs/Web/CSS/Reference/At-rules/@container)
- [container](/en-US/docs/Web/CSS/Reference/Properties/container)
- [container-name](/en-US/docs/Web/CSS/Reference/Properties/container-name)
- [container-type](/en-US/docs/Web/CSS/Reference/Properties/container-type)
- [content](/en-US/docs/Web/CSS/Reference/Properties/content)
- [content-visibility](/en-US/docs/Web/CSS/Reference/Properties/content-visibility)
- [contrast()](/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast)
- [cos()](/en-US/docs/Web/CSS/Reference/Values/cos)
- [<counter>](/en-US/docs/Web/CSS/Reference/Values/counter)
- [counter-increment](/en-US/docs/Web/CSS/Reference/Properties/counter-increment)
- [counter-reset](/en-US/docs/Web/CSS/Reference/Properties/counter-reset)
- [counter-set](/en-US/docs/Web/CSS/Reference/Properties/counter-set)
- [@counter-style](/en-US/docs/Web/CSS/Reference/At-rules/@counter-style)
- [counters()](/en-US/docs/Web/CSS/Reference/Values/counters)
- [cross-fade()](/en-US/docs/Web/CSS/Reference/Values/cross-fade)
- [cubic-bezier()](/en-US/docs/Web/CSS/Reference/Values/easing-function#cubic_bézier_easing_function)
- [::cue](/en-US/docs/Web/CSS/Reference/Selectors/::cue)
- `::cue()`
- [::cue-region](/en-US/docs/Web/API/WebVTT_API)
- `::cue-region()`
- [:current](/en-US/docs/Web/CSS/Reference/Selectors/:current)
- [cursor](/en-US/docs/Web/CSS/Reference/Properties/cursor)
- [<custom-ident>](/en-US/docs/Web/CSS/Reference/Values/custom-ident)
- [cx](/en-US/docs/Web/CSS/Reference/Properties/cx)
- [cy](/en-US/docs/Web/CSS/Reference/Properties/cy)

### D

- [d](/en-US/docs/Web/CSS/Reference/Properties/d)
- [<dashed-ident>](/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
- [:default](/en-US/docs/Web/CSS/Reference/Selectors/:default)
- [:defined](/en-US/docs/Web/CSS/Reference/Selectors/:defined)
- `deg`
- [descent-override (@font-face)](/en-US/docs/Web/CSS/Reference/At-rules/@font-face/descent-override)
- [::details-content](/en-US/docs/Web/CSS/Reference/Selectors/::details-content)
- [<dimension>](/en-US/docs/Web/CSS/Reference/Values/dimension)
- [:dir()](/en-US/docs/Web/CSS/Reference/Selectors/:dir)
- [direction](/en-US/docs/Web/CSS/Reference/Properties/direction)
- [:disabled](/en-US/docs/Web/CSS/Reference/Selectors/:disabled)
- [display](/en-US/docs/Web/CSS/Reference/Properties/display)
- [<display-box>](/en-US/docs/Web/CSS/Reference/Values/display-box)
- [<display-inside>](/en-US/docs/Web/CSS/Reference/Values/display-inside)
- [<display-internal>](/en-US/docs/Web/CSS/Reference/Values/display-internal)
- [<display-legacy>](/en-US/docs/Web/CSS/Reference/Values/display-legacy)
- [<display-listitem>](/en-US/docs/Web/CSS/Reference/Values/display-listitem)
- [<display-outside>](/en-US/docs/Web/CSS/Reference/Values/display-outside)
- [dominant-baseline](/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline)
- `dpcm`
- `dpi`
- `dppx`
- [drop-shadow()](/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow)

### E

- [<easing-function>](/en-US/docs/Web/CSS/Reference/Values/easing-function)
- [element()](/en-US/docs/Web/CSS/Reference/Values/element)
- [ellipse()](/en-US/docs/Web/CSS/Reference/Values/basic-shape#ellipse)
- `em`
- [:empty](/en-US/docs/Web/CSS/Reference/Selectors/:empty)
- [empty-cells](/en-US/docs/Web/CSS/Reference/Properties/empty-cells)
- [:enabled](/en-US/docs/Web/CSS/Reference/Selectors/:enabled)
- [env()](/en-US/docs/Web/CSS/Reference/Values/env)
- `ex`
- [exp()](/en-US/docs/Web/CSS/Reference/Values/exp)

### F

- [fallback (@counter-style)](/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/fallback)
- [field-sizing](/en-US/docs/Web/CSS/Reference/Properties/field-sizing)
- [::file-selector-button](/en-US/docs/Web/CSS/Reference/Selectors/::file-selector-button)
- [fill](/en-US/docs/Web/CSS/Reference/Properties/fill)
- [fill-opacity](/en-US/docs/Web/CSS/Reference/Properties/fill-opacity)
- [fill-rule](/en-US/docs/Web/CSS/Reference/Properties/fill-rule)
- [filter](/en-US/docs/Web/CSS/Reference/Properties/filter)
- [<filter-function>](/en-US/docs/Web/CSS/Reference/Values/filter-function)
- [:first](/en-US/docs/Web/CSS/Reference/Selectors/:first)
- [:first-child](/en-US/docs/Web/CSS/Reference/Selectors/:first-child)
- [::first-letter (:first-letter)](/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)
- [::first-line (:first-line)](/en-US/docs/Web/CSS/Reference/Selectors/::first-line)
- [:first-of-type](/en-US/docs/Web/CSS/Reference/Selectors/:first-of-type)
- [fit-content()](/en-US/docs/Web/CSS/Reference/Values/fit-content)
- [<flex>](/en-US/docs/Web/CSS/Reference/Values/flex_value)
- [flex](/en-US/docs/Web/CSS/Reference/Properties/flex)
- [flex-basis](/en-US/docs/Web/CSS/Reference/Properties/flex-basis)
- [flex-direction](/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
- [flex-flow](/en-US/docs/Web/CSS/Reference/Properties/flex-flow)
- [flex-grow](/en-US/docs/Web/CSS/Reference/Properties/flex-grow)
- [flex-shrink](/en-US/docs/Web/CSS/Reference/Properties/flex-shrink)
- [flex-wrap](/en-US/docs/Web/CSS/Reference/Properties/flex-wrap)
- [float](/en-US/docs/Web/CSS/Reference/Properties/float)
- [flood-color](/en-US/docs/Web/CSS/Reference/Properties/flood-color)
- [flood-opacity](/en-US/docs/Web/CSS/Reference/Properties/flood-opacity)
- [:focus](/en-US/docs/Web/CSS/Reference/Selectors/:focus)
- [:focus-visible](/en-US/docs/Web/CSS/Reference/Selectors/:focus-visible)
- [:focus-within](/en-US/docs/Web/CSS/Reference/Selectors/:focus-within)
- [font](/en-US/docs/Web/CSS/Reference/Properties/font)
- [font-display (@font-face)](/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display)
- [@font-face](/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
- [font-family](/en-US/docs/Web/CSS/Reference/Properties/font-family)
- [font-family (@font-face)](/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-family)
- [font-family (@font-palette-values)](/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/font-family)
- [font-feature-settings](/en-US/docs/Web/CSS/Reference/Properties/font-feature-settings)
- [font-feature-settings (@font-face)](/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-feature-settings)
- [@font-feature-values](/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values)
- [font-kerning](/en-US/docs/Web/CSS/Reference/Properties/font-kerning)
- [font-language-override](/en-US/docs/Web/CSS/Reference/Properties/font-language-override)
- [font-optical-sizing](/en-US/docs/Web/CSS/Reference/Properties/font-optical-sizing)
- [font-palette](/en-US/docs/Web/CSS/Reference/Properties/font-palette)
- [@font-palette-values](/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values)
- [font-size](/en-US/docs/Web/CSS/Reference/Properties/font-size)
- [font-size-adjust](/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust)
- [font-style](/en-US/docs/Web/CSS/Reference/Properties/font-style)
- [font-style (@font-face)](/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style)
- [font-synthesis](/en-US/docs/Web/CSS/Reference/Properties/font-synthesis)
- [font-synthesis-position](/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-position)
- [font-synthesis-small-caps](/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-small-caps)
- [font-synthesis-style](/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-style)
- [font-synthesis-weight](/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-weight)
- [font-variant](/en-US/docs/Web/CSS/Reference/Properties/font-variant)
- [font-variant-alternates](/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates)
- [font-variant-caps](/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps)
- [font-variant-east-asian](/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian)
- [font-variant-emoji](/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji)
- [font-variant-ligatures](/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures)
- [font-variant-numeric](/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric)
- [font-variant-position](/en-US/docs/Web/CSS/Reference/Properties/font-variant-position)
- [font-variation-settings](/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings)
- [font-variation-settings (@font-face)](/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-variation-settings)
- [font-weight](/en-US/docs/Web/CSS/Reference/Properties/font-weight)
- [font-weight (@font-face)](/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight)
- `font-width`
- [forced-color-adjust](/en-US/docs/Web/CSS/Reference/Properties/forced-color-adjust)
- [format()](/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#format)
- `fr`
- [<frequency>](/en-US/docs/Web/CSS/Reference/Values/frequency)
- [<frequency-percentage>](/en-US/docs/Web/CSS/Reference/Values/frequency-percentage)
- [:fullscreen](/en-US/docs/Web/CSS/Reference/Selectors/:fullscreen)
- [:future](/en-US/docs/Web/CSS/Reference/Selectors/:future)

### G

- [gap](/en-US/docs/Web/CSS/Reference/Properties/gap)
- `grad`
- [<gradient>](/en-US/docs/Web/CSS/Reference/Values/gradient)
- [::grammar-error](/en-US/docs/Web/CSS/Reference/Selectors/::grammar-error)
- [grayscale()](/en-US/docs/Web/CSS/Reference/Values/filter-function/grayscale)
- [grid](/en-US/docs/Web/CSS/Reference/Properties/grid)
- [grid-area](/en-US/docs/Web/CSS/Reference/Properties/grid-area)
- [grid-auto-columns](/en-US/docs/Web/CSS/Reference/Properties/grid-auto-columns)
- [grid-auto-flow](/en-US/docs/Web/CSS/Reference/Properties/grid-auto-flow)
- [grid-auto-rows](/en-US/docs/Web/CSS/Reference/Properties/grid-auto-rows)
- [grid-column](/en-US/docs/Web/CSS/Reference/Properties/grid-column)
- [grid-column-end](/en-US/docs/Web/CSS/Reference/Properties/grid-column-end)
- [grid-column-start](/en-US/docs/Web/CSS/Reference/Properties/grid-column-start)
- [grid-row](/en-US/docs/Web/CSS/Reference/Properties/grid-row)
- [grid-row-end](/en-US/docs/Web/CSS/Reference/Properties/grid-row-end)
- [grid-row-start](/en-US/docs/Web/CSS/Reference/Properties/grid-row-start)
- [grid-template](/en-US/docs/Web/CSS/Reference/Properties/grid-template)
- [grid-template-areas](/en-US/docs/Web/CSS/Reference/Properties/grid-template-areas)
- [grid-template-columns](/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
- [grid-template-rows](/en-US/docs/Web/CSS/Reference/Properties/grid-template-rows)

### H

- `Hz`
- [hanging-punctuation](/en-US/docs/Web/CSS/Reference/Properties/hanging-punctuation)
- `:has()`
- [:has-slotted](/en-US/docs/Web/CSS/Reference/Selectors/:has-slotted)
- [height](/en-US/docs/Web/CSS/Reference/Properties/height)
- `::highlight()`
- [@historical-forms](/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values#historical-forms)
- [:host](/en-US/docs/Web/CSS/Reference/Selectors/:host)
- [:host()](/en-US/docs/Web/CSS/Reference/Selectors/:host_function)
- `:host-context()`
- [:hover](/en-US/docs/Web/CSS/Reference/Selectors/:hover)
- [hsl()](/en-US/docs/Web/CSS/Reference/Values/color_value/hsl)
- [hue-rotate()](/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate)
- [hwb()](/en-US/docs/Web/CSS/Reference/Values/color_value/hwb)
- [hyphenate-character](/en-US/docs/Web/CSS/Reference/Properties/hyphenate-character)
- [hyphenate-limit-chars](/en-US/docs/Web/CSS/Reference/Properties/hyphenate-limit-chars)
- [hyphens](/en-US/docs/Web/CSS/Reference/Properties/hyphens)
- [hypot()](/en-US/docs/Web/CSS/Reference/Values/hypot)

### I

- `ic`
- [<ident>](/en-US/docs/Web/CSS/Reference/Values/ident)
- [<image>](/en-US/docs/Web/CSS/Reference/Values/image)
- [image()](/en-US/docs/Web/CSS/Reference/Values/image#the_image_functional_notation)
- [image-orientation](/en-US/docs/Web/CSS/Reference/Properties/image-orientation)
- [image-rendering](/en-US/docs/Web/CSS/Reference/Properties/image-rendering)
- [image-resolution](/en-US/docs/Web/CSS/Reference/Properties/image-resolution)
- [image-set()](/en-US/docs/Web/CSS/Reference/Values/image/image-set)
- [@import](/en-US/docs/Web/CSS/Reference/At-rules/@import)
- `in`
- [:in-range](/en-US/docs/Web/CSS/Reference/Selectors/:in-range)
- [:indeterminate](/en-US/docs/Web/CSS/Reference/Selectors/:indeterminate)
- [inherit](/en-US/docs/Web/CSS/Reference/Values/inherit)
- [inherits (@property)](/en-US/docs/Web/CSS/Reference/At-rules/@property/inherits)
- [initial](/en-US/docs/Web/CSS/Reference/Values/initial)
- [initial-letter](/en-US/docs/Web/CSS/Reference/Properties/initial-letter)
- `initial-letter-align`
- [initial-value (@property)](/en-US/docs/Web/CSS/Reference/At-rules/@property/initial-value)
- [inline-size](/en-US/docs/Web/CSS/Reference/Properties/inline-size)
- [inset](/en-US/docs/Web/CSS/Reference/Properties/inset)
- [inset()](/en-US/docs/Web/CSS/Reference/Values/basic-shape#inset)
- [inset-block](/en-US/docs/Web/CSS/Reference/Properties/inset-block)
- [inset-block-end](/en-US/docs/Web/CSS/Reference/Properties/inset-block-end)
- [inset-block-start](/en-US/docs/Web/CSS/Reference/Properties/inset-block-start)
- [inset-inline](/en-US/docs/Web/CSS/Reference/Properties/inset-inline)
- [inset-inline-end](/en-US/docs/Web/CSS/Reference/Properties/inset-inline-end)
- [inset-inline-start](/en-US/docs/Web/CSS/Reference/Properties/inset-inline-start)
- [<integer>](/en-US/docs/Web/CSS/Reference/Values/integer)
- [interpolate-size](/en-US/docs/Web/CSS/Reference/Properties/interpolate-size)
- [:invalid](/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
- [invert()](/en-US/docs/Web/CSS/Reference/Values/filter-function/invert)
- `:is()`
- [isolation](/en-US/docs/Web/CSS/Reference/Properties/isolation)

### J

- [justify-content](/en-US/docs/Web/CSS/Reference/Properties/justify-content)
- [justify-items](/en-US/docs/Web/CSS/Reference/Properties/justify-items)
- [justify-self](/en-US/docs/Web/CSS/Reference/Properties/justify-self)

### K

- `kHz`
- [@keyframes](/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)

### L

- [lab()](/en-US/docs/Web/CSS/Reference/Values/color_value/lab)
- [:lang()](/en-US/docs/Web/CSS/Reference/Selectors/:lang)
- [:last-child](/en-US/docs/Web/CSS/Reference/Selectors/:last-child)
- [:last-of-type](/en-US/docs/Web/CSS/Reference/Selectors/:last-of-type)
- [@layer](/en-US/docs/Web/CSS/Reference/At-rules/@layer)
- `layer()`
- `layer() (@import)`
- [lch()](/en-US/docs/Web/CSS/Reference/Values/color_value/lch)
- `leader()`
- [:left](/en-US/docs/Web/CSS/Reference/Selectors/:left)
- [left](/en-US/docs/Web/CSS/Reference/Properties/left)
- [@left-top](/en-US/docs/Web/CSS/Reference/At-rules/@page#page-margin-box-type)
- [<length>](/en-US/docs/Web/CSS/Reference/Values/length)
- [<length-percentage>](/en-US/docs/Web/CSS/Reference/Values/length-percentage)
- [letter-spacing](/en-US/docs/Web/CSS/Reference/Properties/letter-spacing)
- [light-dark()](/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark)
- [lighting-color](/en-US/docs/Web/CSS/Reference/Properties/lighting-color)
- [line-break](/en-US/docs/Web/CSS/Reference/Properties/line-break)
- [line-clamp](/en-US/docs/Web/CSS/Reference/Properties/line-clamp)
- [line-gap-override (@font-face)](/en-US/docs/Web/CSS/Reference/At-rules/@font-face/line-gap-override)
- [line-height](/en-US/docs/Web/CSS/Reference/Properties/line-height)
- [line-height-step](/en-US/docs/Web/CSS/Reference/Properties/line-height-step)
- [<line-style>](/en-US/docs/Web/CSS/Reference/Values/line-style)
- [linear()](/en-US/docs/Web/CSS/Reference/Values/easing-function#linear_easing_function)
- [linear-gradient()](/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient)
- [:link](/en-US/docs/Web/CSS/Reference/Selectors/:link)
- [list-style](/en-US/docs/Web/CSS/Reference/Properties/list-style)
- [list-style-image](/en-US/docs/Web/CSS/Reference/Properties/list-style-image)
- [list-style-position](/en-US/docs/Web/CSS/Reference/Properties/list-style-position)
- [list-style-type](/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
- [local()](/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#local)
- [:local-link](/en-US/docs/Web/CSS/Reference/Selectors/:local-link)
- [log()](/en-US/docs/Web/CSS/Reference/Values/log)

### M

- [margin](/en-US/docs/Web/CSS/Reference/Properties/margin)
- [margin-block](/en-US/docs/Web/CSS/Reference/Properties/margin-block)
- [margin-block-end](/en-US/docs/Web/CSS/Reference/Properties/margin-block-end)
- [margin-block-start](/en-US/docs/Web/CSS/Reference/Properties/margin-block-start)
- [margin-bottom](/en-US/docs/Web/CSS/Reference/Properties/margin-bottom)
- [margin-inline](/en-US/docs/Web/CSS/Reference/Properties/margin-inline)
- [margin-inline-end](/en-US/docs/Web/CSS/Reference/Properties/margin-inline-end)
- [margin-inline-start](/en-US/docs/Web/CSS/Reference/Properties/margin-inline-start)
- [margin-left](/en-US/docs/Web/CSS/Reference/Properties/margin-left)
- [margin-right](/en-US/docs/Web/CSS/Reference/Properties/margin-right)
- [margin-top](/en-US/docs/Web/CSS/Reference/Properties/margin-top)
- [margin-trim](/en-US/docs/Web/CSS/Reference/Properties/margin-trim)
- [::marker](/en-US/docs/Web/CSS/Reference/Selectors/::marker)
- [marker](/en-US/docs/Web/CSS/Reference/Properties/marker)
- [marker-end](/en-US/docs/Web/CSS/Reference/Properties/marker-end)
- [marker-mid](/en-US/docs/Web/CSS/Reference/Properties/marker-mid)
- [marker-start](/en-US/docs/Web/CSS/Reference/Properties/marker-start)
- `marks (@page)`
- [mask](/en-US/docs/Web/CSS/Reference/Properties/mask)
- [mask-border](/en-US/docs/Web/CSS/Reference/Properties/mask-border)
- [mask-border-mode](/en-US/docs/Web/CSS/Reference/Properties/mask-border-mode)
- [mask-border-outset](/en-US/docs/Web/CSS/Reference/Properties/mask-border-outset)
- [mask-border-repeat](/en-US/docs/Web/CSS/Reference/Properties/mask-border-repeat)
- [mask-border-slice](/en-US/docs/Web/CSS/Reference/Properties/mask-border-slice)
- [mask-border-source](/en-US/docs/Web/CSS/Reference/Properties/mask-border-source)
- [mask-border-width](/en-US/docs/Web/CSS/Reference/Properties/mask-border-width)
- [mask-clip](/en-US/docs/Web/CSS/Reference/Properties/mask-clip)
- [mask-composite](/en-US/docs/Web/CSS/Reference/Properties/mask-composite)
- [mask-image](/en-US/docs/Web/CSS/Reference/Properties/mask-image)
- [mask-mode](/en-US/docs/Web/CSS/Reference/Properties/mask-mode)
- [mask-origin](/en-US/docs/Web/CSS/Reference/Properties/mask-origin)
- [mask-position](/en-US/docs/Web/CSS/Reference/Properties/mask-position)
- [mask-repeat](/en-US/docs/Web/CSS/Reference/Properties/mask-repeat)
- [mask-size](/en-US/docs/Web/CSS/Reference/Properties/mask-size)
- [mask-type](/en-US/docs/Web/CSS/Reference/Properties/mask-type)
- [math-depth](/en-US/docs/Web/CSS/Reference/Properties/math-depth)
- [math-shift](/en-US/docs/Web/CSS/Reference/Properties/math-shift)
- [math-style](/en-US/docs/Web/CSS/Reference/Properties/math-style)
- [matrix()](/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix)
- [matrix3d()](/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix3d)
- [max()](/en-US/docs/Web/CSS/Reference/Values/max)
- [max-block-size](/en-US/docs/Web/CSS/Reference/Properties/max-block-size)
- [max-height](/en-US/docs/Web/CSS/Reference/Properties/max-height)
- [max-inline-size](/en-US/docs/Web/CSS/Reference/Properties/max-inline-size)
- `max-lines`
- [max-width](/en-US/docs/Web/CSS/Reference/Properties/max-width)
- [@media](/en-US/docs/Web/CSS/Reference/At-rules/@media)
- [min()](/en-US/docs/Web/CSS/Reference/Values/min)
- [min-block-size](/en-US/docs/Web/CSS/Reference/Properties/min-block-size)
- [min-height](/en-US/docs/Web/CSS/Reference/Properties/min-height)
- [min-inline-size](/en-US/docs/Web/CSS/Reference/Properties/min-inline-size)
- [min-width](/en-US/docs/Web/CSS/Reference/Properties/min-width)
- [minmax()](/en-US/docs/Web/CSS/Reference/Values/minmax)
- [mix-blend-mode](/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode)
- `mm`
- [mod()](/en-US/docs/Web/CSS/Reference/Values/mod)
- [:modal](/en-US/docs/Web/CSS/Reference/Selectors/:modal)
- `ms`
- [:muted](/en-US/docs/Web/CSS/Reference/Selectors/:muted)

### N

- [@namespace](/en-US/docs/Web/CSS/Reference/At-rules/@namespace)
- `navigation (@view-transition)`
- [negative (@counter-style)](/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/negative)
- [:not()](/en-US/docs/Web/CSS/Reference/Selectors/:not)
- [:nth-child()](/en-US/docs/Web/CSS/Reference/Selectors/:nth-child)
- [:nth-last-child()](/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child)
- [:nth-last-of-type()](/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-of-type)
- [:nth-of-type()](/en-US/docs/Web/CSS/Reference/Selectors/:nth-of-type)
- [<number>](/en-US/docs/Web/CSS/Reference/Values/number)

### O

- [object-fit](/en-US/docs/Web/CSS/Reference/Properties/object-fit)
- [object-position](/en-US/docs/Web/CSS/Reference/Properties/object-position)
- [object-view-box](/en-US/docs/Web/CSS/Reference/Properties/object-view-box)
- [offset](/en-US/docs/Web/CSS/Reference/Properties/offset)
- [offset-anchor](/en-US/docs/Web/CSS/Reference/Properties/offset-anchor)
- [offset-distance](/en-US/docs/Web/CSS/Reference/Properties/offset-distance)
- [offset-path](/en-US/docs/Web/CSS/Reference/Properties/offset-path)
- [offset-position](/en-US/docs/Web/CSS/Reference/Properties/offset-position)
- [offset-rotate](/en-US/docs/Web/CSS/Reference/Properties/offset-rotate)
- [oklab()](/en-US/docs/Web/CSS/Reference/Values/color_value/oklab)
- [oklch()](/en-US/docs/Web/CSS/Reference/Values/color_value/oklch)
- [:only-child](/en-US/docs/Web/CSS/Reference/Selectors/:only-child)
- [:only-of-type](/en-US/docs/Web/CSS/Reference/Selectors/:only-of-type)
- [opacity](/en-US/docs/Web/CSS/Reference/Properties/opacity)
- [opacity()](/en-US/docs/Web/CSS/Reference/Values/filter-function/opacity)
- [:open](/en-US/docs/Web/CSS/Reference/Selectors/:open)
- [:optional](/en-US/docs/Web/CSS/Reference/Selectors/:optional)
- [order](/en-US/docs/Web/CSS/Reference/Properties/order)
- [@ornaments](/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values#ornaments)
- [orphans](/en-US/docs/Web/CSS/Reference/Properties/orphans)
- [:out-of-range](/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range)
- [outline](/en-US/docs/Web/CSS/Reference/Properties/outline)
- [outline-color](/en-US/docs/Web/CSS/Reference/Properties/outline-color)
- [outline-offset](/en-US/docs/Web/CSS/Reference/Properties/outline-offset)
- [outline-style](/en-US/docs/Web/CSS/Reference/Properties/outline-style)
- [outline-width](/en-US/docs/Web/CSS/Reference/Properties/outline-width)
- [overflow](/en-US/docs/Web/CSS/Reference/Properties/overflow)
- [overflow-anchor](/en-US/docs/Web/CSS/Reference/Properties/overflow-anchor)
- [overflow-block](/en-US/docs/Web/CSS/Reference/Properties/overflow-block)
- [overflow-clip-margin](/en-US/docs/Web/CSS/Reference/Properties/overflow-clip-margin)
- [overflow-inline](/en-US/docs/Web/CSS/Reference/Properties/overflow-inline)
- [overflow-wrap](/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap)
- [overflow-x](/en-US/docs/Web/CSS/Reference/Properties/overflow-x)
- [overflow-y](/en-US/docs/Web/CSS/Reference/Properties/overflow-y)
- [overlay](/en-US/docs/Web/CSS/Reference/Properties/overlay)
- [override-colors (@font-palette-values)](/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/override-colors)
- [overscroll-behavior](/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior)
- [overscroll-behavior-block](/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-block)
- [overscroll-behavior-inline](/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-inline)
- [overscroll-behavior-x](/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-x)
- [overscroll-behavior-y](/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-y)

### P

- [Pseudo-classes](/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
- [Pseudo-elements](/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
- [pad (@counter-style)](/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/pad)
- [padding](/en-US/docs/Web/CSS/Reference/Properties/padding)
- [padding-block](/en-US/docs/Web/CSS/Reference/Properties/padding-block)
- [padding-block-end](/en-US/docs/Web/CSS/Reference/Properties/padding-block-end)
- [padding-block-start](/en-US/docs/Web/CSS/Reference/Properties/padding-block-start)
- [padding-bottom](/en-US/docs/Web/CSS/Reference/Properties/padding-bottom)
- [padding-inline](/en-US/docs/Web/CSS/Reference/Properties/padding-inline)
- [padding-inline-end](/en-US/docs/Web/CSS/Reference/Properties/padding-inline-end)
- [padding-inline-start](/en-US/docs/Web/CSS/Reference/Properties/padding-inline-start)
- [padding-left](/en-US/docs/Web/CSS/Reference/Properties/padding-left)
- [padding-right](/en-US/docs/Web/CSS/Reference/Properties/padding-right)
- [padding-top](/en-US/docs/Web/CSS/Reference/Properties/padding-top)
- [@page](/en-US/docs/Web/CSS/Reference/At-rules/@page)
- [page](/en-US/docs/Web/CSS/Reference/Properties/page)
- [page-orientation (@page)](/en-US/docs/Web/CSS/Reference/At-rules/@page/page-orientation)
- [paint()](/en-US/docs/Web/CSS/Reference/Values/image/paint)
- [paint-order](/en-US/docs/Web/CSS/Reference/Properties/paint-order)
- `palette-mix()`
- `::part()`
- [:past](/en-US/docs/Web/CSS/Reference/Selectors/:past)
- [path()](/en-US/docs/Web/CSS/Reference/Values/basic-shape/path)
- [:paused](/en-US/docs/Web/CSS/Reference/Selectors/:paused)
- `pc`
- [<percentage>](/en-US/docs/Web/CSS/Reference/Values/percentage)
- [perspective](/en-US/docs/Web/CSS/Reference/Properties/perspective)
- [perspective()](/en-US/docs/Web/CSS/Reference/Values/transform-function/perspective)
- [perspective-origin](/en-US/docs/Web/CSS/Reference/Properties/perspective-origin)
- `::picker()`
- [::picker-icon](/en-US/docs/Web/CSS/Reference/Selectors/::picker-icon)
- [:picture-in-picture](/en-US/docs/Web/CSS/Reference/Selectors/:picture-in-picture)
- [place-content](/en-US/docs/Web/CSS/Reference/Properties/place-content)
- [place-items](/en-US/docs/Web/CSS/Reference/Properties/place-items)
- [place-self](/en-US/docs/Web/CSS/Reference/Properties/place-self)
- [::placeholder](/en-US/docs/Web/CSS/Reference/Selectors/::placeholder)
- [:placeholder-shown](/en-US/docs/Web/CSS/Reference/Selectors/:placeholder-shown)
- [:playing](/en-US/docs/Web/CSS/Reference/Selectors/:playing)
- [pointer-events](/en-US/docs/Web/CSS/Reference/Properties/pointer-events)
- [polygon()](/en-US/docs/Web/CSS/Reference/Values/basic-shape#polygon)
- [:popover-open](/en-US/docs/Web/CSS/Reference/Selectors/:popover-open)
- [<position>](/en-US/docs/Web/CSS/Reference/Values/position_value)
- [position](/en-US/docs/Web/CSS/Reference/Properties/position)
- [position-anchor](/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
- [position-area](/en-US/docs/Web/CSS/Reference/Properties/position-area)
- [@position-try](/en-US/docs/Web/CSS/Reference/At-rules/@position-try)
- [position-try](/en-US/docs/Web/CSS/Reference/Properties/position-try)
- [position-try-fallbacks](/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks)
- [position-try-order](/en-US/docs/Web/CSS/Reference/Properties/position-try-order)
- [position-visibility](/en-US/docs/Web/CSS/Reference/Properties/position-visibility)
- [pow()](/en-US/docs/Web/CSS/Reference/Values/pow)
- [prefix (@counter-style)](/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/prefix)
- [print-color-adjust](/en-US/docs/Web/CSS/Reference/Properties/print-color-adjust)
- [@property](/en-US/docs/Web/CSS/Reference/At-rules/@property)
- `pt`
- `px`

### Q

- `Q`
- [quotes](/en-US/docs/Web/CSS/Reference/Properties/quotes)

### R

- [r](/en-US/docs/Web/CSS/Reference/Properties/r)
- `rad`
- [radial-gradient()](/en-US/docs/Web/CSS/Reference/Values/gradient/radial-gradient)
- [range (@counter-style)](/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range)
- [<ratio>](/en-US/docs/Web/CSS/Reference/Values/ratio)
- [ray()](/en-US/docs/Web/CSS/Reference/Values/ray)
- [:read-only](/en-US/docs/Web/CSS/Reference/Selectors/:read-only)
- [:read-write](/en-US/docs/Web/CSS/Reference/Selectors/:read-write)
- [rect()](/en-US/docs/Web/CSS/Reference/Values/shape#rect)
- [rem()](/en-US/docs/Web/CSS/Reference/Values/rem)
- [repeat()](/en-US/docs/Web/CSS/Reference/Values/repeat)
- [repeating-conic-gradient()](/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-conic-gradient)
- [repeating-linear-gradient()](/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient)
- [repeating-radial-gradient()](/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-radial-gradient)
- [:required](/en-US/docs/Web/CSS/Reference/Selectors/:required)
- [resize](/en-US/docs/Web/CSS/Reference/Properties/resize)
- [<resolution>](/en-US/docs/Web/CSS/Reference/Values/resolution)
- `reversed()`
- [revert](/en-US/docs/Web/CSS/Reference/Values/revert)
- [rgb()](/en-US/docs/Web/CSS/Reference/Values/color_value/rgb)
- [:right](/en-US/docs/Web/CSS/Reference/Selectors/:right)
- [right](/en-US/docs/Web/CSS/Reference/Properties/right)
- [@right-top](/en-US/docs/Web/CSS/Reference/At-rules/@page#page-margin-box-type)
- [:root](/en-US/docs/Web/CSS/Reference/Selectors/:root)
- [rotate](/en-US/docs/Web/CSS/Reference/Properties/rotate)
- [rotate()](/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate)
- [rotate3d()](/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d)
- [rotateX()](/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateX)
- [rotateY()](/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateY)
- [rotateZ()](/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateZ)
- [round()](/en-US/docs/Web/CSS/Reference/Values/round)
- [row-gap](/en-US/docs/Web/CSS/Reference/Properties/row-gap)
- [ruby-align](/en-US/docs/Web/CSS/Reference/Properties/ruby-align)
- `ruby-merge`
- [ruby-overhang](/en-US/docs/Web/CSS/Reference/Properties/ruby-overhang)
- [ruby-position](/en-US/docs/Web/CSS/Reference/Properties/ruby-position)
- [rx](/en-US/docs/Web/CSS/Reference/Properties/rx)
- [ry](/en-US/docs/Web/CSS/Reference/Properties/ry)

### S

- `s`
- [saturate()](/en-US/docs/Web/CSS/Reference/Values/filter-function/saturate)
- [scale](/en-US/docs/Web/CSS/Reference/Properties/scale)
- [scale()](/en-US/docs/Web/CSS/Reference/Values/transform-function/scale)
- [scale3d()](/en-US/docs/Web/CSS/Reference/Values/transform-function/scale3d)
- [scaleX()](/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleX)
- [scaleY()](/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleY)
- [scaleZ()](/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleZ)
- [:scope](/en-US/docs/Web/CSS/Reference/Selectors/:scope)
- [@scope](/en-US/docs/Web/CSS/Reference/At-rules/@scope)
- [scroll()](/en-US/docs/Web/CSS/Reference/Properties/overflow)
- [scroll-behavior](/en-US/docs/Web/CSS/Reference/Properties/scroll-behavior)
- `scroll-initial-target`
- [scroll-margin](/en-US/docs/Web/CSS/Reference/Properties/scroll-margin)
- [scroll-margin-block](/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-block)
- [scroll-margin-block-end](/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-block-end)
- [scroll-margin-block-start](/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-block-start)
- [scroll-margin-bottom](/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-bottom)
- [scroll-margin-inline](/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-inline)
- [scroll-margin-inline-end](/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-inline-end)
- [scroll-margin-inline-start](/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-inline-start)
- [scroll-margin-left](/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-left)
- [scroll-margin-right](/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-right)
- [scroll-margin-top](/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-top)
- [::scroll-marker](/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker)
- [::scroll-marker-group](/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group)
- [scroll-padding](/en-US/docs/Web/CSS/Reference/Properties/scroll-padding)
- [scroll-padding-block](/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-block)
- [scroll-padding-block-end](/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-block-end)
- [scroll-padding-block-start](/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-block-start)
- [scroll-padding-bottom](/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-bottom)
- [scroll-padding-inline](/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline)
- [scroll-padding-inline-end](/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline-end)
- [scroll-padding-inline-start](/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline-start)
- [scroll-padding-left](/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-left)
- [scroll-padding-right](/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-right)
- [scroll-padding-top](/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-top)
- [scroll-snap-align](/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align)
- [scroll-snap-stop](/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-stop)
- [scroll-snap-type](/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type)
- `scroll-state()`
- [scroll-timeline](/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline)
- [scroll-timeline-axis](/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-axis)
- [scroll-timeline-name](/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name)
- [scrollbar-color](/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color)
- [scrollbar-gutter](/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter)
- [scrollbar-width](/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width)
- [:seeking](/en-US/docs/Web/CSS/Reference/Selectors/:seeking)
- [::selection](/en-US/docs/Web/CSS/Reference/Selectors/::selection)
- `selector()`
- [sepia()](/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia)
- [shape-image-threshold](/en-US/docs/Web/CSS/Reference/Properties/shape-image-threshold)
- [shape-margin](/en-US/docs/Web/CSS/Reference/Properties/shape-margin)
- [shape-outside](/en-US/docs/Web/CSS/Reference/Properties/shape-outside)
- [shape-rendering](/en-US/docs/Web/CSS/Reference/Properties/shape-rendering)
- [sign()](/en-US/docs/Web/CSS/Reference/Values/sign)
- [sin()](/en-US/docs/Web/CSS/Reference/Values/sin)
- [size (@page)](/en-US/docs/Web/CSS/Reference/At-rules/@page/size)
- [size-adjust (@font-face)](/en-US/docs/Web/CSS/Reference/At-rules/@font-face/size-adjust)
- [skew()](/en-US/docs/Web/CSS/Reference/Values/transform-function/skew)
- [skewX()](/en-US/docs/Web/CSS/Reference/Values/transform-function/skewX)
- [skewY()](/en-US/docs/Web/CSS/Reference/Values/transform-function/skewY)
- `::slotted()`
- [speak-as](/en-US/docs/Web/CSS/Reference/Properties/speak-as)
- [speak-as (@counter-style)](/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as)
- [::spelling-error](/en-US/docs/Web/CSS/Reference/Selectors/::spelling-error)
- [sqrt()](/en-US/docs/Web/CSS/Reference/Values/sqrt)
- [src (@font-face)](/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src)
- [:stalled](/en-US/docs/Web/CSS/Reference/Selectors/:stalled)
- [@starting-style](/en-US/docs/Web/CSS/Reference/At-rules/@starting-style)
- `:state()`
- [steps()](/en-US/docs/Web/CSS/Reference/Values/easing-function#steps_easing_function)
- [stop-color](/en-US/docs/Web/CSS/Reference/Properties/stop-color)
- [stop-opacity](/en-US/docs/Web/CSS/Reference/Properties/stop-opacity)
- [<string>](/en-US/docs/Web/CSS/Reference/Values/string)
- [stroke](/en-US/docs/Web/CSS/Reference/Properties/stroke)
- `stroke-color`
- [stroke-dasharray](/en-US/docs/Web/CSS/Reference/Properties/stroke-dasharray)
- [stroke-dashoffset](/en-US/docs/Web/CSS/Reference/Properties/stroke-dashoffset)
- [stroke-linecap](/en-US/docs/Web/CSS/Reference/Properties/stroke-linecap)
- [stroke-linejoin](/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin)
- [stroke-miterlimit](/en-US/docs/Web/CSS/Reference/Properties/stroke-miterlimit)
- [stroke-opacity](/en-US/docs/Web/CSS/Reference/Properties/stroke-opacity)
- [stroke-width](/en-US/docs/Web/CSS/Reference/Properties/stroke-width)
- `style()`
- [@styleset](/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values#styleset)
- [@stylistic](/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values#stylistic)
- [suffix (@counter-style)](/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/suffix)
- [@supports](/en-US/docs/Web/CSS/Reference/At-rules/@supports)
- `supports() (@import)`
- [@swash](/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values#swash)
- [symbols (@counter-style)](/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/symbols)
- [symbols()](/en-US/docs/Web/CSS/Reference/Values/symbols)
- [syntax (@property)](/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax)
- [system (@counter-style)](/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system)

### T

- [tab-size](/en-US/docs/Web/CSS/Reference/Properties/tab-size)
- [table-layout](/en-US/docs/Web/CSS/Reference/Properties/table-layout)
- [tan()](/en-US/docs/Web/CSS/Reference/Values/tan)
- [:target](/en-US/docs/Web/CSS/Reference/Selectors/:target)
- `target-counter()`
- `target-counters()`
- [:target-current](/en-US/docs/Web/CSS/Reference/Selectors/:target-current)
- [::target-text](/en-US/docs/Web/CSS/Reference/Selectors/::target-text)
- `target-text()`
- [:target-within](/en-US/docs/Web/CSS)
- [text-align](/en-US/docs/Web/CSS/Reference/Properties/text-align)
- [text-align-last](/en-US/docs/Web/CSS/Reference/Properties/text-align-last)
- [text-anchor](/en-US/docs/Web/CSS/Reference/Properties/text-anchor)
- [text-autospace](/en-US/docs/Web/CSS/Reference/Properties/text-autospace)
- [text-box](/en-US/docs/Web/CSS/Reference/Properties/text-box)
- [text-box-edge](/en-US/docs/Web/CSS/Reference/Properties/text-box-edge)
- [text-box-trim](/en-US/docs/Web/CSS/Reference/Properties/text-box-trim)
- [text-combine-upright](/en-US/docs/Web/CSS/Reference/Properties/text-combine-upright)
- [text-decoration](/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
- [text-decoration-color](/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)
- [text-decoration-line](/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line)
- [text-decoration-skip](/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip)
- [text-decoration-skip-ink](/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip-ink)
- [text-decoration-style](/en-US/docs/Web/CSS/Reference/Properties/text-decoration-style)
- [text-decoration-thickness](/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness)
- [<text-edge>](/en-US/docs/Web/CSS/Reference/Values/text-edge)
- [text-emphasis](/en-US/docs/Web/CSS/Reference/Properties/text-emphasis)
- [text-emphasis-color](/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-color)
- [text-emphasis-position](/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position)
- [text-emphasis-style](/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style)
- [text-indent](/en-US/docs/Web/CSS/Reference/Properties/text-indent)
- [text-justify](/en-US/docs/Web/CSS/Reference/Properties/text-justify)
- [text-orientation](/en-US/docs/Web/CSS/Reference/Properties/text-orientation)
- [text-overflow](/en-US/docs/Web/CSS/Reference/Properties/text-overflow)
- [text-rendering](/en-US/docs/Web/CSS/Reference/Properties/text-rendering)
- [text-shadow](/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
- [text-size-adjust](/en-US/docs/Web/CSS/Reference/Properties/text-size-adjust)
- [text-spacing-trim](/en-US/docs/Web/CSS/Reference/Properties/text-spacing-trim)
- [text-transform](/en-US/docs/Web/CSS/Reference/Properties/text-transform)
- [text-underline-offset](/en-US/docs/Web/CSS/Reference/Properties/text-underline-offset)
- [text-underline-position](/en-US/docs/Web/CSS/Reference/Properties/text-underline-position)
- [text-wrap](/en-US/docs/Web/CSS/Reference/Properties/text-wrap)
- [text-wrap-mode](/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode)
- [text-wrap-style](/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style)
- [<time>](/en-US/docs/Web/CSS/Reference/Values/time)
- [<time-percentage>](/en-US/docs/Web/CSS/Reference/Values/time-percentage)
- [timeline-scope](/en-US/docs/Web/CSS/Reference/Properties/timeline-scope)
- [top](/en-US/docs/Web/CSS/Reference/Properties/top)
- [@top-left-corner](/en-US/docs/Web/CSS/Reference/At-rules/@page#page-margin-box-type)
- [touch-action](/en-US/docs/Web/CSS/Reference/Properties/touch-action)
- [transform](/en-US/docs/Web/CSS/Reference/Properties/transform)
- [transform-box](/en-US/docs/Web/CSS/Reference/Properties/transform-box)
- [<transform-function>](/en-US/docs/Web/CSS/Reference/Values/transform-function)
- [transform-origin](/en-US/docs/Web/CSS/Reference/Properties/transform-origin)
- [transform-style](/en-US/docs/Web/CSS/Reference/Properties/transform-style)
- [transition](/en-US/docs/Web/CSS/Reference/Properties/transition)
- [transition-behavior](/en-US/docs/Web/CSS/Reference/Properties/transition-behavior)
- [transition-delay](/en-US/docs/Web/CSS/Reference/Properties/transition-delay)
- [transition-duration](/en-US/docs/Web/CSS/Reference/Properties/transition-duration)
- [transition-property](/en-US/docs/Web/CSS/Reference/Properties/transition-property)
- [transition-timing-function](/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function)
- [translate](/en-US/docs/Web/CSS/Reference/Properties/translate)
- [translate()](/en-US/docs/Web/CSS/Reference/Values/transform-function/translate)
- [translate3d()](/en-US/docs/Web/CSS/Reference/Values/transform-function/translate3d)
- [translateX()](/en-US/docs/Web/CSS/Reference/Values/transform-function/translateX)
- [translateY()](/en-US/docs/Web/CSS/Reference/Values/transform-function/translateY)
- [translateZ()](/en-US/docs/Web/CSS/Reference/Values/transform-function/translateZ)
- `turn`
- [type()](/en-US/docs/Web/CSS/Reference/Values/type)
- `types (@view-transition)`

### U

- [unicode-bidi](/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi)
- [unicode-range (@font-face)](/en-US/docs/Web/CSS/Reference/At-rules/@font-face/unicode-range)
- [unset](/en-US/docs/Web/CSS/Reference/Values/unset)
- [<url>](/en-US/docs/Web/CSS/Reference/Values/url_value)
- [url()](/en-US/docs/Web/CSS/Reference/Values/url_value#the_url_functional_notation)
- [:user-invalid](/en-US/docs/Web/CSS/Reference/Selectors/:user-invalid)
- [user-select](/en-US/docs/Web/CSS/Reference/Properties/user-select)
- [:user-valid](/en-US/docs/Web/CSS/Reference/Selectors/:user-valid)

### V

- [:valid](/en-US/docs/Web/CSS/Reference/Selectors/:valid)
- [var()](/en-US/docs/Web/CSS/Reference/Values/var)
- [vector-effect](/en-US/docs/Web/CSS/Reference/Properties/vector-effect)
- [vertical-align](/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
- `vh`
- [view()](/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)
- [view-timeline](/en-US/docs/Web/CSS/Reference/Properties/view-timeline)
- [view-timeline-axis](/en-US/docs/Web/CSS/Reference/Properties/view-timeline-axis)
- [view-timeline-inset](/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset)
- [view-timeline-name](/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name)
- [::view-transition](/en-US/docs/Web/CSS/Reference/Selectors/::view-transition)
- [@view-transition](/en-US/docs/Web/CSS/Reference/At-rules/@view-transition)
- [view-transition-class](/en-US/docs/Web/CSS/Reference/Properties/view-transition-class)
- `::view-transition-group()`
- `::view-transition-image-pair()`
- [view-transition-name](/en-US/docs/Web/CSS/Reference/Properties/view-transition-name)
- `::view-transition-new()`
- `::view-transition-old()`
- [visibility](/en-US/docs/Web/CSS/Reference/Properties/visibility)
- [:visited](/en-US/docs/Web/CSS/Reference/Selectors/:visited)
- `vmax`
- `vmin`
- [:volume-locked](/en-US/docs/Web/CSS/Reference/Selectors/:volume-locked)
- `vw`

### W

- `:where()`
- [white-space](/en-US/docs/Web/CSS/Reference/Properties/white-space)
- [white-space-collapse](/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse)
- [widows](/en-US/docs/Web/CSS/Reference/Properties/widows)
- [width](/en-US/docs/Web/CSS/Reference/Properties/width)
- [will-change](/en-US/docs/Web/CSS/Reference/Properties/will-change)
- [word-break](/en-US/docs/Web/CSS/Reference/Properties/word-break)
- [word-spacing](/en-US/docs/Web/CSS/Reference/Properties/word-spacing)
- [word-wrap](/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap)
- [writing-mode](/en-US/docs/Web/CSS/Reference/Properties/writing-mode)

### X

- [x](/en-US/docs/Web/CSS/Reference/Properties/x)
- `:xr-overlay`
- `xywh()`

### Y

- [y](/en-US/docs/Web/CSS/Reference/Properties/y)

### Z

- [z-index](/en-US/docs/Web/CSS/Reference/Properties/z-index)
- [zoom](/en-US/docs/Web/CSS/Reference/Properties/zoom)

## [Selectors](#selectors)

The following are the various [selectors](/en-US/docs/Web/CSS/Reference/Selectors), which allow styles to be conditional based on various features of elements within the DOM.

### [Basic selectors](#basic_selectors)

Basic selectors are fundamental selectors; these are the most basic selectors that are frequently combined to create other, more complex selectors.

- [Universal selector](/en-US/docs/Web/CSS/Reference/Selectors/Universal_selectors)`*`
- [Type selector](/en-US/docs/Web/CSS/Reference/Selectors/Type_selectors)`elementname`
- [Class selector](/en-US/docs/Web/CSS/Reference/Selectors/Class_selectors)`.classname`
- [ID selector](/en-US/docs/Web/CSS/Reference/Selectors/ID_selectors)`#idname`
- [Attribute selector](/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors)`[attr=value]`

### [Grouping selectors](#grouping_selectors)

[Selector list](/en-US/docs/Web/CSS/Reference/Selectors/Selector_list)`A, B`

Specifies that both `A` and `B` elements are selected. This is a grouping method to select several matching elements.

### [Combinators](#combinators)

Combinators are selectors that establish a relationship between two or more simple selectors, such as "`A` is a child of `B`" or "`A` is adjacent to `B`", creating a complex selector.

[Next-sibling combinator](/en-US/docs/Web/CSS/Reference/Selectors/Next-sibling_combinator)`A + B`

Specifies that the elements selected by both `A` and `B` have the same parent and that the element selected by `B` immediately follows the element selected by `A` horizontally.

[Subsequent-sibling combinator](/en-US/docs/Web/CSS/Reference/Selectors/Subsequent-sibling_combinator)`A ~ B`

Specifies that the elements selected by both `A` and `B` share the same parent and that the element selected by `A` comes before—but not necessarily immediately before—the element selected by `B`.

[Child combinator](/en-US/docs/Web/CSS/Reference/Selectors/Child_combinator)`A > B`

Specifies that the element selected by `B` is the direct child of the element selected by `A`.

[Descendant combinator](/en-US/docs/Web/CSS/Reference/Selectors/Descendant_combinator)`A B`

Specifies that the element selected by `B` is a descendant of the element selected by `A`, but is not necessarily a direct child.

[Column combinator](/en-US/docs/Web/CSS/Reference/Selectors/Column_combinator)`A || B`Experimental

Specifies that the element selected by `B` is located within the table column specified by `A`. Elements which span multiple columns are considered to be a member of all of those columns.

### [Pseudo](#pseudo)

[Pseudo classes](/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)`:`

Specifies a special state of the selected element(s).

[Pseudo elements](/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)`::`

Represents entities that are not included in HTML.

See also [selectors in the Selectors specification](https://drafts.csswg.org/selectors/) and the [pseudo-element specification](https://drafts.csswg.org/css-pseudo/).

## [Concepts](#concepts)

### [Syntax and semantics](#syntax_and_semantics)

- [CSS syntax](/en-US/docs/Web/CSS/Guides/Syntax/Introduction)
- [At-rules](/en-US/docs/Web/CSS/Reference/At-rules)
- [Cascade](/en-US/docs/Web/CSS/Guides/Cascade/Introduction)
- [Comments](/en-US/docs/Web/CSS/Guides/Syntax/Comments)
- [Descriptor](/en-US/docs/Glossary/CSS_Descriptor)
- [Inheritance](/en-US/docs/Web/CSS/Guides/Cascade/Inheritance)
- [Shorthand properties](/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
- [Specificity](/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
- [Values](/en-US/docs/Web/CSS/Reference/Values)
- [Value definition syntax](/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax)
- [CSS values and units](/en-US/docs/Web/CSS/Guides/Values_and_units)
- [CSS functional notations](/en-US/docs/Web/CSS/Reference/Values/Functions)

### [Values](#values)

- [Actual value](/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#actual_value)
- [Computed value](/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
- [Initial value](/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value)
- [Resolved value](/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#resolved_value)
- [Specified value](/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#specified_value)
- [Used value](/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#used_value)

### [Layout](#layout)

- [Block formatting context](/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)
- [Box model](/en-US/docs/Web/CSS/Guides/Box_model/Introduction)
- [Containing block](/en-US/docs/Web/CSS/Guides/Display/Containing_block)
- [Layout mode](/en-US/docs/Glossary/Layout_mode)
- [Margin collapsing](/en-US/docs/Web/CSS/Guides/Box_model/Margin_collapsing)
- [Replaced elements](/en-US/docs/Glossary/Replaced_elements)
- [Stacking context](/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context)
- [Visual formatting model](/en-US/docs/Web/CSS/Guides/Display/Visual_formatting_model)

## [DOM-CSS / CSSOM](#dom-css_cssom)

### [Major object types](#major_object_types)

- [Document.styleSheets](/en-US/docs/Web/API/Document/styleSheets)
- [HTMLElement.style](/en-US/docs/Web/API/HTMLElement/style)
- [Element.className](/en-US/docs/Web/API/Element/className)
- [Element.classList](/en-US/docs/Web/API/Element/classList)
- [StyleSheetList](/en-US/docs/Web/API/StyleSheetList)
- [CSSRuleList](/en-US/docs/Web/API/CSSRuleList)
- [CSSRule](/en-US/docs/Web/API/CSSRule)
- [CSSStyleRule](/en-US/docs/Web/API/CSSStyleRule)
- [CSSStyleDeclaration](/en-US/docs/Web/API/CSSStyleDeclaration)

### [Important methods](#important_methods)

- [CSSStyleSheet.insertRule()](/en-US/docs/Web/API/CSSStyleSheet/insertRule)
- [CSSStyleSheet.deleteRule()](/en-US/docs/Web/API/CSSStyleSheet/deleteRule)

## [See also](#see_also)

- [Mozilla CSS extensions](/en-US/docs/Web/CSS/Reference/Mozilla_extensions) (prefixed with `-moz-`)
- [WebKit CSS extensions](/en-US/docs/Web/CSS/Reference/Webkit_extensions) (mostly prefixed with `-webkit-`)

## [External Links](#external_links)

- [CSS Indices (w3.org)](https://www.w3.org/TR/css/#indices)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/CSS/Reference/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F93b85a5bc2b4589d93185263fd2c14381c36f821%0A*+Document+last+modified%3A+2025-11-13T17%3A22%3A29.000Z%0A%0A%3C%2Fdetails%3E)
