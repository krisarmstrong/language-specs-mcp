Cookie Store API Standardhttps://whatwg.org/

# Cookie Store API

Living Standard — Last Updated 11 December 2025

Participate: [GitHub whatwg/cookiestore](https://github.com/whatwg/cookiestore) ([new issue](https://github.com/whatwg/cookiestore/issues/new/choose), [open issues](https://github.com/whatwg/cookiestore/issues)) [Chat on Matrix](https://whatwg.org/chat)Commits: [GitHub whatwg/cookiestore/commits](https://github.com/whatwg/cookiestore/commits)[Snapshot as of this commit](/commit-snapshots/7ccd2e9abd0779cf702f4f13ea07fc45efc72349/)[@cookiestoreapi](https://twitter.com/cookiestoreapi)Tests: [web-platform-tests cookiestore/](https://github.com/web-platform-tests/wpt/tree/master/cookiestore) ([ongoing work](https://github.com/web-platform-tests/wpt/labels/cookiestore)) Translations (non-normative): [简体中文](https://htmlspecs.com/cookiestore/)[日本語](https://jp.htmlspecs.com/cookiestore/)[한국어](https://ko.htmlspecs.com/cookiestore/)

## Abstract

An asynchronous JavaScript cookies API for documents and service workers.

## Table of Contents

1. [1 Introduction](#intro)

  1. [1.1 Alternative to document.cookie](#intro-proposed-change)
  2. [1.2 Summary](#intro-summary)
  3. [1.3 Querying cookies](#intro-query)
  4. [1.4 Modifying cookies](#intro-modify)
  5. [1.5 Monitoring cookies](#intro-monitor)

2. [2 Concepts](#concepts)

  1. [2.1 Cookie](#cookie-concept)
  2. [2.2 Cookie store](#cookie-store--concept)
  3. [2.3 Extensions to Service Workers](#service-worker-extensions)

3. [3 The CookieStore interface](#CookieStore)

  1. [3.1 The get() method](#CookieStore-get)
  2. [3.2 The getAll() method](#CookieStore-getAll)
  3. [3.3 The set() method](#CookieStore-set)
  4. [3.4 The delete() method](#CookieStore-delete)

4. [4 The CookieStoreManager interface](#CookieStoreManager)

  1. [4.1 The subscribe() method](#CookieStoreManager-subscribe)
  2. [4.2 The getSubscriptions() method](#CookieStoreManager-getSubscriptions)
  3. [4.3 The unsubscribe() method](#CookieStoreManager-unsubscribe)
  4. [4.4 The ServiceWorkerRegistration interface](#ServiceWorkerRegistration)

5. [5 Event interfaces](#event-interfaces)

  1. [5.1 The CookieChangeEvent interface](#CookieChangeEvent)
  2. [5.2 The ExtendableCookieChangeEvent interface](#ExtendableCookieChangeEvent)

6. [6 Global interfaces](#globals)

  1. [6.1 The Window interface](#Window)
  2. [6.2 The ServiceWorkerGlobalScope interface](#ServiceWorkerGlobalScope)

7. [7 Algorithms](#algorithms)

  1. [7.1 Query cookies](#query-cookies-algorithm)
  2. [7.2 Set a cookie](#set-cookie-algorithm)
  3. [7.3 Delete a cookie](#delete-cookie-algorithm)
  4. [7.4 Process changes](#process-changes)

8. [8 Security considerations](#security)

  1. [8.1 Gotcha!](#gotcha)
  2. [8.2 Restrict?](#restrict)
  3. [8.3 Secure cookies](#secure-cookies)
  4. [8.4 Surprises](#surprises)
  5. [8.5 Prefixes](#prefixes)
  6. [8.6 URL scoping](#url-scoping)
  7. [8.7 Cookie aversion](#aversion)

9. [9 Privacy considerations](#privacy)

  1. [9.1 Clear cookies](#clear-cookies)

10. [Acknowledgments](#acknowledgements)
11. [Intellectual property rights](#ipr)
12. [Index](#index)

  1. [Terms defined by this specification](#index-defined-here)
  2. [Terms defined by reference](#index-defined-elsewhere)

13. [References](#references)

  1. [Normative References](#normative)

14. [IDL Index](#idl-index)

## 1. Introduction#intro

This section is non-normative.

This standard defines an asynchronous cookie API for scripts running in HTML documents and [service workers](#biblio-service-workers).

[HTTP cookies](#biblio-rfc6265bis-14) have, since their origins at Netscape [(documentation preserved by archive.org)](https://web.archive.org/web/0/http://wp.netscape.com/newsref/std/cookie_spec.html), provided a [valuable state-management mechanism](https://montulli.blogspot.com/2013/05/the-reasoning-behind-web-cookies.html) for the web.

The synchronous single-threaded script-level [document.cookie](https://html.spec.whatwg.org/multipage/dom.html#dom-document-cookie) interface to cookies has been a source of [complexity and performance woes](https://lists.w3.org/Archives/Public/public-whatwg-archive/2009Sep/0083.html) further exacerbated by the move in many browsers from:

- 

a single browser process,

- 

a single-threaded event loop model, and

- 

no general expectation of responsiveness for scripted event handling while processing cookie operations

… to the modern web which strives for smoothly responsive high performance:

- 

in multiple browser processes,

- 

with a multithreaded, multiple-event loop model, and

- 

with an expectation of responsiveness on human-reflex time scales.

On the modern web a cookie operation in one part of a web application cannot block:

- 

the rest of the web application,

- 

the rest of the web origin, or

- 

the browser as a whole.

Newer parts of the web built in service workers [need access to cookies too](https://github.com/w3c/ServiceWorker/issues/707) but cannot use the synchronous, blocking [document.cookie](https://html.spec.whatwg.org/multipage/dom.html#dom-document-cookie) interface at all as they both have no document and also cannot block the event loop as that would interfere with handling of unrelated events.

### 1.1. Alternative to `document.cookie`#intro-proposed-change

Today writing a cookie means blocking your event loop while waiting for the browser to synchronously update the cookie jar with a carefully-crafted cookie string in `Set-Cookie` format:

#example-e33babf4

```
document.cookie =
  '__Secure-COOKIENAME=cookie-value' +
  '; Path=/' +
  '; expires=Fri, 12 Aug 2016 23:05:17 GMT' +
  '; Secure' +
  '; Domain=example.org';
// now we could assume the write succeeded, but since
// failure is silent it is difficult to tell, so we
// read to see whether the write succeeded
var successRegExp =
  /(^|; ?)__Secure-COOKIENAME=cookie-value(;|$)/;
if (String(document.cookie).match(successRegExp)) {
  console.log('It worked!');
} else {
  console.error('It did not work, and we do not know why');
}
```

What if you could instead write:

#example-e2699daa

```
const one_day_ms = 24 * 60 * 60 * 1000;
cookieStore.set(
  {
    name: '__Secure-COOKIENAME',
    value: 'cookie-value',
    expires: Date.now() + one_day_ms,
    domain: 'example.org'
  }).then(function() {
    console.log('It worked!');
  }, function(reason) {
    console.error(
      'It did not work, and this is why:',
      reason);
  });
// Meanwhile we can do other things while waiting for
// the cookie store to process the write...
```

This also has the advantage of not relying on document and not blocking, which together make it usable from [service workers](https://w3c.github.io/ServiceWorker/#dfn-service-worker), which otherwise do not have cookie access from script.

This standard also includes a power-efficient monitoring API to replace `setTimeout`-based polling cookie monitors with cookie change observers.

### 1.2. Summary#intro-summary

In short, this API offers the following functionality:

- 

[write](#intro-modify) (or "set") and delete (or "expire") cookies

- 

[read](#intro-query) (or "get") [script-visible](#script-visible) cookies

  - 

... including for specified in-scope request paths in [service worker](#biblio-service-workers) contexts

- 

[monitor](#intro-monitor)[script-visible](#script-visible) cookies for changes using `CookieChangeEvent`

  - 

... in long-running script contexts (e.g. `document`)

  - 

... for script-supplied in-scope request paths in [service worker](#biblio-service-workers) contexts

### 1.3. Querying cookies#intro-query

Both [documents](https://dom.spec.whatwg.org/#concept-document) and [service workers](https://w3c.github.io/ServiceWorker/#dfn-service-worker) access the same query API, via the [cookieStore](#dom-window-cookiestore) property on the [global object](#globals).

The [get()](#dom-cookiestore-get-options) and [getAll()](#dom-cookiestore-getall-options) methods on [CookieStore](#cookiestore) are used to query cookies. Both methods return [Promise](https://webidl.spec.whatwg.org/#idl-promise)s. Both methods take the same arguments, which can be either:

- 

a name, or

- 

a dictionary of options (optional for [getAll()](#dom-cookiestore-getall-options))

The [get()](#dom-cookiestore-get-options) method is essentially a form of [getAll()](#dom-cookiestore-getall-options) that only returns the first result.

#example-75b57f43 Reading a cookie: 

```
try {
  const cookie = await cookieStore.get('session_id');
  if (cookie) {
    console.log(`Found ${cookie.name} cookie: ${cookie.value}`);
  } else {
    console.log('Cookie not found');
  }
} catch (e) {
  console.error(`Cookie store error: ${e}`);
}
```

#example-9453f9c5 Reading multiple cookies: 

```
try {
  const cookies = await cookieStore.getAll('session_id'});
  for (const cookie of cookies)
    console.log(`Result: ${cookie.name} = ${cookie.value}`);
} catch (e) {
  console.error(`Cookie store error: ${e}`);
}
```

[Service workers](https://w3c.github.io/ServiceWorker/#dfn-service-worker) can obtain the list of cookies that would be sent by a [fetch](https://fetch.spec.whatwg.org/#concept-fetch) to any URL under their [scope](https://w3c.github.io/ServiceWorker/#dfn-scope-url).

#example-2f07df9d Read the cookies for a specific URL (in a [service worker](https://w3c.github.io/ServiceWorker/#dfn-service-worker)): 

```
await cookieStore.getAll({url: '/admin'});
```

[Documents](https://dom.spec.whatwg.org/#concept-document) can only obtain the cookies at their current URL. In other words, the only valid [url](#dom-cookiestoregetoptions-url) value in [Document](https://dom.spec.whatwg.org/#concept-document) contexts is the document’s URL.

The objects returned by [get()](#dom-cookiestore-get-options) and [getAll()](#dom-cookiestore-getall-options) contain all the relevant information in the cookie store, not just the [name](#cookie-name) and the [value](#cookie-value) as in the older [document.cookie](https://html.spec.whatwg.org/multipage/dom.html#dom-document-cookie) API.

#example-74bb82cb Accessing all the cookie data: 

```
await cookie = cookieStore.get('session_id');
console.log(`Cookie scope - Domain: ${cookie.domain} Path: ${cookie.path}`);
if (cookie.expires === null) {
  console.log('Cookie expires at the end of the session');
} else {
  console.log(`Cookie expires at: ${cookie.expires}`);
}
if (cookie.secure)
  console.log('The cookie is restricted to secure origins');
```

### 1.4. Modifying cookies#intro-modify

Both [documents](https://dom.spec.whatwg.org/#concept-document) and [service workers](https://w3c.github.io/ServiceWorker/#dfn-service-worker) access the same modification API, via the [cookieStore](#dom-window-cookiestore) property on the [global object](#globals).

Cookies are created or modified (written) using the [set()](#dom-cookiestore-set) method.

#example-cf76b712 Write a cookie: 

```
try {
  await cookieStore.set('opted_out', '1');
} catch (e) {
  console.error(`Failed to set cookie: ${e}`);
}
```

The [set()](#dom-cookiestore-set) call above is shorthand for using an options dictionary, as follows:

```
await cookieStore.set({
  name: 'opted_out',
  value: '1',
  expires: null,  // session cookie

  // By default, domain is set to null which means the scope is locked at the current domain.
  domain: null,
  path: '/'
});
```

Cookies are deleted (expired) using the [delete()](#dom-cookiestore-delete) method.

#example-7990c896 Delete a cookie: 

```
try {
  await cookieStore.delete('session_id');
} catch (e) {
  console.error(`Failed to delete cookie: ${e}`);
}
```

Under the hood, deleting a cookie is done by changing the cookie’s expiration date to the past, which still works.

#example-e0eca546 Deleting a cookie by changing the expiry date: 

```
try {
  const one_day_ms = 24 * 60 * 60 * 1000;
  await cookieStore.set({
    name: 'session_id',
    value: 'value will be ignored',
    expires: Date.now() - one_day_ms });
} catch (e) {
  console.error(`Failed to delete cookie: ${e}`);
}
```

### 1.5. Monitoring cookies#intro-monitor

To avoid polling, it is possible to observe changes to cookies.

In [documents](https://dom.spec.whatwg.org/#concept-document), `change` events are fired for all relevant cookie changes.

#example-7e599641 Register for `change` events in documents: 

```
cookieStore.addEventListener('change', event => {
  console.log(`${event.changed.length} changed cookies`);
  for (const cookie in event.changed)
    console.log(`Cookie ${cookie.name} changed to ${cookie.value}`);

  console.log(`${event.deleted.length} deleted cookies`);
  for (const cookie in event.deleted)
    console.log(`Cookie ${cookie.name} deleted`);
});
```

In [service workers](https://w3c.github.io/ServiceWorker/#dfn-service-worker), `cookiechange` events are fired against the global scope, but an explicit subscription is required, associated with the service worker’s registration.

#example-1ce710fe Register for `cookiechange` events in a service worker: 

```
self.addEventListener('activate', (event) => {
  event.waitUntil(async () => {
    // Snapshot current state of subscriptions.
    const subscriptions = await self.registration.cookies.getSubscriptions();

    // Clear any existing subscriptions.
    await self.registration.cookies.unsubscribe(subscriptions);

    await self.registration.cookies.subscribe([
      {
        name: 'session_id',  // Get change events for cookies named session_id.
      }
    ]);
  });
});

self.addEventListener('cookiechange', event => {
  // The event has |changed| and |deleted| properties with
  // the same semantics as the Document events.
  console.log(`${event.changed.length} changed cookies`);
  console.log(`${event.deleted.length} deleted cookies`);
});
```

Calls to [subscribe()](#dom-cookiestoremanager-subscribe) are cumulative, so that independently maintained modules or libraries can set up their own subscriptions. As expected, a [service worker](https://w3c.github.io/ServiceWorker/#dfn-service-worker)’s subscriptions are persisted for with the [service worker registration](https://w3c.github.io/ServiceWorker/#dfn-service-worker-registration).

Subscriptions can use the same options as [get()](#dom-cookiestore-get-options) and [getAll()](#dom-cookiestore-getall-options). The complexity of fine-grained subscriptions is justified by the cost of dispatching an irrelevant cookie change event to a [service worker](https://w3c.github.io/ServiceWorker/#dfn-service-worker), which is much higher than the cost of dispatching an equivalent event to a [Window](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window). Specifically, dispatching an event to a [service worker](https://w3c.github.io/ServiceWorker/#dfn-service-worker) might require waking up the worker, which has a significant impact on battery life.

The [getSubscriptions()](#dom-cookiestoremanager-getsubscriptions) allows a [service worker](https://w3c.github.io/ServiceWorker/#dfn-service-worker) to introspect the subscriptions that have been made.

#example-5e735d9a Checking change subscriptions: 

```
const subscriptions = await self.registration.cookies.getSubscriptions();
for (const sub of subscriptions) {
  console.log(sub.name, sub.url);
}
```

## 2. Concepts#concepts

### 2.1. Cookie#cookie-concept

A cookie is normatively defined for user agents by [Cookies § User Agent Requirements](https://tools.ietf.org/html/draft-ietf-httpbis-rfc6265bis-14#name-user-agent-requirements).

 Per [Cookies § Storage Model](https://tools.ietf.org/html/draft-ietf-httpbis-rfc6265bis-14#name-storage-model), a [cookie](#cookie) has the following fields: name, value, domain, path, http-only-flag. 

To normalize a cookie name or value given a [string](https://infra.spec.whatwg.org/#string)input: remove all U+0009 TAB and U+0020 SPACE that are at the start or end of input.

A cookie is script-visible when it is in-scope and its [http-only-flag](#cookie-http-only-flag) is unset. This is more formally enforced in the processing model, which consults [Cookies § Retrieval Model](https://tools.ietf.org/html/draft-ietf-httpbis-rfc6265bis-14#name-retrieval-model) at appropriate points.

A cookie is also subject to certain size limits. Per [Cookies § Storage Model](https://tools.ietf.org/html/draft-ietf-httpbis-rfc6265bis-14#name-storage-model):

- 

The combined lengths of the name and value fields must not be greater than 4096 [bytes](https://infra.spec.whatwg.org/#byte) (the maximum name/value pair size).

- 

The length of every field except the name and value fields must not be greater than 1024 [bytes](https://infra.spec.whatwg.org/#byte) (the maximum attribute value size).

[Cookie](#cookie) attribute-values are stored as [byte sequences](https://infra.spec.whatwg.org/#byte-sequence), not strings. 

### 2.2. Cookie store#cookie-store--concept

A cookie store is normatively defined for user agents by [Cookies § User Agent Requirements](https://tools.ietf.org/html/draft-ietf-httpbis-rfc6265bis-14#name-user-agent-requirements).

When any of the following conditions occur for a [cookie store](#cookie-store), perform the steps to [process cookie changes](#process-cookie-changes).

- 

A newly-created [cookie](#cookie) is inserted into the [cookie store](#cookie-store).

- 

A user agent evicts expired [cookies](#cookie) from the [cookie store](#cookie-store).

- 

A user agent removes excess [cookies](#cookie) from the [cookie store](#cookie-store).

### 2.3. Extensions to Service Workers#service-worker-extensions

[[Service-Workers]](#biblio-service-workers) defines [service worker registration](https://w3c.github.io/ServiceWorker/#dfn-service-worker-registration), which this specification extends.

A [service worker registration](https://w3c.github.io/ServiceWorker/#dfn-service-worker-registration) has an associated cookie change subscription list which is a [list](https://infra.spec.whatwg.org/#list); each member is a cookie change subscription. A [cookie change subscription](#cookie-change-subscription) is  a [tuple](https://infra.spec.whatwg.org/#tuple) of name and url. 

## 3. The [CookieStore](#cookiestore) interface#CookieStore

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=(ServiceWorker,Window),
 SecureContexthttps://webidl.spec.whatwg.org/#SecureContext]
interface CookieStore : EventTargethttps://dom.spec.whatwg.org/#eventtarget {
  Promisehttps://webidl.spec.whatwg.org/#idl-promise<CookieListItem#dictdef-cookielistitem?> get#dom-cookiestore-get(USVStringhttps://webidl.spec.whatwg.org/#idl-USVString name);
  Promisehttps://webidl.spec.whatwg.org/#idl-promise<CookieListItem#dictdef-cookielistitem?> get#dom-cookiestore-get-options(optional CookieStoreGetOptions#dictdef-cookiestoregetoptions options = {});

  Promisehttps://webidl.spec.whatwg.org/#idl-promise<CookieList#typedefdef-cookielist> getAll#dom-cookiestore-getall(USVStringhttps://webidl.spec.whatwg.org/#idl-USVString name);
  Promisehttps://webidl.spec.whatwg.org/#idl-promise<CookieList#typedefdef-cookielist> getAll#dom-cookiestore-getall-options(optional CookieStoreGetOptions#dictdef-cookiestoregetoptions options = {});

  Promisehttps://webidl.spec.whatwg.org/#idl-promise<undefinedhttps://webidl.spec.whatwg.org/#idl-undefined> set#dom-cookiestore-set(USVStringhttps://webidl.spec.whatwg.org/#idl-USVString name, USVStringhttps://webidl.spec.whatwg.org/#idl-USVString value);
  Promisehttps://webidl.spec.whatwg.org/#idl-promise<undefinedhttps://webidl.spec.whatwg.org/#idl-undefined> set#dom-cookiestore-set-options(CookieInit#dictdef-cookieinit options);

  Promisehttps://webidl.spec.whatwg.org/#idl-promise<undefinedhttps://webidl.spec.whatwg.org/#idl-undefined> delete#dom-cookiestore-delete(USVStringhttps://webidl.spec.whatwg.org/#idl-USVString name);
  Promisehttps://webidl.spec.whatwg.org/#idl-promise<undefinedhttps://webidl.spec.whatwg.org/#idl-undefined> delete#dom-cookiestore-delete-options(CookieStoreDeleteOptions#dictdef-cookiestoredeleteoptions options);

  [Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
  attribute EventHandlerhttps://html.spec.whatwg.org/multipage/webappapis.html#eventhandler onchange;
};

dictionary CookieStoreGetOptions {
  USVStringhttps://webidl.spec.whatwg.org/#idl-USVString name;
  USVStringhttps://webidl.spec.whatwg.org/#idl-USVString url;
};

enum CookieSameSite {
  "strict",
  "lax",
  "none"
};

dictionary CookieInit {
  required USVStringhttps://webidl.spec.whatwg.org/#idl-USVString name;
  required USVStringhttps://webidl.spec.whatwg.org/#idl-USVString value;
  DOMHighResTimeStamphttps://w3c.github.io/hr-time/#dom-domhighrestimestamp? expires = null;
  USVStringhttps://webidl.spec.whatwg.org/#idl-USVString? domain = null;
  USVStringhttps://webidl.spec.whatwg.org/#idl-USVString path = "/";
  CookieSameSite#enumdef-cookiesamesite sameSite = "strict";
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean partitioned = false;
  long longhttps://webidl.spec.whatwg.org/#idl-long-long? maxAge = null;
};

dictionary CookieStoreDeleteOptions {
  required USVStringhttps://webidl.spec.whatwg.org/#idl-USVString name;
  USVStringhttps://webidl.spec.whatwg.org/#idl-USVString? domain = null;
  USVStringhttps://webidl.spec.whatwg.org/#idl-USVString path = "/";
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean partitioned = false;
};

dictionary CookieListItem {
  USVStringhttps://webidl.spec.whatwg.org/#idl-USVString name;
  USVStringhttps://webidl.spec.whatwg.org/#idl-USVString value;
};

typedef sequencehttps://webidl.spec.whatwg.org/#idl-sequence<CookieListItem#dictdef-cookielistitem> CookieList;
```

### 3.1. The [get()](#dom-cookiestore-get-options) method#CookieStore-get

cookie = await cookieStore . [get](#dom-cookiestore-get)(name) cookie = await cookieStore . [get](#dom-cookiestore-get-options)(options) 

Returns a promise resolving to the first in-scope [script-visible](#script-visible) value for a given cookie name (or other options). In a service worker context this defaults to the path of the service worker’s registered scope. In a document it defaults to the path of the current document and does not respect changes from [replaceState()](https://html.spec.whatwg.org/multipage/nav-history-apis.html#dom-history-replacestate) or [document.domain](https://html.spec.whatwg.org/multipage/browsers.html#dom-document-domain).

 The `get(name)` method steps are: 

1. 

Let settings be [this](https://webidl.spec.whatwg.org/#this)’s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

2. 

Let origin be settings’s [origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-origin).

3. 

If origin is an [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque), then return [a promise rejected with](https://webidl.spec.whatwg.org/#a-promise-rejected-with) a "[SecurityError](https://webidl.spec.whatwg.org/#securityerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException).

4. 

Let url be settings’s [creation URL](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-creation-url).

5. 

Let p be [a new promise](https://webidl.spec.whatwg.org/#a-new-promise).

6. 

Run the following steps [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel):

  1. 

Let list be the results of running [query cookies](#query-cookies) with url and name.

  2. 

If list is failure, then [reject](https://webidl.spec.whatwg.org/#reject)p with a [TypeError](https://webidl.spec.whatwg.org/#exceptiondef-typeerror) and abort these steps.

  3. 

If list[is empty](https://infra.spec.whatwg.org/#list-is-empty), then [resolve](https://webidl.spec.whatwg.org/#resolve)p with null.

  4. 

Otherwise, [resolve](https://webidl.spec.whatwg.org/#resolve)p with the first item of list.

7. 

Return p.

 The `get(options)` method steps are: 

1. 

Let settings be [this](https://webidl.spec.whatwg.org/#this)’s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

2. 

Let origin be settings’s [origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-origin).

3. 

If origin is an [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque), then return [a promise rejected with](https://webidl.spec.whatwg.org/#a-promise-rejected-with) a "[SecurityError](https://webidl.spec.whatwg.org/#securityerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException).

4. 

Let url be settings’s [creation URL](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-creation-url).

5. 

If options[is empty](https://infra.spec.whatwg.org/#map-is-empty), then return [a promise rejected with](https://webidl.spec.whatwg.org/#a-promise-rejected-with) a [TypeError](https://webidl.spec.whatwg.org/#exceptiondef-typeerror).

6. 

If options["[url](#dom-cookiestoregetoptions-url)"] [exists](https://infra.spec.whatwg.org/#map-exists):

  1. 

Let parsed be the result of [parsing](https://url.spec.whatwg.org/#concept-basic-url-parser)options["[url](#dom-cookiestoregetoptions-url)"] with settings’s [API base URL](https://html.spec.whatwg.org/multipage/webappapis.html#api-base-url).

  2. 

If [this](https://webidl.spec.whatwg.org/#this)’s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) is a [Window](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window) object and parsed does not [equal](https://url.spec.whatwg.org/#concept-url-equals)url with [exclude fragments](https://url.spec.whatwg.org/#url-equals-exclude-fragments) set to true, then return [a promise rejected with](https://webidl.spec.whatwg.org/#a-promise-rejected-with) a [TypeError](https://webidl.spec.whatwg.org/#exceptiondef-typeerror).

  3. 

If parsed’s [origin](https://url.spec.whatwg.org/#concept-url-origin) and url’s [origin](https://url.spec.whatwg.org/#concept-url-origin) are not the [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin), then return [a promise rejected with](https://webidl.spec.whatwg.org/#a-promise-rejected-with) a [TypeError](https://webidl.spec.whatwg.org/#exceptiondef-typeerror).

  4. 

Set url to parsed.

7. 

Let p be [a new promise](https://webidl.spec.whatwg.org/#a-new-promise).

8. 

Run the following steps [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel):

  1. 

Let list be the results of running [query cookies](#query-cookies) with url and options["[name](#dom-cookiestoregetoptions-name)"] [with default](https://infra.spec.whatwg.org/#map-with-default) null.

  2. 

If list is failure, then [reject](https://webidl.spec.whatwg.org/#reject)p with a [TypeError](https://webidl.spec.whatwg.org/#exceptiondef-typeerror) and abort these steps.

  3. 

If list[is empty](https://infra.spec.whatwg.org/#list-is-empty), then [resolve](https://webidl.spec.whatwg.org/#resolve)p with null.

  4. 

Otherwise, [resolve](https://webidl.spec.whatwg.org/#resolve)p with the first item of list.

9. 

Return p.

### 3.2. The [getAll()](#dom-cookiestore-getall-options) method#CookieStore-getAll

cookies = await cookieStore . [getAll](#dom-cookiestore-getall)(name) cookies = await cookieStore . [getAll](#dom-cookiestore-getall-options)(options) 

Returns a promise resolving to the all in-scope [script-visible](#script-visible) value for a given cookie name (or other options). In a service worker context this defaults to the path of the service worker’s registered scope. In a document it defaults to the path of the current document and does not respect changes from [replaceState()](https://html.spec.whatwg.org/multipage/nav-history-apis.html#dom-history-replacestate) or [document.domain](https://html.spec.whatwg.org/multipage/browsers.html#dom-document-domain).

 The `getAll(name)` method steps are: 

1. 

Let settings be [this](https://webidl.spec.whatwg.org/#this)’s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

2. 

Let origin be settings’s [origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-origin).

3. 

If origin is an [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque), then return [a promise rejected with](https://webidl.spec.whatwg.org/#a-promise-rejected-with) a "[SecurityError](https://webidl.spec.whatwg.org/#securityerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException).

4. 

Let url be settings’s [creation URL](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-creation-url).

5. 

Let p be [a new promise](https://webidl.spec.whatwg.org/#a-new-promise).

6. 

Run the following steps [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel):

  1. 

Let list be the results of running [query cookies](#query-cookies) with url and name.

  2. 

If list is failure, then [reject](https://webidl.spec.whatwg.org/#reject)p with a [TypeError](https://webidl.spec.whatwg.org/#exceptiondef-typeerror).

  3. 

Otherwise, [resolve](https://webidl.spec.whatwg.org/#resolve)p with list.

7. 

Return p.

 The `getAll(options)` method steps are: 

1. 

Let settings be [this](https://webidl.spec.whatwg.org/#this)’s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

2. 

Let origin be settings’s [origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-origin).

3. 

If origin is an [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque), then return [a promise rejected with](https://webidl.spec.whatwg.org/#a-promise-rejected-with) a "[SecurityError](https://webidl.spec.whatwg.org/#securityerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException).

4. 

Let url be settings’s [creation URL](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-creation-url).

5. 

If options["[url](#dom-cookiestoregetoptions-url)"] [exists](https://infra.spec.whatwg.org/#map-exists):

  1. 

Let parsed be the result of [parsing](https://url.spec.whatwg.org/#concept-basic-url-parser)options["[url](#dom-cookiestoregetoptions-url)"] with settings’s [API base URL](https://html.spec.whatwg.org/multipage/webappapis.html#api-base-url).

  2. 

If [this](https://webidl.spec.whatwg.org/#this)’s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) is a [Window](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window) object and parsed does not [equal](https://url.spec.whatwg.org/#concept-url-equals)url with [exclude fragments](https://url.spec.whatwg.org/#url-equals-exclude-fragments) set to true, then return [a promise rejected with](https://webidl.spec.whatwg.org/#a-promise-rejected-with) a [TypeError](https://webidl.spec.whatwg.org/#exceptiondef-typeerror).

  3. 

If parsed’s [origin](https://url.spec.whatwg.org/#concept-url-origin) and url’s [origin](https://url.spec.whatwg.org/#concept-url-origin) are not the [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin), then return [a promise rejected with](https://webidl.spec.whatwg.org/#a-promise-rejected-with) a [TypeError](https://webidl.spec.whatwg.org/#exceptiondef-typeerror).

  4. 

Set url to parsed.

6. 

Let p be [a new promise](https://webidl.spec.whatwg.org/#a-new-promise).

7. 

Run the following steps [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel):

  1. 

Let list be the results of running [query cookies](#query-cookies) with url and options["[name](#dom-cookiestoregetoptions-name)"] [with default](https://infra.spec.whatwg.org/#map-with-default) null.

  2. 

If list is failure, then [reject](https://webidl.spec.whatwg.org/#reject)p with a [TypeError](https://webidl.spec.whatwg.org/#exceptiondef-typeerror).

  3. 

Otherwise, [resolve](https://webidl.spec.whatwg.org/#resolve)p with list.

8. 

Return p.

### 3.3. The [set()](#dom-cookiestore-set) method#CookieStore-set

await cookieStore . [set](#dom-cookiestore-set)(name, value) await cookieStore . [set](#dom-cookiestore-set-options)(options) 

Writes (creates or modifies) a cookie.

The options default to:

- 

Path: `/`

- 

Domain: same as the domain of the current document or service worker’s location

- 

No expiry date

- 

SameSite: strict

 The `set(name, value)` method steps are: 

1. 

Let settings be [this](https://webidl.spec.whatwg.org/#this)’s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

2. 

Let origin be settings’s [origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-origin).

3. 

If origin is an [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque), then return [a promise rejected with](https://webidl.spec.whatwg.org/#a-promise-rejected-with) a "[SecurityError](https://webidl.spec.whatwg.org/#securityerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException).

4. 

Let url be settings’s [creation URL](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-creation-url).

5. 

Let p be [a new promise](https://webidl.spec.whatwg.org/#a-new-promise).

6. 

Run the following steps [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel):

  1. 

Let r be the result of running [set a cookie](#set-a-cookie) with url, name, value, null, null, "`/`", "[strict](#dom-cookiesamesite-strict)", false, and null.

  2. 

If r is failure, then [reject](https://webidl.spec.whatwg.org/#reject)p with a [TypeError](https://webidl.spec.whatwg.org/#exceptiondef-typeerror) and abort these steps.

  3. 

[Resolve](https://webidl.spec.whatwg.org/#resolve)p with undefined.

7. 

Return p.

 The `set(options)` method steps are: 

1. 

Let settings be [this](https://webidl.spec.whatwg.org/#this)’s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

2. 

Let origin be settings’s [origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-origin).

3. 

If origin is an [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque), then return [a promise rejected with](https://webidl.spec.whatwg.org/#a-promise-rejected-with) a "[SecurityError](https://webidl.spec.whatwg.org/#securityerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException).

4. 

Let url be settings’s [creation URL](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-creation-url).

5. 

Let p be [a new promise](https://webidl.spec.whatwg.org/#a-new-promise).

6. 

Run the following steps [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel):

  1. 

Let r be the result of running [set a cookie](#set-a-cookie) with url, options["[name](#dom-cookieinit-name)"], options["[value](#dom-cookieinit-value)"], options["[expires](#dom-cookieinit-expires)"], options["[domain](#dom-cookieinit-domain)"], options["[path](#dom-cookieinit-path)"], options["[sameSite](#dom-cookieinit-samesite)"], options["[partitioned](#dom-cookieinit-partitioned)"], and options["[maxAge](#dom-cookieinit-maxage)"].

  2. 

If r is failure, then [reject](https://webidl.spec.whatwg.org/#reject)p with a [TypeError](https://webidl.spec.whatwg.org/#exceptiondef-typeerror) and abort these steps.

  3. 

[Resolve](https://webidl.spec.whatwg.org/#resolve)p with undefined.

7. 

Return p.

### 3.4. The [delete()](#dom-cookiestore-delete) method#CookieStore-delete

await cookieStore . [delete](#dom-cookiestore-delete)(name) await cookieStore . [delete](#dom-cookiestore-delete-options)(options) 

Deletes (expires) a cookie with the given name or name and optional domain and path.

 The `delete(name)` method steps are: 

1. 

Let settings be [this](https://webidl.spec.whatwg.org/#this)’s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

2. 

Let origin be settings’s [origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-origin).

3. 

If origin is an [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque), then return [a promise rejected with](https://webidl.spec.whatwg.org/#a-promise-rejected-with) a "[SecurityError](https://webidl.spec.whatwg.org/#securityerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException).

4. 

Let url be settings’s [creation URL](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-creation-url).

5. 

Let p be [a new promise](https://webidl.spec.whatwg.org/#a-new-promise).

6. 

Run the following steps [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel):

  1. 

Let r be the result of running [delete a cookie](#delete-a-cookie) with url, name, null, "`/`", and true.

  2. 

If r is failure, then [reject](https://webidl.spec.whatwg.org/#reject)p with a [TypeError](https://webidl.spec.whatwg.org/#exceptiondef-typeerror) and abort these steps.

  3. 

[Resolve](https://webidl.spec.whatwg.org/#resolve)p with undefined.

7. 

Return p.

 The `delete(options)` method steps are: 

1. 

Let settings be [this](https://webidl.spec.whatwg.org/#this)’s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

2. 

Let origin be settings’s [origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-origin).

3. 

If origin is an [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque), then return [a promise rejected with](https://webidl.spec.whatwg.org/#a-promise-rejected-with) a "[SecurityError](https://webidl.spec.whatwg.org/#securityerror)" [DOMException](https://webidl.spec.whatwg.org/#idl-DOMException).

4. 

Let url be settings’s [creation URL](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-creation-url).

5. 

Let p be [a new promise](https://webidl.spec.whatwg.org/#a-new-promise).

6. 

Run the following steps [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel):

  1. 

Let r be the result of running [delete a cookie](#delete-a-cookie) with url, options["[name](#dom-cookiestoredeleteoptions-name)"], options["[domain](#dom-cookiestoredeleteoptions-domain)"], options["[path](#dom-cookiestoredeleteoptions-path)"], and options["[partitioned](#dom-cookiestoredeleteoptions-partitioned)"].

  2. 

If r is failure, then [reject](https://webidl.spec.whatwg.org/#reject)p with a [TypeError](https://webidl.spec.whatwg.org/#exceptiondef-typeerror) and abort these steps.

  3. 

[Resolve](https://webidl.spec.whatwg.org/#resolve)p with undefined.

7. 

Return p.

## 4. The [CookieStoreManager](#cookiestoremanager) interface#CookieStoreManager

A [CookieStoreManager](#cookiestoremanager) has an associated registration which is a [service worker registration](https://w3c.github.io/ServiceWorker/#dfn-service-worker-registration).

The [CookieStoreManager](#cookiestoremanager) interface allows [Service Workers](https://w3c.github.io/ServiceWorker/#dfn-service-worker) to subscribe to events for cookie changes. Using the [subscribe()](#dom-cookiestoremanager-subscribe) method is necessary to indicate that a particular [service worker registration](https://w3c.github.io/ServiceWorker/#dfn-service-worker-registration) is interested in change events.

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=(ServiceWorker,Window),
 SecureContexthttps://webidl.spec.whatwg.org/#SecureContext]
interface CookieStoreManager {
  Promisehttps://webidl.spec.whatwg.org/#idl-promise<undefinedhttps://webidl.spec.whatwg.org/#idl-undefined> subscribe#dom-cookiestoremanager-subscribe(sequencehttps://webidl.spec.whatwg.org/#idl-sequence<CookieStoreGetOptions#dictdef-cookiestoregetoptions> subscriptions);
  Promisehttps://webidl.spec.whatwg.org/#idl-promise<sequencehttps://webidl.spec.whatwg.org/#idl-sequence<CookieStoreGetOptions#dictdef-cookiestoregetoptions>> getSubscriptions#dom-cookiestoremanager-getsubscriptions();
  Promisehttps://webidl.spec.whatwg.org/#idl-promise<undefinedhttps://webidl.spec.whatwg.org/#idl-undefined> unsubscribe#dom-cookiestoremanager-unsubscribe(sequencehttps://webidl.spec.whatwg.org/#idl-sequence<CookieStoreGetOptions#dictdef-cookiestoregetoptions> subscriptions);
};
```

### 4.1. The [subscribe()](#dom-cookiestoremanager-subscribe) method#CookieStoreManager-subscribe

await registration . cookies . [subscribe](#dom-cookiestoremanager-subscribe)(subscriptions) 

Subscribe to changes to cookies. Subscriptions can use the same options as [get()](#dom-cookiestore-get-options) and [getAll()](#dom-cookiestore-getall-options), with optional[name](#dom-cookiestoregetoptions-name) and [url](#dom-cookiestoregetoptions-url) properties.

Once subscribed, notifications are delivered as "`cookiechange`" events fired against the [Service Worker](https://w3c.github.io/ServiceWorker/#dfn-service-worker)’s global scope:

 The `subscribe(subscriptions)` method steps are: 

1. 

Let settings be [this](https://webidl.spec.whatwg.org/#this)’s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

2. 

Let registration be [this](https://webidl.spec.whatwg.org/#this)’s [registration](#cookiestoremanager-registration).

3. 

Let p be [a new promise](https://webidl.spec.whatwg.org/#a-new-promise).

4. 

Run the following steps [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel):

  1. 

Let subscription list be registration’s associated [cookie change subscription list](#cookie-change-subscription-list).

  2. 

[For each](https://infra.spec.whatwg.org/#list-iterate)entry in subscriptions, run these steps:

    1. 

Let name be entry["[name](#dom-cookiestoregetoptions-name)"].

    2. 

[Normalize](#normalize-a-cookie-name-or-value)name.

    3. 

Let url be the result of [parsing](https://url.spec.whatwg.org/#concept-basic-url-parser)entry["[url](#dom-cookiestoregetoptions-url)"] with settings’s [API base URL](https://html.spec.whatwg.org/multipage/webappapis.html#api-base-url).

    4. 

If url does not start with registration’s [scope url](https://w3c.github.io/ServiceWorker/#dfn-scope-url), then [reject](https://webidl.spec.whatwg.org/#reject)p with a [TypeError](https://webidl.spec.whatwg.org/#exceptiondef-typeerror) and abort these steps.

    5. 

Let subscription be the [cookie change subscription](#cookie-change-subscription) (name, url).

    6. 

If subscription list does not already [contain](https://infra.spec.whatwg.org/#list-contain)subscription, then [append](https://infra.spec.whatwg.org/#list-append)subscription to subscription list.

  3. 

[Resolve](https://webidl.spec.whatwg.org/#resolve)p with undefined.

5. 

Return p.

### 4.2. The [getSubscriptions()](#dom-cookiestoremanager-getsubscriptions) method#CookieStoreManager-getSubscriptions

subscriptions = await registration . cookies . [getSubscriptions()](#dom-cookiestoremanager-getsubscriptions)

This method returns a promise which resolves to a list of the cookie change subscriptions made for this Service Worker registration.

 The `getSubscriptions()` method steps are: 

1. 

Let registration be [this](https://webidl.spec.whatwg.org/#this)’s [registration](#cookiestoremanager-registration).

2. 

Let p be [a new promise](https://webidl.spec.whatwg.org/#a-new-promise).

3. 

Run the following steps [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel):

  1. 

Let subscriptions be registration’s associated [cookie change subscription list](#cookie-change-subscription-list).

  2. 

Let result be « ».

  3. 

[For each](https://infra.spec.whatwg.org/#list-iterate)subscription in subscriptions, run these steps:

    1. 

[Append](https://infra.spec.whatwg.org/#list-append) «[ "name" → subscription’s [name](#cookie-change-subscription-name), "url" → subscription’s [url](#cookie-change-subscription-url)]» to result.

  4. 

[Resolve](https://webidl.spec.whatwg.org/#resolve)p with result.

4. 

Return p.

### 4.3. The [unsubscribe()](#dom-cookiestoremanager-unsubscribe) method#CookieStoreManager-unsubscribe

await registration . cookies . [unsubscribe](#dom-cookiestoremanager-unsubscribe)(subscriptions) 

Calling this method will stop the registered service worker from receiving previously subscribed events. The subscriptions argument ought to list subscriptions in the same form passed to [subscribe()](#dom-cookiestoremanager-subscribe) or returned from [getSubscriptions()](#dom-cookiestoremanager-getsubscriptions).

 The `unsubscribe(subscriptions)` method steps are: 

1. 

Let settings be [this](https://webidl.spec.whatwg.org/#this)’s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

2. 

Let registration be [this](https://webidl.spec.whatwg.org/#this)’s [registration](#cookiestoremanager-registration).

3. 

Let p be [a new promise](https://webidl.spec.whatwg.org/#a-new-promise).

4. 

Run the following steps [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel):

  1. 

Let subscription list be registration’s associated [cookie change subscription list](#cookie-change-subscription-list).

  2. 

[For each](https://infra.spec.whatwg.org/#list-iterate)entry in subscriptions, run these steps:

    1. 

Let name be entry["[name](#dom-cookiestoregetoptions-name)"].

    2. 

[Normalize](#normalize-a-cookie-name-or-value)name.

    3. 

Let url be the result of [parsing](https://url.spec.whatwg.org/#concept-basic-url-parser)entry["[url](#dom-cookiestoregetoptions-url)"] with settings’s [API base URL](https://html.spec.whatwg.org/multipage/webappapis.html#api-base-url).

    4. 

If url does not start with registration’s [scope url](https://w3c.github.io/ServiceWorker/#dfn-scope-url), then [reject](https://webidl.spec.whatwg.org/#reject)p with a [TypeError](https://webidl.spec.whatwg.org/#exceptiondef-typeerror) and abort these steps.

    5. 

Let subscription be the [cookie change subscription](#cookie-change-subscription) (name, url).

    6. 

[Remove](https://infra.spec.whatwg.org/#list-remove) any [item](https://infra.spec.whatwg.org/#list-item) from subscription list equal to subscription.

  3. 

[Resolve](https://webidl.spec.whatwg.org/#resolve)p with undefined.

5. 

Return p.

### 4.4. The [ServiceWorkerRegistration](https://w3c.github.io/ServiceWorker/#serviceworkerregistration) interface#ServiceWorkerRegistration

The [ServiceWorkerRegistration](https://w3c.github.io/ServiceWorker/#serviceworkerregistration) interface is extended to give access to a [CookieStoreManager](#cookiestoremanager) via [cookies](#dom-serviceworkerregistration-cookies) which provides the interface for subscribing to cookie changes.

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=(ServiceWorker,Window)]
partial interface ServiceWorkerRegistrationhttps://w3c.github.io/ServiceWorker/#serviceworkerregistration {
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute CookieStoreManager#cookiestoremanager cookies#dom-serviceworkerregistration-cookies;
};
```

Each [ServiceWorkerRegistration](https://w3c.github.io/ServiceWorker/#serviceworkerregistration) has an associated [CookieStoreManager](#cookiestoremanager) object. The [CookieStoreManager](#cookiestoremanager)’s [registration](#cookiestoremanager-registration) is equal to the [ServiceWorkerRegistration](https://w3c.github.io/ServiceWorker/#serviceworkerregistration)’s [service worker registration](https://w3c.github.io/ServiceWorker/#dfn-service-worker-registration).

The `cookies` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s associated [CookieStoreManager](#cookiestoremanager) object.

#example-45f94580 Subscribing to cookie changes from a Service Worker script: 

```
self.registration.cookies.subscribe([{name:'session-id'}]);
```

#example-254a868d Subscribing to cookie changes from a script in a window context: 

```
navigator.serviceWorker.register('sw.js').then(registration => {
  registration.cookies.subscribe([{name:'session-id'}]);
});
```

## 5. Event interfaces#event-interfaces

### 5.1. The [CookieChangeEvent](#cookiechangeevent) interface#CookieChangeEvent

A [CookieChangeEvent](#cookiechangeevent) is [dispatched](https://dom.spec.whatwg.org/#concept-event-dispatch) against [CookieStore](#cookiestore) objects in [Window](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window) contexts when any [script-visible](#script-visible) cookie changes have occurred.

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window,
 SecureContexthttps://webidl.spec.whatwg.org/#SecureContext]
interface CookieChangeEvent : Eventhttps://dom.spec.whatwg.org/#event {
  constructor(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString type, optional CookieChangeEventInit#dictdef-cookiechangeeventinit eventInitDict = {});
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute FrozenArrayhttps://webidl.spec.whatwg.org/#idl-frozen-array<CookieListItem#dictdef-cookielistitem> changed;
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute FrozenArrayhttps://webidl.spec.whatwg.org/#idl-frozen-array<CookieListItem#dictdef-cookielistitem> deleted;
};

dictionary CookieChangeEventInit : EventInithttps://dom.spec.whatwg.org/#dictdef-eventinit {
  CookieList#typedefdef-cookielist changed;
  CookieList#typedefdef-cookielist deleted;
};
```

The [changed](#dom-cookiechangeevent-changed) and [deleted](#dom-cookiechangeevent-deleted) attributes must return the value they were initialized to.

### 5.2. The [ExtendableCookieChangeEvent](#extendablecookiechangeevent) interface#ExtendableCookieChangeEvent

An [ExtendableCookieChangeEvent](#extendablecookiechangeevent) is [dispatched](https://dom.spec.whatwg.org/#concept-event-dispatch) against [ServiceWorkerGlobalScope](https://w3c.github.io/ServiceWorker/#serviceworkerglobalscope) objects when any [script-visible](#script-visible) cookie changes have occurred which match the [Service Worker](https://w3c.github.io/ServiceWorker/#dfn-service-worker)’s [cookie change subscription list](#cookie-change-subscription-list).

Note:[ExtendableEvent](https://w3c.github.io/ServiceWorker/#extendableevent) is used as the ancestor interface for all events in [Service Workers](https://w3c.github.io/ServiceWorker/#dfn-service-worker) so that the worker itself can be kept alive while the async operations are performed.

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=ServiceWorker]
interface ExtendableCookieChangeEvent : ExtendableEventhttps://w3c.github.io/ServiceWorker/#extendableevent {
  constructor(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString type, optional ExtendableCookieChangeEventInit#dictdef-extendablecookiechangeeventinit eventInitDict = {});
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute FrozenArrayhttps://webidl.spec.whatwg.org/#idl-frozen-array<CookieListItem#dictdef-cookielistitem> changed;
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute FrozenArrayhttps://webidl.spec.whatwg.org/#idl-frozen-array<CookieListItem#dictdef-cookielistitem> deleted;
};

dictionary ExtendableCookieChangeEventInit : ExtendableEventInithttps://w3c.github.io/ServiceWorker/#dictdef-extendableeventinit {
  CookieList#typedefdef-cookielist changed;
  CookieList#typedefdef-cookielist deleted;
};
```

The [changed](#dom-extendablecookiechangeevent-changed) and [deleted](#dom-extendablecookiechangeevent-deleted) attributes must return the value they were initialized to.

## 6. Global interfaces#globals

A [CookieStore](#cookiestore) is accessed by script using an attribute in the global scope in a [Window](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window) or [ServiceWorkerGlobalScope](https://w3c.github.io/ServiceWorker/#serviceworkerglobalscope) context.

### 6.1. The [Window](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window) interface#Window

```
[SecureContexthttps://webidl.spec.whatwg.org/#SecureContext]
partial interface Windowhttps://html.spec.whatwg.org/multipage/nav-history-apis.html#window {
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute CookieStore#cookiestore cookieStore#dom-window-cookiestore;
};
```

A [Window](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window) has an associated CookieStore, which is a [CookieStore](#cookiestore).

The `cookieStore` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [associated CookieStore](#window-associated-cookiestore).

### 6.2. The [ServiceWorkerGlobalScope](https://w3c.github.io/ServiceWorker/#serviceworkerglobalscope) interface#ServiceWorkerGlobalScope

```
partial interface ServiceWorkerGlobalScopehttps://w3c.github.io/ServiceWorker/#serviceworkerglobalscope {
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute CookieStore#cookiestore cookieStore#dom-serviceworkerglobalscope-cookiestore;

  attribute EventHandlerhttps://html.spec.whatwg.org/multipage/webappapis.html#eventhandler oncookiechange;
};
```

A [ServiceWorkerGlobalScope](https://w3c.github.io/ServiceWorker/#serviceworkerglobalscope) has an associated CookieStore, which is a [CookieStore](#cookiestore).

The `cookieStore` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)’s [associated CookieStore](#serviceworkerglobalscope-associated-cookiestore).

## 7. Algorithms#algorithms

 To date serialize a [DOMHighResTimeStamp](https://w3c.github.io/hr-time/#dom-domhighrestimestamp)millis, let dateTime be the date and time millis milliseconds after 00:00:00 UTC, 1 January 1970 (assuming that there are exactly 86,400,000 milliseconds per day), and return a [byte sequence](https://infra.spec.whatwg.org/#byte-sequence) corresponding to the closest `cookie-date` representation of dateTime according to [Cookies § Dates](https://tools.ietf.org/html/draft-ietf-httpbis-rfc6265bis-14#name-dates). 

### 7.1. Query cookies#query-cookies-algorithm

To query cookies given a [URL](https://url.spec.whatwg.org/#concept-url)url and [scalar value string](https://infra.spec.whatwg.org/#scalar-value-string)-or-null name:

1. 

Perform the steps defined in [Cookies § Retrieval Model](https://tools.ietf.org/html/draft-ietf-httpbis-rfc6265bis-14#name-retrieval-model) to compute the "cookie-string from a given cookie store" with url as request-uri. The cookie-string itself is ignored, but the intermediate cookie-list is used in subsequent steps.

For the purposes of the steps, the cookie-string is being generated for a "non-HTTP" API.

2. 

Let list be « ».

3. 

[For each](https://infra.spec.whatwg.org/#list-iterate)cookie of cookie-list:

  1. 

Assert: cookie’s [http-only-flag](#cookie-http-only-flag) is false.

  2. 

If name is non-null:

    1. 

[Normalize](#normalize-a-cookie-name-or-value)name.

    2. 

Let cookieName be the result of running [UTF-8 decode without BOM](https://encoding.spec.whatwg.org/#utf-8-decode-without-bom) on cookie’s [name](#cookie-name).

    3. 

If cookieName does not equal name, then [continue](https://infra.spec.whatwg.org/#iteration-continue).

  3. 

Let item be the result of running [create a CookieListItem](#create-a-cookielistitem) from cookie.

  4. 

[Append](https://infra.spec.whatwg.org/#list-append)item to list.

4. 

Return list.

To create a [CookieListItem](#dictdef-cookielistitem) from a [cookie](#cookie)cookie:

1. 

Let name be the result of running [UTF-8 decode without BOM](https://encoding.spec.whatwg.org/#utf-8-decode-without-bom) on cookie’s [name](#cookie-name).

2. 

Let value be the result of running [UTF-8 decode without BOM](https://encoding.spec.whatwg.org/#utf-8-decode-without-bom) on cookie’s [value](#cookie-value).

3. 

Return «[ "[name](#dom-cookielistitem-name)" → name, "[value](#dom-cookielistitem-value)" → value ]».

Note: One implementation is known to expose information beyond _name_ and _value_.

### 7.2. Set a cookie#set-cookie-algorithm

To set a cookie given a [URL](https://url.spec.whatwg.org/#concept-url)url, [scalar value string](https://infra.spec.whatwg.org/#scalar-value-string)name, [scalar value string](https://infra.spec.whatwg.org/#scalar-value-string)value, [DOMHighResTimeStamp](https://w3c.github.io/hr-time/#dom-domhighrestimestamp)-or-null expires, [scalar value string](https://infra.spec.whatwg.org/#scalar-value-string)-or-null domain, [scalar value string](https://infra.spec.whatwg.org/#scalar-value-string)path, [string](https://infra.spec.whatwg.org/#string)sameSite, [boolean](https://infra.spec.whatwg.org/#boolean)partitioned, and [64-bit signed integer](https://infra.spec.whatwg.org/#64-bit-signed-integer)-or-null maxAge:

1. 

[Normalize](#normalize-a-cookie-name-or-value)name.

2. 

[Normalize](#normalize-a-cookie-name-or-value)value.

3. 

If name or value contain U+003B (;), any [C0 control](https://infra.spec.whatwg.org/#c0-control) character except U+0009 TAB, or U+007F DELETE, then return failure.

 Note that it’s up for discussion whether these character restrictions should also apply to expires, domain, path, and sameSite as well. [[httpwg/http-extensions Issue #1593]](https://github.com/httpwg/http-extensions/issues/1593)

4. 

If name contains U+003D (=), then return failure.

5. 

If name’s [length](https://infra.spec.whatwg.org/#string-length) is 0:

  1. 

If value contains U+003D (=), then return failure.

  2. 

If value’s [length](https://infra.spec.whatwg.org/#string-length) is 0, then return failure.

  3. 

If value, [byte-lowercased](https://infra.spec.whatwg.org/#byte-lowercase), [starts with](https://infra.spec.whatwg.org/#byte-sequence-starts-with) ``__host-``, ``__host-http-``, ``__http-``, or ``__secure-``, then return failure.

6. 

If name, [byte-lowercased](https://infra.spec.whatwg.org/#byte-lowercase), [starts with](https://infra.spec.whatwg.org/#byte-sequence-starts-with) ``__host-http-`` or ``__http-``, then return failure.

7. 

Let encodedName be the result of [UTF-8 encoding](https://encoding.spec.whatwg.org/#utf-8-encode)name.

8. 

Let encodedValue be the result of [UTF-8 encoding](https://encoding.spec.whatwg.org/#utf-8-encode)value.

9. 

If the [byte sequence](https://infra.spec.whatwg.org/#byte-sequence)[length](https://infra.spec.whatwg.org/#byte-sequence-length) of encodedName plus the [byte sequence](https://infra.spec.whatwg.org/#byte-sequence)[length](https://infra.spec.whatwg.org/#byte-sequence-length) of encodedValue is greater than the [maximum name/value pair size](#cookie-maximum-name-value-pair-size), then return failure.

10. 

Let host be url’s [host](https://url.spec.whatwg.org/#concept-url-host)

11. 

Let attributes be « ».

12. 

If domain is non-null:

  1. 

If domain starts with U+002E (.), then return failure.

  2. 

If name, [byte-lowercased](https://infra.spec.whatwg.org/#byte-lowercase), [starts with](https://infra.spec.whatwg.org/#byte-sequence-starts-with) ``__host-``, then return failure.

  3. 

If domain[is not a registrable domain suffix of and is not equal to](https://html.spec.whatwg.org/multipage/browsers.html#is-a-registrable-domain-suffix-of-or-is-equal-to)host, then return failure.

  4. 

Let parsedDomain be the result of [host parsing](https://url.spec.whatwg.org/#concept-host-parser)domain.

  5. 

Assert: parsedDomain is not failure.

  6. 

Let encodedDomain be the result of [UTF-8 encoding](https://encoding.spec.whatwg.org/#utf-8-encode)parsedDomain.

  7. 

If the [byte sequence](https://infra.spec.whatwg.org/#byte-sequence)[length](https://infra.spec.whatwg.org/#byte-sequence-length) of encodedDomain is greater than the [maximum attribute value size](#cookie-maximum-attribute-value-size), then return failure.

  8. 

[Append](https://infra.spec.whatwg.org/#list-append) (``Domain``, encodedDomain) to attributes.

13. 

If expires is non-null:

  1. 

If maxAge is non-null, then return failure.

  2. 

[Append](https://infra.spec.whatwg.org/#list-append) (``Expires``, expires ([date serialized](#date-serialize))) to attributes.

14. 

Otherwise, if maxAge is non-null, then [append](https://infra.spec.whatwg.org/#list-append) (``Max-Age``, [ToString](https://tc39.github.io/ecma262/#sec-tostring)(maxAge)) to attributes.

15. 

If path is the empty string, then set path to the [serialized cookie default path](https://fetch.spec.whatwg.org/#serialized-cookie-default-path) of url.

16. 

If path does not start with U+002F (/), then return failure.

17. 

If path is not U+002F (/), and name, [byte-lowercased](https://infra.spec.whatwg.org/#byte-lowercase), [starts with](https://infra.spec.whatwg.org/#byte-sequence-starts-with) ``__host-``, then return failure.

18. 

Let encodedPath be the result of [UTF-8 encoding](https://encoding.spec.whatwg.org/#utf-8-encode)path.

19. 

If the [byte sequence](https://infra.spec.whatwg.org/#byte-sequence)[length](https://infra.spec.whatwg.org/#byte-sequence-length) of encodedPath is greater than the [maximum attribute value size](#cookie-maximum-attribute-value-size), then return failure.

20. 

[Append](https://infra.spec.whatwg.org/#list-append) (``Path``, encodedPath) to attributes.

21. 

[Append](https://infra.spec.whatwg.org/#list-append) (``Secure``, ``) to attributes.

22. 

Switch on sameSite:

"[none](#dom-cookiesamesite-none)" 

[Append](https://infra.spec.whatwg.org/#list-append) (``SameSite``, ``None``) to attributes.

"[strict](#dom-cookiesamesite-strict)" 

[Append](https://infra.spec.whatwg.org/#list-append) (``SameSite``, ``Strict``) to attributes.

"[lax](#dom-cookiesamesite-lax)" 

[Append](https://infra.spec.whatwg.org/#list-append) (``SameSite``, ``Lax``) to attributes.

23. 

If partitioned is true, [Append](https://infra.spec.whatwg.org/#list-append) (``Partitioned``, ``) to attributes.

24. 

Perform the steps defined in [Cookies § Storage Model](https://tools.ietf.org/html/draft-ietf-httpbis-rfc6265bis-14#name-storage-model) for when the user agent "receives a cookie" with url as request-uri, encodedName as cookie-name, encodedValue as cookie-value, and attributes as cookie-attribute-list.

For the purposes of the steps, the newly-created cookie was received from a "non-HTTP" API.

25. 

Return success.

Note: Storing the cookie can still fail due to requirements in [[RFC6265BIS-14]](#biblio-rfc6265bis-14), but these steps will be considered successful.

### 7.3. Delete a cookie#delete-cookie-algorithm

To delete a cookie given a [URL](https://url.spec.whatwg.org/#concept-url)url, [scalar value string](https://infra.spec.whatwg.org/#scalar-value-string)name, [scalar value string](https://infra.spec.whatwg.org/#scalar-value-string)-or-null domain, [scalar value string](https://infra.spec.whatwg.org/#scalar-value-string)path, and [boolean](https://infra.spec.whatwg.org/#boolean)partitioned:

1. 

[Normalize](#normalize-a-cookie-name-or-value)name.

2. 

Let value be the empty string.

3. 

If name’s [length](https://infra.spec.whatwg.org/#string-length) is 0, then set value to any non-empty [implementation-defined](https://infra.spec.whatwg.org/#implementation-defined) string.

4. 

Return the results of running [set a cookie](#set-a-cookie) with url, name, value, null, domain, path, "[strict](#dom-cookiesamesite-strict)", partitioned, and 0.

### 7.4. Process changes#process-changes

To process cookie changes, run the following steps:

1. 

For every [Window](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window)window, run the following steps:

  1. 

Let url be window’s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object)’s [creation URL](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-creation-url).

  2. 

Let changes be the [observable changes](#observable-changes) for url.

  3. 

If changes[is empty](https://infra.spec.whatwg.org/#list-is-empty), then [continue](https://infra.spec.whatwg.org/#iteration-continue).

  4. 

[Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [DOM manipulation task source](https://html.spec.whatwg.org/multipage/webappapis.html#dom-manipulation-task-source) given window to [fire a change event](#fire-a-change-event) named "`change`" with changes at window’s [CookieStore](#cookiestore).

2. 

For every [service worker registration](https://w3c.github.io/ServiceWorker/#dfn-service-worker-registration)registration, run the following steps:

  1. 

Let changes be a new [set](https://infra.spec.whatwg.org/#ordered-set).

  2. 

[For each](https://infra.spec.whatwg.org/#list-iterate)change in the [observable changes](#observable-changes) for registration’s [scope url](https://w3c.github.io/ServiceWorker/#dfn-scope-url), run these steps:

    1. 

Let cookie be change’s cookie.

    2. 

[For each](https://infra.spec.whatwg.org/#list-iterate)subscription in registration’s [cookie change subscription list](#cookie-change-subscription-list), run these steps:

      1. 

If change is not [in](https://infra.spec.whatwg.org/#list-contain) the [observable changes](#observable-changes) for subscription’s [url](#cookie-change-subscription-url), then [continue](https://infra.spec.whatwg.org/#iteration-continue).

      2. 

Let cookieName be the result of running [UTF-8 decode without BOM](https://encoding.spec.whatwg.org/#utf-8-decode-without-bom) on cookie’s [name](#cookie-name).

      3. 

If cookieName equals subscription’s [name](#cookie-change-subscription-name), then [append](https://infra.spec.whatwg.org/#set-append)change to changes and [break](https://infra.spec.whatwg.org/#iteration-break).

  3. 

If changes[is empty](https://infra.spec.whatwg.org/#list-is-empty), then [continue](https://infra.spec.whatwg.org/#iteration-continue).

  4. 

Let changedList and deletedList be the result of running [prepare lists](#prepare-lists) from changes.

  5. 

[Fire a functional event](https://w3c.github.io/ServiceWorker/#fire-functional-event) named "`cookiechange`" using [ExtendableCookieChangeEvent](#extendablecookiechangeevent) on registration with these properties:

[changed](#dom-extendablecookiechangeevent-changed)

changedList

[deleted](#dom-extendablecookiechangeevent-deleted)

deletedList

The observable changes for url are the [set](https://infra.spec.whatwg.org/#ordered-set) of [cookie changes](#cookie-change) to [cookies](#cookie) in a [cookie store](#cookie-store) which meet the requirements in step 1 of [Cookies § Retrieval Algorithm](https://tools.ietf.org/html/draft-ietf-httpbis-rfc6265bis-14#name-retrieval-algorithm)’s steps to compute the "cookie-string from a given cookie store" with url as request-uri, for a "non-HTTP" API.

A cookie change is a [cookie](#cookie) and a type (either changed or deleted):

- 

A [cookie](#cookie) which is removed due to an insertion of another [cookie](#cookie) with the same [name](#cookie-name), [domain](#cookie-domain), and [path](#cookie-path) is ignored.

- 

A newly-created [cookie](#cookie) which is not immediately evicted is considered changed.

- 

A newly-created [cookie](#cookie) which is immediately evicted is considered deleted.

- 

A [cookie](#cookie) which is otherwise evicted or removed is considered deleted

To fire a change event named type with changes at target, run the following steps:

1. 

Let event be the result of [creating an Event](https://dom.spec.whatwg.org/#concept-event-create) using [CookieChangeEvent](#cookiechangeevent).

2. 

Set event’s [type](https://dom.spec.whatwg.org/#dom-event-type) attribute to type.

3. 

Set event’s [bubbles](https://dom.spec.whatwg.org/#dom-event-bubbles) and [cancelable](https://dom.spec.whatwg.org/#dom-event-cancelable) attributes to false.

4. 

Let changedList and deletedList be the result of running [prepare lists](#prepare-lists) from changes.

5. 

Set event’s [changed](#dom-cookiechangeevent-changed) attribute to changedList.

6. 

Set event’s [deleted](#dom-cookiechangeevent-deleted) attribute to deletedList.

7. 

[Dispatch](https://dom.spec.whatwg.org/#concept-event-dispatch)event at target.

To prepare lists from changes, run the following steps:

1. 

Let changedList be « ».

2. 

Let deletedList be « ».

3. 

[For each](https://infra.spec.whatwg.org/#list-iterate)change in changes, run these steps:

  1. 

Let item be the result of running [create a CookieListItem](#create-a-cookielistitem) from change’s cookie.

  2. 

If change’s type is changed, then [append](https://infra.spec.whatwg.org/#list-append)item to changedList.

  3. 

Otherwise, run these steps:

    1. 

Set item["[value](#dom-cookielistitem-value)"] to undefined.

    2. 

[Append](https://infra.spec.whatwg.org/#list-append)item to deletedList.

4. 

Return changedList and deletedList.

## 8. Security considerations#security

Other than cookie access from service worker contexts, this API is not intended to expose any new capabilities to the web.

### 8.1. Gotcha!#gotcha

Although browser cookie implementations are now evolving in the direction of better security and fewer surprising and error-prone defaults, there are at present few guarantees about cookie data security.

- 

unsecured origins can typically overwrite cookies used on secure origins

- 

superdomains can typically overwrite cookies seen by subdomains

- 

cross-site scripting attacks and other script and header injection attacks can be used to forge cookies too

- 

cookie read operations (both from script and on web servers) don’t give any indication of where the cookie came from

- 

browsers sometimes truncate, transform or evict cookie data in surprising and counterintuitive ways

  - 

... due to reaching storage limits

  - 

... due to character encoding differences

  - 

... due to differing syntactic and semantic rules for cookies

For these reasons it is best to use caution when interpreting any cookie’s value, and never execute a cookie’s value as script, HTML, CSS, XML, PDF, or any other executable format.

### 8.2. Restrict?#restrict

This API may have the unintended side-effect of making cookies easier to use and consequently encouraging their further use. If it causes their further use in [non-secure contexts](https://html.spec.whatwg.org/multipage/webappapis.html#non-secure-context) this could result in a web less safe for users. For that reason this API has been restricted to [secure contexts](https://html.spec.whatwg.org/multipage/webappapis.html#secure-context) only.

### 8.3. Secure cookies#secure-cookies

This section is non-normative.

This API only allows writes for `Secure` cookies to encourage better decisions around security. However the API will still allow reading non-`Secure` cookies in order to facilitate the migration to `Secure` cookies. As a side-effect, when fetching and modifying a non-`Secure` cookie with this API, the non-`Secure` cookie will automatically be modified to `Secure`.

### 8.4. Surprises#surprises

Some existing cookie behavior (especially domain-rather-than-origin orientation, [non-secure contexts](https://html.spec.whatwg.org/multipage/webappapis.html#non-secure-context) being able to set cookies readable in [secure contexts](https://html.spec.whatwg.org/multipage/webappapis.html#secure-context), and script being able to set cookies unreadable from script contexts) may be quite surprising from a web security standpoint.

Other surprises are documented in [Cookies § Introduction](https://tools.ietf.org/html/draft-ietf-httpbis-rfc6265bis-14#name-introduction) - for instance, a cookie may be set for a superdomain (e.g. app.example.com may set a cookie for the whole example.com domain), and a cookie may be readable across all port numbers on a given domain name.

Further complicating this are historical differences in cookie-handling across major browsers, although some of those (e.g. port number handling) are now handled with more consistency than they once were.

### 8.5. Prefixes#prefixes

Where feasible the examples use the `__Host-` and `__Secure-` name prefixes which causes some current browsers to disallow overwriting from [non-secure contexts](https://html.spec.whatwg.org/multipage/webappapis.html#non-secure-context), disallow overwriting with no `Secure` flag, and — in the case of `__Host-` — disallow overwriting with an explicit `Domain` or non-'/' `Path` attribute (effectively enforcing same-origin semantics.) These prefixes provide important security benefits in those browsers implementing Secure Cookies and degrade gracefully (i.e. the special semantics may not be enforced in other cookie APIs but the cookies work normally and the async cookies API enforces the secure semantics for write operations) in other browsers. A major goal of this API is interoperation with existing cookies, though, so a few examples have also been provided using cookie names lacking these prefixes.

Prefix rules are also enforced in write operations by this API, but may not be enforced in the same browser for other APIs. For this reason it is inadvisable to rely on their enforcement too heavily until and unless they are more broadly adopted.

### 8.6. URL scoping#url-scoping

Although a service worker script cannot directly access cookies today, it can already use controlled rendering of in-scope HTML and script resources to inject cookie-monitoring code under the remote control of the service worker script. This means that cookie access inside the scope of the service worker is technically possible already, it’s just not very convenient.

When the service worker is scoped more narrowly than `/` it may still be able to read path-scoped cookies from outside its scope’s path space by successfully guessing/constructing a 404 page URL which allows IFRAME-ing and then running script inside it the same technique could expand to the whole origin, but a carefully constructed site (one where no out-of-scope pages are IFRAME-able) can actually deny this capability to a path-scoped service worker today and I was reluctant to remove that restriction without further discussion of the implications.

### 8.7. Cookie aversion#aversion

To reduce complexity for developers and eliminate the need for ephemeral test cookies, this async cookies API will explicitly reject attempts to write or delete cookies when the operation would be ignored. Likewise it will explicitly reject attempts to read cookies when that operation would ignore actual cookie data and simulate an empty cookie jar. Attempts to observe cookie changes in these contexts will still "work", but won’t invoke the callback until and unless read access becomes allowed (due e.g. to changed site permissions.)

Today writing to [document.cookie](https://html.spec.whatwg.org/multipage/dom.html#dom-document-cookie) in contexts where script-initiated cookie-writing is disallowed typically is a no-op. However, many cookie-writing scripts and frameworks always write a test cookie and then check for its existence to determine whether script-initiated cookie-writing is possible.

Likewise, today reading [document.cookie](https://html.spec.whatwg.org/multipage/dom.html#dom-document-cookie) in contexts where script-initiated cookie-reading is disallowed typically returns an empty string. However, a cooperating web server can verify that server-initiated cookie-writing and cookie-reading work and report this to the script (which still sees empty string) and the script can use this information to infer that script-initiated cookie-reading is disallowed.

## 9. Privacy considerations#privacy

### 9.1. Clear cookies#clear-cookies

This section is non-normative.

When a user clears cookies for an origin, the user agent needs to wipe all storage for that origin; including service workers and DOM-accessible storage for that origin. This is to prevent websites from restoring any user identifiers in persistent storage after a user initiates the action.

## Acknowledgments#acknowledgements

Thanks to Benjamin Sittler, who created the initial proposal for this API.

Many thanks to Adam Barth, Alex Russell, Andrea Marchesini, Andrew Williams, Anne van Kesteren, Ayu Ishii Ben Kelly, Craig Francis, Daniel Appelquist, Daniel Murphy, Domenic Denicola, Elliott Sprehn, Fagner Brack, Idan Horowitz, Jake Archibald, Joel Weinberger, Joshua Bell, Kenneth Rohde Christiansen, Lukasz Olejnik, Marijn Kruisselbrink, Mike West, Raymond Toy, Rupin Mittal, Tab Atkins, and Victor Costan for helping craft this standard.

This standard is written by Dylan Cutler ([Google](https://www.google.com/), [dylancutler@google.com](mailto:dylancutler@google.com)).

## Intellectual property rights#ipr

This Living Standard was originally developed in the W3C WICG, where it was available under the [W3C Software and Document License](https://www.w3.org/Consortium/Legal/2015/copyright-software-and-document). 

Copyright © WHATWG (Apple, Google, Mozilla, Microsoft). This work is licensed under a [Creative Commons Attribution 4.0
International License](https://creativecommons.org/licenses/by/4.0/). To the extent portions of it are incorporated into source code, such portions in the source code are licensed under the [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause) instead.

This is the Living Standard. Those interested in the patent-review version should view the [Living Standard Review Draft](/review-drafts/2025-11/).

## Index#index

### Terms defined by this specification#index-defined-here

-  associated CookieStore 

  - [dfn for ServiceWorkerGlobalScope](#serviceworkerglobalscope-associated-cookiestore), in § 6.2
  - [dfn for Window](#window-associated-cookiestore), in § 6.1

-  changed 

  - [attribute for CookieChangeEvent](#dom-cookiechangeevent-changed), in § 5.1
  - [attribute for ExtendableCookieChangeEvent](#dom-extendablecookiechangeevent-changed), in § 5.2
  - [dict-member for CookieChangeEventInit](#dom-cookiechangeeventinit-changed), in § 5.1
  - [dict-member for ExtendableCookieChangeEventInit](#dom-extendablecookiechangeeventinit-changed), in § 5.2

-  constructor(type) 

  - [constructor for CookieChangeEvent](#dom-cookiechangeevent-cookiechangeevent), in § 5.1
  - [constructor for ExtendableCookieChangeEvent](#dom-extendablecookiechangeevent-extendablecookiechangeevent), in § 5.2

-  constructor(type, eventInitDict) 

  - [constructor for CookieChangeEvent](#dom-cookiechangeevent-cookiechangeevent), in § 5.1
  - [constructor for ExtendableCookieChangeEvent](#dom-extendablecookiechangeevent-extendablecookiechangeevent), in § 5.2

- [cookie](#cookie), in § 2.1
- [cookie change](#cookie-change), in § 7.4
- [CookieChangeEvent](#cookiechangeevent), in § 5.1
- [CookieChangeEventInit](#dictdef-cookiechangeeventinit), in § 5.1
- [CookieChangeEvent(type)](#dom-cookiechangeevent-cookiechangeevent), in § 5.1
- [CookieChangeEvent(type, eventInitDict)](#dom-cookiechangeevent-cookiechangeevent), in § 5.1
- [cookie change subscription](#cookie-change-subscription), in § 2.3
- [cookie change subscription list](#cookie-change-subscription-list), in § 2.3
- [CookieInit](#dictdef-cookieinit), in § 3
- [CookieList](#typedefdef-cookielist), in § 3
- [CookieListItem](#dictdef-cookielistitem), in § 3
- [cookies](#dom-serviceworkerregistration-cookies), in § 4.4
- [CookieSameSite](#enumdef-cookiesamesite), in § 3
- [cookie store](#cookie-store), in § 2.2
- [CookieStore](#cookiestore), in § 3
-  cookieStore 

  - [attribute for ServiceWorkerGlobalScope](#dom-serviceworkerglobalscope-cookiestore), in § 6.2
  - [attribute for Window](#dom-window-cookiestore), in § 6.1

- [CookieStoreDeleteOptions](#dictdef-cookiestoredeleteoptions), in § 3
- [CookieStoreGetOptions](#dictdef-cookiestoregetoptions), in § 3
- [CookieStoreManager](#cookiestoremanager), in § 4
- [create a CookieListItem](#create-a-cookielistitem), in § 7.1
- [date serialize](#date-serialize), in § 7
- [delete a cookie](#delete-a-cookie), in § 7.3
-  deleted 

  - [attribute for CookieChangeEvent](#dom-cookiechangeevent-deleted), in § 5.1
  - [attribute for ExtendableCookieChangeEvent](#dom-extendablecookiechangeevent-deleted), in § 5.2
  - [dict-member for CookieChangeEventInit](#dom-cookiechangeeventinit-deleted), in § 5.1
  - [dict-member for ExtendableCookieChangeEventInit](#dom-extendablecookiechangeeventinit-deleted), in § 5.2

- [delete(name)](#dom-cookiestore-delete), in § 3.4
- [delete(options)](#dom-cookiestore-delete-options), in § 3.4
-  domain 

  - [dfn for cookie](#cookie-domain), in § 2.1
  - [dict-member for CookieInit](#dom-cookieinit-domain), in § 3
  - [dict-member for CookieStoreDeleteOptions](#dom-cookiestoredeleteoptions-domain), in § 3

- [expires](#dom-cookieinit-expires), in § 3
- [ExtendableCookieChangeEvent](#extendablecookiechangeevent), in § 5.2
- [ExtendableCookieChangeEventInit](#dictdef-extendablecookiechangeeventinit), in § 5.2
- [ExtendableCookieChangeEvent(type)](#dom-extendablecookiechangeevent-extendablecookiechangeevent), in § 5.2
- [ExtendableCookieChangeEvent(type, eventInitDict)](#dom-extendablecookiechangeevent-extendablecookiechangeevent), in § 5.2
- [fire a change event](#fire-a-change-event), in § 7.4
- [get()](#dom-cookiestore-get-options), in § 3.1
- [getAll()](#dom-cookiestore-getall-options), in § 3.2
- [getAll(name)](#dom-cookiestore-getall), in § 3.2
- [getAll(options)](#dom-cookiestore-getall-options), in § 3.2
- [get(name)](#dom-cookiestore-get), in § 3.1
- [get(options)](#dom-cookiestore-get-options), in § 3.1
- [getSubscriptions()](#dom-cookiestoremanager-getsubscriptions), in § 4.2
- [http-only-flag](#cookie-http-only-flag), in § 2.1
- ["lax"](#dom-cookiesamesite-lax), in § 3
- [maxAge](#dom-cookieinit-maxage), in § 3
- [maximum attribute value size](#cookie-maximum-attribute-value-size), in § 2.1
- [maximum name/value pair size](#cookie-maximum-name-value-pair-size), in § 2.1
-  name 

  - [dfn for cookie](#cookie-name), in § 2.1
  - [dfn for cookie change subscription](#cookie-change-subscription-name), in § 2.3
  - [dict-member for CookieInit](#dom-cookieinit-name), in § 3
  - [dict-member for CookieListItem](#dom-cookielistitem-name), in § 3
  - [dict-member for CookieStoreDeleteOptions](#dom-cookiestoredeleteoptions-name), in § 3
  - [dict-member for CookieStoreGetOptions](#dom-cookiestoregetoptions-name), in § 3

- ["none"](#dom-cookiesamesite-none), in § 3
- [normalize](#normalize-a-cookie-name-or-value), in § 2.1
- [normalize a cookie name or value](#normalize-a-cookie-name-or-value), in § 2.1
- [observable changes](#observable-changes), in § 7.4
- [onchange](#dom-cookiestore-onchange), in § 3
- [oncookiechange](#dom-serviceworkerglobalscope-oncookiechange), in § 6.2
-  partitioned 

  - [dict-member for CookieInit](#dom-cookieinit-partitioned), in § 3
  - [dict-member for CookieStoreDeleteOptions](#dom-cookiestoredeleteoptions-partitioned), in § 3

-  path 

  - [dfn for cookie](#cookie-path), in § 2.1
  - [dict-member for CookieInit](#dom-cookieinit-path), in § 3
  - [dict-member for CookieStoreDeleteOptions](#dom-cookiestoredeleteoptions-path), in § 3

- [prepare lists](#prepare-lists), in § 7.4
- [process cookie changes](#process-cookie-changes), in § 7.4
- [query cookies](#query-cookies), in § 7.1
- [registration](#cookiestoremanager-registration), in § 4
- [sameSite](#dom-cookieinit-samesite), in § 3
- [script-visible](#script-visible), in § 2.1
- [set a cookie](#set-a-cookie), in § 7.2
- [set(name, value)](#dom-cookiestore-set), in § 3.3
- [set(options)](#dom-cookiestore-set-options), in § 3.3
- ["strict"](#dom-cookiesamesite-strict), in § 3
- [subscribe(subscriptions)](#dom-cookiestoremanager-subscribe), in § 4.1
- [unsubscribe(subscriptions)](#dom-cookiestoremanager-unsubscribe), in § 4.3
-  url 

  - [dfn for cookie change subscription](#cookie-change-subscription-url), in § 2.3
  - [dict-member for CookieStoreGetOptions](#dom-cookiestoregetoptions-url), in § 3

-  value 

  - [dfn for cookie](#cookie-value), in § 2.1
  - [dict-member for CookieInit](#dom-cookieinit-value), in § 3
  - [dict-member for CookieListItem](#dom-cookielistitem-value), in § 3

### Terms defined by reference#index-defined-elsewhere

- [DOM] defines the following terms: 

  - Event
  - EventInit
  - EventTarget
  - bubbles
  - cancelable
  - creating an event
  - dispatch
  - document
  - type

- [ECMA262] defines the following terms: 

  - ToString

- [ENCODING] defines the following terms: 

  - UTF-8 decode without BOM
  - UTF-8 encode

- [FETCH] defines the following terms: 

  - fetch
  - serialized cookie default path

- [HR-TIME-3] defines the following terms: 

  - DOMHighResTimeStamp

- [HTML] defines the following terms: 

  - EventHandler
  - Window
  - API base URL
  - cookie
  - creation URL
  - DOM manipulation task source
  - domain
  - in parallel
  - is a registrable domain suffix of or is equal to
  - non-secure context
  - opaque origin
  - origin
  - queue a global task
  - relevant global object
  - relevant settings object
  - replaceState(data, unused, url)
  - same origin
  - secure context

- [INFRA] defines the following terms: 

  - 64-bit signed integer
  - append (for list)
  - append (for set)
  - boolean
  - break
  - byte
  - byte sequence
  - byte-lowercase
  - c0 control
  - contain
  - continue
  - exist
  - for each
  - implementation-defined
  - is empty (for list)
  - is empty (for map)
  - item
  - length (for byte sequence)
  - length (for string)
  - list
  - remove
  - scalar value string
  - set
  - starts with
  - string
  - tuple
  - with default

- [Service-Workers] defines the following terms: 

  - ExtendableEvent
  - ExtendableEventInit
  - ServiceWorkerGlobalScope
  - ServiceWorkerRegistration
  - fire a functional event
  - scope url
  - service worker
  - service worker registration

- [URL] defines the following terms: 

  - basic URL parser
  - equal
  - exclude fragments
  - host
  - host parser
  - origin
  - URL

- [WEBIDL] defines the following terms: 

  - DOMException
  - DOMString
  - Exposed
  - FrozenArray
  - Promise
  - SameObject
  - SecureContext
  - SecurityError
  - TypeError
  - USVString
  - a new promise
  - a promise rejected with
  - boolean
  - long long
  - reject
  - resolve
  - sequence
  - this
  - undefined

## References#references

### Normative References#normative

[DOM] Anne van Kesteren. [DOM Standard](https://dom.spec.whatwg.org/). Living Standard. URL: [https://dom.spec.whatwg.org/](https://dom.spec.whatwg.org/)[ENCODING] Anne van Kesteren. [Encoding Standard](https://encoding.spec.whatwg.org/). Living Standard. URL: [https://encoding.spec.whatwg.org/](https://encoding.spec.whatwg.org/)[FETCH] Anne van Kesteren. [Fetch Standard](https://fetch.spec.whatwg.org/). Living Standard. URL: [https://fetch.spec.whatwg.org/](https://fetch.spec.whatwg.org/)[HR-TIME-3] Yoav Weiss. [High Resolution Time](https://w3c.github.io/hr-time/). URL: [https://w3c.github.io/hr-time/](https://w3c.github.io/hr-time/)[HTML] Anne van Kesteren; et al. [HTML Standard](https://html.spec.whatwg.org/multipage/). Living Standard. URL: [https://html.spec.whatwg.org/multipage/](https://html.spec.whatwg.org/multipage/)[INFRA] Anne van Kesteren; Domenic Denicola. [Infra Standard](https://infra.spec.whatwg.org/). Living Standard. URL: [https://infra.spec.whatwg.org/](https://infra.spec.whatwg.org/)[RFC6265BIS-14] S. Bingler; M. West; J. Wilander. [Cookies: HTTP State Management Mechanism](https://tools.ietf.org/html/draft-ietf-httpbis-rfc6265bis-14). Internet-Draft. URL: [https://tools.ietf.org/html/draft-ietf-httpbis-rfc6265bis-14](https://tools.ietf.org/html/draft-ietf-httpbis-rfc6265bis-14)[Service-Workers] Monica CHINTALA; Yoshisato Yanagisawa. [Service Workers Nightly](https://w3c.github.io/ServiceWorker/). URL: [https://w3c.github.io/ServiceWorker/](https://w3c.github.io/ServiceWorker/)[URL] Anne van Kesteren. [URL Standard](https://url.spec.whatwg.org/). Living Standard. URL: [https://url.spec.whatwg.org/](https://url.spec.whatwg.org/)[WEBIDL] Edgar Chen; Timothy Gu. [Web IDL Standard](https://webidl.spec.whatwg.org/). Living Standard. URL: [https://webidl.spec.whatwg.org/](https://webidl.spec.whatwg.org/)

## IDL Index#idl-index

```
[Exposedhttps://webidl.spec.whatwg.org/#Exposed=(ServiceWorker,Window),
 SecureContexthttps://webidl.spec.whatwg.org/#SecureContext]
interface CookieStore#cookiestore : EventTargethttps://dom.spec.whatwg.org/#eventtarget {
  Promisehttps://webidl.spec.whatwg.org/#idl-promise<CookieListItem#dictdef-cookielistitem?> get#dom-cookiestore-get(USVStringhttps://webidl.spec.whatwg.org/#idl-USVString name#dom-cookiestore-get-name-name);
  Promisehttps://webidl.spec.whatwg.org/#idl-promise<CookieListItem#dictdef-cookielistitem?> get#dom-cookiestore-get-options(optional CookieStoreGetOptions#dictdef-cookiestoregetoptions options#dom-cookiestore-get-options-options = {});

  Promisehttps://webidl.spec.whatwg.org/#idl-promise<CookieList#typedefdef-cookielist> getAll#dom-cookiestore-getall(USVStringhttps://webidl.spec.whatwg.org/#idl-USVString name#dom-cookiestore-getall-name-name);
  Promisehttps://webidl.spec.whatwg.org/#idl-promise<CookieList#typedefdef-cookielist> getAll#dom-cookiestore-getall-options(optional CookieStoreGetOptions#dictdef-cookiestoregetoptions options#dom-cookiestore-getall-options-options = {});

  Promisehttps://webidl.spec.whatwg.org/#idl-promise<undefinedhttps://webidl.spec.whatwg.org/#idl-undefined> set#dom-cookiestore-set(USVStringhttps://webidl.spec.whatwg.org/#idl-USVString name#dom-cookiestore-set-name-value-name, USVStringhttps://webidl.spec.whatwg.org/#idl-USVString value#dom-cookiestore-set-name-value-value);
  Promisehttps://webidl.spec.whatwg.org/#idl-promise<undefinedhttps://webidl.spec.whatwg.org/#idl-undefined> set#dom-cookiestore-set-options(CookieInit#dictdef-cookieinit options#dom-cookiestore-set-options-options);

  Promisehttps://webidl.spec.whatwg.org/#idl-promise<undefinedhttps://webidl.spec.whatwg.org/#idl-undefined> delete#dom-cookiestore-delete(USVStringhttps://webidl.spec.whatwg.org/#idl-USVString name#dom-cookiestore-delete-name-name);
  Promisehttps://webidl.spec.whatwg.org/#idl-promise<undefinedhttps://webidl.spec.whatwg.org/#idl-undefined> delete#dom-cookiestore-delete-options(CookieStoreDeleteOptions#dictdef-cookiestoredeleteoptions options#dom-cookiestore-delete-options-options);

  [Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window]
  attribute EventHandlerhttps://html.spec.whatwg.org/multipage/webappapis.html#eventhandler onchange#dom-cookiestore-onchange;
};

dictionary CookieStoreGetOptions#dictdef-cookiestoregetoptions {
  USVStringhttps://webidl.spec.whatwg.org/#idl-USVString name#dom-cookiestoregetoptions-name;
  USVStringhttps://webidl.spec.whatwg.org/#idl-USVString url#dom-cookiestoregetoptions-url;
};

enum CookieSameSite#enumdef-cookiesamesite {
  "strict"#dom-cookiesamesite-strict,
  "lax"#dom-cookiesamesite-lax,
  "none"#dom-cookiesamesite-none
};

dictionary CookieInit#dictdef-cookieinit {
  required USVStringhttps://webidl.spec.whatwg.org/#idl-USVString name#dom-cookieinit-name;
  required USVStringhttps://webidl.spec.whatwg.org/#idl-USVString value#dom-cookieinit-value;
  DOMHighResTimeStamphttps://w3c.github.io/hr-time/#dom-domhighrestimestamp? expires#dom-cookieinit-expires = null;
  USVStringhttps://webidl.spec.whatwg.org/#idl-USVString? domain#dom-cookieinit-domain = null;
  USVStringhttps://webidl.spec.whatwg.org/#idl-USVString path#dom-cookieinit-path = "/";
  CookieSameSite#enumdef-cookiesamesite sameSite#dom-cookieinit-samesite = "strict";
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean partitioned#dom-cookieinit-partitioned = false;
  long longhttps://webidl.spec.whatwg.org/#idl-long-long? maxAge#dom-cookieinit-maxage = null;
};

dictionary CookieStoreDeleteOptions#dictdef-cookiestoredeleteoptions {
  required USVStringhttps://webidl.spec.whatwg.org/#idl-USVString name#dom-cookiestoredeleteoptions-name;
  USVStringhttps://webidl.spec.whatwg.org/#idl-USVString? domain#dom-cookiestoredeleteoptions-domain = null;
  USVStringhttps://webidl.spec.whatwg.org/#idl-USVString path#dom-cookiestoredeleteoptions-path = "/";
  booleanhttps://webidl.spec.whatwg.org/#idl-boolean partitioned#dom-cookiestoredeleteoptions-partitioned = false;
};

dictionary CookieListItem#dictdef-cookielistitem {
  USVStringhttps://webidl.spec.whatwg.org/#idl-USVString name#dom-cookielistitem-name;
  USVStringhttps://webidl.spec.whatwg.org/#idl-USVString value#dom-cookielistitem-value;
};

typedef sequencehttps://webidl.spec.whatwg.org/#idl-sequence<CookieListItem#dictdef-cookielistitem> CookieList#typedefdef-cookielist;

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=(ServiceWorker,Window),
 SecureContexthttps://webidl.spec.whatwg.org/#SecureContext]
interface CookieStoreManager#cookiestoremanager {
  Promisehttps://webidl.spec.whatwg.org/#idl-promise<undefinedhttps://webidl.spec.whatwg.org/#idl-undefined> subscribe#dom-cookiestoremanager-subscribe(sequencehttps://webidl.spec.whatwg.org/#idl-sequence<CookieStoreGetOptions#dictdef-cookiestoregetoptions> subscriptions#dom-cookiestoremanager-subscribe-subscriptions-subscriptions);
  Promisehttps://webidl.spec.whatwg.org/#idl-promise<sequencehttps://webidl.spec.whatwg.org/#idl-sequence<CookieStoreGetOptions#dictdef-cookiestoregetoptions>> getSubscriptions#dom-cookiestoremanager-getsubscriptions();
  Promisehttps://webidl.spec.whatwg.org/#idl-promise<undefinedhttps://webidl.spec.whatwg.org/#idl-undefined> unsubscribe#dom-cookiestoremanager-unsubscribe(sequencehttps://webidl.spec.whatwg.org/#idl-sequence<CookieStoreGetOptions#dictdef-cookiestoregetoptions> subscriptions#dom-cookiestoremanager-unsubscribe-subscriptions-subscriptions);
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=(ServiceWorker,Window)]
partial interface ServiceWorkerRegistrationhttps://w3c.github.io/ServiceWorker/#serviceworkerregistration {
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute CookieStoreManager#cookiestoremanager cookies#dom-serviceworkerregistration-cookies;
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=Window,
 SecureContexthttps://webidl.spec.whatwg.org/#SecureContext]
interface CookieChangeEvent#cookiechangeevent : Eventhttps://dom.spec.whatwg.org/#event {
  constructor#dom-cookiechangeevent-cookiechangeevent(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString type#dom-cookiechangeevent-cookiechangeevent-type-eventinitdict-type, optional CookieChangeEventInit#dictdef-cookiechangeeventinit eventInitDict#dom-cookiechangeevent-cookiechangeevent-type-eventinitdict-eventinitdict = {});
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute FrozenArrayhttps://webidl.spec.whatwg.org/#idl-frozen-array<CookieListItem#dictdef-cookielistitem> changed#dom-cookiechangeevent-changed;
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute FrozenArrayhttps://webidl.spec.whatwg.org/#idl-frozen-array<CookieListItem#dictdef-cookielistitem> deleted#dom-cookiechangeevent-deleted;
};

dictionary CookieChangeEventInit#dictdef-cookiechangeeventinit : EventInithttps://dom.spec.whatwg.org/#dictdef-eventinit {
  CookieList#typedefdef-cookielist changed#dom-cookiechangeeventinit-changed;
  CookieList#typedefdef-cookielist deleted#dom-cookiechangeeventinit-deleted;
};

[Exposedhttps://webidl.spec.whatwg.org/#Exposed=ServiceWorker]
interface ExtendableCookieChangeEvent#extendablecookiechangeevent : ExtendableEventhttps://w3c.github.io/ServiceWorker/#extendableevent {
  constructor#dom-extendablecookiechangeevent-extendablecookiechangeevent(DOMStringhttps://webidl.spec.whatwg.org/#idl-DOMString type#dom-extendablecookiechangeevent-extendablecookiechangeevent-type-eventinitdict-type, optional ExtendableCookieChangeEventInit#dictdef-extendablecookiechangeeventinit eventInitDict#dom-extendablecookiechangeevent-extendablecookiechangeevent-type-eventinitdict-eventinitdict = {});
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute FrozenArrayhttps://webidl.spec.whatwg.org/#idl-frozen-array<CookieListItem#dictdef-cookielistitem> changed#dom-extendablecookiechangeevent-changed;
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute FrozenArrayhttps://webidl.spec.whatwg.org/#idl-frozen-array<CookieListItem#dictdef-cookielistitem> deleted#dom-extendablecookiechangeevent-deleted;
};

dictionary ExtendableCookieChangeEventInit#dictdef-extendablecookiechangeeventinit : ExtendableEventInithttps://w3c.github.io/ServiceWorker/#dictdef-extendableeventinit {
  CookieList#typedefdef-cookielist changed#dom-extendablecookiechangeeventinit-changed;
  CookieList#typedefdef-cookielist deleted#dom-extendablecookiechangeeventinit-deleted;
};

[SecureContexthttps://webidl.spec.whatwg.org/#SecureContext]
partial interface Windowhttps://html.spec.whatwg.org/multipage/nav-history-apis.html#window {
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute CookieStore#cookiestore cookieStore#dom-window-cookiestore;
};

partial interface ServiceWorkerGlobalScopehttps://w3c.github.io/ServiceWorker/#serviceworkerglobalscope {
  [SameObjecthttps://webidl.spec.whatwg.org/#SameObject] readonly attribute CookieStore#cookiestore cookieStore#dom-serviceworkerglobalscope-cookiestore;

  attribute EventHandlerhttps://html.spec.whatwg.org/multipage/webappapis.html#eventhandler oncookiechange#dom-serviceworkerglobalscope-oncookiechange;
};

```
