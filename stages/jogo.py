import pygame
from stage import BaseStage

class Stage(BaseStage):
  def __init__(self, window, state) -> None:
      super(Stage, self).__init__('jogo', window, state)

  def run (self):
    self.window.fill((0, 10, 0))

    #Definindo a Alessandra
    x = 48
    y = 60
    alessandr = pygame.image.load('referencia/png-teste.png').convert()
    alessandra = pygame.transform.scale(alessandr, (x, y))
    alessandra_x = 2
    alessandra_y = 0

    #Definindo as posições iniciais
    alessandra_x = 360
    alessandra_y = 400

    #Definindo a velocidade por eixo(isso depois precisa mudar de acordo com os obstaculos e boosts)
    alessandra_speedx = -0.1
    alessandra_speedy = 0

    #Atualizando a posição (esse dentro do for events)
    alessandra_x+=alessandra_speedx
    alessandra_y+=alessandra_speedy
    #Se ela atravessar a tela ela volta pro inicio dela
    if alessandra_x<-2:
        alessandra_x = 360

    #saída
    self.window.blit(alessandra, (alessandra_x, alessandra_y))