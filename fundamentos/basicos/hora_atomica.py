#!/usr/local/bin/python
#reports how many seconds you are off the atomic clock.
#Positive mean you are ahead, negative means you are behind.
import urllib,re,time

URL = 'http://nist.time.gov/timezone.cgi?UTC/s/0'
print 'Acessando %s...' % URL
html = urllib.urlopen(URL).read()
hora_atom, min_atom, seg_atom = re.search('<b>(\d\d:\d\d:\d\d)',html).group(1).split(":")
hora_sis, min_sis, seg_sis = time.gmtime()[3:6]
diferenca = ((hora_sis - int(hora_atom)) * 3600 + (min_sis - int(min_atom))) * 60 + (seg_sis-int(seg_atom))
if diferenca > 0:
	erro = 'adiantada'
elif diferenca < 0:
	erro = 'atrasada'
	diferenca = -diferenca
else:
	erro = None
if erro: 
	print 'Hora local %s em %ss' % (erro, diferenca)
else:
	print 'Hora local correta (erro < 1s)'