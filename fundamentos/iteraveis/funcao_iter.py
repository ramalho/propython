from random import randint
from functools import partial
dado = partial(randint,1,6)
print dado()
print dado()
print dado()

# exibe valores ate que um 6 seja sorteado
# 6 e' o "sentinela"
for r in iter(dado, 6): print r
