from Classes.classe import *
import pygame
import random
class Gerenciador():
    def __init__(self):
        self.notas=[]
        self.tempo_spawn=0
        self.intervalo=240
        self.colunas={'1':240, '2':320,'3':400}
        self.x_escolhido=self.colunas[random.choice(['1','2','3'])]

    def criar_notas(self,janela,r,g,b,velocidade,tamanho=()):
        self.notas.append(Notas(janela,r,g,b,1,[self.x_escolhido,0],(tamanho)))

    def atualizar(self):
        if self.tempo_spawn>=self.intervalo:
            self.tempo_spawn = 0
            self.x_escolhido = self.colunas[random.choice(['1', '2', '3'])]
            if self.x_escolhido == 240:
                self.r = 0
                self.g = 255
                self.b = 0
            elif self.x_escolhido == 320:
                self.r = 255
                self.g = 0
                self.b = 0
            elif self.x_escolhido == 400:
                self.r = 255
                self.g = 255
                self.b = 0
            self.criar_notas(janela, self.r, self.g, self.b, 1, (40, 40))
    def excluir(self):
        for i in self.notas:
            if i.pos[1]> 600:
                self.notas.remove(i)


janela=pygame.display.set_mode((800,600))
gerenciador=Gerenciador()
gerenciador.criar_notas(janela,0,0,0,1,(40,40))