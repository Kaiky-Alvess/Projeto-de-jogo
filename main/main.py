import pygame

from pygame.locals import *
from sys import exit
from random import randint

from pygame.sprite import collide_rect

pygame.init()



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
menu= True

while menu==True:
    janela.fill((0,0,0))
    relogio.tick(240)
    clique_start=pygame.Rect(350,200,100,40)
    clique_sair=pygame.Rect(350,260,100,40)

    comeco=f'Start'
    texto_comeco=fonte.render(comeco, True, (255, 255, 255), (0, 0, 0))


    posicao_mouse=pygame.mouse.get_pos()

    if clique_start.collidepoint(posicao_mouse):
        start = fonte.render('Start', True, (155, 155, 155))
    else:
        start = fonte.render('Start', True, (255, 255, 255))

    if clique_sair.collidepoint(posicao_mouse):
        sair = fonte.render('Sair', True, (155, 155, 155))
    else:
        sair = fonte.render('Sair', True, (255, 255, 255))

    texto_start_rect = start.get_rect(center=clique_start.center)
    janela.blit(start, texto_start_rect)

    texto_sair_rect = sair.get_rect(center=clique_sair.center)
    janela.blit(sair, texto_sair_rect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if clique_start.collidepoint(event.pos):
                    menu=False
                elif clique_sair.collidepoint(event.pos):
                    pygame.quit()
    pygame.display.update()

pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load('../sons/Thunderstruck.mp3')
pygame.mixer.music.play()
barulho_acerto= pygame.mixer.Sound('../sons/coin.wav')


while pygame.mixer.music.get_busy():
    janela.fill((0,0,0))
    relogio.tick(240)
    mensagem= f'Pontos: {pontuacao}'

    texto= fonte.render(mensagem, True, (255,255,255), (0,0,0))



    nota = pygame.draw.rect(janela, (0, 255, 0), (x_verde, y_verde, 40, 40))
    seta_verde = pygame.draw.rect(janela, (0, 255, 0), (x_verde, 540, 40, 40))


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_w:
                if nota.colliderect(seta_verde):
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
