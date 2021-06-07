from stages import MenuStage
from stages import JogoStage
from stages import EndStage
import pygame

from constants import WIDTH, HEIGHT

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Café com a Alessandra')

game = True

stages = [
  MenuStage.Stage(window),
  JogoStage.Stage(window),
  EndStage.Stage(window)
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
  if res == 'dead':
    res = get_stage('end').run()
    if res == "restart":
      res = get_stage('jogo').run()
  else:
    done = True
    
   
pygame.quit()