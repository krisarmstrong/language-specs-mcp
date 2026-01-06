# Permissions API

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The Permissions API provides a consistent programmatic way to query the status of API permissions attributed to the current context, such as a web page or worker. For example, it can be used to determine if permission to access a particular feature or API has been granted, denied, or requires specific user permission.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

Historically different APIs handle their own permissions inconsistently — for example the [Notifications API](/en-US/docs/Web/API/Notifications_API) provided its own methods for requesting permissions and checking permission status, whereas the [Geolocation API](/en-US/docs/Web/API/Geolocation) did not. The Permissions API provides the tools to allow developers to implement a consistent user experience for working with permissions.

The permissions from this API effectively aggregate all security restrictions for the context, including any requirement for an API to be used in a secure context, [Permissions-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy) restrictions applied to the document, requirements for user interaction, and user prompts. So, for example, if an API is restricted by permissions policy, the returned permission would be `denied` and the user would not be prompted for access.

The `permissions` property has been made available on the [Navigator](/en-US/docs/Web/API/Navigator) object, both in the standard browsing context and the worker context ([WorkerNavigator](/en-US/docs/Web/API/WorkerNavigator) — so permission checks are available inside workers), and returns a [Permissions](/en-US/docs/Web/API/Permissions) object that provides access to the Permissions API functionality.

Once you have this object you can then use the [Permissions.query()](/en-US/docs/Web/API/Permissions/query) method to return a promise that resolves with the [PermissionStatus](/en-US/docs/Web/API/PermissionStatus) for a specific API.

### [Requesting permission](#requesting_permission)

If the permission status is `prompt`, the user must acknowledge a prompt to grant access to the feature.

The mechanism that triggers this prompt will depend on the specific API — it is not defined as part of the Permissions API. Generally the trigger is code calling a method to access or open the feature, or that registers for notifications from the feature that will subsequently access it.

Note that not all features require a prompt. Permission might be granted by a `Permission Policy`, implicitly by [transient activation](/en-US/docs/Glossary/Transient_activation), or via some other mechanism.

### [Revoking permission](#revoking_permission)

Permission revocation is not managed by the API. More specifically, a [Permissions.revoke()](/en-US/docs/Web/API/Permissions/revoke) method was proposed, but has since been removed from those browsers where it was implemented.

Users can manually remove permission for particular sites using browser settings:

- Firefox: Hamburger Menu > Settings > Privacy & Security > Permissions (then select the Settings button for the permission of interest).
- Chrome: Hamburger Menu > Settings > Show advanced settings. In the Privacy section, click Content Settings. In the resulting dialog, find the Location section and select Ask when a site tries to…. Finally, click Manage Exceptions and remove the permissions you granted to the sites you are interested in.

### [Permission-aware APIs](#permission-aware_apis)

Not all APIs' permission statuses can be queried using the Permissions API. A non-exhaustive list of permission-aware APIs includes:

- [Background Synchronization API](/en-US/docs/Web/API/Background_Synchronization_API): `background-sync` (should always be granted)
- [Clipboard API](/en-US/docs/Web/API/Clipboard_API#security_considerations): `clipboard-read`, `clipboard-write`
- [Compute Pressure API](/en-US/docs/Web/API/Compute_Pressure_API): `compute-pressure`
- [Geolocation API](/en-US/docs/Web/API/Geolocation_API#security_considerations): `geolocation`
- [Local Font Access API](/en-US/docs/Web/API/Local_Font_Access_API): `local-fonts`
- [Media Capture and Streams API](/en-US/docs/Web/API/Media_Capture_and_Streams_API): `microphone`, `camera`
- [Notifications API](/en-US/docs/Web/API/Notifications_API): `notifications`
- [Payment Handler API](/en-US/docs/Web/API/Payment_Handler_API): `payment-handler`
- [Push API](/en-US/docs/Web/API/Push_API): `push`
- [Screen Capture API](/en-US/docs/Web/API/Screen_Capture_API): `captured-surface-control`, `display-capture`
- [Screen Wake Lock API](/en-US/docs/Web/API/Screen_Wake_Lock_API): `screen-wake-lock`
- [Sensor APIs](/en-US/docs/Web/API/Sensor_APIs): `accelerometer`, `gyroscope`, `magnetometer`, `ambient-light-sensor`
- [Storage Access API](/en-US/docs/Web/API/Storage_Access_API): `storage-access`, `top-level-storage-access`
- [Storage API](/en-US/docs/Web/API/Storage_API): `persistent-storage`
- [Web Bluetooth API](/en-US/docs/Web/API/Web_Bluetooth_API): `bluetooth`
- [Web MIDI API](/en-US/docs/Web/API/Web_MIDI_API): `midi`
- [Window Management API](/en-US/docs/Web/API/Window_Management_API): `window-management`

## [Interfaces](#interfaces)

[Permissions](/en-US/docs/Web/API/Permissions)

Provides the core Permission API functionality, such as methods for querying and revoking permissions.

[PermissionStatus](/en-US/docs/Web/API/PermissionStatus)

Provides access to the current status of a permission, and an event handler to respond to changes in permission status.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[Navigator.permissions](/en-US/docs/Web/API/Navigator/permissions) and [WorkerNavigator.permissions](/en-US/docs/Web/API/WorkerNavigator/permissions)Read only

Provides access to the [Permissions](/en-US/docs/Web/API/Permissions) object from the main context and worker context respectively.

## [Examples](#examples)

We have created an example called Location Finder. You can [run the example live](https://chrisdavidmills.github.io/location-finder-permissions-api/), [view the source code on GitHub](https://github.com/chrisdavidmills/location-finder-permissions-api/tree/gh-pages), or read more about how it works in our article [Using the Permissions API](/en-US/docs/Web/API/Permissions_API/Using_the_Permissions_API).

The [Permissions.query() example](/en-US/docs/Web/API/Permissions/query#test_support_for_various_permissions) also so shows code that tests most permissions on the current browser and logs the result.

## [Specifications](#specifications)

Specification[Permissions](https://w3c.github.io/permissions/)

## [Browser compatibility](#browser_compatibility)

### [api.Permissions](#api.Permissions)

### [api.Navigator.permissions](#api.Navigator.permissions)

### [api.WorkerNavigator.permissions](#api.WorkerNavigator.permissions)

## [See also](#see_also)

- [Using the Permissions API](/en-US/docs/Web/API/Permissions_API/Using_the_Permissions_API)
- [Using the Permissions API to Detect How Often Users Allow or Deny Camera Access](https://blog.addpipe.com/using-permissions-api-to-detect-getusermedia-responses/)
- [Notification.permission](/en-US/docs/Web/API/Notification/permission_static)
- [Privacy, permissions, and information security](/en-US/docs/Web/Privacy)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 20, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Permissions_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/permissions_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPermissions_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpermissions_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPermissions_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpermissions_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F01658f45c6d90bd1098ad02f42fd32e95b59beaf%0A*+Document+last+modified%3A+2025-09-20T16%3A40%3A58.000Z%0A%0A%3C%2Fdetails%3E)
