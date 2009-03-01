# -*- coding: utf-8 -*-
 
'''
euro_iso = '€'
print ord(euro_iso)
Traceback (most recent call last):
  File "coding-utf-8.py", line 4, in ?
    print ord(euro_iso)
TypeError: ord() expected a character, but string of length 3 found
'''
euro_unicode = u'€'
print ord(euro_unicode)

