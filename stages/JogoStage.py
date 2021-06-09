from constants import HEIGHT, WIDTH
from sprites import Alessandra
from sprites import Prova
from sprites import Cone
from sprites import Boost
from sprites import Som
from structures import BaseStage
import pygame

class Stage(BaseStage.BaseStage):
  def __init__(self, window) -> None:
    super(Stage, self).__init__('jogo', window)
    self.window = window
    self.speed = -5

  def run (self):
    all_sprites = pygame.sprite.Group()
    all_provas = pygame.sprite.Group()
    all_obs = pygame.sprite.Group()
    all_boosts = pygame.sprite.Group()
    all_Som_1 = pygame.sprite.Group()
    player = Alessandra.Alessandra()
    prova = Prova.Prova()
    obstaculo = Cone.Cone()
    boost = Boost.Boost()
    som_2 = Som.som_1()
    
    bg_img = pygame.transform.scale(pygame.image.load('./assets/fundo_atualizado(1).jpg').convert(), (WIDTH, HEIGHT))
    bg_img2 = pygame.transform.scale(pygame.image.load('./assets/Background2.png').convert(), (WIDTH, HEIGHT))
    bg1 = 0
    bg2 = WIDTH

    all_sprites.add(prova)
    all_sprites.add(player)
    all_sprites.add(obstaculo)
    all_sprites.add(boost)
    all_obs.add(obstaculo)
    all_provas.add(prova)
    all_boosts.add(boost)
    all_Som_1.add(som_2)
  
    vidas = 3
    score = 0
    turno = 0
    self.speed = -5
    
    done = False
    frame_count = 0

    while not done:
      pygame.time.Clock().tick(60)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          done = True

      frame_count += 1

      if frame_count == 240:
        frame_count = 0
        self.speed += -1

      bg1 += self.speed
      bg2 += self.speed

      if bg2 < -WIDTH:
        bg2 = bg1 + WIDTH

      if bg1 < -WIDTH:
        bg1 = bg2 + WIDTH

      all_sprites.update(self.speed)

      colisoes_prova = pygame.sprite.spritecollide(player, all_provas, True)
      colisoes_cone = pygame.sprite.spritecollide(player, all_obs, True)
      colisoes_cafe = pygame.sprite.spritecollide(player, all_boosts, True)
      
      # Diminui um de vida se colidir com um obstáculo
      if colisoes_prova or colisoes_cone:
        vidas -= 1

      # Aumenta um de vida se colidir com um café
      if colisoes_cafe:
        vidas += 1

      # VIDAS
      font = pygame.font.SysFont(None, 30)
      Vidas = font.render('Vidas: {}'.format(vidas), True, (0, 255, 0))

      # SCORE
      score+=1
      Pontos = font.render('Score: {}'.format(score), True, (0, 0, 255))

      self.window.fill((0, 0, 0))
      if turno<1000:
        self.window.blit(bg_img, (bg1, 0))
        self.window.blit(bg_img, (bg2, 0))
        turno+=1
      elif turno==1000:
         turno=2000
      elif turno>1000 and turno<=2000:
        self.window.blit(bg_img2, (bg1, 0))
        self.window.blit(bg_img2, (bg2, 0))
        turno-=1
        if turno==1000:
          turno=0

      self.window.blit(Vidas, (50, 100))
      self.window.blit(Pontos, (50, 130))

      all_sprites.draw(self.window)
      pygame.display.flip()

      if vidas == 0:
        done = True
        return 'dead'