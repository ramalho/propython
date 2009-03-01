# -*- encoding: utf-8 -*-

__doc__ = """

This test should pass::

  >>> print('ä')
  ä

"""
import doctest

print('-' * 70)
failures, tests = doctest.testmod()
print('No doctest output, everything works:')
print('%s tests, %s failures' % (tests, failures))
print('-' * 70)
try:
    failures, tests = doctest.testmod(verbose=True)
except UnicodeEncodeError as ue:
    print('Doctest output would contain non-ASCII character, testmod aborts with')
    print('exception class:', ue.__class__)
    print('encoding:', ue.encoding)
    print('reason:', ue.reason)
    print('start:', ue.start)
    print('end:', ue.end)
    print('object:')
    print(ue.object)
    

