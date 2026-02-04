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
        if self.pos[1]>600:
            self.pos[1]=0

    def colidir(self):
        if self.colisor.colliderect(240,540,40,40):
            print('a')


class Setas():
    def __init__(self,janela,r,g,b,pos=[],tamanho=()):
        self.r = r
        self.g = g
        self.b = b
        self.pos = pos
        self.tamanho = tamanho
        self.janela = janela
    def criar_obj(self):
        self.seta=pygame.draw.rect(self.janela, (self.r,self.g, self.b), (self.pos,self.tamanho))

janela=pygame.display.set_mode((800,600))
Nota_verde=Notas(janela,0,255,0,1,[240,0],(40,40))
seta_verde=Setas(janela,0,255,0,[240,540],(40,40))

while True:
    janela.fill((0,0,0))
    relogio=pygame.time.Clock()
    relogio.tick(240)
    Nota_verde.criar_obj()
    seta_verde.criar_obj()
    Nota_verde.cair()
    Nota_verde.atualizar()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Nota_verde.colidir()
                Nota_verde.atualizar()
    pygame.display.update()
