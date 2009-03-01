import pacote
from pacote import mod1

for c in pacote.__dict__:
    print c, pacote.__dict__[c]
    
print pacote.mod1

for c in mod1.__dict__:
    print c, mod1.__dict__[c]

