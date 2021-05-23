import pygame
from stage import BaseStage

class Stage(BaseStage):
  def __init__(self, window, state) -> None:
      super(Stage, self).__init__('jogo', window, state)

  def run (self):
    self.window.fill((0, 10, 0))


pygame.init()
window = pygame.display.set_mode((480,600))
#Definindo a Alessandra
x = 48
y = 60
alessandr = pygame.image.load('png-teste.png').convert()
alessandra = pygame.transform.scale(alessandr, (x, y))

game = True
#Definindo a posição inicial
alessandra_x = 24
alessandra_y = 120

#Definindo a velocidade por eixo(isso depois precisa mudar de acordo com os obstaculos e boosts)
alessandra_speedx = 0.5
alessandra_speedy = 0

while game:
  pygame.time.Clock().tick(60)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game = False

  keys = pygame.key.get_pressed()

  if alessandra_y>0:
    alessandra_y = 0
  if keys[pygame.K_UP]:
    alessandra_y += 2
  
  if keys[pygame.K_LEFT]:
    alessandra_x += alessandra_speedx
  if keys[pygame.K_RIGHT]:
    alessandra_x -= alessandra_speedx 
  

 

  window.fill((0, 0, 0))
  window.blit(alessandra, (alessandra_x, alessandra_y))
  pygame.display.update()

  




    
  