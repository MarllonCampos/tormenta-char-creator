"""Classe que descreve o deus Aharadak"""
from .base import BaseGod
from src.project_typing import EnergiesEnum
from src.weapons import CorrenteEspinhos
class Aharadak(BaseGod):
  def __init__(self) -> None:
    super().__init__()
    self.name = __class__.__name__
    self.blessed_weapons = CorrenteEspinhos()
    self.energy = EnergiesEnum.NEGATIVA
    self.provided_powers = []
    self.beliefs: str = "Reverenciar a Tormenta, apregoar a inevitabilidade de sua chegada ao mundo. Praticar a devassidão e a perversão. Deturpar tudo que é correto, desfigurar tudo que é normal. Abraçar a agonia, crueldade e loucura"
    self.followers = []
    self.obligations_restrictions: str = None

