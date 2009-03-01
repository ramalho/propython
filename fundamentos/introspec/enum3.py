#!/usr/bin/env python
# -*- encoding: utf-8

'''
Enum, an internationalized enumeration class

To instantiate, pass a list of strings::

    >>> state = Enum('draft published retracted'.split())
    
Integer constants are created as uppercase instance attributes::    
    
    >>> state.PUBLISHED
    1

Non-Ascii strings using the Latin alphabet are handled sensibly::

    >>> estado = Enum(['esboço', 'publicado', 'retirado'])
    >>> estado.ESBOCO
    0
    
The original strings can be retrieved by index::

    >>> state[state.RETRACTED]
    'retracted'
        
Therefore, Enum instances are iterable::

    >>> for i in state: print i
    draft
    published
    retracted

The enumeration constants are read-only::

    >>> state.DRAFT = 99   
    Traceback (most recent call last):
        ...
    AttributeError: can't set attribute 'DRAFT'

For Django programmers, the tuples method generates a tuple of two-tuples
suitable for use as choices in fields::

    >>> state.tuples()
    ((0, 'draft'), (1, 'published'), (2, 'retracted'))

As usual in Python, only existing attributes can be referenced::
    
    >>> state.FOO   
    Traceback (most recent call last):
        ...
    AttributeError: 'Enum' object has no attribute 'FOO'
    
Finally, note that duplicate items are not allowed::

    >>> dept = Enum(['DA', 'DB', 'DC', 'DB'])
    Traceback (most recent call last):
        ...
    AttributeError: duplicate name 'DB'
    
'''







from unicodedata import normalize

class Enum(object):
    def __init__(self, names, encoding='utf-8'):
        self.__names = []
        self.__encoding = encoding
        for value, name in enumerate(names):
            self[value] = name
            
    def __setitem__(self, index, name):
        if index == len(self.__names):
            uni_name = name.decode(self.__encoding)
            ascii_name = normalize('NFKD', uni_name).encode('ASCII','ignore')
            attr_name = ascii_name.upper()
            if hasattr(self, attr_name):
                raise AttributeError("duplicate name '%s'" % attr_name)
            setattr(self, attr_name, index)
            self.__names.append(name)
        else:
            raise IndexError('items must be assigned in sequence from 0')

    def __setattr__(self, name, value):
        if hasattr(self, name):
            raise AttributeError("can't set attribute '%s'" % name)
        else:
            self.__dict__[name] = value

    def __getitem__(self, i):
        return self.__names[i]

    def tuples(self):
        return tuple(enumerate(self))

if __name__=='__main__':
    import doctest
    doctest.testmod()

