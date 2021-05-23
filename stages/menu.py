from stage import BaseStage

class Stage(BaseStage):
  def __init__(self, window) -> None:
      super(Stage, self).__init__('menu', window)

  def run (self):
    self.window.fill((255, 0, 0))