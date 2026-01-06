Module[java.net.http](../../../module-summary.html)

# Package java.net.http

package java.net.http

## HTTP Client and WebSocket APIs

 Provides high-level client interfaces to HTTP (versions 1.1 and 2) and low-level client interfaces to WebSocket. The main types defined are: 

- [HttpClient](HttpClient.html)
- [HttpRequest](HttpRequest.html)
- [HttpResponse](HttpResponse.html)
- [WebSocket](WebSocket.html)

 The protocol-specific requirements are defined in the [Hypertext Transfer Protocol
 Version 2 (HTTP/2)](https://tools.ietf.org/html/rfc7540), the [Hypertext Transfer Protocol (HTTP/1.1)](https://tools.ietf.org/html/rfc2616), and [The WebSocket Protocol](https://tools.ietf.org/html/rfc6455). 

 In general, asynchronous tasks execute in either the thread invoking the operation, e.g. [sending](HttpClient.html#send(java.net.http.HttpRequest,java.net.http.HttpResponse.BodyHandler)) an HTTP request, or by the threads supplied by the client's [executor](HttpClient.html#executor()). Dependent tasks, those that are triggered by returned CompletionStages or CompletableFutures, that do not explicitly specify an executor, execute in the same [default executor](../../../../java.base/java/util/concurrent/CompletableFuture.html#defaultExecutor()) as that of `CompletableFuture`, or the invoking thread if the operation completes before the dependent task is registered. 

`CompletableFuture`s returned by this API will throw [UnsupportedOperationException](../../../../java.base/java/lang/UnsupportedOperationException.html) for their [obtrudeValue](../../../../java.base/java/util/concurrent/CompletableFuture.html#obtrudeValue(T)) and [obtrudeException](../../../../java.base/java/util/concurrent/CompletableFuture.html#obtrudeException(java.lang.Throwable)) methods. Invoking the [cancel](../../../../java.base/java/util/concurrent/CompletableFuture.html#cancel(boolean)) method on a `CompletableFuture` returned by this API may not interrupt the underlying operation, but may be useful to complete, exceptionally, dependent stages that have not already completed. 

 Unless otherwise stated, `null` parameter values will cause methods of all classes in this package to throw `NullPointerException`.

Since:11

- Related PackagesModulePackageDescription[java.base](../../../../java.base/module-summary.html)[java.net](../../../../java.base/java/net/package-summary.html)Provides the classes for implementing networking applications.[java.base](../../../../java.base/module-summary.html)[java.net.spi](../../../../java.base/java/net/spi/package-summary.html)Service-provider classes for the [java.net](../../../../java.base/java/net/package-summary.html) package.
- All Classes and InterfacesInterfacesClassesEnum ClassesException ClassesClassDescription[HttpClient](HttpClient.html)An HTTP Client.[HttpClient.Builder](HttpClient.Builder.html)A builder of [HTTP Clients](HttpClient.html).[HttpClient.Redirect](HttpClient.Redirect.html)Defines the automatic redirection policy.[HttpClient.Version](HttpClient.Version.html)The HTTP protocol version.[HttpConnectTimeoutException](HttpConnectTimeoutException.html)Thrown when a connection, over which an `HttpRequest` is intended to be sent, is not successfully established within a specified time period.[HttpHeaders](HttpHeaders.html)A read-only view of a set of HTTP headers.[HttpRequest](HttpRequest.html)An HTTP request.[HttpRequest.BodyPublisher](HttpRequest.BodyPublisher.html)A `BodyPublisher` converts high-level Java objects into a flow of byte buffers suitable for sending as a request body.[HttpRequest.BodyPublishers](HttpRequest.BodyPublishers.html)Implementations of [BodyPublisher](HttpRequest.BodyPublisher.html) that implement various useful publishers, such as publishing the request body from a String, or from a file.[HttpRequest.Builder](HttpRequest.Builder.html)A builder of [HTTP requests](HttpRequest.html).[HttpResponse](HttpResponse.html)<T>An HTTP response.[HttpResponse.BodyHandler](HttpResponse.BodyHandler.html)<T>A handler for response bodies.[HttpResponse.BodyHandlers](HttpResponse.BodyHandlers.html)Implementations of [BodyHandler](HttpResponse.BodyHandler.html) that implement various useful handlers, such as handling the response body as a String, or streaming the response body to a file.[HttpResponse.BodySubscriber](HttpResponse.BodySubscriber.html)<T>A `BodySubscriber` consumes response body bytes and converts them into a higher-level Java type.[HttpResponse.BodySubscribers](HttpResponse.BodySubscribers.html)Implementations of [BodySubscriber](HttpResponse.BodySubscriber.html) that implement various useful subscribers, such as converting the response body bytes into a String, or streaming the bytes to a file.[HttpResponse.PushPromiseHandler](HttpResponse.PushPromiseHandler.html)<T>A handler for push promises.[HttpResponse.ResponseInfo](HttpResponse.ResponseInfo.html)Initial response information supplied to a [BodyHandler](HttpResponse.BodyHandler.html) when a response is initially received and before the body is processed.[HttpTimeoutException](HttpTimeoutException.html)Thrown when a response is not received within a specified time period.[WebSocket](WebSocket.html)A WebSocket Client.[WebSocket.Builder](WebSocket.Builder.html)A builder of [WebSocket Clients](WebSocket.html).[WebSocket.Listener](WebSocket.Listener.html)The receiving interface of `WebSocket`.[WebSocketHandshakeException](WebSocketHandshakeException.html)Thrown when the opening handshake has failed.
