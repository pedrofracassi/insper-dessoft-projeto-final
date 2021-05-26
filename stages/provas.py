import pygame
from constants import WIDTH, HEIGHT

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


class p(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    pr= pygame.image.load('stages/pixil-frame-0 (1).png').convert_alpha()
    provinha = pygame.transform.scale(pr, (100, 100))
    self.image = provinha
    self.rect = self.image.get_rect()
    self.rect.centerx = WIDTH
    self.rect.bottom = HEIGHT / (1.2)
    self.chao = HEIGHT / (1.2)
    self.speedx = -4

  def update (self):
    self.rect.centerx += self.speedx
    self.rect.bottom+=0
    if self.rect.centerx<=-5:
        self.rect.centerx = 600

    
    