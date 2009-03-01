# coding: utf-8

import locale
from operator import itemgetter

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

cidades = [
    {'uf':'SP','nome':u'Santos'}, 
    {'uf':'SP','nome':u'Sarutaiá'}, 
    {'uf':'SP','nome':u'São Paulo'},
    {'uf':'PE','nome':u'Terezinha'},
    {'uf':'TO','nome':u'Alvorada'},
]

print 'Ordenando os itens sem especificar a chave:'

indice = sorted(cidades)

for cidade in indice:
    print cidade['uf'], cidade['nome']
    
print '\nOrdenando os itens por UF:'
    
indice = sorted(cidades, key=itemgetter('uf'))

for cidade in indice:
    print cidade['uf'], cidade['nome']

print '\nOrdenando os itens por nome:'

indice = sorted(cidades, key=itemgetter('nome'))

for cidade in indice:
    print cidade['uf'], cidade['nome']

print '\nOrdenando os itens por nome com letras acentuadas no lugar certo:'

indice = sorted(cidades, key=itemgetter('nome'), cmp=locale.strcoll)

for cidade in indice:
    print cidade['uf'], cidade['nome']

indice = sorted(cidades, key=lambda x: x['uf']+' '+x['nome'], cmp=locale.strcoll)

print '\nOrdenando os itens por uf e nome:'

for cidade in indice:
    print cidade['uf'], cidade['nome']


