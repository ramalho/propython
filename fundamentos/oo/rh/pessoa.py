# coding: cp1252

from datetime import date

class Pessoa(object):
    nome = ''
    peso = None
    data_nasc = None

    def __init__(self, nome):
        self.nome = nome

    def aniversario(self):
        return self.data_nasc.month, self.data_nasc.day

    def idade(self):
        hoje = date.today()
        anos = hoje.year - self.data_nasc.year
        if (hoje.month, hoje.day) < self.aniversario():
            anos -= 1
        return anos

    def __str__(self):
        if self.data_nasc:
            return '%s, %s' % (self.nome, self.idade())
        else:
            return self.nome

    def __cmp__(self, outro):
        if self.data_nasc > outro.data_nasc:
            return -1
        elif self.data_nasc < outro.data_nasc:
            return 1
        else:
            return 0
        # a mesma coisa, em uma linha:
        # return cmp(self.data_nasc, outro.data_nasc)


if __name__=='__main__':
    
    juca = Pessoa('Jose Neves')
    print juca
    juca.data_nasc = date(1980,6,30)

    print juca.nome, juca.aniversario(), juca.idade()
    print juca

    bia = Pessoa('Beatriz Souza')
    bia.data_nasc = date(1990,12,20)
    print bia.nome, bia.aniversario(), bia.idade() 
    print bia

    print juca > bia

    
