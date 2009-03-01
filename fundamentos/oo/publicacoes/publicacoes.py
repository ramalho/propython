# coding: utf-8

class Publicacao(object):
    titulo = ''
    ano = ''
    criadores = None
    
    def __init__(self, titulo, criadores=None, ano=''):
        self.titulo = titulo
        self.criadores = criadores
        self.ano = ano
        
    def elencar_criadores(self):
        if self.criadores:
            if len(self.criadores) == 1:
                return self.criadores[0]
            else:
                criadores = ', '.join(self.criadores[:-1])
                return criadores + ' e ' + self.criadores[-1]
        else:
            return ''

    def ficha(self):
        if self.ano:
            ano = ' (%s)' % self.ano
        else:
            ano = ''
        if self.criadores:
            return self.titulo + ano + '\n  por ' + self.elencar_criadores()
        else:
            return self.titulo + ano
            
    def __str__(self):
        return (self.titulo + ' ' + self.ano).strip()
        
class Livro(Publicacao):
    num_paginas = 0
    isbn = ''
    
    def __init__(self, titulo, criadores=None, isbn='', ano='', 
            num_paginas=0):
        super(Livro, self).__init__(titulo, criadores, ano)

        
def testar():
    import doctest
    doctest.testfile('teste_publicacoes.txt')
    
if __name__ == '__main__':
    testar()