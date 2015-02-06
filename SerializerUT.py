# -*- coding: utf-8 -*-
#con = httplib.HTTPConnection('api.bandcamp.com')
#con.request("GET", "/api/band/3/search?key=<>name=amanda%20palmer")
#resp = con.getresponse()
#print( resp.read() )
from lxml import objectify, etree
from cStringIO import StringIO
import pickle
import httplib
import re
from XMLSerializer import Serializer


class MemberClass:
    def __init__(self):
        self.m_strTest = "just some junk..."
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            print "eq : " + str(self.__dict__ )+ " AND : " +  str(other.__dict__)
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


class myClass(object):
    def __init__(self):
        self.m_strContent = 'some string content'
        self.m_iContent = 123
        self.m_fcontent = 2.3
        self.m_Array = [1, 2, 3, 4]
        self.m_classMember = MemberClass()
    def initDifferent(self):
        self.m_strContent = 'tralalala'
        self.m_iContent = 345
        self.m_fcontent = 8.8
        self.m_Array = [5, 6, 7, 8]
        self.m_classMember = MemberClass()
        self.m_classMember.m_strTest = "some differnt junk"

    def __eq__(self, other):
        return self.m_strContent == other.m_strContent and self.m_iContent == other.m_iContent and self.m_fcontent == other.m_fcontent and self.m_Array == other.m_Array and self.m_classMember.m_strTest == other.m_classMember.m_strTest

    def __ne__(self, other):
        return not self.__eq__(other)

    m_strContent = 'some string content'
    m_iContent = 123
    m_fcontent = 2.3
    m_Array = [1, 2, 3, 4]
    m_classMember = MemberClass()
    def giveSomeString(self):
        return "hello yeah!"

src = StringIO()
p = pickle.Pickler(src)

testList = list()
for k in range(0, 10):
    aInst = myClass()
    aInst.m_iContent = k
    aInst.m_strContent = "Iteration No." + str(k)
    aInst.m_fcontent = float(k)
    testList.append( aInst )
p.dump(testList)

value = src.getvalue()

print( value )


aInst = myClass()
ser = Serializer()
strXml = ser.Serialize(aInst)
print "XML : " + strXml

anotherInst = myClass()
anotherInst.initDifferent()
print "now they are different? : " + str(aInst != anotherInst)

anotherInst = ser.DeSerialize( strXml, anotherInst )
#just for contol
strXml = ser.Serialize(anotherInst)

print "Deserialized XML : " + strXml
print "same as before? : " + str(aInst == anotherInst)

#loadedList = pickle.load( value )
#print(loadedList)