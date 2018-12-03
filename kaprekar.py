def kaprekar(start, indent=0):
    if start == 6174:
        print(indent * '  ' + 'end:', start)
        return
    start_str = str(start).rjust(4, '0')
    print(indent * '  ' + 'seed:', start_str)
    a = int(''.join(sorted(start_str)))
    b = int(''.join(sorted(start_str, reverse=True)))
    small, big = sorted([a, b])
    print(indent * '  ' + 'pair:', big, '-', small)
    kaprekar(big - small, indent + 1)

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        seed = sys.argv[1].rjust(4, '0')
        if len(seed) > 4:
            raise ValueError('Seed requires four or less digits.')            
        if len(set(seed)) == 1:
            raise ValueError('Seed requires two or more distinct digits.')
    else:
        seed = 1
    kaprekar(seed)
