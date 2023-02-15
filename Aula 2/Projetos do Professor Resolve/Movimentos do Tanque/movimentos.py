#Movimentando o Tanque

import pygame
import math
from pygame.locals import *
from sys import exit


def movimento(superficie,anglulo):
    move_x, move_y = pygame.mouse.get_pos()
    rel_x, rel_y = move_x - x, move_y - y
    print(rel_x, rel_y)
    anglulo = (720 / math.pi) * -math.atan2(rel_y, rel_x)
    rotated_surface = pygame.transform.movimento(superficie,int(anglulo))
    rotated_rect = rotated_surface.get_rect(center=(300,300))
    return rotated_surface,rotated_rect

#inicia os móduloas dessa biblioteca
pygame.init()

#seta o tamanho da janela
screen = pygame.display.set_mode([600,600])
tank = pygame.image.load('toptank.png')

anglulo = 0

x=0
y=0
move_x = 1
move_y = 1

while True:

    #Fecha o jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    #muda a cor da tela para branco     
    screen.fill((255,255,255))
    
    tank_rotated, tank_rotated_rect = movimento(tank,anglulo)
    screen.blit(tank_rotated,tank_rotated_rect)
    
    #atualiza a cor da janela
    pygame.display.flip()
