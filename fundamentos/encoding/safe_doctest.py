# -*- encoding: utf-8 -*-

__doc__ = u"""

This test should always pass::

  >>> print u'a'
  a

This should also pass, but can raise encoding errors::

  >>> print u'ä' 
  ä
  
This test never passes (to enable it, replace +SKIP with -SKIP)::

  >>> print 9 # doctest: +SKIP
  7

"""

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

