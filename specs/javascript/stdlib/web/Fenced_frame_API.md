# Fenced Frame API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFenced_frame_API&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Warning: This feature is currently opposed by one browser vendor. See the [Standards positions](#standards_positions) section below for details.

The Fenced Frame API provides functionality for controlling content embedded in [<fencedframe>](/en-US/docs/Web/HTML/Reference/Elements/fencedframe) elements.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [How do <fencedframe>s work?](#how_do_fencedframes_work)
- [Interfaces](#interfaces)
- [Enrollment and local testing](#enrollment_and_local_testing)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

One major source of [privacy](/en-US/docs/Web/Privacy) and [security](/en-US/docs/Web/Security) problems on the web is content embedded in [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe) elements. Historically `<iframe>`s have been used to set third-party cookies, which can be used to share information and track users across sites. In addition, content embedded in an `<iframe>` can communicate with its embedding document (for example, using [Window.postMessage()](/en-US/docs/Web/API/Window/postMessage)).

The embedding document can also use scripting to read various forms of information from the `<iframe>` — for example you can potentially get significant tracking/fingerprinting data from reading the embedded URL from the `src` property, especially if it contains [URL parameters](/en-US/docs/Web/URI/Reference/Query). The `<iframe>` can also access the embedding context's DOM, and vice versa.

Most modern browsers are working on mechanisms to partition storage so that cookie data can no longer be used for tracking (for example see [Cookies Having Independent Partitioned State (CHIPS)](/en-US/docs/Web/Privacy/Guides/Privacy_sandbox/Partitioned_cookies) or [Firefox State Partitioning](/en-US/docs/Web/Privacy/Guides/State_Partitioning)).

`<fencedframe>` elements aim to solve another piece of this puzzle — they are very similar to `<iframe>`s in form and function, except that:

- Communication cannot be shared between the `<fencedframe>` content and its embedding site.
- A `<fencedframe>` can access cross-site data, but only in a very specific set of controlled circumstances that preserve user privacy.
- A `<fencedframe>` cannot be freely manipulated or have its data accessed via regular scripting (for example reading or setting the source URL). `<fencedframe>` content can only be embedded via [specific APIs](#use_cases).
- A `<fencedframe>` cannot access the embedding context's DOM, nor can the embedding context access the `<fencedframe>`'s DOM.

For more information about the communication model of fenced frames, read the [communication with embedded frames](/en-US/docs/Web/API/Fenced_frame_API/Communication_with_embedded_frames) guide.

### [Use cases](#use_cases)

`<fencedframe>`s are used by other APIs to embed different types of cross-site content or collect data, fulfilling different use cases in a privacy-preserving manner. Most of these previously relied on third-party cookies or other mechanisms that were bad for privacy.

- The [Shared Storage API](https://privacysandbox.google.com/private-advertising/shared-storage) provides access to unpartitioned cross-site data in a secure environment, calculating and/or displaying results in a `<fencedframe>`. For example: 

  - Advertisers can measure the reach of an ad, or serve subsequent ads based on which ones users have already seen on other sites.
  - Developers can do A/B testing, showing variants to a user based on a group they are assigned to, or based on how many users have seen each one already.
  - Businesses can customize the user's experience based on what they have seen on other sites. For example, if they have already purchased membership, you might not want to show them membership sign-up ads across your other properties.

- The [Protected Audience API](https://privacysandbox.google.com/private-advertising/protected-audience) allows developers to implement interest group-based advertising, namely remarketing and custom audience use cases. It can evaluate multiple bids for ad space and display the winning ad in a `<fencedframe>`.
- The [Private Aggregation API](https://privacysandbox.google.com/private-advertising/private-aggregation) can gather data from `<fencedframe>`s (originating from shared storage or the Protected Audience API) and create aggregated reports.

## [How do <fencedframe>s work?](#how_do_fencedframes_work)

As mentioned above, you don't control the content embedded in a [<fencedframe>](/en-US/docs/Web/HTML/Reference/Elements/fencedframe) directly via regular script.

To set what content will be shown in a `<fencedframe>`, a utilizing API (such as [Protected Audience](https://privacysandbox.google.com/private-advertising/protected-audience) or [Shared Storage](https://privacysandbox.google.com/private-advertising/shared-storage)) generates a [FencedFrameConfig](/en-US/docs/Web/API/FencedFrameConfig) object, which is then set via JavaScript as the value of the `<fencedframe>`'s [HTMLFencedFrameElement.config](/en-US/docs/Web/API/HTMLFencedFrameElement/config) property.

The following example gets a `FencedFrameConfig` from a Protected Audience API's ad auction, which is then used to display the winning ad in a `<fencedframe>`:

js

```
const frameConfig = await navigator.runAdAuction({
  // … auction configuration
  resolveToConfig: true,
});

const frame = document.createElement("fencedframe");
frame.config = frameConfig;
```

`resolveToConfig: true` must be passed in to the `runAdAuction()` call to obtain a `FencedFrameConfig` object. If `resolveToConfig` is set to `false`, the resulting [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) will resolve to an opaque [URN](/en-US/docs/Web/URI/Reference/Schemes/urn) (for example `urn:uuid:c36973b5-e5d9-de59-e4c4-364f137b3c7a`) that can only be used in an `<iframe>`.

Either way, the browser stores a URL containing the target location of the content to embed — mapped to the opaque URN, or the `FencedFrameConfig`'s internal `url` property. The URL value cannot be read by JavaScript running in the embedding context.

Note: Support is provided for opaque URNs in `<iframe>`s to ease migration of existing implementations over to [privacy sandbox](https://privacysandbox.google.com/) APIs. This support is intended to be temporary and will be removed in the future as adoption grows.

Note:`FencedFrameConfig` has a [setSharedStorageContext()](/en-US/docs/Web/API/FencedFrameConfig/setSharedStorageContext) method that is used to pass in data from the embedding document to the `<fencedframe>`'s shared storage. It could for example be accessed in a [Worklet](/en-US/docs/Web/API/Worklet) via the `<fencedframe>` and used to generate a report. See the [Shared Storage API](https://privacysandbox.google.com/private-advertising/shared-storage) for more details.

### [Accessing fenced frame functionality on the Fence object](#accessing_fenced_frame_functionality_on_the_fence_object)

Inside documents embedded in `<fencedframe>`s, JavaScript has access to a [Window.fence](/en-US/docs/Web/API/Window/fence) property that returns a [Fence](/en-US/docs/Web/API/Fence) instance for that document. This object contains several functions specifically relevant to fenced frame API functionality. For example, [Fence.reportEvent()](/en-US/docs/Web/API/Fence/reportEvent) provides a way to trigger the submission of report data via a [beacon](/en-US/docs/Web/API/Beacon_API) to one or more specified URLs, in order to report ad views and clicks.

### [Permissions policy](#permissions_policy)

Only specific features designed to be used in `<fencedframe>`s can be enabled via permissions policies set on them; other policy-controlled features are not available in this context. See [Permissions policies available to fenced frames](/en-US/docs/Web/HTML/Reference/Elements/fencedframe#permissions_policies_available_to_fenced_frames) for more details.

### [HTTP headers](#http_headers)

A [Sec-Fetch-Dest](/en-US/docs/Web/HTTP/Reference/Headers/Sec-Fetch-Dest) header with a value of `fencedframe` will be set for any requests made from inside a `<fencedframe>`, including child `<iframe>`s embedded within a `<fencedframe>`.

http

```
Sec-Fetch-Dest: fencedframe
```

The server must set a [Supports-Loading-Mode](/en-US/docs/Web/HTTP/Reference/Headers/Supports-Loading-Mode) response header with a value of `fenced-frame` for any document intended to be loaded into a `<fencedframe>`, or `<iframe>` embedded within a `<fencedframe>`.

http

```
Supports-Loading-Mode: fenced-frame
```

Other effects of fenced frames on HTTP headers are as follows:

- [User-agent client hints](/en-US/docs/Web/HTTP/Guides/Client_hints#user_agent_client_hints) are not available inside fenced frames because they rely on [permissions policy](/en-US/docs/Web/HTTP/Guides/Permissions_Policy) delegation, which could be used to leak data.
- Strict [Cross-Origin-Opener-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Opener-Policy) settings are enforced on new browsing contexts opened from inside fenced frames, otherwise they could be used to leak information to other origins. Any new window opened from inside a fenced frame will have [rel="noopener"](/en-US/docs/Web/HTML/Reference/Attributes/rel/noopener) and `Cross-Origin-Opener-Policy: same-origin` set to ensure that [Window.opener](/en-US/docs/Web/API/Window/opener) returns `null` and place it in its own browsing context group.
- [Content-Security-Policy: fenced-frame-src](/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/fenced-frame-src) has been added for specifying valid sources for nested browsing contexts loaded into `<fencedframe>` elements.
- [Content-Security-Policy: sandbox](/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/sandbox) custom settings cannot be inherited by fenced frames, to mitigate privacy issues. For a fenced frame to load, you need to specify no `sandbox` CSP (which implies the below values), or specify the following sandbox values: 

  - `allow-same-origin`
  - `allow-forms`
  - `allow-scripts`
  - `allow-popups`
  - `allow-popups-to-escape-sandbox`
  - `allow-top-navigation-by-user-activation`

### [beforeunload and unload events](#beforeunload_and_unload_events)

[beforeunload](/en-US/docs/Web/API/Window/beforeunload_event) and [unload](/en-US/docs/Web/API/Window/unload_event) events do not fire on fenced frames, because they can leak information in the form of a page deletion timestamp. Implementations aim to eliminate as many potential leakages as possible.

## [Interfaces](#interfaces)

[FencedFrameConfig](/en-US/docs/Web/API/FencedFrameConfig)

Represents the navigation of a [<fencedframe>](/en-US/docs/Web/HTML/Reference/Elements/fencedframe), i.e., what content will be displayed in it. A `FencedFrameConfig` is returned from a source such as the [Protected Audience API](https://privacysandbox.google.com/private-advertising/protected-audience) and set as the value of [HTMLFencedFrameElement.config](/en-US/docs/Web/API/HTMLFencedFrameElement/config).

[Fence](/en-US/docs/Web/API/Fence)

Contains several functions relevant to fenced frame functionality. Available only to documents embedded inside a `<fencedframe>`.

[HTMLFencedFrameElement](/en-US/docs/Web/API/HTMLFencedFrameElement)

Represents a `<fencedframe>` element in JavaScript and provides properties to configure it.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[Navigator.deprecatedReplaceInURN()](/en-US/docs/Web/API/Navigator/deprecatedReplaceInURN)

Substitutes specified strings inside the mapped URL corresponding to a given opaque URN or `FencedFrameConfig`'s internal `url` property.

[Window.fence](/en-US/docs/Web/API/Window/fence)

Returns a [Fence](/en-US/docs/Web/API/Fence) object instance for the current document context. Available only to documents embedded inside a `<fencedframe>`.

## [Enrollment and local testing](#enrollment_and_local_testing)

Certain API features that create [FencedFrameConfig](/en-US/docs/Web/API/FencedFrameConfig)s such as `Navigator.runAdAuction()` ([Protected Audience API](https://privacysandbox.google.com/private-advertising/protected-audience)) and [WindowSharedStorage.selectURL()](/en-US/docs/Web/API/WindowSharedStorage/selectURL) ([Shared Storage API](/en-US/docs/Web/API/Shared_Storage_API)), as well as other features such as [Fence.reportEvent()](/en-US/docs/Web/API/Fence/reportEvent), require you to enroll your site in a [privacy sandbox enrollment process](/en-US/docs/Web/Privacy/Guides/Privacy_sandbox/Enrollment). If you don't do this, the API calls will fail with a console warning.

Note: In Chrome, you can still test your fenced frame code locally without enrollment. To allow local testing, enable the following Chrome developer flag:

`chrome://flags/#privacy-sandbox-enrollment-overrides`

## [Examples](#examples)

The following demos all make use of `<fencedframe>`s:

- [Shared Storage API demos](https://shared-storage-demo.web.app/) (which also includes some Private Aggregation API examples)
- [Protected Audience API demo](https://protected-audience-demo-advertiser.web.app/)

## [Specifications](#specifications)

Specification
[Fenced Frame# the-fencedframe-element](https://wicg.github.io/fenced-frame/#the-fencedframe-element)

### [Standards positions](#standards_positions)

One browser vendor [opposes](/en-US/docs/Glossary/Web_standards#opposing_standards) this specification. Known standards positions are as follows:

- Mozilla (Firefox): [Negative](https://github.com/mozilla/standards-positions/issues/781)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Fenced frames](https://privacysandbox.google.com/private-advertising/fenced-frame) on privacysandbox.google.com
- [The Privacy Sandbox](https://privacysandbox.google.com/) on privacysandbox.google.com

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 24, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Fenced_frame_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/fenced_frame_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFenced_frame_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffenced_frame_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFenced_frame_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffenced_frame_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa84b606ffd77c40a7306be6c932a74ab9ce6ab96%0A*+Document+last+modified%3A+2025-06-24T06%3A12%3A11.000Z%0A%0A%3C%2Fdetails%3E)
