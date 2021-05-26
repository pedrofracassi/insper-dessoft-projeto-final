from game_state import GameState
from stages import MenuStage
from stages import JogoStage
import pygame

from constants import WIDTH, HEIGHT

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Café com a Alessandra')

game = True

state = GameState()

stages = [
  MenuStage(window, state),
  JogoStage(window, state)
]

def get_stage(name):
  for stage in stages:
    if stage.name == name:
      return stage

done = False
while not done:
  res = get_stage('menu').run()
  if res == 'game':
    res = get_stage('jogo').run()
    if res != 'dead':
      done = True

pygame.quit()