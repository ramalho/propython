#!/usr/bin/env python

'''
Exemplo da técnica de currying. 

A função rectFactory é um "curry" que retorna uma função que realiza o 
serviço de rect fixando um dos parâmetros para que ele não precise ser
fornecidos a cada invocação.

Em rectFactory2 temos um exemplo que demonstra a mesma técnica implementada
com o comando lambda.

Em rectFactory3 o curry fixa ambos argumentos da função rect.
'''

def rect(larg, alt):
    if larg > 0 and alt > 0:
        print '*' * larg
        if alt > 1:
            for i in range(alt-2):
                print '*' + ' '*(larg-2) + '*'
            print '*' * larg
    
def rectFactory(larg):
    def func(alt):
        return rect(larg, alt)
    return func
 
def rectFactory2(larg):
    return lambda alt: rect(larg, alt)

def rectFactory3(larg, alt):
    return lambda: rect(larg, alt)

if __name__=='__main__':
    f = rectFactory(20)
    f(7)
    g = rectFactory2(40)
    g(3)
    g(5)
    h = rectFactory3(30,3)
    h()
    h()
