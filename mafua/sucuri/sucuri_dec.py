# coding: utf-8

import codecs

RESERVADAS = (
	('and', 'e'),
    ('assert', 'assegurar'),
    ('break', 'interromper'),
    ('class', 'classe'),
    ('continue', 'continuar'),
    ('def', 'def'),
    ('del', 'apagar'),
    ('elif', 'senaose'),
    ('else', 'senao'),
    ('except', 'exceto'),
    ('exec', 'exec'),
    ('finally', 'finalmente'),
    ('global', 'global'),
    ('import', 'importar'),
    ('lambda', 'lambda'),
    ('pass', 'passar'),
    ('print', 'exibir'),
    ('raise', 'levantar'),
    ('return', 'devolver'),
    ('try', 'tentar'),
    ('while', 'enquanto'),
    ('yield', 'produzir'),
    # os comandos mais curtos tem que ser processados depois dos mais longos
    # para evitar que 'e' seja substituido antes de 'finalmente'
    ('as', 'como'), 
    ('for', 'para'),
    ('not', 'nao'),
    ('with', 'com'),
    ('or', 'ou'),
    ('if', 'se'),
    ('in', 'em'),
    ('is', 'eh'),
    ('from', 'de'),
)


class StreamReader(codecs.StreamReader):
    def decode(self, entrada, erros='strict'): 
        utf_reader = codecs.getreader('utf8')
        saida = entrada
        # saida, n = utf_reader.decode(entrada, erros)
        for orig, trad in RESERVADAS:
            if trad+' ' in saida:
                saida = saida.replace(trad+' ', orig+' ')
            
            if trad+':' in saida:
                saida = saida.replace(trad+':', orig+':')
        return unicode(saida), len(entrada)

def get_my_codec(name):
    if name == 'sucuri':
        return (codecs.utf_8_encode, None, StreamReader, None)

codecs.register(get_my_codec)
__builtins__['tam'] = len
__builtins__['faixa'] = range

