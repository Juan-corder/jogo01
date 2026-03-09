from code.Menu import Menu

import pygame

class Jogo:
    def __init__(self):




        pygame.init()
        self.janela = pygame.display.set_mode(size=(800, 600))  # estou criando a janela do jogo com essas dimensões

    def executar(self):


        while True:
            menu = Menu(self.janela)
            menu.executar()

            pass
            #for event in pygame.event.get(): # é para ele verificar qualquer tipo de evento como tocar no teclado
             #   if event.type == pygame.QUIT: # verifica se você clicou em fechar a janela
              #      pygame.quit() # esse é comando que fecha a janela caso voce tenha apertado
               #     quit() # encerramento
