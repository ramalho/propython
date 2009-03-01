
'''
Tipos que se recusaram a participar do sort

complex
TypeError: no ordering relation is defined for complex numbers

frozenset
set
TypeError: can only compare to a set
'''    

TIPOS = 'bool dict float int list long str tuple unicode'.split()

lista = [None]
for nome_tipo in TIPOS:
    obj = getattr(__builtins__,nome_tipo)()
    lista.append(obj)
    
print sorted(lista)
    

