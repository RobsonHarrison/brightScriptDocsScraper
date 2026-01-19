# Node
The abstract base class of all SceneGraph nodes and the equivalent of the BrightScript roSGNode component. See [roSGNode](https://developer.roku.com/docs/references/brightscript/components/rosgnode.md "roSGNode") for supported interfaces.
**Node** class objects do not draw anything and are skipped in the render traversal of the SceneGraph node tree. The Node class provides the core parenting and key focus management functionality used by all nodes.
## Fields
Field | Type | Default | Access Permission | Description
---|---|---|---|---
id | string | "" | READ_WRITE | Adds a dictionary entry that allows the node to be retrieved with [ifSGNodeDict](https://developer.roku.com/docs/references/brightscript/interfaces/ifsgnodedict.md "ifSGNodeDict") findNode() function.
focusedChild | N/A | N/A | READ_WRITE | When a node or one of its children gains or loses the keyboard focus, the focusedChild field will be set and call its observer functions. In the observer function, typically, you use [ifSGNodeFocus](https://developer.roku.com/docs/references/brightscript/interfaces/ifsgnodefocus.md "ifSGNodeFocus") functions to query whether this node or some other node has the key focus or is in the key focus chain. Accessing the value of the field will result in script errors.
focusable | Boolean | false | READ_WRITE | Provides a hint as to whether or not this node can take the key focus.
change | associative array | { Index1: 0, Index2: 0, Operation: none } | READ_ONLY | Operations affecting the set of children of a Node are recorded in this field if, and only if, this field has been observed. The field associative array indicates the operation and two indexes, index1 and index 2, involved in the change. The operation is denoted by these value strings:  | Value | Meaning
---|---
none | No operation on the children nodes since the change field was observed, indexes are irrelevant
insert | A child node was inserted at _index1_. If multiple child nodes were inserted (for example, via the [insertChildren() function](https://developer.roku.com/docs/references/brightscript/interfaces/ifsgnodechildren.md#insertchildrenchild_nodes-as-object-index-as-integer-as-boolean)), the last inserted child node is stored at _index2_.
add | A child node was added to the end of the children node tree (at _index 1_). If multiple child nodes were added (for example, via the [appendChildren() function](https://developer.roku.com/docs/references/brightscript/interfaces/ifsgnodechildren.md#appendchildrenchild_nodes-as-object-as-boolean)), the last added child node is stored at _index2_.
remove | A child node was removed from position _index1_ , and if _index2_ >_index1_ , all the children nodes between _index1_ and _index2_ inclusive were removed
set | The child node at position _index1_ was replaced with a new child node
clear | All the children nodes were removed
move | The child node at position _index1_ was moved to the new position _index2_
setall | All the children nodes were replaced
modify | A pre-defined content meta-data field of a **ContentNode** node child at _index1_ was changed (_only_ set for **ContentNode** node children when a pre-defined content meta-data field changes)