Introducing HTTP Tracing - The Go Programming Language/[Skip to Main Content](#main-content)

- [Why Go arrow_drop_down](#) Press Enter to activate/deactivate dropdown 

  - [Case Studies](/solutions/case-studies)

Common problems companies solve with Go

  - [Use Cases](/solutions/use-cases)

Stories about how and why companies use Go

  - [Security](/security/)

How Go can help keep you secure by default

- [Learn](/learn/) Press Enter to activate/deactivate dropdown 
- [Docs arrow_drop_down](#) Press Enter to activate/deactivate dropdown 

  - [Go Spec](/ref/spec)

The official Go language specification

  - [Go User Manual](/doc)

A complete introduction to building software with Go

  - [Standard library](https://pkg.go.dev/std)

Reference documentation for Go's standard library

  - [Release Notes](/doc/devel/release)

Learn what's new in each Go release

  - [Effective Go](/doc/effective_go)

Tips for writing clear, performant, and idiomatic Go code

- [Packages](https://pkg.go.dev) Press Enter to activate/deactivate dropdown 
- [Community arrow_drop_down](#) Press Enter to activate/deactivate dropdown 

  - [Recorded Talks](/talks/)

Videos from prior events

  - [Meetups
                           open_in_new](https://www.meetup.com/pro/go)

Meet other local Go developers

  - [Conferences
                           open_in_new](/wiki/Conferences)

Learn and network with Go developers from around the world

  - [Go blog](/blog)

The Go project's official blog.

  - [Go project](/help)

Get help and stay informed from Go

  -  Get connected 

https://groups.google.com/g/golang-nutshttps://github.com/golanghttps://twitter.com/golanghttps://www.reddit.com/r/golang/https://invite.slack.golangbridge.org/https://stackoverflow.com/tags/go

/

- [Why Go navigate_next](#)[navigate_beforeWhy Go](#)

  - [Case Studies](/solutions/case-studies)
  - [Use Cases](/solutions/use-cases)
  - [Security](/security/)

- [Learn](/learn/)
- [Docs navigate_next](#)[navigate_beforeDocs](#)

  - [Go Spec](/ref/spec)
  - [Go User Manual](/doc)
  - [Standard library](https://pkg.go.dev/std)
  - [Release Notes](/doc/devel/release)
  - [Effective Go](/doc/effective_go)

- [Packages](https://pkg.go.dev)
- [Community navigate_next](#)[navigate_beforeCommunity](#)

  - [Recorded Talks](/talks/)
  - [Meetups
                           open_in_new](https://www.meetup.com/pro/go)
  - [Conferences
                           open_in_new](/wiki/Conferences)
  - [Go blog](/blog)
  - [Go project](/help)
  - Get connectedhttps://groups.google.com/g/golang-nutshttps://github.com/golanghttps://twitter.com/golanghttps://www.reddit.com/r/golang/https://invite.slack.golangbridge.org/https://stackoverflow.com/tags/go

# [The Go Blog](/blog/)

# Introducing HTTP Tracing

 Jaana Burcu Dogan
 4 October 2016 

## Introduction

In Go 1.7 we introduced HTTP tracing, a facility to gather fine-grained information throughout the lifecycle of an HTTP client request. Support for HTTP tracing is provided by the [net/http/httptrace](/pkg/net/http/httptrace/) package. The collected information can be used for debugging latency issues, service monitoring, writing adaptive systems, and more.

## HTTP events

The `httptrace` package provides a number of hooks to gather information during an HTTP round trip about a variety of events. These events include:

- Connection creation
- Connection reuse
- DNS lookups
- Writing the request to the wire
- Reading the response

## Tracing events

You can enable HTTP tracing by putting an [*httptrace.ClientTrace](/pkg/net/http/httptrace/#ClientTrace) containing hook functions into a request’s [context.Context](/pkg/context/#Context). Various [http.RoundTripper](/pkg/net/http/#RoundTripper) implementations report the internal events by looking for context’s `*httptrace.ClientTrace` and calling the relevant hook functions.

The tracing is scoped to the request’s context and users should put a `*httptrace.ClientTrace` to the request context before they start a request.

```
    req, _ := http.NewRequest("GET", "http://example.com", nil)
    trace := &httptrace.ClientTrace{
        DNSDone: func(dnsInfo httptrace.DNSDoneInfo) {
            fmt.Printf("DNS Info: %+v\n", dnsInfo)
        },
        GotConn: func(connInfo httptrace.GotConnInfo) {
            fmt.Printf("Got Conn: %+v\n", connInfo)
        },
    }
    req = req.WithContext(httptrace.WithClientTrace(req.Context(), trace))
    if _, err := http.DefaultTransport.RoundTrip(req); err != nil {
        log.Fatal(err)
    }
```

During a round trip, `http.DefaultTransport` will invoke each hook as an event happens. The program above will print the DNS information as soon as the DNS lookup is complete. It will similarly print connection information when a connection is established to the request’s host.

## Tracing with http.Client

The tracing mechanism is designed to trace the events in the lifecycle of a single `http.Transport.RoundTrip`. However, a client may make multiple round trips to complete an HTTP request. For example, in the case of a URL redirection, the registered hooks will be called as many times as the client follows HTTP redirects, making multiple requests. Users are responsible for recognizing such events at the `http.Client` level. The program below identifies the current request by using an `http.RoundTripper` wrapper.

```
package main

import (
    "fmt"
    "log"
    "net/http"
    "net/http/httptrace"
)

// transport is an http.RoundTripper that keeps track of the in-flight
// request and implements hooks to report HTTP tracing events.
type transport struct {
    current *http.Request
}

// RoundTrip wraps http.DefaultTransport.RoundTrip to keep track
// of the current request.
func (t *transport) RoundTrip(req *http.Request) (*http.Response, error) {
    t.current = req
    return http.DefaultTransport.RoundTrip(req)
}

// GotConn prints whether the connection has been used previously
// for the current request.
func (t *transport) GotConn(info httptrace.GotConnInfo) {
    fmt.Printf("Connection reused for %v? %v\n", t.current.URL, info.Reused)
}

func main() {
    t := &transport{}

    req, _ := http.NewRequest("GET", "https://google.com", nil)
    trace := &httptrace.ClientTrace{
        GotConn: t.GotConn,
    }
    req = req.WithContext(httptrace.WithClientTrace(req.Context(), trace))

    client := &http.Client{Transport: t}
    if _, err := client.Do(req); err != nil {
        log.Fatal(err)
    }
}
```

The program will follow the redirect of google.com to [www.google.com](http://www.google.com) and will output:

```
Connection reused for https://google.com? false
Connection reused for https://www.google.com/? false
```

The Transport in the `net/http` package supports tracing of both HTTP/1 and HTTP/2 requests.

If you are an author of a custom `http.RoundTripper` implementation, you can support tracing by checking the request context for an `*httptest.ClientTrace` and invoking the relevant hooks as the events occur.

## Conclusion

HTTP tracing is a valuable addition to Go for those who are interested in debugging HTTP request latency and writing tools for network debugging for outbound traffic. By enabling this new facility, we hope to see HTTP debugging, benchmarking and visualization tools from the community — such as [httpstat](https://github.com/davecheney/httpstat).

Next article: [Seven years of Go](/blog/7years)
Previous article: [Using Subtests and Sub-benchmarks](/blog/subtests)
[Blog Index](/blog/all)[Why Go](/solutions/)[Use Cases](/solutions/use-cases)[Case Studies](/solutions/case-studies)[Get Started](/learn/)[Playground](/play)[Tour](/tour/)[Stack Overflow](https://stackoverflow.com/questions/tagged/go?tab=Newest)[Help](/help/)[Packages](https://pkg.go.dev)[Standard Library](/pkg/)[About Go Packages](https://pkg.go.dev/about)[About](/project)[Download](/dl/)[Blog](/blog/)[Issue Tracker](https://github.com/golang/go/issues)[Release Notes](/doc/devel/release)[Brand Guidelines](/brand)[Code of Conduct](/conduct)[Connect](https://www.twitter.com/golang)[Twitter](https://www.twitter.com/golang)[GitHub](https://github.com/golang)[Slack](https://invite.slack.golangbridge.org/)[r/golang](https://reddit.com/r/golang)[Meetup](https://www.meetup.com/pro/go)[Golang Weekly](https://golangweekly.com/) Opens in new window. 

- [Copyright](/copyright)
- [Terms of Service](/tos)
- [Privacy Policy](http://www.google.com/intl/en/policies/privacy/)
- [Report an Issue](/s/website-issue)
- 

https://google.comgo.dev uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)Okay
