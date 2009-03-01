#!/usr/bin/env python
# coding: utf-8

from eagle import App, Table, Button, QuitButton, Label, Password, Group, yesno, error, run

from chaveiro import Chaveiro, SenhaIncorreta, ArquivoCorrompido

from os import path

MSG_SENHA_INICIAL = 'Digite a senha-mestre antes de armazenar dados.'
MSG_SENHA_ABRIR = 'Digite a senha-mestre para ler e decifrar os dados do disco.'

class TabelaChaveiro(Table):

    def __init__(self, *args, **kwargs):
        self.senha = kwargs['senha']
        del kwargs['senha']
        super(TabelaChaveiro, self).__init__(*args, **kwargs)
        self.chaveiro = Chaveiro(self.senha)
                        
    def mudou(self):
        dados = []
        for linha in self:
            itens = []
            for valor in linha:
                itens.append(valor)
            dados.append(itens)
        if dados:
            self.chaveiro.carregar(dados)
            self.chaveiro.gravar()

    def senha_digitada(self, controle, nova_senha):
        if self.chaveiro and self.chaveiro.senha != nova_senha:
            if yesno('Alterar a senha-mestre?'):
                self.chaveiro.senha = nova_senha
                self.mudou()
            else:
                controle.set_value(self.chaveiro.senha)
        else:
            self.chaveiro.senha = nova_senha
            
        if len(nova_senha):
            janela['acao'].enable()
        else:
            janela['acao'].disable()
        
    def carregar(self):
        try:
            self.chaveiro.ler()
        except (SenhaIncorreta, ArquivoCorrompido), erro:
            error(erro.__doc__)
        else:
            self[:] = self.chaveiro.chaves
    
# Quem não gosta de lambda pode chamar estas funções no lugar dos lambdas...
#def mudou(janela, tabela, valor):
#    tabela.mudou()

#def senha_digitada(janela, controle, valor):
#    tabela.senha_digitada(controle, valor)

#def carregar(janela, botao):
#    tabela.carregar()

janela = App(title='Chaveiro',
    center=(
        TabelaChaveiro('tabela', 'Sites',
            senha = '1234',
            types=( str, str, str, str ),
            headers=( 'titulo', 'URL', 'login', 'senha' ),
            expand_columns_indexes=(0,1),
            editable=True,
            data_changed_callback=lambda app,ctr,vlr:tabela.mudou()
        ),
        Group('duas-celulas',
            horizontal=True,
            children=(
                Group('area-senha',
                    label='Senha-mestre',
                    children=(
                        Label('mensagem-senha',
                            label=MSG_SENHA_ABRIR),
                        Password('senha', 
                            active=True,
                            persistent=False,
                            callback=lambda app,campo,valor:tabela.senha_digitada(campo, valor),
                        )
                    )
                ),
                Button('acao',label='Ler e decifrar',callback=lambda app,btn:tabela.carregar()),
                QuitButton(),
            )
        )
    )
)
        
janela['acao'].disable()
tabela = janela['tabela']
if path.exists(tabela.chaveiro.nome_arq):
    janela['mensagem-senha'] = MSG_SENHA_ABRIR
else:
    janela['mensagem-senha'] = MSG_SENHA_INICIAL

run()
