from constants import HEIGHT, WIDTH
import pygame
import structures.BaseStage
from sprites import button

class Stage(structures.BaseStage.BaseStage):
  def __init__(self, window):
      super(Stage, self).__init__('menu', window)
      self.y = 0
      self.x = 0
      self.window = window

  def run (self):
    button_start = button.button(100, 100, 300, 100, 'BOTÃO DAORA')

    done = False
    while not done:
      pygame.time.Clock().tick(60)
      button_start.draw(self.window)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          done = True
        if event.type == pygame.KEYDOWN:
          done = True
          return 'game'

      font = pygame.font.SysFont(None, 32)

      texto = font.render('APERTE ESPAÇO PARA INICIAR', True, (0, 0, 255))
      texto2 = font.render('MENU DAORA', True, (255, 255, 255))
      largura, altura = font.size('APERTE ESPAÇO PARA INICIAR')
      largura2, altura2 = font.size('MENU DAORA')
      self.window.blit(texto, (WIDTH / 2 - largura / 2, HEIGHT / 2 - altura/2))
      self.window.blit(texto2, (WIDTH / 2 - largura2 / 2, HEIGHT / 2 - altura/2 - 20))
      pygame.display.update()
      pygame.display.flip()