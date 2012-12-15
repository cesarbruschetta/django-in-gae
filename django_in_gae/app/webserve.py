# -*- coding: utf-8 -*-

import urllib2, xmltodict, convertXML
from django_in_gae.config import *

from xml.etree.ElementTree import XML

def to_dict(xml):
    try:
        tree = XML(xml)            
        tables = tree.getchildren()
        L = []
        for table in tables:
            D = {}
            for i in table.getchildren():
                D.update({i.tag.lower():i.text})
            L.append(D)
        return L
    except:
        return None

def getPrevisaoByWC(codigoWC):
    """
        Retorna as iformações climaticas atraver do Weather Location Codes/IDs 
        Disponivel no site http://edg3.co.uk/snippets/weather-location-codes/
         
    """
    response = urllib2.urlopen(URL_PREVICAO+codigoWC)
    
    headers = response.info()
    data = response.read()
    try:
        return xmltodict.parse(data)
        #return convertXML.ConvertXmlToDict(data)
        #return to_dict(data)
    except:
        return None
