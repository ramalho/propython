total = 0
dic={}
arq = file('doacoes.txt').readlines()
for linha in arq:
    linha = linha.strip()
    if not linha: continue
    linha = linha.split()
    if len(linha) != 2:
        print 'linha invalida, encerrando!', linha
        break
    cod = linha[0]
    val = linha[-1]
    dic[cod] = dic.get(cod,0) + float(val.replace(',','.'))
    # print 'codigo %s valor%6.2f' % (cod, dic[cod])
else:
    lanctos = dic.items()
    lanctos = [(val,cod) for (cod,val) in lanctos]
    lanctos.sort()
    lanctos.reverse()
    for val, cod in lanctos:
        print 'cod:%s  R$ %10.2f' % (cod, val)
        total += val

    print '-' * 23
    print 'total:    R$ %10.2f' % total

        
