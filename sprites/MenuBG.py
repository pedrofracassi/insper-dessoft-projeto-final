import pygame
from constants import WIDTH, HEIGHT

class MenuBG (pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.transform.scale(pygame.image.load('./assets/menu.png').convert(), (WIDTH, HEIGHT))
    self.rect = self.image.get_rect()
    self.rect.x = 0
    self.rect.y = 0

  def update (self):
    self.rect.draw()
    return