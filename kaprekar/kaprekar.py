def kaprekar(start, verbose, indent=0):
    if start == 6174:
        if verbose:
            print(indent * '  ' + 'end:', start)
        else:
            print(start)
        return
    digits = str(start).rjust(4, '0')
    if verbose:
        print(indent * '  ' + 'seed:', digits)
    else:
        print(digits, end=' '   )
    a = int(''.join(sorted(digits)))
    b = int(''.join(sorted(digits, reverse=True)))
    if verbose:
        print(indent * '  ' + 'pair:', b, '-', a)
    kaprekar(b - a, verbose, indent + 1)

if __name__ == '__main__':
    import sys
    if '-v' in sys.argv:
        sys.argv.remove('-v')
        verbose = True
    else:
        verbose = False
    if len(sys.argv) == 2:
        seed = sys.argv[1].rjust(4, '0')
        if len(seed) > 4:
            raise ValueError('Seed requires four or less digits.')            
        if len(set(seed)) == 1:
            raise ValueError('Seed requires at least two distinct digits.')
    else:
        seed = 1
    kaprekar(seed, verbose)
