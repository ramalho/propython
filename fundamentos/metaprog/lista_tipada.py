# coding: utf-8

'''

Um exemplo inspirado pela pergunta "Python tem polimorfismo parametrizado?"

    >>> l = ListaLimitada(str)
    >>> l.append('bla')
    >>> len(l)
    1
    >>> l[0]
    'bla'
    >>> l[0] = 'bli'
    >>> l[0]    
    'bli'
    >>> l[0] = 2
    Traceback (most recent call last):
       ...
    TypeError: Esta lista aceita apenas tipo <str>
    >>> l.append('blu')
    >>> len(l)
    2
    >>> l.append(3.1592)
    Traceback (most recent call last):
       ...
    TypeError: Esta lista aceita apenas tipo <str>
    

'''

class ListaLimitada(list):
    def __init__(self, tipo, *args, **kwargs):
        super(ListaLimitada,self).__init__(*args, **kwargs)
        self.tipo = tipo
        
    def __checa_tipo(self, item):
        # import pdb; pdb.set_trace()
        if isinstance(item, self.tipo):
            nome_tipo = self.tipo.__name__
            raise TypeError('Esta lista aceita apenas tipo <%s>'% nome_tipo)        
    
    def __setitem__(self, pos, item):
        self.__checa_tipo(item)
        super(ListaLimitada,self).__setitem__(pos, item)

    def append(self, item):
        self.__checa_tipo(item)
        super(ListaLimitada,self).append(item)


            
if __name__=='__main__':
    import doctest
    print doctest.testmod()
