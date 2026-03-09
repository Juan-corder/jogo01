from tkinter.font import Font

import pygame.image

from code.Const import WIN_HEIGHT


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
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rodando = False



