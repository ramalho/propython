import Image

bici = Image.open('imagens/bici-2.jpg')

for i in range(0,90,5):
    b2 = bici.rotate(i)
    b2.save('imagens/bici-2-%02d.jpg' % i)
    
