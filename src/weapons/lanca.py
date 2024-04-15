"""Lança"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType,WeaponRange, WeaponProficiency, WeaponHilt
class Lanca(BaseWeapon):
    """Representação da Lança no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.type = WeaponType.PERFURACAO
        self.weight = 1
        self.damage = "1d6"
        self.range = WeaponRange.CURTO
        self.weapon_threat = "x2"
        self.price = 2
        self.name = "Lança"
        self.proficiency = WeaponProficiency.SIMPLES
        self.is_melee = True
        self.hilt = WeaponHilt.SINGULAR
