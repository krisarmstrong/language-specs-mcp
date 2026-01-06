# Houdini APIs

Houdini is a set of low-level APIs that exposes parts of the CSS engine, giving developers the power to extend CSS by hooking into the styling and layout process of a browser's rendering engine. Houdini is a group of APIs that give developers direct access to the [CSS Object Model](/en-US/docs/Web/API/CSS_Object_Model) (CSSOM), enabling developers to write code the browser can parse as CSS, thereby creating new CSS features without waiting for them to be implemented natively in browsers.

## In this article

- [Advantages of Houdini](#advantages_of_houdini)
- [The Houdini APIs](#the_houdini_apis)
- [See also](#see_also)

## [Advantages of Houdini](#advantages_of_houdini)

Houdini enables faster parse times than using JavaScript [HTMLElement.style](/en-US/docs/Web/API/HTMLElement/style) for style changes. Browsers parse the CSSOM — including layout, paint, and composite processes — before applying any style updates found in scripts. In addition, layout, paint, and composite processes are repeated for JavaScript style updates. Houdini code doesn't wait for that first rendering cycle to be complete. Rather, it is included in that first cycle — creating renderable, understandable styles. Houdini provides an object-based API for working with CSS values in JavaScript.

Houdini's [CSS Typed Object Model API](/en-US/docs/Web/API/CSS_Typed_OM_API) is a CSS Object Model with types and methods, exposing values as JavaScript objects making for more intuitive CSS manipulation than previous string based [HTMLElement.style](/en-US/docs/Web/API/HTMLElement/style) manipulations. Every element and style sheet rule has a style map which is accessible via its [StylePropertyMap](/en-US/docs/Web/API/StylePropertyMap).

A feature of CSS Houdini is the [Worklet](/en-US/docs/Web/API/Worklet). With worklets, you can create modular CSS, requiring a single line of JavaScript to import configurable components: no pre-processors, post-processors or JavaScript frameworks needed.

js

```
CSS.paintWorklet.addModule("css-component.js");
```

This added module contains [PaintWorkletGlobalScope.registerPaint](/en-US/docs/Web/API/PaintWorkletGlobalScope/registerPaint) functions, which register completely configurable worklets.

The CSS `paint()` function is an additional function supported by the [<image>](/en-US/docs/Web/CSS/Reference/Values/image) type. It takes parameters that include the name of the worklet, plus additional parameters needed by the worklet. The worklet also has access to the element's custom properties: they don't need to be passed as function arguments.

In the following example the `paint()` function is passed a worklet called `my-component`.

css

```
li {
  background-image: paint(my-component, stroke, 10px);
  --highlights: blue;
  --theme: green;
}
```

Note: With great power comes great responsibility! With Houdini you could invent your own masonry, grid, or regions implementation, but doing so is not necessarily the best idea. The CSS Working group does a lot of work to ensure every feature is performant, handles all edge cases, and considers security, privacy, and accessibility. As you extend CSS with Houdini, make sure to keep these considerations in mind, and start small before moving on to more ambitious projects.

## [The Houdini APIs](#the_houdini_apis)

Below you can find links to the main reference pages covering the APIs that fall under the Houdini umbrella, along with links to guides to help you if you need guidance in learning how to use them.

### [CSS Properties and Values API](#css_properties_and_values_api)

Defines an API for registering new CSS properties. Properties registered using this API are provided with a parse syntax that defines a type, inheritance behavior, and an initial value.

- [CSS Properties and Values API reference](/en-US/docs/Web/API/CSS_Properties_and_Values_API)
- [CSS Properties and Values API guide](/en-US/docs/Web/API/CSS_Properties_and_Values_API/guide)
- [Smarter custom properties with Houdini's new API](https://web.dev/articles/css-props-and-vals)

### [CSS Typed OM](#css_typed_om)

Converting CSSOM value strings into meaningfully typed JavaScript representations and back can incur a significant performance overhead. The CSS Typed OM exposes CSS values as typed JavaScript objects to allow their performant manipulation.

- [CSS Typed OM reference](/en-US/docs/Web/API/CSS_Typed_OM_API)
- [CSS Typed OM guide](/en-US/docs/Web/API/CSS_Typed_OM_API/Guide)
- [Working with the new CSS Typed Object Model](https://developer.chrome.com/docs/css-ui/cssom)

### [CSS Painting API](#css_painting_api)

Developed to improve the extensibility of CSS, the Painting API allows developers to write JavaScript functions that can draw directly into an element's background, border, or content via the `paint()` CSS function.

- [CSS Painting API reference](/en-US/docs/Web/API/CSS_Painting_API)
- [CSS Painting API guide](/en-US/docs/Web/API/CSS_Painting_API/Guide)
- [CSS Paint API](https://developer.chrome.com/blog/paintapi/)
- [The CSS Paint API](https://css-tricks.com/the-css-paint-api/)
- [Simulating Drop Shadows with the CSS Paint API](https://css-tricks.com/simulating-drop-shadows-with-the-css-paint-api/)
- [CSS Paint API Being predictably random](https://jakearchibald.com/2020/css-paint-predictably-random/)

### [Worklets](#worklets)

An API for running scripts in various stages of the rendering pipeline independent of the main JavaScript execution environment. Worklets are conceptually similar to [Web Workers](/en-US/docs/Web/API/Web_Workers_API/Using_web_workers), and are called by and extend the rendering engine.

- [Worklets reference](/en-US/docs/Web/API/Worklet)

### [CSS Layout API](#css_layout_api)

Designed to improve the extensibility of CSS, this API enables developers to write their own layout algorithms, like masonry or line snapping.

This API has some partial support in Chrome Canary. It is not yet documented on MDN.

### [CSS Parser API](#css_parser_api)

An API exposing the CSS parser more directly, for parsing arbitrary CSS-like languages into a mildly typed representation.

This API is currently a proposal, and has no browser implementations or documentation on MDN.

- [Proposal](https://github.com/WICG/css-parser-api)

### [Font Metrics API](#font_metrics_api)

An API exposing font metrics, giving access to typographic layout results.

This API is currently a proposal, and has no browser implementations or documentation on MDN.

- [Proposal](https://github.com/w3c/css-houdini-drafts/blob/main/font-metrics-api/README.md)

## [See also](#see_also)

- [A Practical Overview of CSS Houdini](https://www.smashingmagazine.com/2020/03/practical-overview-css-houdini/)
- [Smarter custom properties with Houdini's new API](https://web.dev/articles/css-props-and-vals)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 5, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Houdini_APIs/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/houdini_apis/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHoudini_APIs&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhoudini_apis%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHoudini_APIs%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhoudini_apis%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F635820782735cd00f71ce3929ff9377b091f8995%0A*+Document+last+modified%3A+2025-08-05T14%3A01%3A02.000Z%0A%0A%3C%2Fdetails%3E)
