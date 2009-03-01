#!/usr/bin/env python

'''
 exec
'''

import sys
from math import sin as seno
from StringIO import StringIO

buf = StringIO()
stdout = sys.stdout 
# sys.stdout = buf

try:
	try:
		assert (True) and (False) or (not True), 'unTrue'
	except AssertionError:
		print 'False result is expected'
finally:
	print 'Always print this'
	
class Void:
	pass
	
prefix = 'pre-'	
def prepend(word):
	global prefix
 	res = prefix+word
	prefix = prefix.upper()
	return res
	
print prepend('mature')
print prepend('MATURE')
	
inc = lambda x: x+1

def numbers(start):
	n = start
	while True:
		try:
			if n == 20:
				break
			elif n == 10:
				raise ValueError('Here would be ten')
			else:	
				yield n
		except ValueError, e:
			print e
		n = inc(n)
			
						
for i in numbers(4):
	if i in range(1,30,2): continue
	print i		

n = 99		
while not False:		
	try:
		print inc(n)
		inc = None
	except TypeError:
		if inc is None:
			print 'inc is None'
		del inc
	except NameError:
		print 'inc is gone'
		raise SystemExit

print buf
sys.stdout = stdout
print 'The End'