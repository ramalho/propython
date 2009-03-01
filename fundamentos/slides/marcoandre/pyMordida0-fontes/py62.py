#!/usr/bin/env python
#-*- coding:utf-8 -*-

def tag(nome, *linhas, **atributos):
    saida = ['<' + nome]
    for par in atributos.items():
        saida.append(' %s="%s"' % par)
    if linhas:
        saida.append('>')
        if len(linhas) == 1: 
            saida.append(linhas[0])
        else:
            saida.append('\n')
            for linha in linhas:
                saida.append('\t%s\n' % linha)
        saida.append('</%s>' % nome)
    else:
        saida.append(' />')
    return ''.join(saida)

print tag('br')
print tag('img',src='foto.jpg',width=3,height=4)
print tag('a','Wikipédia',
    href='http://wikipedia.org')
print tag('p','Eu não devia te dizer',
    'mas essa lua','mas esse conhaque',
    'botam a gente comovido como o diabo.',
    id='poesia')
