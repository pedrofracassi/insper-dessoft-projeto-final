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
    self.image = pygame.Surface((10, 10))
    self.image.fill(YELLOW)
    self.rect = self.image.get_rect()
    self.rect.centerx = 600
    self.rect.bottom = (HEIGHT / 2) + 45
    self.chao = HEIGHT / 2
    self.speedx = -2

  def update (self):
    self.rect.centerx += self.speedx
    self.rect.bottom+=0
    if self.rect.centerx<=-5:
        self.rect.centerx = 600

    
    