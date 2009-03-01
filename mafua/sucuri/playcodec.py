import codecs

class StreamReader(codecs.StreamReader):
   def decode(self, input, errors='strict'):
       output = input.replace('until ', 'while not ')
       output = output.replace('++', '+= 1')
       return unicode(output), len(input)

def get_my_codec(name):
   if name == 'play-language':
       return (codecs.utf_8_encode, None, StreamReader, None)

codecs.register(get_my_codec)

