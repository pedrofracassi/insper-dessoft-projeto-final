import pygame
from constants import WIDTH, HEIGHT

class BackgroundMenu (pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.transform.scale(pygame.image.load('./assets/menu.png').convert(), (WIDTH, HEIGHT))
    self.rect = self.image.get_rect()
    
    

    
    