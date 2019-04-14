def kaprekar(n):
    seen = set()
    while n not in seen:
        yield n
        seen.add(n)
        digits = sorted(f'{n:04d}')
        a = int(''.join(digits))
        b = int(''.join(reversed(digits)))
        n = b - a

if __name__ == '__main__':
    for n in range(10_000):
        digits = set(f'{n:04d}')
        if len(digits) < 2:
            print(n, '(invalid)')
            continue
        l = list(kaprekar(n))
        assert l[-1] == 6174, l
        if len(l) == 4:
            print(' '.join(f'{n:04d} ' for n in l))
