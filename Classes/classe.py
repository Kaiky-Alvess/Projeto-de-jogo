import pygame

class Notas():
    def __init__(self,janela,r,g,b,velocidade,pos=[],tamanho=()):
        self.r=r
        self.g=g
        self.b=b
        self.pos=pos
        self.tamanho=tamanho
        self.janela=janela
        self.velocidade= velocidade

    def criar_obj(self):
        self.nota=pygame.draw.rect(self.janela, (self.r,self.g, self.b), (self.pos,self.tamanho))
        self.colisor=pygame.Rect(self.pos,self.tamanho)

    def cair(self):
        self.pos[1]+=self.velocidade
        self.colisor = pygame.Rect(self.pos, self.tamanho)
        return self.pos

    def atualizar(self):
        if self.pos[1]>600:
            self.pos[1]=0

    def colidir(self):
        if self.colisor.colliderect(240,540,40,40):
            self.pos[1]=0
        self.colisor = pygame.Rect(self.pos, self.tamanho)

class Setas():
    def __init__(self,janela,r,g,b,pos=[],tamanho=()):
        self.r = r
        self.g = g
        self.b = b
        self.pos = pos
        self.tamanho = tamanho
        self.janela = janela
        self.colisor = pygame.Rect(self.pos, self.tamanho)
        
    def criar_obj(self):
        self.seta=pygame.draw.rect(self.janela, (self.r,self.g, self.b), (self.pos,self.tamanho))

