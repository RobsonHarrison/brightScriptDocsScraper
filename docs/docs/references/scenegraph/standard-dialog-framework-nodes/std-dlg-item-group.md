# StdDlgItemGroup
Extends [StdDlgItemBase](https://developer.roku.com/docs/references/scenegraph/standard-dialog-framework-nodes/std-dlg-item-base.md)
The **StdDlgItemGroup** node is used to visually group a set of StdDlgAreaBase child nodes in a custom dialog. Developers can use this node to reduce the vertical spacing between the StdDlgItemBase child nodes. For [**StdDlgActionCardItem**](https://developer.roku.com/docs/references/scenegraph/standard-dialog-framework-nodes/std-dlg-action-card-item.md) nodes, the **StdDlgItemGroup** node enforces the rule that when multiple items **StdDlgActionCardItem** nodes have their **iconType** field set to "radiobutton", only one may have its **selected** status be set to "true".
The **StdDlgItemGroup** node may contain one or more [**StdDlgItemBase**](https://developer.roku.com/docs/references/scenegraph/standard-dialog-framework-nodes/std-dlg-item-base.md) child nodes (for example, StdDlgTextItem, StdDlgGraphicItem, and so on) as its children. It will visually group those child **StdDlgItemBase** nodes by reducing the amount of vertical space between them. However, the primary benefit of the StdDlgItemGroup node is managing **StdDlgActionCardItem** child nodes that have their **iconType** field set to "radiobutton".
![roku815px - actionCards-radio-checkbox-items](https://image.roku.com/ZHZscHItMTc2/actionCards-radio-checkbox-items.jpg)
> See the [**stdDlgActionCardItem** documentation](https://developer.roku.com/docs/references/scenegraph/standard-dialog-framework-nodes/std-dlg-action-card-item.md#radiobutton-icontype) for code demonstarting how to use the **StdDlgItemGroup** node in a custom dialog.
#### Fields
Field | Type | Default | Access Permission | Description
---|---|---|---|---
selectedIndex | integer | 0 | READ_WRITE | The index of the currently selected [StdDlgAreaBase](https://developer.roku.com/docs/references/scenegraph/standard-dialog-framework-nodes/std-dlg-area-base.md) child node. This field is updated when the user selects any of the [StdDlgActionCardItem](https://developer.roku.com/docs/references/scenegraph/standard-dialog-framework-nodes/std-dlg-action-card-item.md) child nodes.

This field can also be updated via BrightScript to change which child node in the StdDlgItemGroup is selected.

When this field is updated and it corresponds to a [StdDlgActionCardItem](https://developer.roku.com/docs/references/scenegraph/standard-dialog-framework-nodes/std-dlg-action-card-item.md) node that has its **iconType** field set to "radiobutton", the **StdDlgItemGroup** node enforces the "only 1 of _n_ " rule for radio buttons by setting the **iconStatus** field of the other radio button action card items to "false".
## Sample app
You can download and install a [sample app](https://github.com/rokudev/standard-dialog-framework) that demonstrates how to create a custom dialog that includes action card items in an item group.