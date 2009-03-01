#!/usr/bin/env python
# -*- coding: iso-8859-1 -*- 

"""
"""

from hx_roman import cp1252_ascii

def main():
    freqs = {}
    texto = open('alienista-iso.txt').read()
    texto = cp1252_ascii(texto).lower()
    for letra in texto:
        if letra.isalpha():
            freqs[letra] = freqs.get(letra, 0) + 1
    letras = freqs.items()
    letras = [ (freq, letra) for (letra, freq) in letras ]
    letras.sort()
    letras.reverse()
    for freq, letra in letras:
        print '%s\t%s' % (letra, freq)
        
        
    

if __name__ == '__main__':
    main()
