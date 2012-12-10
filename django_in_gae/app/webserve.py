# -*- coding: utf-8 -*-

import urllib2, xmltodict
from django_in_gae.config import *



def getPrevisaoByWC(codigoWC):
    """
        Retorna as iformações climaticas atraver do Weather Location Codes/IDs 
        Disponivel no site http://edg3.co.uk/snippets/weather-location-codes/
         
    """
    import pdb;pdb.set_trace()
    response = urllib2.urlopen(URL_PREVICAO+codigoWC)
    
    headers = response.info()
    data = response.read()
    try:
        return xmltodict.parse(data)
    except:
        return None
    
    
    



