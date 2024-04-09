"""Mangual"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType,WeaponRange, WeaponProficiency, WeaponHilt
class Mangual(BaseWeapon):
    """Representação da Mangual no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.proficiency = WeaponProficiency.MARCIAL
        self.is_melee = True
        self.hilt = WeaponHilt.SINGULAR
        self.name = "Mangual"
        self.price = 8
        self.damage = "1d8"
        self.weapon_threat = "x2"
        self.range = WeaponRange.PESSOAL
        self.type = WeaponType.IMPACTO
        self.weight = 1
