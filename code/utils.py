import sys, os, pygame

def resource_path(relative_path):
    """Retorna o caminho correto do arquivo, mesmo dentro do .exe"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(relative_path)

def load_image(path):
    """Carrega imagem já com o caminho ajustado"""
    return pygame.image.load(resource_path(path)).convert_alpha()

def load_sound(path):
    """Carrega som já com o caminho ajustado"""
    return pygame.mixer.Sound(resource_path(path))