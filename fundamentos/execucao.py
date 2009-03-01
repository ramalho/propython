import sys
import atexit

print '-> 1 inicio'

def funcaoA():
    print '-> 6 funcao A'
    return 'resultado A'

def funcaoB():
    print '-> 8 funcao B'

    def funcaoC():
        print '-> 11 funcao C'
        
    return funcaoC
    
funcaoD = lambda:sys.stdout.write('-> 12 funcao D\n')

def funcaoE():
    print '-> 13 funcao E'
    print 'FIM'
        
class Classe(object):
    print '-> 2 bloco de declaracoes da Classe'
    
    def __init__(self):
        print '-> 9 inicializacao da instancia da Classe'
        
    def metodo(self):
        print '-> 10 metodo da instancia da Classe'
        return 'resultado metodo'
        
if True:
    print '-> 3 condicional True'
    
if False:
    assert False, 'Isso nunca devia acontecer'

atexit.register(funcaoE)

print '-> 4 logo antes do if __main__'

if __name__=='__main__':
    print '-> 5 __main__'
    print funcaoA
    print funcaoA()
    print '-> 7 __main__ (cont.)'
    print funcaoB
    resultadoB = funcaoB()
    print resultadoB
    objeto = Classe()
    objeto.metodo()
    resultadoB()
    print funcaoD
    funcaoD()
    


