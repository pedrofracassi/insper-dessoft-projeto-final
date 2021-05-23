import pygame
from stage import BaseStage

class Stage(BaseStage):
  def __init__(self, window, state) -> None:
      super(Stage, self).__init__('menu', window, state)

  def run (self):
    game = True
    while game:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          game = False
      self.window.fill((255, 0, 0))
      pygame.display.update()
      