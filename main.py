from game_state import GameState
from stages import menu, jogo
import pygame

pygame.init()

window = pygame.display.set_mode((600, 500))
pygame.display.set_caption('Café com a Alessandra')

game = True

state = GameState()

stage_atual = 'menu'
stages = [
  menu.Stage(window, state),
  jogo.Stage(window, state)
]

def get_stage(name):
  for stage in stages:
    if stage.name == name:
      return stage

get_stage(stage_atual).run()

pygame.quit()