# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from django_in_gae.app.webserve import getPrevisaoByWC, getGeoIPbyIP, getCodigoCidadeWC
from django_in_gae.app.forms import SearchForm
from utils import  remover_acentos, parserDadosTempo

def helloword(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def home(request):
    contexto = {}
    WC_cod = 'BRXX0217'
    # Produção
    client_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
    # Desenvolvimento
    #client_address = '189.54.5.124'
    #client_address = '67.23.238.98'
    #client_address = '187.75.167.198'
    #client_address = '178.33.147.177'
    
    info_geo = getGeoIPbyIP(client_address)
    text = '%s %s' %(info_geo.get('city',''), info_geo.get('country_code',''))
    
    busca_cod = getCodigoCidadeWC(remover_acentos(text))

    if busca_cod:
        WC_cod = busca_cod[0].get('id','0')
    
    data = parserDadosTempo(getPrevisaoByWC(WC_cod))
    contexto['previsao'] = data
    contexto['cidade'] = data.get('cidade','') #busca_cod[0].get('text','')   #'%s, %s' %(info_geo.get('city'),info_geo.get('country_name'))    
    
    return render_to_response('index.html',
           contexto, RequestContext(request))
     
def capitais(request,cidade):
    contexto = {}
    cod_city = {'riodejaneiro-rj':'BRXX0201',
                'brasilia-df':'BRXX0043',
                'saopaulo-sp':'BRXX0232',
                'vitoria-es':'BRXX0259',
                'belohorizonte-mg':'BRXX0033'}
    
    name_city = {'riodejaneiro-rj':'Rio de Janeiro',
                'brasilia-df':'Brasilia',
                'saopaulo-sp':'São Paulo',
                'vitoria-es':'Vítoria',
                'belohorizonte-mg':'Belo Horizonte'} 
    
    contexto['previsao'] = parserDadosTempo(getPrevisaoByWC(cod_city.get(cidade)))
    contexto['cidade'] = name_city.get(cidade)    
    
    return render_to_response('capitais.html',
           contexto, RequestContext(request))

def search(request):   
    contexto = {}
    
    if request.method == 'POST':
        form = SearchForm(request.POST)
        
        #if form.is_valid():
        busca = form.data.get('query','')
        city = form.data.get('cidades','0')
        
        busca_cod = getCodigoCidadeWC(remover_acentos(busca))
        if len(busca_cod) > 1 and city == '0' :
            from_cid =  form.fields['cidades']
            from_cid.choices = [('0','Selecione')]
             
            for item in busca_cod:
                from_cid.choices.append(tuple([item.get('id','0'),item.get('text','')]))
            
        elif len(busca_cod) == 1:
            code_city = busca_cod[0].get('id','0')
            data = parserDadosTempo(getPrevisaoByWC(code_city))
            contexto['previsao'] = data
            contexto['results'] = True
            contexto['cidade'] = data.get('cidade','')
        
        else:
            data = parserDadosTempo(getPrevisaoByWC(city))
            contexto['previsao'] = data
            contexto['results'] = True 
            contexto['cidade'] = data.get('cidade','')
        
        contexto['form'] = form
    else:
        contexto['form'] = SearchForm()
    
    return render_to_response('search.html',
           contexto, RequestContext(request))
     
