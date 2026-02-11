import pygame

nota_d=pygame.image.load('../Imgs/D_azul.png')
nota_d=pygame.transform.scale(nota_d,(70,70))
nota_s=pygame.image.load('../Imgs/S_amarelo.png')
nota_s=pygame.transform.scale(nota_s,(70,70))
nota_w=pygame.image.load('../Imgs/W_vermelho.png')
nota_w=pygame.transform.scale(nota_w,(70,70))
nota_a=pygame.image.load('../Imgs/A_verde.png')
nota_a=pygame.transform.scale(nota_a,(70,70))

seta_w=pygame.image.load('../Imgs/W_cinza.png')
seta_w=pygame.transform.scale(seta_w,(70,70))
seta_d=pygame.image.load('../Imgs/D_cinza.png')
seta_d=pygame.transform.scale(seta_d,(70,70))
seta_s=pygame.image.load('../Imgs/S_cinza.png')
seta_s=pygame.transform.scale(seta_s,(70,70))
seta_a=pygame.image.load('../Imgs/A_cinza.png')
seta_a=pygame.transform.scale(seta_a,(70,70))

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
        if self.pos[0] ==240:
            self.janela.blit(nota_a,(self.pos[0],self.pos[1]))
        elif self.pos[0] ==320:
            self.janela.blit(nota_w,(self.pos[0],self.pos[1]))
        elif self.pos[0] ==400:
            self.janela.blit(nota_s,(self.pos[0],self.pos[1]))
        elif self.pos[0] ==480:
            self.janela.blit(nota_d,(self.pos[0],self.pos[1]))
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
        if self.pos[0] == 240 and self.pos[1] == 540:
            self.janela.blit(seta_a, (self.pos[0], self.pos[1]))
        elif self.pos[0] == 320 and self.pos[1] == 540:
            self.janela.blit(seta_w, (self.pos[0], self.pos[1]))
        elif self.pos[0] == 400 and self.pos[1] == 540:
            self.janela.blit(seta_s, (self.pos[0], self.pos[1]))
        elif self.pos[0] == 480 and self.pos[1] == 540:
            self.janela.blit(seta_d, (self.pos[0], self.pos[1]))

