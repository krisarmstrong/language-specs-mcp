# FeaturePolicy

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `FeaturePolicy` interface represents the set of [Permissions Policies](/en-US/docs/Web/HTTP/Guides/Permissions_Policy) applied to the current execution context.

## In this article

- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

[FeaturePolicy.allowsFeature](/en-US/docs/Web/API/FeaturePolicy/allowsFeature)Experimental

Returns a Boolean that indicates whether or not a particular feature is enabled in the specified context.

[FeaturePolicy.features](/en-US/docs/Web/API/FeaturePolicy/features)Experimental

Returns a list of names of all features supported by the User Agent. Features whose names appear on the list might not be allowed by the Permissions Policy of the current execution context and/or might be restricted by user-granted permissions.

[FeaturePolicy.allowedFeatures](/en-US/docs/Web/API/FeaturePolicy/allowedFeatures)Experimental

Returns a list of names of all features supported by the User Agent and allowed by the Permissions Policy. Note that features appearing on this list might still be behind a user permission.

[FeaturePolicy.getAllowlistForFeature](/en-US/docs/Web/API/FeaturePolicy/getAllowlistForFeature)Experimental

Returns the allow for the specified feature.

## [Specifications](#specifications)

This feature does not appear to be defined in any specification.

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Permissions-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy)
- [Privacy, permissions, and information security](/en-US/docs/Web/Privacy)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/FeaturePolicy/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/featurepolicy/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFeaturePolicy&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffeaturepolicy%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFeaturePolicy%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffeaturepolicy%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4d929bb0a021c7130d5a71a4bf505bcb8070378d%0A*+Document+last+modified%3A+2025-03-13T12%3A48%3A23.000Z%0A%0A%3C%2Fdetails%3E)
