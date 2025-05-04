def zip1(*iterables, strict=False):
    if not iterables:
        return
    iterators = [iter(i) for i in iterables]
    try:
        while True:
            row = []
            for itr in iterators:
                element = next(itr)
                row.append(element)
            yield tuple(row)
    except StopIteration:
        if strict and len(iterables) > 1:
            len_row = len(row)
            if len_row == 1:
                msg = 'argument 2 is shorter than argument 1'
            elif len_row > 1:
                msg = f'argument {len_row+1} is shorter than arguments 1-{len_row}'
            else:  # len(row) == 0 -> first iterator exhausted, check the rest
                sentinel = object()
                for arg_n, itr in enumerate(iterators[1:], 2):
                    element = next(itr, sentinel)
                    if element is not sentinel:
                        break
                else:
                    return  # all exhausted, don't raise ValueError
                if arg_n == 2:
                    msg = 'argument 2 is longer than argument 1'
                elif arg_n > 2:
                    msg = f'argument {arg_n} is longer than arguments 1-{arg_n-1}'

            raise ValueError(msg)