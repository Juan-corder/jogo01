import sys
import pygame

from code.Const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION
from code.Menu import Menu
from code.Nivel import Nivel
from code.Comandos import TelaComandos

class Jogo:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.janela = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("City")

    def executar(self):
        while True:
            menu = Menu(self.janela)
            menu_return = menu.executar()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1]]:
                nivel = Nivel(self.janela, 'Nível 1', menu_return)
                nivel.executar()

            elif menu_return == MENU_OPTION[2]:
                tela_comandos = TelaComandos(self.janela)
                tela_comandos.executar()

            elif menu_return == MENU_OPTION[3]:
                pygame.quit()
                quit()