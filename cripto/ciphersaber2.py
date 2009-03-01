#!/usr/bin/env python
# coding: utf-8

from os import urandom
from optparse import OptionParser

from rc4 import rc4

def cifrar(chave, entrada, loops=20):
    vetor_inicial = urandom(10)
    chave = chave + vetor_inicial
    return vetor_inicial + rc4(chave, entrada, loops)

def decifrar(chave, entrada, loops=20):
    chave = chave + entrada[:10]
    entrada = entrada[10:]
    return rc4(chave, entrada, loops)

def _teste():
    # fonte: http://ciphersaber.gurus.com/faq.html#cs2    
    claro = 'This is a test of CipherSaber-2.'
    cifrado = '''ba 9a b4 cf fb 77 00 e6 18 e3 82 e8 fc c5 ab 98
                 13 b1 ab c4 36 ba 7d 5c de a1 a3 1f b7 2f b5 76
                 3c 44 cf c2 ac 77 af ee 19 ad'''
    cifrado = ''.join([chr(int(s,16)) for s in cifrado.split()])
    chave = 'asdfg'
    assert decifrar(chave, cifrado, 10) == claro
    cifrado2 = cifrar(chave, claro, 10)
    assert cifrado != cifrado2
    assert decifrar(chave, cifrado2 , 10) == claro
    print 'OK'
    
def ciphersaber(op_cifrar, loops, chave, nome_arq_ent, nome_arq_sai):
    operacao = (decifrar, cifrar)[op_cifrar]
    entrada = file(nome_arq_ent, 'rb').read()
    saida = file(nome_arq_sai, 'wb')
    saida.write(operacao(chave, entrada, loops))
    saida.close()

def main():
    uso = 'Modo de usar: %prog [options] chave origem destino'
    parser = OptionParser(uso)
    parser.add_option("-c", "--cifrar", 
                        action='store_true', 
                        default=True,
                        help="cifrar arquivo")
    parser.add_option("-d", "--decifrar", 
                        action='store_false', 
                        dest='cifrar',
                        help="decifrar arquivo")
    parser.add_option("-l", "--loops", 
                        type="int", 
                        default=20,
                        help="num. de loops para inicializar vetor de estado")
    parser.add_option("-t", "--teste", 
                        action='store_true', 
                        default=False,
                        help="executar auto-teste")
    parser.add_option("-v", "--verboso", 
                        action="store_true")
    opcoes, args = parser.parse_args()
    if opcoes.teste:
        if opcoes.verboso:
            print 'Autoteste:',
        _teste()
    elif len(args) == 3:
        if opcoes.loops < 1:
            parser.error('--loops deve ser um inteiro >= 1')
        else:
            if opcoes.verboso:
                operacao = ('decifrar','cifrar')[opcoes.cifrar]
                print '%s (loops=%d): %s -> %s' % (
                                operacao, opcoes.loops, args[1], args[2])  
            ciphersaber(opcoes.cifrar, opcoes.loops, *args)
    else:
        parser.error("obrigatorio fornecer 3 argumentos:\n"
                     "    chave origem destino")

if __name__=='__main__':
    main()
