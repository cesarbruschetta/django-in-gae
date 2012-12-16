# -*- coding: utf-8 -*-
from django import template
from django.utils.html import strip_tags

register = template.Library()

@register.filter
def convertDate(data):
    valor = data.split('-')
    try:
        return '%s/%s/%s' %(valor[2],valor[1],valor[0])
    except:
        return '00/00/0000'

@register.filter
def limitTextSize(html, size):
    text = strip_tags(html)
    if len(text) > size:
        i = size
        while (text[i] != " ") and (text[i] < len(text)):
            i += 1              
        return text[:i]+'...'
    else:
        return text  
    
@register.filter
def hash(h, key):
    return h[key]    
    
