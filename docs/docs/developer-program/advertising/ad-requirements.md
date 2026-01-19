# Roku advertising requirements
This document lists the requirements for displaying video and interactive ads in a channel. These requirements are applicable for both client-side and server-side ad requests. Apps must adhere to these requirements to pass certification, including those related to the Roku Advertising Framework (RAF).
## Roku advertising framework (RAF) requirements
### RAF 1 Integration requirements
Apps must integrate the following RAF-related requirements to pass certification:
Requirement | Description | Documentation |
---|---|---|---
RAF 1.1 | RAF integration | Apps must integrate RAF for all ads without modifying, obstructing, or disabling RAF functionality in any way. Replays of live broadcast streams are exempt from this requirement, unless ad insertion is used to insert new ads. | [RAF integration guide](https://developer.roku.com/docs/developer-program/advertising/roku-advertising-framework.md)
RAF 1.2 | Measurement beacons | Apps must fire all measurement beacons client-side via RAF. This requirement is applicable for both client-side and server-side ad insertion. | [Roku Advertising Watermark integration guide](https://developer.roku.com/docs/developer-program/advertising/ad-watermark.md)
RAF 1.3 | Audience measurement | Apps in the U.S. Streaming Store only that are not child-directed must support Roku ad tracking by calling the [enableAdMeasurements()](https://developer.roku.com/docs/developer-program/advertising/raf-api.md#enableadmeasurementsenabled) method and passing the required content metadata within the following methods: [setContentGenre()](https://developer.roku.com/docs/developer-program/advertising/raf-api.md#setcontentgenregenres-as-string-kidscontent-as-boolean), [setContentId()](https://developer.roku.com/docs/developer-program/advertising/raf-api.md#setcontentgenregenres-as-string-kidscontent-as-boolean), and [setContentLength()](https://developer.roku.com/docs/developer-program/advertising/raf-api.md#setcontentlengthlength-as-integer). Optionally, apps may use the [setNielsenGenre API](https://developer.roku.com/docs/developer-program/advertising/raf-api.md#setnielsengenregenre-as-string) to pass specific Nielsen Genre granularity and the [setNielsenAppId API](https://developer.roku.com/docs/developer-program/advertising/raf-api.md#setnielsenappidid-as-string) for those who specify a custom Nielsen App ID. The [enableAdMeasurements](https://developer.roku.com/docs/developer-program/advertising/raf-api.md#enableadmeasurementsenabled) method deprecates the [enableNielsenDAR](https://developer.roku.com/docs/developer-program/advertising/raf-api.md#nielsen-dar) API; therefore, do not use the [enableNielsenDAR](https://developer.roku.com/docs/developer-program/advertising/raf-api.md#nielsen-dar) API. | [General Audience Measurement](https://developer.roku.com/docs/developer-program/advertising/raf-api.md#general-audience-measurement)
RAF 1.4 | Ad break - numbering | For ads inserted client-side, apps must display the number of ads during ad breaks using the standard Roku-branded label applied by RAF. | [RAF integration guide](https://developer.roku.com/docs/developer-program/advertising/integrating-roku-advertising-framework.md)
## General advertising requirements
### ADS 1 General integration requirements
Requirement | Name | Description | Documentation
---|---|---|---
ADS 1.1 | SDKs and libraries | Partners must disclose integration/use of all non-Roku SDKs, libraries, or other software systems and external advertising partners (for example, DSPs) that enable video, audio, or banner ad insertion, and Roku has the right to approve or deny such non-Roku SDKs, libraries, or other software systems. | [Roku Advertising Framework overview](https://developer.roku.com/docs/developer-program/advertising/roku-advertising-framework.md)
ADS 1.2 | Ad terms | Apps that have an inventory relationship with Roku must meet the advertising terms specified in all applicable agreements. | [Video Advertising](https://developer.roku.com/docs/features/monetization/video-advertisements.md)
ADS 1.3 | Ad experience | Apps selling ads exclusively and/or with Roku must comply with ad load, ad frequency, and acceptable ad requirements. | [Roku Advertising Guidelines](http://www.roku.com/adguidelines)
ADS 1.4 | Demand API | Apps in the U.S. Streaming Store that have both streamed more than an average of 100,000 hours per month and averaged more than 10,000 new installs per month over the last three months may be required to implement the Demand API as part of their integration (this requirement may also be applicable to new apps projected to reach the specified thresholds shortly after launch).

Apps outside the U.S. Streaming Store that have streamed more than an average of 200,000 hours per month over the last three months, and new apps outside the U.S. Streaming Store that are projected to reach this threshold, may also be required to implement the Demand API. | [Implementing the Demand API](https://developer.roku.com/docs/developer-program/advertising/demand-api.md)
ADS 1.5 | RFI screen for authenticated ad-monetized apps | Authenticated ad-monetized apps must use the [getUserData](https://developer.roku.com/docs/references/scenegraph/control-nodes/channelstore.md#getuserdata) command to display a Request For Information (RFI) screen during the sign-up and sign-in workflows to enable customers to share their Roku account information with the channel. Only if the user declines the request may apps require the customer to manually enter their information. |  [Signup requirements and best practices](https://developer.roku.com/docs/developer-program/roku-pay/signup-best-practices.md)

[Sign-in requirements and best practices](https://developer.roku.com/docs/developer-program/roku-pay/signin-best-practices.md)
### ADS 2 Privacy requirements
Requirement | Name | Description | Documentation
---|---|---|---
ADS 2.1 | Roku ID for Advertisers (RIDA) identifier Limit Ad Tracking (LAT) flag | Apps must pass Roku's ID for Advertisers (RIDA) and "limit ad tracking" (LAT) value on ad server requests. If the user has opted out, apps must still pass the temporary ID returned by the [rodeviceInfo.GetRida()](https://developer.roku.com/docs/references/brightscript/interfaces/ifdeviceinfo.md#getrida-as-string) function to support frequency capping (this temporary ID is different than the UUID returned if the user has not opted out; it expires after 30 days). |  [GetRida()](https://developer.roku.com/docs/references/brightscript/interfaces/ifdeviceinfo.md#getrida-as-string)

[IsRIDADisabled()asBoolean](https://developer.roku.com/docs/references/brightscript/interfaces/ifdeviceinfo.md#isridadisabled-as-boolean)

[URL parameter macros](https://developer.roku.com/docs/developer-program/advertising/integrating-roku-advertising-framework.md#url-parameter-macros)
ADS 2.2 | Child-directed content | Apps with child-directed content must make ad requests that indicate that content is child-directed when serving ads during child-directed content. |  [kidsContent parameter in the setContentGenre() method](https://developer.roku.com/docs/developer-program/advertising/raf-api.md#setcontentgenregenres-as-string-kidscontent-as-boolean)

[ROKU_ADS_KIDS_CONTENT URL parameter macro](https://developer.roku.com/docs/developer-program/advertising/integrating-roku-advertising-framework.md#url-parameter-macros)
### ADS 3 Ad request requirements
Requirement | Name | Description | Documentation
---|---|---|---
ADS 3.1 | Channel ID | Apps must pass their Roku channel ID in ad server requests to Roku. |  [roChannelInfo.getId() function](https://developer.roku.com/docs/references/brightscript/interfaces/ifappinfo.md#getid-as-string)

[ROKU_ADS_APP_ID URL parameter macro populated by RAF](https://developer.roku.com/docs/developer-program/advertising/integrating-roku-advertising-framework.md#url-parameter-macros)
ADS 3.2 | User agent | Apps must use the Roku-generated device user agent in all server-side ad requests. | [RAF integration guide](https://developer.roku.com/docs/developer-program/advertising/integrating-roku-advertising-framework.md#3-user-agent-requirements)
### ADS 4 Ad break playback requirements
Requirement | Name | Description | Documentation
---|---|---|---
ADS 4.1 | Ad break - back button behavior | All apps must return to the previous screen when the back button is pressed during an ad break (if the app can't return to the previous screen, the app must display an exit confirmation dialog).

All apps must attempt to initiate an ad break to preserve the previously exited ad experience when playback resumes. Exemptions from this requirement include (1) live streams and (2) replays of broadcast streams, unless ad insertion is used to insert new ads in the replay. | [RAF integration guide](https://developer.roku.com/docs/developer-program/advertising/integrating-roku-advertising-framework.md)
ADS 4.2 | Ad break - FF/REW commands | All apps must ignore FF/REW commands received during an ad break (via either key presses or voice commands). Exemptions from this requirement include (1) live streams and (2) replays of broadcast streams, unless ad insertion is used to insert new ads in the replay. | [RAF integration guide](https://developer.roku.com/docs/developer-program/advertising/integrating-roku-advertising-framework.md)