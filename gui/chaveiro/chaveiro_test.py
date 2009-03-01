#!/usr/bin/env python
# coding: utf-8

import unittest
from os import urandom, path, remove
from string import letters

from chaveiro import Chaveiro, cifrar, decifrar, SenhaIncorreta, ArquivoCorrompido
    
class TestesCifrarDecifrar(unittest.TestCase):
    
    def setUp(self):
        self.byte = 'A'
        self.bytes100 = (letters * 4)[:100]
        self.bytes10000 = urandom(10000)
        self.senha = 'asdfghij'

    def test_cifrar_vetor(self):
        ''' verificar que o vetor de inicialização de 10 bytes é incluído 
            no arquivo cifrado '''
        self.assertEqual(10, len(cifrar(self.senha, self.byte))-len(self.byte))
        self.assertEqual(10, len(cifrar(self.senha, self.bytes100))-len(self.bytes100))
        self.assertEqual(10, len(cifrar(self.senha, self.bytes10000))-len(self.bytes10000))

    def test_cifrado_diferente(self):
        ''' verificar se os dados cifrados ficam diferentes do originais,
            ignorando o vetor de inicialização (é o mínimo que se espera!)'''
        cifrado = cifrar(self.senha, self.byte)[10:]
        self.assertEqual(len(self.byte), len(cifrado))
        self.assertNotEqual(self.byte, cifrado)
        cifrado = cifrar(self.senha, self.bytes100)[10:]
        self.assertEqual(len(self.bytes100), len(cifrado))
        self.assertNotEqual(self.bytes100, cifrado)
        cifrado = cifrar(self.senha, self.bytes10000)[10:]
        self.assertEqual(len(self.bytes10000), len(cifrado))
        self.assertNotEqual(self.bytes10000, cifrado)

    def test_cifrar_cifrar(self):
        ''' verificar se os bytes cifrados e decifrados são iguais aos originais '''
        self.assertEqual(self.byte, decifrar(self.senha, cifrar(self.senha, self.byte)))
        self.assertEqual(self.bytes100, decifrar(self.senha, cifrar(self.senha, self.bytes100)))
        self.assertEqual(self.bytes10000, decifrar(self.senha, cifrar(self.senha, self.bytes10000)))
        
class TestesChaveiroIteravel(unittest.TestCase):

    def setUp(self):
        self.chaveiro0 = Chaveiro('000')
        self.itens9 = [str(i) for i in range(1,10)]
        self.chaveiro9 = Chaveiro('999')
        [self.chaveiro9.incluir(i) for i in self.itens9]

    def test_iter(self):
        self.assertEqual([], [x for x in self.chaveiro0])
        self.assertEqual(self.itens9, [x for x in self.chaveiro9])
        
    def test_incluir_excluir(self):
        self.chaveiro0.incluir('zzz')
        self.assertEqual(1, len([x for x in self.chaveiro0]))
        self.chaveiro0.excluir(0)
        self.assertEqual(0, len([x for x in self.chaveiro0]))

    def test_incluir_excluir_posicao(self):
        self.chaveiro9.incluir('1234',3)
        itens = [i for i in self.chaveiro9]
        self.assertEqual('1234', itens[3])
        self.chaveiro9.excluir(3)
        self.assertEqual(self.itens9, [i for i in self.chaveiro9])
        self.chaveiro9.excluir(0)
        itens = [i for i in self.chaveiro9]
        self.assertEqual('2', itens[0])
        
class TestesCarregar(unittest.TestCase):
    def setUp(self):
        self.chaveiro0 = Chaveiro('000')
        self.chaves = [
            ('Wikipedia', 'http://pt.wikipedia.org', 'ramalho', 'senha-nao'),
            ('Incubadora Virtual', 'http://incubadora.fapesp.br', 'luciano', 'senha-nem'),
            ('PythonBrasil', 'http://www.pythonbrasil.com.br', 'luciano', 'senha-outra'),
        ]
        self.itens9 = [str(i) for i in range(1,10)]
        self.chaveiro9 = Chaveiro('999')
        [self.chaveiro9.incluir(i) for i in self.itens9]
    
    def test_carregar_adicionando(self):
        self.chaveiro9.carregar(self.chaves, sobrescrever=False)
        self.assertEqual(9+len(self.chaves), len(self.chaveiro9))
        for original, copia in zip(self.itens9+self.chaves, self.chaveiro9):
            self.assertEqual(original, copia)

    def test_carregar_sobrescrevendo(self):
        self.chaveiro9.carregar(self.chaves, sobrescrever=True)
        self.assertEqual(len(self.chaves), len(self.chaveiro9))
        for original, copia in zip(self.chaves, self.chaveiro9):
            self.assertEqual(original, copia)

class TestesChaveiroGravarLer(unittest.TestCase):
    
    def setUp(self):
        self.chaveiro0 = Chaveiro('000', nome_arq='chaveiro0.dat')
        self.itens9 = [str(i) for i in range(1,10)]
        self.chaveiro9 = Chaveiro('999', nome_arq='chaveiro9.dat')
        [self.chaveiro9.incluir(i) for i in self.itens9]

    def test_gravar(self):
        self.chaveiro0.gravar()
        self.assert_(path.exists(self.chaveiro0.nome_arq))
        self.chaveiro9.gravar()
        self.assert_(path.exists(self.chaveiro9.nome_arq))
        
    def test_ler(self):
        self.chaveiro0.gravar()
        self.chaveiro_lido = Chaveiro('000', nome_arq='chaveiro0.dat')
        self.chaveiro_lido.ler()
        self.assertEqual([], [x for x in self.chaveiro_lido])
        self.chaveiro9.gravar()
        self.chaveiro_lido = Chaveiro('999', nome_arq='chaveiro9.dat')
        self.chaveiro_lido.ler()
        self.assertEqual(self.itens9, [x for x in self.chaveiro_lido])
        
    def test_senha_incorreta(self):
        self.chaveiro0.gravar()
        chaveiro_lido = Chaveiro(senha='', nome_arq='chaveiro0.dat')
        self.assertRaises(SenhaIncorreta, chaveiro_lido.ler)
        self.chaveiro9.gravar()
        chaveiro_lido = Chaveiro(senha='ERRADA', nome_arq='chaveiro9.dat')
        self.assertRaises(SenhaIncorreta, chaveiro_lido.ler)
        
    def test_detectar_arquivo_corrompido(self):
        self.chaveiro0.gravar()
        arq = file('chaveiro0.dat', 'ab')
        arq.write('x')
        arq.close()
        chaveiro_lido = Chaveiro('000', nome_arq='chaveiro0.dat')
        self.assertRaises(ArquivoCorrompido,chaveiro_lido.ler)
                
    def tearDown(self):
        for nome_arq in 'chaveiro0.dat chaveiro9.dat'.split():
            if path.exists(nome_arq):
                remove(nome_arq)


if __name__ == '__main__':
    unittest.main()