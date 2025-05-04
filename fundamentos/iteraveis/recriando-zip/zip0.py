def zip1(*iterables):
    if not iterables:
        return
    iterators = [iter(i) for i in iterables]
    while True:
        row = []
        for itr in iterators:
            try:
                element = next(itr)
            except StopIteration:
                return
            row.append(element)
        yield tuple(row)
