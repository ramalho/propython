
def tag(nome,cont='',**atribs):
    ''' gera tag XML no formato:
        <nome atrib1="valor1">cont</nome>
    '''
    listaAtribs = []
    for atrib, valor in atribs.items():
        valor = valor.replace('"',"'")
        listaAtribs.append('%s="%s"' % (atrib, valor))
    if listaAtribs:
        atribs = ' '.join(listaAtribs)
        return '<%s %s>%s</%s>' % (nome,
           atribs, cont, nome)
    return '<%s>%s</%s>' % (nome, cont, nome)

print tag('autor')
print tag('autor','Machado de Assis', cpf='1234567890')
print tag('autor','Machado de Assis', apelido='"Tatu"')   