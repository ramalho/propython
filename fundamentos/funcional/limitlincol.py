#!/usr/bin/env python

'''
Currying example

The limit2x2 function returns a function which evaluates
limitLinCol(2, 2, value). It's used like this:

>>> limit2x2()('a')
True
>>> limit2x2()('abc')
False

Note: trailing newlines count as lines, therefore

>>> countLinCol('a\nb\n')
(3,1)

To avoid counting trailing newlines, use rstrip:

>>> countLinCol('a\nb\n'.rstrip())
(2,1)
'''

def countLinCol(text):
    '''returns (lineCount, columnCount); trailing newlines count as lines'''
    lines = text.split('\n')
    maxCols = max(len(l.strip()) for l in lines)
    return len(lines), maxCols
    
def limitLinCol(maxLines, maxCols, value):
    lines, cols = countLinCol(value)
    return lines <= maxLines and cols <= maxCols
    
def limit2x2():
    return lambda value: limitLinCol(2,2,value)
    
def _test():
    data = {
        (1,0):'',
        (2,0):'\n',
        (3,0):'\n\n',
        (1,1):'a',
        (2,1):'a\n',
        (2,1):'a\na',
        (2,2):'ab\nab',
        (3,3):'abc\nab\n',
        (3,3):'a\nab\nabc',
    }
    for result, text in data.items():
        assert result == countLinCol(text), '%r =/= %r' % (result, text)
        if max(result) <= 2:
            assert limit2x2()(text), '%r =/= %r' % (result, text)
        else:
            assert not limit2x2()(text), '%r =/= %r' % (result, text)
    print 'OK'
        
if __name__=='__main__':
    _test()
