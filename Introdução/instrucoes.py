#Todas essa instruções se encontram no primeiro vídeo do Professor Resolve da Aula 2

#Recomenda-se intalar o Python versão 3.4.0

#Download do Python:
#http://pygame.org/download.shtml

#Instalação e configuração do PyGame:
#https://www.youtube.com/watch?v=wAI0ee2d5jk


####################################################################################
#                           Instruções de comandos
####################################################################################

#importa a biblioteca do pygame
import pygame

#inicia os móduloas dessa biblioteca
pygame.init()

#seta o tamanho da janela, aqui de 600 por 400
screen = pygame.display.set_mode((600,400))

#troca a cor da janela de fundo para branco
screen.fill((255,255,255))

#atualiza a cor da janela
pygame.display.flip()
