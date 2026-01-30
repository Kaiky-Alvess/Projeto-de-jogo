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
    
    y_verde+=1
    y_vermelho+=1
    if y_verde>=600:
        y_verde=0
    pygame.display.update()


