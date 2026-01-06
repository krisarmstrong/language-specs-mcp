Module[jdk.httpserver](../../../../module-summary.html)

# Package com.sun.net.httpserver

package com.sun.net.httpserverProvides a simple high-level Http server API, which can be used to build embedded HTTP servers. Both "http" and "https" are supported. The API provides a partial implementation of RFC [2616](https://www.ietf.org/rfc/rfc2616.txt) (HTTP 1.1) and RFC [2818](https://www.ietf.org/rfc/rfc2818.txt) (HTTP over TLS). Any HTTP functionality not provided by this API can be implemented by application code using the API. 

 The main components are: 

- the [HttpExchange](HttpExchange.html) class that describes a request and response pair,
- the [HttpHandler](HttpHandler.html) interface to handle incoming requests, plus the [HttpHandlers](HttpHandlers.html) class that provides useful handler implementations,
- the [HttpContext](HttpContext.html) class that maps a URI path to a `HttpHandler`,
- the [HttpServer](HttpServer.html) class to listen for connections and dispatch requests to handlers,
- the [Filter](Filter.html) class that allows pre- and post- processing of requests.

 The [SimpleFileServer](SimpleFileServer.html) class offers a simple HTTP-only file server (intended for testing, development and debugging purposes only). A default implementation is provided via the `jwebserver` tool. 

 Programmers must implement the [HttpHandler](HttpHandler.html) interface. This interface provides a callback which is invoked to handle incoming requests from clients. A HTTP request and its response is known as an exchange. HTTP exchanges are represented by the [HttpExchange](HttpExchange.html) class. The [HttpServer](HttpServer.html) class is used to listen for incoming TCP connections and it dispatches requests on these connections to handlers which have been registered with the server. 

 A minimal Http server example is shown below: 

```

   class MyHandler implements HttpHandler {
       public void handle(HttpExchange t) throws IOException {
           InputStream is = t.getRequestBody();
           read(is); // .. read the request body
           String response = "This is the response";
           t.sendResponseHeaders(200, response.length());
           OutputStream os = t.getResponseBody();
           os.write(response.getBytes());
           os.close();
       }
   }
   ...

   HttpServer server = HttpServer.create(new InetSocketAddress(8000), 0);
   server.createContext("/applications/myapp", new MyHandler());
   server.setExecutor(null); // creates a default executor
   server.start();
   
```

The example above creates a simple HttpServer which uses the calling application thread to invoke the handle() method for incoming http requests directed to port 8000, and to the path /applications/myapp/. 

 The [HttpExchange](HttpExchange.html) class encapsulates everything an application needs to process incoming requests and to generate appropriate responses. 

 Registering a handler with a HttpServer creates a [HttpContext](HttpContext.html) object and [Filter](Filter.html) objects can be added to the returned context. Filters are used to perform automatic pre- and post-processing of exchanges before they are passed to the exchange handler. 

 For sensitive information, a [HttpsServer](HttpsServer.html) can be used to process "https" requests secured by the SSL or TLS protocols. A HttpsServer must be provided with a [HttpsConfigurator](HttpsConfigurator.html) object, which contains an initialized [SSLContext](../../../../../java.base/javax/net/ssl/SSLContext.html). HttpsConfigurator can be used to configure the cipher suites and other SSL operating parameters. A simple example SSLContext could be created as follows: 

```

   char[] passphrase = "passphrase".toCharArray();
   KeyStore ks = KeyStore.getInstance("JKS");
   ks.load(new FileInputStream("testkeys"), passphrase);

   KeyManagerFactory kmf = KeyManagerFactory.getInstance("SunX509");
   kmf.init(ks, passphrase);

   TrustManagerFactory tmf = TrustManagerFactory.getInstance("SunX509");
   tmf.init(ks);

   SSLContext ssl = SSLContext.getInstance("TLS");
   ssl.init(kmf.getKeyManagers(), tmf.getTrustManagers(), null);
   
```

 In the example above, a keystore file called "testkeys", created with the keytool utility is used as a certificate store for client and server certificates. The following code shows how the SSLContext is then used in a HttpsConfigurator and how the SSLContext and HttpsConfigurator are linked to the HttpsServer. 

```

    server.setHttpsConfigurator (new HttpsConfigurator(sslContext) {
        public void configure (HttpsParameters params) {

        // get the remote address if needed
        InetSocketAddress remote = params.getClientAddress();

        SSLContext c = getSSLContext();

        // get the default parameters
        SSLParameters sslparams = c.getDefaultSSLParameters();
        if (remote.equals (...) ) {
            // modify the default set for client x
        }

        params.setSSLParameters(sslparams);
        // statement above could throw IAE if any params invalid.
        // eg. if app has a UI and parameters supplied by a user.

        }
    });
   
```

Since:1.6

- Related PackagesPackageDescription[com.sun.net.httpserver.spi](spi/package-summary.html)Provides a pluggable service provider interface, which allows the HTTP server implementation to be replaced with other implementations.
- All Classes and InterfacesInterfacesClassesEnum ClassesClassDescription[Authenticator](Authenticator.html)Authenticator represents an implementation of an HTTP authentication mechanism.[Authenticator.Failure](Authenticator.Failure.html)Indicates an authentication failure.[Authenticator.Result](Authenticator.Result.html)Base class for return type from [Authenticator.authenticate(HttpExchange)](Authenticator.html#authenticate(com.sun.net.httpserver.HttpExchange)) method.[Authenticator.Retry](Authenticator.Retry.html)Indicates an authentication must be retried.[Authenticator.Success](Authenticator.Success.html)Indicates an authentication has succeeded and the authenticated user [principal](HttpPrincipal.html) can be acquired by calling [Authenticator.Success.getPrincipal()](Authenticator.Success.html#getPrincipal()).[BasicAuthenticator](BasicAuthenticator.html)BasicAuthenticator provides an implementation of HTTP Basic authentication.[Filter](Filter.html)A filter used to pre- and post-process incoming requests.[Filter.Chain](Filter.Chain.html)A chain of filters associated with a [HttpServer](HttpServer.html).[Headers](Headers.html)HTTP request and response headers are represented by this class which implements the interface [Map](../../../../../java.base/java/util/Map.html)<[String](../../../../../java.base/java/lang/String.html), [List](../../../../../java.base/java/util/List.html) <[String](../../../../../java.base/java/lang/String.html)>>.[HttpContext](HttpContext.html)`HttpContext` represents a mapping between the root [URI](../../../../../java.base/java/net/URI.html) path of an application to a [HttpHandler](HttpHandler.html) which is invoked to handle requests destined for that path on the associated [HttpServer](HttpServer.html) or [HttpsServer](HttpsServer.html).[HttpExchange](HttpExchange.html)This class encapsulates a HTTP request received and a response to be generated in one exchange.[HttpHandler](HttpHandler.html)A handler which is invoked to process HTTP exchanges.[HttpHandlers](HttpHandlers.html)Implementations of [HttpHandler](HttpHandler.html) that implement various useful handlers, such as a static response handler, or a conditional handler that complements one handler with another.[HttpPrincipal](HttpPrincipal.html)Represents a user authenticated by HTTP Basic or Digest authentication.[HttpsConfigurator](HttpsConfigurator.html)This class is used to configure the https parameters for each incoming https connection on a [HttpsServer](HttpsServer.html).[HttpServer](HttpServer.html)This class implements a simple HTTP server.[HttpsExchange](HttpsExchange.html)This class encapsulates a HTTPS request received and a response to be generated in one exchange and defines the extensions to [HttpExchange](HttpExchange.html) that are specific to the HTTPS protocol.[HttpsParameters](HttpsParameters.html)Represents the set of parameters for each https connection negotiated with clients.[HttpsServer](HttpsServer.html)This class is an extension of [HttpServer](HttpServer.html) which provides support for HTTPS.[Request](Request.html)A view of the immutable request state of an HTTP exchange.[SimpleFileServer](SimpleFileServer.html)A simple HTTP file server and its components (intended for testing, development and debugging purposes only).[SimpleFileServer.OutputLevel](SimpleFileServer.OutputLevel.html)Describes the log message output level produced by the server when processing exchanges.
