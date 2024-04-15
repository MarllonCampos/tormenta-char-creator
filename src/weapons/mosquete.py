"""Mosquete"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType, WeaponRange, WeaponProficiency, WeaponHilt


class Mosquete(BaseWeapon):
    """Representação da Mosquete no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.proficiency = WeaponProficiency.FOGO
        self.is_melee = False
        self.hilt = WeaponHilt.DUPLA
        self.name = "Mosquete"
        self.price = 500
        self.damage = "2d8"
        self.weapon_threat = [19, "x3"]
        self.range = WeaponRange.MEDIO
        self.type =  WeaponType.PERFURACAO
        self.weight = 1
