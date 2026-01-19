# Roku Pay integration requirements
All apps with transactional content or in-app purchases (SVOD, TVOD, and other subscription services) must integrate and enable Roku Pay services. This document lists the requirements for integrating Roku Pay services in an app. Apps must adhere to all of these requirements to pass certification.
## RP 1 Channel setup requirements
Requirement | Name | Description | Documentation
---|---|---|---
RP 1.1 | Channel name | Apps must provide a name, description, and poster (a 540x405 JPEG or PNG image) in each language supported by the channel.

The app name must clearly identify the company associated with the service, and the publisher must have full legal rights or consent for their app names and the rights to all trademarks and copyright expressions associated with the name.

The app name may not include the name "Roku", and it may not contain any profanity, or derogatory or misleading language. | [App publishing](https://developer.roku.com/docs/developer-program/publishing/channel-publishing-guide.md#create-a-channel)
## RP 2 Sign-up and sign-in requirements
Requirement | Name | Description | Documentation
---|---|---|---
RP 2.1 | RFI screen | All authenticated transactional apps (SVOD, TVOD, and other subscription services) must use the [getUserData](https://developer.roku.com/docs/references/scenegraph/control-nodes/channelstore.md#getuserdata) command to display a Request For Information (RFI) screen during the sign-up and sign-in workflows to enable customers to share their Roku account information with the app.

Only if the user declines the request, may apps require the customer to manually enter information other than a password. |
  * [Signup requirements and best practices](https://developer.roku.com/docs/developer-program/roku-pay/signup-best-practices.md)
  * [Sign-in requirements and best practices](https://developer.roku.com/docs/developer-program/roku-pay/signin-best-practices.md)

## RP 3 Payment requirements
Requirement | Name | Description | Documentation
---|---|---|---
RP 3.1 | Product groups | Subscription services must create product groups in the [Developer Dashboard](https://developer.roku.com/developer) for any set of subscription products that the consumer should not be able to be subscribed to simultaneously.

For example, if an app has two in-channel products for the same monthly subscription but with different free trial durations, these two products must be added to the same product group to prevent the customer from paying for two separate monthly subscriptions | [In-app purchases - Product groups](https://developer.roku.com/docs/developer-program/roku-pay/quickstart/in-channel-products.md#adding-product-groups)
RP 3.2 | Multiple purchase protection | Apps must protect against multiple purchases of content or subscriptions through Roku Pay before passing new orders to the Streaming Store service.

The Streaming Store service inherently protects against purchasing the same subscription code multiple times, but preventing, for example, the purchase of a free trial subscription and a non-free trial subscription must be done in the channel. | [In-app purchases -Product Groups](https://developer.roku.com/docs/developer-program/roku-pay/quickstart/in-channel-products.md#adding-product-groups)
RP 3.3 | Price changes | SVOD apps must provide notice and otherwise comply with all applicable laws before changing the price of their service.

In all cases, Roku requires that SVOD apps provide at least 15 days notice to all existing customers before a price increase. | [In-app purchases - Product pricing](https://developer.roku.com/docs/developer-program/roku-pay/quickstart/in-channel-products.md#product-pricing)
RP 3.4 | In-channel product naming | Apps must name in-app products so that the service being offered is clearly identifiable. The publisher must have full legal rights or consent for their in-app product names and the rights to all trademarks and copyright expressions associated with the names. The in-app product names may not include the name "Roku", text related to a trial or discount offer**,** or any profane, derogatory, or misleading language. | [In-app purchases - Product basics](https://developer.roku.com/docs/developer-program/roku-pay/quickstart/in-channel-products.md#product-basics)
## RP 4 Authentication and entitlement requirements
Requirement | Name | Description | Documentation
---|---|---|---
RP 4.1 | On-device authentication | Apps that include authentication must complete account sign-ups and sign-ins on the device using [On-device authentication](https://developer.roku.com/docs/developer-program/authentication/on-device-authentication.md).

Sign-up and sign-in workflows are prohibited from including external webpages, links to off-device promotional or marketing materials, or utilizing off-device sign-up or sign-in mechanisms such as rendezvous linking. | [On-device authentication](https://developer.roku.com/docs/developer-program/authentication/on-device-authentication.md)
RP 4.2 | On-device upgrades and downgrades | Apps must complete upgrades and downgrades on the device using [On-device upgrade and downgrade](https://developer.roku.com/docs/developer-program/roku-pay/implementation/on-device-upgrade-downgrade.md). The upgrade/downgrade workflows are prohibited from including external webpages. | [On-device upgrade and downgrade](https://developer.roku.com/docs/developer-program/roku-pay/implementation/on-device-upgrade-downgrade.md)
RP 4.3 | Account-based entitlements | Apps must automatically entitle content or subscriptions purchased through Roku Pay across all devices tied to the purchasing Roku account.

Apps can use the [getAllPurchases](https://developer.roku.com/docs/references/scenegraph/control-nodes/channelstore.md#getallpurchases) API can upon launch to return the transactionID for an active subscription, and they can use an entitlement server to look up an account via a call to the [validate-transaction API](https://developer.roku.com/docs/developer-program/roku-pay/implementation/roku-web-service.md#validate-transaction). |
  * [getPurchases ChannelStore API](https://developer.roku.com/docs/references/scenegraph/control-nodes/channelstore.md#getuserdata)
  * [validate-transaction Roku Pay Web service API](https://developer.roku.com/docs/developer-program/roku-pay/implementation/roku-web-service.md#validate-transaction)

RP 4.4 | Abandonment tracking | All subscription services that have streamed more than an average of 5 million hours per month over the last three months (and new subscription services projected to reach the specified streaming hour threshold shortly after launch) must implement Roku Event Dispatcher (RED) in the signup workflow.

Apps must fire a RED event upon loading each page within the signup flow and submission of the final page to help track where users are abandoning the process. This includes, but is not limited to, the following pages: landing, sign up, registration, device activation, subscription selection, payment, purchase confirmation, and cancellation.

If the app's sign-up flow is contained within a form that covers one or more pages, channels must fire a RED event when each element in the form is completed. Streaming hours per month information is available in the Developer Dashboard. |  [Tracking signup abandonment](https://developer.roku.com/docs/developer-program/roku-pay/implementation/tracking-signup-abandonment.md).
RP 4.5 | Enhanced Subscription Recovery (churn mitigation) | All apps offering subscriptions must implement Enhanced Subscription Recovery to pass [certification](https://developer.roku.com/docs/developer-program/roku-pay/roku-pay-requirements.md#rp-4-authentication-and-entitlement-requirements) | [Enhanced Subscription Recovery](https://developer.roku.com/docs/developer-program/roku-pay/subscription-recovery/subscription-on-hold.md)