#/usr/bin/env python

DE = 'cp1252'
PARA = 'utf-8'

nome_ent = 'alienista-cp1252.txt'
nome_sai = 'alienista-utf-8.txt'

ent = open(nome_ent)
sai = open(nome_sai,'wb')

for lin in ent:
    ulin = lin.decode(DE)
    sai.write(ulin.encode(PARA))

sai.close()
ent.close()

