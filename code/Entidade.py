from abc import ABC, abstractmethod
import pygame.image
import pygame.transform

class Entidade(ABC):
    def __init__(self, name: str, position: tuple, janela_size=(1080, 720)):
        self.name = name
        # Carrega a imagem
        self.superficie = pygame.image.load('./Assets/' + name + '.png').convert_alpha()

        # Redimensiona a imagem para caber na janela
        self.superficie = pygame.transform.scale(self.superficie, janela_size)

        # Define o retângulo de posicionamento
        self.retangulo = self.superficie.get_rect(left=position[0], top=position[1])

        # Velocidade inicial
        self.velocidade = 0

    @abstractmethod
    def mover(self):
        pass