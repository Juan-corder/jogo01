import pygame

from code.Const import ENTIDADE_VELOCIDADE, WIN_WIDTH
from code.Entidade import Entidade


class Inimigos(Entidade):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.superficie = pygame.transform.scale(self.superficie, (84, 84))

        self.retangulo = self.superficie.get_rect(topleft=position)



    def mover(self):
        self.retangulo.centerx -= ENTIDADE_VELOCIDADE[self.name]
        if self.retangulo.right <= 0:
            self.retangulo.left = WIN_WIDTH
