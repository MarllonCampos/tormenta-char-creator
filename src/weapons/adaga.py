"""Arma Adaga"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType, WeaponRange, WeaponProficiency, WeaponHilt


class Adaga(BaseWeapon):
    """Representação da adaga no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.type = WeaponType.PERFURACAO
        self.weight = 1
        self.damage = "1d4"
        self.range = WeaponRange.CURTO
        self.weapon_threat = 19
        self.price = 2
        self.name = "Adaga"
        self.proficiency = WeaponProficiency.SIMPLES
        self.is_melee = True
        self.hilt = WeaponHilt.LEVE
