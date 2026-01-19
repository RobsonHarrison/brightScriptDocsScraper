# Scene
Extends [**Group**](https://developer.roku.com/docs/references/scenegraph/layout-group-nodes/group.md "**Group**")
The **Scene** node class serves as the root of a SceneGraph node tree. Every **roSGScreen** object must have a **Scene** node, or a node that derives from the **Scene** node class as its root, including an XML markup component that extends the Scene node class or subclass. That node must be created using the **roSGScreen** createScene() function, with an argument that is a string of the name of the **Scene** node object created. For example:
```
screen = CreateObject("roSGScreen")
scene = screen.CreateScene("Scene")

```

While it is technically possible to have more than one scene per app, we recommend you only have one **roSGScreen** and one **Scene** node. Child nodes of the scene can be treated as different "scenes" where you can then implement transitions between them.
## Fields
Field | Type | Default | Access Permission | Description
---|---|---|---|---
backgroundURI | uri | invalid | READ_WRITE | Specifies a graphic image file to be used for the Scene node background.
limitBackgroundToUIResolution | boolean | true | READ_WRITE | If the scene background URI is overridden with a non-theme value and this field is set to true, the **backgroundURI** image is limited to the current screen size after being loaded.

if this field is set to false, the **backgroundURI** image is loaded without any scaling applied.
backgroundColor | color | 0x000000FF | READ_WRITE | Loads an image using the provided background URI as-is and does not apply any scaling whatsoever when "limitBackgroundToUIResolution" is false. Specifies a background color for the scene. This color is only used if the backgroundURI field is set to an empty string. For example:

scene.backgroundColor="0xEB1010FF"
scene.backgroundUri = ""
backExitsScene | Boolean | true | READ_WRITE | If true, a Back key press causes the scene to exit, back to the last user-focused item. If false, a Back key press does not cause the scene to exit. In order for the Back key to cause the scene to exit, the remote control focus must be explicitly set on the scene, or a child of the scene, using the [ifSGNodeFocus](https://developer.roku.com/docs/references/brightscript/interfaces/ifsgnodefocus.md "ifSGNodeFocus") interface setFocus(true) function. A Home key press always causes the scene to exit.
dialog | Node | invalid |  | Setting this field to a node extended from a **Dialog** node causes the dialog to be displayed
currentDesignResolution | assocarray |  | READ_WRITE | This read-only field is set when the Scene is initialized. It indicates which of an app's design resolutions (per manifest's ui_resolutions value) is being used, based on the player model and connected display type. Previously, a developer could deduct the same information by using both [roDeviceInfo.GetUIResolution](https://developer.roku.com/docs/references/brightscript/interfaces/ifdeviceinfo.md#getuiresolution-as-object\(\) "roDeviceInfo.GetUIResolution") and [roAppInfo.getValue](https://developer.roku.com/docs/references/brightscript/interfaces/ifappinfo.md#getvaluekey-as-string-as-string "roAppInfo.getValue")("ui_resolutions"). This new field simplifies the process.

The field is set to an AA with two numeric-valued keys — width and height — as well as a string value indicating the current design resolution ("HD", "FHD" or "SD").

```
Brightscript Debugger> ? myNode.getScene().currentDesignResolution
<Component: roAssociativeArray> =
{
    height: 720
    resolution: "HD"
    width: 1280
}

```

palette | RSGPalette node | not set | READ_WRITE | Defines the default color palette used by those nodes that have a **palette** field (for example, the **Scene** node, [standard dialogs](https://developer.roku.com/docs/references/scenegraph/standard-dialog-framework-nodes/standard-dialog.md), [dynamic custom voice keyboards](https://developer.roku.com/docs/references/scenegraph/dynamic-voice-keyboard-nodes/dynamic-keyboard-base.md), and so on).

Apps typically set the **Scene.palette** field to consistently color the standard dialogs and keyboards in the app.

Nodes that include a **palette** field can be set to an **RSGPalette** node to override the default colors specified in the **Scene** node.

If a node that supports a palette does not set its **palette** filed, the node looks up the scene graph until it finds a node with its **palette** field set.

If no ancestor node is found with its palette field set, the default color palette is used (grey with white text).

The RSGPalette color values used by the Scene node are as follows:
| Palette Color Name | Usages
---|---
PrimaryTextColor | The text color used for the entered text displayed in the VoiceTextEditBox node.
SecondaryTextColor | The text color used for the hints displayed in the VoiceTextEditBox.
InputFieldColor | The blend color applied to the VoiceTextEditBox background
DialogBackgroundColor | Blend color for dialog's background bitmap.
DialogItemColor | Blend color for the following items:

  * [StdDlgProgressItem's](https://developer.roku.com/docs/references/scenegraph/standard-dialog-framework-nodes/std-dlg-progress-item.md) spinner bitmap
  * [StdDlgDeterminateProgressItem's](https://developer.roku.com/docs/references/scenegraph/standard-dialog-framework-nodes/std-dlg-determinate-progress-item.md) graphic

DialogTextColor | Color for the text in the following items:

  * [StdDlgTextItem](https://developer.roku.com/docs/references/scenegraph/standard-dialog-framework-nodes/std-dlg-text-item.md) and [StdDlgGraphicItem](https://developer.roku.com/docs/references/scenegraph/standard-dialog-framework-nodes/std-dlg-graphic-item.md) if the **namedTextStyle** field is set to "normal" or "bold".
  * All [content area items](https://developer.roku.com/docs/references/scenegraph/standard-dialog-framework-nodes/std-dlg-item-base.md), except for [StdDlgTextItem](https://developer.roku.com/docs/references/scenegraph/standard-dialog-framework-nodes/std-dlg-text-item.md) and [StdDlgGraphicItem](https://developer.roku.com/docs/references/scenegraph/standard-dialog-framework-nodes/std-dlg-graphic-item.md).
  * [Title area](https://developer.roku.com/docs/references/scenegraph/standard-dialog-framework-nodes/std-dlg-title-area.md#fields). Unfocused button.

DialogFocusColor | Blend color for the following:

  * The [button area](https://developer.roku.com/docs/references/scenegraph/standard-dialog-framework-nodes/std-dlg-button-area.md#fields) focus bitmap.
  * The focused scrollbar thumb.

DialogFocusItemColor | Color for the text of the focused button.
DialogSecondaryTextColor | Color for the text of in the following items:

  * [StdDlgTextItem](https://developer.roku.com/docs/references/scenegraph/standard-dialog-framework-nodes/std-dlg-text-item.md) and [StdDlgGraphicItem](https://developer.roku.com/docs/references/scenegraph/standard-dialog-framework-nodes/std-dlg-graphic-item.md) if the **namedTextStyle** field is set to "secondary".
  * Disabled button.

DialogSecondaryItemColor | Color for the following items:

  * The divider displayed below the title area.
  * The unfilled portion of the [StdDlgDeterminateProgressItem's](https://developer.roku.com/docs/references/scenegraph/standard-dialog-framework-nodes/std-dlg-determinate-progress-item.md) graphic.

DialogInputFieldColor | The blend color for the text edit box background bitmap for keyboards used inside dialogs.
DialogKeyboardColor | The blend color for the keyboard background bitmap for keyboards used inside dialogs
DialogFootprintColor | The blend color for the following items:

  * The button focus footprint bitmap that is displayed when the [button area](https://developer.roku.com/docs/references/scenegraph/standard-dialog-framework-nodes/std-dlg-button-area.md#fields) does not have focus.
  * Unfocused scrollbar thumb and scrollbar track.