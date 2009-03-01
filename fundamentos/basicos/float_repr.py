# coding: utf-8

'''
Este exemplo mostra como a representação interna dos floats 
é diferente daquela que é normalmente apresentado ao usuário.

Para demonstrar, produzimos uma série de floats, cada um a partir 
de uma string de .00 até .99. Convertemos este float de volta 
para string usando as funções str() e repr() e comparamos.

Note que no comando print o valor f é automaticamente convertido
para string usando str().
'''

for i in range(100):
    f = float('.%02d' % i)
    if str(f) == repr(f): 
        marca = '=='
    else: 
        marca = '!='
    
    print marca, '\t', f, '\t', repr(f)
