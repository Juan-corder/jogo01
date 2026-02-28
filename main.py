import pygame

pygame.init()  # comando que inicia os recursos do pygame
janela = pygame.display.set_mode(size=(600, 480))  # criei uma variável que recebe o comando set que inicializa a janela
# Abaixo irei criar um loop para que a janela fique aberta sempre
while True:

    # Agora eu vou checar todos os eventos que ocorrem como tocar em uma tecla, mouse e etc..
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # ira checar se o evento de fechar a janela foi feito
            pygame.quit()  # ou seja quando eu apetar em fechar a janela esse comando é ativado o comando de fechar a janela pygame.quit
            quit()  # comando que fecha o pygame após o fechamento da janela
