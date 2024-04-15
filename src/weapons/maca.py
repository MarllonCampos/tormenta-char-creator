"""Maça"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType,WeaponRange, WeaponProficiency, WeaponHilt
class Maca(BaseWeapon):
    """Representação da Maça no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.type = WeaponType.IMPACTO
        self.weight = 1
        self.damage = "1d8"
        self.range = WeaponRange.PESSOAL
        self.weapon_threat = "x2"
        self.price = 12
        self.name = "Maça"
        self.proficiency = WeaponProficiency.SIMPLES
        self.is_melee = True
        self.hilt = WeaponHilt.SINGULAR
