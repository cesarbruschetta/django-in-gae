# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def helloword(request):
    return render_to_response(
           'hello.html',RequestContext(request))


