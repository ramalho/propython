def zip1(*iteráveis, strict=False):
    if not iteráveis:
        return
    iteradores = [iter(i) for i in iteráveis]
    try:
        while True:
            linha = []
            for itr in iteradores:
                element = next(itr)
                linha.append(element)
            yield tuple(linha)
    except StopIteration:
        if strict and len(iteráveis) > 1:
            tam_linha = len(linha)
            if tam_linha == 1:
                msg = 'argument 2 is shorter than argument 1'
            elif tam_linha > 1:
                msg = f'argument {tam_linha+1} is shorter than arguments 1-{tam_linha}'
            else:  # len(linha) == 0 -> primeiro iterador vazio, checar os demais
                sentinela = object()
                for arg_n, itr in enumerate(iteradores[1:], 2):
                    element = next(itr, sentinela)
                    if element is not sentinela:
                        break
                else:
                    return  # todos vazios, não levantar exceção
                if arg_n == 2:
                    msg = 'argument 2 is longer than argument 1'
                elif arg_n > 2:
                    msg = f'argument {arg_n} is longer than arguments 1-{arg_n-1}'

            raise ValueError(msg)