"""Florete"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType, WeaponRange, WeaponProficiency, WeaponHilt


class Florete(BaseWeapon):
    """Representação da Florete no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.proficiency = WeaponProficiency.MARCIAL
        self.is_melee = True
        self.hilt = WeaponHilt.SINGULAR
        self.name = "Florete"
        self.price = 20
        self.damage = "1d6"
        self.weapon_threat = 18
        self.range = WeaponRange.PESSOAL
        self.type = WeaponType.PERFURACAO
        self.weight = 1
