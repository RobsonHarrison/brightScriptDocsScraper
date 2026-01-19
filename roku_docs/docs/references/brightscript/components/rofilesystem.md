# roFileSystem
The roFilesystem component implements common filesystem inspection and modificationroutines.
All paths are matched case-insensitively, regardless of the case-sensitivity of the underlying filesystem. The supported character set is limited to only those characters supported by vfat filesystems (valid Windows characters). The usbplayer sample application is a good example of roFileSystem usage. USB devices with NTFS, HFS+, FAT16/32, exFAT, and Ext2/3 filesystems are supported. The USB filesystems are currently mounted read only.
This object is created with no parameters:
`CreateObject("roFileSystem")`
## Supported interfaces
  * [ifFileSystem](https://developer.roku.com/docs/references/brightscript/interfaces/iffilesystem.md "ifFileSystem")
  * [ifSetMessagePort](https://developer.roku.com/docs/references/brightscript/interfaces/ifsetmessageport.md "ifSetMessagePort")
  * [ifGetMessagePort](https://developer.roku.com/docs/references/brightscript/interfaces/ifgetmessageport.md "ifGetMessagePort")

## Supported events
  * [roFileSystemEvent](https://developer.roku.com/docs/references/brightscript/events/rofilesystemevent.md "roFileSystemEvent")