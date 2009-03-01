#!/usr/bin/env python

import MySQLdb
from pprint import pprint

cnx = MySQLdb.Connect(host="127.0.0.1", port=3306, user="xxxx", passwd="yyyy", db="temporeal")

cur = cnx.cursor()

campos = 'isbn titulo nome_autor_texto categorias num_paginas ano idioma id_editora'.split()

# um teste:
# sql = "SELECT tipo, count(*) FROM produtos GROUP BY tipo"

sql = """SELECT %s FROM produtos WHERE tipo='Livro'""" % ', '.join(campos)
cur.execute(sql)
field_names = cur.description

results = cur.fetchall()

lista = []
for res in results:
    reg = {}
    for chave, valor in zip(campos, res):
        reg[chave] = valor
    lista.append(reg)
cnx.close()

pprint(lista)

