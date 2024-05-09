"""Classe Base para Deuses"""
from typing import List
from src.weapons import BaseWeapon
from src.project_typing import EnergiesEnum
from src.races.base import BaseRace

class BaseGod:
    """Classe padrão para extender para so próximos Deuses"""
    def __init__(self) -> None:
        self.name: str = ""
        self.energy: EnergiesEnum  = None
        self.provided_powers: List = List
        self.beliefs: str = None
        self.blessed_weapons: BaseWeapon = None
        self.followers: List(BaseRace) = List # BaseClass
        self.obligations_restrictions: str = None

        self.name = __class__.__name__
        self.blessed_weapons: BaseWeapon  = None
        self.energy = EnergiesEnum.NEGATIVA
        self.provided_powers = []
        self.beliefs: str = ""
        self.followers: BaseRace  = []
        self.obligations_restrictions: str = None

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return (
            f"{class_name} -> [\nname: {self.name}, \nblessed_weapons:\n{self.blessed_weapons}, "
            f"\nbeliefs: {self.beliefs}, \nfollowers: {self.followers},"
            f"\nenergy: {self.energy}, \nprovided_powers: {self.provided_powers},"
            f"\nobligations_restrictions: {self.obligations_restrictions}\n]"
        )
