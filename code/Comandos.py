import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, LISTA_COMANDOS

class TelaComandos:
    def __init__(self, janela):
        self.janela = janela
        self.font_titulo = pygame.font.SysFont("Arial", 36)
        self.font_texto = pygame.font.SysFont("Arial", 24)

    def executar(self):
        rodando = True
        clock = pygame.time.Clock()

        while rodando:
            clock.tick(60)
            self.janela.fill((0, 0, 0))

            # Guia rápido das regras
            titulo = self.font_titulo.render("Guia Rápido das Regras", True, (255, 255, 0))
            self.janela.blit(titulo, (WIN_WIDTH // 2 - titulo.get_width() // 2, 40))

            regras = [
                "1. Evite colidir com os inimigos.",
                "2. Você tem 3 vidas.",
                "3. O jogo termina quando todas as vidas acabam.",
                "4. Use os comandos abaixo para se mover."
            ]

            y_offset = 100
            for regra in regras:
                texto = self.font_texto.render(regra, True, (255, 255, 255))
                self.janela.blit(texto, (50, y_offset))
                y_offset += 30

            # Lista de comandos
            comandos_titulo = self.font_titulo.render("Lista de Comandos", True, (0, 255, 0))
            self.janela.blit(comandos_titulo, (WIN_WIDTH // 2 - comandos_titulo.get_width() // 2, y_offset + 20))

            y_offset += 70
            for nome, tecla in LISTA_COMANDOS.items():
                texto = self.font_texto.render(f"{nome}: {tecla}", True, (200, 200, 200))
                self.janela.blit(texto, (50, y_offset))
                y_offset += 30

            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # ESC volta ao menu
                        rodando = False

            pygame.display.flip()