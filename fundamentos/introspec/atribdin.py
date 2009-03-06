# coding: utf-8


class C(object):
    '''
        >>> o = C(7)
        >>> o.x
        7
        >>> o.y
        'Y!'
        >>> o.z
        0
        >>> o.i
        Traceback (most recent call last):
            ...
        AttributeError: 'C' object has no attribute 'i'
        
    '''
    def __init__(self, x):
        self.x = x
        
    def __getattr__(self, atrib):
        if atrib == 'z':
            return 0
        elif atrib == 'i':
            msg = "'%s' object has no attribute '%s'"
            classe = self.__class__.__name__
            raise AttributeError(msg % (classe, atrib))
        return atrib.upper() + '!'

class D(object):
    '''
        >>> d = D(a=1, b=2, c=3)
        >>> d.a
        1
        >>> d.x
        Traceback (most recent call last):
            ...
        AttributeError: 'D' object has no attribute 'x'

    '''
    def __init__(self, **kwargs):
        self.__vars = kwargs
    def __getattr__(self, atrib):
        if atrib in self.__vars:
            return self.__vars[atrib]
        else:
            msg = "'%s' object has no attribute '%s'"
            classe = self.__class__.__name__
            raise AttributeError(msg % (classe, atrib))
        
if __name__=='__main__':
    import doctest
    doctest.testmod()        

