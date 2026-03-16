from code import Entidade


class Nivel():
    def __init__(self, janela, name, game_mode):
        self.janela = janela
        self.name = name
        self.game_mode = game_mode
        self.entidade_lista = list[Entidade] = []

    def executar(self):
        pass
