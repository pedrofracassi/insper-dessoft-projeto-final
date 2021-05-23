import pygame
from stage import BaseStage

class Stage(BaseStage):
  def __init__(self, window, state) -> None:
      super(Stage, self).__init__('jogo', window, state)

  def run (self):
    self.window.fill((0, 10, 0))


pygame.init()
window = pygame.display.set_mode((600,500))
#Definindo a Alessandra
x = 48
y = 60
alessandr = pygame.image.load('png-teste.png').convert()
alessandra = pygame.transform.scale(alessandr, (x, y))
#Definindo 
game = True
#Definindo a posição inicial
alessandra_x = 300
alessandra_y = 350
#Definindo obstáculo
c = pygame.image.load('cone.png').convert()
cone = pygame.transform.scale(c, (30, 40))
cone_x = 0
cone_y = 370
#Definindo score
i=0
score = 0
#Definindo as vidas
lives = 3

while game:
  pygame.time.Clock().tick(60)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game = False
  
  #SCORE
  font = pygame.font.SysFont(None, 20)
  texto = font.render('Score: {}'.format(score), True, (0, 0, 255))
  #Atualizando score
  i+=1
  if i==50:
    score+=10
    i=0
  #VIDAS
  font = pygame.font.SysFont(None, 20)
  texto2 = font.render('Vidas: {}'.format(lives), True, (0, 255, 0))
  #Atualizando as vidas
  '''colisão = 
  if len(colisão)>0:
    lives-=1'''
  if lives == 0:
    game = False

  #Atualizando posição do cone
  cone_x+=1
  if cone_x == 599:
    cone_x = 0
  #Atualizando posição Alesssandra
  keys = pygame.key.get_pressed()
  if alessandra_y<350:
    alessandra_y = 350
  if keys[pygame.K_UP]:
        alessandra_y -=50
  

  
  

 

  window.fill((0,0,0))
  window.blit(alessandra, (alessandra_x, alessandra_y))
  window.blit(cone,(cone_x,cone_y))
  window.blit(texto, (500, 10))
  window.blit(texto2, (500, 30))
  pygame.display.update()

  




    
  