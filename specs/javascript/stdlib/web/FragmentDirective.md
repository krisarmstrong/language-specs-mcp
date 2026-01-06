# FragmentDirective

 Baseline  2025 Newly available

 Since ⁨March 2025⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFragmentDirective&level=low)

The `FragmentDirective` interface is an object exposed to allow code to check whether or not a browser supports [text fragments](/en-US/docs/Web/URI/Reference/Fragment/Text_fragments).

It is accessed via the [Document.fragmentDirective](/en-US/docs/Web/API/Document/fragmentDirective) property.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

None.

## [Instance methods](#instance_methods)

None.

## [Examples](#examples)

### [Checking if text fragments are supported](#checking_if_text_fragments_are_supported)

The code below logs whether or not text fragments are supported in your browser by checking that [Document.fragmentDirective](/en-US/docs/Web/API/Document/fragmentDirective) is defined. Note that the object is empty, and at present is mainly intended for feature detection. In the future, it might include other information.

```
<pre id="log"></pre>
```

```
const logElement = document.querySelector("#log");
function log(text) {
  logElement.innerText = text;
}
```

```
#log {
  height: 20px;
}
```

js

```
if (document.fragmentDirective) {
  log("Your browser supports text fragments.");
} else {
  log("Text fragments are not supported in your browser.");
}
```

## [Specifications](#specifications)

Specification
[URL Fragment Text Directives# fragmentdirective](https://wicg.github.io/scroll-to-text-fragment/#fragmentdirective)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [::target-text](/en-US/docs/Web/CSS/Reference/Selectors/::target-text)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 18, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/FragmentDirective/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/fragmentdirective/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFragmentDirective&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffragmentdirective%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFragmentDirective%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffragmentdirective%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4d9320f9857fb80fef5f3fe78e3d09b06eb0ebbd%0A*+Document+last+modified%3A+2025-02-18T11%3A44%3A37.000Z%0A%0A%3C%2Fdetails%3E)
