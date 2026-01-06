# MediaKeys

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2019⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaKeys&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `MediaKeys` interface of [Encrypted Media Extensions API](/en-US/docs/Web/API/Encrypted_Media_Extensions_API) represents a set of keys that an associated [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement) can use for decryption of media data during playback.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

None.

## [Instance methods](#instance_methods)

[MediaKeys.createSession()](/en-US/docs/Web/API/MediaKeys/createSession)

Returns a new [MediaKeySession](/en-US/docs/Web/API/MediaKeySession) object, which represents a context for message exchange with a content decryption module (CDM).

[MediaKeys.getStatusForPolicy()](/en-US/docs/Web/API/MediaKeys/getStatusForPolicy)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to a status string indicating whether the CDM would allow the presentation of encrypted media data using the keys, based on specified policy requirements.

[MediaKeys.setServerCertificate()](/en-US/docs/Web/API/MediaKeys/setServerCertificate)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) to a server certificate to be used to encrypt messages to the license server.

## [Examples](#examples)

### [Check if keys are usable with HDCP restriction](#check_if_keys_are_usable_with_hdcp_restriction)

This example shows how `getStatusForPolicy()` can be used to check if keys can decrypt a particular video format in a setup that has a minimum HDCP version of `2.2`. For more information, see the [MediaKeys: getStatusForPolicy() method](/en-US/docs/Web/API/MediaKeys/getStatusForPolicy) documentation.

#### HTML

html

```
<pre id="log"></pre>
```

```
#log {
  height: 100px;
  overflow: scroll;
  padding: 0.5rem;
  border: 1px solid black;
}
```

#### JavaScript

```
const logElement = document.querySelector("#log");
function log(text) {
  logElement.innerText = `${logElement.innerText}${text}\n`;
  logElement.scrollTop = logElement.scrollHeight;
}
```

js

```
const config = [
  {
    videoCapabilities: [
      {
        contentType: 'video/mp4; codecs="avc1.640028"',
        encryptionScheme: "cenc",
        robustness: "SW_SECURE_DECODE", // Widevine L3
      },
    ],
  },
];

getMediaStatus(config);

async function getMediaStatus(config) {
  try {
    const mediaKeySystemAccess = await navigator.requestMediaKeySystemAccess(
      "com.widevine.alpha",
      config,
    );
    const mediaKeys = await mediaKeySystemAccess.createMediaKeys();
    const mediaStatus = await mediaKeys.getStatusForPolicy({
      minHdcpVersion: "2.2",
    });
    log(mediaStatus);

    // Get the content or fallback to an alternative if the
    // keys are not usable
    if (mediaStatus === "usable") {
      console.log("HDCP 2.2 can be enforced.");
      // Fetch the high resolution protected content
    } else {
      log("HDCP 2.2 cannot be enforced");
      // Fallback other content, get license, etc.
    }
  } catch (error) {
    log(error);
  }
}
```

#### Results

## [Specifications](#specifications)

Specification
[Encrypted Media Extensions# mediakeys-interface](https://w3c.github.io/encrypted-media/#mediakeys-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 23, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/MediaKeys/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mediakeys/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaKeys&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmediakeys%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaKeys%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmediakeys%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0a9c10fc67901972221dc7b3d006334fbfa73dce%0A*+Document+last+modified%3A+2024-09-23T14%3A02%3A45.000Z%0A%0A%3C%2Fdetails%3E)
