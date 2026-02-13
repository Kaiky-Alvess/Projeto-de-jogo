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
mapa = [(800,240), (912,240),(1024,240), (1136,240), (1248,240), (1360,240), (1472,240), (1584,240), (1696,320), (1808,240), (1920,240), (2032,240), (2144,240), (2256,240), (2368,400), (2480,240), (2592,240), (2704,240), (2816,240), (2928,240), (3040,480), (3152,240), (3264,240), (3376,240), (3488,240), (3600,240), (3712,320), (3824,240), (3936,240), (4048,240), (4160,240), (4272,240), (4384,240), (4496,240), (4608,240), (4720,240), (4832,240), (4944,240), (5056,320), (5168,240), (5280,240), (5392,240), (5504,400), (5616,240), (5728,240), (5840,240), (5952,480), (6064,240), (6176,240), (6288,240), (6400,320), (6512,400), (6624,240), (6736,320), (6848,480), (6960,240), (7072,400), (7184,240), (7296,320), (7408,240), (7520,480), (7632,240), (7744,400), (7856,240), (7968,320), (8080,240), (8192,240), (8304,240), (8416,320), (8528,240), (8640,400), (8752,240), (8864,320), (8976,240), (9088,480), (9200,240), (9312,400), (9424,240), (9536,320), (9648,400), (9760,480), (9872,240), (9984,320), (10096,240), (10208,400), (10320,240), (10432,480), (10544,320), (10656,240), (10768,400), (10880,240), (10992,320), (11104,240), (11216,480), (11328,240), (11440,320), (11552,240), (11632,400), (11712,480), (11824,240), (11936,320), (12016,400), (12096,240), (12208,320), (12320,240), (12400,480), (12480,400), (12560,320), (12672,240), (12784,320), (12896,240), (13008,240), (13120,320), (13232,240), (13232,400), (13312,480), (13392,320), (13504,240), (13616,320), (13672,400), (13728,480), (13784,240), (13784,320), (13896,400), (13976,320), (14056,240), (14168,240), (14280,320), (14392,240), (14472,480), (14552,400), (14632,320), (14712,240), (14824,240), (14936,320), (15048,240), (15048,400), (15128,480), (15208,320), (15320,240), (15432,320), (15512,480), (15592,400), (15672,320), (15784,240), (15896,240), (15952,320), (16008,400), (16064,240), (16064,480), (16176,240), (16256,320), (16336,400), (16416,480), (16528,240), (16640,320), (16752,240), (16864,240), (16976,240), (17088,320), (17200,240), (17312,400), (17424,240), (17536,320), (17648,240), (17760,240), (17872,240), (17984,240), (18096,240), (18208,320), (18320,240), (18432,400), (18544,240), (18656,480), (18768,320), (18880,240), (18992,240), (19104,320), (19216,240), (19328,400), (19440,240), (19440,480), (19552,320), (19664,240), (19776,400), (19888,240), (20000,320), (20112,400), (20224,240), (20336,480), (20448,320), (20560,240), (20672,400), (20784,240), (20896,320), (20896,480), (21008,240), (21120,400), (21232,320), (21344,240), (21456,240), (21568,320), (21680,400), (21792,480), (21904,240), (21904,400), (22016,320), (22128,240), (22240,480), (22352,320), (22464,240), (22576,320), (22688,240), (22800,400), (22912,240), (23024,320), (23136,240), (23248,480), (23328,320), (23408,400), (23520,240), (23632,320), (23632,480), (23744,240), (23856,400), (23936,480), (24016,320), (24128,240), (24240,240), (24352,240), (24464,320), (24576,240), (24688,400), (24800,240), (24912,320), (25024,240), (25136,240), (25248,320), (25360,240), (25472,400), (25584,240), (25696,320), (25808,240), (25920,480), (26032,320), (26144,400), (26256,240), (26368,480), (26480,320), (26592,240), (26704,400), (26816,240), (26896,480), (26976,320), (27088,240), (27200,400), (27312,320), (27424,240), (27536,320), (27648,400), (27760,480), (27872,240), (27872,480), (27984,320), (28096,240), (28208,400), (28320,240), (28432,320), (28544,240), (28656,480), (28768,320), (28848,400), (28928,320), (29040,240), (29152,480), (29264,240), (29376,320), (29488,400), (29600,240), (29712,480), (29824,320), (29936,240), (30048,400), (30160,320), (30160,400), (30272,240), (30384,480), (30496,320), (30608,240), (30720,240), (30832,320), (30944,400), (31056,480), (31136,320), (31216,240), (31328,400), (31440,320), (31552,240), (31552,400), (31664,480), (31776,320), (31888,240), (32000,400), (32080,320), (32160,240), (32272,480), (32384,400), (32464,320), (32544,240), (32656,400), (32768,480), (32880,320), (32880,480), (32992,240), (33104,400), (33216,240), (33296,320), (33376,400), (33456,480), (33568,320), (33680,240), (33760,400), (33840,320), (33920,240), (34032,480), (34144,240), (34144,320), (34256,400), (34368,240), (34480,480), (34560,400), (34640,320), (34720,240), (34832,320), (34944,400), (35000,480), (35056,320), (35168,240), (35280,400), (35360,320), (35440,240), (35520,480), (35600,400), (35712,240), (35824,240), (35936,240), (36048,320), (36160,240), (36272,400), (36384,240), (36496,320), (36608,240), (36720,240), (36832,320), (36944,240), (37056,480), (37168,240), (37280,320), (37392,400), (37504,480), (37616,240), (37616,480), (37728,320), (37840,400), (37952,240), (38032,480), (38112,320), (38192,240), (38304,400), (38416,320), (38528,240), (38640,320), (38640,400), (38752,480), (38864,240), (38976,240), (39088,320), (39200,400), (39312,480), (39424,240), (39536,320), (39648,240), (39760,400), (39840,480), (39920,320), (40032,240), (40144,400), (40256,320), (40368,240), (40448,320), (40528,400), (40608,480), (40720,240), (40832,320), (40912,400), (40992,480), (41104,240), (41216,320), (41328,400), (41440,240), (41440,480), (41552,320), (41664,240), (41776,240), (41888,240), (42000,240), (42112,240), (42224,320), (42336,320), (42448,480), (42560,400), (42672,240), (42784,240)]


#proporção da tela
largura=800
altura=600

janela=pygame.display.set_mode((largura,altura))
gerenciador=Gerenciador(janela)


fundo=pygame.image.load('../Imgs/Rockeiros.png')
fundo = pygame.transform.scale(fundo,(largura,altura))



seta_verde=Setas(janela,0,255,0,[240,540],(40,40))
seta_vermelha=Setas(janela,255,0,0,[320,540],(40,40))
seta_amarela=Setas(janela,255,255,0,[400,540],(40,40))
seta_azul=Setas(janela,0,255,255,[480,540],(40,40))

#fonte das mensagens
fonte=pygame.font.SysFont('comicsans', 30)

#Pontuação no jogo
pontuacao=0
linha_acerto = 540
janela_acerto = 40



#Geração de peças infinitas


#Janela
pygame.display.set_caption("Jogo")




#Variavel que receberá os fps do jogo
relogio=pygame.time.Clock()

#Estado em que se encontra o jogo menu/play/fim de jogo
estado= 'menu_principal'

musica_atual=''
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load('../sons/menu-music.mp3')
pygame.mixer.music.play(-1)
def tempo_atual():
    return pygame.time.get_ticks()-inicio_musica
indice_mapa = 0
SPAWN_DELAY = 1500

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
        inicio_musica = pygame.time.get_ticks()
        barulho_acerto= pygame.mixer.Sound('../sons/coin.wav')

        #Enquanto estiver tocando a música
        while pygame.mixer.music.get_busy():
            #limpar a tela
            janela.blit(fundo,(0,0))
            tempo = tempo_atual()
            while indice_mapa < len(mapa) and mapa[indice_mapa][0] - SPAWN_DELAY <= tempo:

                tempo_nota, coluna = mapa[indice_mapa]

                gerenciador.spawnar_nota(coluna)

                indice_mapa += 1

            for i, nota in enumerate(gerenciador.notas):
                gerenciador.notas[i].atualizar()
                gerenciador.notas[i].cair()
                gerenciador.notas[i].criar_obj()

            gerenciador.excluir()

            #fps
            relogio.tick(240)

            #Texto de pontuação
            mensagem= f'Pontos: {pontuacao}'

            texto= fonte.render(mensagem, True, (255,255,255))


            seta_verde.criar_obj()
            seta_vermelha.criar_obj()
            seta_amarela.criar_obj()
            seta_azul.criar_obj()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_a:
                        nota_certa = None
                        for nota in gerenciador.notas:
                            if nota.pos[0] == 240:
                                distancia = abs(nota.pos[1] - linha_acerto)
                                if distancia <= janela_acerto:
                                    nota_certa = nota
                                    break
                        if nota_certa:
                            pontuacao += 1
                            barulho_acerto.play()
                            gerenciador.notas.remove(nota_certa)
                        else:
                            pontuacao -= 1

                    if event.key == K_w:
                        nota_certa = None
                        for nota in gerenciador.notas:
                            if nota.pos[0] ==320:
                                distancia = abs(nota.pos[1] - linha_acerto)
                                if distancia <= janela_acerto:
                                    nota_certa = nota
                                    break
                        if nota_certa:
                            pontuacao += 1
                            barulho_acerto.play()
                            gerenciador.notas.remove(nota_certa)
                        else:
                            pontuacao -= 1

                    if event.key == K_s:
                        nota_certa = None
                        for nota in gerenciador.notas:
                            if nota.pos[0] == 400:
                                distancia = abs(nota.pos[1] - linha_acerto)
                                if distancia <= janela_acerto:
                                    nota_certa = nota
                                    break
                        if nota_certa:
                            pontuacao += 1
                            barulho_acerto.play()
                            gerenciador.notas.remove(nota_certa)
                        else:
                            pontuacao -= 1


                    if event.key == K_d:
                        nota_certa = None
                        for nota in gerenciador.notas:
                            if nota.pos[0] == 480:
                                distancia = abs(nota.pos[1] - linha_acerto)
                                if distancia <= janela_acerto:
                                    nota_certa = nota
                                    break
                        if nota_certa:
                            pontuacao += 1
                            barulho_acerto.play()
                            gerenciador.notas.remove(nota_certa)
                        else:
                            pontuacao -= 1
            for nota in gerenciador.notas[:]:
                if nota.pos[1]>= 600:
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
