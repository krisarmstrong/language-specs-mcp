# NDEFReader

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNDEFReader&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `NDEFReader` interface of the [Web NFC API](/en-US/docs/Web/API/Web_NFC_API) is used to read from and write data to compatible NFC devices, e.g., NFC tags supporting NDEF, when these devices are within the reader's magnetic induction field.

## In this article

- [Constructor](#constructor)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[NDEFReader()](/en-US/docs/Web/API/NDEFReader/NDEFReader)Experimental

Returns a new `NDEFReader` object.

## [Instance methods](#instance_methods)

The `NDEFReader` interface inherits the methods of [EventTarget](/en-US/docs/Web/API/EventTarget), its parent interface.

[NDEFReader.scan()](/en-US/docs/Web/API/NDEFReader/scan)Experimental

Activates a reading device and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that either resolves when an NFC tag read operation is scheduled or rejects if a hardware or permission error is encountered. This method triggers a permission prompt if the "nfc" permission has not been previously granted.

[NDEFReader.write()](/en-US/docs/Web/API/NDEFReader/write)Experimental

Attempts to write an NDEF message to a tag and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that either resolves when a message has been written to the tag or rejects if a hardware or permission error is encountered. This method triggers a permission prompt if the "nfc" permission has not been previously granted.

## [Events](#events)

Inherits events from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[reading](/en-US/docs/Web/API/NDEFReader/reading_event)Experimental

Fires when a new reading is available from compatible NFC devices.

[readingerror](/en-US/docs/Web/API/NDEFReader/readingerror_event)Experimental

Fires when a tag is in proximity of a reading device, but cannot be read.

## [Examples](#examples)

### [Handling initial reads while writing](#handling_initial_reads_while_writing)

The example below shows how to coordinate between a common reading handler and one used specifically for a single write. In order to write, a tag needs to be found and read. This gives you the ability to check whether it is actually a tag that you want to write to. That's why it's recommended that you call `write()` from a reading event.

js

```
const ndef = new NDEFReader();
let ignoreRead = false;

ndef.onreading = (event) => {
  if (ignoreRead) {
    return; // write pending, ignore read.
  }

  console.log("We read a tag, but not during pending write!");
};

function write(data) {
  ignoreRead = true;
  return new Promise((resolve, reject) => {
    ndef.addEventListener(
      "reading",
      (event) => {
        // Check if we want to write to this tag, or reject.
        ndef
          .write(data)
          .then(resolve, reject)
          .finally(() => (ignoreRead = false));
      },
      { once: true },
    );
  });
}

await ndef.scan();
try {
  await write("Hello World");
  console.log("We wrote to a tag!");
} catch (err) {
  console.error("Something went wrong", err);
}
```

## [Specifications](#specifications)

Specification
[Web NFC# the-ndefreader-object](https://w3c.github.io/web-nfc/#the-ndefreader-object)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/NDEFReader/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/ndefreader/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNDEFReader&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fndefreader%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNDEFReader%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fndefreader%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F702cd9e4d2834e13aea345943efc8d0c03d92ec9%0A*+Document+last+modified%3A+2025-04-03T04%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
