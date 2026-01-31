import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load('Thunderstruck.mp3')
pygame.mixer.music.play()

barulho_acerto= pygame.mixer.Sound('coin.wav')
largura=800
altura=600
x_verde=240
y_verde=0

fonte=pygame.font.SysFont('comicsans', 30)

pontuacao=0

proxima_aparicao=randint(10,50)

pygame.display.set_caption("Jogo")

janela=pygame.display.set_mode((largura,altura))
relogio=pygame.time.Clock()
while pygame.mixer.music.get_busy():
    janela.fill((0,0,0))
    relogio.tick(240)
    mensagem= f'Pontos: {pontuacao}'

    texto= fonte.render(mensagem, True, (255,255,255), (0,0,0))



    nota = pygame.draw.rect(janela, (0, 255, 0), (x_verde, y_verde, 40, 40))
    seta = pygame.draw.rect(janela, (0, 255, 0), (x_verde, 540, 40, 40))


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_w:
                if nota.colliderect(seta):
                    barulho_acerto.play()
                    pontuacao += 1
                    y_verde=0
                    y_verde-=proxima_aparicao
                else:
                    pontuacao -= 1
                    y_verde = 0 - proxima_aparicao


    y_verde+=1
    if y_verde>=600:
        y_verde=0
        pontuacao-=1

    janela.blit(texto, (600, 20))

    pygame.display.update()
while True:
    janela.fill((0, 0, 0))
    relogio.tick(240)
    mensagem= f'Pontuação final: {pontuacao}'
    game_over = f'Fim de jogo'

    texto_final = fonte.render(game_over, True, (255, 255, 255), (0, 0, 0))
    texto= fonte.render(mensagem, True, (255, 255, 255), (0, 0, 0))

    janela.blit(texto_final, (largura/2-100, altura/2-100,))
    janela.blit(texto, (largura/2-145, altura/2-50))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
