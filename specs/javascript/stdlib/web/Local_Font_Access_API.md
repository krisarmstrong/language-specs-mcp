# Local Font Access API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FLocal_Font_Access_API&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The Local Font Access API provides a mechanism to access the user's locally installed font data — this includes higher-level details such as names, styles, and families, as well as the raw bytes of the underlying font files.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Extensions to other interfaces](#extensions_to_other_interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

[Web fonts](/en-US/docs/Learn_web_development/Core/Text_styling/Web_fonts) were revolutionary in enabling typography on the web by allowing web designers to provide custom fonts to use on a web document. Specified via the [@font-face](/en-US/docs/Web/CSS/Reference/At-rules/@font-face) at-rule, a web font can be loaded from a URL provided in the `url()` function.

`@font-face` has several other useful features available. In particular, you can also specify the font's full or Postscript name inside the `local()` function to tell the browser to use a local copy if the user has the font installed on their computer. This is not without its problems — `local()` has become notorious as a [fingerprinting vector](https://developer.chrome.com/docs/capabilities/web-apis/local-fonts#local_fonts_as_fingerprint_vector).

In addition, high-end design tools have historically been difficult to deliver on the web, due to challenges in accurate font enumeration and accessing low-level font data (for example, to apply filters and transformations). Current apps often rely on workarounds such as asking users to upload their fonts to a server where they are processed to get raw byte data, or installing a separate local program to provide additional capabilities.

The Local Font Access API has been created to address these problems.

The [Window.queryLocalFonts()](/en-US/docs/Web/API/Window/queryLocalFonts) method provides access to an array of locally-installed fonts, each represented by a [FontData](/en-US/docs/Web/API/FontData) object instance. [FontData](/en-US/docs/Web/API/FontData) has several properties providing access to names, styles, and families, and it also has a [blob()](/en-US/docs/Web/API/FontData/blob) method providing access to a [Blob](/en-US/docs/Web/API/Blob) containing the raw bytes of the underlying font file.

In terms of privacy and security:

- The Local Font Access API is designed to only provide access to the data required to solve the above problems. There is also no requirement for browsers to provide the full list of available local fonts, nor to provide the data in the same order as it appears on disk.
- When [Window.queryLocalFonts()](/en-US/docs/Web/API/Window/queryLocalFonts) is invoked, the user is asked for permission to access their local fonts. The status of this permission can be queried via the [Permissions API](/en-US/docs/Web/API/Permissions_API) (the `local-fonts` permission).
- You can control access to this feature using a [local-fonts](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/local-fonts)[Permissions Policy](/en-US/docs/Web/HTTP/Guides/Permissions_Policy).

## [Interfaces](#interfaces)

[FontData](/en-US/docs/Web/API/FontData)

Represents a single local font face.

## [Extensions to other interfaces](#extensions_to_other_interfaces)

[Window.queryLocalFonts()](/en-US/docs/Web/API/Window/queryLocalFonts)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with an array of [FontData](/en-US/docs/Web/API/FontData) objects representing the font faces available locally.

## [Examples](#examples)

For a working live demo, see our [Local Font Access API demo](https://mdn.github.io/dom-examples/local-font-access/).

### [Feature detection](#feature_detection)

js

```
if ("queryLocalFonts" in window) {
  // The Local Font Access API is supported
}
```

### [Font enumeration](#font_enumeration)

The following snippet will query for all available fonts, and log metadata. This could be used, for example, to populate a font-picker control.

js

```
async function logFontData() {
  try {
    const availableFonts = await window.queryLocalFonts();
    for (const fontData of availableFonts) {
      console.log(fontData.postscriptName);
      console.log(fontData.fullName);
      console.log(fontData.family);
      console.log(fontData.style);
    }
  } catch (err) {
    console.error(err.name, err.message);
  }
}
```

### [Accessing low-level data](#accessing_low-level_data)

The [blob()](/en-US/docs/Web/API/FontData/blob) method provides access to low-level [SFNT](https://en.wikipedia.org/wiki/SFNT) data — this is a font file format that can contain other font formats, such as PostScript, TrueType, OpenType, or Web Open Font Format (WOFF).

js

```
async function computeOutlineFormat() {
  try {
    const availableFonts = await window.queryLocalFonts({
      postscriptNames: ["ComicSansMS"],
    });
    for (const fontData of availableFonts) {
      // `blob()` returns a Blob containing valid and complete
      // SFNT-wrapped font data.
      const sfnt = await fontData.blob();
      // Slice out only the bytes we need: the first 4 bytes are the SFNT
      // version info.
      // Spec: https://learn.microsoft.com/en-us/typography/opentype/spec/otff#organization-of-an-opentype-font
      const sfntVersion = await sfnt.slice(0, 4).text();

      let outlineFormat = "UNKNOWN";
      switch (sfntVersion) {
        case "\x00\x01\x00\x00":
        case "true":
        case "typ1":
          outlineFormat = "truetype";
          break;
        case "OTTO":
          outlineFormat = "cff";
          break;
      }
      console.log("Outline format:", outlineFormat);
    }
  } catch (err) {
    console.error(err.name, err.message);
  }
}
```

## [Specifications](#specifications)

Specification[Local Font Access API](https://wicg.github.io/local-font-access/)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Use advanced typography with local fonts](https://developer.chrome.com/docs/capabilities/web-apis/local-fonts)
- [@font-face](/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
- The [local-fonts](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/local-fonts)[Permissions Policy](/en-US/docs/Web/HTTP/Guides/Permissions_Policy) directive

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 4, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Local_Font_Access_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/local_font_access_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FLocal_Font_Access_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Flocal_font_access_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FLocal_Font_Access_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Flocal_font_access_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6855bf0bdd644345f66b88b477fd219a5e7f866e%0A*+Document+last+modified%3A+2025-07-04T16%3A12%3A11.000Z%0A%0A%3C%2Fdetails%3E)
