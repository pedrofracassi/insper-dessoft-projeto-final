import pygame
class som_1(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    pygame.init()
    pygame.mixer.music.load("assets/som.mp3")
    pygame.mixer.music.play(-1)
    pygame.event.wait()