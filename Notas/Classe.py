import pygame

class Notas:
    def __init__(self,janela,r,g,b,tamanho=() ):
        self.r=r
        self.g=g
        self.b=b
        self.tamanho=tamanho
        self.janela=janela
    def criar_obj(self):
        self.nota=pygame.draw.rect(self.janela, (self.r,self.g, self.b), (self.tamanho))
        self.colisor=pygame.Rect(self.tamanho)
janela=pygame.display.set_mode((800,600))
Nota_verde=Notas(janela,0,255,255,(0,0,40,40))
Nota_verde.criar_obj()

