# -*- encoding: utf-8 -*-

__doc__ = u"""

This test should pass::

  >>> print u'ä'
  ä

"""
import doctest

print '-' * 70
failures, tests = doctest.testmod()
print 'No doctest output:'
print '%s tests, %s failures' % (tests, failures)
print '-' * 70
try:
    # next line raises UnicodeEncodeError on Python 2.5
    failures, tests = doctest.testmod(verbose=True) 
    print 'With doctest output:'
    print '%s tests, %s failures' % (tests, failures)
except UnicodeEncodeError, ue:
    print 'Doctest output would contain non-ASCII character, testmod aborts with'
    print 'exception class:', ue.__class__
    print 'encoding:', ue.encoding
    print 'reason:', ue.reason
    print 'start:', ue.start
    print 'end:', ue.end
    print 'object:'
    print ue.object
    

