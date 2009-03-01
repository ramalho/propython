def exibir(texto, estilo=None, cor='black'):
    atribs = ' style="color: %s;"' % cor
    if estilo:
        atribs = atribs + ' class="%s"' % estilo
    return '<p%s>%s</p>' % (atribs, texto)

def testes_exibir():
    print exibir('BSGI')
    print exibir('BSGI','manchete')
    print exibir('BSGI','destaque','red')
    print exibir('BSGI',cor='blue')
    print exibir(cor='blue',estilo='destaque',texto='BSGI')

def listar(*lista, **atribs):
    if not lista: return ''
    if atribs:
        tag = '<ol'
        for chave, valor in atribs.items():
            if chave=='class_': chave = 'class'
            tag += ' %s="%s"' % (chave, valor)
        tag += '>'
    else:
        tag = '<ol>'
    saida = [tag]
    for item in lista:
        saida.append('<li>%s</li>' % item)
    saida.append('</ol>')
    return '\n'.join(saida)

def testes_listar():
    print listar('abacaxi','banana')
    print listar()
    print listar('aaa','bbb','ccc',class_='destaque',id='listagem')
testes_listar()
