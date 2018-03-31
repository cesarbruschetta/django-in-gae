# -*- coding: utf-8 -*-

import urllib2, xmltodict, convertXML
from xml.etree.ElementTree import XML
from pygeoip import GeoIP

from django_in_gae.config import *

def to_dict(xml):
    try:
        tree = XML(xml)            
        tables = tree.getchildren()
        L = []

        for table in tables:
            D = {}
            for i in table.keys():
                D[i] = table.get(i)
            D['text'] = table.text
            
#            for i in table.getchildren():
#                D.update({i.tag.lower():i.text})
            L.append(D)
        return L
    except:
        return []

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
        return {}
    
def getCodigoCidadeWC(search):
    """
        Retorna o codigo WC (Weather Codes) da cidade buscada 
        Disponivel no site http://edg3.co.uk/snippets/weather-location-codes/
         
    """
    response = urllib2.urlopen(URL_BUSCA+urllib2.quote(search))
            
    headers = response.info()
    data = response.read()
    try:
        return to_dict(data)
    except:
        return {}

def getGeoIPbyIP(ip):
    return IP_by_DataBase(ip)
    # return IP_by_WebServer(ip)

def IP_by_DataBase(ip):
    """
        Retorna as iformações de geo posicionamento atraver da base de dados local 
        Disponivel no site http://appliedsec.github.com/pygeoip/
        Data Base http://dev.maxmind.com/geoip/geolite
         
    """
    gi = GeoIP(PATH_GEOIP_CITY)
    return gi.record_by_addr(ip) or {}
    
def IP_by_WebServer(ip):
    """
        Retorna as iformações de geo posicionamento atraver do Simple GeoIP service 
        Disponivel no site http://geo.xjs.pl/ ou http://goeipxjs.appspot.com/
         
    """
    response = urllib2.urlopen(URL_GEOIP+ip)
    
    headers = response.info()
    data = response.read()
    try:
        return xmltodict.parse(data)
    except:
        return {}
    