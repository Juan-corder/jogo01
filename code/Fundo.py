from code.Entidade import Entidade
from code.Const import WIN_WIDTH, ENTIDADE_VELOCIDADE


class Fundo(Entidade):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.velocidade = -7

    def mover(self):
        # move para a esquerda
        self.retangulo.centerx -=  ENTIDADE_VELOCIDADE[self.name]

        if self.retangulo.right <= 0:
            self.retangulo.left = WIN_WIDTH





