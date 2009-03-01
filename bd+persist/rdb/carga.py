#!/usr/bin/env python
# coding: cp1252

from pprint import pprint

def ler_arq_delim_tabs(nome_arq, num_registros=None):
    arq = file(nome_arq)
    registros = []
    for lin in arq:
        lin = lin.strip()
        if not lin: continue
        lin = lin.split('\t')
        if len(lin) != 4: continue
        isbn, pags, titulo, autores = lin 
        autores = [a.strip() for a in autores.split('/')]
        autores_dir = []
        try:
            for autor in autores:
                autor = [nome.strip() for nome in autor.split(',')]
                if len(autor) == 2:
                    autor = autor[1] + ' ' + autor[0]
                else:
                    raise ValueError, 'len(autor)!=2: '+repr(autor)
                autores_dir.append(autor)
            autores = '|'.join(autores_dir)
        except ValueError:
            autores = '???' + repr(autores)
            
        reg_dic = {'isbn':isbn, 'pags':pags, 'titulo':titulo, 'autores':autores}
        registros.append(reg_dic)
        if num_registros is not None and len(registros) == num_registros:
            break
    return registros

if __name__=='__main__':
	res = ler_arq_delim_tabs('temporeal_dump.txt')
	print len(res), 'registros lidos'
  
               
