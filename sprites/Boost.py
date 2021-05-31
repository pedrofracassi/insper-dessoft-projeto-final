import pygame
from constants import WIDTH, HEIGHT

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)



class cafe(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    boost= pygame.image.load('assets/café.png').convert_alpha()
    provinha = pygame.transform.scale(boost, (60, 70))
    self.image = provinha
    self.rect = self.image.get_rect()
    self.rect.centerx = WIDTH
    self.rect.bottom = HEIGHT / (1.5)
    self.chao = HEIGHT / (1.2)
    self.speedx = -4

  def update (self):
    self.rect.centerx += self.speedx
    self.rect.bottom+=0
    if self.rect.centerx<=-5:
        self.rect.centerx = WIDTH*3