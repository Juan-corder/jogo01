import pygame


from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Menu import Menu



class Jogo:
    def __init__(self):




        pygame.init()
        pygame.font.init()
        self.janela = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # estou criando a janela do jogo com essas dimensões
        pygame.display.set_caption("City")

    def executar(self):




            menu = Menu(self.janela)
            menu.executar()




