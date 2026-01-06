# CookieStore

 Baseline  2025  * Newly available

 Since ⁨June 2025⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCookieStore&level=low)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

The `CookieStore` interface of the [Cookie Store API](/en-US/docs/Web/API/Cookie_Store_API) provides methods for getting and setting cookies asynchronously from either a page or a service worker.

The `CookieStore` is accessed via attributes in the global scope in a [Window](/en-US/docs/Web/API/Window) or [ServiceWorkerGlobalScope](/en-US/docs/Web/API/ServiceWorkerGlobalScope) context. Therefore there is no constructor.

## In this article

- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance methods](#instance_methods)

[CookieStore.delete()](/en-US/docs/Web/API/CookieStore/delete)

The `delete()` method deletes a cookie with the given `name` or `options` object. It returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when the deletion completes or if no cookies are matched.

[CookieStore.get()](/en-US/docs/Web/API/CookieStore/get)

The `get()` method gets a single cookie with the given `name` or `options` object. It returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with details of a single cookie.

[CookieStore.getAll()](/en-US/docs/Web/API/CookieStore/getAll)

The `getAll()` method gets all matching cookies. It returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with a list of cookies.

[CookieStore.set()](/en-US/docs/Web/API/CookieStore/set)

The `set()` method sets a cookie with the given `name` and `value` or `options` object. It returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when the cookie is set.

## [Events](#events)

[change](/en-US/docs/Web/API/CookieStore/change_event)

The `change` event fires when a change is made to any cookie.

## [Examples](#examples)

The examples below can be tested by copying the code into a test harness and running it with a [local server](/en-US/docs/Learn_web_development/Howto/Tools_and_setup/set_up_a_local_testing_server), or deploying it to a website site such as GitHub pages.

### [Setting cookies](#setting_cookies)

This example shows how to set cookies by passing a `name` and `value`, and by setting an `options` value.

The `cookieTest()` method sets one cookie with `name` and `value` properties and another with `name`, `value`, and `expires` properties. We then use the [CookieStore.get()](/en-US/docs/Web/API/CookieStore/get) method to get each of the cookies, which are then logged.

js

```
async function cookieTest() {
  // Set cookie: passing name and value
  try {
    await cookieStore.set("cookie1", "cookie1-value");
  } catch (error) {
    console.log(`Error setting cookie1: ${error}`);
  }

  // Set cookie: passing options
  const day = 24 * 60 * 60 * 1000;

  try {
    await cookieStore.set({
      name: "cookie2",
      value: "cookie2-value",
      expires: Date.now() + day,
      partitioned: true,
    });
  } catch (error) {
    log(`Error setting cookie2: ${error}`);
  }

  // Get named cookies and log their properties
  const cookie1 = await cookieStore.get("cookie1");
  console.log(cookie1);

  const cookie2 = await cookieStore.get("cookie2");
  console.log(cookie2);
}

cookieTest();
```

### [Getting cookies](#getting_cookies)

This example shows how you can get a particular cookie using [CookieStore.get()](/en-US/docs/Web/API/CookieStore/get) or all cookies using [CookieStore.getAll()](/en-US/docs/Web/API/CookieStore/getAll).

The example code first sets three cookies that we'll use for demonstrating the get methods. First it creates `cookie1` and `cookie2` using the [CookieStore.set()](/en-US/docs/Web/API/CookieStore/set) method. Then it creates a third cookie using the older synchronous [Document.cookie](/en-US/docs/Web/API/Document/cookie) property (just so we can show that these are also fetched using the `get()` and `getAll()` methods).

The code then uses [CookieStore.get()](/en-US/docs/Web/API/CookieStore/get) to fetch "cookie1" and log its properties, and [CookieStore.getAll()](/en-US/docs/Web/API/CookieStore/getAll) (without arguments) to fetch all cookies in the current context.

js

```
async function cookieTest() {
  // Set a cookie passing name and value
  try {
    await cookieStore.set("cookie1", "cookie1-value");
  } catch (error) {
    console.log(`Error setting cookie1: ${error}`);
  }

  // Set a cookie passing an options object
  const day = 24 * 60 * 60 * 1000;
  try {
    await cookieStore.set({
      name: "cookie2",
      value: `cookie2-value`,
      expires: Date.now() + day,
      partitioned: true,
    });
  } catch (error) {
    console.log(`Error setting cookie2: ${error}`);
  }

  // Set cookie using document.cookie
  // (to demonstrate these are are fetched too)
  document.cookie = "favorite_food=tripe; SameSite=None; Secure";

  // Get named cookie and log properties
  const cookie1 = await cookieStore.get("cookie1");
  console.log(cookie1);

  // Get all cookies and log each
  const cookies = await cookieStore.getAll();
  if (cookies.length > 0) {
    console.log(`getAll(): ${cookies.length}:`);
    cookies.forEach((cookie) => console.log(cookie));
  } else {
    console.log("Cookies not found");
  }
}

cookieTest();
```

The example should log "cookie1" and all three cookies separately. One thing to note is that the cookie created using [Document.cookie](/en-US/docs/Web/API/Document/cookie) may have a different path than those created using [set()](/en-US/docs/Web/API/CookieStore/set) (which defaults to `/`).

### [Delete a named cookie](#delete_a_named_cookie)

This example shows how to delete a named cookie using the [delete()](/en-US/docs/Web/API/CookieStore/delete) method.

The code first sets two cookies and logs them to the console. We then delete one of the cookies, and then list all cookies again. The deleted cookie ("cookie1") is present in the first log array, and not in the second.

js

```
async function cookieTest() {
  // Set two cookies
  try {
    await cookieStore.set("cookie1", "cookie1-value");
  } catch (error) {
    console.log(`Error setting cookie1: ${error}`);
  }

  try {
    await cookieStore.set("cookie2", "cookie2-value");
  } catch (error) {
    console.log(`Error setting cookie2: ${error}`);
  }

  // Log cookie names
  let cookieNames = (await cookieStore.getAll())
    .map((cookie) => cookie.name)
    .join(" ");
  console.log(`Initial cookies: ${cookieNames}`);

  // Delete cookie1
  await cookieStore.delete("cookie1");

  // Log cookies again (to show cookie1 deleted)
  cookieNames = (await cookieStore.getAll())
    .map((cookie) => cookie.name)
    .join(" ");
  console.log(
    `Cookies remaining after attempted deletions (cookie1 should be deleted): ${cookieNames}`,
  );
}

cookieTest();
```

## [Specifications](#specifications)

Specification
[Cookie Store API# CookieStore](https://cookiestore.spec.whatwg.org/#CookieStore)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 14, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CookieStore/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cookiestore/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCookieStore&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcookiestore%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCookieStore%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcookiestore%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F372d2f15b56a753235002946c7775d0b38f6f3eb%0A*+Document+last+modified%3A+2025-03-14T05%3A43%3A57.000Z%0A%0A%3C%2Fdetails%3E)
