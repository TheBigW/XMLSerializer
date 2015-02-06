# -*- coding: utf-8 -*-
import lxml.etree as ET

class Serializer(object):

    def __init__(self):
        return None
    def getSerializeMembers(self, SerializeObject):
        strSerializeMembers = []
        for member in dir(SerializeObject):
            strMember = str(member)
            strType = str(type(getattr(SerializeObject, strMember )))
            print strMember + " : " + strType
            if (strType.find("descriptor") == -1) and (strType.find("function") == -1) and (strType.find("method") ==-1) and (strMember.find("__") != 0):
                strSerializeMembers.append(strMember)
        print "Serialize considered members : " + str(strSerializeMembers)
        return strSerializeMembers
    def SerializeArray(self, XMLParent, arrayInst):
        for arrayIndex, arrayItem in enumerate(arrayInst):
            self.SerializeMember(XMLParent, "elem" + str(arrayIndex), arrayItem )
    def SerializeMember(self, XMLParent, MemberName, newValue):
        strType = str(type(newValue))
        #print "serialize type : " + strType
        if strType.find("instance") != -1:
            XMLParent = ET.SubElement(XMLParent, MemberName)
            self.SerializeClass(newValue, XMLParent )
        elif strType.find("list") != -1:
            newElem = ET.SubElement(XMLParent, MemberName)
            self.SerializeArray(newElem, newValue )
        else:
            newElem = ET.SubElement(XMLParent, MemberName)
            newElem.text = str(newValue)
    def SerializeClass(self, SerializeObject, rootElem = None):
        strSerMemberNames = self.getSerializeMembers(SerializeObject)
        for strElem in strSerMemberNames:
            self.SerializeMember( rootElem, strElem, getattr(SerializeObject, strElem ) )
    def Serialize(self, SerializeObject):
        strClassName = SerializeObject.__class__.__name__
        rootElem = ET.Element( strClassName )
        self.SerializeClass(SerializeObject, rootElem)
        return ET.tostring(rootElem)

    def DeserializeArray(self, XMLParent, value):
        #array needs to have at least one value for correct type information, else values are read and treated as string
        theType = str
        if len(value) > 0:
            theType = type(value[0])
        arrayInst = []
        for arrayIndex, arrayNode in enumerate(XMLParent):
            arrayInst.append( self.DeserializeMember( arrayNode, value[0] ) )
        return arrayInst
    def DeserializeMember(self, XMLElem, value ):
        theType = type(value)
        strType = str(theType)
        print "Deserializing : " + strType
        if strType.find("instance") != -1:
            return self.DeserializeClass( value, XMLElem )
        elif strType.find("list") != -1:
            return  self.DeserializeArray( XMLElem, value )
        else:
            return theType(XMLElem.text)

    def DeserializeClass(self, SerializeObject, rootElem):
        strSerMemberNames = self.getSerializeMembers(SerializeObject)
        for strElem, xmlChildElem in zip(strSerMemberNames, rootElem):
            print "Deserializing : " +  strElem + " : "
            print str(xmlChildElem.text)
            setattr(SerializeObject, strElem, self.DeserializeMember(xmlChildElem, getattr(SerializeObject, strElem ) ) )
        return SerializeObject

    def DeSerialize(self, strXmlString, SerializeObject):
        strClassName = SerializeObject.__str__()
        print "className : " + strClassName
        root = ET.fromstring(strXmlString)
        return self.DeserializeClass(SerializeObject, root)