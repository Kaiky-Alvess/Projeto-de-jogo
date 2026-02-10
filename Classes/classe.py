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
        return self.pos

    def atualizar(self):
        self.colisor = pygame.Rect(self.pos, self.tamanho)

    def colidir(self):
        if self.colisor.colliderect(240,540,40,40):
            return

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

