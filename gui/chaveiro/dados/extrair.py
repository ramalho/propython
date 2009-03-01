from BeautifulSoup import BeautifulSoup
from random import choice, randrange
from string import letters
sopa = BeautifulSoup(file('delicious-bookmarks.html').read().decode('utf-8'))

usernames = u'luciano ramalho lramalho admin'.split()
cars = [unichr(i) for i in range(128) if chr(i).strip() and len(repr(chr(i)))==3]

def gerar_senha():
    tam = randrange(4,8)
    senha = []
    while len(senha) < tam:
        senha.append(choice(cars))
    return u''.join(senha)
    
def abrev_tit(texto, tam_max=50):
    texto = texto.strip()
    if len(texto) <= tam_max:
        return texto
    elif texto[50]==u' ':
            return texto[:50]+u'...'
    else:
        pos_esp = texto[:50].rfind(u' ')
        if pos_esp == -1:
            pos_esp = 50
        return texto[:pos_esp]+u'...'
        
def abrev_url(url):
    partes = url.split(u'/')
    return u'/'.join(partes[:4])

for tag in sopa.findAll('a'):
    if len(tag['href']) > 30:
        continue
    if len(tag.string) > 30:
        continue
    print u'\t'.join((
        abrev_tit(tag.string), 
        abrev_url(tag['href']),
        choice(usernames),
        gerar_senha()
    )).encode('utf-8')
