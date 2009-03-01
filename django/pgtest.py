#!/usr/bin/env python2.5

import psycopg2

DSN = "dbname='circulante' user='circ_admin' host='localhost' password='qazwsx'"

def executar(sql):
    cnx = psycopg2.connect(DSN)
    cur = cnx.cursor()
    cur.execute(sql)
    print cur.statusmessage
    cnx.commit()
    return cur

def criar_tabela():
    sql = '''
    CREATE TABLE tblixo ( 
            id      CHARACTER(8) UNIQUE, 
            titulo  CHARACTER VARYING(80), 
            pags    INTEGER 
    ) 
    '''
    executar(sql)

def inserir_dados():
    sql = '''
    INSERT INTO tblixo VALUES ( 
      'a', 
      'A Almofada Alienada', 
      123
    ) 
    '''
    executar(sql)

def listar_dados():
    sql = '''SELECT * FROM tblixo'''
    cur = executar(sql)
    res = cur.fetchall()
    for reg in res:
        print reg
    
def remover_tabela():
    sql = '''DROP TABLE tblixo'''
    executar(sql)
    
if __name__=='__main__':
    try:
        criar_tabela()
    except psycopg2.ProgrammingError:
        print 'tabela previamente criada'
    try:
        inserir_dados()
    except psycopg2.IntegrityError:
        print 'dados previamente inseridos'
    listar_dados()
    remover_tabela()
