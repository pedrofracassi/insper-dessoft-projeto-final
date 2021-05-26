from game_state import GameState
from stages import menu, jogo
import pygame

from constants import WIDTH, HEIGHT

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Café com a Alessandra')

game = True

state = GameState()

stages = [
  menu.Stage(window, state),
  jogo.Stage(window, state)
]

def get_stage(name):
  for stage in stages:
    if stage.name == name:
      return stage

res = get_stage('menu').run()
if res == 'game':
  get_stage('jogo').run()

pygame.quit()