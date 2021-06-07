import pygame
from constants import WIDTH, HEIGHT

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

GRAVIDADE = 0.7


class Alessandra(pygame.sprite.Sprite):
  def __init__(self):
    super(Alessandra, self).__init__()
    Le= pygame.image.load('./assets/alessandra.png').convert_alpha()
    Ale = pygame.transform.scale(Le, (100, 150))
    Le2 = pygame.image.load('./assets/alessandra2.png').convert_alpha()
    Ale2 = pygame.transform.scale(Le2, (100, 150))
    Le3= pygame.image.load('./assets/alessandra3.png').convert_alpha()
    Ale3 = pygame.transform.scale(Le3, (100, 150))
    self.images = [Ale, Ale2, Ale3]
    self.tempo = [0,1,2,3,4,5]
    self.contador1 = 0
    self.contador2 = 0
    self.image = self.images[0]
    self.rect = self.image.get_rect()
    self.rect.centerx = WIDTH / 2
    self.rect.bottom = HEIGHT / (1.09)
    self.pulando = False
    self.chao = HEIGHT /(1.09)
    self.speedy = 0
    self.uphold = False

  def update (self, speed):
    if  self.contador1 in self.tempo and not self.pulando :
      self.image = self.images[0]
      self.contador1+=1
    if self.contador1 not in self.tempo and not self.pulando:
      self.image = self.images[1]
      self.contador2+=1
      if self.contador2 ==5:
        self.contador1 = 0
        self.contador2 = 0

    self.speedx = 0
    keystate = pygame.key.get_pressed()
    
    if keystate[pygame.K_SPACE] and not self.pulando and not self.uphold:
      self.uphold = True
      self.pulando = True
      self.speedy = -15

    if not keystate[pygame.K_SPACE]:
      self.uphold = False

    self.rect.bottom += self.speedy
    
    if self.pulando:
      self.speedy += GRAVIDADE
      self.image = self.images[2]

    if self.rect.bottom > self.chao:
      self.rect.bottom = self.chao
      self.speedy = 0
      self.pulando = False