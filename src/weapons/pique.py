"""Pique"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType, WeaponRange, WeaponProficiency, WeaponHilt


class Pique(BaseWeapon):
    """Representação da Pique no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.type = WeaponType.PERFURACAO
        self.weight = 2
        self.damage = "1d8"
        self.range = WeaponRange.PESSOAL
        self.weapon_threat = "x2"
        self.price = 2
        self.name = "Pique"
        self.proficiency = WeaponProficiency.SIMPLES
        self.is_melee = True
        self.hilt = WeaponHilt.DUPLA
