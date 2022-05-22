"""

O que há na floresta
====================

Boitatá
    Uma cobra gigante iluminada.
    Seu objetivo é fotografá-la com um drone.
    Se você entrar na casa da Boitatá ela te come.

Curupira e Caipora
    Guardiães da floresta.
    Se você ou o drone entrar na casa com um deles,
    o guardião te leva direto pra uma casa aleatória,
    o que pode ser trágico.

Furna
    Duas casas são furnas profundas.
    Se cair numa delas, babau.


Ações
=====

Você pode fazer uma dessas ações:

Andar
    Digite o número da casa para onde quer ir.


Lançar o drone
    Digite ``drone N…`` ou ``d N…``, onde ``N…`` é uma série de até
    cinco números indicando as casas visitadas pelo drone.
    As casas precisam estar conectadas na ordem listada.
    Se o drone terminar o vôo na casa da Boitatá, você ganha o jogo.
    Você tem baterias para 5 vôos de drone.

Sair
    Digite ``sair`` ou ``s`` para sair do jogo.


Mapa
====

As casas são numeradas de 1 a 20.
Cada uma se conecta a outras três.

┌──1──────────────2─────────3──┐
│  │              │         │  │
│  8─────────9───10───11───12  │
│  │         │         │    │  │
│  7───17───18────────19    │  │
│  │    │              │    │  │
│  │   16─────────────20───13  │
│  │    │                   │  │
│  6───15──────────────────14  │
│  │                        │  │
└──5────────────────────────4──┘

A topologia é a mesma dos vértices de um dodecahedro:
as casas são os vértices e os caminhos são as arestas.


"""

import readline
from dataclasses import dataclass
from random import choice


passagens = {
    1: [2, 5, 8],
    2: [1, 3, 10],
    3: [2, 4, 12],
    4: [3, 5, 14],
    5: [1, 4, 6],
    6: [5, 7, 15],
    7: [6, 8, 17],
    8: [1, 7, 9],
    9: [8, 10, 18],
    10: [2, 9, 11],
    11: [10, 12, 19],
    12: [3, 11, 13],
    13: [12, 14, 20],
    14: [4, 13, 15],
    15: [6, 14, 16],
    16: [15, 17, 20],
    17: [7, 16, 18],
    18: [9, 17, 19],
    19: [11, 18, 20],
    20: [13, 16, 19],
}


@dataclass
class Perigo:
    nome: str


@dataclass
class Casa:
    número: int
    vizinhas: list[int]
    perigo: Perigo | None


def escolher_casa_segura(casas):
    while True:
        n = choice(list(casas))
        if not casas[n].perigo:
            return casas[n]

@dataclass
class Jogador:
    posição: Casa
    baterias: int = 5

    def andar(self, destino):
        if destino in self.posição.vizinhas:
            self.posição = casas[destino]
        else:
            print(f'*** {destino} não é uma casa vizinha.')


    def lançar_drone(self, caminho):
        if not caminho or len(caminho) > 5:
            print(f'*** o drone pode visitar de 1 a 5 casas.')
            return
        try:
            caminho = [int(passo) for passo in caminho]
        except ValueError:
            print(f'*** informe os números das casas para o drone visitar.')
            return
        print('vrummmmm')



casas = {n: Casa(n, vizinhas, None) for n, vizinhas in passagens.items()}


def analisar(comando):
    partes = []
    for parte in comando.split():
        try:
            partes.append(int(parte))
        except ValueError:
            partes.append(parte.upper())
    return partes



def jogar():
    perigos = [Perigo(nome) for nome in [
        'Boitatá', 'Curupira', 'Caipora',
        'Furna das Araras', 'Furna dos Andirás']]

    for perigo in perigos:
        escolher_casa_segura(casas).perigo = perigo

    for casa in casas.values():
        if casa.perigo:
            print(casa.número, casa.perigo)

    jogador = Jogador(escolher_casa_segura(casas))

    while True:
        print(f'Você está na casa {jogador.posição.número}.', end=' ')
        vizinhas = ', '.join(str(x) for x in jogador.posição.vizinhas)
        print(f'Casas vizinhas: {vizinhas}.')
        comando = analisar(input('Sua ação: '))
        match comando:
            case int(destino):
                jogador.andar(destino)
            case ['DRONE' | 'D', *caminho]:
                jogador.lançar_drone(caminho)
            case ['FIM' | 'F']:
                raise SystemExit()




if __name__ == '__main__':
    jogar()



