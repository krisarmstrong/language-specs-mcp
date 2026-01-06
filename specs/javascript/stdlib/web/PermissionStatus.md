# PermissionStatus

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2022⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPermissionStatus&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `PermissionStatus` interface of the [Permissions API](/en-US/docs/Web/API/Permissions_API) provides the state of an object and an event handler for monitoring changes to said state.

## In this article

- [Instance properties](#instance_properties)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[PermissionStatus.name](/en-US/docs/Web/API/PermissionStatus/name)Read only

Returns the name of a requested permission, identical to the `name` passed to [Permissions.query](/en-US/docs/Web/API/Permissions/query).

[PermissionStatus.state](/en-US/docs/Web/API/PermissionStatus/state)Read only

Returns the state of a requested permission; one of `'granted'`, `'denied'`, or `'prompt'`.

### [Events](#events)

[change](/en-US/docs/Web/API/PermissionStatus/change_event)

Invoked upon changes to `PermissionStatus.state`.

## [Example](#example)

js

```
navigator.permissions
  .query({ name: "geolocation" })
  .then((permissionStatus) => {
    console.log(`geolocation permission status is ${permissionStatus.state}`);
    permissionStatus.onchange = () => {
      console.log(
        `geolocation permission status has changed to ${permissionStatus.state}`,
      );
    };
  });
```

## [Specifications](#specifications)

Specification
[Permissions# permissionstatus-interface](https://w3c.github.io/permissions/#permissionstatus-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 19, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/PermissionStatus/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/permissionstatus/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPermissionStatus&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpermissionstatus%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPermissionStatus%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpermissionstatus%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fee253ac58d71b2ed336b705ab97dbe93122b3e04%0A*+Document+last+modified%3A+2024-04-19T07%3A50%3A33.000Z%0A%0A%3C%2Fdetails%3E)
