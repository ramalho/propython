#!/usr/bin/env python

from keyword import kwlist

source = file(__file__).readlines()

kws = set(kwlist)
used = set()

for line in source:
	for kw in kwlist:
		
			
unused = kws - used
print sorted(unused)