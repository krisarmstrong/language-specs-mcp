# CSSContainerRule

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨February 2023⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSContainerRule&level=high)

The `CSSContainerRule` interface represents a single CSS [@container](/en-US/docs/Web/CSS/Reference/At-rules/@container) rule.

An object of this type can be used to get the query conditions for the [@container](/en-US/docs/Web/CSS/Reference/At-rules/@container), along with the container name if one is defined. Note that the container name and query together define the "condition text", which can be obtained using [CSSConditionRule.conditionText](/en-US/docs/Web/API/CSSConditionRule/conditionText).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its ancestors [CSSConditionRule](/en-US/docs/Web/API/CSSConditionRule), [CSSGroupingRule](/en-US/docs/Web/API/CSSGroupingRule), and [CSSRule](/en-US/docs/Web/API/CSSRule).

[CSSContainerRule.containerName](/en-US/docs/Web/API/CSSContainerRule/containerName)Read only

Returns a string representing the name of an [@container](/en-US/docs/Web/CSS/Reference/At-rules/@container), or an empty string.

[CSSContainerRule.containerQuery](/en-US/docs/Web/API/CSSContainerRule/containerQuery)Read only

Returns a string representing the set of features or "container conditions" that are evaluated to determine if the styles in the associated [@container](/en-US/docs/Web/CSS/Reference/At-rules/@container) are applied.

## [Instance methods](#instance_methods)

No specific methods; inherits methods from its ancestors [CSSConditionRule](/en-US/docs/Web/API/CSSConditionRule), [CSSGroupingRule](/en-US/docs/Web/API/CSSGroupingRule), and [CSSRule](/en-US/docs/Web/API/CSSRule).

## [Examples](#examples)

### [Unnamed container rule](#unnamed_container_rule)

The example below defines an unnamed [@container](/en-US/docs/Web/CSS/Reference/At-rules/@container) rule, and displays the properties of the associated `CSSContainerRule`. The CSS is the same as in the `@container` example [Setting styles based on a container's size](/en-US/docs/Web/CSS/Reference/At-rules/@container#setting_styles_based_on_a_containers_size).

The first part of the code simply creates a list for logging the container rule properties, along with a JavaScript `log()` method to simplify adding the properties.

html

```
<div id="log">
  <h2>Log</h2>
  <ul></ul>
  <hr />
</div>
```

js

```
// Store reference to log list
const logList = document.querySelector("#log ul");
// Function to log data from underlying source
function log(result) {
  const listItem = document.createElement("li");
  listItem.textContent = result;
  logList.appendChild(listItem);
}
```

Then we define the HTML for a `card` (`<div>`) contained within a `post`.

html

```
<div class="post">
  <div class="card">
    <h2>Card title</h2>
    <p>Card content</p>
  </div>
</div>
```

The CSS for the example is shown below. As described in the corresponding [@container](/en-US/docs/Web/CSS/Reference/At-rules/@container) example, the CSS for the container element specifies the type of the container. The [@container](/en-US/docs/Web/CSS/Reference/At-rules/@container) then applies a new width, font-size and background color to the card if the width is less than 650px.

html

```
<style id="example-styles">
  /* A container context based on inline size */
  .post {
    container-type: inline-size;
  }

  /* Apply styles if the container is narrower than 650px */
  @container (width < 650px) {
    .card {
      width: 50%;
      background-color: gray;
      font-size: 1em;
    }
  }
</style>
```

The code below gets the [HTMLStyleElement](/en-US/docs/Web/API/HTMLStyleElement) associated with the example using its id, and then uses its `sheet` property to get the [StyleSheet](/en-US/docs/Web/API/StyleSheet). From the `StyleSheet` we get the set of `cssRules` added to the sheet. Since we added the `@container` as the second rule above, we can access the associated `CSSContainerRule` using the second entry, with index "1", in the `cssRules`. Last of all, we log the `containerName`, `containerQuery` and `conditionText` (inherited) properties.

js

```
const exampleStylesheet = document.getElementById("example-styles").sheet;
const exampleRules = exampleStylesheet.cssRules;
const containerRule = exampleRules[1]; // a CSSContainerRule representing the container rule.
log(`CSSContainerRule.containerName: "${containerRule.containerName}"`);
log(`CSSContainerRule.containerQuery: "${containerRule.containerQuery}"`);
log(`CSSContainerRule.conditionText: "${containerRule.conditionText}"`);
```

Note: The styles for this example are defined in an inline HTML `style` element with an id in order to make it easy for the code to find the correct sheet. You might also locate the correct sheets for each example from the document by indexing against the length (e.g., `document.styleSheets[document.styleSheets.length-1]` but that makes working out correct sheet for each example more complicated).

The example output is shown below. The log section lists the `containerName`, which is an empty string as no name has been defined. The `containerQuery` and `conditionText` strings are also logged, and have the same value because there is no name defined. The card should change background and as the width of the page transitions through 650px.

### [Named container rule](#named_container_rule)

The example below defines a named [@container](/en-US/docs/Web/CSS/Reference/At-rules/@container) rule, and displays the properties of the associated `CSSContainerRule`. The CSS is very similar to that in the `@container` example [Creating named container contexts](/en-US/docs/Web/CSS/Reference/At-rules/@container#creating_named_container_contexts).

```
<div id="log">
  <h2>Log</h2>
  <ul></ul>
  <hr />
</div>
```

```
// Store reference to log list
const logList = document.querySelector("#log ul");
// Function to log data from underlying source
function log(result) {
  const listItem = document.createElement("li");
  listItem.textContent = result;
  logList.appendChild(listItem);
}
```

First we define the HTML for a `card` (`<div>`) contained within a `post` (the example does not show the logging code, as this is the same as in the previous example).

html

```
<div class="post">
  <div class="card">
    <h2>Card title</h2>
    <p>Card content</p>
  </div>
</div>
```

As described in [@container](/en-US/docs/Web/CSS/Reference/At-rules/@container), the CSS for the container element specifies the type of the container, and may also specify a name for the container. The card has a default font size, which is overridden for the `@container` named `sidebar` if the minimum width is greater than 700px.

html

```
<style id="example-styles">
  .post {
    container-type: inline-size;
    container-name: sidebar;
  }

  /* Default heading styles for the card title */
  .card h2 {
    font-size: 1em;
  }

  @container sidebar (width >= 700px) {
    .card {
      font-size: 2em;
    }
  }
</style>
```

The code for getting the sheet and rules is almost identical to the previous example. The only difference is that in this example we have three CSS rules, so to get the associated `CSSContainerRule` we get the third entry in the `cssRules`.

js

```
const exampleStylesheet = document.getElementById("example-styles").sheet;
const exampleRules = exampleStylesheet.cssRules;
const containerRule = exampleRules[2]; // a CSSContainerRule representing the container rule.
log(`CSSContainerRule.containerName: "${containerRule.containerName}"`);
log(`CSSContainerRule.containerQuery: "${containerRule.containerQuery}"`);
log(`CSSContainerRule.conditionText: "${containerRule.conditionText}"`);
```

The example output is shown below. The log section lists the `containerName` and `containerQuery` strings. The `conditionText` is also logged, and shows the combination of these two strings. The title in the card section should double in size as the width of the page goes over 700px.

## [Specifications](#specifications)

Specification
[CSS Conditional Rules Module Level 5# the-csscontainerrule-interface](https://drafts.csswg.org/css-conditional-5/#the-csscontainerrule-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- CSS [container-name](/en-US/docs/Web/CSS/Reference/Properties/container-name), [container-type](/en-US/docs/Web/CSS/Reference/Properties/container-type), and [container](/en-US/docs/Web/CSS/Reference/Properties/container) shorthand properties
- [CSS containment module](/en-US/docs/Web/CSS/Guides/Containment)
- [Container queries](/en-US/docs/Web/CSS/Guides/Containment/Container_queries)
- [Using container size and style queries](/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSContainerRule/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/csscontainerrule/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSContainerRule&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcsscontainerrule%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSContainerRule%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcsscontainerrule%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
