# Presentation API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPresentation_API&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The Presentation API lets a [user agent](/en-US/docs/Glossary/User_agent) (such as a Web browser) effectively display web content through large presentation devices such as projectors and network-connected televisions. Supported types of multimedia devices include both displays which are wired using HDMI, DVI, or the like, or wireless, using [DLNA](https://www.dlna.org/), [Chromecast](https://developers.google.com/cast/), [AirPlay](https://developer.apple.com/documentation/technologyoverviews/streaming), or [Miracast](https://www.wi-fi.org/applications).

In general, a web page uses the Presentation Controller API to specify the web content to be rendered on presentation device and initiate the presentation session. With Presentation Receiver API, the presenting web content obtains the session status. With providing both the controller page and the receiver one with a messaged-based channel, a Web developer can implement the interaction between these two pages.

Depending on the connection mechanism provided by the presentation device, any controller- and receiver page can be rendered by the same user agent, or by separated user agents.

- For 1-UA mode devices, both pages are loaded by the same user agent. However, rendering result of the receiver page will be sent to the presentation device via supported remote rendering protocol.
- For 2-UAs mode device, the receiver page is loaded directly on the presentation device. Controlling user agent communicates with presentation device via supported presentation control protocol, to control the presentation session and to transmit the message between two pages.

## In this article

- [Interfaces](#interfaces)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Interfaces](#interfaces)

[Presentation](/en-US/docs/Web/API/Presentation)

In controlling browsing context, the `Presentation` interface provides a mechanism to override the browser default behavior of launching presentation to external screen. In receiving browsing context, `Presentation` interface provides the access to the available presentation connections.

[PresentationRequest](/en-US/docs/Web/API/PresentationRequest)

Initiates or reconnects to a presentation made by a controlling browsing context.

[PresentationAvailability](/en-US/docs/Web/API/PresentationAvailability)

A [PresentationAvailability](/en-US/docs/Web/API/PresentationAvailability) object is associated with available presentation displays and represents the presentation display availability for a presentation request.

[PresentationConnectionAvailableEvent](/en-US/docs/Web/API/PresentationConnectionAvailableEvent)

The `PresentationConnectionAvailableEvent` is fired on a [PresentationRequest](/en-US/docs/Web/API/PresentationRequest) when a connection associated with the object is created.

[PresentationConnection](/en-US/docs/Web/API/PresentationConnection)

Each presentation connection is represented by a [PresentationConnection](/en-US/docs/Web/API/PresentationConnection) object.

[PresentationConnectionCloseEvent](/en-US/docs/Web/API/PresentationConnectionCloseEvent)

A `PresentationConnectionCloseEvent` is fired when a presentation connection enters a `closed` state.

[PresentationReceiver](/en-US/docs/Web/API/PresentationReceiver)

The [PresentationReceiver](/en-US/docs/Web/API/PresentationReceiver) allows a receiving browsing context to access the controlling browsing contexts and communicate with them.

[PresentationConnectionList](/en-US/docs/Web/API/PresentationConnectionList)

`PresentationConnectionList` represents the collection of non-terminated presentation connections. It is also a monitor for the event of new available presentation connection.

## [Example](#example)

Example codes below highlight the usage of main features of the Presentation API: `controller.html` implements the controller and `presentation.html` implements the presentation. Both pages are served from the domain `https://example.org` (`https://example.org/controller.html` and `https://example.org/presentation.html`). These examples assume that the controlling page is managing one presentation at a time. Please refer to the comments in the code examples for further details.

### [Monitor availability of presentation displays](#monitor_availability_of_presentation_displays)

In `controller.html`:

html

```
<button id="presentBtn" class="hidden">Present</button>
```

css

```
.hidden {
  display: none;
}
```

js

```
// The Present button is visible if at least one presentation display is available
const presentBtn = document.getElementById("presentBtn");

// It is also possible to use relative presentation URL e.g. "presentation.html"
const presUrls = [
  "https://example.com/presentation.html",
  "https://example.net/alternate.html",
];

// Show or hide present button depending on display availability
const handleAvailabilityChange = (available) => {
  if (available) {
    presentBtn.classList.remove("hidden");
  } else {
    presentBtn.classList.add("hidden");
  }
};

// Promise is resolved as soon as the presentation display availability is known.
const request = new PresentationRequest(presUrls);
request
  .getAvailability()
  .then((availability) => {
    // availability.value may be kept up-to-date by the controlling UA as long
    // as the availability object is alive. It is advised for the web developers
    // to discard the object as soon as it's not needed.
    handleAvailabilityChange(availability.value);
    availability.onchange = () => {
      handleAvailabilityChange(availability.value);
    };
  })
  .catch(() => {
    // Availability monitoring is not supported by the platform, so discovery of
    // presentation displays will happen only after request.start() is called.
    // Pretend the devices are available for simplicity; or, one could implement
    // a third state for the button.
    handleAvailabilityChange(true);
  });
```

### [Starting a new presentation](#starting_a_new_presentation)

In `controller.html`:

js

```
presentBtn.onclick = () => {
  // Start new presentation.
  request
    .start()
    // The connection to the presentation will be passed to setConnection on success.
    .then(setConnection);
  // Otherwise, the user canceled the selection dialog or no screens were found.
};
```

### [Reconnect to a presentation](#reconnect_to_a_presentation)

In the `controller.html` file:

html

```
<button id="reconnectBtn" class="hidden">Reconnect</button>
```

js

```
const reconnect = () => {
  const presId = localStorage.getItem("presId");
  // presId is mandatory when reconnecting to a presentation.
  if (presId) {
    request
      .reconnect(presId)
      // The new connection to the presentation will be passed to
      // setConnection on success.
      .then(setConnection);
    // No connection found for presUrl and presId, or an error occurred.
  }
};
// On navigation of the controller, reconnect automatically.
reconnect();
// Or allow manual reconnection.
reconnectBtn.onclick = reconnect;
```

### [Presentation initiation by the controlling UA](#presentation_initiation_by_the_controlling_ua)

In the `controller.html` file:

js

```
navigator.presentation.defaultRequest = new PresentationRequest(presUrls);
navigator.presentation.defaultRequest.onconnectionavailable = (evt) => {
  setConnection(evt.connection);
};
```

Setting `presentation.defaultRequest` allows the page to specify the `PresentationRequest` to use when the controlling UA initiates a presentation.

### [Monitor connection's state and exchange data](#monitor_connections_state_and_exchange_data)

In `controller.html`:

html

```
<button id="disconnectBtn" class="hidden">Disconnect</button>
<button id="stopBtn" class="hidden">Stop</button>
<button id="reconnectBtn" class="hidden">Reconnect</button>
```

js

```
let connection;

// The Disconnect and Stop buttons are visible if there is a connected presentation
const stopBtn = document.querySelector("#stopBtn");
const reconnectBtn = document.querySelector("#reconnectBtn");
const disconnectBtn = document.querySelector("#disconnectBtn");

stopBtn.onclick = () => {
  connection?.terminate();
};

disconnectBtn.onclick = () => {
  connection?.close();
};

function setConnection(newConnection) {
  // Disconnect from existing presentation, if not attempting to reconnect
  if (
    connection &&
    connection !== newConnection &&
    connection.state !== "closed"
  ) {
    connection.onclose = undefined;
    connection.close();
  }

  // Set the new connection and save the presentation ID
  connection = newConnection;
  localStorage.setItem("presId", connection.id);

  function showConnectedUI() {
    // Allow the user to disconnect from or terminate the presentation
    stopBtn.classList.remove("hidden");
    disconnectBtn.classList.remove("hidden");
    reconnectBtn.classList.add("hidden");
  }

  function showDisconnectedUI() {
    disconnectBtn.classList.add("hidden");
    stopBtn.classList.add("hidden");
    if (localStorage.getItem("presId")) {
      // If there is a presId in localStorage, allow the user to reconnect
      reconnectBtn.classList.remove("hidden");
    } else {
      reconnectBtn.classList.add("hidden");
    }
  }

  // Monitor the connection state
  connection.onconnect = () => {
    showConnectedUI();

    // Register message handler
    connection.onmessage = (message) => {
      console.log(`Received message: ${message.data}`);
    };

    // Send initial message to presentation page
    connection.send("Say hello");
  };

  connection.onclose = () => {
    connection = null;
    showDisconnectedUI();
  };

  connection.onterminate = () => {
    localStorage.removeItem("presId");
    connection = null;
    showDisconnectedUI();
  };
}
```

### [Monitor available connection(s) and say hello](#monitor_available_connections_and_say_hello)

In `presentation.html`:

js

```
const addConnection = (connection) => {
  connection.onmessage = (message) => {
    if (message.data === "Say hello") connection.send("hello");
  };
};

navigator.presentation.receiver.connectionList.then((list) => {
  list.connections.forEach((connection) => {
    addConnection(connection);
  });
  list.onconnectionavailable = (evt) => {
    addConnection(evt.connection);
  };
});
```

### [Passing locale information with a message](#passing_locale_information_with_a_message)

In the `controller.html` file:

html

```
connection.send('{"string": "你好，世界!", "lang": "zh-CN"}');
connection.send('{"string": "こんにちは、世界!", "lang": "ja"}');
connection.send('{"string": "안녕하세요, 세계!", "lang": "ko"}');
connection.send('{"string": "Hello, world!", "lang": "en-US"}');
```

In the `presentation.html` file:

js

```
connection.onmessage = (message) => {
  const messageObj = JSON.parse(message.data);
  const spanElt = document.createElement("SPAN");
  spanElt.lang = messageObj.lang;
  spanElt.textContent = messageObj.string;
  document.body.appendChild(spanElt);
};
```

## [Specifications](#specifications)

Specification
[Presentation API# interface-presentation](https://w3c.github.io/presentation-api/#interface-presentation)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

[Presentation API polyfill](https://mediascape.github.io/presentation-api-polyfill/) contains a JavaScript polyfill of the [Presentation API](https://w3c.github.io/presentation-api/) specification under standardization within the [Second Screen Working Group](https://www.w3.org/2014/secondscreen/) at W3C. The polyfill is mostly intended for exploring how the Presentation API may be implemented on top of different presentation mechanisms.

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 19, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Presentation_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/presentation_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPresentation_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpresentation_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPresentation_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpresentation_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2e427c5c185433c5a6612c63bf877753a5fedc99%0A*+Document+last+modified%3A+2025-09-19T15%3A47%3A25.000Z%0A%0A%3C%2Fdetails%3E)
