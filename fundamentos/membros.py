#!/usr/bin/env python

# KISS - keep it simple, stupid

from os.path import exists, split
from os import mkdir
from storm.locals import *
from storm.exceptions import OperationalError
from config import CONFIG_DB

def criar_tabela_membros(db):
    db.execute('''
        CREATE TABLE membros (
            COD INT PRIMARY KEY,
            nome VARCHAR (40)
        )        
    ''')
    db.commit()

def conectar (local):
    banco, caminho = local.split(':')
    diretorio, arquivo = split(caminho)
    if not exists(diretorio):
        mkdir(diretorio)
        print 'AVISO: criando diretorio de dados', diretorio
    base = create_database(local)
    cadastro = Store(base)
    return cadastro

def criar_database(cadastro):
    try:
        criar_tabela_membros(cadastro)
    except OperationalError:
        pass
    else:
        print 'AVISO: criando nova tabela'       

class Membro(object):
    __storm_table__ = 'membros'
    cod = Int(primary=True)
    nome = Unicode()
    
    def __init__(self, nome):
        self.nome = nome
        
    def __repr__(self):
        return '<Membro "%s" cod=%s>' % (self.nome, self.cod)
        
def listar_membros(cadastro):
    return cadastro.find(Membro)
        
############################################### testes

def testar_listar_membros(cadastro):
    nomes = ['Fulano de Tal', 'Sicrano de Tal', 'Beltrano de Tal']
    for nome in nomes:
        membro = Membro(nome.decode('cp1252'))
        print membro
        cadastro.add(membro)
    cadastro.commit()
    import pdb; pdb.set_trace()
    for i, membro in enumerate(cadastro.find(Membro)):
        print i+1, membro
        
if __name__=='__main__':
    try:
        cadastro = conectar(CONFIG_DB)
        criar_database(cadastro)
        testar_listar_membros(cadastro)
    finally:
        cadastro.close()      
    
    
    