import pygame
from constants import WIDTH, HEIGHT

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)



class x(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    a = pygame.image.load('stages/cone1.png').convert_alpha()
    coninho = pygame.transform.scale(a, (60, 70)) 
    self.image = coninho
    self.rect = self.image.get_rect()
    self.rect.centerx = 2000
    self.rect.bottom = HEIGHT / (1.2)
    self.chao = HEIGHT / (1.2)
    self.speedx = -4

  def update (self):
    self.rect.centerx += self.speedx
    self.rect.bottom+=0
    if self.rect.centerx<=-5:
        self.rect.centerx = 2000