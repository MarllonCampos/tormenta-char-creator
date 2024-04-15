"""Clava"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType, WeaponRange, WeaponProficiency, WeaponHilt


class Clava(BaseWeapon):
    """Representação da Clava no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.type = WeaponType.IMPACTO
        self.weight = 1
        self.damage = "1d6"
        self.range = WeaponRange.PESSOAL
        self.weapon_threat = "x2"
        self.price = None
        self.name = "Clava"
        self.proficiency = WeaponProficiency.SIMPLES
        self.is_melee = True
        self.hilt = WeaponHilt.SINGULAR
