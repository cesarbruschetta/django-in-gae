# -*- coding: utf-8 -*-

from unicodedata import normalize

def remover_acentos(txt, codif='utf-8'):

    ''' Devolve cópia de uma str substituindo os caracteres 
        acentuados pelos seus equivalentes não acentuados.
    
    ATENÇÃO: carateres gráficos não ASCII e não alfa-numéricos,
    tais como bullets, travessões, aspas assimétricas, etc. 
    são simplesmente removidos!
    
    >>> remover_acentos('[ACENTUAÇÃO] ç: áàãâä! éèêë? íì&#297;îï, óòõôö; úù&#361;ûü.')
    '[ACENTUACAO] c: aaaaa! eeee? iiiii, ooooo; uuuuu.'
    
    '''
    if type(txt) == unicode:
        return normalize('NFKD', txt).encode('ASCII','ignore')
    else:
        return normalize('NFKD', txt.decode(codif)).encode('ASCII','ignore')
    

def parserDadosTempo(dados={}):
    """
        Retorna os dados da previsão do tempo em um formato ja
        esperado pela templete previsao.html
    """
    
    data = {}
    if dados:
        weatherdata = dados.get('weatherdata')
        previsao = weatherdata.get('weather')
        data['cidade'] = previsao.get('weatherlocationname','')
        data['url'] = previsao.get('imagerelativeurl','')
        
        data['agora'] = previsao.get('current',{})
        data['tempo'] =  previsao.get('forecast',[])
        
    return data