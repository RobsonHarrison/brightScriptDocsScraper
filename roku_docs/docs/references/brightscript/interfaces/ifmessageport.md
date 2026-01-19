# ifMessagePort
## Implemented by
Name | Description
---|---
[roMessagePort](https://developer.roku.com/docs/references/brightscript/components/romessageport.md "roMessagePort") | A Message Port is the place messages (events) are sent
## Supported methods
### WaitMessage(timeout as Integer) as Dynamic
#### Description
Waits until an event object is available or timeout milliseconds have passed.
#### Parameters
Name | Type | Description
---|---|---
timeout | Integer | The number of milliseconds to wait for a message. If this parameter is set to 0, this method waits indefinitely for a message, with no timeout.

The native [wait()](https://developer.roku.com/docs/references/brightscript/language/global-utility-functions.md#waittimeout-as-integer-port-as-object-as-object) function can also be used to get the event object which WaitMessage() would return. This means that the following two statements have the same effect:
```
msg = port.WaitMessage(timeout)
msg = wait(timeout, port)

```

#### Return Value
If an event is available, it is returned. If the timeout expires, invalid is returned.
### GetMessage() as Dynamic
#### Description
If an event object is available, it is returned. Otherwise invalid is returned. The method returns immediately in either case and does not wait.
#### Return Value
An event object.
### PeekMessage() as Dynamic
#### Description
This method is similar to the [GetMessage()](https://developer.roku.com/en-gb/docs/references/brightscript/interfaces/ifmessageport.md#getmessage-as-dynamic) method, but the returned object (if not invalid) remains in the message queue. A later call to [WaitMessage()](https://developer.roku.com/en-gb/docs/references/brightscript/interfaces/ifmessageport.md#waitmessagetimeout-as-integer-as-dynamic), [GetMessage()](https://developer.roku.com/en-gb/docs/references/brightscript/interfaces/ifmessageport.md#getmessage-as-dynamic) or PeekMessage() will return the same message.
#### Return Value
An event object.