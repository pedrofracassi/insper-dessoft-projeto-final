import pygame
from constants import WIDTH, HEIGHT

class Background (pygame.sprite.Sprite):
  def __init__(self, x_inicial = 0):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.transform.scale(pygame.image.load('./assets/fundo_atualizado(1).jpg').convert(), (WIDTH, HEIGHT))
    self.rect = self.image.get_rect()
    self.rect.x = x_inicial

  def update (self, speed):
    self.rect.x += speed
    if self.rect.x <= -WIDTH:
        self.rect.x = WIDTH