# Topics API

Non-standard: This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

Warning: This feature is currently opposed by two browser vendors. See the [Standards positions](#standards_positions) section below for details.

Note: An [Enrollment process](/en-US/docs/Web/Privacy/Guides/Privacy_sandbox/Enrollment) is required to use the Topics API in your applications. See the [Enrollment](#enrollment) section for details of what sub-features are gated by enrollment.

The Topics API provides a mechanism for developers to implement use cases such as interest-based advertising (IBA) based on topics collected by the browser as the user navigates different pages, rather than collected by the developer by tracking the user's journey around different sites with [third-party cookies](/en-US/docs/Web/Privacy/Guides/Third-party_cookies).

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [HTML elements](#html_elements)
- [HTTP headers](#http_headers)
- [Enrollment](#enrollment)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

A typical mechanism for advertising on the web involves a user visiting publisher sites that use an advertising technology (ad tech) platform to publish ads for an advertiser's products or services. The publisher is paid to display the ads, which helps to fund their content, and more business is driven to advertiser sites.

The above process can be made more effective using interest-based advertising (IBA). The idea is that when users visit the publisher sites, they are served a personalized selection of ads based on their interests. Their interests are inferred from sites they have previously visited. In the past, third-party tracking cookies have been used to collect information on user interests, but browsers are phasing out the availability of third-party cookies for an increasing proportion of users. The Topics API provides part of the path towards this goal — a mechanism to implement IBA that does not depend on user tracking.

First of all, the browser infers a user's interests from the URLs of sites they visit that have ad tech `<iframe>`s embedded. These interests are mapped to specific topics of interest, and the browser calculates and records the users' top topic (i.e., the topic that their interests mapped to most often) at the end of each epoch. An epoch is a week by default. The top topic is updated each week so that interests are kept current and users don't start to see ads for topics that they are no longer interested in.

Note: This process only happens on sites where a Topics API feature is used (see [What API features enable the Topics API?](/en-US/docs/Web/API/Topics_API/Using#what_api_features_enable_the_topics_api)).

Once the browser has observed one or more topics for a user, the Topics API can retrieve them and send them to an ad tech platform. The platform can then use those topics to personalize the ads they serve to the user. The API helps to preserve privacy by only returning topics to an API caller that have been observed by them on pages visited by the current user.

See [Using the Topics API](/en-US/docs/Web/API/Topics_API/Using) for an explanation of how the API works.

### [What topics are there?](#what_topics_are_there)

The available top topics that the browser could calculate are stored in a publicly available [taxonomy of interests](https://github.com/patcg-individual-drafts/topics/blob/main/taxonomy_v2.md). The initial taxonomy has been proposed by Chrome, with the intention that it becomes a resource maintained by trusted ecosystem contributors. The taxonomy has been human-curated to exclude categories generally considered sensitive, such as ethnicity or sexual orientation.

## [Interfaces](#interfaces)

The Topics API has no distinct interfaces of its own.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[Document.browsingTopics()](/en-US/docs/Web/API/Document/browsingTopics)

Returns a promise that fulfills with an array of objects representing the top topics for the user, one from each of the last three epochs. By default, the method also causes the browser to record the current page visit as observed by the caller, so the page's hostname can later be used in topics calculation.

[fetch()](/en-US/docs/Web/API/Window/fetch) / [Request()](/en-US/docs/Web/API/Request/Request), the `browsingTopics` option

A boolean specifying that the selected topics for the current user should be sent in a [Sec-Browsing-Topics](/en-US/docs/Web/HTTP/Reference/Headers/Sec-Browsing-Topics) header with the associated request.

[HTMLIFrameElement.browsingTopics](/en-US/docs/Web/API/HTMLIFrameElement/browsingTopics)

A boolean property specifying that the selected topics for the current user should be sent with the request for the associated [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe)'s source. This reflects the `browsingtopics` content attribute value.

## [HTML elements](#html_elements)

[<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe), the `browsingtopics` attribute

A boolean attribute that, if present, specifies that the selected topics for the current user should be sent with the request for the [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe)'s source.

## [HTTP headers](#http_headers)

[Sec-Browsing-Topics](/en-US/docs/Web/HTTP/Reference/Headers/Sec-Browsing-Topics)

Sends the selected topics for the current user along with a request, which are used by an ad tech platform to choose a personalized ad to display.

[Observe-Browsing-Topics](/en-US/docs/Web/HTTP/Reference/Headers/Observe-Browsing-Topics)

Used to mark topics of interest inferred from a calling site's URL (i.e., the site where the ad tech `<iframe>` is embedded) as observed in the response to a request generated by a [feature that enables the Topics API](/en-US/docs/Web/API/Topics_API/Using#what_api_features_enable_the_topics_api). The browser will subsequently use those topics to calculate top topics for the current user for future epochs.

[Permissions-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy); the [browsing-topics](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/browsing-topics) directive

Controls access to the Topics API. Where a policy specifically disallows the use of the Topics API, any attempts to call the `Document.browsingTopics()` method or send a request with a `Sec-Browsing-Topics` header will fail with a `NotAllowedError`[DOMException](/en-US/docs/Web/API/DOMException).

## [Enrollment](#enrollment)

To use the Topics API in your sites, you must specify it in a [privacy sandbox enrollment process](/en-US/docs/Web/Privacy/Guides/Privacy_sandbox/Enrollment). If you don't do this, the following sub-features won't work:

- The promise returned by the [Document.browsingTopics()](/en-US/docs/Web/API/Document/browsingTopics) method will reject with a `NotAllowedError`[DOMException](/en-US/docs/Web/API/DOMException).
- Creating or modifying the [Sec-Browsing-Topics](/en-US/docs/Web/HTTP/Reference/Headers/Sec-Browsing-Topics) header will fail silently, and any existing `Sec-Browsing-Topics` header will be deleted.

## [Examples](#examples)

See [Using the Topics API](/en-US/docs/Web/API/Topics_API/Using) for code examples.

## [Specifications](#specifications)

This feature is not part of an official standard, although it is specified in the [Topics API Unofficial Proposal Draft](https://patcg-individual-drafts.github.io/topics/).

### [Standards positions](#standards_positions)

Two browser vendors [oppose](/en-US/docs/Glossary/Web_standards#opposing_standards) this specification. Known standards positions are as follows:

- Mozilla (Firefox): [Negative](https://mozilla.github.io/standards-positions/#topics)
- Apple (Safari): [Negative](https://webkit.org/standards-positions/#position-111)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Topics API](https://privacysandbox.google.com/private-advertising/topics) on privacysandbox.google.com (2023)
- [The Privacy Sandbox](https://privacysandbox.google.com/) on privacysandbox.google.com (2023)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Topics_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/topics_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTopics_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftopics_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTopics_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftopics_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe936e7271df947f25184a5ba8a21445bbd4d056c%0A*+Document+last+modified%3A+2025-12-13T02%3A55%3A18.000Z%0A%0A%3C%2Fdetails%3E)
