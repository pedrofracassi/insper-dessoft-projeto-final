class BaseStage(object):
  def __init__(self, name: str, window):
    self.name = name
    self.window = window

  def run (self):
    self.window.fill((255, 255, 255))