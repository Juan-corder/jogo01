from code.Fundo import Fundo


class EntidadeFactory():
    def __init__(self):
        pass

    @staticmethod
    def pegar_entidade(entidade_name: str, position=(0, 0)):
        match entidade_name:
            case 'Level1bg':
                list_bg = []
                for i in [1, 2, 3, 4, 5, 6, 8, 9]:
                    list_bg.append(Fundo(f'Level1bg{i}', (0, 0)))
                return list_bg
