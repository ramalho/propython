#!/usr/bin/env python

'''
Enum, a pragmatic enumeration class

To instantiate, pass a list of strings::

    >>> state = Enum('draft published retracted'.split())
    
Integer "constants" are created as uppercase instance attributes::    
    
    >>> state.PUBLISHED
    1

This class does not prevent someone from assigning a new value to one of 
those "constants", but no sane Python programmer would do that (and Python 
never accepts an assignment statement where a boolean expression is expected).

The original strings can be retrieved by index, so Enums are iterable::

    >>> state[state.RETRACTED]
    'retracted'
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
        self.names = []
        for value, name in enumerate(names):
            if name in self.names:
                raise AttributeError("duplicate name '%s'" % name)
            setattr(self, name.upper(), value)
            self.names.append(name)
            
    def __getitem__(self, i):
        return self.names[i]

    def tuples(self):
        return tuple(enumerate(self))

if __name__=='__main__':
    import doctest
    doctest.testmod()

