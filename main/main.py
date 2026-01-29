import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura=800
altura=600
x_verde=240
y_verde=0
y_vermelho=0
y_amarelo=0
y_azul=0
y_laranja=0
pontuacao=0

proxima_aparicao=randint(10,50)

pygame.display.set_caption("Jogo")

janela=pygame.display.set_mode((largura,altura))
relogio=pygame.time.Clock()
while True:
    janela.fill((0,0,0))
    relogio.tick(240)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    circ_verde=pygame.draw.circle(janela,(0,255,0),(x_verde,y_verde),20)
    circ_vermelho=pygame.draw.circle(janela,(255,0,0),(320,y_vermelho),20)
    circ_amarelo=pygame.draw.circle(janela,(255,255,0),(400,500),20)
    circ_azul=pygame.draw.circle(janela,(0,0,255),(480,500),20)
    circ_laranja=pygame.draw.circle(janela,(255,150,0),(560,500),20)
    seta_verde=pygame.draw.polygon(janela, (0, 255, 0), [(220, 500), (240, 450), (260, 500)])
    seta_vermelha=pygame.draw.polygon(janela, (255, 0, 0), [(300, 500), (320, 450), (340, 500)])


    if pygame.key.get_pressed()[K_w]:
        seta_verde=pygame.draw.polygon(janela, (0, 150, 0), [(220, 500), (240, 450), (260, 500)])
        if circ_verde.collidepoint(240,500):
            pontuacao+=1
            y_verde=0
            print(pontuacao)
            proxima_aparicao = randint(10, 50)
        else:
            pontuacao-=1
            y_verde-=proxima_aparicao
            proxima_aparicao = randint(10, 50)
    if pygame.key.get_pressed()[K_a]:
       seta_vermelha = pygame.draw.polygon(janela, (150, 0, 0), [(300, 500), (320, 450), (340, 500)])
       if circ_vermelho.collidepoint(320, 500):
           pontuacao += 1
           y_vermelho = 0
           print(pontuacao)
           proxima_aparicao = randint(10, 50)
       else:
           pontuacao -= 1
           y_vermelho -= proxima_aparicao
           proxima_aparicao = randint(10, 50)
    y_verde+=1
    y_vermelho+=1
    if y_verde>=600:
        y_verde=0
    pygame.display.update()


