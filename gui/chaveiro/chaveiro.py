#!/usr/bin/env python
# coding: utf-8

import pickle
import zlib
from os import urandom, rename, remove

try: # importar SHA-1 segundo a versao do Python
    from hashlib import sha1 # Python 2.5.x
except ImportError:
    from sha import new as sha1 # Python 2.4.x

from rc4 import rc4

NOME_ARQ_PADRAO = 'chaveiro.dat'
FORMATO_PICKLE = 2

def cifrar(senha, bytes):
    ''' Cifrar bytes usando algoritmo RC4 como no Ciphersaber 2
    
    O Ciphersaber 2 usa um vetor inicial de 10 bytes aleatórios concatenado 
    à senha do usuário, e 20 iterações no laço de inicialização do RC4.
    
    fonte: http://ciphersaber.gurus.com/faq.html#cs2
    '''
    vetor_inicial = urandom(10)
    senha = senha + vetor_inicial
    return vetor_inicial + rc4(senha, bytes, 20)

def decifrar(senha, bytes):
    ''' Decifrar bytes usando algoritmo RC4 como no Ciphersaber 2 '''
    senha = senha + bytes[:10]
    bytes = bytes[10:]
    return rc4(senha, bytes, 20)
    
class SenhaIncorreta(StandardError):
    "Senha-mestre incorreta."    

class ArquivoCorrompido(StandardError):
    "Arquivo de dados corrompido."    
        
class Chaveiro(object):
    ''' Gerencia uma lista de chaves
    
    A lista de chaves pode ser gravada ou lida num arquivo cifrado em RC4.
    
    Para maior segurança contra falhas, ao gravar os dados cifrados, o programa
    salva os dados em um arquivo .NEW, renomeia o arquivo atual para .BKP e só
    então retira o sufixo .NEW e apaga o arquivo .BKP. O arquivo gravado inclui
    um hash SHA-1 que permite verificar sua integridade na leitura.
    '''
    
    def __init__(self, senha, nome_arq=NOME_ARQ_PADRAO):
        self.senha = senha
        self.nome_arq = nome_arq
        self.chaves = []
        
    def __iter__(self):
        for chave in self.chaves:
            yield chave
            
    def __len__(self):
        return len(self.chaves)
            
    def incluir(self, chave, posicao=None):
        if posicao is None:
            self.chaves.append(chave)
        else:
            self.chaves.insert(posicao, chave)
        
    def excluir(self, posicao):
        del self.chaves[posicao]
        
    def carregar(self, chaves, sobrescrever=True):
        if sobrescrever:
            self.chaves = chaves
        else:
            self.chaves.extend(chaves)
        
    def gravar(self):
        arq = file(self.nome_arq+'.NEW','wb')
        bytes = pickle.dumps(self.chaves, FORMATO_PICKLE)
        bytes = zlib.compress(bytes)
        bytes = cifrar(self.senha, bytes)
        assinatura = sha1(bytes).digest()
        arq.write(assinatura)
        arq.write(bytes)
        arq.close()
        try:
            rename(self.nome_arq, self.nome_arq+'.BKP')
        except OSError, erro:
            if 'No such file or directory' in str(erro):
                apagar_backup = False
            else:    
                raise erro
        else:
            apagar_backup = True
        rename(self.nome_arq+'.NEW', self.nome_arq)
        if apagar_backup:
            remove(self.nome_arq+'.BKP')

    def ler(self):
        arq = file(self.nome_arq,'rb')
        verificador = sha1()
        assinatura = arq.read(verificador.digest_size)
        bytes = arq.read()
        arq.close()
        verificador.update(bytes)
        if assinatura != verificador.digest():
            raise ArquivoCorrompido()
        bytes = decifrar(self.senha, bytes)
        try:
            bytes = zlib.decompress(bytes)
        except zlib.error, erro:
            raise SenhaIncorreta()
        else:
            self.chaves = pickle.loads(bytes)
            