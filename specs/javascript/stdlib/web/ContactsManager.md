# ContactsManager

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FContactsManager&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `ContactsManager` interface of the [Contact Picker API](/en-US/docs/Web/API/Contact_Picker_API) allows users to select entries from their contact list and share limited details of the selected entries with a website or application.

The `ContactsManager` is available through the global [navigator.contacts](/en-US/docs/Web/API/Navigator/contacts) property.

## In this article

- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

[select()](/en-US/docs/Web/API/ContactsManager/select)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which, when resolved, presents the user with a contact picker which allows them to select contact(s) they wish to share.

[getProperties()](/en-US/docs/Web/API/ContactsManager/getProperties)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which resolves with an [Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) of [strings](/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) indicating which contact properties are available.

## [Examples](#examples)

### [Feature Detection](#feature_detection)

The following code checks whether the Contact Picker API is supported.

js

```
const supported = "contacts" in navigator && "ContactsManager" in window;
```

### [Checking for Supported Properties](#checking_for_supported_properties)

The following asynchronous function uses the `getProperties` method to check for supported properties.

js

```
async function checkProperties() {
  const supportedProperties = await navigator.contacts.getProperties();
  if (supportedProperties.includes("name")) {
    // run code for name support
  }
  if (supportedProperties.includes("email")) {
    // run code for email support
  }
  if (supportedProperties.includes("tel")) {
    // run code for telephone number support
  }
  if (supportedProperties.includes("address")) {
    // run code for address support
  }
  if (supportedProperties.includes("icon")) {
    // run code for avatar support
  }
}
```

### [Selecting Contacts](#selecting_contacts)

The following example sets an array of properties to be retrieved for each contact, as well as setting an options object to allow for multiple contacts to be selected.

An asynchronous function is then defined which uses the `select()` method to present the user with a contact picker interface and handle the chosen results.

js

```
const props = ["name", "email", "tel", "address", "icon"];
const opts = { multiple: true };

async function getContacts() {
  try {
    const contacts = await navigator.contacts.select(props, opts);
    handleResults(contacts);
  } catch (ex) {
    // Handle any errors here.
  }
}
```

`handleResults()` is a developer defined function.

## [Specifications](#specifications)

Specification
[Contact Picker API# contacts-manager](https://w3c.github.io/contact-picker/#contacts-manager)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [A Contact Picker for the Web](https://developer.chrome.com/docs/capabilities/web-apis/contact-picker)
- [Contact Picker API live demo](https://mdn.github.io/dom-examples/contact-picker/)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 4, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ContactsManager/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/contactsmanager/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FContactsManager&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcontactsmanager%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FContactsManager%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcontactsmanager%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff84cdbda4f9c642f57083e013341f170774f0973%0A*+Document+last+modified%3A+2025-07-04T14%3A20%3A20.000Z%0A%0A%3C%2Fdetails%3E)
