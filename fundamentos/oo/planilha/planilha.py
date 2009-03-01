class Planilha:
    """
    >>> from math import sin, pi
    >>> p = Planilha(sen=sin, pi=pi)
    >>> p['a1'] = '5'
    >>> p['a2'] = 'a1*6'
    >>> p['a3'] = 'a2*7'
    >>> p['a3']
    210
    >>> p['b1'] = 'sen(pi/4)'
    >>> p['b1']
    0.70710678118654746
    >>> p.formula('b1')
    'sen(pi/4)'
    """
    _cels = {}
    _funcs = {}
    def __init__(self, **funcs):
        self._funcs.update(funcs)
    def __setitem__(self, chave, formula):
        self._cels[chave] = formula
    def formula(self, chave):
        return self._cels[chave]
    def __getitem__(self, chave ):
        return eval(self._cels[chave], self._funcs, self)

if __name__ == "__main__":
    print 'Testando...'
    import doctest, planilha
    doctest.testmod(planilha)
    
