# ProcessingInstruction

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FProcessingInstruction&level=high)

The `ProcessingInstruction` interface represents a [processing instruction](https://www.w3.org/TR/xml/#sec-pi); that is, a [Node](/en-US/docs/Web/API/Node) which embeds an instruction targeting a specific application but that can be ignored by any other applications which don't recognize the instruction.

Warning:`ProcessingInstruction` nodes are only supported in XML documents, not in HTML documents. In these, a process instruction will be considered as a comment and be represented as a [Comment](/en-US/docs/Web/API/Comment) object in the tree.

A processing instruction may be different than the [XML declaration](/en-US/docs/Web/XML/Guides/XML_introduction#xml_declaration).

Note: User-defined processing instructions cannot begin with `"xml"`, as `xml`-prefixed processing-instruction target names are reserved by the XML specification for particular, standard uses (see, for example, `<?xml-stylesheet ?>`.

For example:

html

```
<?xml version="1.0"?>
```

is a processing instruction whose `target` is `xml`.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent interfaces, [CharacterData](/en-US/docs/Web/API/CharacterData), [Node](/en-US/docs/Web/API/Node), and [EventTarget](/en-US/docs/Web/API/EventTarget).

[ProcessingInstruction.sheet](/en-US/docs/Web/API/ProcessingInstruction/sheet)Read only

Returns the associated [StyleSheet](/en-US/docs/Web/API/StyleSheet) object, if any; or `null` if none.

[ProcessingInstruction.target](/en-US/docs/Web/API/ProcessingInstruction/target)Read only

A name identifying the application to which the instruction is targeted.

## [Instance methods](#instance_methods)

This interface doesn't have any specific method, but inherits methods from its parent interfaces, [CharacterData](/en-US/docs/Web/API/CharacterData), [Node](/en-US/docs/Web/API/Node), and [EventTarget](/en-US/docs/Web/API/EventTarget).

## [Specifications](#specifications)

Specification
[DOM# interface-processinginstruction](https://dom.spec.whatwg.org/#interface-processinginstruction)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [document.createProcessingInstruction()](/en-US/docs/Web/API/Document/createProcessingInstruction)
- The [DOM API](/en-US/docs/Web/API/Document_Object_Model)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 24, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ProcessingInstruction/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/processinginstruction/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FProcessingInstruction&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fprocessinginstruction%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FProcessingInstruction%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fprocessinginstruction%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa84b606ffd77c40a7306be6c932a74ab9ce6ab96%0A*+Document+last+modified%3A+2025-06-24T06%3A12%3A11.000Z%0A%0A%3C%2Fdetails%3E)
