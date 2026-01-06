# Contact Picker API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FContact_Picker_API&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The Contact Picker API allows users to select entries from their contact list and share limited details of the selected entries with a website or application.

Note: This API is not available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API) (not exposed via [WorkerNavigator](/en-US/docs/Web/API/WorkerNavigator)).

## In this article

- [Contact Picker API Concepts and Usage](#contact_picker_api_concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Contact Picker API Concepts and Usage](#contact_picker_api_concepts_and_usage)

Access to contacts has long been a feature available within native applications. The Contacts Picker API brings that functionality to web applications.

Use cases include selecting contacts to message via an email or chat application, selecting a contacts phone number for use with voice over IP (VOIP), or for discovering contacts who have already joined a social platform. User agents can also offer a consistent experience with other applications on a users device.

When calling the [select](/en-US/docs/Web/API/ContactsManager/select) method of the [ContactsManager](/en-US/docs/Web/API/ContactsManager) interface, the user is presented with a contact picker, whereby they can then select contact information to share with the web application. User interaction is required before permission to display the contact picker is granted and access to contacts is not persistent; the user must grant access every time a request is made by the application.

This API is only available from a secure top-level browsing context and very carefully considers the sensitivity and privacy of contact data. The onus is on the user for choosing data to share and only allows specific data for selected contacts, with no access to any data for other contacts.

## [Interfaces](#interfaces)

[ContactAddress](/en-US/docs/Web/API/ContactAddress)

Represents a physical address.

[ContactsManager](/en-US/docs/Web/API/ContactsManager)

Provides a way for users to select and share limited details of contacts with a web application.

[Navigator.contacts](/en-US/docs/Web/API/Navigator/contacts)

Returns a [ContactsManager](/en-US/docs/Web/API/ContactsManager) object instance, from which all other functionality can be accessed.

## [Examples](#examples)

### [Feature Detection](#feature_detection)

The following code checks whether the Contact Picker API is supported.

js

```
const supported = "contacts" in navigator;
```

### [Checking for Supported Properties](#checking_for_supported_properties)

The following asynchronous function uses the `getProperties()` method to check for supported properties.

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

 This page was last modified on ⁨Jul 4, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Contact_Picker_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/contact_picker_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FContact_Picker_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcontact_picker_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FContact_Picker_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcontact_picker_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff84cdbda4f9c642f57083e013341f170774f0973%0A*+Document+last+modified%3A+2025-07-04T14%3A20%3A20.000Z%0A%0A%3C%2Fdetails%3E)
