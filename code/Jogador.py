import pygame
from code.Const import ENTIDADE_VELOCIDADE, WIN_HEIGHT, WIN_WIDTH, JOGADOR_BAIXO, JOGADOR_ESQUERDA, JOGADOR_DIREITA, JOGADOR_CIMA
from code.Entidade import Entidade

class Jogador(Entidade):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        # Redimensiona a imagem para 64x64 (visual)
        self.superficie = pygame.transform.scale(self.superficie, (64, 64))

        # Rect da imagem
        rect_img = self.superficie.get_rect(topleft=position)

        # Hitbox menor (70% da largura e altura)
        hitbox_width = int(rect_img.width * 0.5)
        hitbox_height = int(rect_img.height * 0.5)

        # Centraliza a hitbox dentro da imagem
        self.retangulo = pygame.Rect(
            rect_img.x + (rect_img.width - hitbox_width) // 2,
            rect_img.y + (rect_img.height - hitbox_height) // 2,
            hitbox_width,
            hitbox_height
        )

    def mover(self):
        precionar_tecla = pygame.key.get_pressed()
        if precionar_tecla[JOGADOR_CIMA[self.name]] and self.retangulo.top > 0:
            self.retangulo.centery -= ENTIDADE_VELOCIDADE[self.name]
        if precionar_tecla[JOGADOR_BAIXO[self.name]] and self.retangulo.bottom < WIN_HEIGHT:
            self.retangulo.centery += ENTIDADE_VELOCIDADE[self.name]
        if precionar_tecla[JOGADOR_ESQUERDA[self.name]] and self.retangulo.left > 0:
            self.retangulo.centerx -= ENTIDADE_VELOCIDADE[self.name]
        if precionar_tecla[JOGADOR_DIREITA[self.name]] and self.retangulo.right < WIN_WIDTH:
            self.retangulo.centerx += ENTIDADE_VELOCIDADE[self.name]

    def update(self):
        pass