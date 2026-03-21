from code.Const import MENU_OPTION
from code.EntidadeFactory import EntidadeFactory
import pygame
from code.Entidade import Entidade  # importante importar para usar na anotação

class Nivel:
    def __init__(self, janela, name, game_mode):
        self.janela = janela
        self.name = name
        self.game_mode = game_mode

        # Lista de entidades do nível
        self.entidade_lista: list[Entidade] = []
        self.entidade_lista.extend(EntidadeFactory.pegar_entidade('Level1bg'))
        self.entidade_lista.append(EntidadeFactory.pegar_entidade('Jogador1'))
        if game_mode in [MENU_OPTION[1]]:
            self.entidade_lista.append(EntidadeFactory.pegar_entidade('Jogador2'))

    def executar(self):
        pygame.mixer_music.load(f'./Assets/Sons/Som da fase 1.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entidade_lista:
                self.janela.blit(source=ent.superficie, dest=ent.retangulo)
                ent.mover()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

            pygame.display.flip()

