from stage import Stage

class Jogo(Stage):
  def __init__(self, window) -> None:
      super(Jogo, self).__init__('jogo', window)

  def run (self):
    self.window.fill((0, 10, 0))