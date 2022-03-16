---
aliases: XML
tags: #50.001
---
[[IS & Programming|ISP]]
[[Android 0]]

## XML Documents must have a Root Element
XML documents must contain one **root** element that is the **parent** of all other elements:
```xml
<root>  
 <child>  
 <subchild>.....</subchild>  
 </child>  
</root>
```
In this example `<note>` is the root element:
```xml
<?xml version="1.0" encoding="UTF-8**"**?>  
<note>  
 <to>Tove</to>  
 <from>Jani</from>  
 <heading>Reminder</heading>  
 <body>Don't forget me this weekend!</body>  
</note>
```
## The XML Prolog
This line is called the XML **prolog**:
```xml
<?xml version="1.0" encoding="UTF-8**"**?>
```
The XML prolog is optional. If it exists, it must come first in the document.

XML documents can contain international characters, like Norwegian øæå or French êèé.

To avoid errors, you should specify the encoding used, or save your XML files as UTF-8.

UTF-8 is the default character encoding for XML documents.

Character encoding can be studied in our [Character Set Tutorial](https://www.w3schools.com/charsets/default.asp).
## All XML Elements must have a closing tag
In XML, it is illegal to omit the closing tag. All elements **must** have a closing tag:
```xml
<p>This is a paragraph.</p>  
<br />
```
## XML Tags are Case Sensitive
XML tags are case sensitive. The tag `<Letter>` is different from the tag `<letter>`.

Opening and closing tags must be written with the same case:
```xml
<message>This is correct</message>
```
"Opening and closing tags" are often referred to as "Start and end tags". Use whatever you prefer. It is exactly the same thing.
## XML Elements must be properly nested
In HTML, you might see improperly nested elements:
```html
<b><i>This text is bold and italic</b></i>
```
In XML, all elements **must** be properly nested within each other:
```xml
<b><i>This text is bold and italic</i></b>
```
In the example above, "Properly nested" simply means that since the `<i>` element is opened inside the `<b>` element, it must be closed inside the `<b>` element.
## XML Attribute Values must always be Quoted
XML elements can have attributes in name/value pairs just like in HTML.

In XML, the attribute values must always be quoted:
```xml
<note date="12/11/2007">  
 <to>Tove</to>  
 <from>Jani</from>  
</note>
```
## Entity References
Some characters have a special meaning in XML.

If you place a character like "<" inside an XML element, it will generate an error because the parser interprets it as the start of a new element.

This will generate an XML error:
```xml
<message>salary < 1000</message>
```
To avoid this error, replace the "<" character with an **entity reference**:
```xml
<message>salary &lt; 1000</message>
```
There are 5 pre-defined entity references in XML:

| Entity reference | Symbol | What it is   |
| ---------------- | ------ | ------------ |
| `&lt;`           | <      | less than    |
| `&gt`            | >      | greater than |
| `&amp;`          | &      | ampersand    |
| `&apos;`         | '      | apostrophe   |
| `&quot;`         | "      | quotation mark             |

Only < and & are strictly illegal in XML, but it is a good habit to replace > with &gt; as well.
## Comments in XML
The syntax for writing comments in XML is similar to that of HTML:
```xml
<!-- This is a comment -->
```
Two dashes in the middle of a comment are not allowed:
```xml
<!-- This is an invalid -- comment -->
```
## White-space is Preserved in XML
XML does not truncate multiple white-spaces (HTML truncates multiple white-spaces to one single white-space):
XML:
`Hello           Tove`

HTML:
`Hello Tove`
## XML stores new line as LF
Windows applications store a new line as: carriage return and line feed (CR+LF).

Unix and Mac OSX use LF.

Old Mac systems use CR.

XML stores a new line as LF
## Well Formed XML
XML documents that conform to the syntax rules above are said to be "Well Formed" XML documents.