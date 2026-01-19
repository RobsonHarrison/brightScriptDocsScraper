# ifArraySet
The ifArraySet interface supports the array indexing operator [].
(See ArrayOperator)
## Implemented by
Name | Description
---|---
[roArray](https://developer.roku.com/docs/references/brightscript/components/roarray.md "roArray") | An array stores an indexed collection of BrightScript objects. Each entry of an array can be a different type, or they may all of the same type
[roByteArray](https://developer.roku.com/docs/references/brightscript/components/robytearray.md "roByteArray") | The byte array component is used to contain and manipulate an arbitrary array of bytes
[roList](https://developer.roku.com/docs/references/brightscript/components/rolist.md "roList") | The list object implements the interfaces: ifList, ifArray, ifEnum and therefore can behave like an array that can dynamically add members
[roXMLList](https://developer.roku.com/docs/references/brightscript/components/roxmllist.md "roXMLList") | Contains a list of roXML objects
## Supported methods
### SetEntry(index As Integer, tvalue As Dynamic) As Void
#### Description
Sets an entry at a given index to the passed value. If index is beyond the bounds of the array, the array is expanded to accommodate it.
#### Parameters
Name | Type | Description
---|---|---
index | Integer | The entry to be updated.
tvalue | Dynamic | The new value for the specified entry.