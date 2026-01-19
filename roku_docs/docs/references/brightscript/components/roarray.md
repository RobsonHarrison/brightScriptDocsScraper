# roArray
An array stores an indexed collection of BrightScript objects. Each entry of an array can be a different type, or they may all of the same type.
An roArray is created with two parameters:
**CreateObject("roArray", size as Integer, resize as Boolean)**
Size is the initial number of elements allocated for the array. If resize is true, the array will be resized if needed to accommodate more elements. If the array is large, this might be slow. The "dim" statement may be used instead of CreateObject to allocate a new array. Dim has the advantage in that it automatically creates arrays of arrays for multi-dimensional arrays.
## Supported interfaces
  * [ifArray](https://developer.roku.com/docs/references/brightscript/interfaces/ifarray.md "ifArray")
  * [ifArrayGet](https://developer.roku.com/docs/references/brightscript/interfaces/ifarrayget.md "ifArrayGet")
  * [ifArraySet](https://developer.roku.com/docs/references/brightscript/interfaces/ifarrayset.md "ifArraySet")
  * [ifEnum](https://developer.roku.com/docs/references/brightscript/interfaces/ifenum.md "ifEnum")
  * [ifArrayJoin](https://developer.roku.com/docs/references/brightscript/interfaces/ifarrayjoin.md "ifArrayJoin")
  * [ifArraySizeInfo](https://developer.roku.com/docs/references/brightscript/interfaces/ifarraysizeinfo.md "ifArraySizeInfo")
  * [ifArraySort](https://developer.roku.com/docs/references/brightscript/interfaces/ifarraysort.md "ifArraySort")
  * [ifArraySlice](https://developer.roku.com/docs/references/brightscript/interfaces/ifarrayslice.md "ifArraySlice")