# CDATASection

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCDATASection&level=high)

The `CDATASection` interface represents a CDATA section that can be used within XML to include extended portions of unescaped text. When inside a CDATA section, the symbols `<` and `&` don't need escaping as they normally do.

In XML, a CDATA section looks like:

xml

```
<![CDATA[ … ]]>
```

For example:

xml

```
<foo>
  Here is a CDATA section: <![CDATA[ < > & ]]> with all kinds of unescaped text.
</foo>
```

The only sequence which is not allowed within a CDATA section is the closing sequence of a CDATA section itself, `]]>`.

Note: CDATA sections should not be used within HTML. They are considered comments and are not displayed.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface has no specific properties and implements those of its parent [Text](/en-US/docs/Web/API/Text).

## [Instance methods](#instance_methods)

This interface has no specific methods and implements those of its parent [Text](/en-US/docs/Web/API/Text).

## [Specifications](#specifications)

Specification
[DOM# interface-cdatasection](https://dom.spec.whatwg.org/#interface-cdatasection)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Document.createCDATASection()](/en-US/docs/Web/API/Document/createCDATASection)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jan 21, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CDATASection/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cdatasection/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCDATASection&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcdatasection%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCDATASection%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcdatasection%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F327710f973e1d6d1cad19faac9a95134c6027d08%0A*+Document+last+modified%3A+2025-01-21T01%3A16%3A46.000Z%0A%0A%3C%2Fdetails%3E)
