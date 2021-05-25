from stages.Alessandra import Alessandra
from stages.provas import p
import pygame
from stage import BaseStage

WIDTH = 600
HEIGHT = 500

class Stage(BaseStage):
  def __init__(self, window, state) -> None:
    super(Stage, self).__init__('jogo', window, state)
    self.window = window

  def run (self):
    all_sprites = pygame.sprite.Group()
    all_provas = pygame.sprite.Group()
    player = Alessandra()
    prova = p()
    all_sprites.add(prova)
    all_provas.add(prova)
    all_sprites.add(player)
    lives = 3
    score = 0
    

    done = False
    while not done:
      pygame.time.Clock().tick(60)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          done = True

    
      all_sprites.update()
      #Verifica colisões
      hits = pygame.sprite.spritecollide(player, all_provas, True)
      #Atualiza vidas
      if hits:
        lives-=1
      if lives == 0:
        done = True
      #Caso haja uma colisão o obstaculo é reposto
      for prova in hits:
        m = p()
        all_sprites.add(m)
        all_provas.add(m)

      #VIDAS
      font = pygame.font.SysFont(None, 20)
      Vidas = font.render('Vidas: {}'.format(lives), True, (0, 255, 0))
      #SCORE
      score+=1
      Pontos = font.render('Score: {}'.format(score), True, (0, 0, 255))
      


      self.window.fill((0, 0, 0))
      all_sprites.draw(self.window)
      self.window.blit(Vidas, (50, 100))
      self.window.blit(Pontos, (50, 130))

      
      pygame.display.flip()

'''
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
  
  if (alessandra_x - cone_x)<-18 and (alessandra_y-cone_y)<-10:
    lives-=1
    cone_x = 0
    cone_y = 370

  window.fill((0,0,0))
  window.blit(alessandra, (alessandra_x, alessandra_y))
  window.blit(cone,(cone_x,cone_y))
  window.blit(texto, (500, 10))
  window.blit(texto2, (500, 30))
  pygame.display.update()
'''