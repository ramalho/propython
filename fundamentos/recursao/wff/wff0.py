#!/usr/bin/env python

'''
Wff 'N Proof game invented by Layman E. Allen

Python implementation by Luciano Ramalho (ramalho at the google mail service)

Unsolved: 
these dice would allow a longer answer but the program accepted a
shorter one:

     . A E N p p s q >>> napp
 8 | OK: NApp
"""


'''

from random import choice
from string import maketrans
from time import time

#C_cube = 'NCAKEZ' # changed R for Z to allow case-insensitive evaluation
#s_cube = 'pqrsio'

C_cube = 'SRDNTK'
s_cube = 'aeoiyw'
OPS = C_cube[1:5]
NEG = C_cube[0]
ARG = s_cube[:4]

def wff(f):
    '''check if f is a WFF''' 
    f = list(f)
    if len(f) == 1:
        return f[0] in ARG
    elif len(f) > 1:
        if f[0] == NEG:
            return wff(f[1:])
        elif f[0] in OPS:
            f1 = f[1:-1]
            f2 = f[-1:]
            while not wff(f1):
                if len(f1) == 0:
                    return 0
                f2.insert(0, f1.pop())
            return wff(f1) and wff(f2)
        else:
            return 0
    else: # len(f) < 1
        return 0
        
def _wff_save(new_wff, wffs):
    '''used by wff_gen'''
    '''insert new_wff in wffs, keeping longest first'''
    i = position = 0
    while i < len(wffs):
        if len(new_wff) >= len(wffs[i]): # keep sorted by size
            if new_wff < wffs[i]:        # keep sorted by ASCII
                position = i
            else:
                position = i + 1    
            break
        i += 1
    wffs.insert(position, new_wff)
    
def wff_gen(symbols):
    symbols = list(symbols)
    # set aside N's which can always be used if we have one WFF
    ens = [s for s in symbols if s == NEG]
    # discard useless symbols
    avail = [s for s in symbols if s in (OPS+ARG)]
    # put Caps in front
    avail.sort() # list of available symbols
    # sorted stack of wffs (wffs[0] is the longest) 
    wffs = []
    while avail:
        symbol = avail.pop()
        if symbol in ARG:
            _wff_save(symbol, wffs)
        else: # symbol in OPS
            if len(wffs) >= 2: # assemble CAKE WFF
                # get first wffs -- they are the longest
                new_wff = symbol + wffs.pop(0) + wffs.pop(0)
                _wff_save(new_wff, wffs)
            else: # no more WFFs to assemble CAKE 
                break # no more WFFs   

    if len(wffs) > 0:
        big_wff = list(wffs[0])
        big_wff = ens + big_wff     # prepend N's
        return ''.join(big_wff)
    else:
        return ''
        
def wff_dice(n):
     dice = []
     for i in range(n):
        if (i % 2) == 0:
            dice.append(choice(s_cube))
        else:
            dice.insert(0, choice(C_cube))
     return dice
     
def _validate(reply, dice):
    '''used by turn'''
    '''check if reply contains only symbols from dice'''
    ok = []
    dice = dice[:]
    for symb in reply:
        if symb in dice:
            dice.remove(symb)
            ok.append(symb)     
    return len(ok) == len(reply)
    
def turn(dice, reply, errors):
    reply = ''.join(reply.split()) # remove blanks
    # for user convenience, set C,A,K,E,N,Z to uppercase
    trans = maketrans(C_cube.lower(), C_cube)
    reply = reply.translate(trans)
    longest = wff_gen(dice)
    num_dice = len(dice)
    if not _validate(reply, dice):
        num_dice -= 1
        errors += 1
        msg = 'reply contains symbols not given'
    elif wff(reply):
        if len(longest) > len(reply):
            num_dice -= 1
            errors += 1
            msg = 'longest: %s (%d)' % (longest, len(longest))
        else:
            num_dice += 1
            msg = 'OK: ' + reply
    else: # not wff
        if reply:
            num_dice -= 1
            errors += 1
            msg = '"%s" is not a WFF; ' % reply
            if longest:
                msg += 'longest: %s (%d)' % (longest, len(longest))
            else:
                msg += 'no WFF possible'
        else:
            if longest:
                num_dice -= 1
                errors += 1
                msg = 'no reply; longest: %s (%d)' % (longest, len(longest))
            else:    
                num_dice += 1
                msg = 'OK, no WFF was possible'
    return (msg, num_dice, errors)
          
def main(max_dice = 10):
    num_dice = 3
    errors = 0
    turns = 0
    t0 = time()
    while (num_dice <= max_dice) and (num_dice > 0):
        dice = wff_dice(num_dice)
        padding = '. ' * (max_dice - num_dice)
        prompt = '(%d) %s%s >>> ' % (num_dice, padding, ' '.join(dice))
        reply = raw_input(prompt).strip()
        msg, num_dice, errors = turn(dice, reply, errors)
        print '...' , msg
        turns += 1
    if num_dice != 0:    
        msg = 'Completed with '
    else:
        msg = 'Read the WFF rules and try again. You made '    
    if errors == 0:
        msg += 'no errors'
    elif errors == 1:
        msg += '1 error'
    else:
        msg += '%d errors' % errors
    msg += ' in %d turns (%f seconds).' % (turns, time()-t0)
    print msg            
        
    
TEST_FORMULAS = [
        (0, 'z'),
        (0, 'C'),
        (0, 'Cp'),
        (0, NEG),
        (0, 'zp'),
        (0, 'pz'),
        (1, 'Nq'),
        (0, 'qN'),
        (1, 'NNp'),
        (0, 'NpNp'),
        (1, 'NNNp'),
        (1, 'CNpq'),
        (1, 'NCpAqr'),
        (0, 'NCpZAqr'),
        (1, 'EKqrr'),
        (1, 'AENpps'),
        (0, 'AENppsq'),
        # from the WFFNEGproof rulebook
        (1, 'p'),           # 1
        (0, 'o'),           # 2
        (0, 'pq'),          # 3
        (1, 'Np'),          # 4
        (1, 'NNq'),         # 5
        (1, 'NNNr'),        # 6
        (0, 'sN'),          # 7
        (0, 'pNs'),         # 8
        (1, 'Cpq'),         # 9
        (1, 'CpNq'),        # 10
        (1, 'CCpqCpNq'),    # 11
        (0, 'pCq'),         # 12
        (0, 'Api'),         # 13
        (1, 'KNpNr'),       # 14
        (1, 'AsKNpNr'),     # 15
        (1, 'EAsKNpNrNq'),  # 16
        (0, 'CNpApi'),      # 17
        (1, 'CpAqKrs'),     # 18
        (1, 'CAKpqrs'),     # 19
        (0, 'CpAqrKs'),     # 20
        (1, 'NCAKpqrs'),    # 21
    ]
    

def test_wff():
    for value, formula in TEST_FORMULAS:
        res = wff(formula)
        if value == res:
            msg = 'OK'
        else:
            msg = 'Error: value = %s, wff(f) = %s' % (value, res)
        print '%s: %s\t%s' % (value, formula, msg)
        
def test_wff_gen():
    for value, formula in TEST_FORMULAS:
        if value != 1: continue
        w = wff_gen(formula)
        if len(w) == len(formula) and wff(w):
            msg = 'OK'
        elif not wff(w):
            msg = 'NOT wff'
        else:
            msg = '(len(f) = %s) != (len(w) = %s)' % (len(formula), len(w))     
        print '%s\t%s\t%s' % (formula, w, msg)
        
if __name__ == '__main__':
    #test_wff()
    test_wff_gen()
    #main()
    
