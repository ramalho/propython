#!/usr/bin/env python2.5
# coding: utf-8 

from sqlite3 import connect, OperationalError
from pprint import pprint
from temporeal_carga import carga
from os.path import split, exists, isdir
import sys, os

CAMINHO_BD = 'dados/livros.bd'

def criar_tabela(bd):
    c = bd.cursor()
    sql = '''
        create table livros (
            isbn text primary key,
            num_pags int,
            titulo text,
            autores text )
    '''
    try:
        c.execute(sql)
    except OperationalError, erro:
        print erro
    else:
        bd.commit()
    c.close()

def testar_insert(bd):
    c = bd.cursor()

    c.execute('''
        insert into livros (isbn, num_pags, titulo, autores)
        values ('9788577800131',568,'Aprendendo Python','Mark Lutz|David Ascher')
    ''')

    c.execute('''select * from livros''')
    pprint(c.description)

    for reg in c:
        pprint(reg)

    bd.commit()
    c.execute('''delete from livros where isbn='9788577800131' ''')

    bd.commit()
    c.close()

def inserir_livros(bd, lista):
    c = bd.cursor()
    for livro in lista:
        for campo in ['titulo','autores']:
            livro[campo] = livro[campo].decode('cp1252').encode('utf-8')
        valores = (livro['isbn'],livro['pags'],
                   livro['titulo'],livro['autores'])
        c.execute('''
                insert into livros (isbn, num_pags, titulo, autores)
                values (?,?,?,?)
            ''', valores)
    bd.commit()
    c.close()

def contar_livros(bd):
    c = bd.cursor()
    c.execute('select count(*) from livros')
    pprint(c.fetchone())
    c.close()

def listar_titulos(bd):
    c = bd.cursor()
    c.execute('select titulo from livros order by titulo')
    for res in c:
        print repr(res[0])
    c.close()

try:
    bd = connect(CAMINHO_BD)
except OperationalError, erro:
    cam_bd, arq_bd = split(CAMINHO_BD)
    if exists(cam_bd):
        print erro
        sys.exit()
    else:
        os.mkdir(cam_bd)
        try:
            bd = connect(CAMINHO_BD)
        except OperationalError, erro:
            print erro
            sys.exit()
        else:
            print 'diretorio %s criado' % cam_bd

criar_tabela(bd)
#testar_insert(bd)
inserir_livros(bd, carga('temporeal_dump.txt',234))
contar_livros(bd)
listar_titulos(bd)

bd.close()





