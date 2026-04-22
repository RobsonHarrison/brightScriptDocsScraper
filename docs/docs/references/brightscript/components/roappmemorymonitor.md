# roAppMemoryMonitor
The **roAppMemoryMonitor** component is used to subscribe apps to low-memory notifications. As of Roku OS 15.2, subscribed apps receive [roAppMemoryNotificationEvent](https://developer.roku.com/docs/references/brightscript/events/roappmemorynotificationevent.md) alerts when memory usage exceeds or falls below thresholds (currently 80%, 85%, 90%, 95% of the per-app limit). These thresholds may change in future releases. Notifications are throttled to prevent excessive events.
> The roAppMemoryMonitor functions are supported on all [current and updatable device models](https://developer.roku.com/docs/specs/hardware.md), except for Liberty, Austin, Mustang and Littlefield.
> Starting October 1, 2026, all apps must integrate the roAppMemoryMonitor interface and events to pass certification testing. If your app does not include these APIs, Static Analysis will report an error and block the publishing of your app.
## Supported interfaces
  * [ifAppMemoryMonitor](https://developer.roku.com/docs/references/brightscript/interfaces/ifappmemorymonitor.md)

## Supported events
  * [roAppMemoryNotificationEvent](https://developer.roku.com/docs/references/brightscript/events/roappmemorynotificationevent.md)
  * [ifSetMessagePort](https://developer.roku.com/docs/references/brightscript/interfaces/ifsetmessageport.md "ifSetMessagePort")
  * [ifGetMessagePort](https://developer.roku.com/docs/references/brightscript/interfaces/ifgetmessageport.md "ifGetMessagePort")