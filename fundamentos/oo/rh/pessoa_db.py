from storm.locals import *
from storm.exceptions import NotOneError, OperationalError
from cadastro_config import PARAM_CNX_BD

PESSOA_DDL = '''
    CREATE TABLE pessoa (
        id INTEGER PRIMARY KEY,
        nome VARCHAR
    )'''

def conectar(local):
    # local e' uma string com a sintaxe:
    # marca_banco://username:password@hostname:port/nome_database
    # onde marca_banco pode ser sqlite, postgres ou mysql
    database = create_database(local)
    cadastro = Store(database)
    return cadastro

def criar_tabela_pessoas(bd):
    res = bd.execute(PESSOA_DDL)
    bd.commit()
    return res

####################################### modelo

class Pessoa(object):
    __storm_table__ = 'pessoa'
    id = Int(primary=True)
    nome = Unicode()

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return '<Pessoa "%s" id=%s>' % (self.nome, self.id)

####################################### testes

def testar_modelo(cad):
    nome = 'Beatriz Nunez'
    bia = Pessoa(nome.decode('cp1252'))
    print bia
    cad.add(bia)
    print bia
    ze = Pessoa(u'Ze das Couve')
    cad.add(ze)
    print ze
    cad.commit()
    print 'COMMIT'
    print ze
    res = cad.find(Pessoa, Pessoa.nome == u'Beatriz Nunez')
    try:
        pessoa = res.one()
        print 'A pessoa eh a Bia?'
        print pessoa is bia
    except NotOneError:
        print 'AVISO: mais de uma Beatriz Nunez no banco!!!'
        lixo = list(res)
    res = cad.find(Pessoa)
    print 'TODO MUNDO:'
    for p in res:
        print p
    
def testar_criar(cad):
    try:
        res = criar_tabela_pessoas(cad)
    except OperationalError:
        print 'AVISO: usando tabela existente'
    else:
        print 'AVISO: criando nova tabela'


if __name__=='__main__':
    cad = conectar(PARAM_CNX_BD)

    try:
        testar_criar(cad)
        testar_modelo(cad)
    finally:
        cad.close()
    
    

