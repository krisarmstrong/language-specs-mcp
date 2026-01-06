# PasswordCredentialInit

The `PasswordCredentialInit` dictionary represents the object passed to [CredentialsContainer.create()](/en-US/docs/Web/API/CredentialsContainer/create) as the value of the `password` option, when creating a password credential.

## In this article

- [Initialization from a form](#initialization_from_a_form)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)

## [Initialization from a form](#initialization_from_a_form)

Instead of passing this dictionary directly, a website can pass an [HTMLFormElement](/en-US/docs/Web/API/HTMLFormElement), and the implementation of `create()` will populate the credential's data from the values of the form's submittable elements, based on the value of the element's [autocomplete](/en-US/docs/Web/HTML/Reference/Attributes/autocomplete) attribute.

`autocomplete` valueCredential property targeted`"username"``id``"name"` or `"nickname"``name``"new-password"` or `"current-password"``password``"photo"``iconURL`

If the form contains both `"new-password"` and `"current-password"` elements, the value for `"new-password"` will be used.

The `origin` property is set to the origin of the document the [HTMLFormElement](/en-US/docs/Web/API/HTMLFormElement) is contained within.

## [Instance properties](#instance_properties)

[iconURL Optional](#iconurl)

A string representing the URL of an icon or avatar to be associated with the credential.

[id](#id)

A string representing the username portion of the username/password combination.

[name Optional](#name)

A string representing a human-understandable name associated with the credential, intended to help the user select this credential in a user interface.

[origin](#origin)

A string representing the credential's origin. [PasswordCredential](/en-US/docs/Web/API/PasswordCredential) objects are origin-bound, which means that they will only be usable on the specified origin they were intended to be used on.

[password](#password)

A string representing the credential password.

## [Examples](#examples)

### [Creating a password credential from an object literal](#creating_a_password_credential_from_an_object_literal)

This example constructs an object literal to initialize a password credential.

js

```
const credInit = {
  id: "serpent1234", // "username" in a typical username/password pair
  name: "Serpentina", // display name for credential
  origin: "https://example.org",
  password: "the last visible dog",
};

const makeCredential = document.querySelector("#make-credential");

makeCredential.addEventListener("click", async () => {
  const cred = await navigator.credentials.create({
    password: credInit,
  });
  console.log(cred.name);
  // Serpentina
  console.log(cred.id);
  // serpent1234
  console.log(cred.password);
  // the last visible dog
});
```

### [Creating a password credential from a form](#creating_a_password_credential_from_a_form)

This example uses a form to initialize a password credential.

#### HTML

The HTML declares a [<form>](/en-US/docs/Web/HTML/Reference/Elements/form) containing three submittable elements, representing the user ID, user's display name, and password.

html

```
<form>
  <div>
    <label for="displayname">Enter your display name: </label>
    <input
      type="text"
      name="displayname"
      id="displayname"
      autocomplete="name" />
  </div>
  <div>
    <label for="username">Enter your username: </label>
    <input type="text" name="username" id="username" autocomplete="username" />
  </div>
  <div>
    <label for="password">Enter your password: </label>
    <input
      type="password"
      name="password"
      id="password"
      autocomplete="new-password" />
  </div>
</form>

<button id="make-credential">Make credential</button>

<pre id="log"></pre>
```

```
form {
  display: table;
}

div {
  display: table-row;
}

label,
input {
  display: table-cell;
  margin-bottom: 10px;
}

label {
  padding-right: 10px;
}

#log {
  height: 60px;
  padding: 0.5rem;
  border: 1px solid black;
}
```

#### JavaScript

The JavaScript passes the form into `create()`, and logs some of the values of the resulting credential.

The promise returned by `create()` will reject if the form does not contain values for the mandatory credential properties.

js

```
const makeCredential = document.querySelector("#make-credential");
const formCreds = document.querySelector("form");

makeCredential.addEventListener("click", async () => {
  try {
    const credential = await navigator.credentials.create({
      password: formCreds,
    });
    log(
      `New credential:\ndisplay name: ${credential.name}, username: ${credential.id}, password: ${credential.password}`,
    );
  } catch (e) {
    if (e.name === "TypeError") {
      log("Error creating credential\nMake sure you filled in all the fields");
    }
  }
});

const logElement = document.querySelector("#log");
function log(text) {
  logElement.innerText = text;
}
```

#### Result

## [Specifications](#specifications)

Specification
[Credential Management Level 1# typedefdef-passwordcredentialinit](https://w3c.github.io/webappsec-credential-management/#typedefdef-passwordcredentialinit)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 26, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/PasswordCredentialInit/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/passwordcredentialinit/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPasswordCredentialInit&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpasswordcredentialinit%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPasswordCredentialInit%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpasswordcredentialinit%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0fe625f488d9b548f57bb7f4c714287ba093d96b%0A*+Document+last+modified%3A+2025-11-26T23%3A20%3A55.000Z%0A%0A%3C%2Fdetails%3E)
