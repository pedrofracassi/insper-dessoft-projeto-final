from pygame.constants import USEREVENT
from constants import HEIGHT, WIDTH
from sprites import Alessandra
from sprites import Prova
from sprites import Cone
from sprites import Boost
from structures import BaseStage
import pygame
import random

class Stage(BaseStage.BaseStage):
  def __init__(self, window) -> None:
    super(Stage, self).__init__('jogo', window)
    self.window = window
    self.speed = -5

  def run (self):
    all_sprites = pygame.sprite.Group()
    all_provas = pygame.sprite.Group()
    all_cones = pygame.sprite.Group()
    all_boosts = pygame.sprite.Group()

    # Inicializar sprites
    player = Alessandra.Alessandra()
    
    bg_img = pygame.transform.scale(pygame.image.load('./assets/background_night.jpg').convert(), (WIDTH, HEIGHT))
    bg_img2 = pygame.transform.scale(pygame.image.load('./assets/background_day.jpg').convert(), (WIDTH, HEIGHT))
    bg1 = 0
    bg2 = WIDTH

    pygame.mixer.music.load("assets/som.mp3")
    pygame.mixer.music.play(-1)
    


    all_sprites.add(player)
  
    vidas = 3
    score = 0
    turno = 0
    self.speed = -5
    
    done = False
    frame_count = 0

    min_timer = 1000
    max_timer = 1500

    pygame.time.set_timer(USEREVENT+2, random.randrange(min_timer, max_timer))

    while not done:
      pygame.time.Clock().tick(60)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          done = True

        if event.type == pygame.USEREVENT+2:
          tipo = random.randrange(0, 10)
          
          if tipo in [0, 1, 2, 3]:
            novo_obstaculo = Prova.Prova()
            all_provas.add(novo_obstaculo)

          if tipo in [4, 5, 6, 7, 8]:
            novo_obstaculo = Cone.Cone()
            all_cones.add(novo_obstaculo)

          if tipo in [9]:
            novo_obstaculo = Boost.Boost()
            all_boosts.add(novo_obstaculo)

          all_sprites.add(novo_obstaculo)

      frame_count += 1

      if frame_count == 240:
        frame_count = 0
        
        if min_timer - 300 > 0 and max_timer - 300 > 0:
          min_timer -= 300
          max_timer -= 300

        self.speed += -1

      bg1 += self.speed
      bg2 += self.speed

      if bg2 < -WIDTH:
        bg2 = bg1 + WIDTH

      if bg1 < -WIDTH:
        bg1 = bg2 + WIDTH

      all_sprites.update(self.speed)

      colisoes_prova = pygame.sprite.spritecollide(player, all_provas, True)
      colisoes_cone = pygame.sprite.spritecollide(player, all_cones, True)
      colisoes_cafe = pygame.sprite.spritecollide(player, all_boosts, True)
      
      # Diminui um de vida se colidir com um obstáculo
      if colisoes_prova or colisoes_cone:
        vidas -= 1

      # Aumenta um de vida se colidir com um café
      if colisoes_cafe:
        vidas += 1
        pygame.mixer.Channel(3).play(pygame.mixer.Sound("assets/cafe.wav"))
        pygame.mixer.music.set_volume(1)

      # VIDAS
      font = pygame.font.SysFont(None, 30)
      Vidas = font.render('Vidas: {}'.format(vidas), True, (0, 255, 0))

      # SCORE
      score+=1
      Pontos = font.render('Score: {}'.format(score), True, (0, 0, 255))

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
        pygame.mixer.music.pause()
        pygame.mixer.Channel(2).play(pygame.mixer.Sound("assets/Humberto.mp3"))


        return 'dead'