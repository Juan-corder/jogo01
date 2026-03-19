from code.Entidade import Entidade


class Fundo(Entidade):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)




    def mover(self):
        self.retangulo.centerx -= 1
        pass




