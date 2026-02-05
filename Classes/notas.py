from classe import *
import pygame
import random
class Gerenciador():
    def __init__(self):
        self.notas=[]
        #self.tempo_spawn=
        #self.intervalo=
        #self.velocidade
        self.colunas={'1':240, '2':320,'3':400}
    def criar_notas(self,janela,r,g,b,velocidade,tamanho=()):
        x_escolhido=self.colunas[random.choice(['1','2','3'])]
        self.notas.append(Notas(janela,r,g,b,velocidade,[x_escolhido,0],(tamanho)))
        for i in self.notas:
            i.criar_obj()

janela=pygame.display.set_mode((800,600))
gerenciador=Gerenciador()
gerenciador.criar_notas(janela,255,255,255,1,(40,40))


while True:
    janela.fill((0,0,0))
    gerenciador.criar_notas(janela, 255, 255, 255, 1, (40, 40))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()