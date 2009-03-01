from datetime import date
from pessoa import Pessoa

class Empresa(object):
    nome = ''
    funcionarios = []
    def __init__(self, nome):
        self.nome = nome

    def contratar(self, pessoa):
        f = Funcionario(pessoa.nome, self)
        self.funcionarios.append(f)
        return f
    
class Funcionario(Pessoa):
    empresa = None

    def __init__(self, nome, empresa):
        self.nome = nome
        self.empresa = empresa

    def __str__(self):
        try:
            mes, dia = self.aniversario()
            return '%s (%s/%s)' % (self.nome,dia,mes)
        except AttributeError:
            return self.nome

    def __repr__(self):
        return self.__str__()
                               

bsgi = Empresa('BSGI')
joca = Pessoa('Jose Neves Jr.')
joca.data_nasc = date(1978,2,25)
print joca
print joca.aniversario()
lara = Pessoa('Lara Ramalho')
f_lara = bsgi.contratar(lara)
print f_lara
bsgi.contratar(joca)
print bsgi.funcionarios

