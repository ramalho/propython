from cmd import Cmd

class Planilha(Cmd):
    _cels = {}
    _funcs = {}
    def __init__(self, **funcs):
        Cmd.__init__(self)
        self._funcs.update(funcs)
        self.cmdloop()
    def __setitem__(self, chave, formula):
        self._cels[chave] = formula
    def formula(self, chave):
        return self._cels[chave]
    def __getitem__(self, chave ):
        return eval(self._cels[chave], self._funcs, self)
    def precmd(self, linha):
        if '=' in linha:
            linha = 'def ' + linha
        else:
            linha = 'calc ' + linha
    def do_def(self, linha):
        local, formula = linha.split('=')
        self[local.strip()] = formula.strip()
        
    def do_calc(self, linha):
        return self[linha.strip()]

if __name__ == "__main__":
    p = Planilha()
    
    
