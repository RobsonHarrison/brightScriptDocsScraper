# Text to speech
> This feature is only available on the following devices: Roku Streaming Stick (3600X), Roku Express (3700X) and Express+ (3710X), Roku Premiere (4620X) and Premiere+ (4630X), Roku Ultra (4640X), and any Roku TV running Roku OS 7.2 and later.
* * *
## Text to speech components
_Components available since Roku OS 7.2_
Text to speech (TTS) allows the developer to provide an audible spoken version of the strings shown to the user in the app. For platforms that are required to comply with the [FCC Communications and Video Accessibility Act of 2010 (CVAA)](https://www.fcc.gov/consumers/guides/21st-century-communications-and-video-accessibility-act-cvaa), this capability can be used as part of compliance with CVAA, and the current text to speech flite_tts library is built into the image. The Roku text to speech capability supports different languages, voices, rates of speech, volume of speech, and other aspects of text to speech. Roku provides text to speech support in the following components, interfaces, and events:
  * [roTextToSpeech](https://developer.roku.com/docs/references/brightscript/components/rotexttospeech.md)
  * [ifTextToSpeech](https://developer.roku.com/docs/references/brightscript/interfaces/iftexttospeech.md)
  * [roTextToSpeechEvent](https://developer.roku.com/docs/references/brightscript/events/rotexttospeechevent.md)

Components available since Roku OS 7.5
  * [roAudioGuide](https://developer.roku.com/docs/references/brightscript/components/roaudioguide.md)
  * [ifAudioGuide](https://developer.roku.com/docs/references/brightscript/interfaces/ifaudioguide.md)

## Screen reader behavior for SceneGraph nodes
  * **[ArrayGrid](https://developer.roku.com/docs/references/scenegraph/abstract-nodes/arraygrid.md)** : speaks focused item ([ContentMetaData::TITLE](https://developer.roku.com/docs/developer-program/getting-started/architecture/content-metadata.md#descriptive-attributes)), followed by navigation hint, then ContentMetaData::AUDIO_GUIDE_SUFFIX (if any).

  * **[Button](https://developer.roku.com/docs/references/scenegraph/widget-nodes/button.md)** : text of button is spoken only if focused

  * **[ButtonGroup](https://developer.roku.com/docs/references/scenegraph/layout-group-nodes/buttongroup.md#fields)** : speaks focused [Button](https://developer.roku.com/docs/references/scenegraph/widget-nodes/button.md), followed by navigation hint (“button 1 of 4”), followed by button-specific hint, if any (Button-specific hint is spoken only for StarRatingButton).

  * **[CheckList](https://developer.roku.com/docs/references/scenegraph/list-and-grid-nodes/checklist.md)** : speaks focused item (ContentMetaData::AUDIO_GUIDE_TEXT if any; otherwise [ContentMetaData::TITLE](https://developer.roku.com/docs/developer-program/getting-started/architecture/content-metadata.md#descriptive-attributes)) followed by navigation hint (“checkbox, checked, 1 of 4”)

  * **[Dialog](https://developer.roku.com/docs/references/scenegraph/dialog-nodes/dialog.md)** : speaks `title`, `message`, and `bulletText` (if any), then reads focused button

  * **[Keyboard](https://developer.roku.com/docs/references/scenegraph/widget-nodes/keyboard.md)** : speaks hint about caps lock toggling (once), then speaks focused key

  * **[KeyboardDialog](https://developer.roku.com/docs/references/scenegraph/standard-dialog-framework-nodes/standard-keyboard-dialog.md)** : speaks title, then keyboard

  * **[Label](https://developer.roku.com/docs/references/scenegraph/label-nodes/label.md)** : speaks `text` field

  * **[LabelList](https://developer.roku.com/docs/references/scenegraph/list-and-grid-nodes/labellist.md)** : speaks focused ContentMetaData::AUDIO_GUIDE_TEXT if any; otherwise speaks [ContentMetaData::TITLE](https://developer.roku.com/docs/developer-program/getting-started/architecture/content-metadata.md#descriptive-attributes), followed by navigation hint.

  * **[MarkupGrid](https://developer.roku.com/docs/references/scenegraph/list-and-grid-nodes/markupgrid.md)** : speaks focused ContentMetaData::AUDIO_GUIDE_TEXT if any; otherwise speaks [ContentMetaData::TITLE](https://developer.roku.com/docs/developer-program/getting-started/architecture/content-metadata.md#descriptive-attributes), followed by navigation hint, then ContentMetaData::AUDIO_GUIDE_SUFFIX (if any), then MEDIA speech (see below)

  * **[MarkupList](https://developer.roku.com/docs/references/scenegraph/list-and-grid-nodes/markuplist.md)** : speaks focused item ([ContentMetaData::TITLE](https://developer.roku.com/docs/developer-program/getting-started/architecture/content-metadata.md#descriptive-attributes)), followed by navigation hint, then ContentMetaData::AUDIO_GUIDE_SUFFIX (if any).

  * **[MiniKeyboard](https://developer.roku.com/docs/references/scenegraph/widget-nodes/minikeyboard.md)** : speaks focused key

  * **[PinDialog](https://developer.roku.com/docs/references/scenegraph/standard-dialog-framework-nodes/standard-pinpad-dialog.md)** : speaks dialog title, whether in key pad, then focused key or button

  * **[PinPad](https://developer.roku.com/docs/references/scenegraph/widget-nodes/pinpad.md)** : speaks focused key

  * **[Poster](https://developer.roku.com/docs/references/scenegraph/renderable-nodes/poster.md)** : if focused, speaks `audioGuideText` field (if set)

  * **[PosterGrid](https://developer.roku.com/docs/references/scenegraph/list-and-grid-nodes/postergrid.md)** : speaks focused item ([ContentMetaData::TITLE](https://developer.roku.com/docs/developer-program/getting-started/architecture/content-metadata.md#descriptive-attributes)), followed by navigation hint.

  * **[ProgressDialog](https://developer.roku.com/docs/references/scenegraph/dialog-nodes/progressdialog.md)** : speaks dialog `title`, `message`, and `bulletText` every 15 seconds. Speaks focused button if there is any.

  * **[RadioButtonList](https://developer.roku.com/docs/references/scenegraph/list-and-grid-nodes/radiobuttonlist.md)** : speaks focused item (ContentMetaData::AUDIO_GUIDE_TEXT if any; otherwise, ContentMetaData::TITLE), followed by navigation and selection hint

  * **RenderableNode** : if speaking focused item (depends on context), will speak focused descendant; otherwise, will speak all descendants

  * **[RowList](https://developer.roku.com/docs/references/scenegraph/list-and-grid-nodes/rowlist.md)** : speaks row label (when row becomes focused), then speaks focused **[PosterGrid](https://developer.roku.com/docs/references/scenegraph/list-and-grid-nodes/postergrid.md)** or **[MarkupGrid](https://developer.roku.com/docs/references/scenegraph/list-and-grid-nodes/markupgrid.md)** (MarkupGrid is used if itemComponentName is non-empty)

  * **[ScrollableText](https://developer.roku.com/docs/references/scenegraph/typographic-nodes/scrollabletext.md)** : speaks `text` field

  * **[ScrollingLabel](https://developer.roku.com/docs/references/scenegraph/typographic-nodes/scrollinglabel.md)** : speaks `text` field

  * **[Video](https://developer.roku.com/docs/references/scenegraph/media-playback-nodes/video.md)** : speaks HUD if displayed by user

**Screen reader behavior for built-in SceneGraph panels and scenes:**
  * **[GridPanel](https://developer.roku.com/docs/references/scenegraph/sliding-panels-nodes/gridpanel.md)** : speaks panel, then **leftLabel**

  * **[ListPanel](https://developer.roku.com/docs/references/scenegraph/sliding-panels-nodes/listpanel.md)** : speaks panel, then **leftLabel**

  * **[PanelSet](https://developer.roku.com/docs/references/scenegraph/sliding-panels-nodes/panelset.md)** :
    * If left panel is focused, speaks focused left panel, then unfocused right panel (if any)
    * If right panel is focused, speaks unfocused left panel, then focused right panel
    * If no panel is focused, speaks unfocused left panel, then unfocused right panel (if any)

  * **[OverhangPanelSetScene](https://developer.roku.com/docs/references/scenegraph/sliding-panels-nodes/overhangpanelsetscene.md)** : uses **[Overhang](https://developer.roku.com/docs/references/scenegraph/sliding-panels-nodes/overhang.md)** title when speaking location

  * **[Scene](https://developer.roku.com/docs/references/scenegraph/scene.md)** : speaks dialog (if any); otherwise speaks [PanelSet](https://developer.roku.com/docs/references/scenegraph/sliding-panels-nodes/panelset.md) (if any); otherwise speaks as RenderableNode

**MEDIA speech is spoken in the following order:**
  * [ContentMetaData::TEXT](https://developer.roku.com/docs/developer-program/getting-started/architecture/content-metadata.md#descriptive-attributes)
  * [ContentMetaData::DESCRIPTION](https://developer.roku.com/docs/developer-program/getting-started/architecture/content-metadata.md#descriptive-attributes)
  * [ContentMetaData::DIRECTORS](https://developer.roku.com/docs/developer-program/getting-started/architecture/content-metadata.md#descriptive-attributes)
  * [ContentMetaData::PRODUCERS](https://developer.roku.com/docs/developer-program/getting-started/architecture/content-metadata.md#descriptive-attributes)
  * [ContentMetaData::ACTORS](https://developer.roku.com/docs/developer-program/getting-started/architecture/content-metadata.md#descriptive-attributes)
**There is no additional speech for the following nodes (they will behave the same as RenderableNode):**
  * [BifDisplay](https://developer.roku.com/docs/references/scenegraph/media-playback-nodes/video.md#fields)
  * [BusySpinner](https://developer.roku.com/docs/references/scenegraph/widget-nodes/busyspinner.md)
  * [LayoutGroup](https://developer.roku.com/docs/references/scenegraph/layout-group-nodes/layoutgroup.md)
  * [Overhang](https://developer.roku.com/docs/references/scenegraph/sliding-panels-nodes/overhang.md)
  * [Panel](https://developer.roku.com/docs/references/scenegraph/sliding-panels-nodes/panel.md)
  * [ProgressBar](https://developer.roku.com/docs/references/scenegraph/media-playback-nodes/video.md#fields)
  * [Rectangle](https://developer.roku.com/docs/references/scenegraph/renderable-nodes/rectangle.md)
  * [TextEditBox](https://developer.roku.com/docs/references/scenegraph/widget-nodes/texteditbox.md)
  * [TrickPlayBar](https://developer.roku.com/docs/references/scenegraph/media-playback-nodes/video.md#fields)

## Implementation tips
### TTS interruptions
Many UI elements have default TTS behavior. It is possible that speech triggered by these implementations can interrupt your TTS implementation at times. You should keep track of the IDs of your TTS utterances, as returned by say() and silence(), and handle interruptions accordingly.
### Other TTS implementation changes
Other TTS implementations may change the current voice, the current language, the current volume, the current pitch, and/or the current speech rate. You should keep track of how these parameters might change.
### Long text delays
A long text string to be spoken by TTS may have a noticeable delay before starting the speech, at least for the first speech of the long string. For long text strings, you can break up the text string so that the first speech is a reasonably short sentence, followed by longer sentences as needed. You should not break up the long text string into individual words, as it will affect phrasing without improving the perceived delay in any noticeable way.