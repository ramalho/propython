#!/usr/bin/env python

romanNumeralMap = (('M',  1000),
                   ('CM', 900),
                   ('D',  500),
                   ('CD', 400),
                   ('C',  100),
                   ('XC', 90),
                   ('L',  50),
                   ('XL', 40),
                   ('X',  10),
                   ('IX', 9),
                   ('V',  5),
                   ('IV', 4),
                   ('I',  1))
                   
romanNumeralDict = dict(romanNumeralMap)

def toRoman(n):
    """convert integer to Roman numeral"""
    if not (0 < n < 4000):
        raise ValueError("number out of range (must be 1..3999)")

    result = ""
    for numeral, integer in romanNumeralMap:
        while n >= integer:
            result += numeral
            n -= integer
    return result
    
def romanoFormatado(n):
    # * marca o lugar reservado para o C em CM, CMLXXXVIII etc.
    r = toRoman(n)
    mascara = '*MMMDCCCLXXXVIII' 
    maior_letra = 'I'
    maior_valor = 1
    pos_maior = 0
    for pos, car in enumerate(r):
        valor = romanNumeralDict[car]
        if valor > maior_valor:
            maior_letra = car
            maior_valor = valor
            pos_maior = pos
    prefixo = mascara.index(maior_letra) - pos_maior
    posfixo = len(mascara) - (prefixo+len(r))
    return (prefixo*' ' + r + posfixo*' ')
    
if __name__=='__main__':
    for i in range(1,4000):
        print romanoFormatado(i)
    
