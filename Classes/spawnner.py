from Classes.classe import *
import pygame
import random
class Gerenciador():
    def __init__(self,janela):
        self.notas=[]
        self.colunas={'1':240, '2':320,'3':400,'4':480}
        self.janela=janela
    def spawnar_nota(self, coluna):
        self.notas.append(
            Notas(self.janela, 0, 255, 0, 5, [coluna, 0], (40, 40))
        )

    def excluir(self):
        for i in self.notas:
            if i.pos[1]> 600:
                self.notas.remove(i)


