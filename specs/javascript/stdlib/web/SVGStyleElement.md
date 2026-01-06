# SVGStyleElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGStyleElement&level=high)

The `SVGStyleElement` interface corresponds to the SVG [<style>](/en-US/docs/Web/SVG/Reference/Element/style) element.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Getting and setting properties](#getting_and_setting_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent interface, [SVGElement](/en-US/docs/Web/API/SVGElement).

[SVGStyleElement.type](/en-US/docs/Web/API/SVGStyleElement/type)Deprecated

A string corresponding to the [type](/en-US/docs/Web/SVG/Reference/Attribute/type) attribute of the given element.

[SVGStyleElement.media](/en-US/docs/Web/API/SVGStyleElement/media)

A string corresponding to the [media](/en-US/docs/Web/SVG/Reference/Attribute/media) attribute of the given element.

[SVGStyleElement.title](/en-US/docs/Web/API/SVGStyleElement/title)

A string corresponding to the [title](/en-US/docs/Web/SVG/Reference/Element/style#title) attribute of the given element.

[SVGStyleElement.sheet](/en-US/docs/Web/API/SVGStyleElement/sheet)Read only

Returns the [CSSStyleSheet](/en-US/docs/Web/API/CSSStyleSheet) object associated with the given element, or `null` if there is none.

[SVGStyleElement.disabled](/en-US/docs/Web/API/SVGStyleElement/disabled)

A boolean value indicating whether or not the associated stylesheet is disabled.

## [Instance methods](#instance_methods)

This interface doesn't implement any specific methods, but inherits methods from its parent interface, [SVGElement](/en-US/docs/Web/API/SVGElement).

## [Examples](#examples)

### [Dynamically adding an SVG style element](#dynamically_adding_an_svg_style_element)

To dynamically create an SVG style element (`SVGStyleElement`), you need to use [Document.createElementNS()](/en-US/docs/Web/API/Document/createElementNS), specifying a `style` element in the SVG namespace.

Note:[Document.createElement()](/en-US/docs/Web/API/Document/createElement) can't be used to create SVG style elements (it returns an [HTMLStyleElement](/en-US/docs/Web/API/HTMLStyleElement)).

Given the following SVG element:

html

```
<svg
  xmlns="http://www.w3.org/2000/svg"
  xmlns:xlink="http://www.w3.org/1999/xlink">
  <circle cx="50" cy="50" r="25" />
</svg>
```

You can create an SVG style element as shown:

js

```
// Get the SVG element object by tag name
const svg = document.querySelector("svg");

// Create the `style` element in the SVG namespace
const style = document.createElementNS("http://www.w3.org/2000/svg", "style");
const node = document.createTextNode("circle { fill: red; }");
style.appendChild(node);

// Append the style element to the SVG element
svg.appendChild(style);
```

### [Accessing an existing SVG style](#accessing_an_existing_svg_style)

You can access an SVG style element that was defined in HTML (or an SVG file) using the normal HTML methods for getting tags, ids, and so on. These include: [Document.getElementsByTagName()](/en-US/docs/Web/API/Document/getElementsByTagName), [Document.getElementById()](/en-US/docs/Web/API/Document/getElementById), [Document.querySelector()](/en-US/docs/Web/API/Document/querySelector), [Document.querySelectorAll()](/en-US/docs/Web/API/Document/querySelectorAll), and so on.

For example, consider the HTML below that defines an SVG file with a style element.

html

```
<svg
  xmlns="http://www.w3.org/2000/svg"
  xmlns:xlink="http://www.w3.org/1999/xlink">
  <style id="circle_style_id">
    circle {
      fill: gold;
      stroke: green;
      stroke-width: 3px;
    }
  </style>
  <circle cx="50" cy="50" r="25" />
</svg>
```

To fetch the first `style` element in the first `svg` element, you might use [Document.querySelector()](/en-US/docs/Web/API/Document/querySelector) as shown below.

js

```
const svg = document.querySelector("svg");
const style = svg.querySelector("style");
```

Alternatively, you can could use [Document.getElementById()](/en-US/docs/Web/API/Document/getElementById), specifying the tag id:

js

```
const svg = document.querySelector("svg");
const style = svg.getElementById("circle_style_id");
```

Or just get the element from document by id (in this case using `document.querySelector()`):

js

```
const style = document.querySelector("#circle_style_id");
```

## [Getting and setting properties](#getting_and_setting_properties)

This example demonstrates how to get and set the properties of a style element, which in this case was specified in an SVG definition.

### [HTML](#html)

The HTML contains an SVG definition for a [<circle>](/en-US/docs/Web/SVG/Reference/Element/circle) with a [<style>](/en-US/docs/Web/SVG/Reference/Element/style) element, along with an HTML [<button>](/en-US/docs/Web/HTML/Reference/Elements/button) element that will be used to enable and disable the style, and an HTML [<textarea>](/en-US/docs/Web/HTML/Reference/Elements/button) element for logging the property values.

html

```
<button>Disable</button>
<textarea id="log" rows="6" cols="90"></textarea>
<svg
  xmlns="http://www.w3.org/2000/svg"
  xmlns:xlink="http://www.w3.org/1999/xlink">
  <style id="circle_style_id" media="(width >= 600px)">
    circle {
      fill: gold;
      stroke: green;
      stroke-width: 3px;
    }
  </style>
  <circle cx="60" cy="60" r="50" />
</svg>
```

Note that above we have set the `media` attribute on the `style` tag. We have not set `type` as it is deprecated, or `disabled` because there is no such attribute (only the property on the element).

### [JavaScript](#javascript)

The code below gets the `style` element (an `SVGStyleElement`) using its id.

js

```
const svg = document.querySelector("svg");
const style = svg.getElementById("circle_style_id");
```

We then add a function to log the style properties. This is called after initialization, whenever the frame resizes, and if the button is pressed.

js

```
// Get logging text area
const log = document.getElementById("log");

function setLogText() {
  // Log current values of properties
  log.value = `style.media: ${style.media} (frame width: ${window.innerWidth})\n`; // 'all' by default
  log.value += `style.title: ${style.title}\n`; // no default value
  log.value += `style.disabled: ${style.disabled}\n`; // 'false' by default
  log.value += `style.type: ${style.type}\n`; // deprecated (do not use)
  log.value += `style.sheet.rules[0].cssText: ${style.sheet.rules[0].cssText}\n`;
}

// Log initial property values
setLogText();

// Log when the frame resizes
addEventListener("resize", () => {
  setLogText();
});
```

Last of all we set an event handler for the button. When the button is clicked the [disabled](/en-US/docs/Web/API/SVGStyleElement/disabled) property is toggled. This also updates the log and the button text.

js

```
const button = document.querySelector("button");

button.addEventListener("click", () => {
  style.disabled = !style.disabled;
  button.textContent = style.disabled ? "Enable" : "Disable";

  // Log after button presses
  setLogText();
});
```

### [Result](#result)

The result is shown below. Toggle the button to enable and disable the SVG style element. If the SVG style is not disabled, you can also resize the window width to see the effect of the `media` property on the style when the frame holding the live example is 600px wide.

## [Specifications](#specifications)

Specification
[Scalable Vector Graphics (SVG) 2# InterfaceSVGStyleElement](https://svgwg.org/svg2-draft/styling.html#InterfaceSVGStyleElement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [HTMLStyleElement](/en-US/docs/Web/API/HTMLStyleElement)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 1, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SVGStyleElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svgstyleelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGStyleElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvgstyleelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGStyleElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvgstyleelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F63cbf204323f117a2a80c7aa6273e50253ab9d07%0A*+Document+last+modified%3A+2025-07-01T15%3A43%3A47.000Z%0A%0A%3C%2Fdetails%3E)
