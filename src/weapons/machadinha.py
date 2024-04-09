"""Machadinha"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType,WeaponRange, WeaponProficiency, WeaponHilt
class Machadinha(BaseWeapon):
    """Representação da Machadinha no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.type = WeaponType.CORTE
        self.weight = 1
        self.damage = "1d6"
        self.range = WeaponRange.CURTO
        self.weapon_threat = "x3"
        self.price = 6
        self.name = "Machadinha"
        self.proficiency = WeaponProficiency.MARCIAL
        self.is_melee = True
        self.hilt = WeaponHilt.LEVE
