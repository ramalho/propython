#!/usr/bin/env python2.5

import MySQLdb
import MySQLdb.cursors

from TRDBCONFIG import USER, PASSWD

conn = MySQLdb.Connect(
    host='localhost', user=USER,
    passwd=PASSWD, db='temporeal',compress=1)

def select():

    # results by field number
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM produtos where tipo='livro'")
    res = cursor.fetchall()
    cursor.close()
    print res


def sel_campos(*campos):
    # results by field name
    cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    sql = "SELECT %s FROM produtos where tipo='Livro'" % ', '.join(campos)
    cursor.execute(sql)

    res = cursor.fetchall()
    cursor.close()
    conn.close()

    for reg in res:
        for campo in campos:
            try:
                print reg[campo]+'\t',
            except TypeError:
                print str(reg[campo])+'\t',
        print

if __name__ == '__main__':
    sel_campos('isbn','num_paginas','titulo','nome_autor_texto')





