Indexing your offline-capable pages with the Content Indexing API | Capabilities | Chrome for Developers[Skip to main content](#main-content)/

- 

[Docs](https://developer.chrome.com/docs)

- Build with Chrome
- Learn how Chrome works, participate in origin trials, and build with Chrome everywhere. 
- [Web Platform](https://developer.chrome.com/docs/web-platform)
- [Capabilities](https://developer.chrome.com/docs/capabilities)
- [ChromeDriver](https://developer.chrome.com/docs/chromedriver)
- [Extensions](https://developer.chrome.com/docs/extensions)
- [Chrome Web Store](https://developer.chrome.com/docs/webstore)
- [Chromium](https://developer.chrome.com/docs/chromium)
- [Web on Android](https://developer.chrome.com/docs/android)
- [Origin trials](https://developer.chrome.com/origintrials/)
- [Release notes](https://developer.chrome.com/release-notes)

- Productivity
- Create the best experience for your users with the web's best tools.
- [DevTools](https://developer.chrome.com/docs/devtools)
- [Lighthouse](https://developer.chrome.com/docs/lighthouse)
- [Chrome UX Report](https://developer.chrome.com/docs/crux)
- [Accessibility](https://developer.chrome.com/docs/accessibility)

- Get things done quicker and neater, with our ready-made libraries. 
- [Workbox](https://developer.chrome.com/docs/workbox)
- [Puppeteer](https://developer.chrome.com/docs/puppeteer)

- Experience
- Design a beautiful and performant web with Chrome. 
- [AI](https://developer.chrome.com/docs/ai)
- [Performance](https://developer.chrome.com/docs/performance)
- [CSS and UI](https://developer.chrome.com/docs/css-ui)
- [Identity](https://developer.chrome.com/docs/identity)
- [Payments](https://developer.chrome.com/docs/payments)
- [Privacy and security](https://developer.chrome.com/docs/privacy-security)

- Resources
- More from Chrome and Google. 
- [All documentation](https://developer.chrome.com/docs)
- [Baseline](https://web.dev/baseline)
- [web.dev](https://web.dev)
- [PageSpeed Insights audit](https://pagespeed.web.dev)
- [The Privacy Sandbox](https://developers.google.com/privacy-sandbox)
- [Isolated Web Apps (IWA)](https://developer.chrome.com/docs/iwa)

[Case studies](https://developer.chrome.com/case-studies)[Blog](https://developer.chrome.com/blog)[New in Chrome](https://developer.chrome.com/new)/

- English
- Deutsch
- Español – América Latina
- Français
- Indonesia
- Italiano
- Nederlands
- Polski
- Português – Brasil
- Tiếng Việt
- Türkçe
- Русский
- עברית
- العربيّة
- فارسی
- हिंदी
- বাংলা
- ภาษาไทย
- 中文 – 简体
- 中文 – 繁體
- 日本語
- 한국어

Sign in

- [Capabilities](https://developer.chrome.com/docs/capabilities)

/

- 

- [Docs](/docs)

  -  More 

- [Case studies](/case-studies)
- [Blog](/blog)
- [New in Chrome](/new)

-  Build with Chrome 
- [Web Platform](/docs/web-platform)
- [Capabilities](/docs/capabilities)
- [ChromeDriver](/docs/chromedriver)
- [Extensions](/docs/extensions)
- [Chrome Web Store](/docs/webstore)
- [Chromium](/docs/chromium)
- [Web on Android](/docs/android)
- [Origin trials](https://developer.chrome.com/origintrials/)
- [Release notes](/release-notes)
-  Productivity 
- [DevTools](/docs/devtools)
- [Lighthouse](/docs/lighthouse)
- [Chrome UX Report](/docs/crux)
- [Accessibility](/docs/accessibility)
- [Workbox](/docs/workbox)
- [Puppeteer](/docs/puppeteer)
-  Experience 
- [AI](/docs/ai)
- [Performance](/docs/performance)
- [CSS and UI](/docs/css-ui)
- [Identity](/docs/identity)
- [Payments](/docs/payments)
- [Privacy and security](/docs/privacy-security)
-  Resources 
- [All documentation](/docs)
- [Baseline](https://web.dev/baseline)
- [web.dev](https://web.dev)
- [PageSpeed Insights audit](https://pagespeed.web.dev)
- [The Privacy Sandbox](https://developers.google.com/privacy-sandbox)
- [Isolated Web Apps (IWA)](/docs/iwa)

- [Home](https://developer.chrome.com/)
- [Docs](https://developer.chrome.com/docs)
- [Capabilities](https://developer.chrome.com/docs/capabilities)

#  Indexing your offline-capable pages with the Content Indexing API Stay organized with collections  Save and categorize content based on your preferences. 

Enabling service workers to tell browsers which pages work offline

 Jeff Posnick https://twitter.com/jeffposnickhttps://github.com/jeffposnickhttps://jeffy.info/

Success: The Content Indexing API, part of the [capabilities project](/docs/capabilities/status), launched in Chrome 84 for Android.

## What is the Content Indexing API?

Using a [progressive web app](https://web.dev/explore/progressive-web-apps) means having access to information people care about—images, videos, articles, and more—regardless of the current state of your network connection. Technologies like [service workers](/docs/workbox/service-worker-overview), the [Cache Storage API](https://web.dev/articles/cache-api-quick-guide), and [IndexedDB](https://developer.mozilla.org/docs/Web/API/IndexedDB_API) provide you with the building blocks for storing and serving data when folks interact directly with a PWA. But building a high-quality, offline-first PWA is only part of the story. If folks don't realize that a web app's content is available while they're offline, they won't take full advantage of the work you put into implementing that functionality.

This is a discovery problem; how can your PWA make users aware of its offline-capable content so that they can discover and view what's available? The Content Indexing API is a solution to this problem. The developer-facing portion of this solution is an extension to service workers, which allows developers to add URLs and metadata of offline-capable pages to a local index maintained by the browser. That enhancement is available in Chrome 84 and later.

Once the index is populated with content from your PWA, as well as any other installed PWAs, it will be surfaced by the browser as shown below.

 First, select the Downloads menu item on Chrome's new tab page.  Media and articles that have been added to the index will be shown in the Articles for You section. 

Additionally, Chrome can proactively recommend content when it detects that a user is offline.

The Content Indexing API is not an alternative way of caching content. It's a way of providing metadata about pages that are already cached by your service worker, so that the browser can surface those pages when folks are likely to want to view them. The Content Indexing API helps with discoverability of cached pages.

Note: The Content Indexing API is not a searchable index. While you can get a list of all indexed entries, there's no way to query against indexed metadata directly.

## See it in action

The best way to get a feel for the Content Indexing API is to try a sample application.

1. Make sure that you're using a supported browser and platform. Currently, that's limited to Chrome 84 or later on Android. Go to `about://version` to see what version of Chrome you're running.
2. Visit [https://contentindex.dev](https://contentindex.dev)
3. Click the `+` button next to one or more of the items on the list.
4. (Optional) Disable your device's Wi-Fi and cellular data connection, or enable airplane mode to simulate taking your browser offline.
5. Choose Downloads from Chrome's menu, and switch to the Articles for You tab.
6. Browse through the content that you previously saved.

You can view [the source of the sample application on GitHub](https://github.com/rayankans/contentindex.dev).

Another sample application, a [Scrapbook PWA](https://scrapbook-pwa.web.app/), illustrates the use of the Content Indexing API with the [Web Share Target API](https://web.dev/web-share-target). The [code demonstrates a technique](https://github.com/GoogleChrome/samples/blob/gh-pages/web-share/src/js/contentIndexing.js) for keeping the Content Indexing API in sync with items stored by a web app using the [Cache Storage API](https://web.dev/cache-api-quick-guide).

## Using the API

To use the API your app must have a service worker and URLs that are navigable offline. If your web app does not currently have a service worker, the [Workbox libraries](/docs/workbox) can simplify creating one.

### What type of URLs can be indexed as offline-capable?

The API supports indexing URLs corresponding to HTML documents. A URL for a cached media file, for example, can't be indexed directly. Instead, you need to provide a URL for a page that displays media, and which works offline.

A recommended pattern is to create a "viewer" HTML page that could accept the underlying media URL as a query parameter and then display the contents of the file, potentially with additional controls or content on the page.

Web apps can only add URLs to the content index that are under the [scope](https://web.dev/learn/pwa/service-workers) of the current service worker. In other words, a web app could not add a URL belonging to a completely different domain into the content index.

### Overview

The Content Indexing API supports three operations: adding, listing, and removing metadata. These methods are exposed from a new property, `index`, that has been added to the [ServiceWorkerRegistration](https://developer.mozilla.org/docs/Web/API/ServiceWorkerRegistration) interface.

The first step in indexing content is getting a reference to the current [ServiceWorkerRegistration](https://developer.mozilla.org/docs/Web/API/ServiceWorkerRegistration). Using [navigator.serviceWorker.ready](https://developer.mozilla.org/docs/Web/API/ServiceWorkerContainer/ready) is the most straightforward way:

```
const registration = await navigator.serviceWorker.ready;

// Remember to feature-detect before using the API:
if ('index' in registration) {
  // Your Content Indexing API code goes here!
}
```

If you're making calls to the Content Indexing API from within a service worker, rather than inside a web page, you can refer to the `ServiceWorkerRegistration` directly via `registration`. It will [already be defined](https://developer.mozilla.org/docs/Web/API/ServiceWorkerGlobalScope/registration) as part of the `ServiceWorkerGlobalScope.`

### Adding to the index

Use the `add()` method to index URLs and their associated metadata. It's up to you to choose when items are added to the index. You might want to add to the index in response to an input, like clicking a "save offline" button. Or you might add items automatically each time cached data is updated via a mechanism like [periodic background sync](/articles/periodic-background-sync).

```
await registration.index.add({
  // Required; set to something unique within your web app.
  id: 'article-123',

  // Required; url needs to be an offline-capable HTML page.
  url: '/articles/123',

  // Required; used in user-visible lists of content.
  title: 'Article title',

  // Required; used in user-visible lists of content.
  description: 'Amazing article about things!',

  // Required; used in user-visible lists of content.
  icons: [{
    src: '/img/article-123.png',
    sizes: '64x64',
    type: 'image/png',
  }],

  // Optional; valid categories are currently:
  // 'homepage', 'article', 'video', 'audio', or '' (default).
  category: 'article',
});
```

Adding an entry only affects the content index; it does not add anything to the [cache](https://web.dev/articles/cache-api-quick-guide).

#### Edge case: Call `add()` from `window` context if your icons rely on a `fetch` handler

When you call `add()`, Chrome will make a request for each icon's URL to ensure that it has a copy of the icon to use when displaying a list of indexed content.

- 

If you call `add()` from the `window` context (in other words, from your web page), this request will trigger a `fetch` event on your service worker.

- 

If you call `add()` within your service worker (perhaps inside another event handler), the request will not trigger the service worker's `fetch` handler. The icons will be fetched directly, without any service worker involvement. Keep this in mind if your icons rely on your `fetch` handler, perhaps because they only exist in the local cache and not on the network. If they do, make sure that you only call `add()` from the `window` context.

### Listing the index's contents

The `getAll()` method returns a promise for an iterable list of indexed entries and their metadata. Returned entries will contain all of the data saved with `add()`.

```
const entries = await registration.index.getAll();
for (const entry of entries) {
  // entry.id, entry.launchUrl, etc. are all exposed.
}
```

### Removing items from the index

To remove an item from the index, call `delete()` with the `id` of the item to remove:

```
await registration.index.delete('article-123');
```

Calling `delete()` only affects the index. It does not delete anything from the [cache](https://web.dev/articles/cache-api-quick-guide).

Warning: Once indexed, entries do not automatically expire. It's up to you to either present an interface in your web app for clearing out entries, or periodically remove older entries that you know should no longer be available offline.

### Handling a user delete event

When the browser displays the indexed content, it may include its own user interface with a Delete menu item, giving people a chance to indicate that they're done viewing previously indexed content. This is how the deletion interface looks in Chrome 80:

When someone selects that menu item, your web app's service worker will receive a `contentdelete` event. While handling this event is optional, it provides a chance for your service worker to "clean up" content, like locally cached media files, that someone has indicated they are done with.

You do not need to call `registration.index.delete()` inside your `contentdelete` handler; if the event has been fired, the relevant index deletion has already been performed by the browser.

```
self.addEventListener('contentdelete', (event) => {
  // event.id will correspond to the id value used
  // when the indexed content was added.
  // Use that value to determine what content, if any,
  // to delete from wherever your app stores it—usually
  // the Cache Storage API or perhaps IndexedDB.
});
```

Note: The `contentdelete` event is only fired when the deletion happens due to interaction with the browser's built-in user interface. It is not fired when `registration.index.delete()` is called. If your web app triggers the index deletion using that API method, it should also [clean up cached
content](https://developer.mozilla.org/docs/Web/API/Cache/delete) at the same time.

### Feedback about the API design

Is there something about the API that's awkward or doesn't work as expected? Or are there missing pieces that you need to implement your idea?

File an issue on the [Content Indexing API explainer GitHub repo](https://github.com/WICG/content-index/issues), or add your thoughts to an existing issue.

### Problem with the implementation?

Did you find a bug with Chrome's implementation?

File a bug at [https://new.crbug.com](https://new.crbug.com). Include as much detail as you can, simple instructions for reproducing, and set Components to `Blink>ContentIndexing`.

### Planning to use the API?

Planning to use the Content Indexing API in your web app? Your public support helps Chrome prioritize features, and shows other browser vendors how critical it is to support them.

- Send a tweet to [@ChromiumDev](https://twitter.com/chromiumdev) using the hashtag [#ContentIndexingAPI](https://twitter.com/search?q=%23ContentIndexingAPI&src=typed_query&f=live) and details on where and how you're using it.

## What are some security and privacy implications of content indexing?

Check out [the answers](https://github.com/WICG/content-index/blob/main/SECURITY_AND_PRIVACY.md) provided in response to the W3C's [Security and Privacy questionnaire](https://www.w3.org/TR/security-privacy-questionnaire/). If you have further questions, please start a discussion via the project's [GitHub repo](https://github.com/WICG/content-index/issues).

Hero image by Maksym Kaharlytskyi on [Unsplash](https://unsplash.com/photos/Q9y3LRuuxmg).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2019-12-12 UTC.

 [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2019-12-12 UTC."],[],[]] 

- 

### Contribute

  - [File a bug](https://issuetracker.google.com/issues/new?component=1400036&template=1897236)
  - [See open issues](https://issuetracker.google.com/issues?q=status:open%20componentid:1400036&s=created_time:desc)

- 

### Related content

  - [Chromium updates](https://blog.chromium.org/)
  - [Case studies](/case-studies)
  - [Archive](/deprecated)
  - [Podcasts & shows](https://web.dev/shows)

- 

### Follow

  - [@ChromiumDev on X](https://twitter.com/ChromiumDev)
  - [YouTube](https://www.youtube.com/user/ChromeDevelopers)
  - [Chrome for Developers on LinkedIn](https://www.linkedin.com/showcase/chrome-for-developers)
  - [RSS](/static/blog/feed.xml)

- [Terms](//policies.google.com/terms)
- [Privacy](//policies.google.com/privacy)
- [Manage cookies](#)

- English
- Deutsch
- Español – América Latina
- Français
- Indonesia
- Italiano
- Nederlands
- Polski
- Português – Brasil
- Tiếng Việt
- Türkçe
- Русский
- עברית
- العربيّة
- فارسی
- हिंदी
- বাংলা
- ภาษาไทย
- 中文 – 简体
- 中文 – 繁體
- 日本語
- 한국어
