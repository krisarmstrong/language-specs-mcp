# OTPCredential

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FOTPCredential&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `OTPCredential` interface of the [WebOTP API](/en-US/docs/Web/API/WebOTP_API) is returned when a WebOTP [navigator.credentials.get()](/en-US/docs/Web/API/CredentialsContainer/get) call (i.e., invoked with an `otp` option) fulfills. It includes a `code` property that contains the retrieved one-time password (OTP).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

This interface also inherits properties from [Credential](/en-US/docs/Web/API/Credential).

[OTPCredential.code](/en-US/docs/Web/API/OTPCredential/code)Read onlyExperimental

The one-time password (OTP).

## [Instance methods](#instance_methods)

None.

## [Examples](#examples)

The below code triggers the browser's permission flow when an SMS message arrives. If permission is granted, then the promise resolves with an `OTPCredential` object. The contained `code` value is then set as the value of an [<input>](/en-US/docs/Web/HTML/Reference/Elements/input) form element, which is then submitted.

js

```
navigator.credentials
  .get({
    otp: { transport: ["sms"] },
    signal: ac.signal,
  })
  .then((otp) => {
    input.value = otp.code;
    if (form) form.submit();
  })
  .catch((err) => {
    console.error(err);
  });
```

Note: For a full explanation of the code, see the [WebOTP API](/en-US/docs/Web/API/WebOTP_API) landing page. You can also [see this code as part of a full working demo](https://chrome.dev/web-otp-demo/).

## [Specifications](#specifications)

Specification
[WebOTP API# OTPCredential](https://wicg.github.io/web-otp/#OTPCredential)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/OTPCredential/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/otpcredential/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FOTPCredential&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fotpcredential%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FOTPCredential%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fotpcredential%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F90eafc463fe122c86a64836f4f3953a0bee85be9%0A*+Document+last+modified%3A+2025-07-07T16%3A29%3A09.000Z%0A%0A%3C%2Fdetails%3E)
