#!/usr/bin/env python

import cgi
import cgitb; cgitb.enable() 
from urllib import urlencode
from os import environ

from wff import wff, wff_dice, turn
from time import time

TITLE = "WFF'n'PROOF"
SCRIPT = environ['SCRIPT_NAME']

jscript = """
document.getElementById('guess_field').focus()
"""

print 'Content-type: text/html\n'

print '<html><head><title>%s</title>' % TITLE
print '</head><body onload="%s">' % jscript

print '<h1>%s</h1>' % TITLE

form = cgi.FieldStorage()
game_over = 0 

if form.has_key('turns'):
    turns = int(form.getfirst('turns'))
    if turns == 0:
        start_time = time()
        num_dice = 3
        max_dice = 8
        errors = 0
        msg = 'The clock is running...'
    else:
        reply = form.getfirst('reply')
        if reply is None:
            reply = ''
        dice = list(form.getfirst('dice'))
        start_time = float(form.getfirst('start_time'))
        num_dice = int(form.getfirst('num_dice'))
        max_dice = int(form.getfirst('max_dice'))
        errors = int(form.getfirst('errors'))
        if (num_dice <= max_dice) and (num_dice > 0):
            msg, num_dice, errors = turn(dice, reply, num_dice, errors)
        else:
            game_over = 1      
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
            msg += ' in %d turns (%f seconds).' % (turns, time()-start_time)
    print '<hr>'
    print '<h4>%s</h4>' % msg
    print '<hr>'
    if not game_over:
        turns += 1
        dice = wff_dice(num_dice)
        print '<form action="%s">' % SCRIPT
        print '<h3>Turn %s</h3>' % turns
        print '<h1>%s</h1>' % '&nbsp;'.join(dice)
        print '<input id="guess_field" type="text" name="reply">'
        print '<input type="submit">'
        print '<input type="hidden" name="start_time" value="%f">' % start_time
        print '<input type="hidden" name="dice" value="%s">' % ''.join(dice)
        print '<input type="hidden" name="num_dice" value="%d">' % num_dice
        print '<input type="hidden" name="max_dice" value="%d">' % max_dice
        print '<input type="hidden" name="turns" value="%d">' % turns
        print '<input type="hidden" name="errors" value="%d">' % errors
        print '</form>'
        print '<hr>'

args = urlencode({'turns':0, 'max_dice':8})
print '<a href="wff.cgi?%s">New game</a>' % args   

print '</body></html>'