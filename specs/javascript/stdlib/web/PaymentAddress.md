# PaymentAddress

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

Non-standard: This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The `PaymentAddress` interface of the [Payment Request API](/en-US/docs/Web/API/Payment_Request_API) is used to store shipping or payment address information.

It may be useful to refer to the Universal Postal Union website's [Addressing S42 standard](https://www.upu.int/en/Postal-Solutions/Programmes-Services/Addressing-Solutions#addressing-s42-standard) materials, which provide information about international standards for postal addresses.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[PaymentAddress.addressLine](/en-US/docs/Web/API/PaymentAddress/addressLine)Read onlyDeprecatedNon-standard

An array of strings providing each line of the address not included among the other properties. The exact size and content varies by country or location and can include, for example, a street name, house number, apartment number, rural delivery route, descriptive instructions, or post office box number.

[PaymentAddress.country](/en-US/docs/Web/API/PaymentAddress/country)Read onlyDeprecatedNon-standard

A string specifying the country in which the address is located, using the [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) standard. The string is always given in its canonical upper-case form. Some examples of valid `country` values: `"US"`, `"GB"`, `"CN"`, or `"JP"`.

[PaymentAddress.city](/en-US/docs/Web/API/PaymentAddress/city)Read onlyDeprecatedNon-standard

A string which contains the city or town portion of the address.

[PaymentAddress.dependentLocality](/en-US/docs/Web/API/PaymentAddress/dependentLocality)Read onlyDeprecatedNon-standard

A string giving the dependent locality or sublocality within a city, for example, a neighborhood, borough, district, or UK dependent locality.

[PaymentAddress.organization](/en-US/docs/Web/API/PaymentAddress/organization)Read onlyDeprecatedNon-standard

A string specifying the name of the organization, firm, company, or institution at the payment address.

[PaymentAddress.phone](/en-US/docs/Web/API/PaymentAddress/phone)Read onlyDeprecatedNon-standard

A string specifying the telephone number of the recipient or contact person.

[PaymentAddress.postalCode](/en-US/docs/Web/API/PaymentAddress/postalCode)Read onlyDeprecatedNon-standard

A string specifying a code used by a jurisdiction for mail routing, for example, the ZIP code in the United States or the PIN code in India.

[PaymentAddress.recipient](/en-US/docs/Web/API/PaymentAddress/recipient)Read onlyDeprecatedNon-standard

A string giving the name of the recipient, purchaser, or contact person at the payment address.

[PaymentAddress.region](/en-US/docs/Web/API/PaymentAddress/region)Read onlyDeprecatedNon-standard

A string containing the top level administrative subdivision of the country, for example a state, province, oblast, or prefecture.

[PaymentAddress.sortingCode](/en-US/docs/Web/API/PaymentAddress/sortingCode)Read onlyDeprecatedNon-standard

A string providing a postal sorting code such as is used in France.

Note: Properties for which values were not specified contain empty strings.

## [Instance methods](#instance_methods)

[PaymentAddress.toJSON()](/en-US/docs/Web/API/PaymentAddress/toJSON)DeprecatedNon-standard

A standard serializer that returns a JSON representation of the `PaymentAddress` object's properties.

## [Examples](#examples)

In the following example, the [PaymentRequest()](/en-US/docs/Web/API/PaymentRequest/PaymentRequest) constructor is used to create a new payment request, which takes three objects as parameters — one containing details of the payment methods that can be used for the payment, one containing details of the actual order (such as items bought and shipping options), and an optional object containing further options.

The first of these three (`supportedInstruments` in the example below) contains a `data` property that has to conform to the structure defined by the payment method.

js

```
const supportedInstruments = [
  {
    supportedMethods: "https://example.com/pay",
  },
];

const details = {
  total: { label: "Donation", amount: { currency: "USD", value: "65.00" } },
  displayItems: [
    {
      label: "Original donation amount",
      amount: { currency: "USD", value: "65.00" },
    },
  ],
  shippingOptions: [
    {
      id: "standard",
      label: "Standard shipping",
      amount: { currency: "USD", value: "0.00" },
      selected: true,
    },
  ],
};

const options = { requestShipping: true };

async function doPaymentRequest() {
  const request = new PaymentRequest(supportedInstruments, details, options);
  // Add event listeners here.
  // Call show() to trigger the browser's payment flow.
  const response = await request.show();
  // Process payment.
  const json = response.toJSON();
  const httpResponse = await fetch("/pay/", { method: "POST", body: json });
  const result = httpResponse.ok ? "success" : "failure";

  await response.complete(result);
}
doPaymentRequest();
```

Once the payment flow has been triggered using [PaymentRequest.show()](/en-US/docs/Web/API/PaymentRequest/show) and the promise resolves successfully, the [PaymentResponse](/en-US/docs/Web/API/PaymentResponse) object available from the fulfilled promise (`instrumentResponse` above) will have a [PaymentResponse.details](/en-US/docs/Web/API/PaymentResponse/details) property containing response details. This has to conform to the structure defined by the payment method provider.

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/PaymentAddress/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/paymentaddress/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPaymentAddress&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpaymentaddress%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPaymentAddress%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpaymentaddress%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Faa8fa82a902746b0bd97839180fc2b5397088140%0A*+Document+last+modified%3A+2024-07-26T02%3A56%3A16.000Z%0A%0A%3C%2Fdetails%3E)
