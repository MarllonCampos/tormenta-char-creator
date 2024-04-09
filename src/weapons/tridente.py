"""Tridente"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType,WeaponRange, WeaponProficiency, WeaponHilt
class Tridente(BaseWeapon):
    """Representação da Tridente no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.proficiency = WeaponProficiency.MARCIAL
        self.is_melee = True
        self.hilt = WeaponHilt.SINGULAR
        self.name = "Tridente"
        self.price = 15
        self.damage = "1d8"
        self.weapon_threat = "x2"
        self.range = WeaponRange.CURTO
        self.type = WeaponType.PERFURACAO
        self.weight = 1
