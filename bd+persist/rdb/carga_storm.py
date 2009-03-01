#!/usr/bin/env python2.5

from pprint import pprint
from storm.locals import *

from carga import ler_arq_delim_tabs

class Livro(object):
    __storm_table__ = 'livros'
    id = Int(primary=True)
    isbn = Chars()
    qt_pgs = Int()
    titulo = Unicode()
    autores = Unicode()
    
def criar_db():
    database = create_database('sqlite:biblioteca.db')
    biblioteca = Store(database)
    biblioteca.execute('''
        create table livros (
            id integer primary key,
            isbn text,
            qt_pgs int,
            titulo text,
            autores text
        )'''
    )
    return biblioteca

def inserir_livro(biblioteca, **dic):
    livro = Livro()
    livro.isbn = dic['isbn']
    livro.titulo = dic['titulo']
    livro.autores = dic['autores']
    livro.qt_pgs = dic['pags']
    biblioteca.add(livro)
    return livro
    
bib = criar_db()
liv = inserir_livro(bib,
                    isbn='9788577800131',
                    pags=568,
                    titulo=u'Aprendendo Python',
                    autores=u'Mark Lutz|David Ascher')

print liv.id, liv.titulo
bib.flush()
print liv.id, liv.titulo
res = bib.find(Livro, Livro.isbn == '9788577800131')
print res
liv2 = res.one()
print liv2.id, liv2.titulo
res = bib.find(Livro, Livro.isbn == '1111111111111')
liv3 = res.one()
print repr(liv3)
                


    