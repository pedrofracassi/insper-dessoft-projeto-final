from menu_principal import Menu
import pygame

pygame.init()

window = pygame.display.set_mode((600, 500))
pygame.display.set_caption('Café com a Alessandra')

game = True

stage_atual = 'menu'
stages = [
  Menu(window),
]

def get_stage(name):
  for stage in stages:
    if stage.name == name:
      return stage

while game:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game = False

  get_stage(stage_atual).run()

  pygame.display.update()

pygame.quit()