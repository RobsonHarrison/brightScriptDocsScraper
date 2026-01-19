# Roku JavaScript Library
Roku's JavaScript Library enables keyword-driven testing of apps. The library resides in a JavaScript class that has methods that map directly to keyword names. The keywords take the same arguments as the methods implementing them. The keywords report failures with exceptions, create logs by writing to standard output, and return values using the `return` statement.
## Instantiating the library
To create an instance of the Roku JavaScript Library, provide the following three arguments:
Argument | Description
---|---
ip | The IP address of the device to be used for testing.
timeout | The amount of time (in milliseconds) that commands are allowed to run.
pressDelay | The amount of time (in milliseconds) between keypress commands. This argument works with the **sendKeys** command.
The following example demonstrates how to instantiate the Roku JavaScript Library:
```
library = new rokuLibrary.Library("192.168.2.121", 20000, 2000);

```

The following example demonstrates how to instantiate the Roku JavaScript Library and runs test case with Mocha and Chai:
```
//import library
const rokuLibrary = require("../library/rokuLibrary");
const expect = require("chai").expect;
const {
    spawn
} = require('child_process');

//start instance of webDriver
const childProcess = spawn('D:/projects/go/webDriver/src/main.exe');
let library;

//test suite
describe('test_3-Grid', () => {
    //this method is executed before all test cases
    before(() => {
        //create instance of jsLibrary
        library = new rokuLibrary.Library("192.168.2.121", 20000, 2000);
    });

    //test case
    it('should launch the app', async function() {
        this.timeout(25000);
        await library.sideLoad("../channels/3_Grid.zip", "rokudev", "your_channel_password");
        await library.verifyIsChannelLoaded('dev');
    });

    //this method executed after all tests
    after(async () => {
        //close session
        await library.close();
        //exit webDriver
        childProcess.kill();
    });
});

```

## Keywords
The Roku's JavaScript Library includes the following keywords:
  * Sideload (_available since release 2.0_)
  * Launch the app
  * Input deep linking data (_available since release 2.0_)
  * Get apps
  * Send key
  * Send keys
  * Send word
  * Mark timer (_available since release 2.0_)
  * Get timer (_available since release 2.0_)
  * Verify is playback started
  * Verify is screen loaded
  * Get child nodes (_available since release 2.1_)
  * Get element
  * Get elements
  * Get focused element
  * Verify is app loaded
  * Get current app info
  * Get device info
  * Get player info
  * Verify is channel exist
  * Set timeout
  * Set press delay
  * Get attribute

> A keyword will fail if its respective WebDriver endpoint returns a 4xx or 500 error.
### sideLoad
(_available since release 2.0_)
Keyword | Argument | Description | Example
---|---|---|---
sideLoad |
  * **channel** : The file path of a zipped package file.
  * **username** : Enter **rokudev** , which is the user name for the Development Application Installer.
  * **password** : The password for accessing the Development Application Installer on your Roku device.

| Sideloads an app that has been packaged into a zip file.

If the **sideLoad** command fails, [sideload](https://developer.roku.com/docs/developer-program/getting-started/developer-setup.md#sideloading-channels) the app to be tested and use the **launchTheChannel** command. | `await library.sideLoad("channel.zip", "rokudev", "your_device_password")`
### launchTheChannel
Keyword | Argument | Description | Example
---|---|---|---
launchTheChannel |
  * **channel_code** : The ID of the app to be launched.
  * **contentId** : The [contentId](https://developer.roku.com/docs/developer-program/discovery/implementing-deep-linking.md#understanding-deep-linking-parameters) of the content to be played. You can include this parameter and the **contentType** to execute deep linking tests.
  * **mediaType** : The [mediaType](https://developer.roku.com/docs/developer-program/discovery/implementing-deep-linking.md#understanding-deep-linking-parameters) of the content to be played. You can include this parameter and the **contentId** to execute deep linking tests.

| Launches the app corresponding to the specified app ID. | `await library.launchTheChannel("dev", "myMovie123", "movie")`
### inputDeepLinkingData
(_available since release 2.0_)
Keyword | Argument | Description | Example
---|---|---|---
inputDeepLinkingData |
  * **channelId** : The ID of the app to be launched.
  * **contentId** : The [contentId](https://developer.roku.com/docs/developer-program/discovery/implementing-deep-linking.md#understanding-deep-linking-parameters) of the content to be played. You can include this parameter and the **contentType** to execute deep linking tests.
  * **mediaType** : The [mediaType](https://developer.roku.com/docs/developer-program/discovery/implementing-deep-linking.md#understanding-deep-linking-parameters) of the content to be played. You can include this parameter and the **contentId** to execute deep linking tests.

| Launches the app corresponding to the specified app ID. | `await library.inputDeepLinkingData("dev", "myMovie123", "movie")`
### getApps
Keyword | Description | Example
---|---|---
getApps | Returns a list of installed apps as an array of objects. Each app object contains the following fields:
  * title
  * id
  * type
  * version
  * subtype

| ```
expect(apps[0].ID).to.equal('some_id')
const apps = await library.getApps()

```

### sendKey
Keyword | Arguments | Description | Example
---|---|---|---
sendKey |
  * **key_press** : The key to be pressed and released, which may be one of the following: "up", "down", "right", "left", "back, "select", "instantreplay", "play", "stop", "rev", "fwd", and "info".
  * **delay** : The delay (in seconds) before the keypresses are executed. This argument is optional, and it defaults to 2 seconds if not specified.

| Simulates the press and release of the specified key. | `await library.sendKey('select', 4)`
### sendKeys
Keyword | Arguments | Description | Example
---|---|---|---
sendKeys |
  * **sequence** : An array containing the sequence of keys to be pressed and released (for example, down, down, down, down, select).
  * **delay** : The delay (in seconds) before the keypresses are executed. This argument is optional, and it defaults to 2 seconds if not specified.

| Simulates the sequence of keypresses and releases. | `await library.sendKeys(['down', 'down', 'down', 'down', 'select'])`
### sendWord
Keyword | Arguments | Description | Example
---|---|---|---
sendWord |
  * **word** : The specified word to be entered.
  * **delay** : The delay (in seconds) before the entry of each letter in the specified word. This argument is optional, and it defaults to 2 seconds if not specified.

| Simulates the press and release of each letter in a word. | `await library.sendWord('user')`
### markTimer
(_available since release 2.0_)
Keyword | Description | Example
---|---|---
markTimer | Starts the timer. | `library.markTimer();`
### getTimer
(_available since release 2.0_)
Keyword | Description | Example
---|---|---
getTimer | Returns the number of milliseconds elapsed since the timer was last started. | ```
let res = await library.verifyIsPlaybackStarted(25, 1);
expect(res).to.equal(true);
let time = library.getTimer();
expect(14000).greaterThan(time);

```

### verifyIsPlaybackStarted
Keyword | Arguments | Description | Example
---|---|---|---
verifyIsPlaybackStarted |
  * **retries** : The number of requests that can be made before returning false. This argument is optional, and it defaults to 10 if not specified.
  * **delay** : The delay (in seconds) between retries. This argument is optional, and it defaults to 1 second if not specified.

| Verify playback has started on the Roku media player.

This keyword fails if player state is not "play". | `verifyIsPlaybackStarted(25, 2)`
### verifyIsScreenLoaded
Keyword | Arguments | Description | Example
---|---|---|---
Verify is screen loaded |
  * **data** : An object with locators for elementData and parentData (parentData is optional). See the [WebDriver element command](https://developer.roku.com/docs/developer-program/dev-tools/automated-channel-testing/web-driver.md#POST-v1/session/:sessionId/elements) command for more information.
  * **retries** : The number of requests that can be made before returning false. This argument is optional, and it defaults to 10 if not specified.
  * **delay** : The delay (in seconds) between retries. This argument is optional, and it defaults to 1 second if not specified.

| Verify that the screen is loaded based on the provided element data. | `verifyIsScreenLoaded({'elementData': [{'using': 'text', 'value': 'Barack Gates, Bill Obama'}]})`
### getChildNodes
Keyword | Arguments | Description | Example
---|---|---|---
getChildNodes |
  * **parentNode** : The parent node for which the child nodes are to be retrieved.

| Retrieves the child component of the specified node. | ```
const rowList = await library.getElement({"elementData" :[{"using": "tag", "value": "ZoomRowList"}]});
const searchData = [{"using": "tag", "value": "RenderableNode"}, {"using": "attr", "attribute": "focused", "value": "true"}];
const result = library.getChildNodes(rowList, searchData);

```

  * **locator** (optional): An array containing search criteria for the child nodes to be retrieved. The locator has the following syntax:
```
  "using" ("attr", "tag", "text") : specify locator type
  "value": tag or attribute value
  "attribute"(only for "attr" type): specify attribute

```

### getElement
Keyword | Arguments | Description | Example
---|---|---|---
Get element |
  * **data** : An object with locators for elementData and parentData (parentData is optional). See the [WebDriver element command](https://developer.roku.com/docs/developer-program/dev-tools/automated-channel-testing/web-driver.md#POST-v1/session/:sessionId/elements) for more information.
  * **delay** : The delay (in seconds) between retries. This argument is optional, and it defaults to 1 second if not specified.

| Searches for an element on the page based on the specified locator starting from the screen root. Returns information on the first matching element. | ```
const element = await library.getElement({'elementData': [{'using': 'attr', 'attribute': 'name', 'value': 'poster'}]}, 4);

const poster = library.getAttribute(element, 'uri');
expect(poster).to.equal('poster.png');

```

### getElements
Keyword | Arguments | Description | Example
---|---|---|---
getElements |
  * **data** : An object with locators for elementData and parentData (parentData is optional). See the [WebDriver element command](https://developer.roku.com/docs/developer-program/dev-tools/automated-channel-testing/web-driver.md#POST-v1/session/:sessionId/elements) for more information.
  * **delay** : The delay (in seconds) between retries. This argument is optional, and it defaults to 1 second if not specified.

| Searches for elements on the page based on the specified locators starting from the screen root. Returns information on the matching elements. | ```
const elements= await library.getElements({'elementData': [{'using': 'attr', 'attribute': 'name', 'value': 'poster'}]}, 4);

const poster = library.getAttribute(elements[0], 'uri');
expect(poster).to.equal('poster.png');

```

### getFocusedElement
Keyword | Description | Example
---|---|---
getFocusedElement | Return the element on the screen that currently has focus. See the [WebDriver active element command](https://developer.roku.com/docs/developer-program/dev-tools/automated-channel-testing/web-driver.md#get-v1/session/:sessionId/element/active) for more information. | ```
const element = await library.getFocusedElement()

const poster = library.getAttribute(element, 'uri');
expect(poster).to.equal('poster.png');

```

### verifyIsChannelLoaded
Keyword | Arguments | Description | Example
---|---|---|---
verifyIsChannelLoaded |
  * **id** : The ID of the app to be launched. Use `dev` to verify a sideloaded app.
  * **retries** : The number of requests that can be made before returning false. This argument is optional, and it defaults to 10 if not specified.
  * **delay** : The delay (in seconds) between retries. This argument is optional, and it defaults to 1 second if not specified.

| Verify that the specified app has been launched.

This keyword fails if the provided app ID does not match a valid app. | `await library.verifyIsChannelLoaded('dev')`
###getCurrentChannelInfo
Keyword | Description | Example
---|---|---
getCurrentChannelInfo | Returns an object containing information about the app currently loaded. This object has the following fields:
| **Key** | **Type** | **Description**
---|---|---
sessionId | string | The advertising ID of the device
status | int | A status code summarizing the result of the command.
value | array |
value[i].Title | string | The title of the app.
value[i].ID | string | The ID of the app.
value[i].Version | string | The build version of the app.
value[i].Subtype | string | "ndka"/"rsga"
value[i].Type | string | "menu"/"appl"
```
const data = await library.getPlayerInfo();
expect(data.Position).greaterThan(9000);

```

### getDeviceInfo
Keyword | Description | Example
---|---|---
getDeviceInfo | Returns an object containing the information about the device. This object has the following fields:
| **Key** | **Type** | **Description**
---|---|---
sessionId | string | The advertisement ID of the device.
status | int | A status code summarizing the result of the command.
value | object |
value.vendorName | string | The vendor of the device.
value.modelName | string | The model of the device.
value.language | string | The language of the device.
value.country | string | The country of the device.
value.ip | string | The IP address of the device.
value.timeout | int | The specified timeout for WebDriver client requests.
value.pressDelay | int | The specified delay between key presses.
```
const info = await library.getDeviceInfo()
expect(info.language).to.equal('en')

```

### getPlayerInfo
Keyword | Description | Example
---|---|---
getPlayerInfo | Returns an object containing information about the Roku media player. This object has the following fields:
| **Key** | **Type** | **Description**
---|---|---
sessionId | string | The advertising ID of the device
status | int | A status code summarizing the result of the command
value | object |
value.error | string | Indicates whether there was a playback error. If no error occurred, this is set to "false"
value.state | string | Indicates the current playback state ("play", "pause", "resume", and so on)
value.format | object | The **format** element contains the following attributes: _audio_ , _caption_ , _container_ , _drm_ , _video_ , and _res_.
value.format.audio | string | The audio compression method ("aac", "aac_adts", and so on.)
value.format.caption | string | The closed caption format ("608_708", for example). This value is set to "none" if there are no captions.
value.format.container | string | The container format ("hls", for example)
value.format.drm | string | The encoding type. If no encoding is used, this us set to "none".
value.format.video | string | The format of the currently playing video stream ("mpeg4-15", for example)
value.format.res | string | The resolution of the currently playing video stream ("1280X720", for example).
value.buffering | object | The **buffering** element contains the following attributes: _current_ , _max_ , _target_.
value.buffering.current | string | The current buffering speed (in kbps).
value.buffering.max | string | The maximum possible buffering speed (in kbps).
value.buffering.target | string | The target buffering speed (in kbps).
value.newStream | object | The **newStream** element contains the following attribute: _speed_.
value.newStream.speed | string | The current playback speed (in bps)
value.position | string | The time of the current position in the stream, expressed as the elapsed time (in ms) since the start of stream or UTC time, depending on the content.
value.duration | string | The duration of the video being played (in seconds). This becomes valid when playback begins and may change if the video is dynamic content, such as a live event.
value.isLive | string | A flag indicating whether the video being played is a live stream.
value.runtime | string | The runtime of the video being played (in seconds).
value.streamSegment | object | The **streamSegment** attribute contains Information about the video segment that is currently streaming. This is only meaningful for segmented video transports, such as DASH and HLS This element contains the following attributes: _bitrate_ , _mediaSequence_ , _segmentType_ , and _time_.
value.streamSegment.bitrate | string | The bitrate of the video segment (in bps).
value.streamSegment.mediaSequence | string | The HLS media sequence ID of the segment in the video.
value.streamSegment.segmentType | string | The type of data in the segment, which may be one of the following values: "audio", "video", "captions", "mux".
value.streamSegment.time | string | The chunk start time.
```
const data = await library.getPlayerInfo();
expect(data.Position).greaterThan(9000);

```

### verifyIsChannelExist
Keyword | Arguments | Description | Example
---|---|---|---
verifyIsChannelExist |
  * **apps** : An array containing currently installed on the device.
  * **id** : The ID of the app to be verified. Use `dev` to verify a sideloaded app.

| Verifies the specified app is installed on the device. This keyword fails if the **apps** array does not contain the app specified in the **id** argument. | ```
const apps = await library.getApps();
const res = library.verifyIsChannelExist(apps, 'dev');
expect(res).equal(true);

```

### setTimeout
Keyword | Arguments | Description | Example
---|---|---|---
setTimeout | **timeout** : The amount of time (in milliseconds) that Web driver client requests are allowed to run. | Sets the timeout for Web driver client requests. | `await library.setTimeout(10000)`
### setDelay
Keyword | Arguments | Description | Example
---|---|---|---
setDelay | **delay** : The interval (in milliseconds) to be used between key presses. | Sets the delay between key presses. This keyword works with the **Send keys** keyword. | `await library.setDelay(1000)`
### getAttribute
Keyword | Arguments | Description | Example
---|---|---|---
getAttribute |
  * **element** : An object that contains element information (attributes, child nodes).
  * **attr** : The name of the attribute to be retrieved.

| Get attribute value. This keyword fails if an element does not contain the specified attribute. | ```
const elements= await library.getElements({'elementData': [{'using': 'attr', 'attribute': 'name', 'value': 'poster'}]}, 4);

const poster = library.getAttribute(elements[0], 'uri');
expect(poster).to.equal('poster.png')

```

## Sample test cases
The [Roku automated app testing repository](https://github.com/rokudev/automated-channel-testing) includes a set of sample JavaScript test cases that can be executed on their corresponding [SceneGraph Developer Extensions (SGDEX) sample apps](https://github.com/rokudev/SceneGraphDeveloperExtensions/tree/master/samples). For example, you can execute the SGDEX GridView test case (**test_3_Grid.js**), which will sideload the corresponding sample app (**3_Grid**) on your device, and then view the test output. You can reference these samples when developing test scripts for the automated testing of your development apps.
> Before running a sample test case, you need to update the **sideload** command in the test case with the Roku device password.
The [**test_basic.js** sample](https://github.com/rokudev/automated-channel-testing/blob/master/jsLibrary/tests/test_basic.js) demonstrates how to create a simple test case that checks whether a user is authenticated before playing content using the Roku JavaScript Library:
```
const rokuLibrary = require("../library/rokuLibrary");
const expect = require("chai").expect;
const {
    spawn
} = require('child_process');
const childProcess = spawn('D:/projects/go/webDriver/src/main.exe');
let library;
describe('App should be launched', () => {
    before(() => {
        library = newrokuLibrary.Library("192.168.1.64");
    });

    it('Check if app exists on the device', asyncfunction() {
        this.timeout(5000);
        const apps = await library.getApps();
        const res = library.verifyIsChannelExist(apps, 'dev');
        expect(res).equal(true);
    });

    it('should launch the app', asyncfunction() {
        this.timeout(5000);
        await library.launchTheChannel('dev');
        await library.verifyIsChannelLoaded('dev');
    });

    after(async () => {
        await library.close();
        childProcess.kill();
    });

});

```

## Viewing the test case report and log
After you run a test case that uses the Roku JavaScript Library, you can view the generated report and log files in the specified output directory. The report summarizes the test case and provides statistics on the percentage of individual tests that passed/failed. The log details the success/failure of the individual keywords used in each test case.