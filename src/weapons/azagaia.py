"""Azagaia"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType,WeaponRange, WeaponProficiency, WeaponHilt
class Azagaia(BaseWeapon):
    """Representação da Azagaia no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.type = WeaponType.PERFURACAO
        self.weight = 1
        self.damage = "1d6"
        self.range = WeaponRange.MEDIO
        self.weapon_threat = "x2"
        self.price = 1
        self.name = "Azagaia"
        self.proficiency = WeaponProficiency.SIMPLES
        self.is_melee = False
        self.hilt = WeaponHilt.SINGULAR
