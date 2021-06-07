import pygame
from constants import WIDTH, HEIGHT

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)



class Cone(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    a = pygame.image.load('assets/cone.png').convert_alpha()
    coninho = pygame.transform.scale(a, (60, 80)) 
    self.image = coninho
    self.rect = self.image.get_rect()
    self.rect.centerx = 2000
    self.rect.bottom = HEIGHT / (1.09)
    self.chao = HEIGHT / (1.09)

  def update (self, speed):
    self.rect.centerx += speed
    self.rect.bottom+=0
    if self.rect.centerx<=-5:
        self.rect.centerx = 2000