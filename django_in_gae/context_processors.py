# -*- encoding: utf-8 -*-
from django.conf import settings



def context(request):
    Menu = [{'id':'riodejaneiro-rj',
             'name':"Rio de Janeiro"},
             {'id':'saopaulo-sp',
              'name':'São Paulo'},
             {'id':'brasilia-df',
              'name':'Brasilia'},
             {'id':'vitoria-es',
              'name':'Vítoria'},
              {'id':'belohorizonte-mg',
               'name':'Belo Horizonte'}
            ]
    

    contexto = {
        'current_absolute_url': request.build_absolute_uri(),
        'static_absolute_url': request.build_absolute_uri(settings.MEDIA_URL),
        'current_path':request.path,
        'Menu':Menu
    }

    return contexto