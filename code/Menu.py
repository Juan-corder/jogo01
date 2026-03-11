from tkinter.font import Font

import pygame.image
from pygame import Surface, Rect

from code.Const import WIN_WIDTH, MENU_OPTION


class Menu():
    def __init__(self, janela):
        self.janela = janela
        imagem_original = pygame.image.load('./Assets/city 1/10.png')  # este comando carrega a imagem do menu

        self.superficie = pygame.transform.smoothscale(imagem_original, (1080, 720))
        self.retangulo = self.superficie.get_rect(left=0, top=0)  # cria um retângulo para colocar a imagem sobre ele

    def executar(self):
        pygame.mixer.init()
        pygame.mixer_music.load('./Assets/Sons/Som do menu.mp3')
        pygame.mixer_music.play(-1)

        rodando = True
        while rodando:
            self.janela.blit(self.superficie, self.retangulo)
            self.texto_menu(70, "City", (255, 255, 0), (540, 200))
            self.texto_menu(80, "Striker", (255, 255, 0), (540, 270))

            for i, option in enumerate(MENU_OPTION):
                y_pos = 340 + i * 50
                self.texto_menu(30, option, (255, 255, 0), (540, y_pos))




            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rodando = False

    def texto_menu(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.janela.blit(text_surf, text_rect)
