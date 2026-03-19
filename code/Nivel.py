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

    def executar(self):
        while True:
            for ent in self.entidade_lista:
                self.janela.blit(source=ent.superficie, dest=ent.retangulo)
                ent.mover()
            pygame.display.flip()

