# CSS Custom Highlight API

The CSS Custom Highlight API provides a mechanism for styling arbitrary text ranges on a document by using JavaScript to create the ranges, and CSS to style them.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

Styling text ranges on a webpage can be very useful. For example, text editing web apps highlight spelling or grammar errors, and code editors highlight syntax errors.

The CSS Custom Highlight API extends the concept of other highlight pseudo-elements such as [::selection](/en-US/docs/Web/CSS/Reference/Selectors/::selection), [::spelling-error](/en-US/docs/Web/CSS/Reference/Selectors/::spelling-error), [::grammar-error](/en-US/docs/Web/CSS/Reference/Selectors/::grammar-error), and [::target-text](/en-US/docs/Web/CSS/Reference/Selectors/::target-text) by providing a way to create and style arbitrary [Range](/en-US/docs/Web/API/Range) objects, rather than being limited to browser-defined ranges.

Using the CSS Custom Highlight API, you can programmatically create text ranges and highlight them without affecting the DOM structure in the page.

There are four steps to style text ranges on a webpage using the CSS Custom Highlight API:

1. Creating [Range](/en-US/docs/Web/API/Range) objects.
2. Creating [Highlight](/en-US/docs/Web/API/Highlight) objects for these ranges.
3. Registering the highlights using the [HighlightRegistry](/en-US/docs/Web/API/HighlightRegistry).
4. Styling the highlights using the [::highlight()](/en-US/docs/Web/CSS/Reference/Selectors/::highlight) pseudo-element.

### [Create ranges](#create_ranges)

The first step is to define the text ranges that you want to style by creating [Range](/en-US/docs/Web/API/Range) objects in JavaScript. For example:

js

```
const parentNode = document.getElementById("foo");

const range1 = new Range();
range1.setStart(parentNode, 10);
range1.setEnd(parentNode, 20);

const range2 = new Range();
range2.setStart(parentNode, 40);
range2.setEnd(parentNode, 60);
```

### [Create highlights](#create_highlights)

The second step is to instantiate [Highlight](/en-US/docs/Web/API/Highlight) objects for your text ranges.

Multiple ranges can be associated to one highlight. If you want to highlight multiple pieces of text the same way, you need to create a single highlight and initialize it with the corresponding ranges.

js

```
const highlight = new Highlight(range1, range2);
```

But you can also create as many highlights as you need. For example, if you are building a collaborative text editor where each user gets a different text color, then you can create one highlight per user, as seen in the code snippet below:

js

```
const user1Highlight = new Highlight(user1Range1, user1Range2);
const user2Highlight = new Highlight(user2Range1, user2Range2, user2Range3);
```

Each highlight can be styled differently.

### [Register highlights](#register_highlights)

Once highlights have been created, register them by using the [HighlightRegistry](/en-US/docs/Web/API/HighlightRegistry) available as [CSS.highlights](/en-US/docs/Web/API/CSS/highlights_static).

The registry is a [Map](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)-like object used to register highlights by names, as seen below:

js

```
CSS.highlights.set("user-1-highlight", user1Highlight);
CSS.highlights.set("user-2-highlight", user2Highlight);
```

In the above code snippet, the `user-1-highlight` and `user-2-highlight` strings are custom identifiers that can be used in CSS to apply styles to the registered highlights.

You can register as many highlights as you need in the registry, as well as remove highlights and clear the entire registry.

js

```
// Remove a single highlight from the registry.
CSS.highlights.delete("user-1-highlight");

// Clear the registry.
CSS.highlights.clear();
```

### [Style highlights](#style_highlights)

The final step is to style the registered highlights. This is done by using the [::highlight()](/en-US/docs/Web/CSS/Reference/Selectors/::highlight) pseudo-element. For example, to style the `user-1-highlight` highlight registered in the previous step:

css

```
::highlight(user-1-highlight) {
  background-color: yellow;
  color: black;
}
```

## [Interfaces](#interfaces)

[Highlight](/en-US/docs/Web/API/Highlight)

This interface is used to represent a collection of ranges to be styled on a document.

[HighlightRegistry](/en-US/docs/Web/API/HighlightRegistry)

Accessible via [CSS.highlights](/en-US/docs/Web/API/CSS/highlights_static), this [Map](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)-like object is used to register highlights with custom identifiers.

## [Examples](#examples)

### [Highlighting search results](#highlighting_search_results)

This example shows how to use the CSS Custom Highlight API to highlight search results.

#### HTML

The HTML code snippet below defines a search field and an article with a few paragraphs of text:

html

```
<label>Search within text <input id="query" type="text" /></label>
<article>
  <p>
    Maxime debitis hic, delectus perspiciatis laborum molestiae labore,
    deleniti, quam consequatur iure veniam alias voluptas nisi quo. Dolorem
    eaque alias, quo vel quas repudiandae architecto deserunt quidem, sapiente
    laudantium nulla.
  </p>
  <p>
    Maiores odit molestias, necessitatibus doloremque dolor illum reprehenderit
    provident nostrum laboriosam iste, tempore perferendis! Ab porro neque esse
    voluptas libero necessitatibus fugiat, ex, minus atque deserunt veniam
    molestiae tempora? Vitae.
  </p>
  <p>
    Dolorum facilis voluptate eaque eius similique ducimus dignissimos assumenda
    quos architecto. Doloremque deleniti non exercitationem rerum quam alias
    harum, nisi obcaecati corporis temporibus vero sapiente voluptatum est
    quibusdam id ipsa.
  </p>
</article>
```

#### JavaScript

JavaScript is used to listen to the `input` event on the search field. When the event is fired, the code locates matches for the input text in the article text. It then creates ranges for the matches, and uses the CSS Custom Highlight API to create and register a `search-results` highlight object:

js

```
const query = document.getElementById("query");
const article = document.querySelector("article");

// Find all text nodes in the article. We'll search within
// these text nodes.
const treeWalker = document.createTreeWalker(article, NodeFilter.SHOW_TEXT);
const allTextNodes = [];
let currentNode = treeWalker.nextNode();
while (currentNode) {
  allTextNodes.push(currentNode);
  currentNode = treeWalker.nextNode();
}

// Listen to the input event to run the search.
query.addEventListener("input", () => {
  // If the CSS Custom Highlight API is not supported,
  // display a message and bail-out.
  if (!CSS.highlights) {
    article.textContent = "CSS Custom Highlight API not supported.";
    return;
  }

  // Clear the HighlightRegistry to remove the
  // previous search results.
  CSS.highlights.clear();

  // Clean-up the search query and bail-out if
  // if it's empty.
  const str = query.value.trim().toLowerCase();
  if (!str) {
    return;
  }

  // Iterate over all text nodes and find matches.
  const ranges = allTextNodes
    .map((el) => ({ el, text: el.textContent.toLowerCase() }))
    .map(({ text, el }) => {
      const indices = [];
      let startPos = 0;
      while (startPos < text.length) {
        const index = text.indexOf(str, startPos);
        if (index === -1) break;
        indices.push(index);
        startPos = index + str.length;
      }

      // Create a range object for each instance of
      // str we found in the text node.
      return indices.map((index) => {
        const range = new Range();
        range.setStart(el, index);
        range.setEnd(el, index + str.length);
        return range;
      });
    });

  // Create a Highlight object for the ranges.
  const searchResultsHighlight = new Highlight(...ranges.flat());

  // Register the Highlight object in the registry.
  CSS.highlights.set("search-results", searchResultsHighlight);
});
```

#### CSS

Finally, the `::highlight()` pseudo-element is used in CSS to style the highlights:

css

```
::highlight(search-results) {
  background-color: #ff0066;
  color: white;
}
```

#### Result

The result is shown below. Type text within the search field to highlight matches in the article:

## [Specifications](#specifications)

Specification[CSS Custom Highlight API Module Level 1](https://drafts.csswg.org/css-highlight-api-1/)

## [Browser compatibility](#browser_compatibility)

### [api.Highlight](#api.Highlight)

### [api.HighlightRegistry](#api.HighlightRegistry)

### [css.selectors.highlight](#css.selectors.highlight)

## [See also](#see_also)

- [CSS Custom Highlight API: The Future of Highlighting Text Ranges on the Web](https://css-tricks.com/css-custom-highlight-api-early-look/)
- HTML [contentEditable](/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable) attribute
- CSS [pseudo-elements](/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
- [CSS custom highlight API](/en-US/docs/Web/CSS/Guides/Custom_highlight_API) module

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSS_Custom_Highlight_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/css_custom_highlight_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSS_Custom_Highlight_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcss_custom_highlight_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSS_Custom_Highlight_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcss_custom_highlight_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
