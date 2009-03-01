lista = []
for simb in sorted(dir(__builtins__)):
    obj = getattr(__builtins__, simb)
    tipo = type(obj).__name__
    lista.append((tipo, simb))

tipo_ant = ''
for tipo, simb in sorted(lista):
    if tipo != tipo_ant:
        print '\n' + '-' * 30 + '\n' + tipo + '\n' + '-' * 30
        tipo_ant = tipo
    print simb
    
 
    
 
