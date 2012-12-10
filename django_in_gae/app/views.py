# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from django_in_gae.app.webserve import getPrevisaoByWC

def helloword(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def home(request):
    return render_to_response(
           'index.html',RequestContext(request))
     
     
def capitais(request,cidade):
    contexto = {}
    cod_city = {'riodejaneiro-rj':'BRXX0201',
                'brasilia-df':'BRXX0043',
                'saopaulo-sp':'BRXX0232',
                'vitoria-es':'BRXX0259',
                'belohorizonte-mg':'BRXX0033'}
    
    name_city = {'riodejaneiro-rj':'Rio de Janeiro',
                'brasilia-df':'São Paulo',
                'saopaulo-sp':'Brasilia',
                'vitoria-es':'Vítoria',
                'belohorizonte-mg':'Belo Horizonte'} 
    
    
    contexto['presicao'] = getPrevisaoByWC(cod_city.get(cidade))
    contexto['cidade'] = name_city.get(cidade)    
    
    return render_to_response('capitais.html',
           contexto, RequestContext(request))
    