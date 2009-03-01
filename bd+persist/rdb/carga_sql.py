#!/usr/bin/env python2.5

from sqlite3 import connect, apilevel
from pprint import pprint
from carga import ler_arq_delim_tabs

def criar_tabela(db):
    c = db.cursor()
    c.execute('''
        create table livros (
            isbn text,
            num_pags int,
            titulo text,
            autores text
        )'''
    )
    db.commit()
    c.close()

def testar_insert(db):
    c = db.cursor()

    c.execute('''
        insert into livros (isbn, num_pags, titulo, autores)
        values ('9788577800131',568,'Aprendendo Python','Mark Lutz|David Ascher')
    ''')

    c.execute('''select * from livros''')
    pprint(c.description)

    for reg in c:
        pprint(reg)

    db.commit()
    c.execute('''delete from livros where isbn='9788577800131' ''')

    db.commit()
    c.close()

def inserir_livros(db, lista):
    c = db.cursor()
    for livro in lista:
        valores = (livro['isbn'],livro['pags'],
                   livro['titulo'],livro['autores'])
        c.execute('''
                insert into livros (isbn, num_pags, titulo, autores)
                values (?,?,?,?)
            ''', valores)
    db.commit()
    c.close()

def contar_livros(db):
    c = db.cursor()
    c.execute('select count(*) from livros')
    pprint(c.fetchone())
    c.close()

db = connect('livros.db')

criar_tabela(db)
#testar_insert(db)

#inserir_livros(db, ler_arq_delim_tabs('temporeal_dump.txt',234))
#contar_livros(db)

db.close()





