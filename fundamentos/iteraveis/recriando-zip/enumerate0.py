def enumerate0(iterável, i=0):
    for item in iterável:
        yield i, item
        i += 1
