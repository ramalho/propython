import pickle
import zlib
from os import rename, remove, path

from eagle import App, Table, Button, QuitButton, Label, Password, Group, yesno, run

from cripto.ciphersaber2 import cifrar, decifrar

NOME_ARQ_DADOS = 'chaveiro.dat'

MSG_SENHA_INICIAL = 'Digite a senha-mestre antes de armazenar dados.'
MSG_SENHA_ABRIR = 'Digite a senha-mestre para ler e decifrar os dados do disco.'
MSG_SENHA_ERRADA = 'Senha-mestre incorreta. Tente novamente.'

senha_mestre = ''
dados_lidos = False

def ler():
    try:
        arq = file(NOME_ARQ_DADOS,'rb')
    except IOError, erro:
        if 'No such file or directory' in str(erro):
            return
        else:
            raise erro
    else:
        bytes = arq.read()
        arq.close()
        bytes = decifrar(senha_mestre, bytes)
        try:
            bytes = zlib.decompress(bytes)
        except zlib.error, erro:
            janela['mensagem-senha'] = MSG_SENHA_ERRADA
            return
        else:
            janela['mensagem-senha'] = MSG_SENHA_ABRIR
            return pickle.loads(bytes)
            
    
def gravar(dados):
    arq = file(NOME_ARQ_DADOS+'.NEW','wb')
    bytes = pickle.dumps(dados, pickle.HIGHEST_PROTOCOL)
    bytes = zlib.compress(bytes)
    bytes = cifrar(senha_mestre, bytes)
    arq.write(bytes)
    arq.close()
    try:
        rename(NOME_ARQ_DADOS, NOME_ARQ_DADOS+'.BKP')
    except OSError, erro:
        if 'No such file or directory' in str(erro):
            apagar_backup = False
        else:    
            raise erro
    else:
        apagar_backup = True
    rename(NOME_ARQ_DADOS+'.NEW', NOME_ARQ_DADOS)
    if apagar_backup:
        remove(NOME_ARQ_DADOS+'.BKP')
    
def mudou(janela, tabela, alteracao=None):
    dados = []
    for linha in tabela:
        itens = []
        for valor in linha:
            itens.append(valor)
        dados.append(itens)
    gravar(dados)
    
def senha_digitada(janela, controle, valor):
    global senha_mestre
    if dados_lidos and valor != senha_mestre:
        if yesno('Alterar a senha-mestre?'):
            senha_mestre = valor    
            mudou(janela, janela['tabela'])
        else:
            controle.set_value(senha_mestre)
    else:
        senha_mestre = valor
    if len(senha_mestre):
        janela['acao'].enable()
    else:
        janela['acao'].disable()

   
def carregar(janela, controle):
    global dados_lidos
    dados = ler()
    if dados:
        janela['tabela'][:] = dados
        dados_lidos = True
    
janela = App(title='Chaveiro',
    center=(
        Table('tabela', 'Sites',
            types=( str, str, str, str ),
            headers=( 'titulo', 'URL', 'login', 'senha' ),
            expand_columns_indexes=(0,1),
            editable=True,
            data_changed_callback=mudou
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
                            callback=senha_digitada),
                    )
                ),
                Button('acao',label='Ler e decifrar',callback=carregar),
                QuitButton(),
            )
        )
    )
)
janela['acao'].disable()
if path.exists(NOME_ARQ_DADOS):
    janela['mensagem-senha'] = MSG_SENHA_ABRIR
else:
    janela['mensagem-senha'] = MSG_SENHA_INICIAL
        

run()
