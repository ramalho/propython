def zip0(*iteráveis):
    if not iteráveis:
        return
    iteradores = [iter(i) for i in iteráveis]
    while True:
        linha = []
        for itr in iteradores:
            try:
                célula = next(itr)
            except StopIteration:
                return
            linha.append(célula)
        yield tuple(linha)
