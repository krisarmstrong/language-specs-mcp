# Window

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWindow&level=high)

The `Window` interface represents a window containing a [DOM](/en-US/docs/Glossary/DOM) document; the `document` property points to the [DOM document](/en-US/docs/Web/API/Document) loaded in that window.

A window for a given document can be obtained using the [document.defaultView](/en-US/docs/Web/API/Document/defaultView) property.

A global variable, `window`, representing the window in which the script is running, is exposed to JavaScript code.

The `Window` interface is home to a variety of functions, namespaces, objects, and constructors which are not necessarily directly associated with the concept of a user interface window. However, the `Window` interface is a suitable place to include these items that need to be globally available. Many of these are documented in the [JavaScript Reference](/en-US/docs/Web/JavaScript/Reference) and the [DOM Reference](/en-US/docs/Web/API/Document_Object_Model).

In a tabbed browser, each tab is represented by its own `Window` object; the global `window` seen by JavaScript code running within a given tab always represents the tab in which the code is running. That said, even in a tabbed browser, some properties and methods still apply to the overall window that contains the tab, such as [resizeTo()](/en-US/docs/Web/API/Window/resizeTo) and [innerHeight](/en-US/docs/Web/API/Window/innerHeight). Generally, anything that can't reasonably pertain to a tab pertains to the window instead.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Interfaces](#interfaces)
- [Listening for events on Window](#listening_for_events_on_window)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

This interface inherits properties from the [EventTarget](/en-US/docs/Web/API/EventTarget) interface.

Note that properties which are objects (e.g., for overriding the prototype of built-in elements) are listed in a separate section below.

[Window.caches](/en-US/docs/Web/API/Window/caches)Read onlySecure context

Returns the [CacheStorage](/en-US/docs/Web/API/CacheStorage) object associated with the current context. This object enables functionality such as storing assets for offline use, and generating custom responses to requests.

[Window.clientInformation](/en-US/docs/Web/API/Window/navigator)Read only

An alias for [Window.navigator](/en-US/docs/Web/API/Window/navigator).

[Window.closed](/en-US/docs/Web/API/Window/closed)Read only

This property indicates whether the current window is closed or not.

[Window.cookieStore](/en-US/docs/Web/API/Window/cookieStore)Read onlySecure context

Returns a reference to the [CookieStore](/en-US/docs/Web/API/CookieStore) object for the current document context.

[Window.credentialless](/en-US/docs/Web/API/Window/credentialless)Read onlyExperimental

Returns a boolean that indicates whether the current document was loaded inside a credentialless [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe). See [IFrame credentialless](/en-US/docs/Web/HTTP/Guides/IFrame_credentialless) for more details.

[Window.crossOriginIsolated](/en-US/docs/Web/API/Window/crossOriginIsolated)Read only

Returns a boolean value that indicates whether the website is in a cross-origin isolation state.

[Window.crypto](/en-US/docs/Web/API/Window/crypto)Read only

Returns the [Crypto](/en-US/docs/Web/API/Crypto) object associated to the global object.

[Window.customElements](/en-US/docs/Web/API/Window/customElements)Read only

Returns a reference to the [CustomElementRegistry](/en-US/docs/Web/API/CustomElementRegistry) object, which can be used to register new [custom elements](/en-US/docs/Web/API/Web_components/Using_custom_elements) and get information about previously registered custom elements.

[Window.devicePixelRatio](/en-US/docs/Web/API/Window/devicePixelRatio)Read only

Returns the ratio between physical pixels and device independent pixels in the current display.

[Window.document](/en-US/docs/Web/API/Window/document)Read only

Returns a reference to the document that the window contains.

[Window.documentPictureInPicture](/en-US/docs/Web/API/Window/documentPictureInPicture)Read onlyExperimentalSecure context

Returns a reference to the [document Picture-in-Picture](/en-US/docs/Web/API/Document_Picture-in-Picture_API) window for the current document context.

[Window.fence](/en-US/docs/Web/API/Window/fence)Read onlyExperimental

Returns a [Fence](/en-US/docs/Web/API/Fence) object instance for the current document context. Available only to documents embedded inside a [<fencedframe>](/en-US/docs/Web/HTML/Reference/Elements/fencedframe).

[Window.frameElement](/en-US/docs/Web/API/Window/frameElement)Read only

Returns the element in which the window is embedded, or null if the window is not embedded.

[Window.frames](/en-US/docs/Web/API/Window/frames)Read only

Returns an array of the subframes in the current window.

[Window.fullScreen](/en-US/docs/Web/API/Window/fullScreen)Non-standard

This property indicates whether the window is displayed in full screen or not.

[Window.history](/en-US/docs/Web/API/Window/history)Read only

Returns a reference to the history object.

[Window.indexedDB](/en-US/docs/Web/API/Window/indexedDB)Read only

Provides a mechanism for applications to asynchronously access capabilities of indexed databases; returns an [IDBFactory](/en-US/docs/Web/API/IDBFactory) object.

[Window.innerHeight](/en-US/docs/Web/API/Window/innerHeight)Read only

Gets the height of the content area of the browser window including, if rendered, the horizontal scrollbar.

[Window.innerWidth](/en-US/docs/Web/API/Window/innerWidth)Read only

Gets the width of the content area of the browser window including, if rendered, the vertical scrollbar.

[Window.isSecureContext](/en-US/docs/Web/API/Window/isSecureContext)Read only

Returns a boolean indicating whether the current context is secure (`true`) or not (`false`).

[Window.launchQueue](/en-US/docs/Web/API/Window/launchQueue)Read onlyExperimental

When a [progressive web app](/en-US/docs/Web/Progressive_web_apps) (PWA) is launched with a [launch_handler](/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/launch_handler)`client_mode` value of `focus-existing`, `navigate-new`, or `navigate-existing`, the `launchQueue` provides access to the [LaunchQueue](/en-US/docs/Web/API/LaunchQueue) class, which allows custom launch navigation handling to be implemented for the PWA.

[Window.length](/en-US/docs/Web/API/Window/length)Read only

Returns the number of frames in the window. See also [window.frames](/en-US/docs/Web/API/Window/frames).

[Window.localStorage](/en-US/docs/Web/API/Window/localStorage)Read only

Returns a reference to the local storage object used to store data that may only be accessed by the origin that created it.

[Window.location](/en-US/docs/Web/API/Window/location)

Gets/sets the location, or current URL, of the window object.

[Window.locationbar](/en-US/docs/Web/API/Window/locationbar)Read only

Returns the locationbar object.

[Window.menubar](/en-US/docs/Web/API/Window/menubar)Read only

Returns the menubar object.

[Window.mozInnerScreenX](/en-US/docs/Web/API/Window/mozInnerScreenX)Read onlyNon-standard

Returns the horizontal (X) coordinate of the top-left corner of the window's viewport, in screen coordinates. This value is reported in CSS pixels. See `mozScreenPixelsPerCSSPixel` in `nsIDOMWindowUtils` for a conversion factor to adapt to screen pixels if needed.

[Window.mozInnerScreenY](/en-US/docs/Web/API/Window/mozInnerScreenY)Read onlyNon-standard

Returns the vertical (Y) coordinate of the top-left corner of the window's viewport, in screen coordinates. This value is reported in CSS pixels. See `mozScreenPixelsPerCSSPixel` for a conversion factor to adapt to screen pixels if needed.

[Window.name](/en-US/docs/Web/API/Window/name)

Gets/sets the name of the window.

[Window.navigation](/en-US/docs/Web/API/Window/navigation)Read only

Returns the current `window`'s associated [Navigation](/en-US/docs/Web/API/Navigation) object. The entry point for the [Navigation API](/en-US/docs/Web/API/Navigation_API).

[Window.navigator](/en-US/docs/Web/API/Window/navigator)Read only

Returns a reference to the navigator object.

[Window.opener](/en-US/docs/Web/API/Window/opener)

Returns a reference to the window that opened this current window.

[Window.origin](/en-US/docs/Web/API/Window/origin)Read only

Returns the global object's origin, serialized as a string.

[Window.originAgentCluster](/en-US/docs/Web/API/Window/originAgentCluster)Read only

Returns `true` if this window belongs to an origin-keyed agent cluster.

[Window.outerHeight](/en-US/docs/Web/API/Window/outerHeight)Read only

Gets the height of the outside of the browser window.

[Window.outerWidth](/en-US/docs/Web/API/Window/outerWidth)Read only

Gets the width of the outside of the browser window.

[Window.pageXOffset](/en-US/docs/Web/API/Window/scrollX)Read only

An alias for [window.scrollX](/en-US/docs/Web/API/Window/scrollX).

[Window.pageYOffset](/en-US/docs/Web/API/Window/scrollY)Read only

An alias for [window.scrollY](/en-US/docs/Web/API/Window/scrollY).

[Window.parent](/en-US/docs/Web/API/Window/parent)Read only

Returns a reference to the parent of the current window or subframe.

[Window.performance](/en-US/docs/Web/API/Window/performance)Read only

Returns a [Performance](/en-US/docs/Web/API/Performance) object, which includes the [timing](/en-US/docs/Web/API/Performance/timing) and [navigation](/en-US/docs/Web/API/Performance/navigation) attributes, each of which is an object providing [performance-related](/en-US/docs/Web/API/Performance_API/Navigation_timing) data. See also [Using Navigation Timing](/en-US/docs/Web/API/Performance_API/Navigation_timing) for additional information and examples.

[Window.personalbar](/en-US/docs/Web/API/Window/personalbar)Read only

Returns the personalbar object.

[Window.scheduler](/en-US/docs/Web/API/Window/scheduler)Read only

Returns the [Scheduler](/en-US/docs/Web/API/Scheduler) object associated with the current context. This is the entry point for using the [Prioritized Task Scheduling API](/en-US/docs/Web/API/Prioritized_Task_Scheduling_API).

[Window.screen](/en-US/docs/Web/API/Window/screen)Read only

Returns a reference to the screen object associated with the window.

[Window.screenX](/en-US/docs/Web/API/Window/screenX) and [Window.screenLeft](/en-US/docs/Web/API/Window/screenLeft)Read only

Both properties return the horizontal distance from the left border of the user's browser viewport to the left side of the screen.

[Window.screenY](/en-US/docs/Web/API/Window/screenY) and [Window.screenTop](/en-US/docs/Web/API/Window/screenTop)Read only

Both properties return the vertical distance from the top border of the user's browser viewport to the top side of the screen.

[Window.scrollbars](/en-US/docs/Web/API/Window/scrollbars)Read only

Returns the scrollbars object.

[Window.scrollMaxX](/en-US/docs/Web/API/Window/scrollMaxX)Non-standardRead only

The maximum offset that the window can be scrolled to horizontally, that is the document width minus the viewport width.

[Window.scrollMaxY](/en-US/docs/Web/API/Window/scrollMaxY)Non-standardRead only

The maximum offset that the window can be scrolled to vertically (i.e., the document height minus the viewport height).

[Window.scrollX](/en-US/docs/Web/API/Window/scrollX)Read only

Returns the number of pixels that the document has already been scrolled horizontally.

[Window.scrollY](/en-US/docs/Web/API/Window/scrollY)Read only

Returns the number of pixels that the document has already been scrolled vertically.

[Window.self](/en-US/docs/Web/API/Window/self)Read only

Returns an object reference to the window object itself.

[Window.sessionStorage](/en-US/docs/Web/API/Window/sessionStorage)

Returns a reference to the session storage object used to store data that may only be accessed by the origin that created it.

[Window.sharedStorage](/en-US/docs/Web/API/Window/sharedStorage)Read onlySecure contextDeprecated

Returns the [WindowSharedStorage](/en-US/docs/Web/API/WindowSharedStorage) object for the current origin. This is the main entry point for writing data to shared storage using the [Shared Storage API](/en-US/docs/Web/API/Shared_Storage_API).

[Window.speechSynthesis](/en-US/docs/Web/API/Window/speechSynthesis)Read only

Returns a [SpeechSynthesis](/en-US/docs/Web/API/SpeechSynthesis) object, which is the entry point into using [Web Speech API](/en-US/docs/Web/API/Web_Speech_API) speech synthesis functionality.

[Window.statusbar](/en-US/docs/Web/API/Window/statusbar)Read only

Returns the statusbar object.

[Window.toolbar](/en-US/docs/Web/API/Window/toolbar)Read only

Returns the toolbar object.

[Window.top](/en-US/docs/Web/API/Window/top)Read only

Returns a reference to the topmost window in the window hierarchy. This property is read only.

[Window.trustedTypes](/en-US/docs/Web/API/Window/trustedTypes)Read only

Returns the [TrustedTypePolicyFactory](/en-US/docs/Web/API/TrustedTypePolicyFactory) object associated with the global object, providing the entry point for using the [Trusted Types API](/en-US/docs/Web/API/Trusted_Types_API).

[Window.viewport](/en-US/docs/Web/API/Window/viewport)ExperimentalRead only

Returns a [Viewport](/en-US/docs/Web/API/Viewport) object instance, which provides information about the current state of the device's viewport.

[Window.visualViewport](/en-US/docs/Web/API/Window/visualViewport)Read only

Returns a [VisualViewport](/en-US/docs/Web/API/VisualViewport) object which represents the visual viewport for a given window.

[Window.window](/en-US/docs/Web/API/Window/window)Read only

Returns a reference to the current window.

[window[0], window[1], etc.](#window0)

Returns a reference to the `window` object in the frames. See [Window.frames](/en-US/docs/Web/API/Window/frames) for more details.

[Named properties](#named_properties)

Some elements in the document are also exposed as window properties:

- For each [<embed>](/en-US/docs/Web/HTML/Reference/Elements/embed), [<form>](/en-US/docs/Web/HTML/Reference/Elements/form), [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe), [<img>](/en-US/docs/Web/HTML/Reference/Elements/img), and [<object>](/en-US/docs/Web/HTML/Reference/Elements/object) element, its `name` (if non-empty) is exposed. For example, if the document contains `<form name="my_form">`, then `window["my_form"]` (and its equivalent `window.my_form`) returns a reference to that element.
- For each HTML element, its `id` (if non-empty) is exposed.

If a property corresponds to a single element, that element is directly returned. If the property corresponds to multiple elements, then an [HTMLCollection](/en-US/docs/Web/API/HTMLCollection) is returned containing all of them. If any of the elements is a navigable `<iframe>` or `<object>`, then the [contentWindow](/en-US/docs/Web/API/HTMLIFrameElement/contentWindow) of first such iframe is returned instead.

### [Deprecated properties](#deprecated_properties)

[Window.event](/en-US/docs/Web/API/Window/event)DeprecatedRead only

Returns the current event, which is the event currently being handled by the JavaScript code's context, or `undefined` if no event is currently being handled. The [Event](/en-US/docs/Web/API/Event) object passed directly to event handlers should be used instead whenever possible.

[Window.external](/en-US/docs/Web/API/Window/external)DeprecatedRead only

Returns an object with functions for adding external search providers to the browser.

[Window.orientation](/en-US/docs/Web/API/Window/orientation)DeprecatedRead only

Returns the orientation in degrees (in 90 degree increments) of the viewport relative to the device's natural orientation.

[Window.status](/en-US/docs/Web/API/Window/status)Deprecated

Gets/sets the text in the statusbar at the bottom of the browser.

## [Instance methods](#instance_methods)

This interface inherits methods from the [EventTarget](/en-US/docs/Web/API/EventTarget) interface.

[Window.atob()](/en-US/docs/Web/API/Window/atob)

Decodes a string of data which has been encoded using base-64 encoding.

[Window.alert()](/en-US/docs/Web/API/Window/alert)

Displays an alert dialog.

[Window.blur()](/en-US/docs/Web/API/Window/blur)Deprecated

Sets focus away from the window.

[Window.btoa()](/en-US/docs/Web/API/Window/btoa)

Creates a base-64 encoded ASCII string from a string of binary data.

[Window.cancelAnimationFrame()](/en-US/docs/Web/API/Window/cancelAnimationFrame)

Enables you to cancel a callback previously scheduled with [Window.requestAnimationFrame](/en-US/docs/Web/API/Window/requestAnimationFrame).

[Window.cancelIdleCallback()](/en-US/docs/Web/API/Window/cancelIdleCallback)

Enables you to cancel a callback previously scheduled with [Window.requestIdleCallback](/en-US/docs/Web/API/Window/requestIdleCallback).

[Window.clearInterval()](/en-US/docs/Web/API/Window/clearInterval)

Cancels the repeated execution set using [Window.setInterval()](/en-US/docs/Web/API/Window/setInterval).

[Window.clearTimeout()](/en-US/docs/Web/API/Window/clearTimeout)

Cancels the delayed execution set using [Window.setTimeout()](/en-US/docs/Web/API/Window/setTimeout).

[Window.close()](/en-US/docs/Web/API/Window/close)

Closes the current window.

[Window.confirm()](/en-US/docs/Web/API/Window/confirm)

Displays a dialog with a message that the user needs to respond to.

[Window.createImageBitmap()](/en-US/docs/Web/API/Window/createImageBitmap)

Accepts a variety of different image sources, and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which resolves to an [ImageBitmap](/en-US/docs/Web/API/ImageBitmap). Optionally the source is cropped to the rectangle of pixels originating at (sx, sy) with width sw, and height sh.

[Window.dump()](/en-US/docs/Web/API/Window/dump)Non-standard

Writes a message to the console.

[Window.fetch()](/en-US/docs/Web/API/Window/fetch)

Starts the process of fetching a resource from the network.

[Window.fetchLater()](/en-US/docs/Web/API/Window/fetchLater)Experimental

Creates a deferred fetch, which is sent once the page is navigated away from (it is destroyed or enters the [bfcache](/en-US/docs/Glossary/bfcache)), or after a provided `activateAfter` timeout — whichever comes first.

[Window.find()](/en-US/docs/Web/API/Window/find)Non-standard

Searches for a given string in a window.

[Window.focus()](/en-US/docs/Web/API/Window/focus)

Sets focus on the current window.

[Window.getComputedStyle()](/en-US/docs/Web/API/Window/getComputedStyle)

Gets computed style for the specified element. Computed style indicates the computed values of all CSS properties of the element.

[Window.getDefaultComputedStyle()](/en-US/docs/Web/API/Window/getDefaultComputedStyle)Non-standard

Gets default computed style for the specified element, ignoring author stylesheets.

[Window.getScreenDetails()](/en-US/docs/Web/API/Window/getScreenDetails)ExperimentalSecure context

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with a [ScreenDetails](/en-US/docs/Web/API/ScreenDetails) object instance representing the details of all the screens available to the user's device.

[Window.getSelection()](/en-US/docs/Web/API/Window/getSelection)

Returns the selection object representing the selected item(s).

[Window.matchMedia()](/en-US/docs/Web/API/Window/matchMedia)

Returns a [MediaQueryList](/en-US/docs/Web/API/MediaQueryList) object representing the specified media query string.

[Window.moveBy()](/en-US/docs/Web/API/Window/moveBy)

Moves the current window by a specified amount.

[Window.moveTo()](/en-US/docs/Web/API/Window/moveTo)

Moves the window to the specified coordinates.

[Window.open()](/en-US/docs/Web/API/Window/open)

Opens a new window.

[Window.postMessage()](/en-US/docs/Web/API/Window/postMessage)

Provides a secure means for one window to send a string of data to another window, which need not be within the same domain as the first.

[Window.print()](/en-US/docs/Web/API/Window/print)

Opens the Print Dialog to print the current document.

[Window.prompt()](/en-US/docs/Web/API/Window/prompt)

Returns the text entered by the user in a prompt dialog.

[Window.queryLocalFonts()](/en-US/docs/Web/API/Window/queryLocalFonts)ExperimentalSecure context

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with an array of [FontData](/en-US/docs/Web/API/FontData) objects representing the font faces available locally.

[Window.queueMicrotask()](/en-US/docs/Web/API/Window/queueMicrotask)

Queues a microtask to be executed at a safe time prior to control returning to the browser's event loop.

[Window.reportError()](/en-US/docs/Web/API/Window/reportError)

Reports an error in a script, emulating an unhandled exception.

[Window.requestAnimationFrame()](/en-US/docs/Web/API/Window/requestAnimationFrame)

Tells the browser that an animation is in progress, requesting that the browser schedule a repaint of the window for the next animation frame.

[Window.requestIdleCallback()](/en-US/docs/Web/API/Window/requestIdleCallback)

Enables the scheduling of tasks during a browser's idle periods.

[Window.resizeBy()](/en-US/docs/Web/API/Window/resizeBy)

Resizes the current window by a certain amount.

[Window.resizeTo()](/en-US/docs/Web/API/Window/resizeTo)

Dynamically resizes window.

[Window.scroll()](/en-US/docs/Web/API/Window/scroll)

Scrolls the window to a particular place in the document.

[Window.scrollBy()](/en-US/docs/Web/API/Window/scrollBy)

Scrolls the document in the window by the given amount.

[Window.scrollByLines()](/en-US/docs/Web/API/Window/scrollByLines)Non-standard

Scrolls the document by the given number of lines.

[Window.scrollByPages()](/en-US/docs/Web/API/Window/scrollByPages)Non-standard

Scrolls the current document by the specified number of pages.

[Window.scrollTo()](/en-US/docs/Web/API/Window/scrollTo)

Scrolls to a particular set of coordinates in the document.

[Window.setInterval()](/en-US/docs/Web/API/Window/setInterval)

Schedules a function to execute every time a given number of milliseconds elapses.

[Window.setTimeout()](/en-US/docs/Web/API/Window/setTimeout)

Schedules a function to execute in a given amount of time.

[Window.showDirectoryPicker()](/en-US/docs/Web/API/Window/showDirectoryPicker)ExperimentalSecure context

Displays a directory picker which allows the user to select a directory.

[Window.showOpenFilePicker()](/en-US/docs/Web/API/Window/showOpenFilePicker)ExperimentalSecure context

Shows a file picker that allows a user to select a file or multiple files.

[Window.showSaveFilePicker()](/en-US/docs/Web/API/Window/showSaveFilePicker)ExperimentalSecure context

Shows a file picker that allows a user to save a file.

[Window.sizeToContent()](/en-US/docs/Web/API/Window/sizeToContent)Non-standard

Sizes the window according to its content.

[Window.stop()](/en-US/docs/Web/API/Window/stop)

This method stops window loading.

[Window.structuredClone()](/en-US/docs/Web/API/Window/structuredClone)

Creates a [deep clone](/en-US/docs/Glossary/Deep_copy) of a given value using the [structured clone algorithm](/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm).

### [Deprecated methods](#deprecated_methods)

[Window.captureEvents()](/en-US/docs/Web/API/Window/captureEvents)Deprecated

Registers the window to capture all events of the specified type.

[Window.clearImmediate()](/en-US/docs/Web/API/Window/clearImmediate)Non-standardDeprecated

Cancels the repeated execution set using `setImmediate()`.

[Window.releaseEvents()](/en-US/docs/Web/API/Window/releaseEvents)Deprecated

Releases the window from trapping events of a specific type.

[Window.requestFileSystem()](/en-US/docs/Web/API/Window/requestFileSystem)Non-standardDeprecated

Lets a website or app gain access to a sandboxed file system for its own use.

[Window.setImmediate()](/en-US/docs/Web/API/Window/setImmediate)Non-standardDeprecated

Executes a function after the browser has finished other heavy tasks.

[Window.setResizable()](/en-US/docs/Web/API/Window/setResizable)Non-standardDeprecated

Does nothing (no-op). Kept for backward compatibility with Netscape 4.x.

[Window.webkitConvertPointFromNodeToPage()](/en-US/docs/Web/API/Window/webkitConvertPointFromNodeToPage)Non-standardDeprecated

Transforms a [WebKitPoint](/en-US/docs/Web/API/WebKitPoint) from the node's coordinate system to the page's coordinate system.

[Window.webkitConvertPointFromPageToNode()](/en-US/docs/Web/API/Window/webkitConvertPointFromPageToNode)Non-standardDeprecated

Transforms a [WebKitPoint](/en-US/docs/Web/API/WebKitPoint) from the page's coordinate system to the node's coordinate system.

## [Events](#events)

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface. In addition to the events listed below, many events can bubble from the [Document](/en-US/docs/Web/API/Document) contained in the window object.

[error](/en-US/docs/Web/API/Window/error_event)

Fired when a resource failed to load, or can't be used. For example, if a script has an execution error or an image can't be found or is invalid.

[languagechange](/en-US/docs/Web/API/Window/languagechange_event)

Fired at the global scope object when the user's preferred language changes.

[resize](/en-US/docs/Web/API/Window/resize_event)

Fired when the window has been resized.

[storage](/en-US/docs/Web/API/Window/storage_event)

Fired when a storage area (`localStorage` or `sessionStorage`) has been modified in the context of another document.

### [Connection events](#connection_events)

[offline](/en-US/docs/Web/API/Window/offline_event)

Fired when the browser has lost access to the network and the value of `navigator.onLine` has switched to `false`.

[online](/en-US/docs/Web/API/Window/online_event)

Fired when the browser has gained access to the network and the value of `navigator.onLine` has switched to `true`.

### [Device orientation events](#device_orientation_events)

[devicemotion](/en-US/docs/Web/API/Window/devicemotion_event)Secure context

Fired at a regular interval, indicating the amount of physical force of acceleration the device is receiving and the rate of rotation, if available.

[deviceorientation](/en-US/docs/Web/API/Window/deviceorientation_event)Secure context

Fired when fresh data is available from the magnetometer orientation sensor about the current orientation of the device as compared to the Earth coordinate frame.

[deviceorientationabsolute](/en-US/docs/Web/API/Window/deviceorientationabsolute_event)Secure context

Fired when fresh data is available from the magnetometer orientation sensor about the current absolute orientation of the device as compared to the Earth coordinate frame.

### [Focus events](#focus_events)

[blur](/en-US/docs/Web/API/Window/blur_event)

Fired when an element has lost focus.

[focus](/en-US/docs/Web/API/Window/focus_event)

Fired when an element has gained focus.

### [Gamepad events](#gamepad_events)

[gamepadconnected](/en-US/docs/Web/API/Window/gamepadconnected_event)

Fired when the browser detects that a gamepad has been connected or the first time a button/axis of the gamepad is used.

[gamepaddisconnected](/en-US/docs/Web/API/Window/gamepaddisconnected_event)

Fired when the browser detects that a gamepad has been disconnected.

### [History events](#history_events)

[hashchange](/en-US/docs/Web/API/Window/hashchange_event)

Fired when the fragment identifier of the URL has changed (the part of the URL beginning with and following the `#` symbol).

[pagehide](/en-US/docs/Web/API/Window/pagehide_event)

Sent when the browser hides the current document while in the process of switching to displaying in its place a different document from the session's history. This happens, for example, when the user clicks the Back button or when they click the Forward button to move ahead in session history.

[pagereveal](/en-US/docs/Web/API/Window/pagereveal_event)

Fired when a document is first rendered, either when loading a fresh document from the network or activating a document (either from [back/forward cache](/en-US/docs/Glossary/bfcache) (bfcache) or [prerender](/en-US/docs/Glossary/Prerender)).

[pageshow](/en-US/docs/Web/API/Window/pageshow_event)

Sent when the browser makes the document visible due to navigation tasks, including not only when the page is first loaded, but also situations such as the user navigating back to the page after having navigated to another within the same tab.

[pageswap](/en-US/docs/Web/API/Window/pageswap_event)

Fired when a document is about to be unloaded due to a navigation.

[popstate](/en-US/docs/Web/API/Window/popstate_event)

Fired when the active history entry changes.

### [Load & unload events](#load_unload_events)

[beforeunload](/en-US/docs/Web/API/Window/beforeunload_event)

Fired when the window, the document and its resources are about to be unloaded.

[load](/en-US/docs/Web/API/Window/load_event)

Fired when the whole page has loaded, including all dependent resources such as stylesheets images.

[unload](/en-US/docs/Web/API/Window/unload_event)

Fired when the document or a child resource is being unloaded.

### [Manifest events](#manifest_events)

[appinstalled](/en-US/docs/Web/API/Window/appinstalled_event)

Fired when the browser has successfully installed a page as an application.

[beforeinstallprompt](/en-US/docs/Web/API/Window/beforeinstallprompt_event)

Fired when a user is about to be prompted to install a web application.

### [Messaging events](#messaging_events)

[message](/en-US/docs/Web/API/Window/message_event)

Fired when the window receives a message, for example from a call to [Window.postMessage()](/en-US/docs/Web/API/Window/postMessage) from another browsing context.

[messageerror](/en-US/docs/Web/API/Window/messageerror_event)

Fired when a `Window` object receives a message that can't be deserialized.

### [Print events](#print_events)

[afterprint](/en-US/docs/Web/API/Window/afterprint_event)

Fired after the associated document has started printing or the print preview has been closed.

[beforeprint](/en-US/docs/Web/API/Window/beforeprint_event)

Fired when the associated document is about to be printed or previewed for printing.

### [Promise rejection events](#promise_rejection_events)

[rejectionhandled](/en-US/docs/Web/API/Window/rejectionhandled_event)

Sent every time a JavaScript [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) is rejected, regardless of whether or not there is a handler in place to catch the rejection.

[unhandledrejection](/en-US/docs/Web/API/Window/unhandledrejection_event)

Sent when a JavaScript [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) is rejected but there is no handler in place to catch the rejection.

### [Scroll events](#scroll_events)

[scrollsnapchange](/en-US/docs/Web/API/Window/scrollsnapchange_event)Experimental

Fired on the scroll container at the end of a scrolling operation when a new scroll snap target has been selected.

[scrollsnapchanging](/en-US/docs/Web/API/Window/scrollsnapchanging_event)Experimental

Fired on the scroll container when the browser determines a new scroll snap target is pending, i.e., it will be selected when the current scroll gesture ends.

### [Deprecated events](#deprecated_events)

[orientationchange](/en-US/docs/Web/API/Window/orientationchange_event)Deprecated

Fired when the orientation of the device has changed.

[vrdisplayactivate](/en-US/docs/Web/API/Window/vrdisplayactivate_event)DeprecatedNon-standard

Fired when a display is able to be presented to.

[vrdisplayconnect](/en-US/docs/Web/API/Window/vrdisplayconnect_event)DeprecatedNon-standard

Fired when a compatible VR device has been connected to the computer.

[vrdisplaydisconnect](/en-US/docs/Web/API/Window/vrdisplaydisconnect_event)DeprecatedNon-standard

Fired when a compatible VR device has been disconnected from the computer.

[vrdisplaydeactivate](/en-US/docs/Web/API/Window/vrdisplaydeactivate_event)DeprecatedNon-standard

Fired when a display can no longer be presented to.

[vrdisplaypresentchange](/en-US/docs/Web/API/Window/vrdisplaypresentchange_event)DeprecatedNon-standard

Fired when the presenting state of a VR device changes — i.e., goes from presenting to not presenting, or vice versa.

### [Bubbled events](#bubbled_events)

Not all events that bubble can reach the `Window` object. Only the following do and can be listened for on the `Window` object:

- `abort`
- [auxclick](/en-US/docs/Web/API/Element/auxclick_event)
- [beforeinput](/en-US/docs/Web/API/Element/beforeinput_event)
- [beforematch](/en-US/docs/Web/API/Element/beforematch_event)
- [beforetoggle](/en-US/docs/Web/API/HTMLElement/beforetoggle_event)
- `cancel`
- [canplay](/en-US/docs/Web/API/HTMLMediaElement/canplay_event)
- [canplaythrough](/en-US/docs/Web/API/HTMLMediaElement/canplaythrough_event)
- [change](/en-US/docs/Web/API/HTMLElement/change_event)
- [click](/en-US/docs/Web/API/Element/click_event)
- [close](/en-US/docs/Web/API/HTMLDialogElement/close_event)
- [contextlost](/en-US/docs/Web/API/HTMLCanvasElement/contextlost_event)
- [contextmenu](/en-US/docs/Web/API/Element/contextmenu_event)
- [contextrestored](/en-US/docs/Web/API/HTMLCanvasElement/contextrestored_event)
- [copy](/en-US/docs/Web/API/Element/copy_event)
- [cuechange](/en-US/docs/Web/API/HTMLTrackElement/cuechange_event)
- [cut](/en-US/docs/Web/API/Element/cut_event)
- [dblclick](/en-US/docs/Web/API/Element/dblclick_event)
- [drag](/en-US/docs/Web/API/HTMLElement/drag_event)
- [dragend](/en-US/docs/Web/API/HTMLElement/dragend_event)
- [dragenter](/en-US/docs/Web/API/HTMLElement/dragenter_event)
- [dragleave](/en-US/docs/Web/API/HTMLElement/dragleave_event)
- [dragover](/en-US/docs/Web/API/HTMLElement/dragover_event)
- [dragstart](/en-US/docs/Web/API/HTMLElement/dragstart_event)
- [drop](/en-US/docs/Web/API/HTMLElement/drop_event)
- [durationchange](/en-US/docs/Web/API/HTMLMediaElement/durationchange_event)
- [emptied](/en-US/docs/Web/API/HTMLMediaElement/emptied_event)
- [ended](/en-US/docs/Web/API/HTMLMediaElement/ended_event)
- [formdata](/en-US/docs/Web/API/HTMLFormElement/formdata_event)
- [input](/en-US/docs/Web/API/Element/input_event)
- [invalid](/en-US/docs/Web/API/HTMLInputElement/invalid_event)
- [keydown](/en-US/docs/Web/API/Element/keydown_event)
- [keypress](/en-US/docs/Web/API/Element/keypress_event)
- [keyup](/en-US/docs/Web/API/Element/keyup_event)
- [loadeddata](/en-US/docs/Web/API/HTMLMediaElement/loadeddata_event)
- [loadedmetadata](/en-US/docs/Web/API/HTMLMediaElement/loadedmetadata_event)
- [loadstart](/en-US/docs/Web/API/HTMLMediaElement/loadstart_event)
- [mousedown](/en-US/docs/Web/API/Element/mousedown_event)
- [mouseenter](/en-US/docs/Web/API/Element/mouseenter_event)
- [mouseleave](/en-US/docs/Web/API/Element/mouseleave_event)
- [mousemove](/en-US/docs/Web/API/Element/mousemove_event)
- [mouseout](/en-US/docs/Web/API/Element/mouseout_event)
- [mouseover](/en-US/docs/Web/API/Element/mouseover_event)
- [mouseup](/en-US/docs/Web/API/Element/mouseup_event)
- [paste](/en-US/docs/Web/API/Element/paste_event)
- [pause](/en-US/docs/Web/API/HTMLMediaElement/pause_event)
- [play](/en-US/docs/Web/API/HTMLMediaElement/play_event)
- [playing](/en-US/docs/Web/API/HTMLMediaElement/playing_event)
- [progress](/en-US/docs/Web/API/HTMLMediaElement/progress_event)
- [ratechange](/en-US/docs/Web/API/HTMLMediaElement/ratechange_event)
- [reset](/en-US/docs/Web/API/HTMLFormElement/reset_event)
- [scrollend](/en-US/docs/Web/API/Element/scrollend_event)
- [securitypolicyviolation](/en-US/docs/Web/API/Element/securitypolicyviolation_event)
- [seeked](/en-US/docs/Web/API/HTMLMediaElement/seeked_event)
- [seeking](/en-US/docs/Web/API/HTMLMediaElement/seeking_event)
- [select](/en-US/docs/Web/API/HTMLInputElement/select_event)
- [slotchange](/en-US/docs/Web/API/HTMLSlotElement/slotchange_event)
- [stalled](/en-US/docs/Web/API/HTMLMediaElement/stalled_event)
- [submit](/en-US/docs/Web/API/HTMLFormElement/submit_event)
- [suspend](/en-US/docs/Web/API/HTMLMediaElement/suspend_event)
- [timeupdate](/en-US/docs/Web/API/HTMLMediaElement/timeupdate_event)
- [toggle](/en-US/docs/Web/API/HTMLElement/toggle_event)
- [volumechange](/en-US/docs/Web/API/HTMLMediaElement/volumechange_event)
- [waiting](/en-US/docs/Web/API/HTMLMediaElement/waiting_event)
- [wheel](/en-US/docs/Web/API/Element/wheel_event)

## [Interfaces](#interfaces)

See [DOM Reference](/en-US/docs/Web/API/Document_Object_Model).

## [Listening for events on Window](#listening_for_events_on_window)

HTML elements have three ways to listen for events:

- Add an event listener to the element using the [EventTarget.addEventListener](/en-US/docs/Web/API/EventTarget/addEventListener) method.
- Assign an event handler to the element's `oneventname` property in JavaScript.
- Add an `on`-prefixed attribute to the element in the HTML.

To listen for events on `Window` objects, in general, you can only use the first two methods, because `Window` has no corresponding HTML element. However, there's a specific group of events whose listeners can be added to the [<body>](/en-US/docs/Web/HTML/Reference/Elements/body) (or the deprecated [<frameset>](/en-US/docs/Web/HTML/Reference/Elements/frameset)) element that's owned by the `Window`'s document, using the second or third methods. These events are:

- `afterprint`
- `beforeprint`
- `beforeunload`
- `blur`
- `error`
- `focus`
- `hashchange`
- `languagechange`
- `load`
- `message`
- `messageerror`
- `offline`
- `online`
- `pagehide`
- `pagereveal`
- `pageshow`
- `pageswap`
- `popstate`
- `rejectionhandled`
- `resize`
- `scroll`
- `storage`
- `unhandledrejection`
- `unload`

This means the following are strictly equivalent:

js

```
window.onresize = (e) => console.log(e.currentTarget);
document.body.onresize = (e) => console.log(e.currentTarget);
```

html

```
<body onresize="console.log(event.currentTarget)"></body>
```

In all three cases, you see the `Window` object logged as `currentTarget`.

## [Specifications](#specifications)

Specification
[HTML# the-window-object](https://html.spec.whatwg.org/multipage/nav-history-apis.html#the-window-object)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Window/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/window/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWindow&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwindow%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWindow%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwindow%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe936e7271df947f25184a5ba8a21445bbd4d056c%0A*+Document+last+modified%3A+2025-12-13T02%3A55%3A18.000Z%0A%0A%3C%2Fdetails%3E)
