# roList
The list object implements the interfaces: ifList, ifArray, ifEnum and therefore can behave like an array that can dynamically add members. The array operator [ ] can be used to access any element in the ordered list.
**Example**
Implementation:
```
list = CreateObject("roList")
list.AddTail("a")
list.AddTail("b")
list.AddTail("c")
list.AddTail("d")
list.ResetIndex()
x= list.GetIndex()
while x <> invalid
    print x
    x = list.GetIndex()
end while

print list[2]

```

Output:
```
a
b
c
d
c

```

## Supported Interfaces
  * [ifList](https://developer.roku.com/docs/references/brightscript/interfaces/iflist.md "ifList")
  * [ifArray](https://developer.roku.com/docs/references/brightscript/interfaces/ifarray.md "ifArray")
  * [ifArrayGet](https://developer.roku.com/docs/references/brightscript/interfaces/ifarrayget.md "ifArrayGet")
  * [ifArraySet](https://developer.roku.com/docs/references/brightscript/interfaces/ifarrayset.md "ifArraySet")
  * [ifEnum](https://developer.roku.com/docs/references/brightscript/interfaces/ifenum.md "ifEnum")
  * [ifListToArray](https://developer.roku.com/docs/references/brightscript/interfaces/iflisttoarray.md "ifListToArray")