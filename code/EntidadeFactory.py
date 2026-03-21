from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Fundo import Fundo
from code.Jogador import Jogador


class EntidadeFactory():
    def __init__(self):
        pass

    @staticmethod
    def pegar_entidade(entidade_name: str, position=(0, 0)):
        match entidade_name:
            case 'Level1bg':
                list_bg = []
                for i in range(1, 10):
                    if i == 7:
                        continue
                    list_bg.append(Fundo(f'Level1bg{i}', (0, 0)))
                    list_bg.append(Fundo(f'Level1bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Jogador1':
                return Jogador('Jogador1', (10, WIN_HEIGHT / 2 - 30))
            case 'Jogador2':
                return Jogador('Jogador2', (10, WIN_HEIGHT / 2 + 30))
