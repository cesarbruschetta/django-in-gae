# -*- coding: utf-8 -*-
from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(
                label='Digite o nome da cidade',
                widget=forms.TextInput(attrs={'size':32})
                )
    
    cidades = forms.ChoiceField(
                label='Selecione uma cidade, apos o filtro do campo superior',
                choices = (('0','Selecione'),),                               
                )
    
    
                 