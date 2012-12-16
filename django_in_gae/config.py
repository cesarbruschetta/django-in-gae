# -*- coding: utf-8 -*-

from django_in_gae.settings import PROJECT_ROOT_PATH
import os

URL_PREVICAO = 'http://weather.service.msn.com/data.aspx?src=vista&weadegreetype=C&culture=pt-BR&wealocations=wc:'

URL_BUSCA = 'http://xoap.weather.com/search/search?where='

URL_GEOIP = 'http://goeipxjs.appspot.com/xml/'


PATH_GEOIP = os.path.join(PROJECT_ROOT_PATH,'geoip','GeoIP.dat')
PATH_GEOIP_CITY = os.path.join(PROJECT_ROOT_PATH,'geoip','GeoLiteCity.dat')