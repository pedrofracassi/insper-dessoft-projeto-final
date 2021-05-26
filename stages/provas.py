import pygame

WIDTH = 600
HEIGHT = 500

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


class p(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    pr= pygame.image.load('stages/pixil-frame-0 (1).png').convert()
    provinha = pygame.transform.scale(pr, (55, 70))
    self.image = provinha
    self.rect = self.image.get_rect()
    self.rect.centerx = 600
    self.rect.bottom = (HEIGHT / 2) + 75
    self.chao = HEIGHT / 2
    self.speedx = -2

  def update (self):
    self.rect.centerx += self.speedx
    self.rect.bottom+=0
    if self.rect.centerx<=-5:
        self.rect.centerx = 600

    
    