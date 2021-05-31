from constants import WIDTH
from sprites import Alessandra
from sprites import Prova
from sprites import Cone
from sprites import Boost
from structures import BaseStage
import pygame

from sprites import Background

class Stage(BaseStage.BaseStage):
  def __init__(self, window) -> None:
    super(Stage, self).__init__('jogo', window)
    self.window = window

  def run (self):
    all_sprites = pygame.sprite.Group()
    all_provas = pygame.sprite.Group()
    all_obs = pygame.sprite.Group()
    all_boosts = pygame.sprite.Group()
    player = Alessandra.Alessandra()
    prova = Prova.Prova()
    obstaculo = Cone.Cone()
    boost = Boost.Boost()

    fundo1 = Background.Background()
    all_sprites.add(fundo1)

    fundo2 = Background.Background(WIDTH)
    all_sprites.add(fundo2)

    all_sprites.add(prova)
    all_sprites.add(player)
    all_sprites.add(obstaculo)
    all_sprites.add(boost)
    all_obs.add(obstaculo)
    all_provas.add(prova)
    all_boosts.add(boost)
    lives = 3
    score = 0
    
    done = False
    while not done:
      pygame.time.Clock().tick(60)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          done = True

      all_sprites.update()
      #Verifica colisões entre obstaculos e Alessandra
      hits = pygame.sprite.spritecollide(player, all_provas, True)
      hits2 = pygame.sprite.spritecollide(player, all_obs, True)
      hits3 = pygame.sprite.spritecollide(player, all_boosts, True)
      #Atualiza vidas
      if hits or hits2:
        lives-=1
      if hits3:
        lives+=1
      if lives == 0:
        done = True
        return 'dead'
      #Caso haja uma colisão o obstaculo é reposto
      for prova in hits:
        prova_ = Prova.Prova()
        all_sprites.add(prova_)
        all_provas.add(prova_)
      for obstaculo in hits2:
        obstaculo_ = Cone.Cone()
        all_sprites.add(obstaculo_)
        all_provas.add(obstaculo_)
      for boost in hits2:
        boost_ = Boost.Boost()
        all_sprites.add(boost_)
        all_provas.add(boost_)

      #VIDAS
      font = pygame.font.SysFont(None, 20)
      Vidas = font.render('Vidas: {}'.format(lives), True, (0, 255, 0))
      #SCORE
      score+=1
      Pontos = font.render('Score: {}'.format(score), True, (0, 0, 255))
    
      self.window.fill((0, 0, 0))
      all_sprites.draw(self.window)
      self.window.blit(Vidas, (50, 100))
      self.window.blit(Pontos, (50, 130))

      pygame.display.flip()