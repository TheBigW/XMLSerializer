# XMLSerializer
I like XML... Yes true I really do, but most if I do not need to care :). This is why I wrote the XML Serializer for python. Just dump in any object and grab your XML. The way back to object shall be easy as well.

Serialization

<code>
from XMLSerializer import Serializer<br><br/>
aInst = myClass()<br/>
ser = Serializer()<br/>
strXml = ser.Serialize(aInst)
</code>
....

Deserialization:

<code>
anotherInst = ser.DeSerialize( strXml, anotherInst )
</code>
