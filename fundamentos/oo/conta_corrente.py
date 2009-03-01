#!/usr/bin/env python
# coding: utf-8

class ContaV1(object):
    '''
    Uma classe de conta corrente para demonstrar uma propriedade
    apenas para leitura (read-only).

        >>> c1 = ContaV1()
        >>> c1.depositar(1000)
        >>> c1.saldo
        1000
        >>> c1.saldo = 9999999
        Traceback (most recent call last):
          ...
        AttributeError: can't set attribute
        >>> c1.saldo
        1000
        >>> c1.sacar(300)
        >>> c1.saldo
        700
        >>> c1.sacar(2000)
        Traceback (most recent call last):
          ...
        ValueError: saque excede o limite
        >>> c1.saldo
        700
        
    '''
    limite = -1000
    __saldo = 0
    def sacar(self, quantia):
        assert quantia > 0
        if (self.__saldo - quantia) >= self.limite:
            self.__saldo -= quantia
        else:
            raise ValueError('saque excede o limite')
    def depositar(self, quantia):
        self.__saldo += quantia
    @property
    def saldo(self):
        return self.__saldo

class ContaV2(object):
    '''
    Uma classe de conta corrente para demonstrar uma propriedade
    que pode receber uma atribuição inicial e depois se torna
    apenas para leitura (read-only).
    
        >>> c2 = ContaV2()
        >>> c2.saldo = 5000
        >>> c2.saldo
        5000
        >>> c2.saldo = 9999999
        Traceback (most recent call last):
          ...
        AttributeError: uma vez inicializado, o saldo pode ser alterado apenas por saques e depositos
        >>> c2.saldo
        5000
        >>> c3 = ContaV2(-2000)
        Traceback (most recent call last):
          ...
        ValueError: saldo negativo excede o limite
        >>> c3 = ContaV2(3000)
        >>> c3.sacar(1000)
        >>> c3.saldo
        2000

    '''
    limite = -1000
    __saldo = None
    def __init__(self, saldo_inicial = None):
        if saldo_inicial is not None: self.setSaldo(saldo_inicial)
    def sacar(self, quantia):
        if quantia < 0:
            raise ValueError('valor do saque tem que ser positivo')
        if (self.__saldo - quantia) >= self.limite:
            self.__saldo -= quantia
        else:
            raise ValueError('saque excede o limite')
    def depositar(self, quantia):
        self.__saldo += quantia
    def getSaldo(self):
        return self.__saldo
    def setSaldo(self, valor):
        if self.__saldo is not None:
            raise AttributeError('uma vez inicializado, o saldo pode ser'
                ' alterado apenas por saques e depositos')
        else:
            if valor < self.limite:
                raise ValueError('saldo negativo excede o limite')
            self.__saldo = valor
                    
    saldo = property(getSaldo, setSaldo)
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
