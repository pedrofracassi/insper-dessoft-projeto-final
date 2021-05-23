import pygame
from stage import BaseStage

class Stage(BaseStage):
  def __init__(self, window, state) -> None:
      super(Stage, self).__init__('menu', window, state)
      self.y = 0
      self.x = 0

  def run (self):
    game = True
    while game:
      pygame.time.Clock().tick(60)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          game = False

      keys = pygame.key.get_pressed()

      if keys[pygame.K_UP]:
        self.y -= 1
      if keys[pygame.K_DOWN]:
        self.y += 1
      if keys[pygame.K_LEFT]:
        self.x -= 1
      if keys[pygame.K_RIGHT]:
        self.x += 1

      self.window.fill((255, 255, 255))

      cor = (255, 0, 0)
      vertices = [(self.x, self.y), (self.x, self.y + 10), (self.x + 10, self.y), (self.x + 10, self.y + 10)]
      pygame.draw.polygon(self.window, cor, vertices)

      pygame.display.update()
