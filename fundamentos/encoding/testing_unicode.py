# coding: utf-8

u"""
    Display several unicode characters:
    
    >>> chars = u'AaÃãÇç€語'
    >>> chars
    u'Aa\\xc3\\xe3\\xc7\\xe7\\u20ac\\u8a9e'
    >>> print chars
    AaÃãÇç€語
    >>> print u'AaÃãÇç€語'
    AaÃãÇç€語
    >>> ' '.join(chars[:3]) == u'A a \\xc3'
    True
    >>> for c in chars:
    ...   print '%s %04x %-10r %s' % (c, ord(c), c, name(c))
    A 0041 u'A'       LATIN CAPITAL LETTER A
    a 0061 u'a'       LATIN SMALL LETTER A
    Ã 00c3 u'\\xc3'    LATIN CAPITAL LETTER A WITH TILDE
    ã 00e3 u'\\xe3'    LATIN SMALL LETTER A WITH TILDE
    Ç 00c7 u'\\xc7'    LATIN CAPITAL LETTER C WITH CEDILLA
    ç 00e7 u'\\xe7'    LATIN SMALL LETTER C WITH CEDILLA
    € 20ac u'\\u20ac'  EURO SIGN
    語 8a9e u'\\u8a9e'  CJK UNIFIED IDEOGRAPH-8A9E
    >>> print unicode2ascii(chars)
    AaAaCc
"""

from unicodedata import normalize, name

def unicode2ascii(u):
    return normalize('NFKD', u).encode('ASCII','ignore')

if __name__=='__main__':
    import doctest
    try:
        doctest.testmod()
    except UnicodeEncodeError, ue:
        import sys
        print '|**Test output aborted by UnicodeEncodeError',
        print 'in positions %d-%d' % (ue.start, ue.end)
        for lin in ue.object.split('\n'):
            try:
                print '|  ' + lin.rstrip()
            except UnicodeEncodeError:
                print '|%-61r # repr of output' % lin
        failures, tests = doctest.testmod(verbose=False)
        # if verbose output is requested from the commmand-line and there are 
        # failures, testmod reports them; if no failures, we report success
        if '-v' in sys.argv and not failures:
            print tests, 'tests.'
            print '%d passed and %d failed.' % (tests-failures, failures)
            print 'Test passed.'  

