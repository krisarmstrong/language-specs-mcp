# FontData

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFontData&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `FontData` interface of the [Local Font Access API](/en-US/docs/Web/API/Local_Font_Access_API) represents a single local font face.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[FontData.family](/en-US/docs/Web/API/FontData/family)Read onlyExperimental

Returns the family of the font face.

[FontData.fullName](/en-US/docs/Web/API/FontData/fullName)Read onlyExperimental

Returns the full name of the font face.

[FontData.postscriptName](/en-US/docs/Web/API/FontData/postscriptName)Read onlyExperimental

Returns the PostScript name of the font face.

[FontData.style](/en-US/docs/Web/API/FontData/style)Read onlyExperimental

Returns the style of the font face.

## [Instance methods](#instance_methods)

[FontData.blob()](/en-US/docs/Web/API/FontData/blob)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with a [Blob](/en-US/docs/Web/API/Blob) containing the raw bytes of the underlying font file.

## [Examples](#examples)

For a live example, see our [Local Font Access API demo](https://mdn.github.io/dom-examples/local-font-access/).

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

Specification
[Local Font Access API# fontdata-interface](https://wicg.github.io/local-font-access/#fontdata-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Use advanced typography with local fonts](https://developer.chrome.com/docs/capabilities/web-apis/local-fonts)
- [@font-face](/en-US/docs/Web/CSS/Reference/At-rules/@font-face)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 4, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/FontData/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/fontdata/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFontData&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffontdata%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFontData%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffontdata%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6855bf0bdd644345f66b88b477fd219a5e7f866e%0A*+Document+last+modified%3A+2025-07-04T16%3A12%3A11.000Z%0A%0A%3C%2Fdetails%3E)
