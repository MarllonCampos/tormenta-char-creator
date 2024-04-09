"""Foice"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType,WeaponRange, WeaponProficiency, WeaponHilt
class Foice(BaseWeapon):
    """Representação da foice no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.type = WeaponType.CORTE
        self.weight = 1
        self.damage = "1d6"
        self.range = WeaponRange.PESSOAL
        self.weapon_threat = "x3"
        self.price = 4
        self.name = "Foice"
        self.proficiency = WeaponProficiency.SIMPLES
        self.is_melee = True
        self.hilt = WeaponHilt.LEVE
