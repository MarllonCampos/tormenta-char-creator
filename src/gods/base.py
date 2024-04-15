"""Classe Base para Deuses"""
from typing import List
from src.weapons import BaseWeapon
from src.project_typing import EnergiesEnum


class BaseGod:
  """Classe padrão para extender para so próximos Deuses"""
  def __init__(self) -> None:
      self.name: str = ""
      self.energy: EnergiesEnum  = None
      self.provided_powers: List = List
      self.beliefs: str = None
      self.blessed_weapons: BaseWeapon = None
      self.followers: List = List
      self.obligations_restrictions: str = None

  def __repr__(self) -> str:
    class_name = self.__class__.__name__
    return (
        f"{class_name} -> [name: {self.name}, blessed_weapons: {self.blessed_weapons}, "
        f"beliefs: {self.beliefs}, followers: {self.followers},"
        f"energy: {self.energy}, provided_powers: {self.provided_powers},"
        f"obligations_restrictions: {self.obligations_restrictions}]"
    )