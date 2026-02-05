import random
from Notas.Classe import *
import pygame

from pygame.locals import *
from sys import exit
from random import randint

from pygame.sprite import collide_rect

pygame.init()


#proporção da tela
largura=800
altura=600



#fonte das mensagens
fonte=pygame.font.SysFont('comicsans', 30)

#Pontuação no jogo
pontuacao=0



#Geração de peças infinitas
proxima_aparicao=randint(10,50)

#Janela
pygame.display.set_caption("Jogo")
janela=pygame.display.set_mode((largura,altura))

#Variavel que receberá os fps do jogo
relogio=pygame.time.Clock()

#Estado em que se encontra o jogo menu/play/fim de jogo
estado= 'menu_principal'

#Notas e setas
nota_verde = Notas(janela, 0, 255, 0, 1, [240, 0], (40, 40))
seta_verde = Setas(janela, 0, 255, 0, [240, 540], (40, 40))

nota_vermelha=Notas(janela, 255, 0, 0, 1,[320, 0], (40, 40))
seta_vermelha=Setas(janela, 255, 0, 0, [320, 540], (40, 40))

nota_amarela=Notas(janela,255,255,0,1,[400,0], (40, 40))
seta_amarela=Setas(janela,255,255,0,[400,540], (40, 40))

#Loop principal
while estado=='menu_principal':
    #preencimento da tela
    janela.fill((0,0,0))

    #frames por segundo
    relogio.tick(240)

    #botões de start e sair
    clique_start=pygame.Rect(350,200,100,40)
    clique_sair=pygame.Rect(350,260,100,40)
    comeco=f'Start'
    texto_comeco=fonte.render(comeco, True, (255, 255, 255), (0, 0, 0))

    #pegar a posição do mouse para inserir clicks
    posicao_mouse=pygame.mouse.get_pos()

    #colisão sobre os botões
    if clique_start.collidepoint(posicao_mouse):
        start = fonte.render('Start', True, (155, 155, 155))
    else:
        start = fonte.render('Start', True, (255, 255, 255))

    if clique_sair.collidepoint(posicao_mouse):
        sair = fonte.render('Sair', True, (155, 155, 155))
    else:
        sair = fonte.render('Sair', True, (255, 255, 255))

    #mostrar botões
    texto_start_rect = start.get_rect(center=clique_start.center)
    janela.blit(start, texto_start_rect)

    texto_sair_rect = sair.get_rect(center=clique_sair.center)
    janela.blit(sair, texto_sair_rect)

    #Verificador de eventos e de clicks
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if clique_start.collidepoint(event.pos):
                    estado='play'
                elif clique_sair.collidepoint(event.pos):
                    pygame.quit()

    #update da tela
    pygame.display.update()

    #Loop da música
    if estado=='play':
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.load('../sons/Thunderstruck.mp3')
        pygame.mixer.music.play()
        barulho_acerto= pygame.mixer.Sound('../sons/coin.wav')

        #Enquanto estiver tocando a música
        while pygame.mixer.music.get_busy():
            #limpar a tela
            janela.fill((0,0,0))

            #fps
            relogio.tick(240)

            #Texto de pontuação
            mensagem= f'Pontos: {pontuacao}'

            texto= fonte.render(mensagem, True, (255,255,255), (0,0,0))


            #Notas e setas
            nota_verde.criar_obj()
            nota_vermelha.criar_obj()
            nota_amarela.criar_obj()

            nota_verde.atualizar()
            nota_vermelha.atualizar()
            nota_amarela.atualizar()

            nota_verde.cair()
            nota_vermelha.cair()
            nota_amarela.cair()

            seta_verde.criar_obj()
            seta_vermelha.criar_obj()
            seta_amarela.criar_obj()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_w:
                        if nota_verde.colisor.colliderect(seta_verde.colisor):
                            nota_verde.colidir()
                            nota_verde.atualizar()
                            barulho_acerto.play()
                            pontuacao += 1
                        else:
                            pontuacao -= 1
                            nota_verde.pos[1]=600
                            nota_verde.atualizar()
                    if event.key == K_e:
                        if nota_vermelha.colisor.colliderect(seta_vermelha.colisor):
                            nota_vermelha.colidir()
                            nota_vermelha.atualizar()
                            barulho_acerto.play()
                            pontuacao += 1
                        else:
                            pontuacao -= 1
                            nota_vermelha.pos[1] = 600
                            nota_vermelha.atualizar()
                    if event.key == K_r:
                        if nota_amarela.colisor.colliderect(seta_amarela.colisor):
                            nota_amarela.colidir()
                            nota_amarela.atualizar()
                            barulho_acerto.play()
                            pontuacao += 1
                        else:
                            pontuacao -= 1
                            nota_amarela.pos[1] = 600
                            nota_amarela.atualizar()


            janela.blit(texto, (600, 20))

            pygame.display.update()
    #Tela final
    if not pygame.mixer.music.get_busy() and not estado=='menu_principal':
        estado='fim_de_jogo'
    if estado=='fim_de_jogo':
        while estado=='fim_de_jogo':
            #Limpar a tela
            janela.fill((0, 0, 0))
            relogio.tick(240)
            #Textos de pontuação e fim de jogo
            mensagem= f'Pontuação final: {pontuacao}'
            game_over = f'Fim de jogo'

            texto_final = fonte.render(game_over, True, (255, 255, 255), (0, 0, 0))
            texto= fonte.render(mensagem, True, (255, 255, 255), (0, 0, 0))
            #Mostrar os textos
            janela.blit(texto_final, (largura/2-100, altura/2-100,))
            janela.blit(texto, (largura/2-145, altura/2-50))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

            pygame.display.update()
