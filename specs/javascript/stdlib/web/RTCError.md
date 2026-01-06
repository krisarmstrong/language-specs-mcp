# RTCError

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCError&level=not)

The `RTCError` interface describes an error which has occurred while handling [WebRTC](/en-US/docs/Web/API/WebRTC_API) operations. It's based upon the standard [DOMException](/en-US/docs/Web/API/DOMException) interface that describes general DOM errors.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

`RTCError()`

Creates and returns a new `RTCError` object initialized with the different parameters and, optionally, a string to use as the value of the error's [message](/en-US/docs/Web/API/DOMException/message) property.

## [Instance properties](#instance_properties)

In addition to the properties defined by the parent interface, [DOMException](/en-US/docs/Web/API/DOMException), `RTCError` includes the following properties:

[errorDetail](/en-US/docs/Web/API/RTCError/errorDetail)Read only

A string specifying the WebRTC-specific error code identifying the type of error that occurred.

[receivedAlert](/en-US/docs/Web/API/RTCError/receivedAlert)Read only

An unsigned long integer value indicating the fatal [DTLS](/en-US/docs/Glossary/DTLS) error which was received from the network. Only valid if the `errorDetail` string is `dtls-failure`. If `null`, no DTLS error was received.

[sctpCauseCode](/en-US/docs/Web/API/RTCError/sctpCauseCode)Read only

If `errorDetail` is `sctp-failure`, this property is a long integer specifying the [SCTP](/en-US/docs/Glossary/SCTP) cause code indicating the cause of the failed SCTP negotiation. `null` if the error isn't an SCTP error.

[sdpLineNumber](/en-US/docs/Web/API/RTCError/sdpLineNumber)Read only

If `errorDetail` is `sdp-syntax-error`, this property is a long integer identifying the line number of the [SDP](/en-US/docs/Glossary/SDP) on which the syntax error occurred. `null` if the error isn't an SDP syntax error.

[sentAlert](/en-US/docs/Web/API/RTCError/sentAlert)Read only

If `errorDetail` is `dtls-failure`, this property is an unsigned long integer indicating the fatal DTLS error that was sent out by this device. If `null`, no DTLS error was transmitted.

Note: All `RTCError` objects have their [name](/en-US/docs/Web/API/DOMException/name) set to `OperationError`.

## [Examples](#examples)

In this example, a handler is established for an [RTCDataChannel](/en-US/docs/Web/API/RTCDataChannel)'s [error](/en-US/docs/Web/API/RTCDataChannel/error_event) event.

js

```
dataChannel.addEventListener("error", (event) => {
  let error = event.error; // event.error is an RTCError

  if (error.errorDetail === "sdp-syntax-error") {
    let errLine = error.sdpLineNumber;
    let errMessage = error.message;

    let alertMessage = `A syntax error occurred interpreting line ${errLine} of the SDP: ${errMessage}`;
    showMyAlertMessage("Data Channel Error", alertMessage);
  } else {
    terminateMyConnection();
  }
});
```

If the error is an SDP syntax error—indicated by its [errorDetail](/en-US/docs/Web/API/RTCError/errorDetail) property being `sdp-syntax-error`—, a message string is constructed to present the error message and the line number within the SDP at which the error occurred. This message is then displayed using a function called `showMyAlertMessage()`, which stands in for whatever output mechanism this code might use.

Any other error is treated as terminal, causing a `terminateMyConnection()` function to be called.

The above example uses [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) to add the handler for `error` events. You can also use the `RTCDataChannel` object's [onerror](/en-US/docs/Web/API/RTCDataChannel/error_event) event handler property, like this:

js

```
dataChannel.onerror = (event) => {
  let error = event.error;

  /* and so forth */
};
```

## [Specifications](#specifications)

Specification
[WebRTC: Real-Time Communication in Browsers# dom-rtcerror](https://w3c.github.io/webrtc-pc/#dom-rtcerror)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 6, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/RTCError/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcerror/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCError&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcerror%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCError%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcerror%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F11f58a4cd8758f89056900a6fb7c21e2d42fa6f1%0A*+Document+last+modified%3A+2024-08-06T16%3A16%3A02.000Z%0A%0A%3C%2Fdetails%3E)
