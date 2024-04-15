"""Alabarda"""
from src.weapons.base import BaseWeapon
from src.project_typing import WeaponType, WeaponRange, WeaponProficiency, WeaponHilt


class Alabarda(BaseWeapon):
    """Representação da Alabarda no Tormenta20"""
    def __init__(self):
        super().__init__()
        self.proficiency = WeaponProficiency.MARCIAL
        self.is_melee = True
        self.hilt = WeaponHilt.DUPLA
        self.name = "Alabarda"
        self.price = 10
        self.damage = "1d10"
        self.weapon_threat = "x3"
        self.range = WeaponRange.PESSOAL
        self.type = [WeaponType.PERFURACAO, WeaponType.CORTE]
        self.weight = 2
