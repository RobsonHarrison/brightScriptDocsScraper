# ifFontRegistry
## Implemented by
Name | Description
---|---
[roFontRegistry](https://developer.roku.com/docs/references/brightscript/components/rofontregistry.md "roFontRegistry") | The roFontRegistry object allows you to create roFont objects, either using the default font or using fonts in TrueType or OpenType files packaged with your application
## Supported methods
### Register(path as String) as Boolean
#### Description
Registers a font file (.ttf or .otf format). Each font file defines one or more font families (usually one).
#### Parameters
#### Return Value
A flag indicating whether the fonts in the specified file were successfully installed.
### GetFamilies() as Object
#### Description
Returns the names of the font families that have been registered via the [Register()](https://developer.roku.com/en-gb/docs/references/brightscript/interfaces/iffontregistry.md#registerpath-as-string-as-boolean) method. Each name can be passed as the first parameter to the [GetFont()](https://developer.roku.com/en-gb/docs/references/brightscript/interfaces/iffontregistry.md#getfontfamily-as-string-size-as-integer-bold-as-boolean-italic-as-boolean-as-object) method.
#### Return Value
An [roArray](https://developer.roku.com/docs/references/brightscript/components/roarray.md "roArray") of strings that represent the names of the font families that have been registered.
### GetFont(family as String, size as Integer, bold as Boolean, italic as Boolean) as Object
#### Description
Returns a font from the specified family, selected from the fonts previously registered via the [Register()](https://developer.roku.com/en-gb/docs/references/brightscript/interfaces/iffontregistry.md#registerpath-as-string-as-boolean) method.
#### Parameters
Name | Type | Description
---|---|---
family | String | The font family name.
size | Integer | The requested font size, in pixels, not points.
bold | Boolean | "bold" specifies a font variant that may be (but is not always) supported by the font file.
italic | Boolean | "italic" specifies a font variant that may be (but is not always) supported by the font file.
#### Return Value
An [roFont](https://developer.roku.com/docs/references/brightscript/components/rofont.md "roFont") object representing a font from the specified family.
### GetDefaultFont() as Object
#### Description
Returns the system font at its default size. Calling this method is the same as calling the [GetDefaultFont()](https://developer.roku.com/en-gb/docs/references/brightscript/interfaces/iffontregistry.md#getdefaultfontsize-as-integer-bold-as-boolean-italic-as-boolean-as-object) method with the following syntax: `reg.GetDefaultFont(reg.GetDefaultFontSize(), false, false)`.
#### Return Value
The system font as its default size.
### GetDefaultFont(size as Integer, bold as Boolean, italic as Boolean) as Object
#### Description
Returns the system font. The system font is always available, even if the [Register()](https://developer.roku.com/en-gb/docs/references/brightscript/interfaces/iffontregistry.md#registerpath-as-string-as-boolean) method has not been called
#### Parameters
Name | Type | Description
---|---|---
size | Integer | The requested font size, in pixels, not points.
bold | Boolean | "bold" specifies a font variant that may be (but is not always) supported by the font file.
italic | Boolean | "italic" specifies a font variant that may be (but is not always) supported by the font file.
#### Return Value
An roFont object representing the system font.
### GetDefaultFontSize() as Integer
#### Description
Returns the default font size.
#### Return Value
The default font size.
### Get(family as String, size as Integer, bold as Boolean, italic as Boolean) as String
#### Description
Returns a valid font string.
#### Parameters
Name | Type | Description
---|---|---
family | String | The font family name.
size | Integer | The requested font size, in pixels, not points.
bold | Boolean | "bold" specifies a font variant that may be (but is not always) supported by the font file.
italic | Boolean | "italic" specifies a font variant that may be (but is not always) supported by the font file.
#### Return Value
A valid font string.