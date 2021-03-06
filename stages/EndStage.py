from constants import HEIGHT, WIDTH
import pygame
import structures.BaseStage
from sprites import button
from sprites import GameOver 

class Stage(structures.BaseStage.BaseStage):
  def __init__(self, window):
      super(Stage, self).__init__('end', window)
      self.y = 0
      self.x = 0
      self.window = window

  def run (self):
    end = GameOver.GameOver()
    btn_width = 200
    btn_height = 70
    button_start = button.button(WIDTH - btn_width - 50, 50, btn_width, btn_height, 'Voltar pro Menu')
    btn_width_1 = 200
    btn_height_1 = 70
    button_start_1 = button.button(WIDTH - btn_width_1 - 50, 130, btn_width_1,btn_height_1, 'Jogar novamente ')
    sprites = pygame.sprite.Group()
    sprites.add(end)

    done = False
    while not done:
      pygame.time.Clock().tick(60)
      self.window.fill((0, 0, 0))
      sprites.draw(self.window)
      button_start.draw(self.window)
      button_start_1.draw(self.window)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          done = True
          return
        if event.type == pygame.MOUSEBUTTONDOWN and button_start.isBeingHovered():
          done = True
          return 'game'
        if event.type == pygame.MOUSEBUTTONDOWN and button_start_1.isBeingHovered():
          done = True 
          return 'restart'
      pygame.display.update()