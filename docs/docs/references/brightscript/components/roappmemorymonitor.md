# roAppMemoryMonitor
The **roAppMemoryMonitor** component is used to subscribe apps to low-memory notifications. When an app is subscribed, it receives a [roAppMemoryNotificationEvent ](https://developer.roku.com/docs/references/brightscript/events/roappmemorynotificationevent.md)when it reaches a specific percentage of the per-app memory limit (80%).
> The roAppMemoryMonitor functions are supported on all [current and updatable device models](https://developer.roku.com/docs/specs/hardware.md), except for Liberty, Austin, Mustang and Littlefield.
## Supported interfaces
  * [ifAppMemoryMonitor](https://developer.roku.com/docs/references/brightscript/interfaces/ifappmemorymonitor.md)

## Supported events
  * [roAppMemoryNotificationEvent](https://developer.roku.com/docs/references/brightscript/events/roappmemorynotificationevent.md)
  * [ifSetMessagePort](https://developer.roku.com/docs/references/brightscript/interfaces/ifsetmessageport.md "ifSetMessagePort")
  * [ifGetMessagePort](https://developer.roku.com/docs/references/brightscript/interfaces/ifgetmessageport.md "ifGetMessagePort")