def zip0(*iterables, strict=False):
    if not iterables:
        return
    iterators = [iter(i) for i in iterables]
    try:
        while True:
            row = []
            for itr in iterators:
                item = next(itr)
                row.append(item)
            yield tuple(row)
    except StopIteration:
        shorter = []
        longer = []
        if strict:
            sentinel = object()
            for n, itr in enumerate(iterators, 1):
                item = next(itr, sentinel)
                if item is sentinel:
                    shorter.append(n)
                else:
                    longer.append(n)
            if longer:
                pass
            else:
                pass

