import pygame

class button (pygame.sprite.Sprite):
  def __init__(self, x, y, width, height, text = ''):
    pygame.sprite.Sprite.__init__(self)
    
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.text = text

    self.hover_move = 10

  def draw (self, window):
    font = pygame.font.SysFont(None, 32)
    text = font.render(self.text, 1, (0, 0, 0))

    if not self.isBeingHovered():
      pygame.draw.rect(window, (0, 234, 249), (self.x, self.y, self.width, self.height), 0)
      pygame.draw.rect(window, (0, 192, 204), (self.x, self.y + self.height - self.hover_move, self.width, self.hover_move), 0)
      window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + ((self.height - self.hover_move)/2 - text.get_height()/2)))
    else:
      pygame.draw.rect(window, (0, 234, 249), (self.x, self.y + self.hover_move, self.width, self.height - self.hover_move), 0)
      window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + ((self.height - self.hover_move)/2 - text.get_height()/2 + self.hover_move)))


  def isBeingHovered (self):
    mouse_pos = pygame.mouse.get_pos()
    return mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.width and mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.height