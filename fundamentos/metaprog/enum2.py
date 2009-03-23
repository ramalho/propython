#!/usr/bin/env python
# -*- encoding: utf-8

'''
Enum, a pragmatic enumeration class

To instantiate, pass a list of strings::

    >>> state = Enum('draft published retracted'.split())
    
Integer constants are created as uppercase instance attributes::    
    
    >>> state.PUBLISHED
    1

The enumeration attributes are read-only, and new attributes can't be set::

    >>> state.DRAFT = 99   
    Traceback (most recent call last):
        ...
    AttributeError: can't set attribute
    >>> state.PENDING = 4   
    Traceback (most recent call last):
        ...
    AttributeError: can't set attribute

The original strings can be retrieved by index::

    >>> state[state.RETRACTED]
    'retracted'
        
Therefore, Enum instances are iterable::

    >>> for i in state: print i
    draft
    published
    retracted

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

class Enum(object):
    def __init__(self, names):
        name_set = set()
        for value, name in enumerate(names):
            attr_name = name.upper()
            if attr_name in name_set:
                raise AttributeError("duplicate name '%s'" % name)
            setattr(self, attr_name, value)
            name_set.add(attr_name)
        self.names = tuple(names)
        self.lock = True
            
    def __getitem__(self, i):
        return self.names[i]

    def __setattr__(self, name, value):
        if hasattr(self, 'lock'):
            raise AttributeError("can't set attribute")
        else:
            self.__dict__[name] = value

    def tuples(self):
        return tuple(enumerate(self))

if __name__=='__main__':
    import doctest
    doctest.testmod()

