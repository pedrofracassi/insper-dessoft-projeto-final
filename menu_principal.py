from stage import Stage

class Menu(Stage):
  def __init__(self, window) -> None:
      super(Menu, self).__init__('menu', window)

  def run (self):
    self.window.fill((255, 0, 0))