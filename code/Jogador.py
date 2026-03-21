import pygame

from code.Const import ENTIDADE_VELOCIDADE, WIN_HEIGHT, WIN_WIDTH, JOGADOR_BAIXO, JOGADOR_ESQUERDA, JOGADOR_DIREITA, \
    JOGADOR_CIMA
from code.Entidade import Entidade


class Jogador(Entidade):


    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.superficie = pygame.transform.scale(self.superficie, (64, 64))

        self.retangulo = self.superficie.get_rect(topleft=position)

    def mover(self):
        precionar_tecla = pygame.key.get_pressed()
        if precionar_tecla[JOGADOR_CIMA[self.name]] and self.retangulo.top > 0:
            self.retangulo.centery -=  ENTIDADE_VELOCIDADE[self.name]
        if precionar_tecla[JOGADOR_BAIXO[self.name]] and self.retangulo.bottom < WIN_HEIGHT:
            self.retangulo.centery +=  ENTIDADE_VELOCIDADE[self.name]
        if precionar_tecla[JOGADOR_ESQUERDA[self.name]] and self.retangulo.left > 0:
            self.retangulo.centerx -=  ENTIDADE_VELOCIDADE[self.name]
        if precionar_tecla[JOGADOR_DIREITA[self.name]] and self.retangulo.right < WIN_WIDTH:
            self.retangulo.centerx += ENTIDADE_VELOCIDADE[self.name]


    def update(self):
        pass
