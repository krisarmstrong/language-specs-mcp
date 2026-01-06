# ContactAddress

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FContactAddress&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `ContactAddress` interface of the [Contact Picker API](/en-US/docs/Web/API/Contact_Picker_API) represents a physical address. Instances of this interface are retrieved from the `address` property of the objects returned by [ContactsManager.getProperties()](/en-US/docs/Web/API/ContactsManager/getProperties).

It may be useful to refer to the Universal Postal Union website's [Addressing S42 standard](https://www.upu.int/en/Postal-Solutions/Programmes-Services/Addressing-Solutions#addressing-s42-standard) materials, which provide information about international standards for postal addresses.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[ContactAddress.addressLine](/en-US/docs/Web/API/ContactAddress/addressLine)Read onlyExperimental

An array of strings providing each line of the address not included among the other properties. The exact size and content varies by country or location and can include, for example, a street name, house number, apartment number, rural delivery route, descriptive instructions, or post office box number.

[ContactAddress.country](/en-US/docs/Web/API/ContactAddress/country)Read onlyExperimental

A string specifying the country in which the address is located, using the [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) standard. The string is always given in its canonical upper-case form. Some examples of valid `country` values: `"US"`, `"GB"`, `"CN"`, or `"JP"`.

[ContactAddress.city](/en-US/docs/Web/API/ContactAddress/city)Read onlyExperimental

A string which contains the city or town portion of the address.

[ContactAddress.dependentLocality](/en-US/docs/Web/API/ContactAddress/dependentLocality)Read onlyExperimental

A string giving the dependent locality or sublocality within a city, for example, a neighborhood, borough, district, or UK dependent locality.

[ContactAddress.organization](/en-US/docs/Web/API/ContactAddress/organization)Read onlyExperimental

A string specifying the name of the organization, firm, company, or institution at the address.

[ContactAddress.phone](/en-US/docs/Web/API/ContactAddress/phone)Read onlyExperimental

A string specifying the telephone number of the recipient or contact person.

[ContactAddress.postalCode](/en-US/docs/Web/API/ContactAddress/postalCode)Read onlyExperimental

A string specifying a code used by a jurisdiction for mail routing, for example, the ZIP code in the United States or the PIN code in India.

[ContactAddress.recipient](/en-US/docs/Web/API/ContactAddress/recipient)Read onlyExperimental

A string giving the name of the recipient, purchaser, or contact person at the address.

[ContactAddress.region](/en-US/docs/Web/API/ContactAddress/region)Read onlyExperimental

A string containing the top level administrative subdivision of the country, for example a state, province, oblast, or prefecture.

[ContactAddress.sortingCode](/en-US/docs/Web/API/ContactAddress/sortingCode)Read onlyExperimental

A string providing a postal sorting code such as is used in France.

## [Instance methods](#instance_methods)

[ContactAddress.toJSON()](/en-US/docs/Web/API/ContactAddress/toJSON)Experimental

A standard serializer that returns a JSON representation of the `ContactAddress` object's properties.

## [Examples](#examples)

The following example prompts the user to select contacts, then prints the first returned address to the console.

js

```
const props = ["address"];
const opts = { multiple: true };

async function getContacts() {
  try {
    const contacts = await navigator.contacts.select(props, opts);
    const contactAddress = contacts[0].address[0];
    console.log(contactAddress);
  } catch (ex) {
    // Handle any errors here.
  }
}
```

## [Specifications](#specifications)

Specification
[Contact Picker API# contactaddress](https://w3c.github.io/contact-picker/#contactaddress)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 27, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/ContactAddress/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/contactaddress/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FContactAddress&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcontactaddress%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FContactAddress%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcontactaddress%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd03a8d7efa6f5476886c915e2261c85b951e4b16%0A*+Document+last+modified%3A+2024-02-27T17%3A12%3A56.000Z%0A%0A%3C%2Fdetails%3E)
