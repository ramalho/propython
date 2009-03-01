

class Cao:

    def __init__(self, nome):
        self.nome = nome
        
    def latir(self):
        print '%s: Au!' % self.nome
        
    def __getitem__(self, idx):
        return self.__dict__[idx]    
        
fido = Cao('Fido')
# fido['latir']()
print Cao.__methods__
