import pygame

WIN_WIDTH = 1080
WIN_HEIGHT = 720

MENU_OPTION = ('NOVO JOGO 1P',
               'NOVO JOGO 2P COOPERATIVO',
               'LISTA DE COMANDOS',
               'RECORDE',
               'SAIR')


LISTA_COMANDOS = {
    "Jogador 1": {
        "Mover para cima": "↑",
        "Mover para baixo": "↓",
        "Mover para esquerda": "←",
        "Mover para direita": "→"
    },
    "Jogador 2": {
        "Mover para cima": "W",
        "Mover para baixo": "S",
        "Mover para esquerda": "A",
        "Mover para direita": "D"
    }
}



ENTIDADE_VELOCIDADE = {
    'Level1bg1': 0,
    'Level1bg2': 1,
    'Level1bg3': 2,
    'Level1bg4': 3,
    'Level1bg5': 4,
    'Level1bg6': 5,
    'Level1bg8': 6,
    'Level1bg9': 7,
    'Jogador1': 2,
    'Jogador2': 3,
    'Inimigo1': 5,
    'Inimigo2': 5,
}

JOGADOR_CIMA = {'Jogador1': pygame.K_UP,
                'Jogador2': pygame.K_w}

JOGADOR_BAIXO = {'Jogador1': pygame.K_DOWN,
                 'Jogador2': pygame.K_s}

JOGADOR_ESQUERDA = {'Jogador1': pygame.K_LEFT,
                    'Jogador2': pygame.K_a}

JOGADOR_DIREITA = {'Jogador1': pygame.K_RIGHT,
                   'Jogador2': pygame.K_d}

JOGADOR_TIRO = {'Jogador1': pygame.K_RCTRL,
                'Jogador2': pygame.K_LCTRL}

EVENTO_INIMIGO = pygame.USEREVENT + 1





