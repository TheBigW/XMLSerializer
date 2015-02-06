# XMLSerializer
I like XML... Yes true I really do, but most if I do not need to care :). This is why I wrote the XML Serializer. Just dump in any object and grab your XML. The way back to object shall be easy as well.

from XMLSerializer import Serializer

aInst = myClass()
ser = Serializer()
strXml = ser.Serialize(aInst)

....

anotherInst = ser.DeSerialize( strXml, anotherInst )
