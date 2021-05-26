from game_state import GameState

class BaseStage(object):
  def __init__(self, name: str, window, state: GameState):
    self.name = name
    self.window = window
    self.state = state

  def run (self):
    self.window.fill((255, 255, 255))