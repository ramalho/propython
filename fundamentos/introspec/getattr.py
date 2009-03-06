# coding: utf-8

'''
-----------------------------------------
Exemplos de atributo dinâmico
-----------------------------------------

    >>> j = Aluno('Juca', 7)
    >>> j
    <Juca (7)>
    >>> print j
    Juca (7)
    >>> j.nick
    'Ju'
    
'''

def apelido(nome):
    u'''
    Devolve um apelido gerado a partir do nome::
    
        >>> apelido('josias')
        'jo'
        >>> apelido('ng')
        'ngu'
        >>> apelido('jo')
        'jojo'
    
    '''
    for i, letra in enumerate(nome):
        if letra.lower() in 'aeiou':
            apelido = nome[:i+1]
            break
    else:
        return nome+'u'
    if apelido == nome:
        return apelido*2
    return apelido


class Aluno(object):
    nome = ''
    idade = 0
    
    def __init__(self, nome=None, idade=None):
        self.nome = nome or self.nome
        self.idade = idade or self.idade
        
    def nome_idade(self):
        return '%s (%s)' % (self.nome, self.idade)
        
    __str__ = nome_idade
    
    def __repr__(self):
        return '<%s>' % self.nome_idade()

    def __getattr__(self, atrib):
        if atrib == 'nick':
            return apelido(self.nome)
        else:
            raise AttributeError()
        
    
if __name__=='__main__':
    import doctest
    print doctest.testmod()
 