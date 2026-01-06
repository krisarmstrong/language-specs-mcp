# Navigator

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigator&level=high)

The `Navigator` interface represents the state and the identity of the user agent. It allows scripts to query it and to register themselves to carry on some activities.

A `Navigator` object can be retrieved using the read-only [window.navigator](/en-US/docs/Web/API/Window/navigator) property.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

Doesn't inherit any properties.

### [Standard properties](#standard_properties)

[Navigator.bluetooth](/en-US/docs/Web/API/Navigator/bluetooth)Read onlyExperimentalSecure context

Returns a [Bluetooth](/en-US/docs/Web/API/Bluetooth) object for the current document, providing access to [Web Bluetooth API](/en-US/docs/Web/API/Web_Bluetooth_API) functionality.

[Navigator.clipboard](/en-US/docs/Web/API/Navigator/clipboard)Read onlySecure context

Returns a [Clipboard](/en-US/docs/Web/API/Clipboard) object that provides read and write access to the system clipboard.

[Navigator.connection](/en-US/docs/Web/API/Navigator/connection)Read only

Returns a [NetworkInformation](/en-US/docs/Web/API/NetworkInformation) object containing information about the network connection of a device.

[Navigator.contacts](/en-US/docs/Web/API/Navigator/contacts)Read onlyExperimentalSecure context

Returns a [ContactsManager](/en-US/docs/Web/API/ContactsManager) interface which allows users to select entries from their contact list and share limited details of the selected entries with a website or application.

[Navigator.cookieEnabled](/en-US/docs/Web/API/Navigator/cookieEnabled)Read only

Returns false if setting a cookie will be ignored and true otherwise.

[Navigator.credentials](/en-US/docs/Web/API/Navigator/credentials)Read onlySecure context

Returns the [CredentialsContainer](/en-US/docs/Web/API/CredentialsContainer) interface which exposes methods to request credentials and notify the user agent when interesting events occur such as successful sign in or sign out.

[Navigator.deviceMemory](/en-US/docs/Web/API/Navigator/deviceMemory)Read onlySecure context

Returns the amount of device memory in gigabytes. This value is an approximation given by rounding to the nearest power of 2 and dividing that number by 1024.

[Navigator.devicePosture](/en-US/docs/Web/API/Navigator/devicePosture)Read onlyExperimental

Returns the browser's [DevicePosture](/en-US/docs/Web/API/DevicePosture) object, which allows developers to query the device's current posture (that is, whether the viewport is in a flat or folded state) and run code in response to posture changes.

[Navigator.geolocation](/en-US/docs/Web/API/Navigator/geolocation)Read only

Returns a [Geolocation](/en-US/docs/Web/API/Geolocation) object allowing accessing the location of the device.

[Navigator.gpu](/en-US/docs/Web/API/Navigator/gpu)Read onlySecure context

Returns the [GPU](/en-US/docs/Web/API/GPU) object for the current browsing context. The entry point for the [WebGPU API](/en-US/docs/Web/API/WebGPU_API).

[Navigator.hardwareConcurrency](/en-US/docs/Web/API/Navigator/hardwareConcurrency)Read only

Returns the number of logical processor cores available.

[Navigator.hid](/en-US/docs/Web/API/Navigator/hid)Read onlyExperimentalSecure context

Returns an [HID](/en-US/docs/Web/API/HID) object providing methods for connecting to HID devices, listing attached HID devices, and event handlers for connected HID devices.

[Navigator.ink](/en-US/docs/Web/API/Navigator/ink)Read onlyExperimental

Returns an [Ink](/en-US/docs/Web/API/Ink) object for the current document, providing access to [Ink API](/en-US/docs/Web/API/Ink_API) functionality.

[Navigator.keyboard](/en-US/docs/Web/API/Navigator/keyboard)Read onlyExperimentalSecure context

Returns a [Keyboard](/en-US/docs/Web/API/Keyboard) object which provides access to functions that retrieve keyboard layout maps and toggle capturing of key presses from the physical keyboard.

[Navigator.language](/en-US/docs/Web/API/Navigator/language)Read only

Returns a string representing the preferred language of the user, usually the language of the browser UI. The `null` value is returned when this is unknown.

[Navigator.languages](/en-US/docs/Web/API/Navigator/languages)Read only

Returns an array of strings representing the languages known to the user, by order of preference.

[Navigator.locks](/en-US/docs/Web/API/Navigator/locks)Read onlySecure context

Returns a [LockManager](/en-US/docs/Web/API/LockManager) object that provides methods for requesting a new [Lock](/en-US/docs/Web/API/Lock) object and querying for an existing [Lock](/en-US/docs/Web/API/Lock) object.

[Navigator.login](/en-US/docs/Web/API/Navigator/login)Read onlySecure context

Provides access to the browser's [NavigatorLogin](/en-US/docs/Web/API/NavigatorLogin) object, which a federated identity provider (IdP) can use to set a user's login status when they sign into or out of the IdP. See [Federated Credential Management (FedCM) API](/en-US/docs/Web/API/FedCM_API) for more details.

[Navigator.maxTouchPoints](/en-US/docs/Web/API/Navigator/maxTouchPoints)Read only

Returns the maximum number of simultaneous touch contact points are supported by the current device.

[Navigator.mediaCapabilities](/en-US/docs/Web/API/Navigator/mediaCapabilities)Read only

Returns a [MediaCapabilities](/en-US/docs/Web/API/MediaCapabilities) object that can expose information about the decoding and encoding capabilities for a given format and output capabilities.

[Navigator.mediaDevices](/en-US/docs/Web/API/Navigator/mediaDevices)Read onlySecure context

Returns a reference to a [MediaDevices](/en-US/docs/Web/API/MediaDevices) object which can then be used to get information about available media devices ([MediaDevices.enumerateDevices()](/en-US/docs/Web/API/MediaDevices/enumerateDevices)), find out what constrainable properties are supported for media on the user's computer and user agent ([MediaDevices.getSupportedConstraints()](/en-US/docs/Web/API/MediaDevices/getSupportedConstraints)), and to request access to media using [MediaDevices.getUserMedia()](/en-US/docs/Web/API/MediaDevices/getUserMedia).

[Navigator.mediaSession](/en-US/docs/Web/API/Navigator/mediaSession)Read only

Returns [MediaSession](/en-US/docs/Web/API/MediaSession) object which can be used to provide metadata that can be used by the browser to present information about the currently-playing media to the user, such as in a global media controls UI.

[Navigator.onLine](/en-US/docs/Web/API/Navigator/onLine)Read only

Returns a boolean value indicating whether the browser is working online.

[Navigator.pdfViewerEnabled](/en-US/docs/Web/API/Navigator/pdfViewerEnabled)Read only

Returns `true` if the browser can display PDF files inline when navigating to them, and `false` otherwise.

[Navigator.permissions](/en-US/docs/Web/API/Navigator/permissions)Read only

Returns a [Permissions](/en-US/docs/Web/API/Permissions) object that can be used to query and update permission status of APIs covered by the [Permissions API](/en-US/docs/Web/API/Permissions_API).

[Navigator.presentation](/en-US/docs/Web/API/Navigator/presentation)Read onlySecure context

Returns a reference to the [Presentation](/en-US/docs/Web/API/Presentation) API.

[Navigator.scheduling](/en-US/docs/Web/API/Navigator/scheduling)Read onlyExperimental

Returns a [Scheduling](/en-US/docs/Web/API/Scheduling) object for the current document.

[Navigator.serial](/en-US/docs/Web/API/Navigator/serial)Read onlyExperimentalSecure context

Returns a [Serial](/en-US/docs/Web/API/Serial) object, which represents the entry point into the [Web Serial API](/en-US/docs/Web/API/Web_Serial_API) to enable the control of serial ports.

[Navigator.serviceWorker](/en-US/docs/Web/API/Navigator/serviceWorker)Read onlySecure context

Returns a [ServiceWorkerContainer](/en-US/docs/Web/API/ServiceWorkerContainer) object, which provides access to registration, removal, upgrade, and communication with the [ServiceWorker](/en-US/docs/Web/API/ServiceWorker) objects for the [associated document](https://html.spec.whatwg.org/multipage/browsers.html#concept-document-window).

[Navigator.storage](/en-US/docs/Web/API/Navigator/storage)Read onlySecure context

Returns the singleton [StorageManager](/en-US/docs/Web/API/StorageManager) object used for managing persistence permissions and estimating available storage on a site-by-site/app-by-app basis.

[Navigator.usb](/en-US/docs/Web/API/Navigator/usb)Read onlySecure context

Returns a [USB](/en-US/docs/Web/API/USB) object for the current document, providing access to [WebUSB API](/en-US/docs/Web/API/WebUSB_API) functionality.

[Navigator.userActivation](/en-US/docs/Web/API/Navigator/userActivation)Read only

Returns a [UserActivation](/en-US/docs/Web/API/UserActivation) object containing information about the current window's user activation state.

[Navigator.userAgent](/en-US/docs/Web/API/Navigator/userAgent)Read only

Returns the user agent string for the current browser.

[Navigator.userAgentData](/en-US/docs/Web/API/Navigator/userAgentData)Read onlyExperimentalSecure context

Returns a [NavigatorUAData](/en-US/docs/Web/API/NavigatorUAData) object, which gives access to information about the browser and operating system of the user.

[Navigator.virtualKeyboard](/en-US/docs/Web/API/Navigator/virtualKeyboard)Read onlyExperimentalSecure context

Returns a reference to the [VirtualKeyboard](/en-US/docs/Web/API/VirtualKeyboard) API, to take control of the on-screen virtual keyboard.

[Navigator.wakeLock](/en-US/docs/Web/API/Navigator/wakeLock)Read onlySecure context

Returns a [WakeLock](/en-US/docs/Web/API/WakeLock) interface you can use to request screen wake locks and prevent screen from dimming, turning off, or showing a screen saver.

[Navigator.webdriver](/en-US/docs/Web/API/Navigator/webdriver)Read only

Indicates whether the user agent is controlled by automation.

[Navigator.windowControlsOverlay](/en-US/docs/Web/API/Navigator/windowControlsOverlay)Read onlySecure context

Returns the [WindowControlsOverlay](/en-US/docs/Web/API/WindowControlsOverlay) interface which exposes information about the geometry of the title bar in desktop Progressive Web Apps, and an event to know whenever it changes.

[Navigator.xr](/en-US/docs/Web/API/Navigator/xr)Read onlyExperimentalSecure context

Returns [XRSystem](/en-US/docs/Web/API/XRSystem) object, which represents the entry point into the [WebXR API](/en-US/docs/Web/API/WebXR_Device_API).

### [Non-standard properties](#non-standard_properties)

[Navigator.buildID](/en-US/docs/Web/API/Navigator/buildID)Read onlyNon-standard

Returns the build identifier of the browser. In modern browsers this property now returns a fixed timestamp as a privacy measure, e.g., `20181001000000` in Firefox 64 onwards.

[Navigator.globalPrivacyControl](/en-US/docs/Web/API/Navigator/globalPrivacyControl)Read onlyExperimental

Returns a boolean indicating a user's consent to their information being shared or sold.

`Navigator.standalone`Non-standard

Returns a boolean indicating whether the browser is running in standalone mode. Available on Apple's iOS Safari only.

### [Deprecated properties](#deprecated_properties)

[Navigator.activeVRDisplays](/en-US/docs/Web/API/Navigator/activeVRDisplays)Read onlyDeprecatedNon-standard

Returns an array containing every [VRDisplay](/en-US/docs/Web/API/VRDisplay) object that is currently presenting ([VRDisplay.isPresenting](/en-US/docs/Web/API/VRDisplay/isPresenting) is `true`).

[Navigator.appCodeName](/en-US/docs/Web/API/Navigator/appCodeName)Read only

Always returns `'Mozilla'`, in any browser.

[Navigator.appName](/en-US/docs/Web/API/Navigator/appName)Read only

Always returns `'Netscape'`, in any browser.

[Navigator.appVersion](/en-US/docs/Web/API/Navigator/appVersion)Read only

Returns the version of the browser as a string. Do not rely on this property to return the correct value.

[Navigator.doNotTrack](/en-US/docs/Web/API/Navigator/doNotTrack)Read onlyDeprecatedNon-standard

Reports the value of the user's do-not-track preference. When this value is "1", your website or application should not track the user.

[Navigator.mimeTypes](/en-US/docs/Web/API/Navigator/mimeTypes)Read only

Returns a [MimeTypeArray](/en-US/docs/Web/API/MimeTypeArray) listing the MIME types supported by the browser.

[Navigator.oscpu](/en-US/docs/Web/API/Navigator/oscpu)Read only

Returns a string that represents the current operating system.

[Navigator.platform](/en-US/docs/Web/API/Navigator/platform)Read only

Returns a string representing the platform of the browser. Do not rely on this function to return a significant value.

[Navigator.plugins](/en-US/docs/Web/API/Navigator/plugins)Read only

Returns a [PluginArray](/en-US/docs/Web/API/PluginArray) listing the plugins installed in the browser.

[Navigator.product](/en-US/docs/Web/API/Navigator/product)Read only

Always returns `'Gecko'`, in any browser.

[Navigator.productSub](/en-US/docs/Web/API/Navigator/productSub)Read only

Returns either the string `'20030107'`, or `'"20100101'`.

[Navigator.vendor](/en-US/docs/Web/API/Navigator/vendor)Read only

Returns either the empty string, `'Apple Computer Inc.'`, or `'Google Inc.'`.

[Navigator.vendorSub](/en-US/docs/Web/API/Navigator/vendorSub)Read only

Always returns the empty string.

## [Instance methods](#instance_methods)

Doesn't inherit any method.

[Navigator.canShare()](/en-US/docs/Web/API/Navigator/canShare)Secure context

Returns `true` if a call to `Navigator.share()` would succeed.

[Navigator.clearAppBadge()](/en-US/docs/Web/API/Navigator/clearAppBadge)Secure context

Clears a badge on the current app's icon and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with [undefined](/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined).

[Navigator.deprecatedReplaceInURN()](/en-US/docs/Web/API/Navigator/deprecatedReplaceInURN)Experimental

Substitutes specified strings inside the mapped URL corresponding to a given opaque URN or `FencedFrameConfig`'s internal `url` property. This method has been made available as a temporary measure (hence "deprecated") to enable that substitution for fenced frame URLs, helping ad tech providers to migrate existing implementations across to [privacy sandbox](https://privacysandbox.google.com/) APIs.

[Navigator.getAutoplayPolicy()](/en-US/docs/Web/API/Navigator/getAutoplayPolicy)Experimental

Returns a value indicating whether the specified media element, audio context, or media feature "type" is allowed to autoplay.

[Navigator.getBattery()](/en-US/docs/Web/API/Navigator/getBattery)Secure context

Returns a promise that resolves with a [BatteryManager](/en-US/docs/Web/API/BatteryManager) object that returns information about the battery charging status.

[Navigator.getGamepads()](/en-US/docs/Web/API/Navigator/getGamepads)

returns an array of [Gamepad](/en-US/docs/Web/API/Gamepad) objects, one for each gamepad connected to the device.

[Navigator.getInstalledRelatedApps()](/en-US/docs/Web/API/Navigator/getInstalledRelatedApps)ExperimentalSecure context

Returns a promise that resolves with an array of objects representing any related native or [Progressive Web Applications](/en-US/docs/Web/Progressive_web_apps) that the user has installed.

[Navigator.registerProtocolHandler()](/en-US/docs/Web/API/Navigator/registerProtocolHandler)Secure context

Allows websites to register themselves as a possible handler for a given protocol.

[Navigator.requestMediaKeySystemAccess()](/en-US/docs/Web/API/Navigator/requestMediaKeySystemAccess)Secure context

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) for a MediaKeySystemAccess object.

[Navigator.requestMIDIAccess()](/en-US/docs/Web/API/Navigator/requestMIDIAccess)Secure context

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) representing a request for access to MIDI devices on the user's system.

[Navigator.sendBeacon()](/en-US/docs/Web/API/Navigator/sendBeacon)

Used to asynchronously transfer a small amount of data using [HTTP](/en-US/docs/Glossary/HTTP) from the User Agent to a web server.

[Navigator.setAppBadge()](/en-US/docs/Web/API/Navigator/setAppBadge)Secure context

Sets a badge on the icon associated with this app and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with [undefined](/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined).

[Navigator.share()](/en-US/docs/Web/API/Navigator/share)Secure context

Invokes the native sharing mechanism of the current platform.

[Navigator.vibrate()](/en-US/docs/Web/API/Navigator/vibrate)

Causes vibration on devices with support for it. Does nothing if vibration support isn't available.

[Navigator.unregisterProtocolHandler()](/en-US/docs/Web/API/Navigator/unregisterProtocolHandler)Secure context

Unregister a website that is a handler for a given protocol.

### [Deprecated methods](#deprecated_methods)

[Navigator.getUserMedia()](/en-US/docs/Web/API/Navigator/getUserMedia)DeprecatedSecure context

After having prompted the user for permission, returns the audio or video stream associated to a camera or microphone on the local computer.

[Navigator.getVRDisplays()](/en-US/docs/Web/API/Navigator/getVRDisplays)DeprecatedNon-standard

Returns a promise that resolves to an array of [VRDisplay](/en-US/docs/Web/API/VRDisplay) objects representing any available VR devices connected to the computer.

[Navigator.javaEnabled()](/en-US/docs/Web/API/Navigator/javaEnabled)

Always returns false.

[Navigator.taintEnabled()](/en-US/docs/Web/API/Navigator/taintEnabled)

Returns `false`. JavaScript taint/untaint functions removed in JavaScript 1.2.

## [Specifications](#specifications)

Specification
[HTML# the-navigator-object](https://html.spec.whatwg.org/multipage/system-state.html#the-navigator-object)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Navigator/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/navigator/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigator&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fnavigator%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigator%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fnavigator%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fcf79b60471db6f148fa4ba36f2cdeafbbeb70%0A*+Document+last+modified%3A+2025-10-30T21%3A49%3A49.000Z%0A%0A%3C%2Fdetails%3E)
