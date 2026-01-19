# Roku Voice overview
Roku Voice enables publishers to build voice-enabled apps that empower customers with the convenience of using their voice to launch, access, and control the playback of content. With Roku Voice, publishers can integrate the following features to accelerate content delivery and simplify playback:
  * [**Direct to Play**](https://developer.roku.com/en-gb/docs/features/voice/overview.md#direct-to-play). Launches requested content directly into playback.
  * [**Voice keyboards**](https://developer.roku.com/en-gb/docs/features/voice/overview.md#voice-keyboards). Enables customers to say their email address, password, PIN, and method of payment (MOP) when accessing an app.
  * [**Voice-enabled profile selection screens**](https://developer.roku.com/en-gb/docs/features/voice/overview.md#voice-enabled-profile-selection-screens). Enables customers to audibly select which user profile to use when accessing an app.
  * [**Voice controls**](https://developer.roku.com/en-gb/docs/features/voice/overview.md#voice-controls). Handles voice commands for controlling the playback of content.

## Direct to Play
Customers can use their Roku voice remote or mobile app to tell their device to play a movie, TV show, song, or other content. Their Roku device will then directly launch the app where the customer is entitled to the requested content and begin playback using a deep link.
For example, if a new viewer says "play Die Hart", the first episode of the Die Hart series on The Roku Channel is launched directly into playback.
To participate in direct-to-play, apps must have already implemented Roku Search and deep linking. SVOD and TVE apps must also send authentication status events to Roku.
For more information: [Direct to Play integration guide](https://developer.roku.com/docs/developer-program/discovery/direct-to-play.md).
## Voice keyboards
When customers sign up for an app or sign in, they can use their Roku voice remote or mobile app to audibly enter their credentials on a voice-enabled keyboard. This is faster and more convenient than having to manually locate and select each character on a legacy text keyboard. Roku provides voice keyboards for email, password, street address, PIN, and method of payment (MOP) entry with standard layouts, and apps may also build their own voice keyboards with custom layouts.
For more information: [Voice Keyboard reference documentation](https://developer.roku.com/docs/references/scenegraph/dynamic-voice-keyboard-nodes/dynamic-keyboard-base.md).
## Voice-enabled profile selection screens
Apps with a profile selection screen can audibly and visually prompt the customer to select a user profile and then handle a voice request with the name or position of the selected profile.
For more information: [Voice Profile Selection integration guide](https://developer.roku.com/docs/developer-program/media-playback/voice-controls/voice-profile-selector.md).
## Voice controls
Once playback begins, customers can use basic voice commands to fast forward, rewind, and pause the video. Apps can further enhance their voice capabilities and make it even easier for customers to control the playback of their content by supporting enhanced voice commands such as “skip ahead 2 minutes”, “go back 30 seconds”, and “start over”. Apps can also support additional enhanced controls such as "what's playing" to display the name of the content currently in playback.
For more information: [Voice controls integration guide](https://developer.roku.com/docs/developer-program/media-playback/voice-controls/transport-controls.md).