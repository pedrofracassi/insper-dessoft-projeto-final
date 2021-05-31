import pygame
from constants import WIDTH, HEIGHT

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

GRAVIDADE = 0.5

class Alessandra(pygame.sprite.Sprite):
  def __init__(self):
    super(Alessandra, self).__init__()
    Le= pygame.image.load('./assets/alessandra.png').convert_alpha()
    Ale = pygame.transform.scale(Le, (200, 300))
    self.image = Ale
    self.rect = self.image.get_rect()
    self.rect.centerx = WIDTH / 2
    self.rect.bottom = HEIGHT / (1.05)
    self.pulando = False
    self.chao = HEIGHT /(1.05)
    self.speedy = 0
    self.uphold = False

  def update (self):
    self.speedx = 0
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_SPACE] and not self.pulando and not self.uphold:
      self.uphold = True
      self.pulando = True
      self.speedy = -15

    if not keystate[pygame.K_SPACE]:
      self.uphold = False

    self.rect.y += self.speedy
    
    if self.pulando:
      self.speedy += GRAVIDADE

    if self.rect.bottom > self.chao:
      self.speedy = 0
      self.pulando = False