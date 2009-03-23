# coding: utf-8

'''
-----------------------------------------
Exemplos de atributo dinâmico
-----------------------------------------

    >>> j = Aluno('Juca', 7)
    >>> j
    <Juca (7)>
    >>> j = Aluno('Maria', -1) # <-- esta atribuicao nao acontece
    Traceback (most recent call last):
      ...
    ValueError: A idade nao pode ser negativa.
    >>> j.idade = 8
    >>> j
    <Juca (8)>
    >>> j.idade = 5
    Traceback (most recent call last):
      ...
    ValueError: A idade nao pode ser diminuida.

    
'''

class Aluno(object):
    def __init__(self, nome, idade=0):
        self.nome = nome
        self.idade = idade
        
    def nome_idade(self):
        return '%s (%s)' % (self.nome, self.idade)
        
    __str__ = nome_idade
    
    def __repr__(self):
        return '<%s>' % self.nome_idade()

    def __setattr__(self, atrib, valor):
        if (atrib == 'idade') and (valor < 0):
            raise ValueError('A idade nao pode ser negativa.')
        elif hasattr(self, 'idade') and valor < self.idade:
            raise ValueError('A idade nao pode ser reduzida.')
        super(Aluno, self).__setattr__(atrib, valor)    

        
if __name__=='__main__':
    import doctest
    print doctest.testmod()
 