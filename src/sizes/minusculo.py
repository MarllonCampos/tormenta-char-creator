from .base import BaseSize

class Minusculo(BaseSize):
  def __init__(self) -> None:
    super().__init__()
    self.ocuppied_space = 1.5
    self.natural_reach = 1.5
    self.furtive_modifier = +5
    self.maneuver_modifier = -5