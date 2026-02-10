import random
from Classes.classe import *
import pygame
from Imgs import *
from Classes.spawnner import *
from pygame.locals import *
from sys import exit
from random import randint

from pygame.sprite import collide_rect

pygame.init()

#proporção da tela
largura=800
altura=600

fundo=pygame.image.load('../Imgs/Rockeiros.png')
fundo = pygame.transform.scale(fundo,(largura,altura))

seta_verde=Setas(janela,0,255,0,[240,540],(40,40))
seta_vermelha=Setas(janela,255,0,0,[320,540],(40,40))
seta_amarela=Setas(janela,255,255,0,[400,540],(40,40))

#fonte das mensagens
fonte=pygame.font.SysFont('comicsans', 30)

#Pontuação no jogo
pontuacao=0



#Geração de peças infinitas


#Janela
pygame.display.set_caption("Jogo")
janela=pygame.display.set_mode((largura,altura))



#Variavel que receberá os fps do jogo
relogio=pygame.time.Clock()

#Estado em que se encontra o jogo menu/play/fim de jogo
estado= 'menu_principal'

musica_atual=''
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load('../sons/menu-music.mp3')
pygame.mixer.music.play(-1)
#Loop principal
while estado=='menu_principal':
    #preencimento da tela
    janela.blit(fundo,(0,0))

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
        pygame.mixer.music.load('../sons/Thunderstruck.mp3')
        pygame.mixer.music.play()
        barulho_acerto= pygame.mixer.Sound('../sons/coin.wav')

        #Enquanto estiver tocando a música
        while pygame.mixer.music.get_busy():
            #limpar a tela
            janela.blit(fundo,(0,0))

            for i, nota in enumerate(gerenciador.notas):
                gerenciador.notas[i].atualizar()
                gerenciador.notas[i].cair()
                gerenciador.notas[i].criar_obj()
            gerenciador.atualizar()
            gerenciador.excluir()

            #fps
            relogio.tick(240)
            gerenciador.tempo_spawn += 1
            #Texto de pontuação
            mensagem= f'Pontos: {pontuacao}'

            texto= fonte.render(mensagem, True, (255,255,255), (0,0,0))


            seta_verde.criar_obj()
            seta_vermelha.criar_obj()
            seta_amarela.criar_obj()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_w:
                        for nota in gerenciador.notas:
                            if nota.pos[0]==240:
                                verde_mais_perto=nota
                                if verde_mais_perto is None or nota.pos[1] >verde_mais_perto.pos[1]:
                                    verde_mais_perto=nota
                                if verde_mais_perto.colisor.colliderect(seta_verde.colisor):
                                    verde_mais_perto.colidir()
                                    verde_mais_perto.atualizar()
                                    barulho_acerto.play()
                                    pontuacao += 1
                                    break
                        else:
                            pontuacao -= 1

                    if event.key == K_e:
                        for nota in gerenciador.notas:
                            if nota.pos[0]==320:
                                vermelho_mais_perto=nota
                                if vermelho_mais_perto is None or nota.pos[1] >vermelho_mais_perto.pos[1]:
                                    vermelho_mais_perto=nota
                                if vermelho_mais_perto.colisor.colliderect(seta_vermelha.colisor):
                                    vermelho_mais_perto.colidir()
                                    vermelho_mais_perto.atualizar()
                                    barulho_acerto.play()
                                    pontuacao += 1
                                    break
                        else:
                            pontuacao -= 1

                    if event.key == K_r:
                        for nota in gerenciador.notas:
                            if nota.pos[0]==400:
                                amarelo_mais_perto=nota
                                if amarelo_mais_perto is None or nota.pos[1] >amarelo_mais_perto.pos[1]:
                                    amarelo_mais_perto=nota
                                if amarelo_mais_perto.colisor.colliderect(seta_amarela.colisor):
                                    amarelo_mais_perto.colidir()
                                    amarelo_mais_perto.atualizar()
                                    barulho_acerto.play()
                                    pontuacao += 1
                        else:
                            pontuacao -= 1



            janela.blit(texto, (600, 20))

            pygame.display.update()
    #Tela final
    if not pygame.mixer.music.get_busy() and not estado=='menu_principal':
        estado='fim_de_jogo'
    if estado=='fim_de_jogo':
        while estado=='fim_de_jogo':
            #Limpar a tela
            janela.blit(fundo,(0,0))
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
