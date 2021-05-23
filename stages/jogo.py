from stage import BaseStage

class Stage(BaseStage):
  def __init__(self, window, state) -> None:
      super(Stage, self).__init__('jogo', window, state)

  def run (self):
    self.window.fill((0, 10, 0))