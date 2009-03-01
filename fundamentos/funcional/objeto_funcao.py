x = 99

def funcao(a, b=2, c='xyz'):
   z = 77
   return '%s, %s, %s, %s' % (x, a, b, c)
   
for atr in dir(funcao):
    if atr.startswith('func_'):
        print '%14s: %r' % (atr, getattr(funcao,atr))

cod = funcao.func_code

for atr in dir(cod):
    if atr.startswith('co_'):
        print '%14s: %r' % (atr, getattr(cod,atr))
        
arg_defaults = cod.co_varnames[cod.co_argcount-len(funcao.func_defaults):cod.co_argcount]
print 'args com default: ', zip(arg_defaults, funcao.func_defaults)

