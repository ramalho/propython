# -*- coding: utf-8 -*-

class Livro(object):
    def __init__(self, paginas):
        self.paginas=paginas
    def getPaginas(self): 
        return self.__paginas
    def setPaginas(self, num): 
        if num <= 0:
            raise ValueError, 'o número de páginas deve ser maior que zero'
        self.__paginas = num
    def delPaginas(self): 
        del self.__paginas
    paginas = property(getPaginas, setPaginas, delPaginas, 'Número de páginas')
    
l = Livro(99)
print l.paginas
print Livro.paginas.__doc__
l.paginas = 10
print l.paginas
l.paginas = 0
