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
        self.nota.colliderect()
Nota_verde=Notas('Verde', 0, 255, 0, (50, 60, 40, 40))