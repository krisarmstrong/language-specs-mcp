# URL Fragment Text Directives

The URL fragment text directives API allows web apps to interact with text fragments in the URL. [Text fragments](/en-US/docs/Web/URI/Reference/Fragment/Text_fragments) allow linking directly to a specific portion of text in a web document, without requiring the author to annotate it with an ID, using a particular syntax in the URL fragment.

## In this article

- [Interfaces](#interfaces)
- [Extensions to other interfaces](#extensions_to_other_interfaces)
- [CSS selectors](#css_selectors)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Interfaces](#interfaces)

[FragmentDirective](/en-US/docs/Web/API/FragmentDirective)

A (currently) empty object. The existence of an object of this type in [document.fragmentDirective](/en-US/docs/Web/API/Document/fragmentDirective) is used for feature detection.

## [Extensions to other interfaces](#extensions_to_other_interfaces)

[Document.fragmentDirective](/en-US/docs/Web/API/Document/fragmentDirective)

A property that returns a `FragmentDirective` object for the current document. Currently only used for feature detection.

## [CSS selectors](#css_selectors)

[::target-text](/en-US/docs/Web/CSS/Reference/Selectors/::target-text)

Represents the text that has been scrolled to. It allows authors to choose how to highlight that section of text.

## [Specifications](#specifications)

Specification
[URL Fragment Text Directives# dom-document-fragmentdirective](https://wicg.github.io/scroll-to-text-fragment/#dom-document-fragmentdirective)
[URL Fragment Text Directives# fragmentdirective](https://wicg.github.io/scroll-to-text-fragment/#fragmentdirective)
[CSS Pseudo-Elements Module Level 4# selectordef-target-text](https://drafts.csswg.org/css-pseudo/#selectordef-target-text)

## [Browser compatibility](#browser_compatibility)

### [api.Document.fragmentDirective](#api.Document.fragmentDirective)

### [api.FragmentDirective](#api.FragmentDirective)

### [css.selectors.target-text](#css.selectors.target-text)

## [See also](#see_also)

- [URI fragment](/en-US/docs/Web/URI/Reference/Fragment)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 18, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/URL_Fragment_Text_Directives/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/url_fragment_text_directives/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FURL_Fragment_Text_Directives&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Furl_fragment_text_directives%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FURL_Fragment_Text_Directives%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Furl_fragment_text_directives%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4d9320f9857fb80fef5f3fe78e3d09b06eb0ebbd%0A*+Document+last+modified%3A+2025-02-18T11%3A44%3A37.000Z%0A%0A%3C%2Fdetails%3E)
