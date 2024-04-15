"""Martelo de Guerra"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType, WeaponRange, WeaponProficiency, WeaponHilt


class MarteloGuerra(BaseWeapon):
    """Representação da Martelo de Guerra no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.proficiency = WeaponProficiency.MARCIAL
        self.is_melee = True
        self.hilt = WeaponHilt.SINGULAR
        self.name = "Martelo de Guerra"
        self.price = 12
        self.damage = "1d8"
        self.weapon_threat = "x3"
        self.range = WeaponRange.PESSOAL
        self.type = WeaponType.IMPACTO
        self.weight = 1
