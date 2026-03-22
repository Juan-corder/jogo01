import random
from random import choice
import pygame
from code.Const import MENU_OPTION, EVENTO_INIMIGO, ENTIDADE_VELOCIDADE, WIN_WIDTH, WIN_HEIGHT
from code.EntidadeFactory import EntidadeFactory
from code.Entidade import Entidade
from code.Inimigos import Inimigos

class Nivel:
    def __init__(self, janela, name, game_mode):
        self.janela = janela
        self.name = name
        self.game_mode = game_mode
        self.vidas = 3
        self.tempo_inicio = pygame.time.get_ticks()

        self.entidade_lista: list[Entidade] = []
        self.entidade_lista.extend(EntidadeFactory.pegar_entidade('Level1bg'))
        self.jogador1 = EntidadeFactory.pegar_entidade('Jogador1')
        self.entidade_lista.append(self.jogador1)

        if game_mode in [MENU_OPTION[1]]:
            self.jogador2 = EntidadeFactory.pegar_entidade('Jogador2')
            self.entidade_lista.append(self.jogador2)

        pygame.time.set_timer(EVENTO_INIMIGO, 2000)
        self.font = pygame.font.SysFont("Arial", 28)

    def executar(self):
        pygame.mixer_music.load('./Assets/Sons/Som da fase 1.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            self.janela.fill((0, 0, 0))

            # desenha entidades
            for ent in self.entidade_lista:
                self.janela.blit(ent.superficie, ent.retangulo)

                if isinstance(ent, Inimigos):
                    ent.update()   # inimigos se movem automaticamente
                else:
                    ent.mover()    # jogadores dependem do teclado

            # contador de vidas
            vidas_text = self.font.render(f"Vidas: {self.vidas}", True, (255, 0, 0))
            self.janela.blit(vidas_text, (10, 10))

            # colisão com inimigos
            for ent in self.entidade_lista:
                if isinstance(ent, Inimigos):
                    if self.jogador1.retangulo.colliderect(ent.retangulo):
                        self.vidas -= 1
                        self.entidade_lista.remove(ent)
                        if self.vidas <= 0:
                            self.game_over()

            # eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENTO_INIMIGO:
                    novo_inimigo = EntidadeFactory.pegar_entidade(choice(('Inimigo1', 'Inimigo2')))
                    self.entidade_lista.append(novo_inimigo)

            # aumenta dificuldade a cada 15s
            tempo_passado = (pygame.time.get_ticks() - self.tempo_inicio) // 1000
            if tempo_passado % 15 == 0 and tempo_passado > 0:
                if ENTIDADE_VELOCIDADE['Inimigo1'] < 6:
                    ENTIDADE_VELOCIDADE['Inimigo1'] += 0.2
                if ENTIDADE_VELOCIDADE['Inimigo2'] < 7:
                    ENTIDADE_VELOCIDADE['Inimigo2'] += 0.2

            pygame.display.flip()

    def game_over(self):
        self.janela.fill((0, 0, 0))
        text = self.font.render("GAME OVER", True, (255, 0, 0))
        rect = text.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
        self.janela.blit(text, rect)
        pygame.display.flip()
        pygame.time.delay(3000)

        from code.Menu import Menu
        menu = Menu(self.janela)
        opcao = menu.executar()
        from code.Nivel import Nivel
        nivel = Nivel(self.janela, "Nível 1", opcao)
        nivel.executar()