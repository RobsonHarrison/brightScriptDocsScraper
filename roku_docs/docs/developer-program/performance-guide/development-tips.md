# Top development tips
  * Processing Power: If your app is experiencing low frame rate or laggy transitions, Processing Power is probably the culprit. The difference in CPU between the low end and high end Roku device is large, and will likely only continue to grow as new models are released. As such, it is important to keep in mind that the animation that runs smoothly on a Dallas might not look as good, or even work at all, on a Tyler. Developers should be conscious of CPU intensive tasks and their impact on older devices.

> Developers should be conscious of CPU intensive tasks and their impact on older devices.
  * Know the remote control codes for special screens:
    * Dump Core: **Home 5x, Up, Rew 2x, FF 2x**
    * Debug Info on screen: **Home 5x, Rew 3x, FF 2x**
    * Channel Version Info: **Home 3x, Up 2x, Left, Right, Left, Right, Left**
    * Developer Settings Page: **Home 3x, Up 2x, Right, Left, Right, Left, Right**

  * The Developer settings page is necessary for enabling developer mode on your box.

  * All file paths are prefixed by the device name and a colon: `pkg:/filename.txt`. See [File System](https://developer.roku.com/docs/developer-program/getting-started/architecture/file-system.md) for more information.

  * Always use a screen facade object when launching your application so that it appears to the user that your app launches immediately and avoids screen flicker when exiting.

  * You can use the theme attributes of `roApplicationManager` (see [BrightScript Component Reference](https://developer.roku.com/docs/references/brightscript/language/component-architecture.md)) to create a new UI skin for your app.

  * When using rendezvous style registration and account linking, be sure to store the linking information in the device registry and not on your servers. We require that users are able to do a "Factory Reset" and be confident that no personally identifiable information is associated with the device. This is not possible if you have saved permanent serial number information on your servers.

  * There are a limited number of video content and streaming formats supported on the Roku Streaming Player. See [Audio and Video Support](https://developer.roku.com/docs/specs/media/streaming-specifications.md) for complete information on the supported formats.

  * We support `.mp3` audio files in the audio player.

  * Be sure to use a unique key for each application you publish and reuse this key each time you update your application using the "rekey" option. This ensures that all versions of your application will have access to the same registry data and avoid causing users to re-link after an update.

  * When using the slide show component, a high resolution image may take a while to download. A good trick to provide quick feedback to the user is to put an image in your package (so it's not downloading) that may have your logo, and informs the user that the slideshow is "Retrieving…". This slide could be the first slide in your slideshow so that feedback to the user is instant, and the slideshow never appears "hung".

  * We require that your web servers support range requests. If they do not, you may run into content that is not playable, or large images that do not display. The data will appear as a corrupted file format to our components, as the first block may be resent by the web server when we expect data at a particular range or offset.
  * The screens are displayed in a LIFO (stack) order. If this behavior is causing your screen to flicker (perhaps you wanted to pop two screens after you are done with the current one) there is a `Close()` method in the screen interface of all the screen and dialog components that deletes the screen out of the display stack. An example might be coming out of a Registration or Search page to a content springboard. From the content springboard, you might want to exit to your main screen, not the registration screen or search screen.