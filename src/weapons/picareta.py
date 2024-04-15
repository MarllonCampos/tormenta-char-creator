"""Picareta"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType,WeaponRange, WeaponProficiency, WeaponHilt
class Picareta(BaseWeapon):
    """Representação da Picareta no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.proficiency = WeaponProficiency.MARCIAL
        self.is_melee = True
        self.hilt = WeaponHilt.SINGULAR
        self.name = "Picareta"
        self.price = 8
        self.damage = "1d6"
        self.weapon_threat = "x4"
        self.range = WeaponRange.PESSOAL
        self.type = WeaponType.PERFURACAO
        self.weight = 1
