import pygame
from code.Const import ENTIDADE_VELOCIDADE, WIN_WIDTH, WIN_HEIGHT
from code.Entidade import Entidade

class Inimigos(Entidade):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        # Redimensiona a imagem para 84x84
        self.superficie = pygame.transform.scale(self.superficie, (84, 84))
        rect_img = self.superficie.get_rect(topleft=position)

        # Hitbox menor (50%)
        hitbox_width = int(rect_img.width * 0.5)
        hitbox_height = int(rect_img.height * 0.5)

        self.retangulo = pygame.Rect(
            rect_img.x + (rect_img.width - hitbox_width) // 2,
            rect_img.y + (rect_img.height - hitbox_height) // 2,
            hitbox_width,
            hitbox_height
        )

        # velocidade inicial negativa → entra pela direita e anda para a esquerda
        self.velocidade_x = -ENTIDADE_VELOCIDADE.get(name, 2)
        self.velocidade_y = 0

    def mover(self):
        # movimento horizontal
        self.retangulo.x += self.velocidade_x

        # quando sair pela esquerda, reaparece na direita
        if self.retangulo.right < 0:
            self.retangulo.left = WIN_WIDTH + 10

        # garantir que não ultrapasse topo ou fundo
        if self.retangulo.top < 0:
            self.retangulo.top = 0
        if self.retangulo.bottom > WIN_HEIGHT:
            self.retangulo.bottom = WIN_HEIGHT

    def update(self):
        self.mover()